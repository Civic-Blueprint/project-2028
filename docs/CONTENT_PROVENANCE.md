---
description: Project standard for labeling human and AI involvement in authored content.
provenance: "collaborative"
---

# Content Provenance Standard

## Purpose

This document defines how Project 2028 labels content provenance across all public and internal artifacts. The goal is straightforward: make authorship and generation pathways legible so readers can evaluate claims with appropriate context.

This standard is part of the project's trust posture and directly relates to:

- [Principles](../PRINCIPLES.md), especially Principle 4 (accountable, legible power) and Principle 14 (truth and evidence as public goods)
- [Roadmap Recommendation 5](../ROADMAP.md#recommendation-5-commit-to-transparent-evidence-integration-in-advance)
- [Proposal `P-020` in the Proposal Catalog](../proposals/PROPOSAL_CATALOG.md#p-020-ai-content-provenance-mandate)

The project is intentionally dog-fooding its own provenance policy position.

---

## Provenance labels

Use exactly one primary label per artifact.

| Label | Definition | Typical examples |
|---|---|---|
| human | Written directly by the steward without AI drafting. | Outreach messages, direct steward reflections, personal notes |
| collaborative | Human-directed, AI-drafted, steward-edited. Steward sets intent/constraints, AI helps draft, steward revises and approves final form. | Core synthesis docs and public memos with steward sign-off |
| ai-generated, steward-curated | AI generates candidate content under defined protocols; steward curates, selects, and contextualizes outputs. | Proposal catalog entries, exchange outputs synthesized from multi-round generation |
| ai-generated | AI-generated content not yet reviewed or adopted by the steward. | Raw drafts, intermediate experimental output |

---

## Application rules

1. **Public-facing pages and documents** should show provenance clearly and early (header, frontmatter-derived metadata, or an explicit callout near the top).
2. **Collaborative and curated artifacts** should briefly describe process (for example: "drafted with AI and revised/approved by steward").
3. **Raw AI output** should not be presented as endorsed project position.
4. **When provenance changes** (for example, a raw AI draft becomes steward-curated), update the label.
5. **Do not over-claim human authorship** for AI-assisted synthesis.
6. **Do not over-claim AI autonomy** where substantial human direction and editorial judgment were applied.

---

## Minimum disclosure template

Use this short form where space is limited:

> **Provenance:** label — one-sentence process note.

Examples:

- **Provenance:** collaborative — Drafted through human-directed AI iteration, then revised and approved by the steward.
- **Provenance:** ai-generated, steward-curated — Generated through structured agent rounds; entries were selected and contextualized by the steward.

---

## Scope

This standard applies to:

- Core documents in `project-2028`
- Memos and proposal catalog artifacts
- Exchange documents where provenance is not already obvious from process descriptions
- Public presentation layers in `civicblueprint.org` that render or summarize project content

---

## Versioning

This is Version 1 of the provenance standard. It is expected to evolve as practitioner feedback arrives and as the project learns which labels are both legible and accurate in practice.
