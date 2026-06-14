---
title: Decorrelation Metrics — A Runnable Instrument for Measuring Evaluator Independence
description: Operationalizes the metrics brainstormed in the Anthropic Framework Contribution-Surface riff §9.3 into a runnable instrument for measuring whether a cross-lineage review pool is actually decorrelated. Defines six metrics, triages them into runnable-now vs. needs-instrumentation, computes the runnable-now ones on Pipeline Run 001 as the first worked application, and specifies the Stage-0 instrumentation a future Cross-Lineage Review Harness run needs to make the rest computable — turning the harness into a self-measuring instrument. Working claim; routes to the harness (with a Rung-0 self-reference caveat) before any promotion.
provenance: collaborative
status: Working claim / proposed instrument (June 2026) — NOT doctrine; routes to the Cross-Lineage Review Harness before promotion, with the self-reference caveat noted in §6
created: 2026-06-14
---

# Decorrelation Metrics — A Runnable Instrument for Measuring Evaluator Independence

> **Provenance:** `collaborative` — human-directed AI drafting, steward synthesis and approval pending. See [Content Provenance Standard](../docs/CONTENT_PROVENANCE.md).

> **Status.** Working-claim memo proposing a measurement instrument. It operationalizes the [Anthropic Framework Contribution-Surface riff §9.3](../agent/explorations/anthropic-framework-contribution-surface-riff.md) metrics brainstorm and supports the [Decorrelation as a First-Class Requirement for Independent AI Evaluation memo](decorrelation-independent-ai-evaluation-memo.md) (which needs measurement backing) and the [Decorrelation as a Civic-Governance Primitive riff](../agent/explorations/decorrelation-civic-governance-primitive-riff.md) (whose load-bearing open question is whether these metrics survive the jump from model lineages to human institutions). Like the other verifier-cluster memos, it routes itself to the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) before promotion — with the caveat (§6) that a metrics memo *about* the harness, reviewed *by* the harness, is partially self-referential.

---

## 1. The question

The [verifier cluster](agent-automation-and-the-verifier-memo.md) and the [harness](../agent/process/cross-lineage-review-harness-protocol.md) rest on a claim: that **decorrelated** reviewers catch what a single-lineage reviewer misses. That claim has been *demonstrated once* (Pipeline Run 001) but never *measured*. "Convergence is not the success metric; surviving the adversary is" is the right principle — but without metrics, the project cannot tell a genuinely decorrelated pool from one that merely *looks* diverse, nor detect when its review is degrading into correlated rubber-stamping.

This memo makes decorrelation **measurable**: it defines the metrics, says which can be computed from existing data and which need new instrumentation, computes the former on Run 001, and specifies the latter so the harness becomes self-measuring going forward.

---

## 2. The six metrics

Grouped into three families (per the riff §9.3 brainstorm).

### Family 1 — decorrelation metrics (is the pool actually independent?)

- **M1 — Single-lineage-catch fraction.** Of the BLOCKING findings that survive synthesis, the fraction caught by *exactly one* lineage. High = the pool's diversity is load-bearing (a less diverse pool would have missed those findings). The cleanest single decorrelation signal.
- **M2 — Drop-one non-redundancy.** For each reviewer lineage, how many surviving BLOCKING findings are lost if that lineage is removed and no other lineage caught them. A lineage that loses ≥1 unique BLOCKING when dropped is *non-redundant*. Counts how many of the pool's lineages are pulling unique weight.
- **M3 — Challenge rate.** Fraction of findings (and of overall verdicts) that are non-affirming. The [Adversarial Review Protocol](../agent/process/adversarial-review-protocol.md) rewards challenge; a pool that mostly affirms is suspect (either the artifact is excellent or the pool is correlated/sycophantic — M1/M2 disambiguate).
- **M4 — Lineage-diversity index (structural, pre-hoc).** Count and spread of distinct vendors / model families / (eventually) training-corpus and institutional axes across the pool, with an honest discount for shared environment and shared training paradigm.

### Family 2 — validity-vs-reliability separation (the deeper worry)

