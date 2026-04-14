---
description: Comparative alignment workspace for analyzing external formation documents against Civic Blueprint's principles.
---

# Formation Documents

This directory is now the `project-2028` side of a two-repository workflow for comparative formation-document analysis.

- retained source texts, source metadata, sourcing policy, and translation workflow now live in [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs)
- analysis memos, synthesis artifacts, framework guidance, exchanges, and protocol decisions stay here in `project-2028`

The split is intentional. `external-formation-docs` preserves the source corpus as reference material. This directory interprets that corpus and compares it to [PRINCIPLES.md](../PRINCIPLES.md).

---

## What belongs here

This directory should contain only project-authored analysis and comparative workflow materials:

- source-by-source alignment memos
- synthesis artifacts that aggregate findings across the corpus
- the shared alignment rubric for comparing external texts to the 17 principles
- the registry that tracks which sources are in scope and where they live

It should not be used to retain or edit canonical external source texts.

---

## Where the source corpus lives

Use [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs) for:

- `documents/` containing retained texts and `_source-meta.yaml`
- `SOURCING_POLICY.md`
- `TRANSLATION_WORKFLOW.md`
- `_source-meta-template.yaml`

That repository is the canonical home for constitutions, charters, declarations, cooperative identity statements, and similar external formation documents used by this analysis track.

---

## Directory map

```text
project-2028/formation-docs/
  README.md
  SOURCE_REGISTRY.md
  ALIGNMENT_FRAMEWORK.md
  analysis/
    principle-maps/
    synthesis/
```

- `SOURCE_REGISTRY.md` tracks which sources are in scope and links out to their folders in `external-formation-docs`.
- `ALIGNMENT_FRAMEWORK.md` defines how external provisions map to Civic Blueprint's 17 principles.
- `analysis/principle-maps/` contains one alignment memo per source or source set.
- `analysis/synthesis/` contains cross-source outputs such as the alignment matrix, gap analysis, and uniqueness tracking.

---

## Analysis workflow

This track uses the [Comparative Alignment Protocol](../agent/process/comparative-alignment-protocol.md), then feeds into the rest of the project's review stack:

1. Add or register a source in [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs).
2. Record or update `_source-meta.yaml` in that repository.
3. Produce a source-specific alignment memo in `analysis/principle-maps/`.
4. Update synthesis artifacts in `analysis/synthesis/`.
5. If the source exposes meaningful tensions or omissions, open or extend an exchange in `agent/exchanges/`.
6. Use the [Adversarial Review Protocol](../agent/process/adversarial-review-protocol.md) to test any strong synthesis claim that emerges.
7. Use the [Coherence Audit Protocol](../agent/process/coherence-audit-protocol.md) if findings imply changes to [PRINCIPLES.md](../PRINCIPLES.md), the roadmap, exchange dependencies, or source-handling assumptions.

---

## Translation and expert review

Many of the most valuable formation documents are multilingual or translation-sensitive. Translation-status tracking, native-language review requests, and retention decisions now live with the source corpus in [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs), especially in:

- [`TRANSLATION_WORKFLOW.md`](https://github.com/Civic-Blueprint/external-formation-docs/blob/main/TRANSLATION_WORKFLOW.md)
- per-source `_source-meta.yaml`

Analysis written here should state whether it relies on original-language text, an official translation, an unofficial public translation, or an AI working translation. Claims that depend materially on wording nuance should remain provisional until expert or official verification exists.

---

## Current scope

The corpus currently spans four source families:

- nation-state formation documents
- U.S. state constitutions
- international charters and declarations
- organizational identity and governance texts

The goal is not to rebuild the broader comparative-constitutional ecosystem. The goal is to pressure-test Civic Blueprint's principles against a disciplined external corpus and make overlap, divergence, silence, and possible gaps legible.

---

## Relationship to the rest of the repo

This directory remains a comparative analysis layer, not a replacement for the core project documents.

- [PRINCIPLES.md](../PRINCIPLES.md) remains the thing being tested
- [ROADMAP.md](../ROADMAP.md) remains the canonical tracker of major project next steps
- `agent/exchanges/` remains where consequential findings are debated
- `agent/process/` remains where the reusable review protocols live

The value of this directory is not that it stores texts. Its value is that it gives the project a disciplined place to interpret external founding commitments without collapsing them into Civic Blueprint's own voice.
