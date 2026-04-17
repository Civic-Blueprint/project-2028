---
title: "Source Digest — AI Governance Practice: EU AI Act, California SB 1047/SB 53, U.S. Executive-Order Sequence, NIST AI RMF"
source_type: regulatory_practice_cluster
source_title: "The 2024–2026 Regulatory Record on Frontier AI"
source_author: "Multiple (European Commission; California Legislature; U.S. Executive Branch; NIST; AO Shearman; Carnegie; CalMatters)"
source_publication: "Various (primary legal texts + analytical commentary)"
source_date: 2026-04-16
source_url: "https://artificialintelligenceact.eu/"
source_url_secondary: "https://www.nist.gov/itl/ai-risk-management-framework"
provenance: "ai-generated, steward-curated"
viewpoint: "institutional-design case studies of frontier-AI governance"
sub_debates: [7, 8]
copyright_notice: "Government regulatory texts are public. Commentary excerpts are cited under fair use for analytical purposes."
---

# Source Digest — AI Governance Practice (2024–2026)

> **Status (April 2026):** Complete standard digest. Four thematic clusters: (1) the EU AI Act implementation record; (2) California SB 1047 veto and SB 53 enactment; (3) the U.S. federal executive-order sequence (Biden EO 14110 → Trump rescission → ongoing); (4) NIST AI Risk Management Framework as voluntary scaffold. Companion to the [AI Existential Risk digest](source-ai-existential-risk-digest.md).

---

## Source identification

