---
description: Source digests — curated reference documents for external source material that informs project analysis.
provenance: "collaborative"
---

# Sources

This directory contains **source digests**: curated reference documents that capture, organize, and contextualize external source material relevant to Project 2028's analysis.

Source digests are **not exchanges**. They do not contain structured agent-steward discussion. They are permanent reference artifacts — analogous to retained formation documents in `external-formation-docs`, but for media, interviews, commentary, and other non-formation-document source material.

## Purpose

The project frequently encounters external analysis, commentary, and argument that intersects with its domains. Some of this material is rich enough to warrant systematic capture: the claims, the evidence cited, the rhetorical structure, and what independent sources say about the underlying assertions.

Source digests serve three functions:

1. **Preservation.** Ensure that the full thematic content of a source is captured in a structured form, so that future exchanges can reference specific claims without losing context.
2. **Research context.** Provide additional sourcing and context for factual claims made in the source, so exchanges can build on a richer evidence base.
3. **Dependency bridging.** Allow multiple exchanges to reference the same source material without duplicating it, and without forcing a single exchange to cover every theme the source raises.

## Relationship to exchanges

Exchanges in `agent/exchanges/` reference source digests the same way they reference core documents or formation-document analysis. A source digest may spawn multiple exchanges, each focused on a different thematic cluster.

## File naming convention

Source digest files use lowercase kebab-case with the format: `source-[short-identifier]-digest.md`

Example: `source-modern-wisdom-1084-friedberg-digest.md`

## Master index

As the corpus grows, browse the [Source Index](SOURCE_INDEX.md) to find digests grouped by sub-debate and viewpoint. The index tracks all digests that have been written in support of the [Government Overreach / Ownership Ratchet exchange](../agent/exchanges/government-overreach-ownership-ratchet-exchange.md) and adjacent exchanges.

## Authoring guard — quote actual section titles from core normative documents

When a digest claims a linkage to any of the project's core normative documents in its **Project 2028 mapping** section (or anywhere in body text), the author **must** quote the section's actual current title verbatim, not paraphrase it from memory or summary. This rule exists because the [April 2026 coherence audit](../agent/process/audits/coherence-audit-2026-04.md) found that the first bulk-authoring pass of source digests cited section titles and anchors that *had never existed in any commit of the target documents* — phantom phrasings invented at digest-authoring time. **Pass 1** found 17 digests with this failure against [`PRINCIPLES.md`](../PRINCIPLES.md). **Pass 2** found ~50 digests with the same failure against [`PROBLEM_MAP.md`](../PROBLEM_MAP.md) — including invented domain titles like "Housing has decoupled from wages," "Post-scarcity future," "Work and purpose are decoupling," and "Transformative technology is arriving" that exist nowhere in `PROBLEM_MAP.md`'s git history. The fix in both passes was to re-author every affected mapping section against the actual document text.

To prevent the same failure mode going forward, every digest author **must** apply the following per-document checklist before committing a digest:

1. **Quote the section's H2 heading verbatim.** Open the target document, locate the relevant section, and copy the H2 text exactly. Do not paraphrase from prior digests, prior exchanges, or memory.
2. **Generate the anchor mechanically from the heading.** The anchor is the heading lowercased, with non-alphanumerics removed, words joined by hyphens, and the leading number (if any) prefixed (GitHub Flavored Markdown rules). Example: `## 2. Essential needs should not be held hostage to avoidable scarcity` → `#2-essential-needs-should-not-be-held-hostage-to-avoidable-scarcity`.
3. **Match the digest's substantive claim against the section's actual content.** If the source's substance does not fit the section's actual scope, pick a different section — do not bend the section's description to fit the source. Citing a misaligned section is a [Hallucinated reference](../agent/process/coherence-audit-protocol.md#3-issue-types) under the Coherence Audit Protocol.

This checklist applies to every core normative document. Specifically:

