---
title: "Source Digest — Anthropic's Advanced AI Framework (\"Policy on the AI Exponential\")"
source_type: industry_policy_proposal
source_title: "Anthropic's Advanced AI Framework"
source_author: "Anthropic PBC"
source_publication: "Anthropic (Policy on the AI Exponential)"
source_date: 2026-06
source_url: "https://www.anthropic.com/policy-on-the-ai-exponential"
source_url_secondary: "https://www-cdn.anthropic.com/files/4zrzovbb/website/0a58d567024a8b448ff15158ebc3625328dfcc1f.pdf"
provenance: "ai-generated, steward-curated"
viewpoint: "industry / frontier-AI-developer policy proposal (self-interested party proposing rules for its own class)"
sub_debates: [7, 8]
research_tier: "T2 — targeted gap-close; the major-lab regulatory *proposal* companion to the enacted-record AI Governance Practice digest"
copyright_notice: "The framework is published by Anthropic for public comment. Brief excerpts are quoted for analytical commentary under fair use; a link to the open-access original is provided."
---

# Source Digest — Anthropic's Advanced AI Framework ("Policy on the AI Exponential")

> **Status (June 2026):** Complete standard digest. Captures Anthropic's June 2026 policy proposal in two parts — (1) frontier-developer obligations and (2) societal-resilience investments — plus the scope thresholds, the federalism/preemption position, and the conclusion's explicit invitation to collaborate. Companion to the [AI Governance Practice digest](source-ai-governance-practice-digest.md) (the enacted regulatory *record*) and the [AI Existential Risk digest](source-ai-existential-risk-digest.md) (the expert-judgment *risk basis*). This digest is the major-lab *proposal* alongside those two.

---

## Why this digest

The project has digests for the enacted AI-governance record (EU AI Act, SB 1047/SB 53, the U.S. EO sequence, NIST) and for the catastrophic-risk literature, but none for a **frontier developer's own proposal for how it should be regulated**. That is a distinct and load-bearing object: it is the rare case of a [Problem Map §11](../PROBLEM_MAP.md#11-ai-and-compute-power-are-concentrating-faster-than-governance-can-respond) actor — a company racing on capability — asking to be bound. Capturing it lets future exchanges test §11's claim that "voluntary commitments have been largely performative" against a concrete counter-instance, and gives the [bounded-governance design package](source-ai-governance-practice-digest.md) a live worked example authored by a regulated party rather than a regulator.

**Provenance caution carried throughout.** This is a `W3`-type **primary document** for the claim *"what Anthropic proposes"* — it is **not evidence** that the proposals are correct, balanced, or adequate. The author is a self-interested party (a Covered Developer proposing the rules that would bind Covered Developers), the document is not peer-reviewed, and the thresholds it recommends conveniently exempt smaller and differently-funded developers. The digest records the proposal faithfully and flags the self-interest rather than laundering it.

---

## Source identification

