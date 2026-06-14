---
title: Coherence Audit — June 2026
description: Full coherence audit produced under the Coherence Audit Protocol, triggered by the June 13–14 2026 "meaning → game → political-economy" flurry (two new steward-anchor source digests and three new exchanges, #29/#30/#31, plus index and roadmap updates). Run as a mechanical pre-pass (scripts/coherence-check.py) plus two independent cross-lineage interpretive sub-agents (GPT-5.5 and Gemini 3.1 Pro) reconciled by the auditing agent.
provenance: "collaborative"
audit_date: 2026-06-14
audit_trigger: "Recent-activity flurry: source-weekly-show-stewart-slobodian-muskism-digest.md + source-suits-grasshopper-digest.md + source-modern-wisdom-1109-brooks-digest.md added; Exchanges #29 (principle-2-solvable-vs-perennial-boundary), #30 (demand-side-misinformation-meaning-deficit), and #31 (abundance-vs-discipline-capital-bottleneck) opened; SOURCE_INDEX.md, sources/README.md, _EXCHANGE_INDEX.md, ROADMAP.md, and several explorations/process files revised. Steward requested a full audit, explicitly authorizing parallel cross-lineage sub-agents to compare notes."
audit_scope: "project-2028 (repo-wide mechanical pre-pass; interpretive read scoped to the flurry + adjacent corpus)"
audit_method: "mechanical pre-pass + two independent cross-lineage interpretive sub-agents reconciled"
audit_status: "complete (6 items fixed this pass; ≈23 pre-existing references in 5 clusters (C1–C5) carried forward; April-2026 carried-forward items not re-litigated)"
---

# Coherence Audit — June 2026

> **Status:** Complete. This is the second full audit under the [Coherence Audit Protocol](../coherence-audit-protocol.md) (the first was [April 2026](coherence-audit-2026-04.md)). It was triggered by the June 13–14 2026 flurry: two new steward-anchor source digests (Suits *Grasshopper*, Stewart × Slobodian *Muskism*; the Brooks #1109 digest was also recent), three new exchanges (**#29**, **#30**, **#31**), and the accompanying index/roadmap updates. Per protocol §1, "a new exchange is created" and "approximately every 3–5 exchanges" both fired.
>
> **Method (steward-authorized):** A deterministic **mechanical pre-pass** ([`scripts/coherence-check.py`](../../../scripts/coherence-check.py)) was run repo-wide for link/anchor integrity and the Hallucinated-vs-Stale distinction. Then **two independent interpretive sub-agents on different model lineages** (one GPT-5.5, one Gemini 3.1 Pro), each blind to the other, ran the protocol's interpretive layer (exchange-index integrity, count/set-equality, cross-document drift, recommendation tracking, terminology) and returned coherence checklists. The auditing agent (Claude) reconciled the three outputs. The cross-lineage step earned its keep: the two interpretive agents **converged** on the high-risk mechanics being clean and **diverged** on two real findings neither would have caught alone (see [Cross-lineage reconciliation](#cross-lineage-reconciliation)).
>
> **Headline:** The high-risk recent mechanics are **clean** — #29/#30/#31 are correctly indexed with statuses matching their status blocks, the dependency graph includes them, the "57 digests" and steward-anchor counts are accurate, and the newly created Muskism digest and Exchange #31 carry **no** broken links or anchors. The substantive finding is a **drift**: when the prior session opened #29 and #30, it updated the Brooks digest's candidates table and cross-references but left **three** downstream locations still describing those exchanges as a "candidate"/"future"/"not-yet-in-corpus" idea. That drift, one flurry-introduced broken link, and one metadata gap are fixed in this pass. The mechanical pre-pass also surfaced a cluster of **pre-existing** broken links/anchors (the April audit predates this script); they are catalogued and carried forward.

---

## Document classes covered

- **Core normative documents:** [PRINCIPLES.md](../../../PRINCIPLES.md), [PROBLEM_MAP.md](../../../PROBLEM_MAP.md), [FOUNDATIONAL_COMMITMENTS.md](../../../FOUNDATIONAL_COMMITMENTS.md) — referenced as link targets; no substantive revision occurred in the flurry, so they were checked for inbound-reference accuracy only.
- **Project-authored analysis & coordination (primary scope):** `sources/**` (the three new digests + the index/README), `agent/exchanges/**` (#29/#30/#31 + the index), `agent/explorations/**` (the new riffs + the cross-linked riffs), `agent/process/**`, [ROADMAP.md](../../../ROADMAP.md).
- **Retained external source corpus:** `external-formation-docs/**` — **not touched** in the flurry; no source-handling, translation-status, or canonical-source findings in this pass. No lightweight corpus-integrity check was triggered.

---

## Coherence checklist — fixed this pass

| # | Type | Class | Artifact A | Artifact B | Issue | Resolution |
|---|---|---|---|---|---|---|
| F1 | Broken reference | Project-authored analysis (source digest) | [`source-suits-grasshopper-digest.md`](../../../sources/source-suits-grasshopper-digest.md) (interpretive notes, "Nozick guard" bullet) | [`principle-2-solvable-vs-perennial-boundary-exchange.md`](../../../agent/exchanges/principle-2-solvable-vs-perennial-boundary-exchange.md) | The `E29-C3` link pointed to `../agent/**explorations**/principle-2-…-exchange.md`; the exchange lives in `agent/**exchanges**/`. Flurry-introduced (the Suits digest is new). | **Fixed.** Corrected `explorations` → `exchanges` in the link path. |
| F2a | Drift | Project-authored analysis (source digest) | [`source-modern-wisdom-1109-brooks-digest.md`](../../../sources/source-modern-wisdom-1109-brooks-digest.md) §"Project 2028 mapping" (Cluster 4) | [`Exchange #29`](../../../agent/exchanges/principle-2-solvable-vs-perennial-boundary-exchange.md) | The Cluster-4 mapping line still called #29 "candidate input for a **future** Principle 2 adversarial exchange," although the same digest's own *Future exchange candidates* table already records it as **opened**. Internal drift. | **Fixed.** Re-worded to "the source input for the now-open Principle 2 adversarial exchange (#29) (opened June 13, 2026; Round 1 complete)." |
| F2b | Drift | Project-authored coordination (index) | [`SOURCE_INDEX.md`](../../../sources/SOURCE_INDEX.md) (Brooks anchor row + status note) | [`Exchange #29`](../../../agent/exchanges/principle-2-solvable-vs-perennial-boundary-exchange.md), [`Exchange #30`](../../../agent/exchanges/demand-side-misinformation-meaning-deficit-exchange.md) | The Brooks row still called the demand-side misinformation idea "not-yet-in-corpus" and the Principle 2 exchange a "candidate," but both opened June 13. | **Fixed.** Both phrases now link to #30 and #29 respectively as opened exchanges. **A fourth instance** — the same "candidate Principle 2 adversarial exchange" phrasing in the SOURCE_INDEX **status note** (line 8) — was found and corrected during the June-14 steward-anchor normalization pass. |
| F2c | Drift | Project-authored coordination (README) | [`sources/README.md`](../../../sources/README.md) (June 2026 additions, Brooks) | [`Exchange #29`](../../../agent/exchanges/principle-2-solvable-vs-perennial-boundary-exchange.md), [`Exchange #30`](../../../agent/exchanges/demand-side-misinformation-meaning-deficit-exchange.md) | Same stale "candidate Principle 2 adversarial exchange" phrasing. | **Fixed.** Now cites #29 and #30 as opened June 13, 2026. |
| F3 | Drift (metadata completeness) | Project-authored analysis (source digest) | [`source-modern-wisdom-1109-brooks-digest.md`](../../../sources/source-modern-wisdom-1109-brooks-digest.md) front matter | Convention across `sources/` (55 of 57 digests carry `sub_debates`) | The Brooks digest body and its SOURCE_INDEX row both state it cross-cuts Sub-debates 1, 5, and 9, but the front matter omitted the `sub_debates` field that 55/57 digests carry. | **Fixed.** Added `sub_debates: [1, 5, 9]` to match the body/index claim. (Platner's identical omission is **carried forward** — see below — because its sub-debate mapping is not as explicitly stated in-body.) |
| F4 | Broken reference (pre-existing, safe) | Project-authored coordination + analysis | [`first-practitioner-critique-ai-provenance-exchange.md`](../../../agent/exchanges/first-practitioner-critique-ai-provenance-exchange.md) L248; [`source-weekly-show-stewart-ai-future-of-work-digest.md`](../../../sources/source-weekly-show-stewart-ai-future-of-work-digest.md) L110/L393 | [`_EXCHANGE_INDEX.md`](../../../agent/exchanges/_EXCHANGE_INDEX.md); [`historical-parallel-test-protocol.md`](../../../agent/process/historical-parallel-test-protocol.md) | Two unambiguous path typos with existing targets: `../_EXCHANGE_INDEX.md` (resolved to `agent/_EXCHANGE_INDEX.md`) and `../process/…` (should be `../agent/process/…`). Pre-existing, but zero-risk and clearly correctable. | **Fixed.** Corrected both paths. |

---

## Verified clean (recorded for the audit log)

Independently confirmed by **both** interpretive lineages and spot-checked by the auditing agent:

- **Digest count.** 57 `sources/source-*-digest.md` files on disk; the "57" claim in [SOURCE_INDEX.md](../../../sources/SOURCE_INDEX.md) and [sources/README.md](../../../sources/README.md) is correct.
- **Steward-anchor counting.** Friedberg #1, Acemoglu/Autor #2, Platner #3, Brooks #4, Muskism #5; Muskism is correctly the **third** *Weekly Show* anchor. Consistent across the Muskism digest, SOURCE_INDEX, and README.
- **Exchange index integrity.** #29, #30, #31 are present as numbered entries; their index **Status** values ("Active; Round 1 complete; Rounds 2–N reserved") match their file status blocks; all three appear in the dependency graph. Set-equality holds: 31 numbered exchanges, one index file, and three intentionally non-numbered `discovery-principle-develop-leg-*` support artifacts.
- **New-artifact link health.** The [Muskism digest](../../../sources/source-weekly-show-stewart-slobodian-muskism-digest.md) and [Exchange #31](../../../agent/exchanges/abundance-vs-discipline-capital-bottleneck-exchange.md) — the two artifacts created in this chat session — produced **zero** mechanical findings.
- **Roadmap tracking.** [ROADMAP.md](../../../ROADMAP.md) tracks #29/#30/#31, the Brooks/Suits/Muskism digests, the reserved Round-2 next step, and the open Suits-"transition" steward decision.
- **Terminology.** The Suits *"a project about transition"* framing is held consistently as an **open/candidate** lens (not a ratified thesis) across the [Suits digest](../../../sources/source-suits-grasshopper-digest.md), the [constitutional-ecology riff](../../../agent/explorations/constitutional-ecology-and-coordination-architecture-riff.md) addendum, and the ROADMAP.

---

## Coherence checklist — carried forward (pre-existing; newly surfaced by the mechanical checker)

The April 2026 audit predates [`scripts/coherence-check.py`](../../../scripts/coherence-check.py); this is the first audit to run it, so the script surfaced a backlog of pre-existing link/anchor breakage **outside the flurry** — **≈23 broken references across 12 files**, grouped below into 5 clusters. **None were introduced by the recent activity**, and the two artifacts created in this session (the Muskism digest and Exchange #31) are clean. They are deferred (not silently auto-fixed) because each needs interpretive judgment or a content decision, and per [protocol §3](../coherence-audit-protocol.md#3-issue-types) a hallucinated/stale anchor must be re-evaluated against the *actual* target rather than substituted with the closest match. (An earlier draft of this audit under-counted these, having read only a `tail`-truncated checker run; the full untruncated run is recorded here.)

| # | Type | Class | Artifacts (file : line) | Issue | Suggested resolution |
|---|---|---|---|---|---|
| C1 | Broken reference (deleted file) | Coordination / process | [`agent/explorations/README.md`](../../../agent/explorations/README.md) L31; [`agent/process/research-protocol.md`](../../../agent/process/research-protocol.md) L204 | Both link to `SCRATCHPAD.md`, **intentionally deleted** in commit `6e3c6aa` ("Remove SCRATCHPAD.md to streamline project documentation"). | **Defer → cheap fix.** Remove the two dead references (or redirect to ROADMAP, where the scratchpad's planning content migrated). Editorial wording only. |
| C2 | Hallucinated reference (file never existed) | Coordination / exploration | [`agent/exchanges/_EXCHANGE_INDEX.md`](../../../agent/exchanges/_EXCHANGE_INDEX.md) L275; [`phase-3-front-door-riff.md`](../../../agent/explorations/phase-3-front-door-riff.md) L337; [`reciprocity-and-decolonial-frame-riff.md`](../../../agent/explorations/reciprocity-and-decolonial-frame-riff.md) L415 | Three links to `docs/REVIEWER_PACKAGE_PRINCIPLE_5_F1_2026_04.md`. `git log --all` shows the file **never existed** in any commit. | **Defer.** Re-evaluate substance: a planned-but-never-built reviewer package. Either build it, point to the actual artifact (e.g. [`docs/REVIEWER_PACKET_TEMPLATE.md`](../../../docs/REVIEWER_PACKET_TEMPLATE.md) or the Exchange #23 Principle-5 materials), or mark it an unbuilt deliverable. Do **not** silently substitute. |
| C3 | Hallucinated/stale anchors (one co-authoring cluster) | Process ↔ exploration ↔ exchange | [`agent/process/research-protocol.md`](../../../agent/process/research-protocol.md) L3, L13 (×2), L35, L53, L79, L237; [`constitutional-ecology-and-coordination-architecture-riff.md`](../../../agent/explorations/constitutional-ecology-and-coordination-architecture-riff.md) L15; [`coordination-architecture-reframe-exchange.md`](../../../agent/exchanges/coordination-architecture-reframe-exchange.md) L5 | ~9 anchors into the constitutional-ecology riff don't resolve. At least one is a clear **heading rename**: the riff's §11.6 is now "Adjacent coordination-architecture projects — first-pass mapping **(v2 deliverable)**" (slug `#116-adjacent-coordination-architecture-projects--first-pass-mapping-v2-deliverable`), but the citing anchors use the older "…across the diffuse sovereignty layers" wording. The §2.3/§3.5/§1.6/§2.3.3-bis and §4.2-Path-β anchors need per-heading verification. | **Defer → focused re-author.** Per [protocol §3 note](../coherence-audit-protocol.md#3-issue-types), fix the whole cluster together against the riff's *actual current* headings (the riff, research-protocol, and the #24 exchange were co-authored, so the same pass produced all of them). The §11.6 target is unambiguous; the others require reading each current heading. |
| C4 | Stale / hallucinated `ROADMAP.md` anchors | Coordination / doctrine / exchange | [`ROADMAP.md`](../../../ROADMAP.md) L15 (`#thread-c-…`), L228 (`#riff--constitutional-ecology-…`); [`agent/doctrine/_DOCTRINE_INDEX.md`](../../../agent/doctrine/_DOCTRINE_INDEX.md) L7, L52 (×2) (`#high-priority`); [`first-practitioner-critique-ai-provenance-exchange.md`](../../../agent/exchanges/first-practitioner-critique-ai-provenance-exchange.md) L7 (`#recommendation-2-…`); [`docs/REVIEWER_PACKET_TEMPLATE.md`](../../../docs/REVIEWER_PACKET_TEMPLATE.md) L286 (`#medium-priority`) | Seven references to ROADMAP headings that have been renamed/restructured/archived. Two are unambiguous (`#high-priority` → `#high-priority-unblocks-multiple-workstreams`; `#medium-priority` → `#medium-priority-advance-when-bandwidth-allows`); the `#thread-c-…`, `#riff-…`, and `#recommendation-2-…` targets were archived to [ROADMAP_ARCHIVE.md](../../../ROADMAP_ARCHIVE.md) and need substance re-evaluation. | **Defer.** Fix the two unambiguous slugs; for the archived-section anchors, re-point at the ROADMAP_ARCHIVE.md target (or remove) after confirming substance. |
| C5 | Hallucinated self-anchors (section never created) | Exchange / coordination | [`ownership-taxonomy-systems-framework-exchange.md`](../../../agent/exchanges/ownership-taxonomy-systems-framework-exchange.md) L71 (`#round-3--reserved-response--taxonomy-v3`); [`agent/exchanges/_EXCHANGE_INDEX.md`](../../../agent/exchanges/_EXCHANGE_INDEX.md) L210 (`#16-starting-proposal-comparative-review`) | Two intra-file forward-references to sections that were never written: the ownership taxonomy was **falsified** before its reserved Round 3 materialized, and the index's `#16-starting-proposal-comparative-review` heading does not exist. | **Defer.** Re-point to the actual superseding section or remove the forward-reference, noting the falsification/rename. Do not invent the section. |

---

## Cross-lineage reconciliation

The steward authorized parallel sub-agents to "compare notes." Outcome:

- **Convergence (high confidence):** Both the GPT-5.5 and Gemini 3.1 Pro agents independently verified the 57-digest count, the steward-anchor counting, the #29/#30/#31 index entries and status-block agreement, the dependency-graph inclusion, and the exchange set-equality. Independent agreement across lineages is the strongest signal that the recent mechanics are sound.
- **Convergence (a real finding):** Both flagged that the Brooks digest is *described* as cross-cutting sub-debates but is not represented the way the convention would suggest. Reconciliation refined this: the digest's own body claims Sub-debates **1 and 5** (the index adds **9**), and the substantive issue was the **missing `sub_debates` front matter** plus an open **categorization-convention** question (do steward-anchor digests belong in the per-sub-debate tables, or only in the cross-cutting anchor table?). Fixed the metadata (F3); logged the convention question as a steward decision (below).
- **Divergence — GPT-5.5 only:** Caught the stale "candidate / not-yet-in-corpus" status language for #29/#30 across the Brooks digest, SOURCE_INDEX, and README (finding **F2**). This is the audit's headline substantive finding and would have been missed by the other lineage. Confirmed against the files and fixed.
- **Divergence — Gemini 3.1 Pro only:** Caught the missing `sub_debates` front matter (folded into **F3**) and raised whether the **Round-3 (external-human) reviewer** needs of #29/#30/#31 should be consolidated under [ROADMAP TODO #11](../../../ROADMAP.md) (the human-reviewer recruitment workstream). Reconciliation: **Accept/Defer** — Round 3 is correctly **gated behind** the agent-runnable Round 2, which has not yet been run; consolidating into TODO #11 now would be premature (the same logic the [April audit](coherence-audit-2026-04.md) applied to deferring the Platner digest into the dependency graph). Revisit when any of the three Round 2 passes completes.

A single-lineage audit would have caught one of F2/F3 but likely not both. The compare-notes step is recorded here as evidence the method adds value for this corpus.

---

## Steward decisions (resolved June 14, 2026)

1. **Steward-anchor categorization convention → "Normalize" (executed June 14).** The steward chose to **dual-list all five anchors** in their per-sub-debate tables (the Muskism precedent). Acemoglu/Autor (Sub-debates 3, 4, 6, 7, 8), Platner (3, 8), and Muskism (3, 4, 8) were already dual-listed; this pass added **Friedberg** to Sub-debates 1, 2, 3, 4, 5 (one dedicated cluster each) and **Brooks** to Sub-debates 1, 5, 9 (the last as a *cautionary* scientism cross-listing, with the §9 intro reworded from "single digest"). While normalizing, a fourth instance of the F2 stale-"candidate" drift was found in the SOURCE_INDEX status note and fixed (see F2b).
2. **Round-3 human-reviewer tracking for #29/#30/#31 → accepted the deferral (June 14).** The steward accepted that Round 3 stays gated behind the agent-runnable Round 2 and is **not** consolidated into ROADMAP TODO #11 now; revisit when any of the three Round 2 passes runs.

---

## Carried forward from the April 2026 audit (not re-litigated)

- **P2-2 — PRINCIPLES.md §5 ↔ FOUNDATIONAL_COMMITMENTS.md §5 drift:** tracked to close when [Exchange #23](../../exchanges/principle-5-revision-exchange.md) Round 5 lands the v3 §5 text into both documents at one commit. Not revisited in this pass.
- **Alignment-memo deeper corpus-integrity check** (`formation-docs/analysis/**` vs retained `external-formation-docs` excerpts): still deferred to its own cadence; no `external-formation-docs` change triggered it.
- **Filename typo `iniital-systems-framework-review.md`** (Exchange #2): accepted; rename only as part of a broader URL-cleanup pass.

---

## Resolution summary

- **Fixed this pass (6):** F1 (Suits broken link, flurry), F2a/F2b/F2c (Brooks→#29/#30 stale-status drift across three artifacts), F3 (Brooks `sub_debates` metadata), F4 (two safe pre-existing path typos).
- **Carried forward (pre-existing, deferred with precise resolutions): ≈23 references in 5 clusters (C1–C5)** — a deleted `SCRATCHPAD.md`, a never-created reviewer package, an anchor cluster from the research-protocol / constitutional-ecology / #24-exchange co-authoring pass, a set of renamed/archived `ROADMAP.md` anchors, and two never-written-section self-anchors.
- **Carried forward from April:** 3 items, unchanged.

The mechanical checker still exits non-zero (the C1–C5 pre-existing breakages remain). That is expected; closing C1–C5 is a recommended focused follow-up, ideally before the checker is wired into CI as a pre-commit gate. Note these are entirely **pre-existing** — the recent flurry introduced exactly one broken link (F1), now fixed.

---

## Next-audit trigger conditions

Per [Coherence Audit Protocol §1](../coherence-audit-protocol.md#1-trigger):

- Any Round 2 of #29/#30/#31 completes (changes their status and may spawn adopt-targets).
- The C1–C5 carried-forward clusters are cleaned up (re-run the checker to confirm a clean exit).
- A core normative document is substantively revised, or [Exchange #23](../../exchanges/principle-5-revision-exchange.md) lands the §5 v3 text (closes April P2-2).
- Approximately 3–5 further exchanges complete.
- A lightweight corpus-integrity check should run after any change to `external-formation-docs` or `formation-docs/analysis/`.
