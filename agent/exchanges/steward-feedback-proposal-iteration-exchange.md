# Steward Feedback Proposal Iteration — Exchange

> **Status (April 2026):** Active discussion. This exchange captures the next experiment: using steward feedback on a subset of cataloged proposals as a new input layer for another round of proposal refinement and generation.
>
> **Why this exchange:** [Exchange #13](autonomous-proposal-generation-stress-test.md) generated a large proposal set, and the follow-up [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) was created so a steward could react to proposals individually. The steward has now begun annotating proposals with priorities and comments and wants to test whether that human feedback changes what the agents generate next. This exchange starts now because the project is shifting from one-shot autonomous generation toward iterative, steward-in-the-loop proposal development.

---

## Dependency context

- **Prior exchanges:** [Exchange #7 — Proof-of-Usefulness Memo: Feedback Timescale Review](proof-of-usefulness-feedback-timescale-review.md), [Exchange #13 — Autonomous Proposal Generation: Agent Stress Test](autonomous-proposal-generation-stress-test.md), [Exchange #14 — Permitting Stack Recursive Uplift](permitting-stack-recursive-uplift-exchange.md)
- **Core documents:** [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md)
- **Proposal source:** [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md)
- **Cross-repo artifacts:** None yet

---

## Opening question

When steward feedback is added to a subset of proposals in the catalog, does that human input materially change what a new proposal-development round produces — in specificity, originality, prioritization, coalition awareness, or recursive-uplift logic?

---

## Why this experiment matters

The first proposal-generation exchange tested autonomous breadth: what agents could produce from the project's analytical framework without steward intervention. This new exchange tests something different:

1. Whether steward judgment acts as a useful constraint rather than a creativity bottleneck
2. Whether proposal iteration is more valuable than fresh proposal generation
3. Whether agent outputs become more politically or strategically grounded when they are forced to react to concrete human comments

This is directly responsive to the conclusion recorded after Exchange #13: the value likely compounds when agents build on existing proposals rather than regenerating from the framework from scratch.

---

## Current state of the experiment

The steward reports having added priorities and comments to **35 proposals** in the catalog and wants to use those as the basis for a new exchange.

At the moment this exchange is being opened, the current saved file state visible to the agent does **not yet expose the specific 35 annotated entries**. That means:

- the experiment is officially started
- the exchange can frame the methodology and the questions
- the exact proposal subset still needs to be incorporated from the steward-annotated catalog state in a follow-up round

This should be treated as a sequencing issue, not a conceptual blocker.

---

## Initial hypothesis

Steward feedback should improve the next round along at least four dimensions:

1. **Selection pressure:** agents spend effort on proposals a human already thinks are worth engaging
2. **Constraint quality:** comments expose hidden objections, ambiguities, or opportunities that generic adversarial prompts miss
3. **Cross-proposal pattern recognition:** steward annotations may reveal shared concerns across domains that justify new synthesis proposals
4. **Proposal evolution:** feedback may generate revised variants, mergers, splits, or sequencing changes that are more useful than novel one-off ideas

---

## Relationship to `P-004 / P-107`

The steward has separately chosen `P-004 / P-107` as the strongest candidate for recursive-uplift follow-up, and that work now has its own dedicated home in [Exchange #14](permitting-stack-recursive-uplift-exchange.md).

This exchange is broader. It asks whether steward feedback across **35 proposals** produces a different kind of value than the single-proposal deep dive:

- Exchange #14 = depth on the strongest starting node
- This exchange = breadth-through-feedback on a curated proposal subset

The two experiments should eventually inform each other.

---

## Candidate outcomes for this exchange

If the experiment works, it may produce one or more of the following:

- revised versions of existing proposals
- merged proposal clusters
- new sequencing logic across the 35 annotated proposals
- stronger coalition or implementation analysis
- a shortlist of proposals ready for domain-specific exchanges
- updates back into the [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md)

If the experiment fails, that is also informative: it may show that steward comments help with prioritization but do not materially improve generative output.

---

## Initial tensions to resolve

1. **Iteration vs. regeneration:** should agents refine only the 35 annotated proposals, or also generate adjacent new ones?
2. **Faithfulness vs. creativity:** how tightly should agents adhere to steward comments before they stop being useful as generators?
3. **Proposal-level vs. pattern-level feedback:** are the steward annotations mostly about individual proposals, or do they reveal higher-order patterns across the catalog?
4. **Catalog update threshold:** what standard should a newly generated variant meet before it gets folded back into the proposal catalog?
5. **Mixing experiments:** how much should the broader 35-proposal experiment interact with the more focused `P-004 / P-107` exchange?

---

## Starter questions for the next round

1. Which exact 35 proposals were annotated by the steward?
2. What kinds of annotations were added: priority, objection, riff, merge suggestion, feasibility concern, or sequencing note?
3. Should the next round optimize for new proposal variants, better prioritization, or cross-domain synthesis?
4. What would count as a meaningful improvement over Exchange #13 rather than a restatement of it?
5. Which outputs, if any, should be folded back into the proposal catalog and under what labeling convention?
