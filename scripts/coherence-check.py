#!/usr/bin/env python3
"""coherence-check.py — mechanical link/anchor validator for the markdown corpus.

This implements the **Layer-A (mechanical detection)** slice of the
[Coherence Audit Protocol](../agent/process/coherence-audit-protocol.md). It
resolves every intra-repo Markdown link and heading anchor across the repo and,
for each broken anchor, uses git history to classify it the way the April 2026
audit did by hand:

  - **Broken reference**   — the link target file does not exist.
  - **Hallucinated reference** — the anchor never existed in *any* commit of the
    target file (per Coherence Audit Protocol §3, the dominant failure mode of
    agent-authored citations).
  - **Stale reference**    — the anchor existed in a past commit of the target
    but the heading has since been renamed/removed (classic drift).

It is **read-only**: it never modifies any file (the repo bans markdown
formatters; this tool respects that). It has **zero third-party dependencies**
(Python 3.8+ stdlib only), matching the markdown-only, tooling-light ethos.

What it does NOT do (Layer B — human/agent judgment, or future expansion):
semantic drift, terminological inconsistency, interpretive overreach,
recommendation tracking, index/registry set-equality, front-matter validation,
or cross-repo URL checks. It feeds the protocol; it does not replace it.

The slug algorithm emulates GitHub (github-slugger): lowercase, delete the
disallowed Unicode set (em/en dashes, smart quotes, parentheses, punctuation),
replace each remaining space with "-" with NO run-collapsing, and disambiguate
duplicate headings with "-1", "-2", ... suffixes.

Usage:
  scripts/coherence-check.py                 # human-readable report; exit 1 if findings
  scripts/coherence-check.py --checklist     # emit a Coherence Audit checklist table
  scripts/coherence-check.py --json          # machine-readable findings
  scripts/coherence-check.py --no-history     # skip git hallucinated/stale classification
  scripts/coherence-check.py --max-history N # cap commits scanned per target (0 = all)
  scripts/coherence-check.py --root PATH     # repo root (default: parent of scripts/)
  scripts/coherence-check.py --exit-zero     # always exit 0 (report only)
  scripts/coherence-check.py --self-test     # run built-in unit tests
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Set, Tuple

# --- Markdown structural patterns -------------------------------------------

_ATX_RE = re.compile(r"^[ ]{0,3}(#{1,6})[ \t]+(.*)$")
_FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")
_CLOSE_ATX_RE = re.compile(r"[ \t]+#+[ \t]*$")
_INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
# [text](dest "title")  /  [text](<dest>)  — dest captured, optional title dropped.
_INLINE_LINK_RE = re.compile(
    r"\]\([ \t]*(<[^>]*>|[^)\s]+)(?:[ \t]+(?:\"[^\"]*\"|'[^']*'))?[ \t]*\)"
)
# Reduce links/images inside heading text to their visible text before slugging.
_MD_LINK_TEXT_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
_MD_REFLINK_TEXT_RE = re.compile(r"!?\[([^\]]*)\]\[[^\]]*\]")
_MD_AUTOLINK_RE = re.compile(r"<([^>\s]+)>")
_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")

_CORE_NORMATIVE = {
    "PRINCIPLES.md",
    "PROBLEM_MAP.md",
    "SYSTEMS_FRAMEWORK.md",
    "CONTRIBUTING.md",
    "FOUNDATIONAL_COMMITMENTS.md",
}
# `.cursor/` holds ephemeral Cursor plans/skills that use repo-root-relative
# paths and fall outside the Coherence Audit Protocol's scope, so it is skipped.
_SKIP_DIRS = {".git", ".cursor", "node_modules", ".next", ".venv", "__pycache__"}


# --- GitHub-compatible slugging ---------------------------------------------


def _keep_char(ch: str) -> bool:
    """True if GitHub keeps this char in a slug (letters, numbers, combining
    marks, ASCII hyphen, underscore). Spaces are handled separately."""
    return ch.isalnum() or ch in "-_" or unicodedata.combining(ch) != 0


def slugify(text: str) -> str:
    """Base slug for a single heading's plain text, matching github-slugger's
    `slug()` (no duplicate tracking)."""
    text = text.lower()
    out: List[str] = []
    for ch in text:
        if ch == " ":
            out.append(" ")
        elif _keep_char(ch):
            out.append(ch)
        # everything else is dropped
    return "".join(out).replace(" ", "-")


class Slugger:
    """Stateful slugger replicating github-slugger's duplicate disambiguation."""

    def __init__(self) -> None:
        self.occ: Dict[str, int] = {}

    def slug(self, value: str) -> str:
        result = slugify(value)
        base = result
        while result in self.occ:
            self.occ[base] += 1
            result = f"{base}-{self.occ[base]}"
        self.occ[result] = 0
        return result