- **M5 — False-pass rate.** Fraction of harness-passed artifacts that later fail external human/practitioner review or the [historical backtest](../agent/process/historical-parallel-test-protocol.md#strategic-tier-backtest-the-projects-core-bench-analog). The honest proxy for *validity* (reliability is cheap; validity needs ground truth, so track downstream failures). This is the [Civic-Bench](civic-bench-design-memo.md) discipline.

### Family 3 — capture / Goodhart detection

- **M6 — Harness-pass vs. external-pass divergence over time.** If harness-pass rate climbs while external-review-pass rate does not, the project is optimizing to beat its own test. An early-warning gauge for the [harness §7.3](../agent/process/cross-lineage-review-harness-protocol.md#7-honest-limits) Goodhart risk.

---

## 3. Triage — what is runnable now vs. what needs instrumentation

| Metric | Runnable on Run 001? | Why / what it needs |
| --- | --- | --- |
| **M1 — single-lineage-catch fraction** | **Yes (approximate)** | The consolidated BLOCKING list + convergence notes give per-finding lineage attribution. |
| **M2 — drop-one non-redundancy** | **Yes (approximate)** | Same attribution data; computed by removal. |
| **M3 — challenge rate** | **Yes** | Per-role severity tallies are recorded in the run log. |
| **M4 — lineage-diversity index** | **Yes (structural)** | The role→lineage table is explicit. |
| **M1/M2 — *true* (not approximate)** | **No** | Needs a **per-issue × per-lineage detection matrix** logged at run time, not reconstructed from a consolidated list. |
| **Joint-miss rate (true)** | **No** | Needs a **pre-registered, held-out ground-truth defect set**. Run 001's flaws were reviewer-discovered, so "all flaws" = union-of-found, which forces joint-miss ≈ 0 by construction (§5.3). |
| **M5 — false-pass rate** | **No** | Needs longitudinal external-review history the project does not yet have. |
| **M6 — harness/external divergence** | **No** | Same — needs a track record of multiple artifacts through both gates. |

The honest split: **the Family-1 structural/decorrelation metrics are computable now; the Family-2/3 validity metrics need time and instrumentation.** That is itself the finding — the project can measure *whether its reviewers are independent* today, but can only measure *whether independence yields truth* after building a longitudinal record.

---

## 4. Worked application — scoring Pipeline Run 001

Source data: [Pipeline Run 001 §1, §5](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md). Author lineage = Anthropic/Claude. Four blind reviewers: OpenAI (measurement skeptic), xAI (adversary), Google (ethics; also non-author synthesizer), Moonshot (verifier). Five consolidated BLOCKING findings B1–B5.

### 4.1 BLOCKING → lineage attribution (reconstructed from §5.1–§5.3)

| Finding | Lead lineage(s) | Caught by >1 lineage? |
| --- | --- | --- |
| **B1** F3↔ethics contradiction | xAI ("F3 can't trip") + Google ("enforce manufactured-crisis ban") | Yes (2) |
| **B2** objective-washing / status confound | OpenAI + Google (xAI "hollow ecological guard" partial) | Yes (2–3) |
| **B3** Rung-0 circularity + preemptive exit + no numeric cutoffs | xAI (preemptive-exit also Google) | Mostly single (xAI) |
| **B4** consent illusion (leader opt-in ≠ member consent) | Google (ethics) | No (1) |
| **B5** Edmondson overstretch + miscitation | Moonshot (verifier) | No (1) |

*Caveat: this is reconstructed from the consolidated list and the convergence/divergence sections, not from a per-issue matrix logged at run time. The numbers below are therefore approximate and are the strongest argument for the §5 instrumentation.*

### 4.2 Computed metrics

- **M1 — single-lineage-catch fraction = 3/5 (60%).** B3, B4, B5 were each caught by essentially one lineage. **Headline: a majority of the blocking findings would likely have been missed by a less diverse pool.** This is the quantified version of Run 001's "five BLOCKING the same-lineage author missed."
- **M2 — drop-one non-redundancy = 3 of 4 reviewer lineages non-redundant.**
  - Drop **xAI** → lose B3 (unique) and break B1 (the contradiction needs the "F3 can't trip" half). *Non-redundant.*
  - Drop **Google** → lose B4 (unique) and the ethics half of B1. *Non-redundant.*
  - Drop **Moonshot** → lose B5 (unique citation-fidelity catch). *Non-redundant.*
  - Drop **OpenAI** → B2 survives via Google; OpenAI's unique value sat at the MAJOR tier (4 MAJOR), not BLOCKING. *Redundant for BLOCKING; non-redundant at MAJOR.*
  - Reading: decorrelation paid off heaviest through the **adversary, ethics, and verifier** roles; the skeptic added depth (MAJOR) more than unique blocking. A useful, non-obvious result — diversity value is *role-dependent*, not uniform.
- **M3 — challenge rate.** Verdict-level **4/4 (100%)** reviewers non-affirming. Finding-level **26/31 (≈84%)** non-affirming (affirming: skeptic 1, adversary 0, ethics 1, verifier 3). High challenge rate, and M1/M2 confirm it is *substantive* challenge, not noise.
- **M4 — lineage-diversity index.** 5 distinct lineages (Anthropic author + OpenAI + xAI + Google + Moonshot); adversary blind; synthesizer non-author. **Honest discount:** all four reviewers ran in one Cursor environment and share the broad LLM training paradigm — so structural diversity (high) **overstates** epistemic decorrelation ([harness §7.1, §7.5](../agent/process/cross-lineage-review-harness-protocol.md#7-honest-limits)). A practitioner in the field would be more decorrelated from all four than they are from each other.

### 4.3 What the scoring shows

The Family-1 numbers corroborate the decorrelation claim **at model scale and n=1**: 60% single-lineage catches and 3-of-4 non-redundant lineages mean the pool's diversity did real work, not decorative work. They do **not** show the review was *correct* (that is M5, uncomputable yet), and they do **not** transfer to human institutions (the [governance-primitive riff §4](../agent/explorations/decorrelation-civic-governance-primitive-riff.md) gating risk).

---

## 5. Making it runnable going forward — Stage-0 instrumentation

To move from "reconstructed approximation" to "measured," a future [harness](../agent/process/cross-lineage-review-harness-protocol.md) run adds three cheap instruments at Stage 0 (none require model calls beyond the run itself):

1. **Per-issue × per-lineage detection matrix.** Each reviewer's findings are logged with a stable issue ID at submission; the synthesizer records, per consolidated finding, *which lineages independently raised it*. This makes M1/M2 exact and yields a true **marginal-catch curve** (issues vs. lineages-added).
2. **Seeded-defect calibration run (periodic).** Plant N pre-registered, known flaws in a target artifact (frozen at Stage 0, hidden from reviewers) and measure detection per lineage. This is the only way to compute a true **joint-miss rate** (fraction of seeded defects missed by *every* lineage) — the metric Run 001 structurally cannot produce.
3. **Longitudinal pass-tracking ledger.** Record every harness-passed artifact and its later disposition under external/practitioner review or historical backtest. Over time this yields **M5 (false-pass rate)** and **M6 (harness/external divergence)**.

Instruments 1 is a logging change (adopt now); 2 is an occasional calibration exercise; 3 is a standing ledger. Together they make the harness **self-measuring** — the missing feedback loop the [verifier memo](agent-automation-and-the-verifier-memo.md) says the project needs to know whether its judgment is improving rather than guessing.

---

## 6. Honest limits

- **n = 1, agent-scale, reconstructed.** §4 scores a single run, at model scale, from a consolidated list rather than a per-issue matrix. Suggestive, not established.
- **Decorrelation ≠ validity.** Every Family-1 metric measures *independence of error*, not *correctness*. A perfectly decorrelated pool can be confidently, independently wrong about a value-contested civic claim ([verifier memo §6](agent-automation-and-the-verifier-memo.md): the strategic/normative tier has no cheap verifier).
- **Structural diversity overstates epistemic diversity (M4).** Shared training paradigm and shared environment mean the index is an upper bound on real decorrelation.
- **The institutional jump is unsolved.** These metrics are defined for *model-lineage* pools. Measuring correlation between *human institutions* (shared formation, incentives, information diet) is the open problem the [governance-primitive riff](../agent/explorations/decorrelation-civic-governance-primitive-riff.md) flags; nothing here solves it.
- **Self-reference (Rung-0).** A metrics memo arguing the harness works, reviewed *by* the harness, is partially circular — the same [Rung-0 firewall](../agent/process/cross-lineage-review-harness-protocol.md#7-honest-limits) Run 001's own adversary flagged. Route it cross-lineage anyway, and look hardest for the result that cuts against.
- **Goodhart on the metrics themselves.** Once decorrelation is a number, the project could optimize the *number* (assemble maximally diverse-looking pools) over the *thing* (genuinely independent judgment). M5/M6 are the partial guard; they only work once the longitudinal ledger exists.

---

## 7. Routing and open questions

**Routing.** Working claim. Run through the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) (blind, independent-lineage), accepting the §6 self-reference caveat, before any promotion. Instrument 5.1 (the detection matrix) is adoptable immediately as a harness logging change regardless of this memo's promotion status.

**Open questions.**

1. **Is single-lineage-catch fraction (M1) the right headline, or does it reward over-diverse pools that miss obvious things?** A pool can be so decorrelated it shares no *competence*, not just no bias.
2. **What is a good *target* for M1/M3?** A 100% single-lineage-catch fraction would mean zero corroboration; 0% would mean full redundancy. The useful range is unknown.
3. **Do the model-scale metrics transfer to institutions at all?** The gating question shared with the [governance-primitive riff](../agent/explorations/decorrelation-civic-governance-primitive-riff.md).
4. **Can a seeded-defect run be designed without training the project to find *that kind* of defect?** Calibration sets leak into the thing they measure.

---

## Provenance and register

`collaborative` — human-directed AI drafting; steward synthesis and approval pending. Working-claim register: named uncertainty, no promotion, no rhetorical flourish. Member of the verifier cluster alongside the [agent-automation memo](agent-automation-and-the-verifier-memo.md), the [Civic-Bench design memo](civic-bench-design-memo.md), and the [harness protocol](../agent/process/cross-lineage-review-harness-protocol.md). Not registered in [`_EXCHANGE_INDEX.md`](../agent/exchanges/_EXCHANGE_INDEX.md); it is a memo.
