---
name: cross-lineage-decorrelation-check
description: Spins up independent-lineage subagents (blind, parallel, reduced context) to adversarially pressure-test the claim or recommendation currently on the table, then synthesizes a detection matrix and a steward-facing verdict. The on-demand, in-chat escalation from the epistemic-honesty rule's passive check — a stronger but still partial (and itself untested) mitigation, not a fix; see Honest limits. Use when the user asks to decorrelate, red-team, cross-lineage check, stress-test, "run the rule's check", or "spin up the subagents" on a current claim, or before treating a single-lineage claim as settled.
---

# Cross-Lineage Decorrelation Check

The [epistemic-honesty rule](../../.cursor/rules/epistemic-honesty-default.mdc) is the passive mitigation; this skill is the active one — a **stronger but still partial mitigation, not a fix**. It is a fast, in-chat version of the [Cross-Lineage Review Harness Protocol](../../agent/process/cross-lineage-review-harness-protocol.md). For anything headed into a core document, a Principle, doctrine, or a public artifact, escalate to the **full harness with a frozen, registered pre-registration file** — this skill is the cheap check, not the formal one.

## The load-bearing weakness (read this first)

This skill's structural flaw is that the **author lineage (Claude) selects the assertions and writes the synthesis** — the same lineage the skill calls too correlated to catch its own errors owns the framing and the merge. A blind panel run "in a cage the author built" can be quietly defused at the assertion-selection or synthesis step. This is not a footnote; it is the most likely way the skill becomes *theater* (an after-the-fact credential — "it survived a 4-family panel" — rather than real quality control). Mitigate every run by: (1) handing the steward the **raw critiques**, not only the synthesis; (2) **labeling the synthesis author-side** when Claude does the merge; and (3) for any consequential claim, spawning a **non-author lineage as the synthesizer** and escalating to the full pre-registered harness. The skill's own value claim was cross-lineage-checked on June 26, 2026 and did **not** survive as stated (see Honest limits).

## When to run / when to skip

- **Run** when a single-lineage (Claude) claim is about to shape a decision, or the user invokes it ("decorrelate this", "red-team that", "spin up the subagents"). Treat the invocation as the steward's **GO**.
- **Skip** for trivial/mechanical work, and don't run it on *every* message — over-running it trains toward defensible-looking work over correct work (Goodhart). It is for substantive claims.

## Workflow

```
- [ ] 1. Freeze the target (assertions + panel) and show it
- [ ] 2. Spawn the panel BLIND + PARALLEL via the Task tool
- [ ] 3. Collect critiques
- [ ] 4. Synthesize: detection matrix + convergence + open divergence + revise-list
- [ ] 5. Hand the verdict to the steward (agents propose, steward disposes)
```

### Step 1 — Freeze the target

Restate the live claim as **3–6 falsifiable assertions** (Option B framing — assertions to break, not a conversation to join). Show them plus the panel in a compact freeze block so the steward can see what is being tested before subagents spawn. If the claim is ambiguous, confirm the assertions in one line before spawning. Once shown, the assertions are immutable for the run.

### Step 2 — Spawn the panel (blind, parallel, reduced context)

Spawn each reviewer with the **Task tool**, `subagent_type: generalPurpose`, `readonly: true`, and an explicit `model` slug. Put **all Task calls in one message** so they run as one parallel batch. Each subagent gets **only** its role prompt + the assertions (+ minimal named context) — **not this chat, not each other's output**.

**Hard rules** (from [harness §3](../../agent/process/cross-lineage-review-harness-protocol.md)): every judgment role is a **different family from Claude** and, where possible, from each other; the **adversary is blind** (assertions only); **rotate the adversary family across runs** so no lineage's bias becomes structural. The harness also requires a **non-author synthesizer**; this lightweight skill *relaxes* that to author-side synthesis for quick checks only — flagged as the load-bearing weakness above — and reinstates it (non-author synthesizer) for any consequential claim.

**Models available for subagents** (pass as the `model` slug): independent lineages for judgment roles — `gemini-3.1-pro` (Google), `gpt-5.5-medium` / `gpt-5.4-medium` (OpenAI), `grok-4.3` (xAI), `kimi-k2.5` (Moonshot). Coding-specialized (`gpt-5.3-codex`, `grok-build-0.1`) and Cursor's own (`composer-2.5`) exist but are weaker fits for civic/analytical judgment. Author lineage is Claude (this chat) — never a judgment role.

**Default panel (3–4 reviewers; scale down to 2 for a quick check):**

| Role | Default lineage | Context |
| --- | --- | --- |
| Domain skeptic (hostile expert in the relevant field) | `gemini-3.1-pro` | assertions + the one relevant section/definition (Opt A) |
| Verifier / empiricist (source fidelity + "is this testable?") | `gpt-5.5-medium` | assertions + any cited sources |
| Adversary / falsifier-hunter **[blind]** | rotate (`kimi-k2.5` ↔ `grok-4.3`) | assertions only (Opt B) |
| Second domain lens (optional) | the family not yet used | assertions + relevant section |

