---
description: Recommended next steps drawn from exchange findings and steward decisions — the single source for what's next.
---

# Project 2028 — Roadmap

> **Purpose:** This document tracks the project's recommended next steps, drawn from exchange findings and steward decisions. It is the single source of truth for "what's next" so that neither the steward nor agents lose track of outstanding work.
>
> **Source:** Recommendations below originate from [Exchange #7 — Feedback Timescale Review](agent/exchanges/proof-of-usefulness-feedback-timescale-review.md), which produced six concrete recommendations after four rounds (two adversarial, two constructive).
>
> **Last updated:** April 2026

---

## Active Recommendations

### Recommendation 1: Ship Memo 01 without delay ✅

**Status: Complete.**

Ship the comparative proof-of-usefulness memo as the public-facing artifact. Add a short epistemic-status section naming recursive uplift as plausible but empirically unvalidated.

- Memo 01 is published and live.
- Epistemic-status language has been incorporated.
- Early organic feedback is already arriving (first issue submitted via the website form).

---

### Recommendation 2: Launch structured practitioner critique

**Status: In progress.**

Design and launch a structured review process targeting domain practitioners.

**Current implementation state (April 2026):**

- Outreach is underway; 8 practitioners have been contacted.
- The 4-6 week response collection window is now open from initial outreach.
- First practitioner response has now been received and logged in [First Practitioner Critique and AI Content Provenance — Exchange](agent/exchanges/first-practitioner-critique-ai-provenance-exchange.md).
- Early signal from that response: direct memo entry without orientation caused confusion, and AI-generated writing texture triggered a credibility filter before substantive critique.

**What this means:**

- **Recruit 8-12 reviewers** across housing, AI governance, public administration, and community organizing.
- **Specifically recruit** at least 2 practitioners who have run bounded administrative reforms and measured public response.
- **Write a structured prompt** asking:
  - **Preamble adjustment (new):** briefly state what the project is, how AI is used (generated + curated/synthesized), and what kind of critique is being requested.
  - (a) Does this framework name bottlenecks you recognize from practice?
  - (b) What does it miss or get wrong?
  - (c) Where does the cross-domain comparison help and where does it feel forced?
  - (d) Would you use or recommend this analysis?
- **Collection window:** 4-6 weeks from when the prompt is sent.
- **Output:** Synthesize findings in a short public note.

**Timeline guidance:** The "4-6 weeks" is a collection window for reviewer responses, not a full-time effort by the steward. The steward's work is front-loaded: identify reviewers, write the prompt, send it out. That design + recruitment phase can happen within a few weeks alongside other project work.

**Relationship to organic feedback:** Friends, colleagues, and issue submissions via the website form provide early signal on whether the memo lands. The structured practitioner critique is a different thing: it tests whether the framework survives expert scrutiny from people with relevant operational experience.

**Operational boundary (intake rule):**

- Any issue labeled `website-submission` is treated as **organic feedback** by default.
- Structured practitioner critique includes only invited or intentionally recruited reviewers using the Recommendation 2 prompt in the defined collection window.
- Unsolicited public issues do not become structured-critique evidence unless they are explicitly incorporated into that separate process.

**Current organic feedback triage (April 2026):**

- [#8 Historical case](https://github.com/Civic-Blueprint/project-2028/issues/8): initial disposition `needs-steward-discussion` (candidate for debt/fiscal-capture or legitimacy/commonwealth synthesis). Exchange opened: [Debt Legitimacy and Odious Debt](agent/exchanges/debt-legitimacy-odious-debt-exchange.md).
- [#9 Missing perspective](https://github.com/Civic-Blueprint/project-2028/issues/9): initial disposition `needs-steward-discussion` (housing financialization as an upstream-capture mechanism). Exchange opened: [Housing Financialization as Upstream Capture](agent/exchanges/housing-financialization-upstream-capture-exchange.md).
- [#10 Missing perspective](https://github.com/Civic-Blueprint/project-2028/issues/10): initial disposition `needs-steward-discussion` (AI commonwealth framing alongside AI governance framing). Exchange opened: [AI Commonwealth vs. AI Governance](agent/exchanges/ai-commonwealth-vs-governance-exchange.md).

These are organic submissions. They are inputs to steward synthesis and roadmap refinement, not substitutes for structured practitioner critique.

---

### Recommendation 3: Formally separate the three kinds of "first"

**Status: Not yet started.**

The project has been conflating three different questions. This roadmap now makes the separation explicit:

| Question | Current answer | Status |
|---|---|---|
| What is the first public orientation artifact? | Comparative Memo 01 (housing + AI) | **Decided. Shipped.** |
| What is the first fast-feedback learning mechanism? | Structured practitioner critique of Memo 01 | **Decided. Launched.** (See Recommendation 2) |
| What is the first empirical validation case? | To be designed. Criteria established, domain not yet selected. | **Open.** (See Recommendation 4) |

---

### Recommendation 4: Design a fast-feedback validation case

**Status: In progress. Dependency satisfied: Recommendation 2 is underway.**

Design (but do not rush) a bounded reform case where the process is participatory and visible, the execution improvement is measurable, and behavioral trust proxies can be tracked alongside throughput metrics.

**Revised selection criteria** (incorporating all four exchange rounds):

1. Bounded institutional actor
2. Measurable public outputs within roughly a year
3. Plausible connection to **behavioral** trust indicators (uptake, re-engagement, compliance, participation) — not just throughput
4. A reform process that is itself **participatory, visible, and co-designed** with affected communities
5. Enough structural similarity to governance questions that the result teaches something about institutional capacity, not just process improvement
6. Enough public salience that the result matters beyond internal learning

**Candidate search space** (not yet evaluated against criteria):

- Benefits-access or redetermination systems
- Public records or FOIA-style turnaround
- Permitting sub-processes with short-cycle metrics
- Licensing, inspection, or code-enforcement workflows
- Procurement or grant-disbursement processes

**Current implementation state (April 2026):**

- Initial proposal generation completed in [Exchange #13](agent/exchanges/autonomous-proposal-generation-stress-test.md).
- A full catalog of proposals is now available at [Proposal Catalog](proposals/PROPOSAL_CATALOG.md).
- A new focused exchange has been opened for the strongest initial candidate: [Permitting Stack Recursive Uplift — Exchange](agent/exchanges/permitting-stack-recursive-uplift-exchange.md), centered on `P-004` / `P-107`.

**Next step:** Use the permitting-stack exchange to test whether this is the right bounded validation path or whether another candidate domain should be preferred.

---

### Recommendation 5: Commit to transparent evidence integration in advance

**Status: Not yet started.**

Before any evidence arrives, publish a brief note stating:

- What kinds of evidence each track produces
- That practitioner critique tests analytical usefulness, not causal claims
- That a fast-feedback case produces directional evidence on execution and behavioral trust proxies, not proof of recursive uplift
- That ambiguous results will be reported as ambiguous, with multiple interpretations presented
- That the trust-to-sequence layer (Layer 3) is inherently long-cycle and the project will not claim short-cycle evidence for it

This prevents the misuse risk identified in the exchange: ambiguous results being retroactively cited as partial validation.

---

### Recommendation 6: Revise the internal description of recursive uplift

**Status: Not yet started.**

The exchange's most important finding is that recursive uplift, as currently formulated, bundles claims that operate on different timescales and under different evidentiary conditions.

**The three-layer decomposition:**

| Layer | Claim | Testable on short timelines? |
|---|---|---|
| **Execution** | Institutions can deliver visibly better outcomes in a bounded domain | Yes |
| **Trust** | Visible performance shifts behavioral trust indicators (uptake, re-engagement, compliance, participation) | Partially — behavioral proxies are observable but attribution is contested |
| **Sequence** | Trust and legitimacy gains make subsequent reforms more feasible | No — inherently long-cycle, politically mediated |

**The hardest finding:** The visible-competence-to-trust cascade is the framework's most distinctive claim, and it has no direct empirical support. That is not a weakness to hide. It is a gap to name publicly and then work to close.

This decomposition and the honest assessment of which layers are currently supported should appear in the Systems Framework or a dedicated theory-specification note.

---

### Proposal Catalog (from Exchange #13)

**Status: Complete. Awaiting steward triage.**

Exchange #13 (Autonomous Proposal Generation — Agent Stress Test) produced 135 original proposals across all 15 Problem Map domains. These have been cataloged individually in [proposals/PROPOSAL_CATALOG.md](proposals/PROPOSAL_CATALOG.md) for steward review, feedback, and further brainstorming.

**Next steps:**

- Steward triage pass: scan proposals, mark interesting/wrong/debatable in Priority field
- Priority ranking for proposals marked interesting
- Coalition analysis for top-priority proposals
- Open follow-up exchanges for proposals worth developing further
- Steward-in-the-loop iteration experiment opened in [Exchange #15](agent/exchanges/steward-feedback-proposal-iteration-exchange.md)

---

## Key context from the exchange

The exchange established several findings that should inform all future work:

- **Memo 01 is a public orientation artifact, not an empirical validation plan.** Do not ask it to prove recursive uplift.
- **Bounded administrative improvements alone do not reliably produce trust changes on short timelines.** The administrative-burden literature is consistent on this point.
- **Participatory, visible reform processes have stronger evidence for trust effects than insular workflow optimization.** How the improvement happens matters more for trust than what improves.
- **The project should publicly name the evidential limits of recursive uplift.** This honesty is a strength, not a weakness.

---

## Dependency ordering

```
Recommendation 1 (Ship Memo 01) ✅ Complete
    │
    ├─► Recommendation 2 (Practitioner critique) ← IN PROGRESS
    │     │
    │     └─► Recommendation 5 (Evidence integration note)
    │
    ├─► Recommendation 3 (Separate the three "firsts") ← This roadmap satisfies it
    │
    ├─► Recommendation 4 (Fast-feedback validation case) ← UNBLOCKED (Rec 2 underway)
    │
    └─► Recommendation 6 (Revise recursive uplift description) ← Can proceed in parallel
```
