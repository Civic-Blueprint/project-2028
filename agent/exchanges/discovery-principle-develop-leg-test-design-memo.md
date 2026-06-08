---
title: Discovery Principle / Develop-Leg — S17 Test-Design Memo
description: A standalone design artifact for the Exchange #27 Round-4 reframe — the test that would either earn or kill S17 (the cross-scale-transfer claim), recast as a testable civic design hypothesis. Specifies the measurement instrument (collective repair capacity, behavioral), the matched-comparison design, its power/sample-size analysis (count bodies, not heads: ~45–120 bodies / ~700–3,600 people for a powered comparison, conditional on an unknown effect size), the pre-registered falsifier set, the ethics and stop conditions, the staged "rungs" from the project's own review process up to multi-site, and an agent-automation architecture (persona × model-lineage roles, plus a buildable orchestration sketch — endpoint mapping, a frozen run manifest, and a six-stage run flow) for designing/running/verifying/red-teaming the test. It is a design, NOT a run: nothing here is evidence, nothing is promoted, and S17 remains on hold. Same-lineage draft; cross-lineage and human review pending.
provenance: collaborative
status: design only — test not run; S17 on hold; nothing promoted
created: 2026-06-08
governing_protocols:
  - ../process/adversarial-review-protocol.md
  - ../process/comparative-alignment-protocol.md
  - ../process/research-protocol.md
parent_exchange: discovery-principle-develop-leg-exchange.md
---

# Discovery Principle / Develop-Leg — S17 Test-Design Memo