def normalize_heading_text(text: str) -> str:
    """Strip trailing ATX hashes and reduce inline links/images to visible text."""
    text = _CLOSE_ATX_RE.sub("", text).strip()
    text = _MD_LINK_TEXT_RE.sub(r"\1", text)
    text = _MD_REFLINK_TEXT_RE.sub(r"\1", text)
    text = _MD_AUTOLINK_RE.sub(r"\1", text)
    return text


# --- Line classification (skip fenced code + YAML front matter) -------------


def skip_mask(lines: List[str]) -> List[bool]:
    """Mark lines that are YAML front matter or inside fenced code blocks."""
    skip = [False] * len(lines)
    in_fence = False
    fence_char: Optional[str] = None
    in_front_matter = False
    for i, raw in enumerate(lines):
        s = raw.strip()
        if i == 0 and s == "---":
            in_front_matter = True
            skip[i] = True
            continue
        if in_front_matter:
            skip[i] = True
            if s in ("---", "..."):
                in_front_matter = False
            continue
        m = _FENCE_RE.match(raw)
        if m:
            ch = m.group(1)[0]
            skip[i] = True
            if not in_fence:
                in_fence = True
                fence_char = ch
            elif ch == fence_char:
                in_fence = False
                fence_char = None
            continue
        if in_fence:
            skip[i] = True
    return skip


def file_slugs(lines: List[str]) -> Set[str]:
    """All heading anchor slugs for a file, in github-slugger semantics."""
    slugger = Slugger()
    skip = skip_mask(lines)
    slugs: Set[str] = set()
    for i, raw in enumerate(lines):
        if skip[i]:
            continue
        m = _ATX_RE.match(raw)
        if m:
            slugs.add(slugger.slug(normalize_heading_text(m.group(2))))
    return slugs


def extract_links(lines: List[str]) -> List[Tuple[int, str]]:
    """Yield (1-based line number, raw destination) for inline links, skipping
    fenced code, front matter, and inline code spans."""
    skip = skip_mask(lines)
    out: List[Tuple[int, str]] = []
    for i, raw in enumerate(lines):
        if skip[i]:
            continue
        scrubbed = _INLINE_CODE_RE.sub("", raw)
        for m in _INLINE_LINK_RE.finditer(scrubbed):
            dest = m.group(1).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            if dest:
                out.append((i + 1, dest))
    return out


# --- Findings ----------------------------------------------------------------


@dataclass
class Finding:
    kind: str  # "missing-file" | "broken-anchor"
    src: str  # repo-relative path of the citing file
    line: int
    dest: str  # raw link destination
    target: str  # repo-relative path of the resolved target (best effort)
    fragment: Optional[str] = None
    classification: str = ""  # for broken-anchor: Hallucinated/Stale/Unverified
    repro: str = ""

    @property
    def issue_type(self) -> str:
        if self.kind == "missing-file":
            return "Broken reference"
        if self.classification == "Hallucinated reference":
            return "Hallucinated reference"
        return "Broken reference"


def artifact_class(relpath: str) -> str:
    if os.path.basename(relpath) in _CORE_NORMATIVE:
        return "Core normative document"
    return "Project-authored analysis"


def _relto(path: str, root: str) -> str:
    try:
        return os.path.relpath(path, root)
    except ValueError:
        return path


def analyze_link(
    src_abs: str,
    line: int,
    dest: str,
    root: str,
    slugs_for: Callable[[str], Optional[Set[str]]],
) -> Optional[Finding]:
    """Resolve one link; return a Finding if it is broken, else None.

    `slugs_for(target_abs)` returns the slug set for a .md target, or None if the
    target is not a parseable markdown file."""
    if dest.startswith("#"):
        path_part, frag = "", dest[1:]
    elif "#" in dest:
        path_part, frag = dest.split("#", 1)
    else:
        path_part, frag = dest, None

    # External links (http:, https:, mailto:, tel:, ...) are out of scope here.
    if path_part and _SCHEME_RE.match(path_part):
        return None

    if path_part == "":
        target_abs = src_abs
    else:
        from urllib.parse import unquote

        target_abs = os.path.normpath(
            os.path.join(os.path.dirname(src_abs), unquote(path_part))
        )

    if not os.path.exists(target_abs):
        return Finding(
            kind="missing-file",
            src=_relto(src_abs, root),
            line=line,
            dest=dest,
            target=_relto(target_abs, root),
        )

    if frag:
        from urllib.parse import unquote

        frag_norm = unquote(frag).lower()
        slugs = slugs_for(target_abs)
        if slugs is None:
            return None  # non-markdown target: anchors not computable
        if frag_norm not in slugs:
            return Finding(
                kind="broken-anchor",
                src=_relto(src_abs, root),
                line=line,
                dest=dest,
                target=_relto(target_abs, root),
                fragment=frag_norm,
            )
    return None


