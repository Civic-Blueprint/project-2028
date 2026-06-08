---
title: Civic-Bench Design Memo
description: A scoping design for a held-out judgment benchmark built from the project's own curated judgments — website-submission triage scores, exchange epistemic-status gradings and verdicts, adversarial-review severity findings, and (when available) proposal-catalog dispositions. The benchmark measures whether AI agents can reproduce the project's calibrated judgment on its own problems over successive model versions — the project's analog of SWE-bench/CORE-bench, but for the "judgment" tier the recursive-self-improvement evidence treats as the human moat. Carries the load-bearing caveat that matching a steward label is calibration, not truth, so the bench must be run paired with the cross-lineage review harness (which rewards catching steward error) to avoid training agents to amplify the steward's blind spots. Design only — no dataset frozen, no model scored, nothing promoted.
provenance: collaborative
status: Design scope (June 2026) — no dataset frozen, no model scored; routes to the cross-lineage review harness before adoption
created: 2026-06-08
---

# Civic-Bench Design Memo

## A held-out benchmark for measuring agent judgment on the project's own problems

> **Provenance:** `collaborative` — Human-directed AI drafting; steward synthesis and approval pending. See [Content Provenance Standard](../docs/CONTENT_PROVENANCE.md).

> **Status.** This is a **design scope**, not a built benchmark. No dataset is frozen, no model is scored, nothing is promoted. It is the [verifier memo's](agent-automation-and-the-verifier-memo.md) second instrument — the one that *measures* whether the project's bet on automating verifiable judgment is actually paying out. Like the keystone memo, it makes a methodological claim about project direction and **routes itself** to the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) before adoption.

---

## 1. Why build this

