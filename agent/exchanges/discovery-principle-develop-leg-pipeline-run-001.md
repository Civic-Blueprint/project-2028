---
title: Develop-Leg Agent Pipeline — Run 001 (target: the S17 test-design memo)
description: Stage-0 pre-registration for the first concrete run of the test-design memo's §7.5 agent orchestration. The pipeline is run, lightweight, ON the test-design memo itself — which doubles as (a) the memo's overdue independent-lineage review (memo §9 #5), (b) a Rung-0 instance of the develop-leg mechanism operating on the project's own beliefs (memo §6), and (c) a shakeout of the orchestration before any human subject is involved. Cross-lineage via Cursor subagents (no API keys). This file is the artifact the steward FREEZES before any subagent is spawned; results are appended after the run. NON-EVIDENCE for S17.
provenance: collaborative
status: Run complete (June 8 2026) — synthesis verdict REVISE (5 BLOCKING, all repairable; S17 unharmed); Stage-6 steward go/no-go PENDING
created: 2026-06-08
governing_protocols:
  - ../process/adversarial-review-protocol.md
  - ../process/comparative-alignment-protocol.md
  - ../process/research-protocol.md
parent_artifacts:
  - discovery-principle-develop-leg-test-design-memo.md
  - discovery-principle-develop-leg-exchange.md
---

# Develop-Leg Agent Pipeline — Run 001

> **Target:** the [S17 test-design memo](discovery-principle-develop-leg-test-design-memo.md).
> **What this run is, simultaneously:** (1) the **independent-lineage review** the memo says it still needs ([memo §9 #5](discovery-principle-develop-leg-test-design-memo.md)); (2) a **Rung-0** instance — the develop-leg's own mechanism (non-correlated authorities + safety + consolidation) operating on the project's own beliefs ([memo §6](discovery-principle-develop-leg-test-design-memo.md)); (3) a **shakeout** of the [§7.5 orchestration](discovery-principle-develop-leg-test-design-memo.md) before any human is involved.
> **What this run is NOT:** evidence for S17. It is agent-scale, n = 1, and tests *the memo*, not a society. The §7.1 instrument↔subject firewall holds: nothing here is cited as S17 support.
> **Discipline:** this file is **frozen by the steward before any subagent is spawned** (Stage 0). Per the [Adversarial Review Protocol §2 default](../process/adversarial-review-protocol.md) and the steward's standing rule, the adversarial pass is **never auto-run** — it runs only on an explicit go, and it runs **cross-lineage**, not in the authoring lineage.

---

## 1. Role → lineage assignment

Authoring lineage is Anthropic/Claude (it wrote the memo). Every **judgment role is a different lineage** from the author and from each other; the **adversary is blind** and independent. Spawned as parallel Cursor subagents — no API keys.

| Role | Lineage (subagent model) | Context given (reduced — Opt A) | Blind to other reviewers? |
| --- | --- | --- | --- |
| Author / designer | Anthropic — Claude *(already produced the memo)* | full | n/a |
| Measurement skeptic | **OpenAI — `gpt-5.5-medium`** | memo §2–§4 + §3 only | yes |
| Falsifier-hunter (adversary) | **xAI — `grok-4.3`** | memo (full) + F1–F6, framed as assertions (Opt B) | yes |
| Ethics / guardrail monitor | **Google — `gemini-3.1-pro`** | memo §5, §7 + riff §8 | yes |
| Verifier | **Moonshot — `kimi-k2.5`** | memo + [research digest](discovery-principle-develop-leg-research-grounding.md) + cited claims | yes |
| Synthesizer | **Google — `gemini-3.1-pro`** (non-author; reassigned at freeze) | all four critiques + divergence | n/a |

Each subagent receives **only** the named documents and its role prompt — **not this chat**, not each other's output. Independence is enforced by spawning them in one parallel batch.

---

## 2. Role prompts (the actual dispatch)

### 2.1 Measurement skeptic — OpenAI
> You are a hard-nosed psychometrician who distrusts self-report and is hostile to construct-validity hand-waving. You are reviewing §3 of an attached test-design memo (collective "repair capacity"). Attack the measurement. Can the construct be measured *behaviorally* and distinguished from (a) rationalization, (b) eloquence/vocabulary, (c) IQ/education, (d) ideological moderation, (e) ordinary belief-updating? For each of the §3.2 indicators, rate measurability (strong/weak/unmeasurable) and name the most likely **false positive** (rationalization scored as repair) and **false negative**. State plainly whether §3.3 and §3.5 already answer your objections or whether gaps remain. End with the single change that would most improve the instrument.

### 2.2 Falsifier-hunter (adversary) — xAI **[blind]**
> The following is a test design that *claims* to be falsifiable. Your job is to break that claim. Find every place the design **cannot return NO**: un-falsifiable spots, post-hoc escape hatches, researcher degrees of freedom (could pick outcomes after seeing data), and anywhere a committed defender could always declare success. Check each falsifier F1–F6: is it operationalized enough to actually trip? Attack the matched comparison (§4), the ecological-fallacy guard (§3.4), and especially the Rung-0 "the project is its own first subject" move (§6/§7.3) as self-serving. Deliver the strongest possible case that the whole memo is motivated reasoning dressed as rigor. Do not be balanced; be the prosecution.

### 2.3 Ethics / guardrail monitor — Google
> You are an IRB reviewer who has also organized in low-income communities and has watched "reform" become a tool for displacement. Review §5 (ethics) and §7 (agent pipeline) of the attached memo, plus the reflexive guardrail it cites (riff §8). Where could this design harm people? Does "natural shocks only" actually hold, or are there incentives to nudge/manufacture a break? Where are consent and agency thin? Does the agent pipeline risk becoming the mirror-image "machine" it critiques (S21)? Who controls shock-classification, and is that power legible and reversible? List anything that should **stop** the study, ranked by severity.

### 2.4 Verifier — Moonshot
> You are a citation-integrity checker operating under a strict research protocol. Using the attached memo and its research digest, check whether each cited source (e.g., Haidt, Frazier et al., Buchanan & Powell, Edmondson, Pettigrew & Tropp, Sunstein, Yerkes–Dodson) is used **faithfully** — i.e., the source actually supports the specific claim it is attached to. Flag every overclaim, misattribution, or use of a source beyond its scope. Do **not** assess whether the memo is persuasive; assess only fidelity of source-to-claim. Output a table: claim location → cited source → faithful? (yes/overclaim/misattributed) → note.

### 2.5 Synthesizer — Google (non-author lineage)
> Merge the four critiques. Record **convergence vs. divergence** per the Comparative Alignment Protocol — where reviewers agree, and where they conflict (do **not** smooth conflict away). Produce: (1) a severity-ranked **revise-list** for the memo (blocking / major / minor / affirming); (2) the points where the reviewers **disagree with each other**, left open; (3) a recommended **go/no-go** for the steward with the reasoning. You also produced the ethics critique in this run — treat it at arm's length, equal to the other three; your job is fidelity to all four critiques, not defense of any one.

---

## 3. Codebook — what a finding is, and what "the memo survives" means

- **Severity scale:** `BLOCKING` (the design is un-falsifiable, unethical, or the instrument cannot distinguish repair from a confound) · `MAJOR` (a real hole that weakens but doesn't void) · `MINOR` (fix-on-revision) · `AFFIRMING` (holds up).
- **"Survives" is not "S17 is true."** This run cannot support S17 (firewall). "Survives" = **no BLOCKING finding stands** after synthesis — i.e., the memo's *test design* is still falsifiable, ethical, and measurable. A BLOCKING finding sends the memo back to revision (bounded loop), not S17 to the grave.
- **Convergence is not the success metric.** Per [§7.4](discovery-principle-develop-leg-test-design-memo.md), surviving the adversary is. Reviewer disagreement is recorded, not resolved by majority.

## 4. Falsifier checks the adversary must return a verdict on

For each, the adversary states: *operationalized enough to trip? (yes/no)* and *how a defender could dodge it.*

- **F1** practice bodies don't out-repair controls · **F2** practice bodies fracture/polarize more · **F3** effect needs manufactured crises · **F4** effect needs central authority · **F5** "repair" = better justification not better decisions · **F6** effect vanishes under IQ/education/selection controls.

## 5. Run log — results (June 8, 2026)

Run completed cross-lineage via Cursor subagents. Author = Anthropic/Claude (the memo). Four reviewers spawned **blind and in parallel**; synthesizer = Google/Gemini (non-author).

| Role | Lineage | Verdict | Severity tally |
| --- | --- | --- | --- |
| Measurement skeptic | OpenAI | Not measurement-ready | 2 BLOCKING · 4 MAJOR · 1 MINOR · 1 AFFIRMING |
| Adversary (blind) | xAI | Does **not** survive as falsifiable | 3 BLOCKING · 4 MAJOR · 2 MINOR |
| Ethics monitor | Google | Reject and revise (hold) | 2 BLOCKING · 2 MAJOR · 1 MINOR · 1 AFFIRMING |
| Verifier | Moonshot | Mixed citation integrity | 1 BLOCKING · 2 MAJOR · 2 MINOR · 3 AFFIRMING |
| Synthesis | Google (non-author) | **Survives conditionally → REVISE** | 5 BLOCKING consolidated |
| **Steward go/no-go** | human | **PENDING (Stage 6)** | — |

### 5.1 Convergence (2+ lineages independently — strongest signal)

- **Natural-shock classification/matching** — researcher degrees of freedom + an incentive to nudge/harvest trauma to hit sample size *(skeptic + adversary + ethics)*.
- **Objective-washing / status confound** — the instrument rewards education/eloquence and launders one steward's values into "objective" output *(skeptic + ethics; adversary's "hollow ecological guard")*.
- **Preemptive exits / evasion ramps** — the §3.5 validity gate and stop-conditions let the design abort before any falsifier is evaluated *(adversary + ethics)*.

### 5.2 Divergence — left OPEN (not majority-voted)

- **F3 catch-22:** falsifiability (adversary: F3 can't trip) vs. ethics (ethics: enforce the manufactured-crisis ban) — **cannot satisfy both as written.**
- **Rubric rigidity vs. community veto:** skeptic wants a rigid pre-registered rubric; ethics wants a STOP when a community contests its classification (their "calcification" may be their "principled solidarity").
- **Unit of consent vs. unit of analysis:** body-process accepted by skeptic + adversary; ethics calls leader opt-in a "consent illusion" and demands individual consent — which could make the comparison impractical.

### 5.3 Consolidated revise-list

**BLOCKING** — B1 F3↔ethics contradiction · B2 objective-washing / status confound (instrument can't separate repair from rationalization/status; rubric frozen by one steward) · B3 Rung-0 circularity + §3.5 preemptive exit + no numeric F-cutoffs · B4 consent illusion (leader opt-in ≠ member consent; control groups) · B5 Edmondson overstretch (+ uncite-able 3-condition bundle; add Pettigrew & Tropp).
**MAJOR** — pre-register quantitative natural-shock criteria · "repair" weaponization → community-contest log · Frazier and Kapur/Bjork miscitation (measurement/individual, not collective mechanism) · ideological-moderation confound.
**MINOR** — define dissent retention (voice/role/non-punitive standing) · pilot must record falsifiers on failure · cite IQ/education controls + flag Yerkes–Dodson's weak origin.
**AFFIRMING** — body/process unit is necessary · F3 + §8 guardrail are sound *if* made mutually consistent · Haidt, Sunstein, Buchanan & Powell faithfully cited.

### 5.4 Verdict and Rung-0 meta-note

**Verdict: the memo SURVIVES conditionally → REVISE.** No BLOCKING finding kills S17; all five are repairable design flaws. The hypothesis is unharmed; the *current draft of the test* is not yet falsifiable/ethical/measurable and goes back for heavy revision.

**Rung-0 meta-note (non-evidence; n = 1; agent-scale).** The cross-lineage process surfaced **five BLOCKING issues the same-lineage author draft did not flag** — the develop-leg mechanism (non-correlated authorities → better repair) operating on the project's own artifact. Honest caveats, in force: it is agent-scale, not civic; the **adversary itself flagged Rung-0 circularity as BLOCKING** (the recursion is real, not rhetorical); and the project chose this method partly *believing* the mechanism. Suggestive, not confirmatory — and the single most useful thing the run produced is a concrete reason to **distrust** the Rung-0 claim it was supposed to support.

## 6. Known weaknesses of this run (declared up front)

1. **Synthesizer double-roles.** Resolved at freeze: synthesis was reassigned off the author lineage to **Google/Gemini** (the key rule — synthesizer ≠ author — is satisfied). Residual: Gemini also runs the ethics critique, so it merges one of its own outputs; §2.5 instructs it to treat that at arm's length. A lesser concern than author-synthesis.
2. **Agent-scale, n = 1.** Tests the memo, not a society; the S17 transfer gap recurs (memo §6).
3. **Subagents share an environment** (all via Cursor). They are genuinely different model families (Option D holds), but not different *vendors' full stacks* end-to-end.
4. **The project chose this method partly believing the mechanism** — so a clean result is suggestive, not confirmatory (memo §7.3 caveat).

## 7. Stage-0 freeze checklist *(steward)*

- [x] Falsifier set F1–F6 locked (no edits after go)
- [x] Codebook (§3) + role prompts (§2) locked
- [x] Role → lineage assignment (§1) accepted — **synthesizer reassigned to non-author Google** (§6.1)
- [x] Confirmed: this is **non-evidence** for S17, a memo-hardening + Rung-0 run
- [x] **GO** (steward, June 8 2026) — author may spawn the cross-lineage subagents

*Frozen. Reviewers spawned cross-lineage; results in §5.*

---

## Provenance and register

Stage-0 pre-registration, June 2026. Working companion to [Exchange #27](discovery-principle-develop-leg-exchange.md) and the [test-design memo](discovery-principle-develop-leg-test-design-memo.md); like them, **not** registered as a separate entry in [`_EXCHANGE_INDEX.md`](_EXCHANGE_INDEX.md). Idea layer only (riff §1.2 privacy firewall). No results, no promotion; S17 remains on hold.