| Field | Value |
|---|---|
| **EU AI Act — primary** | [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); [Official Commission implementation page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [Implementation timeline resource](https://artificialintelligenceact.eu/implementation-timeline/) |
| **EU AI Act — commentary** | [AO Shearman analysis](https://www.aoshearman.com/en/insights/ao-shearman-on-tech/california-adopts-landmark-ai-law); [Pearl Cohen briefing on upcoming enforcement date](https://www.pearlcohen.com/new-guidance-under-the-eu-ai-act-ahead-of-its-next-enforcement-date/) |
| **California SB 1047** | [Text and veto message (Sept 29, 2024)](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf); [Wikipedia summary of the bill](https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act) |
| **California SB 53 (TFAIA, 2025)** | [Primary bill text; signed 29 Sept 2025](https://leginfo.legislature.ca.gov/); [Carnegie Endowment analysis (Oct 2025)](https://carnegieendowment.org/emissary/2025/10/california-sb-53-frontier-ai-law-what-it-does); [Wharton Accountable AI Lab commentary](https://ai-analytics.wharton.upenn.edu/wharton-accountable-ai-lab/sb-53-what-californias-new-ai-safety-law-means-for-developers/); [Goodwin briefing](https://www.goodwinlaw.com/en/insights/publications/2025/11/alerts-technology-aiml-california-moves-to-regulate-frontier-ai-with-a-focus-on-catastrophic-risk) |
| **U.S. federal EO sequence** | [EO 14110 (Biden, Oct 30, 2023)](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/) — rescinded by Trump EO on AI (Jan 23, 2025); subsequent "AI Action Plan" released July 2025; Congressional proposals ongoing |
| **NIST AI RMF** | [AI Risk Management Framework 1.0 (Jan 2023)](https://www.nist.gov/itl/ai-risk-management-framework) + Generative AI Profile (July 2024); operated by NIST AISI established late 2023 (status partially uncertain after 2025 federal reorganizations) |
| **U.K. AISI** | [UK AI Safety Institute](https://www.aisi.gov.uk/) established November 2023; technical evaluation partnerships with US AISI and other labs |

---

## Thematic cluster 1: EU AI Act — the risk-tiered regulatory architecture

### Structure

The EU AI Act is the first comprehensive cross-sectoral AI regulation in any major jurisdiction. It categorizes AI systems into four risk tiers:

1. **Unacceptable risk** (prohibited): social-scoring systems, untargeted biometric-database scraping, emotion recognition in workplaces/schools, cognitive manipulation, real-time remote biometric ID in public spaces (with narrow exceptions).
2. **High risk** (comprehensive obligations): systems in Annex III domains (biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice, democratic processes) plus AI systems embedded in products regulated under Annex I.
3. **Limited risk** (transparency obligations): chatbots, deepfakes, emotion recognition outside prohibited contexts.
4. **Minimal risk** (no specific obligations, voluntary codes of conduct encouraged).

Separately, **General-Purpose AI (GPAI)** models are regulated with a compute-threshold-based tiering: models trained with >10^25 floating-point operations face additional systemic-risk obligations including risk assessment, incident reporting, and cybersecurity measures.

### Implementation timeline (as of April 2026)

| Milestone | Effective date | Status |
|---|---|---|
| Regulation entered into force | 1 Aug 2024 | ✓ |
| Prohibitions + literacy | 2 Feb 2025 | ✓ In force |
| GPAI obligations + governance structures (AI Office) | 2 Aug 2025 | ✓ In force |
| High-risk Annex III + transparency (Art 50) obligations | **2 Aug 2026** | Approaching |
| High-risk Annex I (embedded in regulated products) | 2 Aug 2027 | Future |
| Commission evaluation checkpoints | 2028, 2031 | Scheduled |

### Current issues (April 2026)

- **"Digital Omnibus" negotiation:** the European Commission is proposing targeted amendments to simplify implementation and adjust timelines for high-risk rules, reinforcing AI Office oversight. Debate ongoing.
- **Code of Practice on content-labeling:** finalization expected June 2026 (ahead of August 2026 enforcement of Article 50 transparency obligations on AI-generated content).
- **Penalties:** up to €35 million or 7% of global turnover for prohibited-AI violations; lower tiers for other categories.

### Assessment

The EU AI Act is a coherent implementation of the risk-tiered compute-governance approach that the AI catastrophic-risk literature (Bengio, CAIS, IDAIS) supports. It includes:

- Compute-threshold-based tiering (GPAI obligations above 10^25 FLOPS).
- Transparency obligations.
- Incident reporting.
- Independent oversight (AI Office plus national competent authorities).
- Codes of practice as operational detail.

Specific criticisms:

- The Annex III high-risk list is broad and potentially over-inclusive for some use cases.
- Compliance costs may disproportionately burden smaller developers and open-source projects (partial exemptions exist but are contested).
- The 10^25 FLOPS threshold may quickly become obsolete as compute cost declines.

### What the EU AI Act teaches for bounded-governance doctrine

The Act is a useful case of *rule-at-scale* design. Strengths: tiered obligation, compute-governance, independent institution, transparency requirements. Weaknesses: no sunset or automatic review provisions built in at the base level; over-reliance on downstream Codes of Practice to carry the operational content; the scope-ratchet risk is non-trivial (Annex III is expandable by the Commission through delegated acts).

---

## Thematic cluster 2: California SB 1047 veto and SB 53 enactment

### SB 1047 (2024): what was proposed and why it was vetoed

**SB 1047 (Wiener):** "Safe and Secure Innovation for Frontier Artificial Intelligence Models Act." Passed both chambers of the California Legislature in August 2024; vetoed by Governor Newsom September 29, 2024.

**Core provisions:**
- Applied to models trained with >10^26 FLOPS and developed at a cost >$100M.
- Required developers to perform safety tests, retain a "kill switch" capability, protect whistleblowers, and certify compliance.
- Created a new Board of Frontier Models to adjust thresholds and issue guidance.
- Provided Attorney General with authority to sue for violations and for "critical harms" caused by covered models.
- Mandated public reporting of safety-incident events.

**Veto reasoning (summary from Newsom's message):**
- The compute-threshold approach is "arbitrary" — it captures frontier developers while missing smaller developers that might deploy equally harmful but differently-developed models.
- Regulatory approach should be evidence-based; insufficient empirical track record to justify the specific obligations.
- California should not regulate in this space alone before federal action.
- Commitment to convene an expert group (Fei-Fei Li and others) to develop a science-based approach.

**Interpretive note.** The veto was consequential. Opponents (industry, some AI researchers) welcomed it. Proponents (other AI safety researchers including Bengio and Hinton who supported SB 1047) considered it a setback. The political coalition on the bill was unusual: Democratic legislators, Republican AI-safety advocates, several major AI lab employees writing in favor against the positions of their employers.

### SB 53 (2025): what was enacted

**SB 53 (Wiener):** "Transparency in Frontier Artificial Intelligence Act (TFAIA)." Signed by Governor Newsom September 29, 2025 — one year to the day after the SB 1047 veto.

**Scope:**
- Applies to "frontier developers" training models with >10^26 FLOPS.
- Additional obligations for "large frontier developers" with annual gross revenue >$500M.

**Key provisions:**
- **Frontier AI Frameworks:** large developers must publish annual frameworks describing how they identify and mitigate catastrophic risks.
- **Transparency reports:** required before deployment, describing model capabilities, intended uses, and risk assessment results.
- **Incident reporting:** "critical safety incidents" (unauthorized access, loss-of-control events, deceptive behavior) must be reported to California Office of Emergency Services (Cal OES).
- **Whistleblower protections:** anonymous reporting channels, anti-retaliation.
- **CalCompute:** establishes a public-cloud-computing consortium framework for safe AI research.
- **Federal deference:** allows state to accept equivalent federal reporting to avoid redundancy.

**Enforcement:** Attorney General may impose civil penalties up to $1M per violation.

### Comparison

| Feature | SB 1047 (vetoed) | SB 53 (enacted) |
|---|---|---|
| Covered systems | >10^26 FLOPS + >$100M cost | >10^26 FLOPS (revenue tier for extra obligations) |
| Safety tests / protocols | Mandated | Not mandated |
| "Kill switch" | Required | Not required |
| Third-party audits | Required | Not required |
| Transparency framework publication | Not explicitly | Yes (large developers) |
| Incident reporting | Yes | Yes |
| Whistleblower protection | Yes | Yes |
| Liability for critical harms | Yes (AG civil action) | Narrower (civil penalty for violations, not for harms) |
| New regulatory body | Board of Frontier Models | No new body (AG enforces) |

SB 53 is a narrower, transparency-and-reporting-focused regime compared with SB 1047's more prescriptive safety-protocol-and-liability regime. It passed where SB 1047 did not because it reduces prescriptive requirements, provides federal deference, and creates no new regulatory body.

### What the SB 1047/SB 53 sequence teaches

- Coalitional politics matters enormously in AI governance. The prescriptive, liability-forward SB 1047 attracted concentrated industry opposition; the transparency-focused SB 53 attracted less and passed.
- Transparency-plus-reporting is the politically available minimum; prescriptive safety-protocol regulation is currently above the political ceiling in the U.S.
- The compute-threshold approach (10^26 FLOPS) has been institutionalized in California law and in several federal proposals, establishing a precedent that is increasingly hard to reverse.
- "Federal deference" clauses are a useful institutional-design feature for sub-federal regulation — they avoid patchwork costs while establishing state-level capacity.

---

## Thematic cluster 3: U.S. federal executive-order sequence

### Biden EO 14110 (October 30, 2023)

- Most comprehensive executive action on AI by any U.S. administration.
- Key provisions:
  - Reporting requirements for models trained above specified compute thresholds.
  - Federal agency guidance on AI in agency operations.
  - Establishment of U.S. AI Safety Institute (AISI) at NIST.
  - Immigration, workforce, civil-rights, privacy, and other domain-specific directives.
  - Collaboration with U.K. AISI on frontier-model evaluation.
- Implementation through 2024 included multiple agency reports, NIST guidelines, and voluntary commitments from major labs.

### Trump rescission and subsequent sequence (2025)

- EO on AI of January 23, 2025 rescinded EO 14110 and directed new "AI Action Plan" to be developed.
- **AI Action Plan (July 2025)** emphasized U.S. AI leadership, reduced regulatory burden, accelerated deployment, and tiered export controls. Established different framing from EO 14110 but retained some reporting measures.
- U.S. AISI's status became uncertain through early 2026; technical evaluation capabilities continue under NIST auspices but with reduced scope.
- Multiple Congressional proposals (bipartisan) have been introduced for federal frontier-AI governance; none had enacted into law as of April 2026.

### Assessment

The U.S. federal trajectory has been volatile and partial. The consistent core across administrations has been NIST's technical-evaluation work; policy direction has shifted substantially. For the project's bounded-governance doctrine, this volatility is itself informative: the U.S. federal executive-branch approach to AI governance illustrates the scope-ratchet's opposite failure mode — instability that makes long-horizon commitment-building difficult.

---

## Thematic cluster 4: NIST AI Risk Management Framework

### Framework structure

The NIST AI RMF 1.0 (January 2023) with Generative AI Profile (July 2024) is a voluntary, non-binding framework organized around four core functions:

1. **Govern** — establish AI risk management culture, policies, and accountability.
2. **Map** — understand AI system context and purpose.
3. **Measure** — assess risks using quantitative and qualitative methods.
4. **Manage** — allocate resources to prioritized risks, treat, transfer, accept, or avoid.

### Significance

Despite being voluntary, the AI RMF has become a de facto standard referenced by:
- EU AI Act Codes of Practice (as one reference for high-risk system obligations).
- California SB 53 transparency obligations (as a reference framework).
- Federal agency AI policies across multiple administrations.
- Industry self-governance programs.

### What NIST AI RMF teaches

Voluntary frameworks can carry significant regulatory weight when they are methodologically rigorous and developed through genuine multistakeholder process. For bounded-governance design, NIST AI RMF is a useful case of *soft-law-as-scaffold*: it does not replace binding regulation but provides the operational substrate on which binding regulation is built.

---

## Representative excerpt — Newsom SB 1047 veto message

> "By focusing only on the most expensive and large-scale models, SB 1047 establishes a regulatory framework that could give the public a false sense of security about controlling this fast-moving technology. Smaller, specialized models may emerge as equally or even more dangerous than the models targeted by SB 1047 — at the potential expense of curtailing the very innovation that fuels advancement in favor of the public good."

This reasoning has been contested by AI-safety researchers (who argue that compute-thresholds are imperfect but tractable, and that refusing to act until a perfect threshold is available is itself a decision with consequences).

---

## Research context

| Claim | Evidence | Context |
|---|---|---|
| EU AI Act is the first comprehensive cross-sectoral AI regulation in a major jurisdiction | **Corroborated** | No comparable measure in U.S., China, U.K., or Japan as of April 2026 |
| SB 53 is substantially narrower than SB 1047 | **Corroborated** | Comparison above based on primary bill text |
| U.S. federal approach has been volatile across administrations | **Corroborated** | EO 14110 → rescission → AI Action Plan sequence |
| Compute-threshold-based tiering is institutionally durable | **Partially corroborated** | EU AI Act (10^25 FLOPS) and SB 53 (10^26 FLOPS) have entrenched the approach; multiple Congressional proposals adopt similar threshold logic |
| Voluntary frameworks (NIST) carry de facto regulatory weight | **Corroborated** | Multiple binding regimes reference NIST AI RMF |

---

## Interpretive notes

- The 2024–2026 regulatory record shows that the Sunstein anti-catastrophe-narrow framework is politically available in practice, not only theoretically. The EU AI Act and SB 53 are roughly anti-catastrophe-narrow regimes: they focus resources on the highest-capability systems, require transparency and incident reporting, but do not freeze AI development or apply uniform restrictions.
- The SB 1047 → SB 53 transition specifically shows the political ceiling on prescriptive AI-safety regulation in the U.S. at present. Projects that ignore this constraint will face SB 1047's fate; projects that work with it (transparency, reporting, federal deference) can pass.
- For the project's bounded-governance doctrine, AI governance is a live instance where the doctrine can be tested. The nine-element design package maps directly: cyclical adjustment (compute-threshold-indexed as capability advances); compensation accounts (incident-reporting-driven adjustment); entrenchment (legislative rather than executive-order); escape clauses (de minimis and open-source exemptions); independent institutions (AI Office, AISI, Cal OES for AI); sunset + review (currently absent, should be added); risk-risk analysis (partly present in NIST RMF); distributional-impact labeling (present in transparency requirements); polycentric (EU + California + federal + voluntary + international).
- Specific project recommendation (for Round 3 or follow-up exchange): the bounded-governance doctrine should include an explicit test case of "how would this apply to frontier AI?" using this digest's material. This would demonstrate the doctrine is not abstract but operational.

---

## Project 2028 mapping

- **Exchange:** [Government Overreach, Ownership as Transition, and the Ratchet Problem](../agent/exchanges/government-overreach-ownership-ratchet-exchange.md). Applied live-case evidence for Sub-debate 7 (fear-based framing — how to do governance under uncertainty without strong-form precaution) and Sub-debate 8 (bounded-governance design — how the design package performs in a live regulatory environment).
- **Problem Map:** [Domain 9 (Technology and AI)](../PROBLEM_MAP.md) — primary evidence base for the domain's governance component. Also engages [Domain 11 (Coordination)](../PROBLEM_MAP.md) on international coordination.
- **Principles:** Directly engages [Principle 4](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible), [Principle 6](../PRINCIPLES.md#6-the-gains-from-automation-should-strengthen-society-not-destabilize-it), [Principle 17](../PRINCIPLES.md#17-collective-power-must-be-exercised-within-principled-constraints).
- **Round 3 use:** Worked example showing how the bounded-governance doctrine applies to a live, empirically rich policy area.

---

## Cross-references

| Related digest | Relationship |
|---|---|
| [AI Existential-Risk Literature (Bengio, Russell, Bostrom)](source-ai-existential-risk-digest.md) | Companion: theoretical and expert-judgment basis for the regulations reviewed here |
| [Sunstein, Laws of Fear](source-sunstein-precautionary-digest.md) | Theoretical foundation for the anti-catastrophe-narrow approach adopted in practice |
| [OECD Fiscal Rules Database](source-oecd-fiscal-rules-digest.md) | Methodological parallel: rule design for bounded interventions |
| [Swiss Debt Brake](source-swiss-debt-brake-digest.md) | Structural parallel: constitutional-level rule + compensation mechanism + independent oversight |
| [Sunset Clauses and Sunsetting Legislation](source-sunset-clauses-digest.md) | Missing-design-element pointer: current AI regulations lack mandatory sunset + review |
