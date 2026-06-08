---
description: A repeatable harness for subjecting any project artifact (exchange claim-set, memo, proposal, doctrine candidate) to blind, independent-model-lineage adversarial review via parallel subagents. Generalizes the bespoke Pipeline Run 001 into a reusable process, and resolves the long-parked ROADMAP Thread C ("Red Team Run"). Operationalizes Adversarial Review Protocol Options A+C+D plus the Comparative Alignment Protocol's convergence/divergence logging, under a hard steward-freeze and human go/no-go.
provenance: collaborative
status: Proposed (June 2026) — fifth sibling to Adversarial Review, Coherence Audit, Historical Parallel Test, and Comparative Alignment; first concrete instance already run as Pipeline Run 001
---

# Cross-Lineage Review Harness Protocol

> **Status:** Proposed (June 2026). Generalizes the bespoke [Develop-Leg Pipeline Run 001](../exchanges/discovery-principle-develop-leg-pipeline-run-001.md) and the orchestration sketch in the [S17 test-design memo §7.5](../exchanges/discovery-principle-develop-leg-test-design-memo.md#75-buildable-orchestration--endpoints-manifest-run-staging) into a **reusable** process applicable to any project artifact. It **resolves [ROADMAP Thread C ("Red Team Run")](../../ROADMAP.md) and decision C1**, which asked for "a protocol extension that breaks out of steward-context convergence bias within the AI pipeline … a fourth sibling to Adversarial / Coherence / Historical-Parallel." It is the operational instrument the [Agent Automation and the Verifier memo](../../memos/agent-automation-and-the-verifier-memo.md) calls the project's proxy verifier for the **adversarial-robustness tier** — the civic-domain analog of running a test suite.

---

## The problem this protocol addresses

The project's analytical output is produced predominantly by AI agents in a single model lineage (the steward's working assistant). The [README](../../README.md) names the resulting risks honestly — convergence, shared framing, false confidence — and the [Adversarial Review Protocol](adversarial-review-protocol.md) counteracts them by *challenging* claims. But adversarial review run **in the authoring lineage** shares that lineage's priors and blind spots: it is **series-wired** in the [develop-leg](../exchanges/discovery-principle-develop-leg-exchange.md) sense (§2.5 correlated collapse / common-mode failure). Same-lineage review can rubber-stamp what an independent lineage would block — exactly what the [rolled-back in-lineage attempt at Exchange #27](../exchanges/discovery-principle-develop-leg-exchange.md#standing-items) did, and what [Pipeline Run 001](../exchanges/discovery-principle-develop-leg-pipeline-run-001.md) corrected when four independent lineages surfaced **five BLOCKING issues** the same-lineage author missed.

