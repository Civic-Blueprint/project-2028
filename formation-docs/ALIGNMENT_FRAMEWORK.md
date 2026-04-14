---
description: Rubric for mapping formation documents against Civic Blueprint's 17 principles.
---

# Alignment Framework

This document defines how formation documents are compared to [PRINCIPLES.md](../PRINCIPLES.md). The goal is not to force foreign documents into Civic Blueprint's language. The goal is to make overlap, divergence, silence, and tension legible.

---

## Unit of analysis

Each source should be analyzed at the provision level.

Depending on the document, a provision may be:

- a preamble clause
- an article
- a section
- a chapter-level principle
- a stated cooperative value or mission statement

The analyst should not map an entire constitution to a principle in one move if the relevant commitments live in distinct provisions.

---

## Alignment categories

Every source-to-principle comparison should use one primary alignment category:

- `explicit-alignment`: the source directly states a substantively similar value or obligation
- `implicit-alignment`: the source does not state the principle directly, but nearby provisions imply a related commitment
- `different-resolution`: the source addresses a similar problem or tension, but resolves it differently than Civic Blueprint does
- `absent`: the source does not materially address the principle
- `contrary`: the source encodes a position that conflicts with the principle

These labels are analytic shortcuts, not final judgments. Use notes whenever the category alone hides important nuance.

---

## Confidence levels

Every mapping should also carry a confidence level:

- `high`: the source text is clear, the cited provision is direct, and translation risk is low
- `medium`: the mapping is plausible but depends on interpretation, structure, or context
- `low`: the mapping is speculative, translation-sensitive, or requires practice-level assumptions

---

## What counts as evidence

Primary evidence:

- the retained text in [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs)
- the source's canonical public text
- official translations where available

Secondary evidence:

- constitutional-court summaries
- government explanatory notes
- official rights guides

Practice evidence should be recorded separately. A constitution that promises a right and a state that routinely violates it are analytically important, but the text still says what it says.

---

## Mapping questions

For each source, ask:

1. Which of the 17 principles are clearly present?
2. Which are only weakly or indirectly present?
3. Which are missing?
4. Which are resolved differently?
5. Which source commitments do not map cleanly onto any current Civic Blueprint principle?

That fifth question is the most important one for revision pressure.

---

## Gap types

When a source contains a meaningful commitment that does not map cleanly to the current 17 principles, classify the gap:

- `candidate-new-principle`: a recurring substantive value that Civic Blueprint may be missing
- `candidate-subprinciple`: a value that fits within an existing principle but deserves explicit naming
- `candidate-tension-note`: a value already present in the principles but not acknowledged as a tension
- `candidate-implementation-note`: not a principle-level gap, but a useful governance or design constraint

---

## Interpretation guardrails

### Do not confuse text with practice

A text may be aspirational, weakly enforced, or symbolic. Record that, but do not silently downgrade the textual commitment.

### Do not confuse scope with strength

A short document can still encode a strong value. A long document can mention many rights weakly.

### Do not over-read silence

Older documents and terse charters may be silent on issues such as ecology, AI, or structural exclusion because the category had not yet been articulated. Mark those as absent, not as morally rejected, unless the text points the other way.

### Do not flatten tensions

If a source protects liberty strongly but says little about material stability, that is not just absence. It may reflect a different theory of freedom. Record that as `different-resolution` when appropriate.

---

## Source memo template

Each file in `analysis/principle-maps/` should include:

1. Source summary
2. Sourcing and language status
3. Alignment table
4. Notable gaps or distinctive commitments
5. Tensions with Civic Blueprint's current principles
6. Open questions

Suggested table format:

| Principle | Alignment | Confidence | Source provisions | Notes |
|---|---|---|---|---|

---

## Synthesis outputs

Per-source memos feed three corpus-wide outputs:

- `analysis/synthesis/alignment-matrix.md`
- `analysis/synthesis/gap-analysis.md`
- `analysis/synthesis/uniqueness-report.md`

These synthesis files should be updated incrementally rather than rewritten from scratch each time.

---

## Principle index

For convenience, the 17 current Civic Blueprint principles are:

1. Dignity is inherent and unconditional
2. Essential needs should not be held hostage to avoidable scarcity
3. AI must augment agency, not replace democratic accountability
4. Power must remain accountable, legible, and reversible
5. Critical systems require public-interest governance
6. The gains from automation should strengthen society, not destabilize it
7. Freedom requires both liberty and material stability
8. No class of people should become structurally excluded
9. Institutions should be designed for competence and trust, not theater
10. The future should be built in the open
11. Civilization depends on a functioning biosphere
12. The present generation holds obligations to the future
13. Pluralism and self-determination are strengths, not obstacles
14. Truth and evidence must be protected as public goods
15. The circle of moral consideration must remain open
16. Justice mediates between competing claims
17. Collective power must be exercised within principled constraints
