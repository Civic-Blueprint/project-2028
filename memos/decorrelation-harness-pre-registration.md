---
title: "Cross-Lineage Harness — Stage-0 Pre-Registration (decorrelation memo pair)"
description: Stage-0 pre-registration freezing a cross-lineage harness run on the two decorrelation memos — the Decorrelation Metrics memo and the Decorrelation as a First-Class Requirement for Independent AI Evaluation (Path B) memo — before any subagent is spawned. Both memos route themselves to the harness before promotion / external use; this is that routing operationalized. Carries the Rung-0 self-reference firewall (a memo arguing the harness works, reviewed by the harness). Frozen by the steward before GO; results appended after the run. Prepared June 14, 2026.
provenance: collaborative
status: Stage-0 pre-registration (prepared June 14, 2026) — FROZEN-PENDING; awaiting steward GO. NON-PROMOTION; the run hardens the memos, it does not adopt them.
created: 2026-06-14
governing_protocols:
  - ../agent/process/cross-lineage-review-harness-protocol.md
  - ../agent/process/adversarial-review-protocol.md
  - ../agent/process/research-protocol.md
parent_artifacts:
  - decorrelation-metrics-memo.md
  - decorrelation-independent-ai-evaluation-memo.md
---

# Cross-Lineage Harness — Stage-0 Pre-Registration (decorrelation memo pair)

> **Targets (dual — a noted deviation from [harness §1](../agent/process/cross-lineage-review-harness-protocol.md)'s single-target default):** the [Decorrelation Metrics memo](decorrelation-metrics-memo.md) and the Path B [Decorrelation as a First-Class Requirement for Independent AI Evaluation memo](decorrelation-independent-ai-evaluation-memo.md). They are reviewed in one batch because the position memo's measurement backing *is* the metrics memo; splitting them would force the position-memo reviewers to evaluate an uncited instrument. Each memo's own §6 routes it here before promotion / external use.
>
> **Frozen by the steward before any subagent is spawned (Stage 0).** Per the [ARP §2 default](../agent/process/adversarial-review-protocol.md), the adversarial pass is **never auto-run** — only on an explicit steward **GO**, cross-lineage, never in the authoring lineage (Anthropic/Claude authored both memos).

---

## 0. The Rung-0 self-reference firewall (read first)

This run is **partially circular by construction**: a harness run that reviews a memo *arguing the harness's decorrelation discipline works* cannot be clean evidence *for* that discipline — the same firewall [Pipeline Run 001](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md) flagged when its own adversary called the Rung-0 move self-serving. Therefore:

- This run is **non-evidence** for the claim "decorrelation improves evaluation." It tests only whether the two memos are **internally sound, faithfully cited, and survive decorrelated scrutiny** — not whether their thesis is true.
- The discipline is to **look hardest for the result that cuts against the memos** (e.g., that the Run 001 scoring is too thin to support the metrics; that "decorrelation as a first-class requirement" over-reaches; that the position memo legitimates the Anthropic frame it should hold at arm's length).
- Promotion / external use remains a separate steward decision after the run; surviving this run is necessary, not sufficient.

---

## 1. Role → lineage assignment

Author lineage = Anthropic/Claude. Every judgment role is a different lineage; the adversary is blind. One parallel batch of Cursor subagents; each given only its named documents + role prompt.

| Role | Lineage (subagent) | Context (reduced — Opt A) | Job |
| --- | --- | --- | --- |
| Evaluation-methodology skeptic | **OpenAI — `gpt-5.5-medium`** | metrics memo §2–§5 + the Run 001 scoring | Attack the metrics' validity: do M1/M2 reward over-diverse pools? is the 60% single-lineage-catch figure an artifact of reconstruction-not-measurement? |
| Adversary / falsifier-hunter **[blind]** | **xAI — `grok-4.3`** | both memos' core claims framed as assertions (Opt B) | Break "decorrelation as a first-class requirement" and "the project can credibly say this"; find where a defender could always declare success |
| Ethics / capture monitor | **Google — `gemini-3.1-pro`** | position memo §4–§6 + the [contribution-surface riff §4.3](../agent/explorations/anthropic-framework-contribution-surface-riff.md) | Does engaging Anthropic's frame legitimate it / risk the capture the memo warns of? Is the scale-asymmetry honest or presumptuous? |
| Verifier — citation fidelity | **Moonshot — `kimi-k2.5`** | both memos + the [framework digest](../sources/source-anthropic-advanced-ai-framework-digest.md), [verifier memo](agent-automation-and-the-verifier-memo.md), [Run 001](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md), [harness protocol](../agent/process/cross-lineage-review-harness-protocol.md) | Check every quote of the Anthropic framework and every internal citation for faithfulness; flag overclaim/misattribution |
| Synthesizer | **OpenAI — `gpt-5.5-medium`** (non-author; doubles the methodology-skeptic critique — treat at arm's length per [Run 001 §6.1](../agent/exchanges/discovery-principle-develop-leg-pipeline-run-001.md)) | all four critiques + divergence | Merge; preserve divergence; severity-ranked revise-list + go/no-go |

---

## 2. Codebook

- **Severity:** `BLOCKING` (a memo is internally unsound, materially misquotes the framework, the metrics cannot bear the weight placed on them, or the position memo is captured-by-frame) · `MAJOR` (a real hole that weakens) · `MINOR` (fix-on-revision) · `AFFIRMING`.
- **"Survives" ≠ "the thesis is true"** (see §0). Survives = no BLOCKING stands after synthesis; a BLOCKING sends the relevant memo back to a bounded revise-loop.
- **Convergence is not the success metric — surviving the adversary is.** Preserve divergence; do not majority-vote.
- **Eat-own-dogfood check:** because the position memo argues *for* decorrelated review, this run is also a live demonstration; the synthesizer should note whether the run itself exhibited real decorrelation (log the per-issue × per-lineage detection matrix per the metrics memo §5 instrument it is reviewing — the cleanest possible test of the instrument is to run it on its own review).

---

## 3. Specific things each reviewer must return a verdict on

- **Metrics memo:** (a) is the Run 001 scoring honestly labeled as reconstructed-not-measured? (b) is the runnable-now / needs-instrumentation triage correct? (c) does M1 (single-lineage-catch fraction) have a defensible target range, or is it un-anchored (the memo's own OQ2)?
- **Position memo:** (d) is the financial-vs-epistemic-independence gap real, or does the full Anthropic framework already address it? (e) is the "credible on method, not domain depth" boundary held, or does the memo over-claim? (f) does §6 (self-application) actually bind, or is it decorative?

---

## 4. Stage-0 freeze checklist *(steward)*

- [ ] Both memos frozen at their current version (no edits after GO)
- [ ] Role → lineage assignment accepted (synthesizer ≠ author confirmed)
- [ ] Codebook + role prompts + the §3 verdict list locked
- [ ] Confirmed: **non-evidence** for the decorrelation thesis (Rung-0 firewall, §0); non-promotion
- [ ] **GO** (steward) — author may spawn the blind cross-lineage batch

*Frozen pending GO. Results — per-role verdict + severity tally, convergence (2+ lineages), open divergence, consolidated revise-list, the per-issue×per-lineage detection matrix, and the steward go/no-go — appended here after the run.*

---

## Provenance and register

`collaborative` — human-directed AI drafting; steward freeze + GO pending. Working companion to the two decorrelation memos; per the [harness Output spec](../agent/process/cross-lineage-review-harness-protocol.md), harness run files are **not** registered in [`_EXCHANGE_INDEX.md`](../agent/exchanges/_EXCHANGE_INDEX.md) — they live beside the artifact under review.