This protocol makes that correction **repeatable and cheap**. It is the difference between adversarial-*within*-context (the existing protocol's default) and adversarial-*across*-context (this one). It is mitigation, not cure: all frontier models share training data and tuning, so cross-lineage agreement reduces common-mode failure but does not establish external truth (see [§7](#7-honest-limits)).

---

## When to apply

**Always apply when:**

- An exchange produces a claim-set that will influence project direction, **before** the reserved adversarial round (this protocol *is* the reserved round's preferred form — independent-lineage, Option D).
- A memo makes a strategic claim about the project ([the verifier memo](../../memos/agent-automation-and-the-verifier-memo.md) routes itself here).
- A doctrine candidate is up for promotion (the [doctrine gate](../doctrine/_DOCTRINE_INDEX.md) requires a post-adversarial v2).

**Consider applying when:**

- A proposal reaches "working hypothesis" confidence and is headed for public release.
- A coherence audit or historical-parallel section introduces material that could carry hidden convergence.

**Skip when:**

- The artifact is still speculative and being explored, not advocated (run it as a riff first).
- The work is mechanical (formatting, link-fixing) with no judgment content.

---

## Protocol

### 1. Trigger and target

A steward (or an agent at steward direction) names one **target artifact** and the **claims or design within it to be tested**. The target can be any of: an exchange claim-set (S-claims, M-claims, etc.), a memo, a proposal, a doctrine candidate, or a protocol draft. The harness does not test "the world"; it tests *whether the artifact survives decorrelated scrutiny*.

### 2. Stage 0 — pre-register and freeze (human, irreducible)

Before any subagent is spawned, the steward freezes a **pre-registration file** (see [Output](#output)) containing:

- the **target** and the specific claims/falsifiers under review;
- the **role → lineage assignment** (§3);
- the **role prompts** (§4);
- the **codebook** (§5);
- a confirmation of what the run **is not** (e.g., "non-evidence for hypothesis X" when the target instantiates a hypothesis — the [Rung-0 firewall](../exchanges/discovery-principle-develop-leg-test-design-memo.md#71-the-instrument--subject-firewall)).

**The adversarial pass is never auto-run.** Per the [Adversarial Review Protocol §2 default](adversarial-review-protocol.md) and the [civic-blueprint-exchange skill](../../.cursor/skills/civic-blueprint-exchange/SKILL.md), it runs only on an explicit steward **GO**, and it runs **cross-lineage**, never in the authoring lineage. Once frozen, the role prompts, codebook, and any pre-registered falsifier set are **immutable** for the run.

### 3. Role → lineage assignment

Assign by **role-class, not by favorite model**. The hard rules:

- the **author/designer** lineage is whatever produced the target;
- every **judgment role is a different lineage from the author and, where budget allows, from each other**;
- the **adversary is independent-lineage and blind**;
- the **verifier is a different lineage from the author**;
- the **synthesizer is not the author lineage** (rotate / least-involved);
- the **steward is a human and an irreducible non-agent node**.

| Role | Job | Lineage rule | Context policy |
| --- | --- | --- | --- |
| Author / designer | Produced the target (already exists) | any single | full |
| Domain skeptic | Attack the substance through a hostile domain lens (Option C) | ≠ author | reduced (Option A) — claims + relevant section only |
| Adversary / falsifier-hunter | Break the claim of falsifiability; find where it cannot return NO | ≠ author, **blind** | reduced + **claims-as-assertions** (Option B) |
| Ethics / guardrail monitor | Harm, consent, capture, the mirror-machine risk | diversity helps | reduced — design + ethics lens |
| Verifier | Citation/source fidelity per [Research Protocol §4](research-protocol.md) | ≠ author | sources + claims only |
| Synthesizer | Merge critiques; log convergence **and** divergence | rotate / non-author | all critiques + divergence |
| Steward | Set falsifiers; own go/no-go and the ethics call | **human** | everything |

Rotate the family↔role assignment across runs so no single lineage's bias becomes structural. Reserve multi-lineage cost for the **judgment** roles only; mechanical steps (scoring to a frozen rubric, hashing, logging, divergence-diffing) are plain scripts, not model calls.

### 4. Role prompts

Each subagent receives **only** its named documents and its role prompt — **not the working chat, not each other's output**. Independence is enforced by spawning them in **one parallel batch**. Prompts adapt the [Run 001 §2](../exchanges/discovery-principle-develop-leg-pipeline-run-001.md) templates to the target. The invariant instructions:

- **Domain skeptic** — "You are a hostile [domain] expert. Attack the substance. For each load-bearing claim, rate it and name the most likely error. State plainly whether the artifact already answers your objection."
- **Adversary** — "The following are *assertions* that claim to be well-founded. Break that claim. Find every place a committed defender could always declare success; attack the weakest load-bearing claim as forcefully as the evidence allows. Be the prosecution, not balanced."
- **Ethics monitor** — "Where could this harm people or recreate the [machine](../explorations/discovery-principle-moral-architecture-riff.md) it critiques? Where are consent, agency, and power-legibility thin? List anything that should STOP the work, ranked by severity."
- **Verifier** — "Check only fidelity of source-to-claim. Flag every overclaim, misattribution, or use beyond scope. Output a table: claim → cited source → faithful? → note."
- **Synthesizer** — "Merge the critiques. Record convergence vs. divergence; do NOT smooth conflict away. Produce a severity-ranked revise-list, the open disagreements, and a recommended go/no-go for the steward."

### 5. Codebook — what a finding is, and what "survives" means

- **Severity:** `BLOCKING` (the artifact is unfalsifiable, unethical, factually unsound, or fails its own test) · `MAJOR` (a real hole that weakens but does not void) · `MINOR` (fix-on-revision) · `AFFIRMING` (holds up).
- **"Survives" ≠ "true."** Survives = **no BLOCKING finding stands** after synthesis. A BLOCKING finding sends the target back to a **bounded revise-loop**, not to the grave.
- **Convergence is not the success metric — surviving the adversary is.** Reviewer disagreement is *recorded and preserved*, not resolved by majority vote ([Comparative Alignment Protocol](comparative-alignment-protocol.md)). Where independent lineages converge on an attack, that is the strong signal; where the author *anticipated* an attack, convergence on it is a *weak* signal.

### 6. Run staging

```
[0 pre-register + freeze] ──human GO──▶ [1 author target exists]
        │  (roles, prompts, codebook, falsifiers locked)
        ▼
[2 blind review ∥]  skeptic(A+C) · adversary(A+B+D, blind) · ethics(A) · verifier   ← reduced context, independent lineages
        │
        ▼
[3 synthesize: keep divergence]  (non-author lineage)
        │
        ▼
[4 human go/no-go]  ── REVISE (bounded loop to author) ── or ── FREEZE/route
        ▲___________________ bounded revise-loop ___________________│
```

- **Stage 1** — the target already exists (the author lineage produced it).
- **Stage 2** — judgment roles run in parallel, reduced context, independent lineages, blind to each other → structured critiques.
- **Stage 3** — a non-author synthesizer merges and **preserves divergence**.
- **Stage 4** — the steward reviews the synthesis + divergence, confirms any pre-registered falsifiers are unmoved, and decides revise (bounded loop) or freeze/route. **Agents propose; the steward disposes.**

### Output

A **pre-registration file**, frozen at Stage 0 and appended with results after the run — the form [Pipeline Run 001](../exchanges/discovery-principle-develop-leg-pipeline-run-001.md) demonstrates. It contains: role→lineage table, role prompts, codebook, the run log (per-role verdict + severity tally), a convergence section (2+ lineages independently), a **divergence section left open** (not majority-voted), the consolidated severity-ranked revise-list, and the steward go/no-go with reasoning. Like the develop-leg companions, harness run files are **not** registered in [`_EXCHANGE_INDEX.md`](../exchanges/_EXCHANGE_INDEX.md); they are working companions to the artifact under review and live beside it.

---

## 7. Honest limits

1. **Mitigation, not cure.** All frontier lineages share training data and RLHF profiles; cross-lineage decorrelation is partial. Claude-vs-GPT-vs-Gemini-vs-Grok is closer to itself than any of them is to a practitioner in Mumbai. **Reliability is not validity.**
2. **Survival ≠ truth.** The harness verifies *defensibility under decorrelated scrutiny*, a proxy for the [tier-3 "adversarial robustness"](../../memos/agent-automation-and-the-verifier-memo.md) signal — not the ground-truth, polity-over-years verifier the strategic tier needs.
3. **Goodhart.** Optimizing artifacts to pass the harness can train the project to produce *defensible-looking* work over *correct* work. The adversary-survival (not convergence) metric and the preserved-divergence rule are partial guards; pairing with the [Civic-Bench](../../memos/civic-bench-design-memo.md) and human review is the offset.
4. **Self-scoring circularity.** When the target *instantiates* the mechanism being tested (e.g., the harness reviewing a memo *about* cross-lineage review), the run is **non-evidence** for that mechanism and must be labeled so at Stage 0 — the [Rung-0 firewall](../exchanges/discovery-principle-develop-leg-test-design-memo.md#71-the-instrument--subject-firewall). Run 001's own adversary flagged this; the discipline is to look hardest for the result that cuts *against*.
5. **Subagent environment.** Cursor subagents are genuinely different model families but share one orchestration environment, not separate vendor stacks end-to-end.

---

## What this protocol does not do

- It does not establish that a claim is **true** — only that it survived independent-lineage scrutiny.
- It does not replace **external human review** ([Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md)); models cannot supply the practitioner's tacit knowledge or the missing standpoint.
- It does not **promote** anything. Promotion is a separate steward decision under the relevant gate (principle, doctrine, or public artifact).

---

## Relationship to other protocols

- **Adversarial Review Protocol:** This is the operational, independent-lineage realization of that protocol's reserved adversarial round (Options A + C + D). Use the harness when the adversarial round should run cross-lineage — which is the default for any direction-influencing claim.
- **Comparative Alignment Protocol:** Supplies the convergence/divergence logging the synthesizer uses; the harness is a standing application of it across model lineages.
- **Research Protocol:** Governs the verifier role's source-fidelity check (§4 W8 discipline) and the re-derivation of any evidence base rather than inheriting it.
- **Coherence Audit Protocol:** A harness run can feed the audit (new revise-lists are new content); the audit's scope already includes [`agent/process/**`](.) and memos.
- **Historical Parallel Test Protocol:** Complementary verifier for a different tier — the harness tests *internal* robustness; the [historical backtest](historical-parallel-test-protocol.md#strategic-tier-backtest-the-projects-core-bench-analog) tests *strategic* claims against the record.

---

## Relationship to project principles

- **Principle 3 (AI must augment agency, not replace democratic accountability):** The harness keeps the human as the irreducible go/no-go node; agents propose, the steward disposes. Automating *review* is licensed; automating *the decision* is not.
- **Principle 4 (Power must remain accountable, legible, and reversible):** Every prompt, output, and pinned model version is logged in an auditable run file; the falsifier set is frozen and immutable; the revise-loop is bounded and visible.
- **Principle 10 (The future should be built in the open):** The run file is a working artifact in-repo, divergence preserved rather than smoothed.
- **The reflexive guardrail ([riff §8](../explorations/discovery-principle-moral-architecture-riff.md) / exchange S21):** The harness is the project's parallel-not-series antibody — *only* parallel if it stays independent-lineage, blind, and challenge-rewarded. A single-lineage harness would be the machine; that is why §3's lineage rules are not optional.
