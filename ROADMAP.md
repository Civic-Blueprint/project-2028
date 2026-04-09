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

**Status: Not yet started.**

Design and launch a structured review process targeting domain practitioners.

**What this means:**

- **Recruit 8-12 reviewers** across housing, AI governance, public administration, and community organizing.
- **Specifically recruit** at least 2 practitioners who have run bounded administrative reforms and measured public response.
- **Write a structured prompt** asking:
  - (a) Does this framework name bottlenecks you recognize from practice?
  - (b) What does it miss or get wrong?
  - (c) Where does the cross-domain comparison help and where does it feel forced?
  - (d) Would you use or recommend this analysis?
- **Collection window:** 4-6 weeks from when the prompt is sent.
- **Output:** Synthesize findings in a short public note.

**Timeline guidance:** The "4-6 weeks" is a collection window for reviewer responses, not a full-time effort by the steward. The steward's work is front-loaded: identify reviewers, write the prompt, send it out. That design + recruitment phase can happen within a few weeks alongside other project work.

**Relationship to organic feedback:** Friends, colleagues, and issue submissions via the website form provide early signal on whether the memo lands. The structured practitioner critique is a different thing: it tests whether the framework survives expert scrutiny from people with relevant operational experience.

---

### Recommendation 3: Formally separate the three kinds of "first"

**Status: Not yet started.**

The project has been conflating three different questions. This roadmap now makes the separation explicit:

| Question | Current answer | Status |
|---|---|---|
| What is the first public orientation artifact? | Comparative Memo 01 (housing + AI) | **Decided. Shipped.** |
| What is the first fast-feedback learning mechanism? | Structured practitioner critique of Memo 01 | **Decided. Not yet launched.** (See Recommendation 2) |
| What is the first empirical validation case? | To be designed. Criteria established, domain not yet selected. | **Open.** (See Recommendation 4) |

---

### Recommendation 4: Design a fast-feedback validation case

**Status: Not yet started. Depends on Recommendation 2 being underway first.**

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

**Next step:** Open a new exchange to evaluate 2-3 candidate domains against these criteria.

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
    ├─► Recommendation 2 (Practitioner critique) ← START HERE
    │     │
    │     └─► Recommendation 5 (Evidence integration note)
    │
    ├─► Recommendation 3 (Separate the three "firsts") ← This roadmap satisfies it
    │
    ├─► Recommendation 4 (Fast-feedback validation case) ← After Rec 2 is underway
    │
    └─► Recommendation 6 (Revise recursive uplift description) ← Can proceed in parallel
```