| Document | Verify by | Expected anchor format | Last canonical-form audit |
|---|---|---|---|
| [`PRINCIPLES.md`](../PRINCIPLES.md) | H2 headings of the form `## N. Principle title.` | `#N-principle-title-lowercased-with-hyphens` | [Pass 1, April 2026](../agent/process/audits/coherence-audit-2026-04.md) |
| [`FOUNDATIONAL_COMMITMENTS.md`](../FOUNDATIONAL_COMMITMENTS.md) | H2 headings of the form `## N. Commitment title` | `#N-commitment-title-lowercased-with-hyphens` | [Pass 2, April 2026](../agent/process/audits/coherence-audit-2026-04.md#pass-2--problem_mapmd-hallucinations-and-principlesmd--foundational_commitmentsmd-5-drift) |
| [`PROBLEM_MAP.md`](../PROBLEM_MAP.md) | H2 headings of the form `## N. Domain title` | `#N-domain-title-lowercased-with-hyphens` | [Pass 2, April 2026](../agent/process/audits/coherence-audit-2026-04.md#pass-2--problem_mapmd-hallucinations-and-principlesmd--foundational_commitmentsmd-5-drift) |
| [`SYSTEMS_FRAMEWORK.md`](../SYSTEMS_FRAMEWORK.md) | H2 headings of the form `## Section title` | `#section-title-lowercased-with-hyphens` | [Pass 2, April 2026](../agent/process/audits/coherence-audit-2026-04.md#pass-2--problem_mapmd-hallucinations-and-principlesmd--foundational_commitmentsmd-5-drift) (zero anchors used in repo at audit time) |

A digest's body text may use a short paraphrase for readability (e.g. "Principle 2 (essential needs)" or "Domain 5 (Housing)"), but the link target and the substantive claim must be grounded in the actual section text. The short paraphrase should be a faithful summary of the actual title, not a different concept smuggled in.

**Open drift caveat:** As of the Pass 2 audit, [`PRINCIPLES.md`](../PRINCIPLES.md) §5 and [`FOUNDATIONAL_COMMITMENTS.md`](../FOUNDATIONAL_COMMITMENTS.md) §5 use different vocabularies ("public-interest governance" vs. "inclusive institutions with bounded rules"). This is a real cross-document drift tracked by [ROADMAP TODO #1 F1](../ROADMAP.md#high-priority-unblocks-multiple-workstreams), not a hallucination. Until F1 resolves, digests citing §5 should pick the document whose vocabulary actually fits the digest's claim and link to that document specifically.

## Current corpus

As of April 2026, the directory contains 53 source digests:

- One originating adversarial anchor (the Modern Wisdom #1084 Friedberg digest).
- 43 curated reference digests from the first research sweep (April 2026), covering the eight sub-debates identified in the Government Overreach exchange.
- 7 curated reference digests from the second research sweep (April 2026), closing the five residual data gaps identified at the end of Round 2 of that exchange: Argentina under Milei; historical fiscal consolidation cases (Canada 1990s, Sweden 1990s, NZ 1984); AI catastrophic-risk literature; AI governance practice (EU AI Act, California SB 1047/SB 53, U.S. EO sequence, NIST AI RMF); cooperative and platform-cooperative ownership forms; sovereign wealth funds (Norway GPFG, Alaska Permanent Fund); Swiss direct democracy.
- One second steward-anchor digest (April 2026): *The Weekly Show with Jon Stewart — AI & The Future of Work*, an interview with Daron Acemoglu and David Autor that complements the Friedberg digest. Where Friedberg locates the obstacle to abundance in government overreach, Acemoglu and Autor locate it in concentrated tech-corporate ownership and the direction of technological development. This digest is the primary external evidence base for the [AI Commonwealth vs. AI Governance exchange](../agent/exchanges/ai-commonwealth-vs-governance-exchange.md) Round 1.
- One third steward-anchor digest (April 2026): *The Weekly Show with Jon Stewart — Politics for ME (and You) with Graham Platner*, an interview with the Maine 2026 U.S. Senate Democratic primary candidate. The speaker type differs from the prior two anchors (working candidate, not academic researcher) and the digest is explicit about that asymmetry. Substantive content includes an explicit theory of power, a New-Deal-shaped reform program (FDR's first 100 days; the 1944 Economic Bill of Rights), an "organizing-as-load-bearing" theory of political infrastructure, and a "good government, not no government" anti-libertarian closing. The digest's primary downstream candidates are Exchange #21 (bounded-governance doctrine F1/F3 follow-ups), Exchange #8 (legitimacy-of-mobilization formulation), Exchange #22 (resolution-mismatch / translation across audience registers), and Exchange #11 (data-extraction-economy worked example with concrete Maine race instance). Exchange-spawn decision deferred to a follow-on planning round.

Viewpoint coverage is balanced across pro-market/libertarian, social-democratic/progressive, and heterodox/institutional positions so that exchange rounds can draw on sympathetic and skeptical evidence for each sub-debate. The ownership taxonomy developed in Round 2 is empirically grounded after the second sweep (cooperatives and SWFs as concrete instances), the AI-governance sub-debate is empirically and theoretically supported by paired digests (existential-risk literature + regulatory practice), and the bounded-governance design package in Sub-debate 8 has real-world case grounding (Argentina, Canada, Sweden, NZ, Switzerland).

Successor sweeps can expand the corpus further in each sub-debate (targeted empirical studies, regional case studies, additional philosophical positions). New digests should be added both to the directory and to the [Source Index](SOURCE_INDEX.md) under the correct sub-debate bucket.