The **synthesizer** may be run by *you* (this chat) as bookkeeping over the returned critiques **for a quick check only** — but author-side synthesis is the skill's load-bearing weakness (see above), so **label it author-side** and, for any consequential claim, **spawn a non-author lineage as the synthesizer** instead.

### Role-prompt templates (adapt the bracketed parts)

**Domain skeptic** — "You are a hostile [domain] expert reviewing assertions drafted for a civic-design project. Attack the substance, do not extend it. For each assertion: rate severity (BLOCKING/MAJOR/MINOR/AFFIRMING), name the single most likely error, say whether it already anticipates your objection, and cite your sharpest source. End with the one change that would most improve it. Agreement is not your goal."

**Verifier / empiricist** — "Check only (a) whether each cited source faithfully supports its claim and (b) whether each assertion is actually testable / supportable by the balanced literature (cite both sides). Flag every overclaim. Output a table: assertion → strongest FOR → strongest AGAINST → supported/contested/under-determined → note."

**Adversary [blind]** — "The following are assertions that claim to be well-founded. Break that claim. Find every place a committed defender could always declare success; attack the weakest load-bearing assertion as forcefully as the evidence allows. Be the prosecution, not balanced. For each: operationalized enough to be falsified? (yes/no), how a defender dodges a NO, and severity. End with the single strongest reason to discard the whole set."

### Step 3–4 — Collect and synthesize

Build, from the returned critiques:
- a **per-assertion × per-lineage detection matrix** (severity per cell);
- **convergence** (findings ≥2 *independent* lineages raised on their own — the strong signal);
- **divergence**, left **OPEN** (do not majority-vote, do not smooth away);
- a severity-ranked **consolidated revise-list**.

### Codebook

- Severity: `BLOCKING` (unfalsifiable / fails its own test / a load-bearing claim is wrong / adds nothing over existing frames) · `MAJOR` · `MINOR` · `AFFIRMING`.
- **"Survives" = no BLOCKING stands** after synthesis — it does **not** mean "true."
- **Convergence is not the metric; surviving the adversary is.** Author-anticipated convergence is a *weak* signal.

### Step 5 — Hand to the steward

Present the matrix + verdict + a recommended disposition. **Agents propose; the steward disposes. Nothing is promoted.** If the target is exchange/memo/doc-bound, offer to record results per the [harness output form](../../agent/process/cross-lineage-review-harness-protocol.md) and register per the [civic-blueprint-exchange skill](../civic-blueprint-exchange/SKILL.md).

## What would actually measure this (the promotion test)

This skill is currently a **mitigation, not a measured intervention** — its value claim is unverified. Promoting "reduces overclaim risk" from plausible to *measured* requires a pre-registered experiment, not more single runs. The minimal design (surfaced by the June 26, 2026 cross-lineage run that judged the skill's own value claim):

- **Corpus:** 30–50 claims with a known mix of clean assertions and **injected, subtle overclaims**; ground truth set by two blinded domain reviewers with adjudication.
- **Four arms**, holding reviewer count and adversarial framing constant so only *lineage diversity* varies: (1) solo Claude, (2) 4× Claude (different seeds/temps, same prompt), (3) 4× adversarially-prompted Claude, (4) the 4-family cross-lineage panel. Randomize the **synthesizer** too (author vs. blinded independent).
- **Primary metric:** sensitivity (fraction of injected overclaims caught as BLOCKING/MAJOR) and false-positive rate on clean claims; **secondary:** inter-rater reliability (quadratic-weighted κ), net issues after synthesis.
- **The claim only earns "decorrelation works"** if arm (4) beats arms (2)/(3) on injected-overclaim sensitivity — otherwise the benefit is reviewer-count + adversarial framing, not lineage independence.

Until that (or an equivalent) is run, describe outputs as *"a candidate mitigation that surfaced X"*, never as a measured risk reduction. Do **not** cite raw cross-run "N blocking findings" counts as evidence — severity labels are not comparable across model families.

## Honest limits (state them in the result)

All these models share training data and RLHF profiles, so cross-lineage agreement reduces common-mode failure but does **not** establish truth (reliability ≠ validity); subagents share one Cursor orchestration environment, not separate vendor stacks; the author lineage still frames and (often) synthesizes (see "The load-bearing weakness"); and this is **not** a substitute for external human review. It is mitigation, not cure.

**Provenance.** On June 26, 2026 this skill was run on its own value claim — *"an on-demand cross-lineage skill measurably reduces overclaim risk."* A blind 4-family panel (Gemini, GPT-5.5, Kimi, Grok) returned **zero AFFIRMING** verdicts: the claim *as worded* does not survive (no operational metric for "overclaim risk"; "decorrelation" confounded with reviewer-count + adversarial framing absent a 4×Claude control; author-side framing/synthesis reintroduces the bias; n=1 + Goodhart risk). What survived is the weaker, honest claim now reflected above: *a cheap, testable mitigation that plausibly reduces some correlated-review failure modes, currently unmeasured.*
