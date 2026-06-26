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
- [ ] 2. Spawn the panel BLIND + PARALLEL, BALANCED STANCES, via the Task tool
- [ ] 3. Collect critiques
- [ ] 4. Synthesize: stance-labeled matrix + cross-stance convergence + open divergence + framing gaps + revise-list
- [ ] 5. Hand the verdict to the steward (agents propose, steward disposes)
```

### Step 1 — Freeze the target

Restate the live claim as **3–6 falsifiable assertions** (Option B framing — assertions to break, not a conversation to join). Show them plus the panel in a compact freeze block so the steward can see what is being tested before subagents spawn. If the claim is ambiguous, confirm the assertions in one line before spawning. Once shown, the assertions are immutable for the run.

### Step 2 — Spawn the panel (blind, parallel, reduced context)

Spawn each reviewer with the **Task tool**, `subagent_type: generalPurpose`, `readonly: true`, and an explicit `model` slug. Put **all Task calls in one message** so they run as one parallel batch. Each subagent gets **only** its role prompt + the assertions (+ minimal named context) — **not this chat, not each other's output**.

**Hard rules** (from [harness §3](../../agent/process/cross-lineage-review-harness-protocol.md)):

- **Different families.** Every judgment role is a different family from Claude and, where possible, from each other.
- **Balanced stances (Run #2 lesson).** The panel must include **at least one evidence-weighing reviewer** (primary posture: affirm what genuinely holds) **and at least one prosecutorial reviewer** (primary posture: break the claim). Severity tracks stance as much as lineage, so a single-stance panel produces a misleading matrix.
- **Blind, rotated adversary.** The adversary is blind (assertions only); rotate the adversary family across runs so no lineage's bias becomes structural.
- **Reduced context is enforced, not assumed.** Inline *all* context a reviewer needs directly in its prompt, and instruct every subagent to **evaluate only what is in the prompt and not read the workspace or open files** — uncontrolled repo access breaks both blindness and reduced context.
- **Synthesizer defaults to non-author.** Default to a **non-author lineage synthesizer whenever a clean independent merge is cheap**; author-side (Claude) synthesis is the quick-check fallback only and must be **labeled author-side** (the load-bearing weakness above). For any consequential claim a non-author synthesizer is **required**.

**Models available for subagents** (pass as the `model` slug): independent lineages for judgment roles — `gemini-3.1-pro` (Google), `gpt-5.5-medium` / `gpt-5.4-medium` (OpenAI), `grok-4.3` (xAI), `kimi-k2.5` (Moonshot). Coding-specialized (`gpt-5.3-codex`, `grok-build-0.1`) and Cursor's own (`composer-2.5`) exist but are weaker fits for civic/analytical judgment. Author lineage is Claude (this chat) — never a judgment role.

**Default panel** (3–4 reviewers; scale down to 2 for a quick check). The **Stance** column carries the Run #2 lesson — keep at least one `weigh` and one `prosecute`:

| Role | Stance | Default lineage | Context |
| --- | --- | --- | --- |
| Domain skeptic (hostile expert in the relevant field) | prosecute | `gemini-3.1-pro` | assertions + the one relevant section/definition (Opt A) |
| Verifier / empiricist (source fidelity + "is this testable?") | weigh | `gpt-5.5-medium` | assertions + any cited sources |
| Adversary / falsifier-hunter **[blind]** | prosecute | rotate (`kimi-k2.5` ↔ `grok-4.3`) | assertions only (Opt B) |
| Framing reviewer (recommended — checks the assertion *set*) | framing | the family not yet used | the assertion **set** only |
| Second domain lens (optional) | weigh | the family not yet used | assertions + relevant section |

The **framing reviewer** is the one cheap check on author-side *assertion-selection* bias: it does not judge whether the assertions are true, only whether they are the **right** assertions (what load-bearing part of the claim no assertion captures; which assertion is framed so it can't fail). Include it whenever the assertions themselves were drafted by the author lineage — i.e., almost always.

The **synthesizer** defaults to a **non-author lineage** spawned to merge the returned critiques whenever a clean independent merge is cheap. Author-side synthesis by *you* (this chat) is the **quick-check fallback only** and must be **labeled author-side** (the skill's load-bearing weakness — see above). For any consequential claim, a non-author synthesizer is **required**.

### Shared instructions (paste into *every* role prompt)

**Severity codebook — use these exact labels and anchors so severity means the same thing across families:**
- `BLOCKING` — the assertion is unfalsifiable, false, or adds nothing over existing frames. *Anchor:* "X reduces risk" with no metric and no result that could ever come out negative.
- `MAJOR` — a load-bearing part is wrong or unsupported, but the assertion is salvageable with real work. *Anchor:* a real association overstated into a causal claim the cited evidence does not carry.
- `MINOR` — a scoping or wording flaw; the core holds. *Anchor:* "polarization" used where the evidence only supports "nationalization."
- `AFFIRMING` — genuinely well-supported as stated.

**Honesty floor (binds *all* reviewers, including the adversary):** Affirm what genuinely holds — **a false kill is itself a failure.** Do not manufacture a BLOCKING to look rigorous; if an assertion cannot be broken, say so and mark it AFFIRMING.

**Boundaries:** Evaluate ONLY what is in this prompt. Do **not** read the workspace or open files, and you cannot see other reviewers' work.

### Role-prompt templates (adapt the bracketed parts; prepend the shared instructions above)

**Domain skeptic** *(stance: prosecute)* — "You are a hostile [domain] expert reviewing assertions drafted for a civic-design project. Attack the substance, do not extend it. For each assertion: severity (per the codebook), the single most likely error, whether it already anticipates your objection, and your sharpest source. End with the one change that would most improve the claim."

**Verifier / empiricist** *(stance: weigh)* — "Check only (a) whether each cited source faithfully supports its claim and (b) whether each assertion is actually testable / supportable by the *balanced* literature (cite both sides). Flag every overclaim **and every understatement**. Output a table: assertion → strongest FOR → strongest AGAINST → supported/contested/under-determined → severity → note."

**Adversary [blind]** *(stance: prosecute)* — "The following are assertions that claim to be well-founded. Try to break that claim: find every place a committed defender could always declare success; attack the weakest load-bearing assertion as forcefully as the evidence allows. Be the prosecution. The honesty floor still binds you — if an assertion genuinely cannot be broken, say so and mark it AFFIRMING (a false kill is a failure). For each: operationalized enough to be falsified? (yes/no), how a defender dodges a NO, and severity. End with the single strongest reason to discard the set — or, if it holds, the single qualification it most needs."

**Framing reviewer** *(stance: framing)* — "You are reviewing only the *framing* of an assertion set drafted by the same AI lineage that produced the original claim. Do **not** judge whether the assertions are true. Judge whether they are the **right** assertions: What load-bearing part of the original claim is captured by *no* assertion? Which assertion is framed so it cannot really fail? What would a defender of the claim be relieved you did not ask? Propose up to three assertions that should have been included. This is the check on author-side assertion-selection bias."

### Step 3–4 — Collect and synthesize

Build, from the returned critiques:
- a **per-assertion × per-reviewer detection matrix**, with each reviewer's **lineage and stance** both labeled (severity per cell);
- **convergence — read across *stance* and *lineage*.** A finding is strong only when reviewers of *different stances* (≥1 weigh + ≥1 prosecute) **and** different lineages raise it independently. Convergence that co-varies with stance (e.g., only the prosecutors BLOCK) is **weak** — it likely measures the prompt, not the claim;
- **divergence**, left **OPEN** (do not majority-vote, do not smooth away);
- a severity-ranked **consolidated revise-list**;
- any **framing gaps** the framing reviewer surfaced (assertions that should have been tested but were not).

### Codebook

- Severity labels + anchors: see the **shared codebook** pasted into every role prompt (above).
- **"Survives" = no BLOCKING stands across stance** after synthesis — it does **not** mean "true." A BLOCKING from a single role/lineage that **no different-stance reviewer shares** is **weak** and must not, by itself, sink an assertion (Run #2 lesson).
- **The signal is cross-stance × cross-lineage convergence, not raw cell counts.** Severity tracks stance, so counting BLOCKINGs rewards hostile prompting rather than measuring the claim. The blind adversary is *one* input, not the verdict. Author-anticipated convergence is a *weak* signal.

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

**Provenance — Run #1 (self-test), June 26, 2026.** This skill was run on its own value claim — *"an on-demand cross-lineage skill measurably reduces overclaim risk."* A blind 4-family panel (Gemini, GPT-5.5, Kimi, Grok) returned **zero AFFIRMING** verdicts: the claim *as worded* does not survive (no operational metric for "overclaim risk"; "decorrelation" confounded with reviewer-count + adversarial framing absent a 4×Claude control; author-side framing/synthesis reintroduces the bias; n=1 + Goodhart risk). What survived is the weaker, honest claim reflected above: *a cheap, testable mitigation that plausibly reduces some correlated-review failure modes, currently unmeasured.*

**Provenance — Run #2 (specificity test), June 26, 2026.** To check whether the panel can *discriminate* or only *shred*, it was run on a claim expected to mostly survive — *"Declining local-news coverage is associated with lower civic participation and higher polarization in U.S. communities"* (panel: Gemini domain-skeptic, GPT-5.5 verifier, Grok blind-adversary, Kimi methods-skeptic). Result: **6 AFFIRMING cells** (vs. 0 in Run #1), and the panel correctly localized the single weak assertion (an A4-association / A5-"independent-causal-weight" motte-and-bailey) rather than nuking uniformly — so the skill carries signal, not just hostility. **But the run also showed severity tracked *role-prompt stance* more than lineage**: the reviewers told to prosecute (blind adversary, methods-skeptic) returned the BLOCKINGs while those told to weigh-and-affirm returned AFFIRMINGs on the same claim. Operative lesson: the discriminating signal is **cross-stance convergence**, not raw cell counts — a lone BLOCKING from a single role/lineage is weak.
