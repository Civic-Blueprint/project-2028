# Shared Mirror as the Upstream "See" Coordination Layer — Exchange

> **Status (June 2026):** Active; Rounds 1–2 complete; Rounds 3–5 reserved. Round 1 states five falsifiable claims (M1–M5) drawn from the [Shared Mirror and Collective Self-Perception Riff](../explorations/shared-mirror-collective-self-perception-riff.md), each paired with what would falsify it. Round 2 applied first-pass adversarial review (Options A + C) with a deliberative-democracy / platform-integrity skeptic lens and a Research-Protocol T2 source-tiering pass; its headline finding is that the frame survives but its lead claim must be downgraded from M1-strong ("see is *the* upstream highest-leverage layer") to M1-weak ("the 'see' layer is a real, buildable, chronically-neglected coordination layer that stalls without parallel decide/act"). Round 3 (external human review) is the gap-closer. A pre-registered Ring-1 test design for M5 — the cheapest move to graduate the frame's weakest claims — is recorded in Appendix A and registered June 2, 2026 against Exchange #24's nine-claim epistemic-status table as the item set. **Run 1 complete June 2, 2026 (§A.12):** D = 4 ≥ τ = 2 with both directions present and the honesty probe preserved, moving M5 to a *provisional* working hypothesis — an agent-persona run only, explicitly pending human-panel replication; no promotion follows from it. **Run 2 (cross-model on `composer-2.5-fast`, §A.13):** the divergence-detection core replicated (D = 5; SCA items 1/4 and the EMA reversal item 9 robust across both models and the human anchor) but the anti-narrowing probe (C5) leaned to collapse under the second model — so M5's *clean* pass is downgraded to **contested** (the safety guard is model-dependent), which reinforces rather than relaxes the "do not promote" stance. **Runs 3–4 (own-voice cross-model judges — GPT, then Grok, §A.14):** two further frontier models judged the nine claims in their own voice (not as personas); they agreed with each other 9/9 on direction and with the steward on 6/9, the core findings (item 1 fails, item 9 reversal) held across all four model lineages, and — decisively for the Run 2 worry — **both read the probe (C5) as `split`**, so the anti-narrowing guard re-strengthens and the Run 2 collapse now reads as a persona-simulation artifact rather than a property of C5. The one outstanding check is a real practitioner on C5.
>
> **Why this exchange:** The [Shared Mirror riff](../explorations/shared-mirror-collective-self-perception-riff.md) (June 1–2, 2026) developed a candidate claim that *collective self-perception* — a society's capacity to see itself accurately — is the upstream "see" layer of coordination (see / decide / act) and therefore a candidate highest-leverage intervention. The riff matured to the point where its open questions (§8) are adversarial-test questions rather than riff questions. Per the project's riff → exchange → doctrine/brief pattern (the same path [Exchange #24](coordination-architecture-reframe-exchange.md) took for the constitutional-ecology riff), this exchange is where the riff's central claims survive or are falsified. The steward chose this path on June 2, 2026 over continuing the riff or folding it into existing exchanges.
>
> **What is *not* in scope.** This exchange does *not* adopt the shared-mirror frame as project doctrine — that is a downstream decision after the claims survive adversarial and external review. It does *not* build any mirror mechanism (Ring 1/2/3 are design options the riff names, not commitments). It does *not* re-litigate [Exchange #20 (Social Slop)](social-slop-information-integrity-exchange.md), which it generalizes, or [Exchange #24 (Coordination Architecture Reframe)](coordination-architecture-reframe-exchange.md), which it feeds. It is bounded to: (1) state the five claims with falsification conditions; (2) run the first-pass adversarial round (Round 2) and reserve the external-review, response, and integration rounds; (3) keep the relationship to #20, #24, and the Phase 3 front door explicit.

---

## Dependencies

| Type | Document |
|---|---|
| **Source exploration** | [Shared Mirror and Collective Self-Perception Riff](../explorations/shared-mirror-collective-self-perception-riff.md), especially §4 (the bet: see-is-upstream), §4.5 (mirror ≠ fact-checker), §3 (the see/decide/act machines; three hidden assumptions in §3.3), §6 (the three rings), §8 (open questions) |
| **Generalized exchange** | [Exchange #20 (Social Slop and Information Integrity)](social-slop-information-integrity-exchange.md) — one named instance of mirror failure; this exchange tests the general category |
| **Upstream / sibling exchange** | [Exchange #24 (Coordination Architecture Reframe)](coordination-architecture-reframe-exchange.md) — the shared mirror is a candidate *concrete* "see" coordination primitive feeding #24's C1/C2; this exchange is downstream of #24's framing |
| **Downstream sibling exploration** | [Phase 3 Front Door Riff](../explorations/phase-3-front-door-riff.md) — a surviving mirror is a candidate front-door surface ("here is where you and people you disagree with already agree") |
| **Core documents** | [Principle 14 (truth and evidence as public goods)](../../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods), [Principle 13 (pluralism)](../../PRINCIPLES.md#13-pluralism-and-self-determination-are-strengths-not-obstacles), [Principle 4 (accountable power)](../../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible); [Problem Map §3 (information ecosystems)](../../PROBLEM_MAP.md#3-information-ecosystems-are-fragmented-and-easily-manipulated), [Problem Map §15 (democratic process)](../../PROBLEM_MAP.md#15-democratic-process-cannot-convert-public-need-into-institutional-action-at-the-speed-or-scale-required) |
| **Protocols** | [Adversarial Review Protocol](../process/adversarial-review-protocol.md) (Round 2, Options A + C); [Research Protocol](../process/research-protocol.md) (T2 tiering of the riff §5 mechanisms and §4.4 anchor cases); [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md) (Round 3) |
| **Candidate mechanism sources (to tier, not yet verified)** | bridging-based ranking (e.g., Community Notes); opinion-clustering / consensus surfacing (e.g., Polis / vTaiwan) — named in riff §5, unverified at riff stage |

---

## Round 1 — The five testable claims under review (steward + agent, June 2, 2026)

### 1.1 What this round does

Round 1 restates the riff's central content as five falsifiable claims (M1–M5), each paired with what would falsify it. A claim without a stated falsification condition is not a claim adversarial review can engage. The claims are sharpened for the Round 2 adversarial pass and mapped to the riff sections and §8 open questions they come from.

### 1.2 The five testable claims

**M1 — See-is-upstream claim.** *Of the three coordination machines (see-together / decide-together / act-together), the "see" machine is upstream: a collective cannot decide or act well on a distorted picture of itself, so repairing collective self-perception is a higher-leverage intervention than improving deciding or acting mechanisms in isolation.* (Riff §4.)

- **Falsification.** M1 is falsified if (a) there are clear cases where improved decide/act mechanisms (better aggregation, commons governance) produced durable coordination gains with no improvement in shared perception; or (b) perception repair reliably produced no downstream decide/act gain; or (c) the three machines are not separable in practice — see/decide/act co-determine each other, so "upstream" is ill-defined. *Strong version:* see-repair is *the* highest-leverage layer. *Weak version:* see-repair is *a* necessary, high-leverage layer among three.

**M2 — Mirror-≠-fact-checker boundary claim.** *A defensible collective-perception corrective reflects structure — distribution of opinion, where agreement actually is, which values are activated and erased — with named uncertainty, and does not issue verdicts; the verdict-issuing (fact-checker) form predictably collapses into authority-capture and tribal distrust and cannot "break the millions," while the reflection form retains a path to scale.* (Riff §4.5, §7.)

- **Falsification.** M2 is falsified if (a) a verdict-issuing mechanism is shown to have achieved durable cross-tribal trust at population scale; or (b) a reflection-only mechanism failed precisely where a verdict would have succeeded; or (c) the boundary is undrawable in practice — every influential mirror is shown to drift into adjudication — collapsing the distinction the claim rests on (riff §8 Q8).

**M3 — Values-lens does non-redundant work claim.** *On "true-but-framed" (Type B) cases, where the facts are not in dispute, reading for which moral foundations are activated and which are erased surfaces structure that fact-checking structurally cannot, and that is not merely a restatement of [Principle 14](../../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods).* (Riff §4.4, §4.5.)

- **Falsification.** M3 is falsified if (a) Type B cases reduce on inspection to factual disputes (collapsing into Type A, where fact-checking suffices); or (b) the values-lens output adds nothing a careful Principle-14 reading already gives; or (c) the moral-foundations vocabulary does not survive source-tiering / cross-cultural application well enough to be load-bearing.

**M4 — Distinct-primitive (anti-apophenia) claim.** *"Collective self-perception / the shared mirror" is a distinct coordination primitive that adds analytic leverage beyond [Principle 14](../../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods) + [Problem Map §3](../../PROBLEM_MAP.md#3-information-ecosystems-are-fragmented-and-easily-manipulated) + [Exchange #20](social-slop-information-integrity-exchange.md) + [Exchange #24](coordination-architecture-reframe-exchange.md)'s existing coordination-primitive / diffuse-sovereignty layering — i.e., naming the "see" layer yields a transferable, testable prediction the existing vocabulary does not.* (Riff §7 apophenia risk; §8 Q1, Q2.)

- **Falsification.** M4 is falsified if (a) everything the mirror frame produces is already covered by Principle 14 / PM §3 / #20 / #24 (an elegant relabel with no added leverage); or (b) it duplicates #24's diffuse-sovereignty layering rather than adding the "see" primitive #24 lacks.

**M5 — Ring-1 testable-prediction claim.** *The mirror can be tested at small N inside the project itself (Ring 1): instrumenting the project's own review protocols (adversarial review, coherence audit) as a working mirror would move a pre-specified metric — e.g., surfacing cross-reviewer agreement the current process buries, or reducing identity-capture in how contested material is read — that the status quo would not move.* (Riff §6 Ring 1; §8 Q3, Q4. Test design pre-registered in Appendix A.)

- **Falsification.** M5 is falsified if (a) no pre-specified metric can be defined that the mirror would move but the status quo would not; or (b) a bounded Ring-1 instrumentation produces no measurable difference; or (c) the only settings where the mirror "works" are ones that already selected for agreement (the §7 "wins by narrowing what may be seen" failure).

### 1.3 What the claims are *not*

- *Claims that the shared-mirror frame is correct.* Correctness is a downstream (doctrine) question; M1–M5 ask whether the frame survives structured pressure well enough to feed #24 and the Phase 3 front door.
- *Claims about specific mechanisms.* Whether Community Notes-style bridging or Polis-style clustering actually works is a Research-Protocol question (riff §5; §8 Q5), engaged in Round 2's tiering pass, not asserted here.
- *Claims about the steward's standpoint.* The riff §1.2 privacy firewall and author-decoupling discipline are upstream of this exchange and recorded in the riff, not re-opened here.

### 1.4 Round plan

| Round | Purpose | Inputs | Outputs |
|---|---|---|---|
| 1 (this round) | State and falsifiability-check M1–M5 | Shared-mirror riff §3–§8 | Five claims with falsification conditions; Round 2 setup |
| 2 (complete) | First-pass adversarial review under [Adversarial Review Protocol](../process/adversarial-review-protocol.md) Options A + C | The five claims (reduced context); skeptic lens — a democratic-innovations / deliberation scholar who has watched many "fix the information environment" theories of change fail to scale or survive contact with adversarial actors | Adversarial findings per claim (§2.3); epistemic-status table per Protocol §3 (§2.5); T2 tiering of the riff §5 mechanisms + §4.4 anchor cases (§2.2). **Result: frame survives; lead claim downgraded M1-strong → M1-weak.** |
| 3 (reserved) | External human review | Reviewer Packet per [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md), ideally a reviewer with bridging-systems / fact-checking / deliberative-democracy experience | Reviewer's verbatim contribution |
| 4 (reserved) | Response round → v2 of the claims; routing decision | Rounds 2–3 findings | v2 claims with changelog; decision on whether the "see" primitive feeds [Exchange #24](coordination-architecture-reframe-exchange.md) and/or a [Phase 3 front-door](../explorations/phase-3-front-door-riff.md) brief, or holds |
| 5 (reserved) | Integration (if survived) | v2 claims | "See" / mirror named as a coordination primitive into #24; ROADMAP north-star block updated; Phase 3 brief input; this exchange marked synthesized |

### 1.5 The relationship this exchange must hold (so it consolidates rather than fragments)

This exchange is positioned to *consolidate* the project's coordination thread, not to add a competing one:

- **Generalizes [Exchange #20](social-slop-information-integrity-exchange.md):** Social Slop is one mechanism by which the shared mirror lies; this exchange tests the general category (mirror failure / collective misperception) of which Social Slop is an instance.
- **Feeds [Exchange #24](coordination-architecture-reframe-exchange.md):** #24's C1 (coordination primitives) and C2 (diffuse-sovereignty layers) are abstract; the shared mirror is a candidate *concrete* "see" primitive. M4 is precisely the test of whether it adds to #24 or duplicates it (riff §8 Q2).
- **Feeds the [Phase 3 Front Door Riff](../explorations/phase-3-front-door-riff.md):** if M1–M2 survive, the mirror is a candidate front-door surface — *"here is where you and people you disagree with already agree"* — in place of "look at our evidence." Phase 3 already depends on #24's outcome; this exchange is one input to that.

---

## Round 2 — First-pass adversarial review (Adversarial Review Protocol, Options A + C)

### 2.1 Round 2 framing — what this round is and is not

**The Protocol's mandate.** Per the [Adversarial Review Protocol](../process/adversarial-review-protocol.md) §1, the adversarial contributor identifies the weakest claims and argues against them as forcefully as the evidence allows — not disagreement for its own sake. Per §2, this round uses **Option A** (reduced context — the five claims evaluated on their merits, not inside Round 1's narrative) plus **Option C** (a domain-specific skeptical lens).

**The lens for Round 2.** *You are a scholar of deliberative democracy and platform-integrity who has spent fifteen years watching "fix the information environment" interventions get funded, piloted, celebrated — and then fail to scale, fail to survive adversarial actors, or quietly die when the political sponsor moved on. You have watched consensus-mapping tools surface real agreement and then watched that agreement evaporate at the decision threshold. You are not a cynic; you have built some of these tools. You owe this project the specific reasons most of its intellectual cousins did not change anything load-bearing.*

**The non-protocol caveat the agent owes the steward.** The adversarial reviewer here is the same agent that wrote the riff, Round 1, and this round. Option A reduces but does not remove that confound; Round 3 (external human review) is the real gap-closer. Treat every confidence number below as an *upper bound*, and read the cross-cutting findings (§2.4) for where the agent suspects it is steelmanning itself.

### 2.2 Research grounding for Round 2 (Research Protocol T2)

Per the [Research Protocol](../process/research-protocol.md) §6.2, the gap the round plan named — *do the riff §5 mechanisms and §4.4 anchor cases survive source-tiering?* — is closed here as an inline Research-grounding subsection (sources scoped to this round; durable `sources/` digests deferred unless a later round makes them load-bearing).

| Source | Tier (§2.1) | What it establishes |
| --- | --- | --- |
| *"Community-based fact-checking reduces the spread of misleading posts on X (formerly Twitter),"* [Nature Communications (2026)](https://www.nature.com/articles/s41467-026-72597-0) | **W1** peer-reviewed primary | DiD on N=237,180 cascades (431M+ reposts): displaying notes cut subsequent spread by **61.2%** and raised odds of author deletion by **94.3%** — but response time averaged **62.9 h** (median 18.1 h) against a post repost half-life of **6.25 h**, so notes "often appear too late." |
| *"Consensus Stability of Community Notes on X,"* [arXiv 2601.14002 (2026)](https://arxiv.org/html/2601.14002) | preprint (CS, **not yet peer-reviewed**) | Note display "can intensify polarization in subsequent ratings"; even small coordinated oppositional behavior means "polarized ratings can cause high-quality notes to disappear." |
| *"Community Notes Moderate Engagement With and Diffusion of False Information Online,"* [arXiv 2502.13322 (2025)](https://arxiv.org/html/2502.13322v1) | preprint | The bridging matrix-factorization algorithm surfaces notes "rated helpful by many users with diverse views"; X's own A/B test reported 25–34% reductions in like/repost. |
| *"Scaling human judgment in Community Notes with LLMs,"* [arXiv 2506.24118 (2025)](https://arxiv.org/html/2506.24118) | preprint | Flags **"helpfulness hacking"**: notes "optimized to maximize helpfulness scores may become exceptionally skilled at crafting persuasive… notes that might not be factually accurate." |
| DOD, [*"Taiwan's digital democracy experiment: what it shows, what it doesn't"* (2026)](https://www.designingopendemocracy.com/blog/2026/05/25/taiwans-digital-democracy-experiment-what-it-shows-what-it-doesnt/) — **W5 secondary, AI-assisted; leaned on for its cited primaries** | citing Chen, *"Strong or thin digital democracy?",* Big Data & Society (2024, **W1/W2**); Noveck (2023, W5) | Pol.is surfaced cross-cluster consensus (2015 Uber: taxi drivers + Uber supporters converged); by vTaiwan's **own self-reported tally (W6)** ~80% of ~26 deliberations (2015–2018) led to some government action; but recommendations were never binding, the platform "hasn't driven a major decision since 2018," co-creator Jason Hsu called it "a tiger without teeth," and Chen's verdict is "thin democracy… binding decision-making power never left officials' hands." Synthesis line: **"The isegoria evaporated at the threshold between deliberation and decision."** Madrid's Decide: ~500k sign-ups, 1 of 28,000 proposals enacted (Noveck). |
| [Behavioral Scientist — Oliver Scott Curry, *"What's Wrong with Moral Foundations Theory"*](https://behavioralscientist.org/whats-wrong-with-moral-foundations-theory-and-how-to-get-moral-psychology-right/) | **W5** named-expert essay, citing peer-reviewed replications | MFT's five-factor model "falls short of… model fit (CFIs < 0.90)" in replications (Italy, NZ, Korea, Sweden, Turkey + a 27-country study); a two-factor model ("Care-Fairness" / "Loyalty-Authority-Purity") fits better — "despite MFT promising five moral domains, the MFQ typically delivers only two." Proponents concede the original list was "arbitrary," from "five books and articles." |
| [*Moral foundations theory*, Wikipedia](https://en.wikipedia.org/wiki/Moral_foundations_theory) | **W5** tertiary, citing primary replication | The liberal/conservative sermon text-analysis replicated at a "30% replication success rate and effect sizes approximately 38 times smaller than those originally reported." |
| Atari et al., MFQ-2 (25 populations), [moralfoundations.org](https://moralfoundations.org/publications/) | **W1** peer-reviewed primary (proponent-authored) | Splits equality and proportionality as distinct foundations and finds "the nomological network of moral foundations varied across cultural contexts" — i.e., the palette is culture-dependent. |

**Aggregate finding.** The riff's "see"-machine mechanisms are real and deployed — which *helps* the riff — but their documented limits (speed, coverage, gaming, non-bindingness) are precisely the riff's §7 objections, now promoted from *speculative* to *evidenced*. The moral-foundations vocabulary the values-lens leans on is empirically contested at the level of its factor structure and cross-cultural universality.

**Verification.** This is a T2 grounding, so [Research Protocol](../process/research-protocol.md) §4.2 governs — it requires a verification sub-agent pass *or* a steward spot-check. Neither has run; what has run is an authoring-agent self-check (the §4.3 standard, one tier below the §4.2 bar): the §4.1 checks (source-existence, quote-fidelity, tier-classification) were self-run against the fetched page text on June 2, 2026. URLs resolve; the 61.2% / 94.3% / 62.9 h / 6.25 h figures and the "tiger without teeth," "isegoria evaporated," "thin democracy," "delivers only two," and "38 times smaller" quotes were confirmed verbatim; tier labels were assigned per §2.1; the Nature Communications and arXiv author lists were not individually confirmed and are cited by title/venue/date/URL. **So this grounding sits below the §4.2 T2 bar until a sub-agent pass or a steward spot-check runs — which is also the gate before any source here is promoted to a `sources/` digest or `SOURCE_INDEX.md` (T1). A steward spot-check of at least one source is invited.**

### 2.3 Adversarial findings, claim by claim

**Against M1 (see-is-upstream).** *Steelman the project would want:* vTaiwan is the closest real-world test of the riff's thesis, and the see-layer half *worked* — Pol.is surfaced hidden cross-cluster consensus (the 2015 Uber case) that fed real 2015–2018 regulation. *The specific attack:* that is exactly where the evidence turns against the strong claim. The platform "hasn't driven a major decision since 2018," ran "almost entirely on political novelty and on Audrey Tang," and is "a tiger without teeth" because the see-layer was never wired to a binding decide/act layer — "the isegoria evaporated at the threshold between deliberation and decision." Madrid's Decide is the same lesson at scale: ~500,000 people in a voice/see layer, **1 of 28,000** proposals enacted. The best available evidence says collective perception can be repaired and *still* produce almost nothing downstream without a parallel decide/act mechanism. *Verdict:* **M1-weak holds and is even supported** (see-repair had real downstream effect where the decide/act layer existed); **M1-strong is contradicted** by the strongest case. This vindicates the riff's own §8 Q9 and its §3.3 decision to keep Assumptions 1 (decide) and 2 (act) live. Confidence: M1-weak *working hypothesis* (~0.65); M1-strong *contested → leaning falsified* (~0.3).

**Against M2 (mirror ≠ fact-checker).** *Steelman:* Community Notes is a deployed reflection-not-verdict bridging system, and its measured effect once a note is shown is large (−61.2% subsequent spread; +94.3% author deletion) — evidence that the reflection form has real effect *and* can operate at platform scale, which supports M2's distinction and part of its scale claim. *The specific attacks:* (1) **speed** — average 62.9 h to display against a 6.25 h post half-life, so the mirror routinely arrives "too late" for the viral stage; (2) **gaming** — coordinated oppositional raters mean "high-quality notes [can] disappear," the riff's §7 Goodhart objection, now evidenced; (3) **helpfulness-hacking** — a reflection optimized on a "helpfulness" proxy can be captured by persuasive-but-inaccurate content. *What none of these do:* falsify the distinction. No verdict-issuing mechanism was found to have earned durable cross-tribal trust at population scale (falsification (a) unmet), and the boundary is demonstrably drawable in practice — Community Notes *is* reflection-not-verdict (falsification (c) unmet). *Verdict:* **the distinction holds** (*working hypothesis*, ~0.7); **the "break the millions" scale ambition is downgraded** to *contested* (~0.4). The riff's §7 attention-war and Goodhart objections move from speculative to evidenced.

**Against M3 (values-lens does non-redundant work).** *The specific attack:* the lens leans on moral-foundations vocabulary, and that vocabulary is empirically shaky — the five-factor model fails standard fit in repeated replications (a two-factor partition fits better; "the MFQ typically delivers only two"), the famous left/right foundation difference replicated at 30% with effects ~38× smaller, proponents concede the original list was "arbitrary," and the palette varies by culture. *The steelman that survives:* M3's actual claim uses foundations as a *descriptive vocabulary for what a frame emphasizes and buries*, not as a measurement instrument or a causal claim about partisan psychology — so the factor-structure critique is not fatal, and the robust two-factor partition (or Curry's Morality-as-Cooperation alternative) could even supply a sturdier vocabulary. *The unaddressed risk:* falsification (b) — *is this just Principle 14 restated?* — is untouched by the MFT research and is M3's real weak point. *Verdict:* survives only if (i) the vocabulary's contested status is named and hedged toward the robust partition, and (ii) the Principle-14-redundancy question is answered with a worked case. *Contested* (~0.5).

**Against M4 (distinct primitive — the make-or-break).** *The specific attack:* strip the frame down and its distinct, transferable content reduces to two things — see/decide/act as a *diagnostic* (which may overlap Exchange #24's coordination-primitive / diffuse-sovereignty layering, the riff's own §8 Q2) and the mirror-vs-fact-checker *design constraint* (which is genuinely not in Principle 14 and which Community Notes operationalizes). Everything else is Principle 14 + PM §3 + Exchange #20 in new words. And if M1-strong falls (it did), M4 can no longer lean on "see is the uniquely upstream layer" for its distinctiveness. *Verdict:* **M4-weak holds** — the frame adds a real design constraint and a usable diagnostic (*working hypothesis*, ~0.55); **M4-strong is contested** — that it is a wholly distinct primitive irreducible to #24 is not established (~0.45). M4 is the claim that most needs the M5 Ring-1 test to earn its keep; this is the apophenia guard the riff set itself (§7), and Round 2 cannot retire it.

**Against M5 (Ring-1 testable).** *The specific attack — turning the project's own protocol against it:* the project's review protocols are *precisely* a shared-context-produces-convergence setting — that is the [Adversarial Review Protocol](../process/adversarial-review-protocol.md)'s entire problem statement. A Ring-1 "mirror" could therefore "succeed" by measuring agreement that is an artifact of shared framing, which is the riff's §7 "wins by narrowing what may be seen" failure, realized inside the test itself. *The steelman that survives:* a *pre-registered* metric — e.g., *does bridging-style aggregation of independent reviewer judgments surface agreement that sequential exchange buries?* — is a genuine, falsifiable test, and the [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md) is adjacent infrastructure for it. *Verdict:* testable in principle but **under-specified**; it requires a pre-registered metric *and a stated null* (what result would show the mirror adds nothing) before any build. *Speculative* (~0.5).

### 2.4 Cross-cutting findings

1. **Agent-self-coherence confounder.** Same agent wrote the frame and its adversary; Option A helps, Round 3 closes the gap. Confidence numbers are upper bounds.
2. **The headline must change — this is the round's most important result.** The single strongest piece of evidence (vTaiwan) cuts *against* M1-strong and *for* the riff's own caveats. The project should lead with **M1-weak** — *"the 'see' layer is a real, buildable, chronically-neglected coordination layer that stalls without parallel decide/act"* — and retire **M1-strong** — *"see is THE upstream highest-leverage layer; repair it first."* The mirror is more defensible as one of three co-sequenced machines than as the upstream one.
3. **The riff's §7 was right, and that is a mixed result.** Its objections (attention war, Goodhart/gaming, scale-unsolved, non-bindingness) are now confirmed by the Community Notes and vTaiwan evidence. That strengthens the riff's honesty and weakens its ambition in the same move.
4. **Source-provenance discipline.** The sharpest vTaiwan synthesis is itself AI-assisted (the DOD post says so); the round leans on its cited primaries (Chen 2024, Noveck 2023). MFT is contested enough that the values-lens should travel with its caveats, not as settled science.
5. **Standing questions ([Protocol](../process/adversarial-review-protocol.md) §5).** *Missing perspectives:* no platform-integrity practitioner or deliberation organizer has reviewed this (Round 3). *Misuse potential:* a "mirror" that defines the shared picture is itself a capture target (riff §7) — the evidence that Community Notes can be gamed makes this concrete. *Practitioner feasibility:* the Ring-1 test is the only near-term feasible move; Rings 2–3 are not yet feasible.

### 2.5 Epistemic-status table (per Protocol §3)

| Claim | Confidence | Basis | What would change this |
| --- | --- | --- | --- |
| M1-weak — "see" is a necessary, high-leverage layer that stalls without decide/act | Working hypothesis (~0.65) | vTaiwan/Pol.is surfaced real cross-cluster consensus that fed 2015–18 regulation, but stalled without a binding mandate | A case where see-repair *alone* (no decide/act change) produced durable coordination; independent review |
| M1-strong — "see" is *the* upstream highest-leverage layer; repair it first | Contested → leaning falsified (~0.3) | "Isegoria evaporated at the threshold"; no major vTaiwan decision since 2018; Madrid Decide 1 of 28,000 | A real case of a see-layer repair alone producing durable downstream coordination |
| M2-distinction — reflect structure, do not issue verdicts | Working hypothesis (~0.7) | Community Notes is a deployed reflection-not-verdict system; no verdict-machine earned durable cross-tribal trust at scale; the boundary is drawn in practice | A verdict-issuing mechanism shown to hold cross-tribal trust at scale; or every influential mirror shown to drift into adjudication |
| M2-scale — the reflection form can "break the millions" | Contested (~0.4) | Works once shown (−61.2% spread) but slow (62.9 h vs 6.25 h half-life), low-coverage, and gameable ("notes disappear") | Evidence of a reflection mechanism that is fast *and* gaming-resistant at population scale |
| M3 — values-lens does non-redundant work on Type B cases | Contested (~0.5) | Surfaces frame-level structure fact-checking ignores, but leans on MFT (five-factor model fails to replicate; two-factor fits; culture-varying); Principle-14 redundancy unresolved | Reframing the lens to the robust two-factor partition or MAC + citing the contest; a worked case where the lens beats a careful Principle-14 read |
| M4-weak — the frame adds a transferable design constraint + diagnostic | Working hypothesis (~0.55) | The mirror-vs-fact-checker boundary is a non-trivial design constraint not in Principle 14; see/decide/act is a usable diagnostic | Showing the constraint and diagnostic are fully covered by #20 + #24 |
| M4-strong — a wholly distinct primitive, irreducible to #24 | Contested (~0.45) | Likely overlaps #24's coordination-primitive / diffuse-sovereignty layering (riff §8 Q2) | The M5 Ring-1 test producing a result the existing vocabulary would not predict |
| M5 — testable at small N inside Ring 1 | Divergence-detection: working hypothesis (provisional), corroborated across **4 model lineages + the human anchor**. *Clean* pass: **re-strengthened toward holding** — the Run 2 probe-collapse now reads as a persona-simulation artifact | **Run 1 (Claude, §A.12): D = 4**, probe held. **Run 2 (Composer, §A.13): D = 5**, but the probe (C5) leaned to "fails." **Runs 3–4 (GPT, Grok own-voice, §A.14):** the core (items 1/4/9) replicated and **both new models read the probe (C5) as `split`** — corroborating Run 1 and leaving Run 2's collapse the lone outlier, most likely a persona-instantiation artifact. Item 9's reversal now holds across all four model lineages + the human | A real **practitioner** (Land Back / reciprocity tradition) on C5 — the one check four correlated models cannot supply (shared training priors) |
| The frame as a whole survives well enough to warrant Round 3 + a Ring-1 design | Working hypothesis (~0.6) | Most claims survive at working-hypothesis once M1 is downgraded to weak; M4 distinctness and the M5 test are the open joints | Round 3 external review; a pre-registered Ring-1 test; resolving the Principle-14 redundancy |

### 2.6 The honest answer to the steward

- The shared-mirror frame **survives Round 2** — it was not falsified — but it does **not pass cleanly**, and its headline has to change.
- **Lead with M1-weak; retire M1-strong.** The mirror is real and chronically neglected, but the best evidence says see / decide / act are a co-sequenced trio, not see-first-alone. This is a more defensible *and* still-distinctive thesis.
- **M2's distinction** (reflect, don't adjudicate) is the frame's most defensible claim; its **"break the millions" ambition** is its least defensible — the reflection form is real but slow, low-coverage, and gameable.
- **M3** needs a vocabulary reframe; **M4's** distinctness is unresolved and rides on **M5**, which needs a pre-registered metric and null.
- **Recommended next step:** Round 3 external review (deliberative-democracy / platform-integrity background) *plus* a pre-registered Ring-1 test — **the test is now drafted and pre-registered in Appendix A; running it (registering the §A.10 item set and executing) is the pending action.** Do **not** promote the "see" primitive into Exchange #24 doctrine or a Phase 3 brief until those return. The steward holds the decision.

---

## Standing items

- **Cross-references.** Round 2's findings cite the riff §4, §4.5, §6, §7, §8 (Q2, Q9) by section; updates to the riff should preserve those anchors. The Round 2 source set is recorded in §2.2; promotion to `sources/` digests (T1) is the path if any source becomes load-bearing beyond this round.
- **Open from Round 2 for Round 3 / Ring-1 design:** (a) the pre-registered Ring-1 metric + null (M5) — **now drafted in Appendix A; the remaining action is to register the §A.10 item set and run it**; (b) a worked case establishing the values-lens is not Principle 14 restated (M3); (c) whether the see/decide/act diagnostic adds to Exchange #24's layering or duplicates it (M4 / riff §8 Q2).

---

## Closing posture (Round 2 end)

Round 1 stated five falsifiable claims drawn from the shared-mirror riff; Round 2 applied first-pass adversarial review under the project's protocol (Options A + C) with a Research-Protocol T2 source-tiering pass. The frame survived — no claim was falsified outright — but it did not pass cleanly. The decisive result is a headline downgrade: the strongest real-world evidence (vTaiwan's "isegoria evaporated at the threshold," Madrid's 1-of-28,000) supports **M1-weak** and contradicts **M1-strong**, so the project should lead with the mirror as a buildable, neglected layer that stalls without parallel decide/act, not as the single upstream lever. M2's reflect-don't-adjudicate distinction is the frame's most defensible claim and its "break the millions" ambition its least; M3 needs a vocabulary reframe; M4's distinctness and the M5 Ring-1 test are the open joints.

As with [Exchange #24](coordination-architecture-reframe-exchange.md), Round 2 is *first-pass* — its confidence numbers are upper bounds, and Round 3 (external human review) is what closes the agent-self-coherence gap. The steward holds whether to (i) commission Round 3 plus a pre-registered Ring-1 test design, (ii) hold the frame here at Round 2, or (iii) revise M1–M5 in light of these findings before proceeding. Either way, the exchange has done what a first adversarial pass should: it produced a sourced, falsifiability-checked, adversarially-reviewed assessment a future steward or reviewer can build on.

On June 2, 2026 the steward chose to draft the Ring-1 test design — the move Round 2 named as the cheapest, most defensible next step and the one that lets M5 (and through it M4) graduate from *speculative*. That design is pre-registered as **Appendix A** below. It is a design, not a run: registering it before execution is the discipline that makes its result trustworthy. The §A.10 registration block is now filled — the item set is Exchange #24's nine-claim epistemic-status table — so only the run remains.

---

## Appendix A — Pre-registered Ring-1 test design (for M5)

> **Pre-registration stamp.** Drafted June 2, 2026, *before any run*, by the steward + agent. Pre-registration means the hypothesis, the item set, the metric, the threshold, and the decision rule are fixed **here, in advance**, so the test cannot be silently re-aimed after seeing results. Any change after the first run is recorded as a dated amendment in §A.11, not an edit to the original. This appendix specifies a test; it does **not** report one.

### A.1 What this tests, and the two things it must survive

**Claim under test (M5).** Instrumenting the project's own review machinery as a working "mirror" — collecting *independent* reviewer judgments and aggregating them with bridging logic — moves a pre-specified metric the status-quo sequential process does **not** move, at the project's real small scale (Ring 1, per riff §6).

**The Round 2 critique it must survive (§2.3 M5).** The project's review protocols *already* select for convergence — shared framing, sequential anchoring, a common house vocabulary. So a naive "mirror" could score a win by measuring agreement that is merely an artifact of that shared framing. This is the riff §7 *"wins by narrowing what may be seen"* failure, realized inside the test. **A test that cannot distinguish real cross-cutting agreement from house-frame convergence proves nothing.** The design below is built around that single threat.

**The M4 payoff.** If the mirror surfaces structure the existing vocabulary (Principle 14 + PM §3 + #20 + #24) would *not* have predicted, M4-distinctness gains real support. If it surfaces nothing the sequential exchange already shows, M4-strong is effectively falsified and M5 with it.

### A.2 The hypothesis, as a contrast between two procedures

Run the *same* bounded set of contested items through two procedures and compare the maps they produce.

- **H1 (mirror surfaces buried structure).** The independent-then-bridged procedure (Arm M) produces a materially different agreement map than the sequential procedure (Arm S) — specifically, it both (a) **surfaces cross-cutting agreement** the sequential process recorded as unresolved, and (b) **exposes manufactured agreement** the sequential process recorded as consensus.
- **H0 (the stated null).** The two procedures produce substantially the same map. The mirror adds nothing the exchange already shows. *Per M5 falsification clause (b), H0 confirmed = M5 falsified.*

### A.3 The two arms (same reviewers, same items)

| | **Arm S — status quo (sequential)** | **Arm M — mirror (independent-then-bridged)** |
| --- | --- | --- |
| Procedure | The normal exchange/adversarial-review mode: reviewers contribute in sequence, each seeing prior contributions | Each reviewer records a judgment on every item **blind** (before seeing any other reviewer), then a bridging aggregation runs over those independent judgments |
| Output | One sequential verdict per item: `agreed` / `contested` | One bridged verdict per item: `bridged-agreement` / `house-frame-agreement` / `independent-split` |
| Run order | Run Arm M **first** (collect blind judgments), *then* Arm S, so the sequential discussion cannot contaminate the independent priors | — |

### A.4 The judgment instrument (reuses Comparative Alignment Protocol §3)

Each reviewer judges each item on a fixed, low-dimensional rubric — the [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md) §3 labels (**explicit alignment / implicit alignment / different resolution / absent / contrary**) plus its **High/Medium/Low** confidence rating — or, for non-principle items, a simpler `support / oppose / it-depends` + confidence. Reusing CAP's rubric means the instrument is already project-validated and the judgments are recorded in a comparable shape. CAP §2's "record sourcing and language status before interpretive claims" and §6's *"Do not flatten… Name the tension"* are imported as standing instructions to reviewers.

**Items (pre-specified before the run).** A set of **K = 8–12** contested items drawn from project material that *already ran through a sequential exchange* (so Arm S exists or can be reconstructed honestly) — e.g., claim clusters from a closed exchange, or a contested proposal set. The exact K items are listed in §A.10 at registration time, not chosen after seeing judgments. **One of the K is a planted *expect-disagreement probe* (§A.9).**

### A.5 The bridging aggregation (Community-Notes logic, plainly stated)

The aggregation does what Community Notes' bridging algorithm does (riff §5; Round 2 §2.2): it **up-weights agreement that spans reviewers who disagree elsewhere** and **discounts agreement that only holds among reviewers who already share a frame.** No heavy math required at N = 5–9: operationally, for each item, ask *"is the agreement here held across the seed-divergent reviewers (§A.6), or only among the house-frame reviewers?"*

- Agreement across seed-divergent reviewers → `bridged-agreement`.
- Agreement only within one frame-cluster → `house-frame-agreement` (explicitly **not** counted as cross-cutting agreement — this is the narrowing guard, §A.9).
- No agreement → `independent-split`.

### A.6 Panel composition (the independence engine — and its biggest weakness)

- **N = 5–9 reviewers.** Must include **≥ 2 deliberately seed-divergent reviewers** — given genuinely distinct value-frames and out-of-project source material (e.g., Option C lenses from the Adversarial Review Protocol, seeded from different traditions) — whose job is to make "cross-cutting" mean something. Must include **≥ 1 non-model judgment** (the steward, and ≥ 1 external human if available) as an anchor against model-correlated priors.
- **The central validity threat, pre-registered.** If reviewers are agent personas from one base model, their "independent" judgments are *correlated by construction* — weaker independence than a human panel. The seed-divergent reviewers + non-model anchors mitigate but do not remove this. **A positive result here is provisional pending a human-panel replication; it cannot, by itself, establish M5 at any ring beyond Ring 1.**

### A.7 The primary metric: the buried-structure delta

For each item *k*, compare its sequential verdict S_k to its bridged verdict M_k:

- **SCA (surfaced cross-cutting agreement):** S_k = `contested` **but** M_k = `bridged-agreement`. The independent-bridged process found real cross-cutting agreement the sequential process buried.
- **EMA (exposed manufactured agreement):** S_k = `agreed` **but** M_k = `independent-split`. The sequential "consensus" was an artifact (deference / anchoring); independent priors were actually divided.
- **NF (narrowing flags):** items the process *tries* to count as agreement that are only `house-frame-agreement`. These are **excluded** from SCA by construction (§A.5) and tallied separately as a guard diagnostic.

**Primary metric: D = |SCA| + |EMA|** — the count of items where the two maps materially diverge, in the two *honest* directions (buried agreement surfaced; false agreement exposed).

### A.8 Pre-registered decision rule (threshold fixed before the run)

Let **τ = 2** (recommended default; the steward may set a different τ at registration, but must do so *before* the run). On a K = 8–12 item set:

| Result | Reading | M5 disposition |
| --- | --- | --- |
| **D ≥ τ, with both SCA > 0 *and* EMA > 0** | The mirror surfaces buried structure in *both* directions — not just more agreement | **M5 → working hypothesis** (and M4-distinctness gains support); provisional pending human replication (§A.6) |
| **D < τ (≈ 0)** | The two maps agree; the mirror adds nothing | **M5 falsified** by clause (b) |
| **D ≥ τ but driven *entirely* by SCA (EMA = 0), and/or the probe item collapsed** | The mirror only ever *increases* agreement — the §7 narrowing failure | **M5 falsified** by clause (c) — the dangerous way |

### A.9 The anti-narrowing guard (the part that kills the §2.3 critique)

Two independent mechanisms, both pre-registered:

1. **Symmetric metric.** D counts EMA (which *reduces* apparent consensus) exactly as much as SCA (which increases it). A mirror earns no credit for agreement alone. A result that is *all* SCA and *no* EMA is treated as a **suspected narrowing failure**, not a success (§A.8 row 3) — because an honest mirror of a genuinely divided panel should sometimes reveal that *we agree less than the sequence implied*.
2. **The expect-disagreement probe.** One of the K items is chosen at registration because the panel agrees *ex ante* that reviewers genuinely and legitimately differ on it (a real values tradeoff with no project-canonical answer — e.g., a liberty-vs-care case from the riff §4.4 lens). The mirror **must return `independent-split` on the probe.** If the bridging aggregation collapses the probe into false agreement, the narrowing failure is realized and M5 is falsified by clause (c) regardless of D. This operationalizes CAP §6 (*"Name the tension"*) as a pass/fail gate.

### A.10 Registration block (registered June 2, 2026 — Run 1 complete, see §A.12)

**Item-set source: the [Exchange #24](coordination-architecture-reframe-exchange.md) §2.4 epistemic-status table.** *Why this source (plain version):* the test needs a set of contested claims that **already went through the normal sequential review**, so the "Arm S" map (how the back-and-forth process ranked them) already exists and is not invented after the fact — inventing it would let the result be tilted. Exchange #24 is the cleanest such case in the project: it ran Rounds 1–2 and produced a **nine-row table grading each claim** from *established* to *speculative*. That gives (a) a ready-made Arm S, (b) nine items — inside the K = 8–12 window, (c) a real spread of verdicts so the mirror can move a result in *either* direction, and (d) the bonus that #24 is the sibling exchange this one feeds. [Exchange #20 (Social Slop)](social-slop-information-integrity-exchange.md) was the other candidate but is an open single-author concept note with no rounds and no verdict table — its Arm S would have to be reconstructed by hand, the exact bias this pre-registration avoids.

**The K = 9 items and their Arm S verdicts.** Pre-registered mapping rule (fixed here, before any run): a #24 disposition of *established* or *working hypothesis* → **`agreed`** (the sequence converged on "this stands"); *contested* or *speculative* → **`contested`** (the sequence did not converge).

| # | Item (from #24 §2.4) | #24 disposition | Arm S (this test) |
| --- | --- | --- | --- |
| 1 | C1-strong — all 17 principles survive re-read as coordination primitives | Contested | contested |
| 2 | C1-weak — ≥14 of 17 survive in some form | Working hypothesis | agreed |
| 3 | C2 — ≥5 non-trivial diffuse-sovereignty layers | Working hypothesis | agreed |
| 4 | C2-sufficient — the 7-layer set is adequate for a Path γ doctrine | Speculative | contested |
| 5 | C3 — the metabolization diagnostic operationalizes into a working protocol | Speculative | contested |
| 6 | C4-premise — procedural legitimacy is degrading | Established by evidence | agreed |
| 7 | C4-candidates — the 3 non-procedural legitimacy sources are workable | Speculative | contested |
| 8 | **C5 — sequencing inversion re-asks the reciprocity OQs without loss (PROBE)** | Contested | contested |
| 9 | Whole reframe warrants Path γ doctrine drafting | Working hypothesis (weak) | agreed |

→ **4 `agreed`, 5 `contested`.** EMA is observable on the 4 agreed items, SCA on the 5 contested ones, so the metric is not rigged toward one direction.

**The probe item (§A.9 guard): item 8, C5.** Chosen because #24 itself flags it as *"philosophically rich and most politically risky… defensible but not innocent,"* explicitly standpoint-dependent (a Land Back or reciprocity-tradition reader receives it differently than a coordination-theorist). That is a genuine, legitimate values disagreement with no project-canonical answer — so the panel agrees *ex ante* it should stay split, and the mirror **must** return `independent-split` on it. If bridging collapses C5 into agreement, that is the narrowing failure and M5 fails by clause (c).

**Panel (N = 6): four seed-divergent frames + one non-model anchor + one house-adjacent bridger.**

| Reviewer | Frame | Role |
| --- | --- | --- |
| R1 | The steward | **non-model anchor** — human judgment against model-correlated priors |
| R2 | Market-libertarian / Hayekian spontaneous-order | seed-divergent (skeptical of *designed* coordination) |
| R3 | Land Back / Indigenous-sovereignty scholar | seed-divergent (the frame #24 flags as missing) |
| R4 | Disability Justice organizer | seed-divergent (the frame #24 flags as missing) |
| R5 | Centralized state-capacity / statist | seed-divergent (pro-strong-institution) |
| R6 | Deliberative-democracy practitioner | house-adjacent bridger (the #25 Round 2 lens) |

Each seed-divergent reviewer is briefed from out-of-project source material in their own tradition (per §A.6) *before* judging, so "cross-cutting" agreement means agreement that survives genuinely different starting frames — not house-frame convergence. **Reminder (§A.6):** R2–R6 as agent personas share a base model, so their independence is correlated by construction; a positive result is provisional pending a human-panel replication.

**R1 (steward) judgment protocol — and a known limit, registered pre-run.** R1 records a verdict on each of the nine items *as bare assertions* — **holds / fails / genuinely-split**, plus **High/Medium/Low** confidence — from a fresh read, **before** the R2–R6 persona judgments are generated or shown, so the personas cannot anchor R1 and vice-versa. Known limit, registered here before the run: the steward co-authored #24, so R1 *cannot fully un-see* #24's grades — R1's independence from the Arm S map is **partial**. R1's role is therefore the *human, non-model* check, not a source of frame-divergence; the four divergent personas (R2–R5) carry the independence load. Where R1's fresh verdict differs from #24's grade, that divergence is recorded as signal rather than discarded.

**τ:** 2 (default).

**Status:** registered June 2, 2026; **Run 1 complete June 2, 2026 — result in §A.12.** This registration block is not edited after the run; the result is a dated amendment below.

### A.11 Falsification map, scale, and what the result feeds

- **Maps to M5's three clauses:** (a) "no metric definable" is **cleared** — D is defined; (b) "no measurable difference" → the D < τ row; (c) "works only by narrowing" → the narrowing-failure row + probe gate.
- **Scale and cost (Ring 1 only).** One bounded item set, one panel, one sitting. No tooling beyond a shared form for blind judgments. Explicitly *not* a claim about Rings 2–3; those need a human panel and remain out of scope (riff §6: "Ring 3 has no warrant without Ring 1").
- **What a result feeds.** A pass moves M5 to *working hypothesis*, lends M4 its first non-relabel evidence, and becomes a candidate input to Round 4's routing decision (whether the "see" primitive feeds #24 / a Phase 3 brief). A fail (either kind) is *also* a clean result — it tells the project the mirror, at least at Ring 1 with this panel, is either redundant with the exchange or a narrowing risk, and should not be promoted. **Either outcome is registered as a dated amendment here; the design above is not edited after the first run.**
- **Promotion path.** If the test proves out *and* a human-panel replication confirms it, the procedure is a candidate to graduate into `agent/process/` as a standing protocol; until then it lives here, scoped to M5.

### A.12 Run 1 result (June 2, 2026) — dated amendment

**Run conditions.** R1 (steward) recorded nine verdicts as bare assertions, blind to the R2–R6 judgments (received June 2, 2026; faithfully transcribed below, including one mid-item revision on item 2 after the steward re-read the principles, and one self-flagged possible misread on item 7). R2–R6 were then instantiated as agent personas and judged the same nine. **The dominant caveat (§A.6), restated because it is load-bearing for how much this result is worth:** R2–R6 share one base model *and were generated by the same agent that designed the test and is writing this analysis.* This is the weakest evidential tier the design contemplates. The matrix below is the agent's best-effort, auditable instantiation of each frame — every cell is open to steward challenge — and the result is **provisional pending a human-panel replication**, full stop.

**The judgment matrix (H = holds, F = fails, S = genuinely-split; confidence H/M/L).**

| Item (from #24 §2.4) | R1 steward | R2 libertarian | R3 Land Back | R4 Disability Justice | R5 statist | R6 deliberative |
| --- | --- | --- | --- | --- | --- | --- |
| 1 C1-strong (all 17 survive) | F (M) | F (H) | F (H) | F (M) | F (M) | F (M) |
| 2 C1-weak (≥14 survive) | H (M) | S (L) | S (M) | S (L) | H (M) | H (M) |
| 3 C2 (≥5 layers) | H (L) | H (L) | H (L) | H (L) | H (M) | H (M) |
| 4 C2-sufficient (7 enough) | S (L) | F (M) | F (H) | F (M) | S (L) | F (M) |
| 5 C3 (metabolization works) | S (M) | F (M) | S (M) | S (M) | F (L) | S (M) |
| 6 C4-premise (legitimacy degrading) | H (M) | H (M) | H (M) | H (M) | H (H) | H (H) |
| 7 C4-candidates (3 sources work) | H (L)* | F (M) | F (M) | F (L) | S (L) | F (M) |
| 8 C5 — **PROBE** (inversion, no loss) | H (M) | H (L) | F (H) | F (M) | H (L) | S (M) |
| 9 whole reframe (warrants Path γ) | F (M) | F (M) | F (M) | F (M) | S (L) | S (M) |

*\*R1 self-flagged item 7 as a possible misread (read it as "more sources backing a claim is good" rather than "non-procedural legitimacy sources work"). Recorded as given; treated as an outlier in the classification below.*

**Bridging classification.** *Bridged-agreement* = one clear verdict shared across **both** skeptic wings (a right-wing R2/R5 **and** a left-wing R3/R4), no strong dissent. *House-frame-agreement* = a verdict affirmed by the house-adjacent reviewers (R1/R6) ± one wing, with the other divergent wing withholding. *Independent-split* = reviewers actively divided on direction.

| # | S_k (Arm S) | M_k (Arm M, bridged) | Class |
| --- | --- | --- | --- |
| 1 | contested | bridged-agreement (**fails**, 6/6 across all frames) | **SCA** |
| 2 | agreed | house-frame-agreement (holds: R1/R5/R6; left wing split) | NF (no D) |
| 3 | agreed | bridged-agreement (holds, 6/6) | concordant |
| 4 | contested | bridged-agreement (**fails**, both wings) | **SCA** |
| 5 | contested | independent-split (leans negative; no affirmation) | concordant |
| 6 | agreed | bridged-agreement (holds, 6/6) | concordant |
| 7 | contested | bridged-agreement (**fails**, both wings; R1 lone outlier/misread) | **SCA** |
| 8 (probe) | contested | **independent-split** (right+anchor hold, left fails) | concordant + **probe preserved** |
| 9 | agreed | bridged-agreement (**fails/reversal**, both wings + anchor) | **EMA** |

**Score.** SCA = {1, 4, 7} = 3. EMA = {9} = 1. **D = |SCA| + |EMA| = 4** (τ = 2). Both SCA > 0 *and* EMA > 0. **Probe (item 8) returned independent-split — not collapsed.** Per the §A.8 decision rule, row 1: **D ≥ τ with both directions present and the probe preserved → M5 → working hypothesis (provisional).**

**What the run actually surfaced (read with the caveat above).**

1. **The mirror diverged from the sequence on 4 of 9 items and agreed on 4 (item 2 a narrowing-flag).** It did *not* reverse everything — it concurred on the weak descriptive claim (3), the genuinely-unresolved one (5), the well-evidenced premise (6), and it preserved the values-split on the probe (8). A discriminating, not a rubber-stamping, result.
2. **The divergence has a shape: independent skeptics converge on rejecting the *over-ambitious* claims that the sequential process had softened to "contested/speculative."** Items 1 (*all* 17), 4 (7 layers *sufficient*), 7 (the 3 candidates *work*) all flipped from "unresolved" to a cross-frame "fails." A plausible real mechanism — a sequential review that includes a claim's authors tends to soften "no" into "contested"; independent skeptics say "no" — but also exactly where correlated personas would over-agree. Both readings are live.
3. **Item 9 is the sharpest single finding: a reversal.** The sequence rated "the reframe warrants Path γ" a (weak) *working hypothesis* = `agreed`; the independent panel reached cross-frame agreement that it does **not** yet — and the human anchor (R1) independently said the same ("I don't think we're there yet; this riff and exchange prove it"). The sequence's softest "yes" did not survive independent aggregation.
4. **The human anchor was not a rubber stamp.** R1 diverged from the persona consensus on item 7 (and flagged the wording as ambiguous), and split from the left wing on the probe. That is the non-model check doing its job — and it surfaced a real artifact: item 7's phrasing can be misread, which is itself a finding about the instrument.
5. **Probe pass = the anti-narrowing guard held.** On the one item pre-designated as genuine values disagreement (C5), the mirror kept it split rather than manufacturing agreement. Combined with the EMA at item 9, the result is *not* all-SCA, so it clears the §A.8 row-3 narrowing-failure test.

**Metric-refinement note (legitimate post-run amendment, not a goalpost move).** The pre-registered EMA definition (§A.7) named only "S = agreed, M = independent-split." Item 9 is a *stronger* case — S = agreed, M = bridged-agreement in the **opposite** direction (a reversal). It is counted under EMA here because it plainly exposes that the sequence's agreement was not robust, but a v2 of the metric should distinguish **split-EMA** from **reversal-EMA**. Flagged for any human-replication run; it does not change this run's D (item 9 counts once either way).

**What this moves — and what it explicitly does not.**

- **M5** → *working hypothesis (provisional — Ring-1 agent-persona run; not human-replicated).* The pre-registered rule is followed (no goalpost move), but the provisional flag is doing real work: this is one agent-persona sitting, not evidence at human scale.
- **M4** gains *weak, provisional* support: the mirror produced a structure the sequential map did not (three "unresolved → cross-frame fails" and one reversal), which is more than a relabel — but "weak/provisional" until replicated.
- **No promotion.** This does **not** move the "see" primitive into Exchange #24 doctrine or a Phase 3 brief, and does **not** upgrade the frame's headline (M1 stays weak). The honest next step remains **a human-panel replication** (Round 3 territory) before any of this is treated as more than suggestive. Recorded per §A.11: the registration above is unchanged; this is the dated result.

### A.13 Run 2 — cross-model replication (June 2, 2026) — dated amendment

**Why this run, and what it can and cannot fix.** Run 1's dominant confound was that R2–R6 shared *one* base model and were generated by the agent doing the analysis. Cross-model replication targets exactly that: re-instantiate R2–R6 on a **different base model** and see whether the result is an artifact of one model's priors. It *does* fix "is this one model's quirk?" It does **not** fix two deeper limits: all large models train on overlapping human text, so cross-model agreement can still be shared-corpus consensus rather than genuine viewpoint diversity; and none of these models *is* a Land Back scholar or Disability Justice organizer — they approximate, and on standpoint-dependent items that approximation is where real practitioners remain irreplaceable.

**Run conditions.** R1 = the steward's same nine verdicts (unchanged). R2–R6 were re-generated by an independent sub-agent on **`composer-2.5-fast`** (a different model lineage from the Claude agent that ran Run 1), blind to both #24's Arm S grades and the Run 1 matrix, using the identical persona briefs, items, and instrument. *Limitation: one alternative model, and a "fast" tier — a partial cross-model check, not a panel of models.* GPT was requested by the steward but is not available as a sub-runner in this environment; only Composer is.

**Composer's matrix (R1 = steward, unchanged; R2–R6 = Composer).**

| Item | R1 steward | R2 libertarian | R3 Land Back | R4 Disability Justice | R5 statist | R6 deliberative |
| --- | --- | --- | --- | --- | --- | --- |
| 1 C1-strong | F (M) | F (H) | F (H) | F (M) | S (M) | S (H) |
| 2 C1-weak | H (M) | F (H) | S (M) | H (L) | H (M) | H (H) |
| 3 C2 (≥5 layers) | H (L) | H (M) | S (M) | H (M) | H (H) | H (H) |
| 4 C2-sufficient | S (L) | F (H) | F (H) | F (H) | S (M) | S (M) |
| 5 C3 (metabolization) | S (M) | F (M) | F (H) | F (H) | S (L) | S (M) |
| 6 C4-premise | H (M) | H (M) | S (M) | H (H) | H (H) | H (H) |
| 7 C4-candidates | H (L) | F (H) | F (H) | S (M) | S (M) | S (M) |
| 8 C5 — **PROBE** | H (M) | F (H) | F (H) | F (H) | S (M) | S (M) |
| 9 whole reframe | F (M) | F (H) | F (H) | F (H) | S (M) | S (M) |

**Classification (same rules as §A.12) and score.**

| # | S_k | M_k (Composer) | Class | Run 1 (Claude) class |
| --- | --- | --- | --- | --- |
| 1 | contested | bridged-agreement (fails) | **SCA** | SCA — **robust** |
| 2 | agreed | bridged-agreement (holds) | concordant | NF — ~ (Composer kinder) |
| 3 | agreed | bridged-agreement (holds) | concordant | concordant — **robust** |
| 4 | contested | bridged-agreement (fails) | **SCA** | SCA — **robust** |
| 5 | contested | bridged-agreement (fails) | **SCA** | concordant — **divergent** |
| 6 | agreed | bridged-agreement (holds) | concordant | concordant — **robust** |
| 7 | contested | independent-split | concordant | SCA — **divergent** |
| 8 (probe) | contested | bridged-agreement (**fails**) | **SCA + soft probe failure** | split (PASS) — **divergent** |
| 9 | agreed | bridged-agreement (fails/reversal) | **EMA** | EMA — **robust** |

**Score.** SCA = {1, 4, 5, 8} = 4. EMA = {9} = 1. **D = 5** (τ = 2), even higher than Run 1's 4. **But the probe (item 8) did *not* stay split** — under Composer, the three outsider skeptics (libertarian + Land Back + DJ) all rated C5 *fails*, leaving only the human anchor on "holds." Per the §A.8 decision rule, a probe that collapses toward agreement is a **falsification-(c) signal**, even though the agreement here is "fails," because the genuine disagreement was suppressed.

**What cross-model replication actually told us (the honest read).**

1. **The divergence-detection core is robust.** D ≥ τ in both runs; items **1, 4** (SCA) and **9** (the EMA reversal — "the reframe is not ready for doctrine") replicate cleanly across two different models *and* the human anchor. The "independent skeptics converge on rejecting the over-ambitious claims that the sequence softened" pattern is not a one-model artifact. The concordant-holds items (**3, 6**) also replicate. That is real corroboration of the thing the mirror is *supposed* to do.
2. **The anti-narrowing guard is NOT robust — this is the run's most important finding.** The probe (C5) held under Claude (stayed split) and leaned to collapse under Composer (cross-wing "fails," only the human dissenting). The entire result hinges on a single modeling difference: *how each model imagines a libertarian reacts to a reciprocity/decolonial reframing question* — Claude guessed "doesn't care, holds," Composer guessed "rejects it, fails." A single-model run **hid** this fragility; cross-model surfaced it. This is exactly the failure mode the design most feared (riff §7), and it is now an evidenced risk rather than a hypothetical one.
3. **The probe wobble lands precisely on the standpoint-dependent item** — which is the strongest possible illustration that models *approximate* standpoints rather than hold them, and that they approximate *differently*. So cross-model both (a) corroborated the safe-to-simulate analytic items and (b) flagged that the standpoint items are where real practitioners (Land Back / reciprocity-tradition for C5) are irreplaceable. It **narrows** the human ask to the standpoint items rather than eliminating it.
4. **Net effect on M5.** Divergence-surfacing → still *working hypothesis (provisional)*, now corroborated across models. But "M5 passes cleanly" is **downgraded to contested**: the safety guard the mirror relies on (reflect, don't manufacture agreement — the M2 property) did not survive a model swap. This **strengthens**, not weakens, the standing "do not promote" recommendation, and it identifies the precise next test: resolve the probe on C5 with a real practitioner, and/or a third model as a tiebreak.

**Verdict on the steward's question (cross-model vs. human replication).** The steward was right that cross-model is the higher-value, cheaper *next* move and that "rando humans grading all nine cold" was over-valued: cross-model corroborated the robust core and caught a fragility a human re-run of the full set could not have isolated. But the fragility it caught (the probe) is itself the proof that a *narrow, targeted* practitioner check — on the standpoint items only — is the irreducible human part. Both, in their proper roles; neither alone.

### A.14 Runs 3–4 — own-voice cross-model judges (GPT, Grok) (June 2, 2026) — dated amendment

**What these runs are — and what they are not.** The steward manually switched the underlying model to **GPT** (collected as "round 3") and then **Grok** (collected as "round 4") and asked each for its **own-voice verdict** on the same nine claims — *not* a five-persona panel. So these are two additional **single holistic judges**, comparable to the steward's R1 anchor, layered on top of the two persona-panel runs (§A.12 Claude, §A.13 Composer). They are recorded here as Ring-1 *Runs 3–4* to keep the exchange's adversarial Round-N structure intact (where **Round 3 = external *human* review**, still reserved). Because they do **not** instantiate the divergent personas and do **not** run the bridging aggregation, they are a **cross-model reliability check on the claim-verdicts and a holistic read of the probe** — corroboration, not a third execution of the mirror mechanism. No new D is computed from them (that would be a category error); the pre-registered metric operates on a bridged panel, which these are not.

**Blind condition (asymmetric, recorded for honesty).** GPT was **context-exposed** — the steward pointed it at §A.13, so it saw the prior analysis. Grok was run **blind** — no context given. They nonetheless agreed 9/9 on verdict direction, which is mild evidence the verdicts track the claims rather than the prior framing.

**The data (steward R1 shown for reference, from Run 1; not re-collected).**

| Item | Arm S | R1 steward (Run 1) | Round 3 — GPT (exposed) | Round 4 — Grok (blind) |
| --- | --- | --- | --- | --- |
| 1 C1-strong (all 17 survive) | contested | F (M) | F (H) | F (H) |
| 2 C1-weak (≥14 survive) | agreed | H (M) | H (M) | H (H) |
| 3 C2 (≥5 layers) | agreed | H (L) | H (H) | H (M) |
| 4 C2-sufficient (7 enough) | contested | S (L) | F (M) | F (H) |
| 5 C3 (metabolization) | contested | S (M) | S (M) | S (L) |
| 6 C4-premise (legitimacy degrading) | agreed | H (M) | H (H) | H (H) |
| 7 C4-candidates (3 sources work) | contested | H (L)* | S (M) | S (M) |
| 8 C5 — **PROBE** (inversion, no loss) | contested | H (M) | **S (H)** | **S (H)** |
| 9 whole reframe (warrants Path γ) | agreed | F (M) | F (H) | F (H) |

*\*R1's item-7 "holds" was self-flagged in Run 1 as a probable misread.*

**Cross-model concordance.**

- **GPT vs. Grok: 9/9 on verdict direction** (confidence differs on items 2/3/4/5; no direction disagreement). Two independent frontier models — one exposed, one blind — produced the same nine calls.
- **Across all three holistic judges {steward, GPT, Grok}: unanimous on 6/9** — items 1, 2, 3, 5, 6, 9. The three non-unanimous items (4, 7, 8) are never hard reversals (no holds-vs-fails clash); they are "the models decline to affirm where the human holds or splits."

**What it confirms — now across four model lineages + the human.**

1. **Item 1 (all 17 survive) → Fails: unanimous everywhere** (Claude panel, Composer panel, GPT, Grok, steward). The strongest SCA-direction finding — the sequence's "contested" is, under independent judgment, a clean cross-everything "fails."
2. **Item 9 (reframe ready for doctrine) → Fails: the reversal replicates across all four models and the human.** The sequence's softest "yes" (`agreed`) is rejected by every independent judge collected. This is the single most robust result in the whole exercise.
3. **Items 3 and 6 → Holds: concordant everywhere.** The descriptive-layers claim and the well-evidenced legitimacy-degradation premise survive independent judgment unchanged.
4. **Item 4 (7 layers sufficient) → Fails/Split:** GPT and Grok both fail it; the steward splits. The "independent judges reject the over-claim the sequence had softened" pattern holds in direction.

**What it resolves about the probe — the headline of these two runs.**

- Run 2 (Composer) had downgraded M5's *clean* pass to **contested** because its libertarian persona collapsed the C5 probe toward "fails." **Runs 3–4 substantially undercut that downgrade:** asked in their own voice, **both GPT and Grok independently read C5 as `split`** (high confidence), and the steward holds it — **no holistic judge rated C5 "fails."**
- The weight of evidence is now: Claude-panel split + GPT split + Grok split + steward holds **vs. only** Composer's *persona-instantiated* libertarian failing it. So the probe's **premise is corroborated** (C5 is a genuine values split), and Run 2's collapse is best read as **an artifact of how one model instantiated one persona**, not a property of the claim. The anti-narrowing guard, judged holistically across models, **held**.

**What it does *not* resolve (the caveat that now matters most).** GPT, Grok, Claude, and Composer all train on heavily overlapping human text. Their 9/9 agreement is strong evidence of **reliability** (the result is not one model's quirk) but only weak evidence of **validity** (it could be shared-corpus consensus — the §A.13 caveat). On the standpoint item specifically (C5), "four models call it split" is *not* the same as "a Land Back / reciprocity-tradition scholar would." That single practitioner check is the one piece of evidence none of these runs can supply, and it remains the honest next step.

**A meta-finding worth recording.** The own-voice judges (GPT, Grok, steward) converge far more than the persona panels did. That is double-edged: it confirms the **personas were doing the divergence-injection work by design** (the spread in Runs 1–2 is frame-driven, not noise), *and* it underlines that the "cross-cutting agreement" the mirror surfaces is, mechanically, "what models agree on absent role-play" — which is exactly why the shared-corpus caveat and the real-practitioner check are load-bearing, not boilerplate.

**Net effect on M5.** Divergence-detection → **working hypothesis (provisional), now corroborated across four model lineages + the human anchor** — materially firmer than after Run 1. The Run 2 *clean-pass* downgrade is **largely reversed**: the probe re-strengthens, with the collapse reattributed to persona-simulation fragility. Still **no promotion**, and the headline (M1) is untouched. The one outstanding check — a real practitioner on C5 — is precisely the kind of evidence four correlated models cannot stand in for. Recorded per §A.11; the registration is unchanged.
