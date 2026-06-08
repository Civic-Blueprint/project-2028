---
title: Agent Automation and the Verifier
description: A working-claim memo on what civic-analysis work the project can responsibly hand to AI agents, and what it cannot. Argues that the AI gains documented in software engineering and AI research ride on cheap, fast, objective verifiers (tests, timers, reproduced numbers), and that "research taste/judgment" persists as a human role precisely where the verifier is slow, contested, or absent. Decomposes "civic taste/judgment" into five tiers by verifiability and maps them onto the project's existing protocol stack — finding that the four review protocols plus the cross-lineage pipeline are already the civic-domain analog of unit tests, each a proxy verifier for a different tier. Concludes that the defensible "fast-track" is to industrialize the verifiable tiers (the cross-lineage review harness), measure judgment over time (Civic-Bench), and strengthen the one weak verifier the strategic tier has (the historical backtest) — while never automating the strategic/normative/legitimacy tier, which Principles 3, 4, and the reflexive guardrail reserve for human, accountable judgment. Keystone of a four-artifact cluster; a strategic claim about project direction and therefore itself routed to cross-lineage adversarial review before any promotion.
provenance: collaborative
status: Working claim (June 2026) — NOT doctrine; routes to the cross-lineage review harness for adversarial review before any promotion
created: 2026-06-08
---

# Agent Automation and the Verifier

## What civic analysis the project can hand to agents — and what it cannot

> **Provenance:** `collaborative` — Human-directed AI drafting, steward synthesis and approval pending. See [Content Provenance Standard](../docs/CONTENT_PROVENANCE.md).

> **Status.** This is a **working-claim memo**, not [doctrine](../agent/doctrine/_DOCTRINE_INDEX.md) and not a [principle](../PRINCIPLES.md). It makes a **strategic claim about the project's own direction** (how far to automate the project's analytical work), which is exactly the trigger the [Adversarial Review Protocol §1](../agent/process/adversarial-review-protocol.md) names for review. Consistent with the project's own discipline, the memo therefore **routes itself** to the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) for a blind, independent-lineage pass before anything here is promoted. Nothing in it is adopted by being written down.