# --- git history classification ---------------------------------------------


def _git(root: str, args: List[str]) -> Optional[str]:
    try:
        proc = subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout


def historical_slugs(
    target_abs: str,
    root: str,
    cache: Dict[str, Optional[Set[str]]],
    max_history: int,
) -> Optional[Set[str]]:
    """Union of all heading slugs that ever existed in the target across git
    history. Returns None if the file is untracked (cannot be classified)."""
    if target_abs in cache:
        return cache[target_abs]
    relpath = _relto(target_abs, root).replace(os.sep, "/")
    log = _git(root, ["log", "--format=%H", "--", relpath])
    if not log or not log.strip():
        # Distinguish untracked-but-existing from no-history.
        tracked = _git(root, ["ls-files", "--error-unmatch", relpath])
        cache[target_abs] = None if tracked is None else set()
        return cache[target_abs]
    shas = [s for s in log.splitlines() if s.strip()]
    if max_history and max_history > 0:
        shas = shas[:max_history]
    all_slugs: Set[str] = set()
    for sha in shas:
        content = _git(root, ["show", f"{sha}:{relpath}"])
        if content is None:
            continue
        all_slugs |= file_slugs(content.splitlines())
    cache[target_abs] = all_slugs
    return all_slugs


def _repro_cmd(fragment: str, target_rel: str) -> str:
    phrase = re.sub(r"^\d+-", "", fragment).replace("-", " ").strip()
    rel = target_rel.replace(os.sep, "/")
    return f"git log --oneline -S {shlex.quote(phrase)} -- {rel}"


def classify_anchor_findings(
    findings: List[Finding], root: str, max_history: int
) -> None:
    """Annotate broken-anchor findings with Hallucinated/Stale/Unverified using
    git history. Mutates findings in place."""
    cache: Dict[str, Optional[Set[str]]] = {}
    for f in findings:
        if f.kind != "broken-anchor" or not f.fragment:
            continue
        target_abs = os.path.normpath(os.path.join(root, f.target))
        hist = historical_slugs(target_abs, root, cache, max_history)
        f.repro = _repro_cmd(f.fragment, f.target)
        if hist is None:
            f.classification = "Unverified (target not tracked in git)"
        elif f.fragment in hist:
            f.classification = "Stale reference (existed in a past commit)"
        else:
            f.classification = "Hallucinated reference"


# --- Scanning ----------------------------------------------------------------


def iter_markdown_files(root: str) -> List[str]:
    found: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                found.append(os.path.join(dirpath, name))
    return sorted(found)