> **What this is.** The artifact [Exchange #27 §4.6](discovery-principle-develop-leg-exchange.md) names as the develop-leg's next step: a **design for the test that would earn or kill S17** — the cross-scale-transfer claim that Round 2 found decisive *against* and Round 4 recast as a **testable civic design hypothesis** (exchange §4.2). It specifies *how* you would test the transfer, with the discipline Round 4 committed to: **the test must be able to come back NO.**
>
> **What this is NOT.** It is **not a test that has been run**, and it is **not evidence.** It carries no results and no confidence numbers. It does not promote anything — not a [principle](../../PRINCIPLES.md), not [doctrine](../doctrine/), not a [Phase 3](../explorations/phase-3-front-door-riff.md) brief. **S17 remains on hold** (the [#25](shared-mirror-see-layer-exchange.md) hold governs); this memo only makes the hold *live* (parked pending a specifiable experiment) rather than parked indefinitely. Same-lineage draft (Opus); independent-lineage and human review pending.
>
> **Provenance / firewall.** Idea layer only ([riff §1.2](../explorations/discovery-principle-moral-architecture-riff.md) privacy firewall). Working-design register; named uncertainty; no rhetorical flourish.

---

## 1. Purpose and the one discipline

S17 says insights about how an *individual* develops moral architecture transfer to how a *society/institution* does. Round 2 ruled it **unwarranted** (not disproven) — there is no matched collective-scale evidence, and the one structural account of collective moral change now catalogued ([digest Cluster D](discovery-principle-develop-leg-research-grounding.md): Buchanan & Powell) runs *against* the individual-capacity story. Round 4's move (the steward's "three-utilities" reframe: *"no evidence yet" ≠ proof of impossibility*) was to stop defending S17 as a claim and instead **design the experiment that would settle it.**

**The discipline this whole memo serves:** every section is built so the test can return **NO**. A design that cannot fail is not a test; it is the machine confirming itself ([riff §8](../explorations/discovery-principle-moral-architecture-riff.md) reflexive guardrail, exchange S21).

---

## 2. The hypothesis under test, and the pre-registered falsifiers

**The civic design hypothesis (exchange §4.2):**

> A civic body (institution, community, or polity) deliberately engineered for (1) routine exposure to **non-correlated** authorities/inputs, (2) **psychological safety** for dissent, and (3) **consolidation** after a shared conclusion breaks — will, when hit by a shock that invalidates a prior shared conclusion, **repair** (revise the broken belief while preserving function) at a higher rate than a matched *answer-transmission* body, **without manufacturing the shock or recentralizing authority.**

**Pre-registered falsifiers — declared before any data, any of which kills or bounds the hypothesis:**

| # | If we observe… | …then |
| --- | --- | --- |
| F1 | Reasoning-practice bodies do **not** out-repair matched answer-transmission controls under the same shock | transfer **dead** |
| F2 | Reasoning-practice bodies **fracture or polarize more** (the group-polarization risk realized — Sunstein, [digest Cluster A](discovery-principle-develop-leg-research-grounding.md)) | transfer **dead / net-harmful** |
| F3 | The effect appears **only** when crises are *manufactured* | **defeats the purpose** (manipulation; §5) |
| F4 | The effect requires a **central authority** to direct the repair | **defeats the purpose** (it is the machine) |
| F5 | "Repair" turns out to be better **justification**, not better **decisions** (Haidt) | transfer **dead** (measuring the wrong thing) |
| F6 | The effect **vanishes** once IQ / education / selection are controlled | **S18 relabel realized at collective scale** (no distinct capacity) |

If none of F1–F6 trips and the predicted difference holds, S17 has earned a *first* warrant — not promotion, just the right to a larger test.

---

## 3. The measurement instrument (the hard part)

The instrument must define **collective repair capacity** so it is observable, behavioral, and distinguishable from the things Round 2 said it might secretly be.

### 3.1 The construct

When a body meets a shock that invalidates a prior shared conclusion, classify its response on the [riff §1.4](../explorations/discovery-principle-moral-architecture-riff.md) hub: **repair** (revise the broken belief, preserve function) vs. **calcify**, **fracture/exit**, or **wholesale convert**. Repair capacity is the *rate and quality* of the first relative to the others.

### 3.2 Behavioral indicators (not self-report)

- **Documented belief revision under evidence** — a recorded position/policy change after the disconfirming shock (minutes, statements, votes), not a survey of feelings.
- **Dissent tolerated without exit** — on-record minority positions present *and* dissenters retained (not excommunicated); measured by retention and the existence of preserved disagreement.
- **Decision quality on a *novel* dilemma** — performance on a dilemma the body has not seen, scored by **blinded** raters for process features (multiple values weighed, consequences anticipated) vs. slogan-application.
- **Function preserved** — the body keeps operating (no schism/collapse) *while* revising.

### 3.3 Discriminant validity — what repair must be distinguished from (the Round 2 attacks, operationalized)

| Confounder | Guard |
| --- | --- |
| Vocabulary / eloquence (better words, same decisions) | Score **decisions/behavior**, not justifications (Haidt) |
| IQ / education | Control for it; repair must predict **beyond** cognitive ability |
| Ideological moderation | Repair ≠ moving to center; measure **revisability**, not direction (answers the §2.5 "S10 directional flexibility" attack) |
| Ordinary belief-updating | Repair is updating a **coupled / identity-linked** belief while preserving identity/function — not updating a trivial one |
| Rationalization / narrative (Frazier et al.) | **Prospective** pre→post behavioral change, not retrospective self-reported "growth" |

### 3.4 Beat the ecological fallacy

**Unit of analysis = the body's process** (its deliberation records, dissent channels, decision outputs) — *not* the average member's attitude survey. We are measuring an institution's behavior, not a pile of individuals (the §2.5 ecological-fallacy attack).

### 3.5 Construct-validity checks

Convergent (does the measure track independent expert ratings of the body's adaptiveness?), discriminant (uncorrelated with eloquence/IQ per §3.3), predictive (does a body's score predict its response to a *future* shock?). If the instrument cannot pass §3.3 + these checks, the test does not proceed — there is nothing trustworthy to measure.

---

## 4. The comparison design

### 4.1 Design

- **Units.** Two or more bodies matched on size, domain, baseline composition, and prior-shock history. One runs **answer-transmission** (authority supplies the conclusion); one runs **reasoning-practice** (the §4.2 conditions: non-correlated inputs + psychological safety + consolidation).
- **The shock.** **Naturally occurring** (see §5) — a real event that invalidates a prior shared conclusion in both bodies. No manufactured crises.
- **Outcome.** The §3 instrument, applied blind. Prediction: reasoning-practice > answer-transmission on repair, *without* F2–F4.
- **Confound control.** Selection is the chief threat (people who join reasoning-practice bodies may differ). Mitigations, strongest first: where ethical, **randomized assignment to practice conditions within a body**; otherwise **matched quasi-experiment** with baseline measurement and **difference-in-differences**; always **control for IQ/education/composition** (F6).
- **Pre-registration.** Hypotheses, measures, analysis plan, and stop rules registered **before** data (answers the Round 2 §2.9 pre-registration cross-examination).

### 4.2 Power and sample size — count bodies, not heads

**The unit is the body, so the primary N is the number of bodies, not people.** Because §3.4 fixes the unit of analysis at the *body's process*, this is a **cluster comparison**: a study of 5,000 people in 4 bodies is underpowered; ~40 bodies of ~25 people is far stronger on fewer total humans. "How many humans" is therefore a *derived* number — bodies × (enough members for the body to function).

**The driver is the effect size, which is unknown.** S17 is untested, so we have no prior for how much reasoning-practice raises the repair rate. The body-count falls straight out of the assumed gap (outcome scored at the body level — repaired vs. calcified/fractured/converted, §3.1):

| Assumed effect (repair rate: control → practice) | Bodies **per arm** | Bodies **total** |
| --- | --- | --- |
| Very large (20% → 60%) | ~22 | **~45** |
| Large (25% → 55%) | ~35 | **~70** |
| Moderate (30% → 55%) | ~60 | **~120** |

*Two-proportion test, 80% power, α = .05 two-sided. A **matched pre/post difference-in-differences** design (§4.1) pulls these toward the low end — roughly a 30–40% reduction. These are illustrative, not authoritative: every row is conditional on a guessed effect.*

Converted to people, assuming a functioning deliberative body is ~15–30 members:

| Scenario | Bodies | × body size | **People (approx.)** |
| --- | --- | --- | --- |
| Optimistic (large effect, small bodies) | ~45 | ×15 | **~700** |
| Middle | ~70 | ×25 | **~1,750** |
| Conservative (moderate effect) | ~120 | ×30 | **~3,600** |

So a real *powered* comparison (Rung 2, §6) is **order ~45–120 bodies / ~700–3,600 people** — but you would never start there.

**Two constraints bind harder than headcount:**

1. **No effect-size prior.** The first real study should be a **pilot (Rung 1.5, §6)** whose only job is to *estimate* the effect and the intracluster correlation, so a later confirmatory trial can be powered honestly. Powering a confirmatory trial on a guessed effect is false precision.
2. **Natural shocks are scarce and not on demand** (§5: no manufactured crises). You cannot enroll dozens of bodies and have each conveniently meet the right disconfirming shock; this likely forces a **natural-experiment** design (find bodies that *happened* to face one), which loses randomization and *raises* the N needed to control confounds. This is harder to satisfy than recruiting people.

**Why this connects to the simulation.** A persona-sim cannot be evidence for S17 (the §7.1 firewall), but it can **sharpen the §3 instrument** and yield a **provisional effect-size prior** — and a better instrument plus a non-zero prior is exactly what powers Rungs 1.5–2 with *fewer real bodies*. "Simulate first" is partly how you avoid burning ~3,600 people on an underpowered first swing. Per-rung counts are carried in the §6 table.

---

## 5. Ethics and stop conditions

- **No manufactured crises.** Only naturally occurring shocks. Manufacturing the break is the manipulation playbook ([riff §8](../explorations/discovery-principle-moral-architecture-riff.md)) and the dose-response hazard (riff §4.2).
- **Voluntary and opt-in.** The reasoning-practice conditions and any exercises are entered by consent; no one is a subject without knowing it.
- **Stop conditions.** Predefined harm thresholds (measurable distress, coercion, exit-punishment of dissenters) halt the study.
- **Reflexive guardrail (S21).** If the design starts to *require* threat-manufacture or central direction to work, that is not a tuning problem — it is F3/F4 firing, and it means we were building the machine.
- **Power legibility.** Who designs the exercises and the shock-classification is named and reversible ([Principle 3](../../PRINCIPLES.md#3-ai-must-augment-agency-not-replace-democratic-accountability), [Principle 4](../../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible)).

---

## 6. The rungs — start with the smallest cylinder

Staged; each rung gated by the prior; nothing promoted at any rung.

| Rung | Unit | What it tests | Bodies | People ≈ (§4.2) | Status of evidence |
| --- | --- | --- | --- | --- | --- |
| **0** | The **project's own cross-lineage review** process | Does a non-correlated-authority + safety + consolidation process repair the project's *own* beliefs better than a single-lineage one would? | 1 (this exchange) | — (agents) | **Already running**; n = 1; **agent-scale, not civic** — suggestive only (see §7) |
| **1** | One bounded human body (a community, school, team, or online group) — observational | Does the §3 instrument even **detect variation** in repair? (instrument validation) | 1 + a few | ~30–150 | Not run |
| **1.5** | A small set of bodies — pilot | Estimate the **effect size + intracluster correlation** to power Rung 2 honestly (no prior exists) | ~6–10 | ~150–300 | Not run |
| **2** | A **matched** comparison (§4) | The actual transfer prediction at minimum viable scale, against F1–F6 | **~45–120** | **~700–3,600** | Not run |
| **3** | **Multi-site** replication | Whether the effect generalizes | ×2–3 sites | thousands | Not run |

Counts are from §4.2 and are *conditional on an unknown effect size* — Rung 1.5 exists precisely to replace the guess with an estimate. The honest caveat carried from exchange §4.3 #6: Rung 0 tests the mechanism among *AI agents reasoning about a project's beliefs* — **agent-scale ≠ human-civic-scale**, so S17 *recurs* between "agent collective" and "human collective." Rung 0 is the first rung, never the proof.

---

## 7. Agent-automation architecture

**Scope decision (steward, June 2026): agents as *instrument* + persona-simulation as *red-team / instrument-validation only*, explicitly labeled NON-EVIDENCE.** Agents design, run, verify, and red-team the test; a persona-sim may stress the *design and the measure*, but a multi-agent "society" is **never** treated as evidence for S17. Conflating instrument with subject is the ecological fallacy one level down.

### 7.1 The instrument ↔ subject firewall

| Use | Allowed? | Why |
| --- | --- | --- |
| Agents **design / verify / adversarially review** the test | **Yes** | In-doctrine (the protocols below); decorrelated judgment improves the design |
| Persona-sim to **validate the measure** ("can §3 tell repair from rationalization on a transcript?") and **red-team** ("can the design be gamed? does the falsifier trip?") | **Yes — labeled non-evidence** | Tests the *instrument*, not the *hypothesis* |
| Multi-agent "society" sim as **evidence for S17** | **No** | A synthetic society is not a civic institution; a clean sim would launder the unproven transfer (apophenia + the machine confirming itself) |

### 7.2 The persona × model-lineage roles

Built from [Adversarial Review Protocol](../process/adversarial-review-protocol.md) **Option C** (persona/domain lens) + **Option D** (independent model lineage), with [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md) recording convergence/divergence and [Research Protocol §4](../process/research-protocol.md) governing verification.

| Role | Job | Persona (Opt C) | Lineage need (Opt D) |
| --- | --- | --- | --- |
| **Designer / author** | Draft the design | neutral | single (it will be reviewed) |
| **Measurement skeptic** | Separate repair from rationalization / vocabulary / IQ / moderation (§3.3) | "psychometrician who distrusts self-report" | **different lineage** |
| **Falsifier-hunter** | Attack until the test *can* return NO; catch un-falsifiability and result pre-commitment | "pre-registration referee" | **independent + blind** (A+C+D) |
| **Ethics / guardrail monitor** | Manufactured-crisis, consent, the mirror-machine risk (§5) | "IRB reviewer / organizer wary of reform-as-displacement" | diversity helps |
| **Three-target red-team** | Simulate sincere holder / mobilizer / instrumental user ([riff §5.4](../explorations/discovery-principle-moral-architecture-riff.md)) to test whether the measure is gameable | three personas | **different lineages** (so personas aren't one model's caricature) — *instrument validation only* |
| **Verifier** | Citation / integrity per Research Protocol §4 | neutral | different from author (default) |
| **Synthesizer** | Consolidate; log convergence/divergence | neutral | ideally a third lineage / rotate |
| **Steward (human)** | Set the falsifier set; own go/no-go and the ethics call | — | **irreducible non-agent node** |

**Why lineage diversity is non-negotiable on the judgment roles:** same-lineage agents share priors and blind spots — common-mode failure, the riff's §2.5 correlated-collapse / [digest Cluster B](discovery-principle-develop-leg-research-grounding.md). A single-lineage pipeline is **series-wired by construction** — the exact anti-pattern the develop-leg diagnoses; testing the develop-leg with one lineage would be self-refuting. Mechanical roles (scoring to a fixed rubric, data wrangling, formatting) do not need multiple lineages — reserve the cost for decorrelated judgment.

### 7.3 The pipeline instantiates the hypothesis (and is therefore Rung 0)

The orchestration should embody the §4.2 conditions: **non-correlated inputs** (multi-lineage = Option D), **psychological safety** (blind / independent so agents are not anchored; the reward is challenge, not agreement — no convergence pressure), and **consolidation** (the synthesis round). Building it this way is both *consistent with what the hypothesis claims* and *makes the pipeline the §6 Rung-0 instance* — with the §6 caveat (agent-scale ≠ civic-scale) in force.

### 7.4 What keeps the pipeline honest

- The **falsifier set (§2) is pre-registered before any runs**; agents cannot revise it mid-stream.
- The **adversary is blind and independent-lineage** (Option D); the synthesizer records divergence rather than smoothing it.
- The **human owns go/no-go and the ethics call** (§7.2 firewall, Principles 3/4). Agents propose; the steward disposes.

### 7.5 Buildable orchestration — endpoints, manifest, run staging

This makes §7.2 concrete: which model endpoints fill which roles, and how one run proceeds.

**Endpoint mapping (one run; rotate families across runs).** Assign by *role-class*, not by favorite model. The hard rules: the **adversary ≠ author lineage** and is **blind**; the **verifier ≠ author lineage**; the three judgment roles should be **three different lineages** from each other where budget allows. Pin the exact version per run for reproducibility; **rotate the family↔role assignment across runs** so no one lineage's bias becomes structural.

| Role | Lineage rule | Example this run (rotate next) | Context policy (Opt A/B) |
| --- | --- | --- | --- |
| Author / designer | any single | Anthropic (Claude Opus 4.x) | full context |
| Measurement skeptic | ≠ author | OpenAI (GPT 5.x) | reduced — claims + instrument only |
| Falsifier-hunter (adversary) | ≠ author, **blind** | xAI (Grok 4.x) | reduced + **claims-as-assertions** (Opt B) |
| Ethics / guardrail monitor | diversity helps | Google (Gemini 3.x) | reduced — design + ethics lens |
| Three-target red-team | spread across lineages | sincere→Anthropic · mobilizer→OpenAI · instrumental→xAI | persona-only (§5.4) |
| Verifier | ≠ author | Google (Gemini 3.x) | sources + claims only (Research Protocol §4) |
| Synthesizer | rotate / least-involved | the family not dominating the critique | all critiques + divergence log |
| Steward | **human** | — | everything |

Families are illustrative (the four the project already uses); the manifest pins versions, and exact versions drift — so do not hardcode them in prose.

**Run manifest (frozen config — illustrative, not a real API):**

```yaml
run_id: s17-instrument-v0.3
stage0_preregistered:          # frozen BEFORE any generative call; hash-checked
  falsifiers: [F1, F2, F3, F4, F5, F6]
  instrument_spec: ref://memo#3
  rubric_hash: sha256:…
roles:
  author:            { lineage: anthropic, model: <pin>, context: full,            persona: neutral }
  measurement_skeptic:{ lineage: openai,    model: <pin>, context: reduced,         persona: psychometrician }
  adversary:         { lineage: xai,       model: <pin>, context: reduced_blind,   framing: assertions }
  ethics_monitor:    { lineage: google,    model: <pin>, context: reduced,         persona: irb_organizer }
  red_team:
    sincere_holder:  { lineage: anthropic, model: <pin>, persona: sincere_holder }
    mobilizer:       { lineage: openai,    model: <pin>, persona: mobilizer }
    instrumental:    { lineage: xai,       model: <pin>, persona: instrumental_user }
  verifier:          { lineage: google,    model: <pin>, context: sources_only }   # != author
  synthesizer:       { lineage: <rotate>,  model: <pin>, context: all_critiques+divergence }
invariants:
  falsifiers_immutable_after: stage0
  adversary_blind: true
  reviewers_blind_to_each_other_until: stage5
  divergence_preserved: true
  persona_sim_outputs_tagged: non_evidence
gates:
  human_signoff: [stage0_freeze, stage6_go_nogo]
```

**Run staging.**

```
[0 pre-register + freeze] ──human ✔──▶ [1 author draft]
     (F1–F6 + instrument + rubric_hash locked)
        │
        ▼
[2 blind review ∥]   skeptic(B) · adversary(C, blind) · ethics(D)      ← reduced context, 3 lineages
        │
        ▼
[3 persona-sim red-team]  3 targets across lineages  ── NON-EVIDENCE ──▶ validates the §3 instrument
        │   (plant positive + negative transcripts; a falsifier MUST trip on a planted negative,
        │    else the measure can't tell repair from rationalization → stop, fix the measure)
        ▼
[4 verify (≠ author)] ──▶ [5 synthesize: keep divergence] ──▶ [6 human go/no-go]
        ▲________________________ bounded revise-loop ________________________│
```

- **Stage 0 — pre-register & freeze.** Author drafts the spec; human locks F1–F6, the §3 instrument, and a `rubric_hash`. No judgment calls yet.
- **Stage 1 — draft.** Author (lineage A) produces the target artifact (instrument operationalization / rubric / sim transcripts).
- **Stage 2 — blind independent review (parallel).** Skeptic, adversary, ethics monitor each get reduced context, a different lineage, and are blind to each other → structured JSON critiques.
- **Stage 3 — persona-sim red-team (labeled non-evidence).** The three §5.4 targets generate planted-positive and planted-negative transcripts; the gate is whether the instrument classifies them correctly and a falsifier *trips* on a planted negative. This validates the **instrument**, never S17.
- **Stage 4 — verify.** Verifier (≠ author) checks citation/integrity, not persuasiveness.
- **Stage 5 — synthesize.** Synthesizer merges and records convergence vs. divergence per the [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md) — divergence is preserved, not smoothed.
- **Stage 6 — human gate.** Steward reviews the synthesis + divergence, confirms the falsifiers are unmoved, and decides revise (bounded loop to Stage 1) or freeze. Convergence is *not* the success criterion; surviving the adversary is.

**Build paths.** A thin orchestrator (Python or TS) holds the frozen manifest, dispatches each role's system-prompt to its mapped provider endpoint (Anthropic / OpenAI / Google / xAI), collects schema-validated JSON, and writes an auditable run log (every prompt + output + pinned version). Equivalent on the Cursor SDK (`@cursor/sdk` / `cursor-sdk`) — one agent per role with MCP repo access instead of raw API calls. **Cost discipline:** only the judgment roles spend multi-lineage tokens; mechanical steps (scoring to the frozen rubric, hashing, logging, divergence-diffing) are plain scripts, not model calls.

---

## 8. What this memo does not do — honest limits

1. **It is a design, not a run.** No results, no evidence, no promotion. S17 stays on hold.
2. **Automation ≠ evidence.** Agents can produce the design, the red-team, the verification, and the Rung-0 instance. They cannot produce the S17 *evidence*, which requires real human collective data (Rungs 1–3). A slick pipeline must not stand in for that.
3. **Agent-scale ≠ civic-scale.** Rung 0 is suggestive only; the transfer gap recurs.
4. **The reflexive trap is live.** A pipeline optimized to *validate* the hypothesis becomes the machine confirming itself; the §2 falsifiers, §7.4 structure, and the human node are the only defenses.

---

## 9. Open questions / next steps

1. **Instrument first.** §3 is the make-or-break — before any comparison, can the measure pass its §3.3 discriminant and §3.5 construct-validity checks (likely a Rung-1 observational pass)?
2. **Unit selection.** What real bodies are matched-comparison candidates without manufacturing anything (§4)?
3. **Rung 0 honesty.** What would a *negative* Rung-0 look like — i.e., the project's cross-lineage process failing to out-repair a single-lineage one — and are we prepared to record it? (The HOLD that three lineages forced where one rubber-stamped is the existing data point; it cuts *for* the mechanism, so the discipline is to look hardest for the case that cuts against.)
4. **Reviewer-surfaced sources to fold in if a real test opens.** [Digest Cluster D](discovery-principle-develop-leg-research-grounding.md) (Kahan, Bandura, Piaget, Latané, Durkheim, Rogers, Kohlberg/Rest, Buchanan & Powell) bears on measurement and on the structural-drivers competitor to the transfer.
5. **Independent-lineage + human review of *this memo*** before any rung is attempted (it is a same-lineage draft).

---

## Provenance and register

Same-lineage (Opus) draft, June 2026, as the [Exchange #27 §4.6](discovery-principle-develop-leg-exchange.md) next artifact. Idea layer only ([riff §1.2](../explorations/discovery-principle-moral-architecture-riff.md) privacy firewall). Like the [research-grounding digest](discovery-principle-develop-leg-research-grounding.md), this is a working companion to Exchange #27 and is **not** itself registered in [`_EXCHANGE_INDEX.md`](_EXCHANGE_INDEX.md). It runs no rounds and reaches no verdict; it is a design awaiting independent-lineage and human review.