> **Genesis.** Prompted by the steward reading *["When AI builds itself"](https://www.anthropic.com/institute/recursive-self-improvement)* (The Anthropic Institute, June 2026) and asking whether the AI gains documented in software and AI research could be "fast-tracked" for civic and governance judgment — extrapolating from the structural dissection in the [Discovery Principle riff](../agent/explorations/discovery-principle-moral-architecture-riff.md) and the [develop-leg exchange](../agent/exchanges/discovery-principle-develop-leg-exchange.md). This memo is the answer, and the keystone of the four-artifact cluster that answer produced. *(The source is cited inline here; promoting it to a [`sources/`](../sources/) digest under the [Research Protocol](../agent/process/research-protocol.md) is a recommended follow-up — see §9.)*

---

## 1. The question

Can the project train or deploy AI for **"taste and judgment" in civics and governance** the way the industry trained it for software — and so reach the project's goals faster?

The honest answer is: **partly, and the project has already built the part that works — but the part the question is really reaching for has a hard limit the project's own corpus has already demonstrated.** The rest of this memo states why, decomposes the claim so the buildable parts separate cleanly from the unbuildable one, and points to the three instruments that operationalize the buildable parts.

---

## 2. The gains in software are not about intelligence — they are about the verifier

The [Anthropic piece](https://www.anthropic.com/institute/recursive-self-improvement) documents AI going from helpful to superhuman on a specific class of work. Every example shares one feature: a **cheap, fast, objective feedback loop with a ground truth.**

| Documented gain | The verifier underneath it |
| --- | --- |
| SWE-bench (low single digits → saturation in 2 years) | The project's own unit tests pass or fail |
| CORE-bench (≈20% → saturated in 15 months) | The published paper's numbers reproduce or they don't |
| Kernel-speedup test (~3× → ~52× in a year) | A timer |
| Weak-to-strong supervision (97% of the gap, 800 hrs) | A pre-set performance floor and ceiling, and a scoring rubric |
| "Next-step" research judgment (51% → 64%) | A retrospective judge that saw how the session actually ended |

The piece's own framing — "perspiration becoming automated" — is true *because perspiration is verifiable*. The "research taste" gap it keeps circling persists exactly where the loop is slow, expensive, ambiguous, or absent. That is the mechanism. It is not that judgment is mystically human; it is that **judgment is the name we give to the work for which no cheap verifier exists yet.**

So the real question is not "can AI get civic taste?" It is: **where in civics can a cheap, trustworthy verifier be built?** Where one can, the software curve is available. Where one cannot, it is not — and no increase in model capability changes that, because the missing thing is the feedback signal, not the intelligence.

---

## 3. Civics lacks the ground-truth verifier — and the project already proved this rigorously

The reason the software playbook does not port directly to governance is the claim three independent model lineages found **decisive** in [Exchange #27](../agent/exchanges/discovery-principle-develop-leg-exchange.md): **S17, the cross-scale transfer failure.** The cleanest statement of the obstacle is the reviewers' own: *societies have institutions, power, incentives, legitimacy, and coalition formation — not a brain that experiences dissonance.* The **ecological fallacy** ([exchange §2.4, §2.5](../agent/exchanges/discovery-principle-develop-leg-exchange.md)). Add the dose-response finding ("**conditions over magnitude**") and the **relabel gate** (S18), and Exchange #27 is, read against the Anthropic piece, an empirical demonstration of *why the civic verifier is missing*:

- **Ground truth is contested.** There is no agreed loss function for "a good society"; values are plural and irreducible ([Principle 13](../PRINCIPLES.md#13-pluralism-and-self-determination-are-strengths-not-obstacles)).
- **The feedback loop is years to decades**, and you cannot rerun a society or hold its variables constant.
- **Outcomes are confounded.** The only fully valid judge of a civic claim is a real polity over time — which is precisely the verifier you cannot make cheap.

This is not a gap a smarter model closes. It is structural, and the project has already paid the cost of learning it.

---

## 4. But "civic taste/judgment" is not one thing — it splits by verifiability

This is the reframe that makes the question tractable. Decompose the skill, and it separates into tiers that differ sharply in whether a cheap verifier exists. Crucially, **each tier already has a home protocol in the project's stack** — the project has been building proxy verifiers all along without naming them as such.

| Tier of "civic judgment" | Cheap verifier? | Automatable now? | Home protocol / instrument |
| --- | --- | --- | --- |
| **Evidential** — are sources real, used faithfully, tiered honestly? | Yes — check citations | **Yes** | [Research Protocol](../agent/process/research-protocol.md); the "verifier" role in [Pipeline Run 001](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md) |
| **Coherence** — does this contradict the rest of the corpus? | Yes — consistency check | **Yes** | [Coherence Audit Protocol](../agent/process/coherence-audit-protocol.md) |
| **Adversarial robustness** — does the claim survive hostile, *independent-lineage* scrutiny? | Yes — convergent failure across decorrelated models | **Yes — the rig already exists** | [Adversarial Review Protocol](../agent/process/adversarial-review-protocol.md) + the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) |
| **Diagnostic / framing** — is this the right problem, the right target? | Partly — backtest against history | **Partly** | [Historical Parallel Test Protocol](../agent/process/historical-parallel-test-protocol.md); the [riff §5.4 three-target decode](../agent/explorations/discovery-principle-moral-architecture-riff.md) |
| **Strategic / normative / outcome** — which reform sequence works; which values win; what counts as a good society | No cheap verifier; only a polity over years | **No** — and [P3](../PRINCIPLES.md#3-ai-must-augment-agency-not-replace-democratic-accountability)/[P4](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible) say it *should not* be | The human steward; the [reflexive guardrail](../agent/explorations/discovery-principle-moral-architecture-riff.md) (riff §8 / exchange S21); a slow, weak historical backtest |

The top three rows are the Anthropic piece's "doing." They are verifiable, therefore automatable — and the project *already automates them*. The bottom row is the piece's "direction-setting / taste"; for civics it is even less verifiable than it is for AI research, because there is no civic equivalent of a training run you can score.

### 4.1 The formalization intuition is right — and here is its exact limit

The steward's instinct — that the **dissection of levels, structures, and entities** in the riff and exchange might let agents operate on civic reasoning the way they operate on code — is correct, and not a coincidence. Part of why code is automatable is that it has **formal structure** (syntax trees, types, tests) an agent can mechanically operate on. The project's own machinery — the S1–S24 falsifiable-claim decomposition, the pre-registered falsification conditions, the epistemic-status tables, the target/layer/mechanism/lever grid of [riff §5.4](../agent/explorations/discovery-principle-moral-architecture-riff.md) — is an attempt to give civic claims comparable machine-checkable structure. That formalization genuinely *is* a fast-track enabler.

But the limit is precise: **formal structure buys machine-checkable *consistency*, *relabel-detection*, and *evidence-fidelity* — not machine-checkable *truth about civic outcomes*.** A falsification condition like S17's ("a matched collective-scale case") is *specified* but cannot be *run* cheaply. So the project can automate everything up to the point where reality is the only valid judge — and in civics, unlike code, reality ships no test suite.

---

## 5. The project already built its "SWE-bench moment" — Pipeline Run 001

The single most important grounding fact: **the project already owns a cheap proxy verifier for civic-reasoning quality.** [Pipeline Run 001](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md) handed one design memo to four blind, non-correlated model lineages (OpenAI / xAI / Google / Moonshot) plus a non-author synthesizer, and surfaced **five BLOCKING issues the same-lineage author draft missed.** That is the [develop-leg](../agent/exchanges/discovery-principle-develop-leg-exchange.md) mechanism — non-correlated authorities + psychological safety + consolidation — operating as a *test on the project's own work*, runnable in minutes via subagents at near-zero cost.

That is the lever. The defensible "fast-track" is **not** "train a model to have governance taste." It is to **industrialize the proxy verifiers the project already has**, so steward review stops being the binding constraint (the Amdahl's-law bottleneck the Anthropic piece names: once the doing is automated, *review* becomes the cap). Three concrete moves, each a companion artifact to this memo:

1. **Industrialize the verifier** → the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md). Generalize Run 001 from a bespoke run into a reusable harness any exchange, memo, or claim-set can be pushed through. This also resolves the long-parked [ROADMAP Thread C ("Red Team Run")](../ROADMAP.md).
2. **Measure the judgment** → the [Civic-Bench Design Memo](civic-bench-design-memo.md). The Anthropic piece's deepest lesson is that *benchmarks made progress measurable*. The project owns held-out judgment material no one else has — triage scores, exchange verdicts, proposal dispositions — and can build a benchmark to track whether agent judgment on *its own* problems is improving, instead of guessing.
3. **Strengthen the one weak verifier the strategic tier has** → the [Historical Parallel Test Protocol §6 backtest extension](../agent/process/historical-parallel-test-protocol.md#strategic-tier-backtest-the-projects-core-bench-analog). The historical backtest is the project's CORE-bench analog for the strategic tier — "given how this reform actually played out, was the predicted leverage right?" It is slow, confounded, and small-n, and will never be cheap — but it is the only verifier that touches the bottom row.

---

## 6. What this licenses — and what it forbids

### 6.1 Licensed: automate the doing

Tiers 1–3 (evidential, coherence, adversarial robustness) are verifiable, so automating them is in keeping with the project's commitments, not in tension with them. This is the work the harness and bench address. Fast-track it.

### 6.2 Forbidden: automate the direction-setting and the legitimacy

The Anthropic piece frames recursive self-improvement as opportunity *and* control risk. This project exists to make the normative claim that **AI must augment agency, not replace democratic accountability** ([P3](../PRINCIPLES.md#3-ai-must-augment-agency-not-replace-democratic-accountability)), and that **power must stay legible and reversible** ([P4](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible)) — plus the explicit reflexive guardrail that *the project must not become the machine it diagnoses* ([riff §8](../agent/explorations/discovery-principle-moral-architecture-riff.md), exchange S21). So "automate getting us there faster" must hold a hard line:

- **Automating the *doing*** (analysis, review, evidence-checking, adversarial pressure) is legitimate, and the project already does it well.
- **Automating *direction-setting and legitimacy*** (which problems matter, which values win, what counts as a good society, the go/no-go) **is the machine.** It is the thing P3/P4 exist to keep from being captured, and an AI that *converges* on it does not produce wisdom — it produces **Goodhart**. The proxy verifier in §5 measures "survives independent scrutiny / internally coherent / well-cited," **not** "actually good for society." Because all frontier models share training data and tuning, convergent agreement can be **shared bias, not truth** — which is precisely why the project's own discipline already insists *"convergence is not the success metric; surviving the adversary is"* ([Pipeline Run 001 §3](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md)). **Reliability is not validity.**

The synthesis, in the Anthropic piece's own terms: **automate the perspiration; protect the inspiration — and in civics, also protect the legitimacy.** The fast-track is real, its engine is already built, and the discipline that keeps it from becoming the failure mode the project is trying to fix is the discipline the project has already written down.

---

## 7. Why the verifier stack is the project's "antibody," not a new risk

A natural worry: does automating the project's own reasoning *increase* the convergence/false-confidence risk the [README](../README.md) already names? The develop-leg work answers this directly. The cross-lineage pipeline is the project's antibody, not a new vector — *if and only if* it stays **parallel, not series**: independent lineages, blind to each other, rewarded for challenge rather than agreement, with a human owning the falsifier set and the go/no-go ([test-design memo §7.2–§7.4](../agent/exchanges/discovery-principle-develop-leg-test-design-memo.md)). A **single-lineage** automation would be *series-wired by construction* — the exact anti-pattern the develop-leg diagnoses, and self-refuting as a method for this project. The verifiability-tier model is therefore not a license to automate broadly; it is a license to automate **only the tiers a decorrelated verifier can police, only through a decorrelated verifier.**

---

## 8. Honest limits and failure modes

- **The proxy is not the ground truth.** Surviving cross-lineage review means "defensible," not "true." The bottom-tier verifier (a real polity over years) is irreplaceable; nothing here substitutes for it.
- **Goodhart.** Optimizing artifacts to pass the harness can train the project to produce *defensible-looking* work rather than *correct* work. The bench's held-out discipline and the harness's adversary-survival (not convergence) metric are partial guards, not cures.
- **Reliability ≠ validity.** Cross-lineage agreement is reduced common-mode failure, not external correctness; the shared-training-corpus caveat stands ([#25 cross-model runs](../agent/exchanges/shared-mirror-see-layer-exchange.md) reached the same conclusion).
- **The Rung-0 circularity is live.** A pipeline that instantiates a hypothesis and then scores itself is circular; Run 001's own adversary flagged it, which is why agent-scale results are explicitly *not* civic evidence ([test-design memo §6, §8](../agent/exchanges/discovery-principle-develop-leg-test-design-memo.md)). The same caution binds this memo: the project choosing to automate *partly believing automation helps* makes a clean result suggestive, not confirmatory.
- **This memo is itself a strategic claim** and has not survived the review it prescribes. It is a working claim pending the §1 harness pass.

---

## 9. Status, routing, and open questions

**Status.** Working claim. Not doctrine, not a principle, not adopted. The verifiability-tier model (§4) and the licensed/forbidden line (§6) are the load-bearing claims; both are contestable.

**Routing.**

1. Run this memo through the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) (blind, independent-lineage) before any promotion — the project's own §1 discipline applied to itself.
2. If it survives, it is a candidate for [doctrine](../agent/doctrine/_DOCTRINE_INDEX.md) (an adopted operational framework for *how the project decides what to automate*), gated on the four doctrine conditions.
3. Promote the [Anthropic source](https://www.anthropic.com/institute/recursive-self-improvement) to a [`sources/`](../sources/) digest under the [Research Protocol](../agent/process/research-protocol.md) so future exchanges cite a tiered digest rather than re-summarizing.

**Open questions.**

1. **Is the five-tier model the right cut?** Do "diagnostic/framing" and "strategic" collapse into one, or split further? (The §1 harness pass should attack this first.)
2. **Where exactly is the line between tier 4 and tier 5?** Diagnostic framing (which target, which layer) is partly backtestable; strategic sequencing is not. The boundary is the most decision-relevant and the least sharp.
3. **Goodhart measurement.** Can the project detect when it is optimizing for harness-survival over correctness — e.g., by tracking whether harness-passed claims later fail human/practitioner review?
4. **Does the bench amplify the steward's blind spots?** A benchmark of steward judgments rewards *matching the steward*; only the harness (which values catching steward error) offsets it. The two instruments must be run together — see [Civic-Bench Design Memo §5](civic-bench-design-memo.md).

---

## Provenance and register

`collaborative` — human-directed AI drafting; steward synthesis and approval pending. Working-claim register: named uncertainty, no rhetorical flourish, no promotion. Keystone of the four-artifact cluster (this memo, the [harness protocol](../agent/process/cross-lineage-review-harness-protocol.md), the [Civic-Bench design memo](civic-bench-design-memo.md), and the [historical-parallel backtest extension](../agent/process/historical-parallel-test-protocol.md#strategic-tier-backtest-the-projects-core-bench-analog)). Like the develop-leg companions, it is **not** registered in [`_EXCHANGE_INDEX.md`](../agent/exchanges/_EXCHANGE_INDEX.md); it is a memo. It reaches no verdict it has not earned, and it has not yet earned one.
