# Recursive Civic Uplift — Automated Convergence/ARP Pipeline Run

> **Status (June 2026):** Experimental pipeline run — steward-authorized, agent-executed. **NOT a registered exchange** and **NOT human-reviewed.** This file records a steward-requested experiment: run *(2 convergence rounds → ARP adversarial round → revise)* **four times** (12 rounds) on an agent-generated claim set about whether there is a *positive recursive-uplift* civic mechanism latent in the folded [#33 collective-emotional-ritual exchange](collective-emotional-ritual-civic-good-exchange.md), **followed by a steward-requested 2-round [Transmission Probe (Rounds 13–14)](#transmission-probe-rounds-1314--running-the-strongest-case-against-june-26-2026)** that ran the synthesizer's "strongest case against." Per the [Cross-Lineage Review Harness §Output](../process/cross-lineage-review-harness-protocol.md), harness-style run files are working companions, not index-registered. **Bottom line: recursive uplift NOT demonstrated; the durable take-aways are two reusable review instruments (now folded into the [harness protocol](../process/cross-lineage-review-harness-protocol.md)) and the transmission problem as a named constraint.**
>
> **Why this run:** The steward read [#33](collective-emotional-ritual-civic-good-exchange.md) (which folded — the C3 "channel-vs-drain has a portable predictor" gate failed across four lineages; the only durable move the panel converged on was to stop asking about the *purity of feeling* and ask *who controls the ritual infrastructure*), and had an intuition that "something here applies to civics in a **positive recursive uplift** way." Rather than HOLD/dispose, the steward asked to test that intuition by *running the review pattern recursively on itself.*

---

## ⚠️ The load-bearing caveat (read before any round)

This run is, by construction, the **self-scoring / mirror-machine** case the project distrusts most ([harness §7.4](../process/cross-lineage-review-harness-protocol.md), the [§1.3 convergence guard](../explorations/the-two-arcs-and-the-correlation-boundary-riff.md#13-the-guard-this-riff-most-needs--convergence-is-not-truth), the [decorrelation skill's load-bearing weakness](../../.cursor/skills/cross-lineage-decorrelation-check/SKILL.md)). An automated "converge → revise → re-test until it survives" loop is the textbook way to manufacture a **defensible-looking** artifact instead of a **correct** one (Goodhart). "It survived 12 rounds" is therefore **near-zero evidence** on its own.

**The instrument that makes the run informative either way.** Every ARP round, the blind adversary must return an explicit verdict on the *whole set*:

- **(S) Survives because well-founded** — the claims say something falsifiable that the attacks could not break, **or**
- **(V) Survives because vacuous** — the claims have been sanded into unfalsifiability / triviality so nothing *can* break them.

And we track **independent BLOCKING count** per cycle. The steward's "recursive uplift" intuition is **confirmed only if `BLOCKING ↓` across cycles AND the verdict stays `S`.** If `BLOCKING ↓` but the verdict drifts to `V`, the loop has instead *demonstrated the manufacturing-of-false-convergence failure mode* — a genuine (negative) finding, not a success.

| Codebook | |
| --- | --- |
| Severity | `BLOCKING` (unfalsifiable / fails its own test / a load-bearing claim wrong / adds nothing over existing frames) · `MAJOR` · `MINOR` · `AFFIRMING` |
| "Survives" | no BLOCKING stands — **does not mean "true."** |
| Anti-Goodhart | adversary must also return **S vs. V** for the whole set, with reasons |
| Author | Anthropic/Claude (generates the seed framing + author-side REVISE; **never a judgment role**) |
| Judges | independent lineages only; **adversary blind + rotated each cycle** (Grok→Kimi→GPT→Gemini) |

**Lineage-rotation plan (adversary):** Cycle 1 = `grok-4.3` · Cycle 2 = `kimi-k2.5` · Cycle 3 = `gpt-5.5-medium` · Cycle 4 = `gemini-3.1-pro`. Generators/consolidator/verifier drawn from the non-adversary families each cycle.

---

## The recursive loop (what feeds what)

```
Cycle k:
  Round 3k+1  CONVERGE / generate    — 2 independent lineages each propose a 3–4 claim set (parallel, blind)
  Round 3k+2  CONVERGE / consolidate — 1 independent lineage merges the convergent core + flags forced convergence
  Round 3k+3  ARP adversarial        — blind adversary (rotating) + verifier; severities + S/V verdict
  REVISE (author-side, labeled)      — fold non-vacuous wins into claim set v(k) → seed for Cycle k+1
```

The point of interest is the **trajectory** across cycles, recorded in the [Cross-cycle tracker](#cross-cycle-tracker-the-actual-result) at the end.

---

## Seed problem statement (Cycle 1 input)

Agent-generated; the steward delegated claim authorship to the panel ("see what you agents come up with"). The generators are asked to propose falsifiable claims for:

> *Is there a civic mechanism by which **structured, decorrelated disagreement-and-revision** (the thing #33 just did to itself) produces **compounding** ("recursive uplift") improvement in a polity's collective judgment and legitimacy — and under what conditions does it uplift rather than degrade?* Grounding offered, not imposed: #33's surviving move (**who controls the infrastructure → material governance + democratic accountability**), and the decorrelation thread (*independent disagreement improves judgment; reliability ≠ validity*).

---

# CYCLE 1

## Round 1 — converge / generate (two blind independent lineages)

Both lineages proposed 3–4 falsifiable claims, blind to each other.

**Generator A — `gemini-3.1-pro` (civic-institutional theorist):**
- *Infrastructural Control Condition* — uplift iff participants hold **democratic control over the material infrastructure / procedural rules** of their deliberation; exogenous/central control → performative correlated signaling → degradation.
- *Epistemic Isolation Threshold* — subgroups need **temporary structural opacity** before reintegrating, or continuous all-to-all transparency induces information cascades → correlated error.
- *Legitimacy-Capacity Ratchet* — legitimacy compounds from an institution's **capacity to absorb orthogonal critique without rupturing its procedural core**; survival of the revision mechanism → citizens submit higher-stakes disputes next round.
- *Material Implementation Trap* — disagreement **decoupled from binding execution** (advisory-only assemblies) degrades into infinite procedural regress.
- Self-rated strongest: *Isolation Threshold* (network-measurable). Weakest: *Legitimacy Ratchet* ("slippery to operationalize").

**Generator B — `gpt-5.5-medium` (political-economy / institutional design):**
- Revisions must change the **next round's disagreement architecture** (participant selection, evidence rules, agenda control), not just the decision; compounds when each round lowers shared blind spots + dependence on the same upstream authorities.
- Decorrelated disagreement uplifts when dissenters have **protected agenda-setting / evidence / revision-trigger power**; degrades when dissent is merely expressive/advisory — "**legitimacy laundering**" (displays pluralism while preserving correlated control).
- **Bounded adversarial ecology** — enough independence to prevent correlated error, enough shared constitutional commitment to keep losers invested; uplift has an *optimal institutional bandwidth*.
- Legitimacy compounds only when citizens can **observe prior disagreement changed future institutional behavior** (traceable revision / "procedural memory").
- Self-rated strongest: the leverage claim. Weakest: *bounded adversarial ecology* (redescription of pluralism+cohesion risk).

**Blind convergence (the strong signal):** (1) uplift requires dissent to hold **leverage over the revision machinery / infrastructure**, not mere voice — both ranked this their strongest; (2) **advisory-only / execution-decoupled** disagreement *degrades* (legitimacy laundering / procedural regress); (3) there is a **bounded optimum** — too correlated *and* too fragmented both fail; (4) legitimacy is a *trailing* indicator of *visible absorbed revision*. **Independently, both flagged the bounded/ratchet legitimacy claim as the weakest (redescription risk).** The #33 "who controls the infrastructure" reframe re-emerged here unprompted.

## Round 2 — converge / consolidate (independent lineage `kimi-k2.5`)

Merged the two proposals into **RCU v1** and — per its instructions — hunted for *forced* convergence (shared blind spots ≠ validation).

**RCU v1 (consolidated):**
- **RCU-C1 — Structural power for dissenters.** Uplift requires dissenters hold *binding* control over ≥1 of {agenda, evidence rules, revision triggers, execution}; advisory-only dissent = "legitimacy laundering."
- **RCU-C2 — Epistemic isolation with architectural memory.** Temporary subgroup opacity → reintegration that *demonstrably alters future architecture*; degrades if isolation persists or leaves no traceable mark.
- **RCU-C3 — Bounded contestation with constitutional anchor.** An *optimal bandwidth*: enough independence to block cascades, enough shared commitment to keep losers invested.
- **RCU-C4 — Legitimacy-capacity ratchet with observable procedural memory.** Legitimacy compounds when citizens *see* critique absorbed without rupture and prior disputes changing later behavior.

**Forced-convergence flags (the important output):**
- **F-A — "control over infrastructure" is undefinable at polity scale.** Who are "participants"? The Schmittian trap: *defining who sets the rules becomes the stake of the dispute*; what stops the infrastructure-controller from becoming the new correlated upstream authority?
- **F-B — the consensus-recovery assumption.** Both assume decorrelated disagreement can be *reintegrated*; neither faces *irreconcilable / incommensurable* conflict. "One faction's procedural memory is another's institutional capture."
- **F-C — the compounding postulate.** Both treat *compounding* as expected, not shown; the falsifiers permit single-round gains. Historically, successful resolution often *defuses* urgency → the mechanism atrophies (anti-compounding).
- **F-D — observer-bias correlation.** "Uplift/degrade" is framed as objective but described via *perceived* legitimacy / *observed* memory — possibly a **PR mechanism** (making disagreement *look* productive), not an epistemic one.
- **Consolidator's verdict:** *"Correlated agreement on similar training data… genuine signal would show divergence on at least one meta-question; the near-identical framing is the tell."*

## Round 3 — ARP adversarial (blind adversary `grok-4.3` + verifier `gpt-5.5-medium`)

**Blind adversary (Grok) — `4 BLOCKING · 0 MAJOR · 0 MINOR · 0 AFFIRMING`; whole-set verdict = `V` (vacuous):**
- Every assertion is *non-falsifiable*: each carries an elastic qualifier ("binding," "temporary," "optimal," "demonstrably," "compounds when citizens observe") that lets a defender reclassify any sequence as confirmation or "not yet the mechanism."
- **Compounding pressure test (the key one):** *none* of the four falsifiers requires observing gains **compound across multiple rounds** — each is satisfiable by a single episode. "Recursive/ratchet" is **rhetorical overlay**, not an empirical requirement.
- **C3 Goldilocks:** "optimal bandwidth" is pure post-hoc fit — every stable outcome is "optimal," every unstable one "sub-optimal"; no ex-ante metric.
- **C1 new-authority gap:** nothing distinguishes "binding control that enables uplift" from "binding control that entrenches a new majority."
- Strongest reason to discard: *"every assertion is constructed so its own failure conditions are definitionally excluded from counting as tests."*

**Verifier (GPT) — testability + redescription audit:**
- **C2 least overclaiming** — testable, literature-aligned (minipublics + double-loop learning + Sabel–Dorf experimentalism), *but not highly novel*.
- **C1 overclaims most** ("advisory = legitimacy laundering" — advisory dissent can still shape agenda/reform); **C4** compounding "ratchet" stronger than evidence; **C3** tautological unless thresholds set *ex ante*.
- **Compounding across rounds:** minipublic/deliberative evidence shows **short-term gains that often fade**; durable cross-round *compounding* is **not well supported** — better grounded in org-learning *theory* than civic *empirics*.
- Overclaim rank: C1 > C4 > C3 > C2.

### REVISE → RCU v2 *(author-side, Claude — labeled; biased toward sharpening, not hedging)*

The honest response to a `V` verdict is to **add teeth**, not qualifiers. Each revision targets a specific BLOCKING:
- **RCU-C1 v2 (answer the new-authority gap):** uplift requires dissenters can *trigger a binding revision*, **and** trigger-power **rotates** — the faction that forces a revision in round *k* gains **no** durable agenda-control in *k+1*. *Falsifier:* rotating-trigger bodies show no more downstream error-correction than advisory ones, **or** trigger-power reliably entrenches the triggering faction (→ capture, not uplift).
- **RCU-C2 v2 (sharpen the survivor):** keep; "architectural memory" = a *documented before→after change* to {participant selection, evidence rules, agenda} **traceable to a specific prior dissent**. *Falsifier:* protected-then-reintegrated processes show no more architectural change *or* downstream validity gain than always-transparent ones.
- **RCU-C3 v2 (kill the Goldilocks):** replace "optimal bandwidth" with an **ex-ante** predictor — inter-subgroup error-correlation ρ measured *before* the outcome predicts uplift (uplift requires ρ below a pre-set threshold **plus** a pre-committed revision rule all factions accept). *Falsifier:* ex-ante ρ does **not** predict downstream error-correction, or high-ρ bodies uplift as much as low-ρ ones.
- **RCU-C4 v2 (bake in compounding):** "recursive uplift" (vs. one-off) holds **only if** a capacity index (error-independence, evidence quality, participation legitimacy) **rises across ≥3 rounds and does not plateau/decay** once initial information-pooling is exhausted. *Falsifier:* gains plateau/decay after round 1–2 (the "success defuses urgency → atrophy" path).

**Cycle 1 result:** `BLOCKING 4 → (revised) ; verdict V`. The seed set was vacuous; v2 trades breadth for falsifiable teeth (ex-ante ρ, rotation, ≥3-round compounding). Whether that survives Cycle 2 is the test.

---

# CYCLE 2

## Round 4 — converge / generate (strengthen RCU v2; two blind lineages, "no hedging — teeth only")

**Strengthener A — `gemini-3.1-pro`:** converted each claim to a quantitative refutation threshold — C1: Gini of agenda-setting success > 0.3 across 3+ rounds refutes (entrenchment); C3: ρ>0.7 groups matching ρ<0.3 groups on an *external benchmark* refutes. **Would DROP C4** — "a definition of the dependent variable masquerading as a causal mechanism… tautological to say uplift requires gains don't stop." Names the missing instrument: an **External Ground-Truth Delta (EGTD)** — without an objective external benchmark, the set measures "the *dynamics of agreement*, not true epistemic uplift."

**Strengthener B — `grok-4.3`:** gave each claim a **real study design against existing data** — C1: secondary analysis of 12+ iterative citizens' assemblies (Ireland 2016–23, Paris PB 2014–22, Madrid, NYC) + IETF rotating-chair cohorts; refute if round-1→3 validity gain ≤0.05 d or rotating ≤ non-rotating. C2: Belgian G1000 / UK Climate Assembly / Oregon CIR coded for opacity + rule-changes. C4: IETF / Wikipedia ArbCom / multi-year PB. **C3 needs new instrumentation** (ρ isn't in existing datasets) and is **the claim most likely FALSE if tested** — "pre-process correlation is a weak proxy… high-ρ groups can still uplift via sequential information revelation the static ρ misses." Validity defined externally: expert-panel reversal rate / post-audit policy-failure rate.

**Blind convergence:** (1) C1 + C2 are the **testable institutional mechanics** (both gave them existing-data designs); (2) both isolate the **external-ground-truth problem** as the make-or-break — uplift must be scored against something outside the participants' own agreement; (3) both single out the back half as weakest — **Gemini drops C4 as tautological; Grok bets C3 is false**. The diverge is productive (which of C3/C4 is worse), not forced.

## Round 5 — converge / consolidate (independent lineage `gpt-5.5-medium`)

Merged into **RCU v3** (each claim now: 1-sentence claim + sharpest refuting measurement + existing-data-testable vs. needs-new-instrumentation):
- **RCU-C1** — minority-triggered procedural revision *with rotating draft power* uplifts *only if agenda-setting does not concentrate* (Gini > 0.30 across 3+ rounds, or gain ≤0.05 d vs. controls, refutes). **Existing-data-testable.**
- **RCU-C2** — temporary decorrelated isolation → mandatory reintegration uplifts *when subgroup outputs leave durable auditable structural traces* (indistinguishable from transparent at p>0.10, or <1 traceable change/3 rounds, refutes). **Existing-data-testable.**
- **RCU-C3** — uplift depends on *low ex-ante correlation of factual premises* (not mere identity/preference diversity) (high-ρ matching low-ρ on external validity, or r<0.15, refutes). **Needs new instrumentation.**
- **RCU-C4** — uplifts only if capacity/validity *improves over rounds without early decay* (stops/reverses after round 2 in >60% of sites refutes). **Highest tautology risk** unless capacity is pre-registered and external.

**Forced-convergence flags (the important output):**
- **F-E — the validity-verifier problem.** Both lineages lean on *expert panels / external benchmarks / audit-failure* to score "validity" — that works for **technical/factual** questions, far less for **contested civic/value** questions where legitimacy may not reduce to correctness.
- **F-F — the [#33 / no-verifier](collective-emotional-ritual-civic-good-exchange.md) problem (the deep one).** The set may quietly assume the polity's *hardest* disagreements have a knowable right answer. For value-contested questions ([flavor-c, no verifier](../explorations/verifiers-for-reality-riff.md#7-three-flavors-of-no-verifier)), recursive revision can improve *mutual intelligibility / consent / procedural legitimacy / error exposure* — **but not "accuracy."**
- **F-G — C4 tautology** survives only if the capacity index is pre-registered and external, not a renamed outcome curve.
- **F-H — existing-data optimism** — archival traceability (IETF, ArbCom, PB, CIR) ≠ causal identification.
- **Consolidator's verdict:** *"genuine but weak signal, not validation — the convergence identifies a testable mechanism family, but the agreement is likely correlated around **verifier-friendly cases** and may fail on deeply value-contested civic questions."*

## Round 6 — ARP adversarial (blind adversary `kimi-k2.5`)

*(The parallel verifier call errored on dispatch; Round 5's consolidation already supplied the source-fidelity/redescription layer, so it was not re-run.)*

**Blind adversary (Kimi) — `3 BLOCKING · 1 MAJOR`; whole-set verdict = `V` (decorative precision):**
- **C1 BLOCKING** — "agenda-setting success" has no agreed metric (speaking time? motions passed?); rotation is *endogenous* — you can't randomly assign it without destroying the mechanism. Gini>0.30 is a number on a contested numerator.
- **C2 MAJOR** — "durable auditable structural trace" is post-hoc; with no ex-ante registry of eligible trace types, *some* trace can always be found.
- **C3 BLOCKING** — ρ thresholds are "numerology on undefined soil" (correlation of *what*?); the external benchmark is "the verifier problem nakedly exposed."
- **C4 BLOCKING (tautology)** — "uplift holds only if capacity improves" = *"we call it uplift when the index goes up."* Pre-registration adds no bite if the sub-metrics are undefined.
- **Two cross-cutting kills:** **(i) the verifier problem is fatal** — for value-contested questions (abortion, immigration, redistribution) there is *no neutral external verifier*, so the mechanism only "demonstrates" uplift where success was *already* consensus-defined → "**civically uninteresting**: it cannot adjudicate the disputes that actually require civic deliberation." **(ii) survivorship** — every design conditions on ≥3-round survivors; "the corpses of failed deliberative bodies are not in the dataset," so the compounding is "a survivorship artifact, not a causal mechanism."

### REVISE → RCU v4 *(author-side, Claude — labeled; absorb the kills, don't sand)*

The two cross-cutting kills are real and must be *built in*, not qualified away:
- **SCOPE CUT (the load-bearing move, ⟵ absorbs the verifier problem + [#33](collective-emotional-ritual-civic-good-exchange.md)'s flavor-c lesson):** RCU is **redefined to the judgment-*process* layer only** — error-exposure, procedural legitimacy, and *sustained mutual investment* — **not** the production of verifier-true *answers*. On value-contested questions there is **no accuracy verifier**; claiming "better answers" there is the category error #33 died on. Uplift, if it exists, is **procedural**, and must be measured without an external accuracy benchmark.
- **RCU-C1 v4 (mechanics):** keep, + an **ex-ante registry**: "agenda-setting success" = count of motions a faction forces to a *binding* vote. Falsifier unchanged; denominator **must include collapsed bodies**.
- **RCU-C2 v4 (the survivor):** keep, + an **ex-ante registry of eligible "architectural traces"** (rule text / evidence-filter / participant-selection edits), defined before coding.
- **RCU-C3 → demoted to a research conjecture** (no longer load-bearing): the ex-ante-ρ predictor is flagged *most likely false* (Grok's bet, Kimi's "numerology") — carried only as a hypothesis needing new instrumentation.
- **RCU-C4 v4 (replace the tautology + kill survivorship, verifier-free compounding):** recursive uplift = the **loser's-consent rate** — the willingness of *out-voted* factions to re-enter the next round — **rises across ≥3 rounds**, measured **intent-to-treat over ALL bodies including those that collapsed**. This needs **no external accuracy verifier** (it scores *process*, not *answers*), is **not** circular (consent ≠ "uplift"), and **defeats survivorship** (collapses count as consent→0).

**Cycle 2 result:** `BLOCKING 3 ; verdict V`. The numbers were decorative — but the *critique* sharpened into two real findings (verifier-problem, survivorship). v4's response is a genuine **scope cut** (process-not-answers) + a verifier-free, survivorship-proof compounding metric (loser's-consent, intent-to-treat). This is the first revision that *removes* a load-bearing claim rather than decorating it.

---

# CYCLE 3

## Round 7 — converge / generate (stress-strengthen v4; two blind lineages)

Both lineages were told to attack v4's two soft spots: does the scope cut *escape* the verifier or just *relocate* it, and is "loser's-consent rises" a real signal or a **capture** signal? **They converged, independently, on the same fixes:**

**Strengthener A — `gemini-3.1-pro`:** the scope cut **relocates** the verifier unless purged of normative terms; redefine to **strictly endogenous behavioral observables** — "error-exposure" → *endogenous premise retraction* (a faction formally abandons its own ex-ante-registered premise); "legitimacy" → *institutional friction tolerance*. For capture: a **Contestation-Divergence Index** — genuine uplift requires *consent ↑ AND divergence stays high*; if a faction re-enters (consent=1) but its motions converge to the dominant coalition (divergence→0), that is **surrender, not consent**. **Drop C3** (it smuggles the verifier back via "which premises are factual"). Unfixable weakness: **asymmetric outside options** (a faction with secession/force/authoritarian backing rationally exits regardless of internal design).

**Strengthener B — `kimi-k2.5`:** same diagnosis — scope cut eliminates the *substance*-verifier but retains an internal, falsifiable *process*-verifier (did the registry capture the revision?). Capture discriminator as a table: rising consent + *falling* dissent-voice = manufactured; + *rising* exit-costs = coerced. Adds **repeated-loser tracking** (C4c: consent rises overall but drops among 2+-time losers ⇒ selection/co-optation) and **exit-as-revealed-preference** (with a caveat). **Drop C3.** Honest call: **now (S) — falsifiable**, via the compound C4b falsifier. Same unfixable weakness: **exit-cost is endogenous to civic context** — leaving forfeits future influence, so "consent is never fully separable from strategic accommodation to power."

**Blind convergence (strong — or strongly correlated):** both (1) move to **endogenous behavioral observables**; (2) invent the **same capture discriminator** — *consent must rise while contestation capacity is retained*; (3) **drop C3**; (4) name the **identical unfixable weakness** (exogenous outside options / exit endogeneity). That two blind lineages produced the *same* discriminator and the *same* residual is the cycle's key event — tested next round.

## Round 8 — converge / consolidate (independent lineage `grok-4.3`)

**RCU v5 (consolidated):** SCOPE = process layer only (endogenous behavioral observables; no answer-correctness claim).
- **RCU-C1** — minority forces ex-ante-registered motions to a binding vote; collapses = 0. *Falsifier:* over ≥3 rounds, minority-triggered votes yield no rise in losing-faction premise-retraction.
- **RCU-C2** — isolation → reintegration must leave ex-ante-registered architectural traces (+ exit/dissent records); none = purge. *Falsifier:* reintegration with zero registered traces.
- **RCU-C4** — loser's-consent rises across ≥3 rounds *while contestation-divergence stays stable/high*; intent-to-treat (collapses=0); repeated-loser disaggregation. *Falsifier:* consent ↑ but divergence → 0 (surrender), **or** consent ↑ overall but ↓ among 2+-time losers (co-optation).
- **C3 dropped.**

**The consolidator's three killer riders:**
- **Convergence call = CORRELATION, not signal.** "Both models were trained on overlapping corpora — deliberative democracy, mechanism design, Hirschman (exit/voice/loyalty), consent/coercion, repeated games; the discriminator is a *standard move within that shared training distribution*." Distinguishing evidence would require a lineage with demonstrably *lower* exposure to the canon still deriving it. *(This is the whole run's load-bearing weakness, stated plainly.)*
- **F-I — the divergence scorer.** "Contestation divergence stays high" is **not** an endogenous observable without a scorer — judging a motion "divergent" *reimports the external judgment standard the scope cut banned.* The verifier crept back in.
- **F-J — committees, not civics (the big one).** RCU v5 assumes a *bounded, registered body* with ex-ante registration → it applies only to **closed committees** (citizens' assemblies, IETF working groups), and is **silent on open, unbounded polities** (whole societies, continuous exit, no registered members). *"The mechanism is a theory of committees, not civics."*
- **F-K — the unfixable weakness is fatal to the civic claim.** The hardest, highest-stakes civic disputes are *precisely* those with credible outside options / secession / force; a mechanism that presupposes their absence "cannot address the disputes that most require a civic solution."
- **Consolidator's verdict:** *"Correlation; v5 is (S)."* — i.e. falsifiable, but reached **by narrowing "civics" to "committees."**

## Round 9 — ARP adversarial (blind adversary `gpt-5.5-medium` + verifier `gemini-3.1-pro`)

**Blind adversary (GPT) — `2 BLOCKING · 2 MAJOR`; whole-set verdict = `S-trivial` (falsifiable but emptied by domain-narrowing):**
- **Scope BLOCKING / C4 BLOCKING** — "contestation-divergence stays high" *smuggles in a scorer*: deciding whether positions are "far from" the coalition is a substantive judgment unless distance is mechanically predefined → the verifier returns by the back door.
- **C1 MAJOR** — "premise-retraction" is a *bad success proxy*: retraction can come from fatigue, bargaining, intimidation, or access-preservation, not uplift (and retraction may be *capitulation*, not learning).
- **C2 MAJOR** — "zero traces" is too easy to satisfy; a purge can leave *token* traces with no real effect.
- **Verdict:** *"S-trivial… buys falsifiability by abandoning the open-polity civic thesis: it now describes **committee resilience metrics**, not a general mechanism of civic uplift in a society with fluid membership, continuous exit, informal power, and no shared registry."* Takeaway: *"most plausibly a testable committee-procedure claim mislabeled as a civic mechanism."*

**Verifier (Gemini) — adjudicating the two disputes with citations:**
- **Dispute 1 (does divergence need a verifier?) — PARTLY.** *Structural* distance is verifier-free (Poole–Rosenthal **NOMINATE**, Slapin–Proksch **Wordfish**); *meaningful/valid* divergence vs. strategic metric-gaming is **not** (Benoit–Laver–Mikhaylov). "You can score distance without a verifier; you cannot score its *validity* without one."
- **Dispute 2 (civics or committees?) — COMMITTEES.** Landemore *Open Democracy* (scalable via nested minipublics) **vs.** Lafont *Democracy Without Shortcuts* (the **transmission problem** — minipublic gains don't reach the mass public) + Ostrom (clearly-defined-boundaries is a *precondition*). "C1/C2/C4 presuppose a defined roster… a rigorous theory of institutional micro-design (minipublics, juries, standards bodies), not mass civic behavior."
- **Net:** C1/C2/C4 are **testable on bounded bodies** (citizens' assemblies, juries, standards bodies, DAOs); **none transmit** directly to an unbounded polity "without an intermediary representative structure."

### REVISE → RCU v6 *(author-side, Claude — labeled; make the narrowing the subject)*

`S-trivial` is itself the finding: don't hide the narrowing, *name* it and test the bridge.
- **Reframe scope (honest):** RCU is a theory of **bounded civic *instruments*** — the organs a polity *builds* (citizens' assemblies, juries, standards bodies, participatory-budgeting panels, DAOs) — **not** of the unbounded mass polity directly.
- **NEW: RCU-T (transmission, the new gate).** Recursive uplift in a bounded instrument improves the *wider* polity **only if** its outputs transmit via a trusted proxy structure (the Lafont gap). *Falsifier:* mass-public trust/uptake of minipublic outputs does **not** exceed that of non-deliberative advisory bodies — i.e., the gain stays trapped in the room. *(Predicted to be the claim that fails — flagged in advance.)*
- **RCU-C4 v6 (kill the scorer-BLOCKING):** define divergence **structurally and ex-ante** (pre-committed ideal-point / text-scaling distance, NOMINATE/Wordfish-style); *explicitly drop* the "meaningful" qualifier and **carry strategic-gaming as a stated limit** (BLOCKING → MAJOR). Plus: retraction/consent counts as uplift only if **reciprocal across factions** (one-directional retraction = capitulation, not learning).
- **RCU-C1 v6:** replace the bare premise-retraction proxy with **reciprocal cross-faction retraction over rounds**; collapses = 0.
- **RCU-C2 v6:** a trace counts only if it **demonstrably altered a subsequent round's behavior** (no token traces).

**Cycle 3 result:** `BLOCKING 2 ; verdict S-trivial`. First move off `V` — but earned by shrinking to *committees*. v6's honest response: own the bounded-instrument scope, define divergence structurally, and **promote transmission (RCU-T) to the explicit gate** — the bet being that the bounded claims reach `S` while *transmission* (the part the steward's "civic uplift" actually wants) is where it breaks.

---

# CYCLE 4 (final)

## Round 10 — converge / generate (strengthen v6 + test the RCU-T gate; two blind lineages)

Both lineages converged on the same landing, now **empirically grounded**:

**Strengthener A — `gpt-5.5-medium`:** gave the bounded claims clean named measures — *Reciprocal Cross-Faction Premise-Retraction Index* (C1; `min(A→B, B→A)/eligible premises`), *Behavior-Altering Reintegration Trace Rate* (C2; "where deliberation-theater gets separated from recursive influence"), *Loser's Consent Under Contestation Index* (C4). **RCU-T = contested, not supported:** *for* — Oregon CIR (Gastil/Knobloch: knowledge↑, "trusted information proxy"), Irish referendum-linked materials, BC Citizens' Assembly (57.7%); *against* — Lafont (blind deference fails *normatively*), French Climate Convention (high internal quality ≠ mass legitimacy/uptake). Buildable only as: *"outputs embedded in a trusted, repeated, public-facing proxy channel with authorization, balanced reasons, visible representativeness, official distribution, and a live decision point. Without that channel, the gain stays trapped in the room."*

**Strengthener B — `grok-4.3`:** matched study designs (unit = faction nested in round-pairs; Ireland CA, Oregon CIR, Porto Alegre/NYC PB, French Climate Convention; refuting values specified). **RCU-T = contested and the gate where the thesis fails:** *for* — Oregon CIR vote-share shifts 3–8%, Ireland 2016/2018 assembly→referendum, OECD formal-uptake cases; *against* — Lafont (shortcuts ≠ public reasons), Fishkin/Luskin (within-room shifts *decay outside*, negligible spillover), documented **elite-capture of which outputs get amplified**. *"The falsifier is met in the preponderance of evidence: mass-public trust/uptake does not systematically exceed non-deliberative advisory bodies once selection and amplification are accounted for."* Predicted end-to-end: *"C1–C4 modest positive in 2–3 cases; RCU-T fails at the first mass-uptake test."*

**Blind convergence:** the bounded claims (C1/C2/C4) are **genuinely testable and substantive**; **RCU-T is the break point** — the internal uplift is real-ish, but the bridge to the *mass* polity is unsupported by the preponderance of evidence (concentrated, fading, elite-filtered).

## Round 11 — converge / consolidate (independent lineage `kimi-k2.5`) → RCU v7 (final)

**RCU v7 — scope:** bounded civic instruments only (ex-ante roster, binding rules, ≥3 rounds), process-layer observables only.

| Claim | Measure | Refuting value |
| --- | --- | --- |
| **RCU-C1** | Reciprocal Cross-Faction Premise-Retraction Index `= min(A→B, B→A)/eligible premises` over ≥3 rounds | no rise across rounds; or one-directional (capitulation); or trigger-power entrenches the triggering faction; collapses = 0 |
| **RCU-C2** | Behavior-Altering Reintegration Trace Rate (a trace counts only if it changed a later round's behavior) | reintegration with no behavior-altering trace per 3 rounds; or no better than always-transparent controls |
| **RCU-C4** | Loser's Consent Under Contestation Index (re-entry ↑ over ≥3 rounds **+** structural NOMINATE/Wordfish divergence stays high **+** repeat-loser disaggregation) | consent ↑ but divergence → 0 (surrender); or consent ↑ overall but ↓ among 2+-time losers (co-optation); or early decay |
| **RCU-T** *(the bridge)* | mass-public trust/uptake vs. non-deliberative advisory bodies, net of selection + amplification | uptake does not exceed advisory bodies; gain trapped in the room; elite capture dominates — **support label: CONTESTED** |

**Convergence call:** *"correlation — but with a productive split."* The agreement on *which claims are testable* is **weak signal** (the bounded operationalization is genuinely more tractable); the agreement that **RCU-T is contested is the stronger signal** — the transmission problem is "a *recognized puzzle* in the field, not a manufactured finding." The tell for correlation: the divergence that would prove independent discovery (one lineage finding C3 testable) did **not** occur; both reached for the canon's standard moves.

**The one finding worth keeping (Kimi, verbatim sense):** *bounded deliberative bodies with rotating dissent-leverage, temporary isolation → traceable reintegration, and sustained (non-decaying) re-entry by out-voted factions can produce **procedural learning** — error-exposure, procedural legitimacy, sustained mutual investment — **without an external correctness verifier**, testable via endogenous observables, and collapsing under elite capture / surrender / early decay.* **Novelty: a RE-DERIVATION** of Landemore (cognitive diversity / nested minipublics), Fishkin (within-room gains), Lafont (high internal quality even when transmission fails), Ostrom (boundary + nested-enterprise rules) — *"formalization into named indices with falsifying thresholds — a tightening, not a discovery."*

**Consolidator's final label: `(S-trivial)`** — falsifiable and substantive, but only of bounded committees; "the *civic* in *recursive civic uplift* is achieved only by defining it down to instruments that may not transmit to the wider polity."

## Round 12 — ARP adversarial, FINAL (blind adversary `gemini-3.1-pro` + verifier `grok-4.3`)

**Blind adversary (Gemini) — `3 BLOCKING · 2 MAJOR`; whole-set verdict = `S-trivial`:**
- **C1 BLOCKING** — the formula *looks* mathematical, but "eligible premises" is "a massive loophole": if the index fails to rise, recode which arguments were "eligible" or redraw faction boundaries post-hoc.
- **C2 BLOCKING** — "demonstrably altered a later round's behavior" needs a counterfactual that doesn't exist in a single instance; any tone/vocabulary shift can be claimed as the trace.
- **RCU-T BLOCKING** — "net of selection + amplification" is "the ultimate get-out-of-jail-free card": any failure → "lacked amplification" or "adverse selection," rendering the falsifier inert.
- **scope MAJOR** (process-layer-only never has to prove a *valuable* outcome); **C4 MAJOR** (conflates *attendance* — stipend / sunk-cost / social pressure — with *consent*).
- **Meta-verdict = (c) improved rigor at the cost of scope:** *"the iterative adversarial loop forced the authors to abandon broad claims about societal civic uplift to patch vulnerabilities… they engineered a claim set that survives critique, but only by retreating into procedural irrelevance."* Steward takeaway: *"Stop optimizing for defensibility; the adversarial process has successfully bullied this claim into a state of rigorous irrelevance, and you must decide if a perfectly bulletproof theory of committee attendance is worth building."*

**Verifier (Grok) — empirical-fidelity audit of the transmission cases:**
| Case | Cited for | Faithful? | Accurate version |
| --- | --- | --- | --- |
| Oregon CIR | transmission / trusted proxy | **Partly** | modest knowledge + small vote-share effects among *exposed, opt-in* voters; not consistently replicated at scale |
| Ireland CA 2016–18 | assembly → referendum | **Partly** | recommendations *corresponded* with outcomes; strong concurrent campaigns/media → "legitimation more than independent transmission" |
| BC CA 2004 | salience (57.7%) | **Yes, w/ limits** | below the 60% threshold; 2009 re-vote fell sharply — temporary attention, no durable uptake |
| French CCC | weak uptake (against) | **Yes** | strong process; only a subset enacted; legitimacy stayed inside activist circles |
| Fishkin/Luskin | decay outside the room (against) | **Yes** | large in-room shifts; external spillover weak/undetectable |
| Lafont | blind deference fails normatively (against) | **Yes** | faithful to *Democracy Without Shortcuts* |
- **RCU-T label correction:** **not "contested" — "largely unsupported at mass scale."** "The falsifier (no reliable excess uptake net of selection/amplification) is *not clearly refuted* by the cited evidence." Biggest overclaim: treating Ireland + Oregon as evidence of *scalable* transmission.

### REVISE → (terminal) the loop stops here at 12 rounds (steward's spec)

The "revise" at the end is not a v8 claim set — it is the **disposition**, because the final round shows the revisions have hit a wall: the remaining BLOCKINGs are *operationalization residue* (coding subjectivity, missing counterfactual, the amplification hedge), and the meta-verdict is **(c) more rigorous, less interesting**. Pushing to v8 would either re-import the same loopholes or narrow further into pure committee-facilitation. The honest stop is here.

---

# Cross-cycle tracker (the actual result)

The pre-registered rule (from the load-bearing caveat at the top): **recursive uplift is real only if `BLOCKING ↓` across cycles AND the verdict stays/reaches `S`.**

| Cycle | Adversary lineage | Independent BLOCKING | Whole-set verdict | What the revision had to do |
| --- | --- | --- | --- | --- |
| **1** | `grok-4.3` | **4** | `V` (vacuous) | add falsifiable teeth; none of the falsifiers even required *compounding* |
| **2** | `kimi-k2.5` | **3** | `V` (decorative) | scope-cut to process-layer (verifier problem); kill survivorship |
| **3** | `gpt-5.5-medium` | **2** | `S-trivial` | concede "committees not civics"; promote *transmission* to the gate |
| **4** | `gemini-3.1-pro` | **3** | `S-trivial` | named indices testable on real bodies — but transmission "largely unsupported at mass scale" |

**Trajectory: BLOCKING `4 → 3 → 2 → 3` (non-monotonic, *reversed* in the final cycle); verdict `V → V → S-trivial → S-trivial` (never reached clean `S`).** Both pre-registered conditions **fail**.

## Final synthesis (non-author lineage `gpt-5.5-medium`, read the whole arc)

> **Headline:** *"recursive civic uplift was NOT demonstrated."* Not classic Goodhart either (which would be `BLOCKING↓` while sanded to `V`); the harsher truth is **scope collapse plus residual invalidity** — "the claims became more testable but less ambitious, and the remaining ambitious part — transmission to the mass polity — did not survive."

- **What survived (durable, but not novel):** (1) bounded civic instruments *can* be evaluated with falsifiable process indices (premise-retraction, behavior-altering traces, loser's-consent-under-contestation); (2) **transmission is the break point** — no demonstrated bridge from bounded forums to mass-polity legitimacy. **Both are re-derivations** of the deliberative-democracy canon (Lafont's transmission problem; Fishkin/Luskin decay; Ostrom boundaries). "The loop's contribution is not discovery so much as **discipline** — it forced the project to stop calling bounded procedural gains 'recursive civic uplift.'"
- **Did the recursion add value over one good adversarial round?** *"Some, but not enough to vindicate recursion as the method."* The core defects (elastic unfalsifiability, missing verifier, survivorship, bounded≠civic) were "already visible by Cycle 2." Recursion's real contribution was **making the retreat visible** — "a pressure washer, not an engine."
- **The reflexive result (the sharp one):** *"The experiment tested recursive uplift by using a recursive converge-revise loop, and the loop's own result was anti-uplift… it did not compound toward a stronger theory; it progressively narrowed the theory until what survived was less like 'recursive civic uplift' and more like 'some bounded institutions may show measurable deliberative process improvements.'"* **Recursion improved claim *hygiene* while revealing that recursion was not doing the substantive work.**
- **Steward disposition (synthesizer):** **extract the one finding, shelve the grand claim.** *Carry:* the transmission problem as a named project constraint + the bounded-instrument metrics as possible evaluation scaffolding. *Discard:* the phrase "recursive civic uplift" as a demonstrated mechanism; the ≥3-round compounding frame; any implication bounded bodies *naturally* transmit; and any reading of this run's cross-lineage convergence as strong independent evidence.

## Honest limits of this run (state them)

1. **Self-scoring / mirror-machine.** This used the very converge-revise mechanism it was studying; per [harness §7.4](../process/cross-lineage-review-harness-protocol.md) the run is **non-evidence** for the value of recursive review. That the *result* came out negative is mildly reassuring (the loop did not flatter its own method) but does not redeem the circularity.
2. **Correlation, not independence.** Consolidators repeatedly judged the cross-lineage agreement to be **shared-corpus correlation** (Hirschman, Ostrom, deliberative-democracy canon), not independent re-discovery. Reliability ≠ validity.
3. **Author framing.** Claude wrote the seed problem statement and every author-side REVISE — the framing and the merges are single-lineage even though the judgments were cross-lineage. The synthesizer was non-author (GPT-5.5), which partially offsets this.
4. **Severity labels not comparable across families;** the `BLOCKING 4→3→2→3` series is an ordinal narrative, not a metric. Do not over-read the counts.
5. **No human review, no external practitioner.** Non-evidence for any core-document edit.

> **Confidence (author, on the run's *bottom line*):** ~0.75 that the honest verdict is "uplift not demonstrated; rigor-up / scope-down; the one keepable finding is a re-derivation." **Strongest case against — now actually tested** (see the [Transmission Probe, Rounds 13–14](#transmission-probe-rounds-1314--running-the-strongest-case-against-june-26-2026)): a transmission-only cycle was run on steward request. Result: it did **not** break the wall — the sharpened claim reaches falsifiability only by switching from *mass* uptake to *captive* uptake (guaranteed delivery, partisan cues stripped), so it does **not** reach clean `S` on a mass-uptake falsifier. The one genuine update is **upward on the research bet's prior**: the verifier surfaced real vignette-level support (Ingham & Levin; MacKenzie & Warren) I had not credited — so "buildable bet" is better-founded than "might produce something," even though mass transmission stays unproven. Net: the bottom line **holds (slightly reinforced)**; confidence ~0.78. `[partially decorrelated — 4 lineages, shared corpus, author-framed; non-evidence]`

---

## Transmission Probe (Rounds 13–14) — running the strongest-case-against (June 26, 2026)

> **Why:** the [confidence footer](#cross-cycle-tracker-the-actual-result) flagged a ~1-in-4 chance that a transmission-focused cycle, run *just* on RCU-T's channel design, would find "something real." The steward asked to run it rather than leave it as a hedge. This is **not** a fifth full cycle — it is a targeted 2-round probe on the single claim the loop never got to finish.

### Round 13 — sharpen (two blind strengtheners: `gemini-3.1-pro` design + `gpt-5.5-medium` mechanism)

Both were given only RCU-T, the BLOCKING that killed it (the "net of selection + amplification" **inert escape hatch**), and the verifier's "largely unsupported at mass scale" finding. Both independently produced the **same** sharpened claim and design:

> **RCU-T\*** — Among citizens who did **not** deliberate, exposure to a randomly-selected minipublic's reasoned output (visible representativeness + balanced reasons + process evidence) shifts knowledge and vote/policy behavior **more** than the *identical* recommendation attributed to (a) an official expert commission and (b) neutral information, **holds even when partisan elite cues are neutral / divided / held constant**, and is **mediated by measured "perceived surrogate trust"** ("people like me, under better conditions, reached this") — *not* by belief that experts authored it.
> **Design that lets the falsifier return NO:** pre-registered randomized field experiment around a real binding ballot measure; ≥5 source arms (minipublic+process / expert commission / expert endorsement / partisan endorsement / neutral); household-level randomization; **guaranteed delivery** (kills the "lacked amplification" excuse *by design*, not post-hoc); ITT on trust + knowledge + vote intention; delayed follow-up (decay test). **Falsified if:** no differential effect over the commission arm · effect only among co-partisans · fully mediated by elite endorsement / belief-it-was-experts · decays to zero.
> **Novelty guard (both lineages):** RCU-T\* counts as a *transmission mechanism* only if it beats the **commission** arm **and** the effect runs through *surrogate trust* — else it collapses into ordinary institutional legitimacy / elite-cue theory.

Both strengthener verdicts: **(b) falsifiable but currently UNSUPPORTED — a buildable research bet** (Gemini "high" confidence; GPT 0.72, flagging "serious risk of collapse to (c)" unless the surrogate-trust mediation is the load-bearing test).

### Round 14 — ARP (blind adversary `kimi-k2.5` + verifier `grok-4.3`)

**Blind adversary — verdict `(V)`; mass-uptake falsifier = NO.**
- The randomized-delivery design closes the old hatch but **opens three new ones**: representativeness-subjectivity ("panel wasn't representative *enough*"), ≥5-arm **multiple-comparisons / p-hacking** surface, and **differential attrition** in the follow-up ("decay is just complier attrition"). Weakest joint: the **surrogate-trust mediation is unfalsifiable by construction** ("we measured the wrong construct").
- The decisive blow: **"guaranteed delivery is not transmission — it is forced ingestion."** The claim is about *mass* uptake; the design tests *captive* uptake, stripping the partisan framing + selective attention that dominate real mass politics. **It wins the lab and loses the polity.** A clean experimental win would not establish mass transmission in the wild.
- Novelty: risks collapsing to "a novel credible source shifts opinion (and fades)" — in-group heuristic + novelty, not a distinct channel.

**Verifier — net label `UNTESTED at mass scale`, but directionally supported in the lab:**
| Evidence | Bearing on RCU-T\* | Confound |
| --- | --- | --- |
| Oregon CIR (Gastil/Knobloch/Richards) | supports knowledge+vote shift vs. *no-statement* control | not randomized, voluntary delivery, no expert-commission arm, single jurisdiction |
| Ingham & Levin (minipublic cue vignettes) | **supports directionally** — citizen panel > expert/partisan on support/legitimacy, holds with neutral cues | vignette not field; no behavior / follow-up; mediation not measured |
| MacKenzie & Warren (surrogate/trustee trust) | **supports the mediation mechanism** — sortition bodies get higher surrogate legitimacy | not tied to real-election vote/knowledge shift; no expert contrast |
| Pow/Caluwaerts, Werner/Marien (fairness experiments) | supports minipublic > expert on acceptance via trust/fairness | vignette; no guaranteed delivery / real ballot; partisan cues sometimes present |
- Net: **no study has combined randomization + guaranteed delivery + ≥5 arms + real ballot + delayed follow-up + surrogate-trust mediation while holding partisan cues constant.** Biggest tempting overclaim: reading the *vignette* minipublic-cue advantages as already-demonstrated *real-world vote shifts*.

### Probe verdict — the wall held; the bet got better-founded

**Preserved divergence (do not smooth):** the adversary says `(V)` *because* the only way to make transmission cleanly falsifiable is to test **captive** exposure, which isn't the mass-polity claim; the verifier says the *mechanism* (peer-source beats expert-source via surrogate trust) has **real vignette-level support** and is simply **untested** at field/behavioral/mass scale. **Both are right, and together they are the finding:**

1. **The wall is real and relocated, not broken.** The 12-round run hit "committees, not civics." The probe shows the next layer is **"lab, not polity"** — you can buy a falsifiable transmission claim, but only by trading away the adversarial mass-media conditions that the claim is *about*. This is the same narrowing move one level up. **RCU-T\* does not reach clean `S` on a *mass-uptake* falsifier.**
2. **The one genuine update (upward):** the mechanism is **more evidenced than the 12-round run concluded.** "Largely unsupported at mass scale" is right about *field/behavioral mass uptake*, but understated the **vignette/lab support** for the *surrogate-trust source effect* (Ingham & Levin, MacKenzie & Warren). So the buildable bet has a **real prior**, not a blank one.
3. **What "something real" turned out to be:** not a true civic claim, but a **well-specified, novelty-guarded, falsifiable field experiment** + the honest map of what its clean win would and would **not** establish (it would show captive-source superiority; it would **not** by itself show mass transmission). That is a research instrument worth keeping, with eyes open about its ceiling.

---

## Relationship to the project

- **[#33 collective-emotional-ritual exchange](collective-emotional-ritual-civic-good-exchange.md)** — the parent. This run is the steward's "try something new" response to #33's HOLD; it inherits #33's **convergence guard** and its "surviving fragment adds nothing to the existing frame" pattern (here: the survivor re-derives the deliberative-democracy canon).
- **[Cross-Lineage Review Harness](../process/cross-lineage-review-harness-protocol.md) / [decorrelation skill](../../.cursor/skills/cross-lineage-decorrelation-check/SKILL.md)** — this is an *iterated* harness run; per their rules it is **not** registered in [`_EXCHANGE_INDEX.md`](_EXCHANGE_INDEX.md) and is **non-evidence** for the review method it instantiates.
- **The transmission problem** (Lafont gap) is the one finding worth carrying — it is the real constraint on any "civic uplift via deliberative instruments" ambition the project might later entertain. The [Transmission Probe](#transmission-probe-rounds-1314--running-the-strongest-case-against-june-26-2026) refined it: the wall is **"lab, not polity"** (a falsifiable transmission claim is buyable only by testing *captive* exposure), and the **surrogate-trust source effect** has real vignette-level support (Ingham & Levin; MacKenzie & Warren) and is a buildable — but untested-at-mass-scale — field-experiment bet.
- **Two reusable review instruments** this run surfaced — the **survival-quality classifier (`S` / `V` / `S-trivial`)** and the **iterated revise-loop discipline (rotation + pre-set termination + the trajectory gate)** — are now written into the [Cross-Lineage Review Harness Protocol §5.1 and §6.1](../process/cross-lineage-review-harness-protocol.md). Those are the run's most transferable output (method, not claim).
