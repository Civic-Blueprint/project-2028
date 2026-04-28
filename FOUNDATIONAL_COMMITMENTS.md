---
title: Foundational Commitments
description: Operational companion to PRINCIPLES.md. Specifies what each principle binds the project to, what counts as meeting it, and what misuse of it would look like — without prescribing any particular mechanism.
provenance: "collaborative"
---

# Foundational Commitments

> **Provenance:** `collaborative` — Human-directed AI drafting with steward synthesis, revision, and final approval. See [Content Provenance Standard](docs/CONTENT_PROVENANCE.md).
>
> **Relationship to Principles:** [PRINCIPLES.md](PRINCIPLES.md) states the project's commitments in short, outcome-level form. This companion specifies, per principle, *what the commitment binds the project to, what counts as meeting it, what would count as violating it, and what misuse-resistant language looks like*. It is an instance of [Round 4 challenge 1d](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-1--challenges-to-the-revised-principle-5) and [Round 5 Deliverable 1 (v2)](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-1--revised-principle-5-text-v2) in Exchange #21, generalized to all 17 principles.

---

## Why this document exists

The project's principles are designed to be readable, short, and poetic enough that they can function as a public commitment document. That form carries a cost: the operational specificity needed to evaluate whether a particular reform *actually meets* a principle — or is being used to justify an outcome the principle would reject — does not fit in the principle itself.

This document carries that specificity.

The structure below, applied per principle, does four jobs:

1. **Operational meaning.** States what the commitment binds the project to in terms concrete enough to evaluate a proposal against.
2. **Minimum mechanism requirements.** Where a principle is vacuous without *some* mechanism existing (e.g., "accountability" requires some mechanism for affected parties to surface complaints), specifies the minimum functional requirements without prescribing a particular form.
3. **Conditions and caveats.** Names the conditions under which the commitment is meaningful, the reference-class limits, and the tradeoffs with neighboring principles.
4. **Anti-misuse clauses.** Names the predictable ways the principle can be weaponized against the outcomes it is meant to protect, and what would count as hollow adoption.