def read_lines(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read().splitlines()


def scan(root: str, with_history: bool, max_history: int) -> Tuple[List[Finding], dict]:
    root = os.path.abspath(root)
    md_files = iter_markdown_files(root)
    slug_cache: Dict[str, Optional[Set[str]]] = {}

    def slugs_for(target_abs: str) -> Optional[Set[str]]:
        if not target_abs.endswith(".md"):
            return None
        if target_abs not in slug_cache:
            try:
                slug_cache[target_abs] = file_slugs(read_lines(target_abs))
            except (OSError, UnicodeDecodeError):
                slug_cache[target_abs] = None
        return slug_cache[target_abs]

    findings: List[Finding] = []
    links_checked = 0
    anchors_checked = 0
    for src in md_files:
        try:
            lines = read_lines(src)
        except (OSError, UnicodeDecodeError):
            continue
        for line, dest in extract_links(lines):
            path_part = dest.split("#", 1)[0]
            if path_part and _SCHEME_RE.match(path_part):
                continue
            links_checked += 1
            if "#" in dest:
                anchors_checked += 1
            finding = analyze_link(src, line, dest, root, slugs_for)
            if finding is not None:
                findings.append(finding)

    if with_history:
        classify_anchor_findings(findings, root, max_history)

    stats = {
        "files_scanned": len(md_files),
        "links_checked": links_checked,
        "anchors_checked": anchors_checked,
        "findings": len(findings),
    }
    return findings, stats


# --- Reporting ---------------------------------------------------------------


def report_text(findings: List[Finding], stats: dict) -> str:
    lines: List[str] = []
    lines.append("Coherence check — link & anchor integrity (Layer A)")
    lines.append(
        f"  files scanned: {stats['files_scanned']}   "
        f"intra-repo links: {stats['links_checked']}   "
        f"anchors: {stats['anchors_checked']}   "
        f"findings: {stats['findings']}"
    )
    lines.append("")
    if not findings:
        lines.append("OK — every intra-repo link and heading anchor resolves.")
        return "\n".join(lines)

    by_src: Dict[str, List[Finding]] = {}
    for f in findings:
        by_src.setdefault(f.src, []).append(f)

    for src in sorted(by_src):
        lines.append(src)
        for f in sorted(by_src[src], key=lambda x: x.line):
            if f.kind == "missing-file":
                lines.append(
                    f"  L{f.line}: BROKEN FILE  -> {f.dest}"
                    f"  (target not found: {f.target})"
                )
            else:
                label = f.classification or "broken anchor"
                lines.append(f"  L{f.line}: {label.upper()}  -> {f.dest}")
                lines.append(f"           target: {f.target}#{f.fragment}")
                if f.repro:
                    lines.append(f"           verify: {f.repro}")
        lines.append("")
    return "\n".join(lines).rstrip()


def report_checklist(findings: List[Finding], root: str) -> str:
    """Emit pre-filled Coherence Audit checklist rows (protocol §5 format)."""
    header = (
        "| # | Type | Class | Artifact A | Artifact B | Issue | "
        "Suggested resolution |\n"
        "| --- | --- | --- | --- | --- | --- | --- |"
    )
    rows: List[str] = [header]
    for n, f in enumerate(findings, start=1):
        cls = artifact_class(f.src)
        if f.kind == "missing-file":
            issue = (
                f"Link `{f.dest}` resolves to `{f.target}`, which does not exist "
                f"on disk."
            )
            resolution = "Update the link to the correct path, or remove it."
            type_ = "Broken reference"
        elif f.classification.startswith("Hallucinated"):
            issue = (
                f"Anchor `#{f.fragment}` in `{f.dest}` has never existed in any "
                f"commit of `{f.target}`."
            )
            resolution = (
                "Re-author the citing text against the target's actual current "
                "headings. Do NOT silently swap to the closest anchor — confirm "
                "the cited substance maps to the real section (protocol §3 note)."
            )
            type_ = "Hallucinated reference"
        elif f.classification.startswith("Stale"):
            issue = (
                f"Anchor `#{f.fragment}` existed in a past commit of `{f.target}` "
                f"but the heading was renamed/removed."
            )
            resolution = (
                "Update the link to the current heading slug and confirm the "
                "surrounding prose still matches the renamed section."
            )
            type_ = "Broken reference"
        else:
            issue = (
                f"Anchor `#{f.fragment}` in `{f.dest}` does not resolve "
                f"({f.classification})."
            )
            resolution = "Verify the target file's git status, then re-check."
            type_ = "Broken reference"
        rows.append(
            f"| {n} | {type_} | {cls} | `{f.src}` (L{f.line}) | "
            f"`{f.target}` | {issue} | {resolution} |"
        )
    return "\n".join(rows)


def report_json(findings: List[Finding], stats: dict) -> str:
    payload = {
        "stats": stats,
        "findings": [
            {
                "type": f.issue_type,
                "kind": f.kind,
                "src": f.src,
                "line": f.line,
                "dest": f.dest,
                "target": f.target,
                "fragment": f.fragment,
                "classification": f.classification,
                "verify": f.repro,
            }
            for f in findings
        ],
    }
    return json.dumps(payload, indent=2)


# --- Self-test ---------------------------------------------------------------


def _slug_heading(text: str) -> str:
    """Convenience: normalize + slug a single heading's text-after-marker."""
    return Slugger().slug(normalize_heading_text(text))


def self_test() -> int:
    failures: List[str] = []

    def check(name: str, got, want) -> None:
        if got != want:
            failures.append(f"{name}: got {got!r}, want {want!r}")

    # Real anchors from the corpus (ground truth).
    check(
        "principle-4",
        _slug_heading("4. Power must remain accountable, legible, and reversible"),
        "4-power-must-remain-accountable-legible-and-reversible",
    )
    check(
        "principle-5-internal-hyphen",
        _slug_heading("5. Critical systems require public-interest governance"),
        "5-critical-systems-require-public-interest-governance",
    )
    check(
        "em-dash-no-collapse-parens",
        _slug_heading("Deliverable 1 — revised Principle 5 text (v2)"),
        "deliverable-1--revised-principle-5-text-v2",
    )
    check(
        "heading-with-link-and-em-dash",
        _slug_heading(
            "1. [Problem Map Review — Priority Follow-Up](initial-problem-map-review.md)"
        ),
        "1-problem-map-review--priority-follow-up",
    )
    check(
        "vs-dot-and-parens-commas",
        _slug_heading(
            "Self-determination vs. substantive commitments "
            "(Principle 13 vs. Principles 2, 8, 11, 12, 15)"
        ),
        "self-determination-vs-substantive-commitments-principle-13-vs-principles-2-8-11-12-15",
    )
    check("plain", _slug_heading("Philosophical positioning"), "philosophical-positioning")
    check("backticks-dropped", _slug_heading("`code` and stuff"), "code-and-stuff")
    check("closing-atx", _slug_heading("Heading ##"), "heading")
    # Slash and dot join with no separating space; trailing punctuation trimmed.
    check(
        "punct-joins",
        _slug_heading('Read "it" and Weep: A/B 3.5!'),
        "read-it-and-weep-ab-35",
    )

    # Duplicate disambiguation (github-slugger semantics).
    s = Slugger()
    check("dup-0", s.slug("Round 1"), "round-1")
    check("dup-1", s.slug("Round 1"), "round-1-1")
    check("dup-2", s.slug("Round 1"), "round-1-2")

    # Heading extraction skips fenced code and front matter.
    doc = [
        "---",
        "title: x",
        "## not a heading: in front matter",
        "---",
        "# Real Heading",
        "```",
        "## Fake Heading In Code",
        "```",
        "    # Indented code, not a heading",
        "## Second Real",
    ]
    check("file-slugs", file_slugs(doc), {"real-heading", "second-real"})

    # Link extraction skips code; captures path and anchor links; strips <>.
    ldoc = [
        "See [a](foo.md) and [b](bar.md#sec).",
        "`[notalink](x.md)` inline code is ignored.",
        "```",
        "[alsoignored](y.md)",
        "```",
        "Auto [c](<spaced name.md>) and [ext](https://example.com).",
    ]
    links = extract_links(ldoc)
    dests = {d for _, d in links}
    check("links-present", {"foo.md", "bar.md#sec"} <= dests, True)
    check("links-code-skipped", "x.md" not in dests and "y.md" not in dests, True)
    check("links-angle-stripped", "spaced name.md" in dests, True)
    check("links-external-present", "https://example.com" in dests, True)

    # analyze_link: external skipped, missing file flagged, anchor resolution.
    def stub_slugs(target_abs: str):
        return {"known-anchor"} if target_abs.endswith("exists.md") else None

    here = os.path.abspath(".")
    ext = analyze_link(
        os.path.join(here, "a.md"), 1, "https://x.com#y", here, stub_slugs
    )
    check("analyze-external", ext, None)
    miss = analyze_link(
        os.path.join(here, "a.md"), 2, "nope-missing-file.md", here, stub_slugs
    )
    check("analyze-missing", miss.kind if miss else None, "missing-file")

    if failures:
        print("SELF-TEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"SELF-TEST PASSED ({'all checks green'})")
    return 0


# --- CLI ---------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    default_root = str(Path(__file__).resolve().parent.parent)
    parser = argparse.ArgumentParser(
        description="Mechanical link & anchor validator (Coherence Audit, Layer A)."
    )
    parser.add_argument("--root", default=default_root, help="Repo root to scan.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument(
        "--checklist", action="store_true", help="Emit a coherence-checklist table."
    )
    parser.add_argument(
        "--no-history",
        action="store_true",
        help="Skip git hallucinated/stale classification.",
    )
    parser.add_argument(
        "--max-history",
        type=int,
        default=0,
        help="Max commits scanned per target (0 = all).",
    )
    parser.add_argument(
        "--exit-zero", action="store_true", help="Always exit 0 (report only)."
    )
    parser.add_argument(
        "--self-test", action="store_true", help="Run built-in unit tests and exit."
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    findings, stats = scan(
        root=args.root,
        with_history=not args.no_history,
        max_history=args.max_history,
    )

    if args.json:
        print(report_json(findings, stats))
    elif args.checklist:
        if findings:
            print(report_checklist(findings, args.root))
        else:
            print("<!-- coherence-check: no broken links or anchors found -->")
    else:
        print(report_text(findings, stats))

    if args.exit_zero:
        return 0
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
