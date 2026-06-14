---
title: "Decorrelation as a First-Class Requirement for Independent AI Evaluation"
description: A position memo (Path B of the Anthropic Framework Contribution-Surface riff) arguing that the independent-evaluator ecosystem Anthropic's Advanced AI Framework calls for treats "independence" as financial / conflict-of-interest independence, leaving epistemic correlation — evaluators that share training lineage, methods, or institutional priors and therefore share blind spots — unaddressed. Proposes evaluator-pool decorrelation as a first-class qualification requirement alongside financial independence, backed by the project's worked cross-lineage practice and the decorrelation-metrics instrument. Written to double as external feedback on the framework and as the project's public methodology surface. Working claim; routes itself to cross-lineage review before any external use.
provenance: collaborative
status: Working claim (June 2026) — NOT doctrine; drafted for potential external delivery and as a website methodology surface, but routes itself to the Cross-Lineage Review Harness before any external use (§6)
created: 2026-06-14
---

# Decorrelation as a First-Class Requirement for Independent AI Evaluation

> **Provenance:** `collaborative` — human-directed AI drafting, steward synthesis and approval pending. See [Content Provenance Standard](../docs/CONTENT_PROVENANCE.md).

> **Status and intended use.** This is a **working-claim** position memo, drafted as the candidate Path B artifact from the [Anthropic Framework Contribution-Surface riff](../agent/explorations/anthropic-framework-contribution-surface-riff.md). It is written so it could serve two purposes at once: **structured feedback** on [Anthropic's Advanced AI Framework](../sources/source-anthropic-advanced-ai-framework-digest.md) (which explicitly invites it), and the project's **public methodology surface** (the front-door freshness the prior session's front-door decision called for). It is **not yet cleared for either use:** per the project's own discipline, a memo arguing for cross-lineage review must itself survive cross-lineage review first (§6). Nothing here is adopted by being written down.

---

## 1. The claim in one paragraph

Anthropic's Advanced AI Framework rightly says self-assessment is not enough and calls for an independent-evaluator ecosystem that "does not yet exist." But the framework's notion of evaluator **independence** is principally *financial and conflict-of-interest* independence. That is necessary and not sufficient. An evaluator can be financially independent and still **epistemically correlated** with what it evaluates — same model lineage, same training corpus, same methods, same institutional formation — and correlated evaluators share blind spots, which means they can converge on a clean bill of health that reflects *shared bias, not safety*. The missing requirement is **decorrelation**: an evaluator pool should be qualified not only on "no financial stake" but on "low shared-blind-spot risk," and that property should be declared and, where possible, measured. **Reliability is not validity**; independence of *interest* is not independence of *error*.

---

## 2. What the framework gets right, and the gap

The framework's independent-evaluation pillar is strong on the parts it addresses:

- It states plainly that "self-assessment is not enough" and that "a mature independent evaluation ecosystem does not yet exist."
- It requires evaluators "not having a financial interest in the developer and being free of major conflicts of interest."
- It names **evaluator-shopping** — "companies seek out whichever evaluator(s) will ask the least of them and be most generous" — and proposes a real institutional answer: rate evaluators and **randomly assign** highly-rated ones in high-stakes cases.

All of that targets **incentive** independence. The gap is **epistemic** independence. None of those provisions prevents an evaluator ecosystem composed of institutions that are financially independent but *correlated in how they think* — drawing on the same foundation models, the same benchmark suites, the same red-team playbooks, the same revolving-door talent pool. Such an ecosystem would satisfy the framework's "independence" while failing at the thing independence is *for*: catching the error the developer's own team also missed, because everyone shares the blind spot.

This is not hypothetical for AI specifically. As frontier evaluation increasingly *uses* frontier models to evaluate frontier models, evaluator and subject share the deepest possible correlation — training lineage. "Independent" then risks meaning "different org, same brain."

---

## 3. The proposal — decorrelation as a qualification requirement

Add **decorrelation** to the evaluator-qualification criteria, alongside financial independence, as a measured-where-possible property:

1. **Declare correlation axes.** A qualified evaluator declares, for each engagement, its correlation with the subject along named axes: model lineage(s) used in evaluation, shared benchmark/tooling provenance, methodological tradition, and talent overlap. The way COI disclosure already works — extended from *incentive* to *epistemic* overlap.
2. **Compose pools for decorrelation, not just for COI-cleanliness.** Where multiple evaluators or methods are engaged for a high-stakes model, require the *pool* to span decorrelated lineages and methods, so a shared blind spot is less likely to be unanimous. This strengthens the framework's own random-assignment idea: assign from **decorrelated strata**, not merely from a flat pool of COI-clean evaluators.
3. **Measure it.** Treat decorrelation as an auditable quantity, not a vibe. The companion [Decorrelation Metrics instrument](decorrelation-metrics-memo.md) defines runnable measures — single-lineage-catch fraction, drop-one non-redundancy, challenge rate, a structural diversity index, and (with seeded-defect calibration) a true joint-miss rate. The point is not these specific numbers but the principle: *if independence is a requirement, it should be measurable enough to fail.*
4. **Reward the catch, not the consensus.** The qualification and rating system should score evaluators on *surfacing what others missed*, not on agreement. Convergence among correlated evaluators is the failure mode wearing the costume of success.

None of this displaces the framework's design; it sharpens the pillar the framework itself flags as immature.

---

## 4. Why this project can say it credibly — and where it cannot

**The credible part: method.** This project was built, from its first protocol, around exactly this problem. Its [Adversarial Review Protocol](../agent/process/adversarial-review-protocol.md) was the first instrument it made, precisely because AI analysis produced in a single model lineage shares that lineage's blind spots. It then built a [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) that runs blind, parallel, independent-lineage review with divergence preserved. In its first run, four independent model lineages surfaced **five blocking issues a same-lineage draft had missed** ([Pipeline Run 001](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md)); scoring that run, **60% of the blocking findings were single-lineage catches** ([metrics memo §4](decorrelation-metrics-memo.md)) — i.e., a less diverse pool would likely have missed a majority of them. That is a small, n=1, agent-scale demonstration of the exact claim this memo makes.

**The honest part: not domain depth.** This project cannot evaluate biological-weapons uplift, offensive-cyber capability, or loss-of-control behavior in a frontier model, and it does not claim to. Its contribution is at the level of **evaluation methodology and governance design**, not technical evaluation. The decorrelation principle is portable precisely because it does not require model weights or bio/cyber expertise — but its portability is also its limit: it improves *how* an evaluator ecosystem is structured, not *what* the evaluators technically do.

---

## 5. Honest limits

- **Mitigation, not cure.** Cross-lineage decorrelation reduces common-mode failure; it does not establish truth. All frontier lineages share training data and tuning, so even a decorrelated AI-evaluator pool is closer to itself than to a human domain expert. Human decorrelation (independent technical teams, not just independent models) remains essential.
- **n = 1, agent-scale.** The project's evidence is one internal run on its own artifact, not a frontier-model evaluation. It is a proof of mechanism, not a track record.
- **Convergence ≠ proof, applied to this very memo.** The structural fit between "independent-evaluator ecosystem" and the project's harness is itself a convergence the project's own discipline says not to trust as proof. This memo is a candidate contribution, offered for challenge, not a finished claim.
- **Scale asymmetry.** This is an early-stage, open-source project addressing a frontier lab. That honesty is deliberate: the contribution stands on the *argument and the worked method*, not on institutional weight.

---

## 6. Self-application (the discipline this memo must pass)

A memo arguing that independent evaluation requires decorrelation cannot credibly be released having skipped decorrelated evaluation itself. Before any external delivery or publication, this memo routes to the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md): blind, independent-lineage review, divergence preserved, human go/no-go. If it cannot survive the discipline it preaches, it does not go out. This is also the cleanest possible demonstration of the claim — the method applied to the argument for the method.

---

## 7. Relationship to the project and the framework

- **Anchoring source:** [Anthropic Advanced AI Framework digest](../sources/source-anthropic-advanced-ai-framework-digest.md) — the independent-evaluation pillar this memo engages.
- **Problem Map:** [Domain 11 (AI and compute power are concentrating faster than governance can respond)](../PROBLEM_MAP.md#11-ai-and-compute-power-are-concentrating-faster-than-governance-can-respond) — this memo is a concrete, method-level contribution to closing the governance gap the domain names.
- **Principles:** [Principle 4 (Power must remain accountable, legible, and reversible)](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible) — decorrelated, logged, divergence-preserving evaluation is what makes a powerful actor's risk claims *legible* and contestable; [Principle 14 (Truth and evidence must be protected as public goods)](../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods) — independence of error is a condition for evaluation that protects rather than launders the evidence; [Principle 17 (Collective power must be exercised within principled constraints)](../PRINCIPLES.md#17-collective-power-must-be-exercised-within-principled-constraints).
- **Method corpus:** the [Agent Automation and the Verifier memo](agent-automation-and-the-verifier-memo.md) (*reliability ≠ validity*), the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md), and the [Decorrelation Metrics memo](decorrelation-metrics-memo.md).
- **Generalization:** the [Decorrelation as a Civic-Governance Primitive riff](../agent/explorations/decorrelation-civic-governance-primitive-riff.md) asks whether this same requirement generalizes from AI evaluators to any judgment-aggregating governance body; this memo is the AI-domain instance of that larger question.

---

## Provenance and register

`collaborative` — human-directed AI drafting; steward synthesis and approval pending. Working-claim register: named uncertainty, no rhetorical flourish, no promotion. Not registered in [`_EXCHANGE_INDEX.md`](../agent/exchanges/_EXCHANGE_INDEX.md); it is a memo. It has not yet survived the cross-lineage review it prescribes for itself, and until it does it is a draft, not a deliverable.