This document does *not* specify particular mechanisms. That work lives in [SYSTEMS_FRAMEWORK.md](SYSTEMS_FRAMEWORK.md) (mechanism tradeoffs), in [`agent/doctrine/`](agent/doctrine/_DOCTRINE_INDEX.md) (adopted operational frameworks — currently empty by design, with the bounded-governance doctrine from [Exchange #21](agent/exchanges/government-overreach-ownership-ratchet-exchange.md) planned as the first entry via [Roadmap follow-up F3](ROADMAP.md)), and in the [Proposal Catalog](proposals/PROPOSAL_CATALOG.md) (specific instantiations). The separation is deliberate: Principles specify the WHAT; Foundational Commitments specify *what it takes to meet the WHAT*; Systems Framework and Doctrine describe the space of HOWs; Proposals are concrete instances.

---

## Reading conventions

- **Commitment sections are numbered to match [PRINCIPLES.md](PRINCIPLES.md).** Principle 5 ↔ Commitment 5.
- **"To be developed" markers** indicate sections that have not yet been stress-tested through an adversarial exchange. Those sections will be populated as their principles go through the review cycle. Do not treat a "To be developed" section as absence of commitment; treat it as operational specificity not yet written.
- **Cross-references to exchanges** point to the specific round or deliverable where the operational specificity was derived.
- **Cross-references to neighboring principles** are included wherever a commitment interacts meaningfully with another. A foundational commitment is rarely fully specified in isolation from the others.

---

## 1. Dignity is inherent and unconditional

> *To be developed.* Principle 1 is one of the project's strongest commitments and is currently expressed almost entirely at the outcome level. An adversarial exchange specifically on Principle 1's operational requirements has not yet been run. Pending that work, the minimum this document records is:
>
> - Dignity applies regardless of economic productivity, social status, immigration status, incarceration status, or any other status a society treats as grounds for differential treatment.
> - A reform that improves outcomes in aggregate while depriving a specific group of dignity fails this commitment even if it improves the aggregate.
> - Misuse test: "dignity is unconditional" must not be weaponized to block triage decisions that are themselves structured to preserve dignity under resource constraint. Triage with dignity-preserving structure is not a violation of this principle; triage that treats certain groups as beneath triage is.

---

## 2. Essential needs should not be held hostage to avoidable scarcity

> *To be developed.* The operational specificity here ties closely to [Systems Framework](SYSTEMS_FRAMEWORK.md) Domain 2 analysis and to the housing and healthcare exchanges. Pending dedicated work, the minimum this document records is:
>
> - "Avoidable" is an empirical claim about the gap between productive capacity and realized provision. A scarcity that cannot be reduced within current technology or ecological limits is not avoidable.
> - Reforms that reduce avoidable scarcity by reducing measurement (e.g., tightening benefit eligibility) do not meet this commitment; they evade it.
> - Misuse test: the principle must not be used to justify authoritarian provision that would require dissolving accountability (Principle 4) or legibility (Principle 10). Fast, compassionate provision that preserves accountability is compatible; provision that requires suspending accountability is not.

---

## 3. AI must augment agency, not replace democratic accountability

> *To be developed.* The AI governance framework is the subject of [Exchange #11](agent/exchanges/ai-commonwealth-vs-governance-exchange.md) and of follow-up F4 from [Exchange #21](agent/exchanges/government-overreach-ownership-ratchet-exchange.md). Operational specificity will be drawn from the v2 frontier-AI package (Round 5 Deliverable 4) once F4 has run. Pending that work, the minimum this document records is:
>
> - "Augment agency" has an evaluable form: does the deployed system expand the number of meaningful choices available to the people it affects, or does it narrow them?
> - Deployment into high-stakes decision pathways (credit, medical, carceral, immigration) must carry human review that is substantive, not rubber-stamp.
> - Misuse test: "democratic oversight" of AI must not be reduced to nominal committees whose decisions have no operational effect.

---

## 4. Power must remain accountable, legible, and reversible

> *To be developed.* Operational commitment will be drafted alongside Commitment 5 (below) since the two principles together carry the project's theory of accountable institutions. The minimum this document records is:
>
> - *Accountable* requires that some mechanism exists by which affected parties can surface grievance, trigger evaluation, and observe response.
> - *Legible* requires that the structure and operation of the power in question are understandable to a non-expert affected party in a time-bounded way.
> - *Reversible* requires that decisions taken under a given authority can be revisited when conditions change; rules that are designed to prevent their own revision fail this commitment.
> - Misuse test: "accountability" must not be reduced to a publication requirement that affected parties cannot access, cannot understand, or cannot act on.

---

## 5. Critical systems require inclusive institutions with bounded rules

> Derived from [Exchange #21 Round 5 Deliverable 1 (v2)](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-1--revised-principle-5-text-v2). This is the first commitment section populated in full. The others will follow the same structure as their dedicated exchanges complete.

### What this commitment binds us to

The project commits to evaluating the governance of every critical system — infrastructure, health, information, finance, and foundational compute — against two conjoint standards that together constitute "public interest" in this document's operational sense: **inclusiveness** and **bounded-ness**. Either standard alone is insufficient; the pairing is the commitment.

- *Inclusive* means power is broadly distributed rather than concentrated in a narrow elite (state, corporate, or other); participation in rule-making is genuine rather than nominal; and the institution is accountable to those it affects.
- *Bounded* means the institution's authority carries credible structural limits — stopping points, reversibility provisions, independent oversight, transparent risk assessment, and scheduled review — so that it cannot expand without accountability or entrench itself against future correction.

### What counts as meeting this commitment

A governance arrangement meets Commitment 5 when all five of the following are demonstrably present in the arrangement's design *and* its observed operation:

1. **Broad distribution of rule-making power.** No single actor (state agency, corporate entity, technocratic body) can unilaterally set, modify, or enforce the rules that govern the critical system in question.
2. **Genuine participatory mechanism.** Some documented mechanism exists by which affected parties can surface concern, contest rules, and observe how their input affected outcomes. The mechanism must be accessible (not require specialist mediators to engage); responsive (must produce observable response, not only acknowledgment); and evaluable (must produce a record against which its own effectiveness can be assessed).
3. **Credible structural limits.** The institution's authority carries enumerated stopping points (defined scope of action), reversibility provisions (mechanisms by which decisions can be undone without extraordinary procedure), and independent oversight (a body with authority to evaluate compliance that is not itself captured by the governed institution).
4. **Scheduled review.** The governing rules carry a scheduled re-authorization requirement, not merely an amendment possibility. Rules that drift into permanence are failing this commitment.
5. **Transparent risk assessment.** The institution's operation must be documented in a way that makes its risks — to the affected public, to future generations, to neighboring systems — legible to a non-specialist.

### Minimum mechanism requirements

This commitment is vacuous without *some* mechanism for each of the five. It does not require any particular mechanism; several are compatible.

| Requirement | Acceptable mechanism forms | Forms that do *not* satisfy |
|---|---|---|
| Broad distribution of rule-making | Democratic legislation; consociational or consensus-democratic procedures; constitutionally entrenched federation; sortition-based citizen assemblies; cooperative/codetermination structures | Unilateral executive action without legislative constraint; corporate self-governance of a critical system without public oversight |
| Participatory mechanism | Public comment with evaluable response obligations; ombudsman with binding referral authority; citizen assemblies with real agenda-setting power; rapid-complaint-to-remediation pathways with triggered escalation | Comment periods with no response obligation; advisory bodies with no authority to affect outcomes |
| Structural limits | Constitutional or super-statutory entrenchment with demanding but not impossible amendment process; independent oversight with publication authority; sunset clauses tied to scheduled review | Rules that cannot be amended at all; rules that can be amended by simple majority of the governing institution itself |
| Scheduled review | 5-year (or shorter) re-authorization requirement with evidentiary review; automatic expiration absent re-authorization; triggered review on specified conditions | Permanent rules with no review mechanism; review processes that are nominal rather than substantive |
| Transparent risk assessment | Mandatory risk-risk analysis (baseline vs. intervention vs. alternative-inaction); distributional-incidence review (see [Exchange #21 Round 5 Deliverable 5](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-5--revised-distributional-incidence-protocol-v2-anti-theater)); public reporting accessible to non-specialists | Proprietary models not subject to external review; assessment delivered only to the governing institution itself |

### Conditions and caveats

- **Reference-class limitation.** The clearest working instances of inclusive-plus-bounded institutions are in small, high-trust, wealthy polities (Switzerland, Sweden, Norway, Alaska) plus two supranational regimes (EU AI Act, California SB 53). Transfer to larger, more heterogeneous polities is an open question the project treats as research debt, not settled fact. A proposal that invokes this commitment in a non-reference-class polity must engage the transferability question explicitly.
- **Ownership-governance interaction.** The question of *who owns* a critical system is distinguishable from the question of *how it is governed* but not independent of it. Ownership concentration structurally shapes governance capacity. A proposal combining a particular ownership form with this commitment must address how that ownership pattern is compatible with inclusive, bounded rule-making in practice.
- **Tradition-naming.** This commitment aligns with the post-1994 rules-based social-democratic tradition (Swedish / Swiss / Acemoglu-Robinson / Rodrik) adapted for larger and more heterogeneous polities. It is not libertarian (permits the full range of public-interest intervention), not unreconstructed progressive (permits no substantive commitment without bounded-rule discipline), and not technocratic (substantive decisions remain political).

### Anti-misuse clauses

1. **Adopt-and-hollow resistance.** A government, corporation, or other institution can adopt the *form* of inclusive-plus-bounded governance while hollowing out its substance (Hungary 2010–present is an active instance). A commitment to this principle requires meeting four authenticity conditions:
   - The oversight institution *demonstrably changes* the governed institution's behavior in observable cases, not only in formal reports.
   - Escape clauses are exercised and compensated on schedule, not retained in name only.
   - Opposition parties or contesting voices participate materially in rule design and continue to have material participation in rule maintenance.
   - Scheduled reviews produce modifications, not only reauthorizations.
2. **Neutrality claim resistance.** This commitment is not neutral. Claiming it is neutral is itself a misuse, because it papers over the normative choice the commitment embodies. Proposals should name the tradition this commitment operates within rather than present it as a view from nowhere.
3. **Ratchet resistance.** Proposals that claim this commitment as justification for *net regulatory expansion* — adding rules without replacing or sunsetting existing ones — must justify the expansion explicitly on asymmetric-risk or coordination grounds. The project's default is *replacement over addition*.

### Companion references

- [Exchange #21 Round 5](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#round-5) — source of this commitment's operational specificity.
- [Adversarial Review Protocol](agent/process/adversarial-review-protocol.md) — the process that produced the Round 4 challenges this commitment responds to.
- Bounded-governance doctrine note (planned, via Exchange #21 follow-up F3) — will house the ten-feature doctrine as an adopted operational framework.

---

## 6. The gains from automation should strengthen society, not destabilize it

> *To be developed.* Operational commitment will be drafted alongside Commitment 3 (AI governance) once follow-up F4 from Exchange #21 and Exchange #11 have produced the AI-governance framework. The relationship to Commitment 5 (bounded governance) is direct: rules distributing automation gains must themselves be inclusive and bounded. The minimum this document records is:
>
> - Distribution of gains is evaluable. "Benefits accrued to society" is meaningful only with a measurable distributional claim.
> - A proposal that improves aggregate productivity while concentrating gains narrowly does not meet this commitment even if the aggregate improvement is large.

---

## 7. Freedom requires both liberty and material stability

> *To be developed.* Operational commitment depends on the outcome of future work on the [positive-liberty philosophical positioning](PRINCIPLES.md#philosophical-positioning). Pending that work, the minimum this document records is:
>
> - Proposals that deliver formal liberty without material stability meet only half of this commitment.
> - Proposals that deliver material stability by suspending formal liberty fail this commitment.
> - The commitment is a conjoint standard; either half alone is insufficient.

---

## 8. No class of people should become structurally excluded

> *To be developed.* Operational commitment will be drafted in coordination with Commitment 1 (dignity) and Commitment 16 (justice). The minimum this document records is:
>
> - "Structural exclusion" is evaluable: is there a class of people for whom meaningful participation in the economy, polity, or civic life is systematically foreclosed?
> - Reforms that reduce structural exclusion by redefining what counts as "structural" or "meaningful" evade rather than meet this commitment.

---

## 9. Institutions should be designed for competence and trust, not theater

> *To be developed.* Operational commitment ties closely to Commitment 5 (bounded-rule authenticity conditions) since nominal adoption of bounded-governance architecture is a form of institutional theater. Pending dedicated work, the minimum this document records is:
>
> - Competence is evaluable through observable delivery, not through communication strategy.
> - Trust is a consequence of sustained visible performance, not a prerequisite for it.
> - An institution that invests more in appearance-management than in delivery is failing this commitment regardless of its formal structure.

---

## 10. The future should be built in the open

> *To be developed.* Operational commitment ties to Commitment 5 (participatory mechanism requirements) and Commitment 14 (truth and evidence as public goods). Pending dedicated work, the minimum this document records is:
>
> - "Open" has evaluable forms: observable process, accessible records, genuine participation pathways.
> - Performative openness (process that cannot affect outcomes) fails this commitment.
> - Openness must be paired with capture resistance; unbounded openness without design protection is itself a failure mode.

---

## 11. Civilization depends on a functioning biosphere

> *To be developed.* Operational commitment will be drafted in coordination with the ecological-ceiling-indexed ownership category from [Exchange #21 Round 5 Deliverable 2](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-2--revised-taxonomy-v2-seven-categories). Pending dedicated work, the minimum this document records is:
>
> - Biophysical ceilings are not negotiable under this commitment. Ownership and economic-activity claims operate *within* the ceiling, not *against* it.
> - Proposals that externalize biosphere costs to future generations or to populations outside the deciding polity fail this commitment.

---

## 12. The present generation holds obligations to the future

> *To be developed.* Operational commitment interacts meaningfully with Commitment 11 (biosphere), Commitment 13 (pluralism), and Commitment 17 (collective power). Pending dedicated work, the minimum this document records is:
>
> - Irreversibility raises the threshold. Reversible choices fall within legitimate present-generation self-determination; irreversible choices require stronger justification.
> - "The future cannot participate" is a design constraint, not an excuse. Proposals must account for future-generation interests even though they cannot be represented in the deciding process.

---

## 13. Pluralism and self-determination are strengths, not obstacles

> *To be developed.* The operational tension with substantive commitments (per the Tensions section of [PRINCIPLES.md](PRINCIPLES.md#self-determination-vs-substantive-commitments-principle-13-vs-principles-2-8-11-12-15)) is the load-bearing case here. Pending dedicated work, the minimum this document records is:
>
> - Self-determination is protected *within the bounds* of the substantive commitments (2, 8, 11, 12, 15), not as an override of them.
> - Diversity of *means* is protected; unilateral rejection of the substantive *ends* is not.

---

## 14. Truth and evidence must be protected as public goods

> *To be developed.* The operational specificity here is the subject of [Exchange #20 (Social Slop)](agent/exchanges/social-slop-information-integrity-exchange.md). Pending that exchange's completion, the minimum this document records is:
>
> - Truth as a public good is defended through infrastructure (education, research, journalism, discourse channels), not through policing of individual content.
> - Systems whose business model structurally rewards decontextualization fail this commitment regardless of whether specific content is factually true.

---

## 15. The circle of moral consideration must remain open

> *To be developed.* Operational commitment interacts with Commitment 1 (dignity) and with emerging questions about AI moral standing. Pending dedicated work, the minimum this document records is:
>
> - The commitment is to keeping the question open, not to any particular resolution of it.
> - Premature closure (claiming the circle is already correctly drawn) fails this commitment.
> - Premature inclusion (granting standing where evidence is absent) also fails this commitment; the discipline runs in both directions.

---

## 16. Justice mediates between competing claims

> *To be developed.* Operational commitment will be drafted alongside Commitment 17 (collective power). Pending dedicated work, the minimum this document records is:
>
> - Justice operates along three axes (distributive, procedural, corrective), and a proposal must be evaluable on each.
> - "Acceptable losses" is not a justice-compatible framing for groups with standing under the other commitments; distributional incidence (see [Exchange #21 Round 5 Deliverable 5](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#deliverable-5--revised-distributional-incidence-protocol-v2-anti-theater)) is the operational test.

---

## 17. Collective power must be exercised within principled constraints

> *To be developed.* The existing text of Principle 17 already carries substantial operational specificity (five conditions for legitimate coercion). This section will formalize those conditions as evaluable commitments and add anti-misuse clauses. Pending dedicated work, the minimum this document records is:
>
> - Coercion is legitimate when all five of the Principle 17 conditions are met: democratic authorization, substantive-commitment justification, proportionality, transparency with challenge, and reversibility.
> - The principle's non-violence commitment is strategic and principled, not absolute pacifism; it operates because the project's theory of change depends on institutional legitimacy and public trust, both degraded by political violence.

---

## How this document evolves

- New operational commitments are added to this document when an adversarial exchange produces a v2-style revision of the material for a principle. See [Exchange #21 Round 5](agent/exchanges/government-overreach-ownership-ratchet-exchange.md#round-5) as the exemplar pattern for Commitment 5.
- The "To be developed" sections are *not* blanks to be filled in by any contributor. They are placeholders for work that will come out of dedicated exchanges, adversarial review, and — per the Thread E and Thread F work in the [Roadmap](ROADMAP.md) — external human reviewer contribution.
- When a commitment is updated, the corresponding principle in [PRINCIPLES.md](PRINCIPLES.md) may or may not need to change. The division of labor is: Principles state the commitment; Foundational Commitments specifies what it takes to meet it. Principles should change only when the substance of the commitment itself changes; Foundational Commitments changes when the project's understanding of *what meeting the commitment requires* changes.
- Cross-references from this document to exchanges, to Systems Framework, to adopted doctrine notes, and to the Proposal Catalog are expected to multiply over time. The [Coherence Audit Protocol](agent/process/coherence-audit-protocol.md) includes this document in its scope.

---

## On the relationship to mechanism

This document specifies what it takes to meet each principle. It does not specify *which particular mechanism* meets any given requirement. That separation is deliberate and reflects a project-level architectural commitment:

| Layer | Specifies | Example |
|---|---|---|
| [Principles](PRINCIPLES.md) | WHAT the project commits to | "Critical systems require inclusive institutions with bounded rules" |
| **This document** | WHAT it takes to meet the commitment | "Commitment 5 requires broad distribution of rule-making + participatory mechanism + structural limits + scheduled review + transparent risk assessment" |
| [Systems Framework](SYSTEMS_FRAMEWORK.md) / [`agent/doctrine/`](agent/doctrine/_DOCTRINE_INDEX.md) | HOW mechanisms can meet the requirements — with tradeoffs | "Rapid-complaint-to-remediation vs. slow deliberative consensus vs. amendment voting vs. standing ombudsman — tradeoffs across responsiveness, cost, capture resistance, scope" |
| [Proposal Catalog](proposals/PROPOSAL_CATALOG.md) | Concrete instances of HOW | "P-### Open Complaint Pathway with 48-hour Automated Triage and Public Escalation" |

This separation makes it possible to argue WHAT without HOW for most principles; where a principle is vacuous without some mechanism existing, this document specifies the *minimum mechanism requirements* without picking a particular form. Derivation: [Roadmap Thread D (archived)](ROADMAP_ARCHIVE.md#thread-d--can-we-argue-what-without-how-resolved-by-thread-b-adoption).