| Field | Value |
| --- | --- |
| **Title** | Anthropic's Advanced AI Framework |
| **Author / publisher** | Anthropic PBC |
| **Date** | June 2026 |
| **Overview page** | [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential) |
| **Full framework (PDF)** | [Advanced AI Framework — June 2026](https://www-cdn.anthropic.com/files/4zrzovbb/website/0a58d567024a8b448ff15158ebc3625328dfcc1f.pdf) |
| **Structure** | Part 1 (frontier-developer obligations) + Part 2 (societal-resilience measures) |
| **Companion announcement** | Paired with an "Economic Policy Framework" on the same overview page (not digested here) |

---

## Thematic cluster 1: Scope — who and what is covered

The framework targets only the largest developers and the most severe risks, deliberately leaving a wide field unregulated.

**Covered Developer** — both criteria must hold:
- Develops models requiring **more than 10²⁵ training FLOP**, **and**
- Earns **more than $500 million in annual AI-derived revenue**, *or* spends **more than $1 billion per year on AI R&D**.

**Four Enumerated Risk categories:** (a) biological weapons, (b) offensive cyber operations, (c) loss of control, and (d) automated research and development that could accelerate or amplify (a)–(c).

**Catastrophic Risk definition** is explicitly borrowed from enacted California law:

> "Consistent with existing US state law, 'Catastrophic Risk' means a foreseeable and material risk that a Covered Developer's development, storage, use, or deployment of a covered model will materially contribute to significant death, injury, or damage."

The framework footnotes that this definition is "in line with the definition provided in California SB 53" — directly linking it to the [AI Governance Practice digest](source-ai-governance-practice-digest.md)'s SB 53 material.

**Capability threshold (forward-looking).** The framework concedes the FLOP threshold will erode ("the FLOP needed to train dangerous models may fall") and anticipates migrating to a capability-based threshold, with **annual Agency review** of the criteria "with input from industry, academia, governmental entities, and civil society."

**Federalism / preemption.** In the U.S. context, "Congress should not preempt state law unless it enacts a rigorous federal regime that meets or exceeds the strongest measures proposed in this framework," and any preemption "should be construed narrowly, with ambiguity resolved in favor of preserving state authority."

---

## Thematic cluster 2: Part 1 — frontier-developer obligations

Four pillars. The throughline: test for the Enumerated Risks, show the mitigations, publish the findings, and answer to a government Agency with authority to act.

### 2a. Transparency

Developers should publish a **safety framework** (how they evaluate risks and make development/deployment decisions, naming an accountable corporate officer), a **system card** when deploying a materially more capable covered model or one under materially weaker safeguards, and a **risk report at least every six months**. **Critical Safety Incidents** must be reported to the designated Agency within **15 days**. The framework is candid that this is necessary-but-insufficient:

> "While transparency alone is not sufficient for advanced AI, it gives governments, evaluators, and the public a record of what a developer's models can do and how risk is being managed."

### 2b. Independent evaluation

The pillar most relevant to the project's own methodology. Within six months of enactment, developers should "regularly engage at least one qualified independent evaluator" who is free of financial interest and major conflicts, gets **unredacted** access to the latest risk report and system cards plus access to the most capable models, and **publishes** a review. The framework is explicit that the ecosystem does not yet exist:

> "Self-assessment is not enough. At the same time, we recognize that a mature independent evaluation ecosystem does not yet exist."

It proposes growing that ecosystem (standards, a possible licensing system, government or pooled funding, resources for "nascent organizations seeking to become evaluators") and names a failure mode the project's own discipline already guards against:

> "There is a risk that companies seek out whichever evaluator(s) will ask the least of them and be most generous in their assessments."

Their mitigation — government rating of evaluators and **random assignment** of highly-rated evaluators in high-stakes cases — is structurally the same anti-capture move as the project's *decorrelated, blind, adversary-rewarded* review discipline.

### 2c. Security

A security program across the full development environment (weights, training/inference infrastructure, partner access, internal processes), "robust to external and insider threats and scaled to the consequences of compromise," described publicly at a general level with detail to the Agency on request; monitoring and reporting channels for **distillation/extraction attacks**; and regular red-teaming and penetration testing.

### 2d. Enforcement and regulatory authority

Applicable under any enforcement model: prohibit materially false statements about compliance; authorize **civil penalties that "escalate with repeated violations and scale with global annual revenue"**; and require whistleblower channels with anti-retaliation protection. Beyond that, the framework lays out options to **block or deter deployment** of models posing significant catastrophic risk, paired with explicit anti-overreach safeguards: **court enforcement** (the Agency sues for remedies rather than imposing them directly, with provisional remedies only for imminent risk), **cabined discretion** (remedies only for enumerated violations, not the Agency's freelance risk judgment), and **expedited judicial review**. Policymakers "could begin with a lighter-touch model and revisit that choice as model capabilities advance."

---

## Thematic cluster 3: Part 2 — societal resilience

Investments that "pay off regardless of where a threat originates" — natural outbreaks and conventional attacks as well as AI-enabled ones — and that "take years to build and cannot be stood up in a crisis."

- **Biological** (organized as prevention / detection / preparedness): modernized biosafety standards, **gene-synthesis screening** and customer verification, two-way CBRN threat-intelligence channels with legal safe harbors; **pathogen-agnostic biosurveillance** and microbial-forensic attribution; hardened public-health infrastructure, **stockpiled reusable respirators**, airborne-transmission suppression in the built environment, AI-accelerated countermeasure development, broad-spectrum antivirals, and binding after-action reviews.
- **Cyber:** fund maintenance and **AI-assisted remediation of open-source/legacy software**; phishing-resistant identity and content provenance; **forward-deployed support for under-resourced operators** (water utilities, municipalities, school districts, regional hospitals, rural electric cooperatives); a national function tracking frontier cyber capability; safe harbors for defensive coordination; coordinated vulnerability remediation and **patching "at scale" (10–100× current volume, sub-seven-day turnaround)**; and end-of-life/legacy-system replacement programs.
- **Loss of control and automated R&D** — explicitly the least developed agenda, and a candid open call:

> "The societal resilience agenda for loss of control and automated R&D is less mature than it is for biological and cyber risks, and we believe it needs much more active work across the field, from governments, researchers, and industry alike."

Promising directions named: "the capacity to detect and respond to AI systems acting outside their developers' control, and infrastructure for containing or shutting down such systems."

### The collaboration signal

The conclusion is an open door, directly relevant to the steward's "would they collaborate?" question:

> "We invite feedback on these proposals, and we are ready to work with policymakers and experts to put them into practice."

> "But the cost of waiting for perfect policy is having none during a critical period: when the most severe risks of AI are in view, but not yet realized."

---

## Representative excerpt — the case for authority "with teeth"

From the [overview page](https://www.anthropic.com/policy-on-the-ai-exponential):

> "When a model poses risks of this kind, the government should have the legal authority to block or deter its deployment—beyond what exists in current law or in existing proposals in Congress—with civil penalties tied to global annual revenue that escalate with repeated violations."

This is notable because the regulated party is asking for enforcement *stronger* than current proposals — the inverse of the usual industry-lobbying posture, and the specific fact that makes the document worth engaging rather than dismissing.

---

## Research context

| Claim | Evidence | Context |
| --- | --- | --- |
| The framework adopts SB 53's *Catastrophic Risk* definition | **Corroborated** | Stated explicitly with a footnote to SB 53; see [AI Governance Practice digest §SB 53](source-ai-governance-practice-digest.md) |
| The 10²⁵ FLOP threshold matches the EU AI Act's GPAI systemic-risk threshold, and is *lower* than SB 1047/SB 53's 10²⁶ | **Corroborated** | EU AI Act uses 10²⁵ FLOPS (AI Governance Practice digest, cluster 1); California used 10²⁶ |
| Anthropic proposes enforcement stronger than current Congressional proposals | **Corroborated (as a proposal)** | "beyond what exists in current law or in existing proposals in Congress" — a statement of position, not of outcome |
| A mature independent-evaluator ecosystem does not yet exist | **Corroborated** | Consistent with the AI Governance Practice digest's account of nascent AISI/evaluation capacity post-2025 reorganizations |
| Transparency-only is no longer sufficient (a shift from prior posture) | **Partially corroborated** | The overview notes Anthropic "supported" prior transparency-focused state laws but now argues "transparency alone is no longer sufficient" |
| The proposal is disinterested public-policy analysis | **Not established / contested by construction** | Author is a Covered Developer; thresholds exempt smaller/differently-funded rivals; treat as W3 "what Anthropic proposes," never as W1 evidence |

---

## Project 2028 mapping

- **Problem Map.** Primary new evidence for [Domain 11 (AI and compute power are concentrating faster than governance can respond)](../PROBLEM_MAP.md#11-ai-and-compute-power-are-concentrating-faster-than-governance-can-respond) — specifically a counter-instance to its "voluntary commitments have been largely performative" line (a developer asking for binding authority). Also engages [Domain 4 (Institutional capacity is too weak for the demands placed on it)](../PROBLEM_MAP.md#4-institutional-capacity-is-too-weak-for-the-demands-placed-on-it) — the framework is a large state-capacity bet (new Agency, evaluator licensing, biosurveillance) — and [Domain 15 (Democratic process cannot convert public need into institutional action at the speed or scale required)](../PROBLEM_MAP.md#15-democratic-process-cannot-convert-public-need-into-institutional-action-at-the-speed-or-scale-required) on the engineering-vs-legislative timescale mismatch the framework's periodic-review machinery tries to bridge.
- **Principles.** Directly engages [Principle 3 (AI must augment agency, not replace democratic accountability)](../PRINCIPLES.md#3-ai-must-augment-agency-not-replace-democratic-accountability) — the loss-of-control pillar and the "block or deter deployment" authority are AI-scale instances of keeping AI under accountable human control; [Principle 4 (Power must remain accountable, legible, and reversible)](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible) — the court-enforcement / cabined-discretion / judicial-review safeguards are a worked example of bounding a new power so it stays reversible; [Principle 6 (The gains from automation should strengthen society, not destabilize it)](../PRINCIPLES.md#6-the-gains-from-automation-should-strengthen-society-not-destabilize-it) — the resilience agenda is destabilization-mitigation; [Principle 14 (Truth and evidence must be protected as public goods)](../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods) — the transparency/system-card/risk-report regime; and [Principle 17 (Collective power must be exercised within principled constraints)](../PRINCIPLES.md#17-collective-power-must-be-exercised-within-principled-constraints) — the framework is an attempt to put principled constraints around concentrated capability.
- **Verifier cluster (the sharpest overlap).** The **independent-evaluation pillar** is structurally the problem the [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) solves at small scale, and the [Agent Automation and the Verifier memo](../memos/agent-automation-and-the-verifier-memo.md) anticipates: decorrelated, conflict-free, adversary-rewarded evaluation with a human owning go/no-go. Anthropic's "avoid evaluator shopping → rate and randomly assign evaluators" maps onto the memo's *convergence-is-not-validity* / *parallel-not-series* caution. This is the most plausible collaboration surface and the natural focus of any downstream riff. **Downstream (June 14, 2026):** this digest spawned the [Contribution-Surface riff](../agent/explorations/anthropic-framework-contribution-surface-riff.md), the [Decorrelation as a Civic-Governance Primitive riff](../agent/explorations/decorrelation-civic-governance-primitive-riff.md), the [Decorrelation Metrics memo](../memos/decorrelation-metrics-memo.md), and the Path B [Decorrelation as a First-Class Requirement for Independent AI Evaluation memo](../memos/decorrelation-independent-ai-evaluation-memo.md).
- **Bounded-governance design package.** Reads as a near-complete instance of the package the [AI Governance Practice digest](source-ai-governance-practice-digest.md) tracks: scoped thresholds (de minimis exemptions), independent institutions (the Agency + evaluators), escape/redaction clauses, judicial review, periodic/annual review (the "sunset + review" element the enacted regimes were missing), and polycentric federalism (state-floor + narrow-preemption). A clean candidate for the doctrine's "how would this apply to frontier AI?" worked example.

---

## Interpretive notes

- **Self-interest is the load-bearing caveat.** A regulated party proposing its own thresholds is doing two things at once: raising the floor on catastrophic-risk governance *and* drawing the perimeter where it is most defensible for an incumbent. Both readings are true; the project should hold them together rather than collapsing into either "industry capture" cynicism or "the good lab" credulity.
- **It is the proposal half of a pair.** Side by side with the [AI Governance Practice digest](source-ai-governance-practice-digest.md), the corpus now holds the enacted *record* and the major-lab *proposal* for the same problem — which is exactly the structure needed to ask "what does industry want that the law has not yet done, and why?"
- **The collaboration door is genuinely open, but the realistic surface is feedback and ecosystem-building, not partnership.** The conclusion's invitation and the stated need for "nascent organizations seeking to become evaluators" are the concrete hooks; the project's contribution is most credible on *method* (decorrelated independent evaluation) and on the admitted-immature *loss-of-control resilience* agenda, not on frontier-risk domain depth.
- **Reflexivity check.** The framework is itself a performative document — published partly to shape the regulatory regime it describes (cf. the [Reflexivity / Performativity digest](source-reflexivity-performativity-control-systems-digest.md)). Engaging it should not mean adopting its frame; it means testing the project's own commitments against a serious, self-interested proposal.

---

## What verification does and does not cover

Per [Research Protocol §4.4](../agent/process/research-protocol.md#44-what-verification-does-not-substitute-for), this digest is a **citation-integrity** artifact: the two source URLs resolve to the Anthropic overview page and the full framework PDF; the quoted excerpts are verbatim from those documents; the tier is labeled honestly (W3 primary document for *what Anthropic proposes*, with an explicit self-interest caveat — never W1 evidence that the proposals are correct); and every linkage in the Project 2028 mapping quotes the target section's current title verbatim per the [authoring guard](README.md#authoring-guard--quote-actual-section-titles-from-core-normative-documents). It is **not** a truth check: whether the thresholds are right, whether the enforcement design is adequate, and whether Anthropic would in fact collaborate are questions reserved for adversarial review and external human judgment. **§4.1 self-verification checks passed for all sources cited (June 2026).**

---

## Cross-references

| Related digest | Relationship |
| --- | --- |
| [AI Governance Practice (EU AI Act, SB 1047/SB 53, U.S. EO, NIST)](source-ai-governance-practice-digest.md) | Companion: the enacted regulatory *record* this *proposal* sits beside; source of the SB 53 definition the framework adopts. |
| [AI Existential-Risk Literature (Bengio, Russell, Bostrom, IDAIS)](source-ai-existential-risk-digest.md) | Companion: the expert-judgment risk basis underlying the four Enumerated Risks. |
| [Sunstein, *Laws of Fear*](source-sunstein-precautionary-digest.md) | The anti-catastrophe-narrow framing the scoped-to-the-most-severe-risks design instantiates. |
| [Sunset Clauses and Sunsetting Legislation](source-sunset-clauses-digest.md) | The framework's annual/periodic Agency review is the review-and-revise element prior AI regimes lacked. |
| [Reflexivity, Performativity, and the Control-System Reframe](source-reflexivity-performativity-control-systems-digest.md) | The framework as a performative document that helps shape the regime it describes. |

### Project artifacts (non-digest)

| Artifact | Relationship |
| --- | --- |
| [Agent Automation and the Verifier memo](../memos/agent-automation-and-the-verifier-memo.md) | The independent-evaluation pillar is the memo's verifier-tier model applied to frontier-AI governance. |
| [Cross-Lineage Review Harness Protocol](../agent/process/cross-lineage-review-harness-protocol.md) | The project's small-scale instance of decorrelated, anti-capture independent evaluation. |