The [Anthropic recursive-self-improvement piece](https://www.anthropic.com/institute/recursive-self-improvement) makes one structural point the project should copy: **benchmarks made progress measurable.** SWE-bench, CORE-bench, and the long-horizon METR tasks are what turned "models feel better" into a curve you can plot and a saturation point you can see. Without a benchmark, the project's claim that "agent judgment on our problems is improving" is a vibe, not a measurement.

The project is unusually well-positioned to build one, because it has been **accumulating curated judgments for over a year** that no general benchmark contains:

- **Website-submission triage scores** — six pre-defined dimensions (Relevance, Specificity, Evidence, Novelty, Actionability, Steward priority), each a numeric steward judgment under a documented rubric ([Website Submission Triage Checklist](../WEBSITE_SUBMISSION_TRIAGE_CHECKLIST.md); [website-submission-triage skill](../.cursor/skills/website-submission-triage/SKILL.md)).
- **Exchange epistemic-status gradings** — claims graded *contested / unsupported / underspecified / relabel / supported* and verdicts (*HOLD*, *REVISE*, *promote*), e.g. the [Exchange #27 §2.3 table](../agent/exchanges/discovery-principle-develop-leg-exchange.md) and the [#25 cross-model runs](../agent/exchanges/shared-mirror-see-layer-exchange.md).
- **Adversarial-review severity findings** — `BLOCKING / MAJOR / MINOR / AFFIRMING` on a known artifact, e.g. the [five BLOCKING issues](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md) Pipeline Run 001 surfaced.
- **Proposal-catalog dispositions** — *interesting / wrong / debatable* steward triage (not yet produced; [ROADMAP TODO #4](../ROADMAP.md) — a *future* source).

These are exactly the **"judgment" tier** the Anthropic piece treats as the lingering human comparative advantage. A benchmark over them measures the one thing the project most wants to know: not "can the agent write," but "**can the agent judge the way the project, at its most careful, judges?**"

---

## 2. What the benchmark measures — and what it does not

**It measures calibration to the project's curated judgment.** Given the same inputs a human (or a cross-lineage exchange) saw, blind to the recorded verdict, can an agent reproduce it?

**It does not measure truth.** The ground truth here is the project's *own past judgments*, which are fallible and can be the very blind spots the project is trying to surface. So a perfect score means "the agent matches us," not "the agent is right." This is the same proxy caveat the [verifier memo §6.2](agent-automation-and-the-verifier-memo.md) and the [harness §7](../agent/process/cross-lineage-review-harness-protocol.md) carry: **reliability is not validity.** The benchmark is a *consistency and progress-tracking* instrument, and it is only safe **paired** with the harness (see [§5](#5-the-pairing-rule-bench-without-harness-is-a-trap)).

---

## 3. Candidate tasks

Each task is a held-out prediction with a recorded answer the agent never sees at inference time.

| Task | Input given to the agent | Held-out target | Scoring |
| --- | --- | --- | --- |
| **T-A: Triage-score reproduction** | A website submission + the six-dimension rubric | The steward's six scores | Per-dimension error + rank correlation; calibration plot |
| **T-B: Claim-status prediction** | A claim + its falsification condition + the shared evidence base | The cross-lineage epistemic status (contested/unsupported/…) | Classification accuracy; confusion matrix (which statuses it confuses) |
| **T-C: Verdict prediction** | A full claim-set + round context | The exchange verdict (HOLD / REVISE / promote) | Accuracy; cost of false "promote" weighted highest |
| **T-D: Known-issue recall** | An artifact a review later found flawed | The set of recorded BLOCKING/MAJOR findings | Recall of known issues; false-positive rate on AFFIRMING artifacts |

**T-D is the closest analog to CORE-bench** ("reproduce the known result"): it asks whether an agent, run blind, *re-finds the problems the project already knows were there.* It is also the most decision-relevant, because the project's real bottleneck is catching defects before they ship.

---

## 4. Construction discipline (the part that makes it honest)

A benchmark built carelessly measures contamination, not judgment. The non-negotiables:

1. **Hold-out and sequester.** The target verdicts must be **removed from any context the scored agent sees**, and stored separately. Prefer items whose verdicts **post-date** the scored model's training cut, or that were never published in a form a model could have ingested.
2. **Score the reasoning, not only the label.** Matching a final label can be luck or parroting (the [Frazier measurement-validity caution](../agent/exchanges/discovery-principle-develop-leg-test-design-memo.md): self-report/surface ≠ actual capacity). Each item carries a short **rationale rubric**; an answer that lands the label with incoherent reasoning is scored as a *near-miss*, not a hit.
3. **Pre-register the scoring** before any model is run, and freeze a `bench_hash` (the [harness Stage-0](../agent/process/cross-lineage-review-harness-protocol.md) discipline).
4. **Multi-coder ground truth where the label is itself a judgment.** Where the "answer" was one steward's call, record inter-rater context; flag single-coder items as lower-confidence.
5. **Version every run.** Pin the model version; the point is a **time series** across model generations (the Anthropic-piece curve), not a single score.
6. **Keep a frozen test split untouched** for cross-version comparability, and a rotating dev split for iteration, so the project does not overfit the instrument.

---

## 5. The pairing rule: bench without harness is a trap

A benchmark of *steward/exchange judgments* rewards **matching the project**. Optimized alone, it trains agents to **reproduce the steward's blind spots** — the precise convergence/false-confidence failure the [README](../README.md) and the [develop-leg](../agent/exchanges/discovery-principle-develop-leg-exchange.md) warn against. The offset is structural:

- the **Civic-Bench** measures *can the agent match our calibrated judgment?* (consistency);
- the **[Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md)** measures *can independent agents catch errors we missed?* (divergence-that-corrects).

Neither alone is sufficient. Run together, they triangulate: the bench tells you the agent is *aligned with the project's best judgment*; the harness tells you the agent (or the project) is *not merely confirming itself*. A high bench score with a harness that never finds blocking issues is the **Goodhart signature** — track that combination explicitly as a warning, not a win.

---

## 6. Staged build — start with the cleanest seed

Mirroring the [test-design memo's rungs](../agent/exchanges/discovery-principle-develop-leg-test-design-memo.md#6-the-rungs--start-with-the-smallest-cylinder): nothing is promoted at any rung, and each is gated by the prior.

| Rung | Scope | What it establishes |
| --- | --- | --- |
| **0** | Spec + scoring frozen; **no data** | The harness reviews *this design* (instrument validation, non-evidence) |
| **1** | T-A on the existing triage corpus (smallest, already-rubric'd, numeric) | Does the bench detect variation in agent judgment at all? |
| **1.5** | Add T-D (known-issue recall) on a handful of reviewed artifacts | Does "re-find the known BLOCKING issues" discriminate model versions? |
| **2** | Add T-B/T-C; freeze a test split; run ≥2 model generations | First **time series** — is judgment improving on the project's problems? |
| **3** | Pair every run with a harness pass; track the Goodhart combination | Calibration *and* error-catching tracked together over time |

T-A is the right rung-1 seed because the triage scores are already **structured, numeric, and rubric-governed** — the lowest-ambiguity ground truth the project owns.

---

## 7. Honest limits

- **Matching us is not being right.** The ceiling of this benchmark is "as good as the project's curated judgment," which is itself under revision. It cannot certify correctness, only consistency and trend.
- **Small n.** The project's judgment corpus is modest; early rungs will be underpowered and noisy. Treat early numbers as directional.
- **Label drift.** The project revises its own verdicts (the develop-leg HOLD became a *live* hold; #25 downgraded M1). A benchmark must record **which version of the verdict** is the target and re-baseline when the project revises.
- **Goodhart and overfitting.** Any benchmark the project optimizes against degrades as a measure; the frozen-split discipline (§4.6) and harness pairing (§5) are partial guards, not cures.
- **Reliability ≠ validity**, carried from the [#25 cross-model runs](../agent/exchanges/shared-mirror-see-layer-exchange.md): agreement across runs is reduced common-mode failure, not external truth.

---

## 8. Status, routing, open questions

**Status.** Design scope. No dataset frozen, no model scored, nothing promoted.

**Routing.** Run this design through the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) (Rung 0) before building Rung 1. If it survives, Rung 1 (T-A on the triage corpus) is the smallest buildable first step and needs only a steward go-ahead and the existing triage records.

**Open questions.**

1. **Consent and privacy.** Triage records and feedback derive from real submissions under the [feedback privacy conventions](../feedback/README.md). Which records are eligible for a benchmark, and under what redaction? (Gating — resolve before Rung 1.)
2. **Whose judgment is "ground truth"** when steward and cross-lineage exchange disagree? Candidate: treat them as *two* targets and measure agreement with each separately.
3. **What counts as "improving"** — higher agreement, better calibration, higher known-issue recall, or lower false-promote rate? The metric the project optimizes is itself a values choice ([P4 legibility](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible)).
4. **Does T-D leak?** Many reviewed artifacts and their findings are in-repo and likely in training data; sequestering enough clean held-out items may be the binding constraint.

---

## Provenance and register

`collaborative` — human-directed AI drafting; steward synthesis and approval pending. Design register: named uncertainty, no rhetorical flourish, no promotion. Companion to the [verifier memo](agent-automation-and-the-verifier-memo.md), the [harness protocol](../agent/process/cross-lineage-review-harness-protocol.md), and the [historical-parallel backtest extension](../agent/process/historical-parallel-test-protocol.md#strategic-tier-backtest-the-projects-core-bench-analog). Not registered in [`_EXCHANGE_INDEX.md`](../agent/exchanges/_EXCHANGE_INDEX.md); it is a memo.
