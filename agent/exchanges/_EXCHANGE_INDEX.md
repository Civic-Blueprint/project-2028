---
description: Chronological index of structured agent-steward exchanges that shaped the project's direction.
---

# Exchange Index

> **Purpose:** This index helps newcomers navigate the project's exchange history. Each exchange is a structured discussion between AI agents and the project steward that shaped the project's direction. They are listed in the order they occurred, with dependency links so a reader knows what context each exchange assumes.
>
> **Maintenance:** This file is updated whenever a new exchange is created. The [Coherence Audit Protocol](../process/coherence-audit-protocol.md) includes this index in its scope. A Cursor skill (`civic-blueprint-exchange`) enforces index registration at exchange creation time.

---

## How to read this

Each entry below tells you:

- **What question the exchange was trying to answer**
- **What it depends on** — what you should read first to understand the context
- **What it produced** — decisions, document changes, or open questions that fed into later work
- **Status** — whether its recommendations have been incorporated, are still active, or were superseded

If you're new to the project, start with the core documents ([Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md)), then read the exchanges in order. If you're arriving at a specific exchange from a link, use the dependency information to backtrack to the context you need.

---

## Exchanges (chronological)

### 1. [Problem Map Review — Priority Follow-Up](initial-problem-map-review.md)

|  |  |
|---|---|
| **Question** | What are the highest-priority gaps in the Problem Map, and how should the map's architecture evolve? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (original version) |
| **Produced** | Democratic process added as a core domain (PM §15, SF §14). Core bottleneck summaries added. Recursive uplift section added. Dependency map updated with recursive loops and network framing. |
| **Status** | Incorporated. Open items: full web/graph model, three-map split, failure vs. stability mechanism distinction. |

---

### 2. [Systems Framework Review — In Light of the Problem Map](iniital-systems-framework-review.md)

|  |  |
|---|---|
| **Question** | Now that the Problem Map models interdependencies and recursive uplift, how must the Systems Framework evolve to match? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (post-review), [Exchange #1](#1-problem-map-review--priority-follow-up) |
| **Produced** | Consensus that the Framework must evolve from parallel domain analyses into a connected dependency/leverage/uplift system. Proposed proof-of-concept rewrite of institutional capacity domain. Introduced failure-mode modeling. Raised sycophancy concern that led to the Adversarial Review Protocol. |
| **Status** | Active exchange. Framework has been substantially revised (dependency mapping, leverage hypotheses, failure modes, sequencing section added). |

---

### 3. [Post-Systems Framework Revision — Next Steps](post-systems-framework-next-steps.md)

|  |  |
|---|---|
| **Question** | The analytical architecture is in place. What does the project need next to start earning its claims empirically? |
| **Depends on** | [Exchange #1](#1-problem-map-review--priority-follow-up), [Exchange #2](#2-systems-framework-review--in-light-of-the-problem-map), all core documents |
| **Produced** | Two-track strategy: (1) public website as entry point for outside contributors, (2) computational dependency analysis. Identified the central gap: all claims produced by one human + AI agents from the same context window. Includes adversarial challenge of the two-track strategy itself. |
| **Status** | Active discussion. Track 1 work is underway in [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org). Track 2 not yet started. |

---

### 4. [Principles — Adversarial Review Exchange](principles-adversarial-review.md)

|  |  |
|---|---|
| **Question** | Do the project's foundational principles withstand structured adversarial challenge? |
| **Depends on** | [Principles](../../PRINCIPLES.md), [Adversarial Review Protocol](../process/adversarial-review-protocol.md) |
| **Produced** | Identified structural gaps (justice, legitimate coercion, prioritization), internal contradictions (Principle 13 vs. substantive commitments), unacknowledged philosophical tradition (liberal-democratic welfare-state). Epistemic status table classifying confidence levels across principle categories. |
| **Status** | Complete exchange. Findings documented; some revisions incorporated into Principles, others deferred. |

---

### 5. [Review Protocol Design Exploration](review-protocol-design-exploration.md)

|  |  |
|---|---|
| **Question** | Is the adversarial protocol the only kind of structured review the project needs? What other failure modes exist, and what protocols address them? |
| **Depends on** | [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Exchange #4](#4-principles--adversarial-review-exchange) (demonstrated the adversarial protocol works) |
| **Produced** | Seven candidate protocols proposed, then subjected to adversarial self-challenge. Two formalized: [Coherence Audit Protocol](../process/coherence-audit-protocol.md), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md). Five others folded into the adversarial protocol as standing questions. |
| **Status** | Complete exchange. Protocols formalized in `agent/process/`. |

---

### 6. [Proof-of-Usefulness Memo — Housing vs. AI Exchange](proof-of-usefulness-housing-vs-ai.md)

|  |  |
|---|---|
| **Question** | Should the project's first public artifact focus on housing permitting, AI governance, or bridge the two? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (established the proof-of-usefulness strategy), [Website Phase 1 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_1_BRIEF.md) |
| **Produced** | Decision to write a comparative memo pairing housing permitting with AI governance, demonstrating the framework's cross-domain method. The housing-only draft was superseded. Canonical memo now maintained in [memos/proof-of-usefulness-memo-01.md](../../memos/proof-of-usefulness-memo-01.md). |
| **Status** | Active discussion. Comparative memo drafted. The timescale objection raised in Exchange #7 reopens part of this decision. |

---

### 7. [Proof-of-Usefulness Memo — Feedback Timescale Review](proof-of-usefulness-feedback-timescale-review.md)

|  |  |
|---|---|
| **Question** | The comparative memo optimized for explanatory legibility. Should the project also optimize for learning velocity — and does the current approach learn fast enough to stay relevant as AI timescales compress? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange) (the decision this exchange re-examines), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Synthesized. Six recommendations produced: (1) ship Memo 01 (done), (2) launch structured practitioner critique, (3) formally separate three kinds of "first," (4) design a fast-feedback validation case, (5) commit to transparent evidence integration, (6) revise the internal description of recursive uplift. Three-layer decomposition of recursive uplift (execution, trust, sequence) established. Key finding: the visible-competence-to-trust cascade has no direct empirical support. Full recommendations tracked in [Roadmap](../../ROADMAP.md). |
| **Status** | Synthesized. Recommendations adopted by steward. Recommendation 1 complete. Remaining recommendations tracked in [Roadmap](../../ROADMAP.md). |

---

### 8. [Voice Synthesis, Accessibility, and Engagement — Feature Exploration](voice-synthesis-accessibility-engagement-exchange.md)

|  |  |
|---|---|
| **Question** | Are synthesized voice narration, multi-level text presentation, and more intentional communication design substantive engagement and accessibility features — and does communication itself function as a hidden cross-cutting variable in reform capacity — or is this cosmetic work that drains resources from higher-priority needs? |
| **Depends on** | [Principles](../../PRINCIPLES.md) (§1 dignity, §2 essential needs, §3 AI augmenting agency, §4 accountable power), [Problem Map](../../PROBLEM_MAP.md) (§3 information ecosystems), [Exchange #3](#3-post-systems-framework-revision--next-steps) (website as public entry point), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (learning velocity and fast-feedback validation) |
| **Produced** | Six rounds plus steward synthesis. Separated accessibility (mandatory) from voice features (deferred). Adopted a falsifiable legibility hypothesis. Adopted "Engagement is part of the reform chain; manipulation is engagement that breaks faith with the reader" as a working tension statement. Adopted a transparency-about-prosody design principle. Deferred the communication stack, plain-language companions, and voice features pending real user data and practitioner feedback. Declined treating voice A/B testing as framework validation per Exchange #7. Identified a candidate unnamed tension (truth-preserving mobilization vs. attention-capturing persuasion) for future consideration. No changes to Roadmap dependency ordering. |
| **Status** | **Synthesized.** Steward decisions recorded. No open action items; adopted formulations are carried in the exchange for future reference. |

---

### 9. [Debt Legitimacy and Odious Debt — Exchange](debt-legitimacy-odious-debt-exchange.md)

|  |  |
|---|---|
| **Question** | Should the project's analysis explicitly name debt legitimacy and odious-debt doctrine as part of its account of institutional capture, and if so, where does that material belong? |
| **Depends on** | [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (created the website-feedback lane), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md) |
| **Produced** | Exchange opened. Initial classification questions captured: example vs. mechanism, domain placement, competence vs. repudiation, and scope discipline for sovereign-debt analysis. |
| **Status** | Active discussion. |

---

### 10. [Housing Financialization as Upstream Capture — Exchange](housing-financialization-upstream-capture-exchange.md)

|  |  |
|---|---|
| **Question** | Should the framework explicitly treat housing financialization as a distinct upstream-capture mechanism alongside housing permitting and zoning, or widen the existing housing analysis without a separately named frame? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Exchange opened. Initial questions captured around mechanism naming, balance between permitting and finance, metro vs. national claims, and whether the current public memo needs revision or a companion artifact. |
| **Status** | Active discussion. |

---

### 11. [AI Commonwealth vs. AI Governance — Exchange](ai-commonwealth-vs-governance-exchange.md)

|  |  |
|---|---|
| **Question** | Should the framework explicitly shift from an "AI governance" frame to an "AI commonwealth" frame centered on ownership, access, and public infrastructure, or preserve governance as the primary frame and incorporate these ideas more narrowly? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Exchange opened. Initial questions captured around governance vs. commonwealth framing, timeline urgency, what counts as commonwealth infrastructure in AI, and whether existing public artifacts need reframing. |
| **Status** | Active discussion. |

---

### 12. [Memo 01 Housing Claims — Historical Parallel Test Exchange](memo-01-housing-parallel-test-exchange.md)

|  |  |
|---|---|
| **Question** | Does the published housing-domain practitioner and research literature confirm, challenge, or complicate Memo 01's core structural claims about institutional capacity, recursive uplift, infrastructure coordination, and reform-as-extraction trust failure? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md), [Roadmap](../../ROADMAP.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | First application of the Historical Parallel Test Protocol. Four structural claims from Memo 01 tested against published housing literature. Claim 2 (recursive uplift) identified as the project's most vulnerable housing claim — no published confirmation of the positive cascade. Claim 3 (infrastructure coordination) identified as the strongest. Sharpened practitioner prompt questions proposed for Recommendation 2. |
| **Status** | Active discussion. |

---

### 13. [Autonomous Proposal Generation — Agent Stress Test](autonomous-proposal-generation-stress-test.md)

|  |  |
|---|---|
| **Question** | Can AI agents, working autonomously across multiple models and protocols, generate concrete proposals that bridge the gap between the project's analytical framework and real-world reform — and what does the output reveal about the framework's generativity, its gaps, and the structural constraints on translating diagnosis into action? |
| **Depends on** | All core documents ([Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md)), all three process protocols ([Adversarial Review](../process/adversarial-review-protocol.md), [Coherence Audit](../process/coherence-audit-protocol.md), [Historical Parallel Test](../process/historical-parallel-test-protocol.md)), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (recursive uplift decomposition), [Exchange #12](#12-memo-01-housing-claims--historical-parallel-test-exchange) (housing evidence) |
| **Produced** | 135 proposals (112 unique after de-duplication) across all 15 Problem Map domains. Adversarial review from 4 perspectives identified political durability, displacement protection, and coalition math as critical gaps. Historical parallel testing on 4 clusters (institutional capacity, housing, democracy, capital). Four integrated reform sequences. Epistemic status assessment. Key finding: the framework is generative but political feasibility — not analytical quality — is the binding constraint. |
| **Status** | Active exchange. No steward input yet. Proposals are AI-generated hypotheses, not endorsed positions. All proposals individually cataloged in [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) for steward review. |

---

### 14. [Permitting Stack Recursive Uplift — Exchange](permitting-stack-recursive-uplift-exchange.md)

|  |  |
|---|---|
| **Question** | If `P-004` / `P-107` is the strongest candidate for initiating a recursive-uplift sequence, what would it take to turn the permitting-stack idea from an AI-generated proposal into a serious project hypothesis that is scoped clearly enough to analyze, critique, prototype, or eventually test in the real world? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (empirical-validation need), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (fast-feedback and recursive-uplift decomposition), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (proposal generation and uplift-chain ranking), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Frames `P-004` / `P-107` as the first candidate proposal for deeper development. Captures the initial case for why the permitting stack is the strongest recursive-uplift starting point, identifies core tensions (standardization vs. local variation, software vs. institutional reform, execution vs. trust claims), and defines starter questions for the next round. |
| **Status** | Active discussion. |

---

### 15. [Steward Feedback Proposal Iteration — Exchange](steward-feedback-proposal-iteration-exchange.md)

|  |  |
|---|---|
| **Question** | When steward feedback is added to a subset of proposals in the catalog, does that human input materially change what a new proposal-development round produces — in specificity, originality, prioritization, coalition awareness, or recursive-uplift logic? |
| **Depends on** | [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (argument for faster, iterative learning), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (original proposal generation), [Exchange #14](#14-permitting-stack-recursive-uplift--exchange) (single-proposal deep dive on `P-004` / `P-107`), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Frames a second experiment: steward-in-the-loop proposal iteration using annotations on 35 proposals from the catalog. Records the experiment's rationale, its relationship to the focused permitting-stack exchange, the likely output types, and the key methodological tensions. At exchange opening, the exact 35 annotated proposals are not yet visible in the saved catalog state available to the agent and remain to be incorporated in the next round. |
| **Status** | Active discussion. |

---

### 16. [Starting Proposal Comparative Review — P-004/P-107 vs. P-053](starting-proposal-comparative-review.md)

|  |  |
|---|---|
| **Question** | The project needs to commit development effort to a starting proposal. Between the Open-Source Permitting Stack (`P-004` / `P-107`) and Federal Skills-First Hiring (`P-053`), which better serves the project's goals of testing recursive uplift, producing visible results, building credibility, and generating empirical learning? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (empirical-validation need), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (fast-feedback and recursive-uplift decomposition), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (proposal generation and uplift-chain ranking), [Exchange #14](#14-permitting-stack-recursive-uplift--exchange) (initial P-004/P-107 development), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Structured comparative framework across six dimensions (recursive uplift potential, learning velocity, visibility, political durability, project credibility, informative failure). Identifies open questions including whether the comparison is actually a sequencing question rather than either/or. |
| **Status** | Active discussion. |

---

### 17. [First Practitioner Critique and AI Content Provenance — Exchange](first-practitioner-critique-ai-provenance-exchange.md)

|  |  |
|---|---|
| **Question** | What does the project's first practitioner feedback reveal about memo credibility, AI-content legibility, and orientation design — and how should the project operationalize content provenance standards in response? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange) (created the memo artifact), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (Recommendation 2 practitioner-critique lane), [Exchange #8](#8-voice-synthesis-accessibility-and-engagement--feature-exploration) (communication and engagement design), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) (`P-020`) |
| **Produced** | Five rounds (three constructive, one adversarial, one coherence audit) plus steward interstitial. Adopted a four-level content provenance standard. Established that provenance labeling is necessary hygiene but not a trust strategy — trust requires demonstrated performance (Principle 9, PM §13). Identified effort calibration and AI-sensitivity as compounding outreach barriers. Concluded outreach-embedded relational disclosure matters more than website labels. Reweighted the three-layer critique model with entry trust as highest-strategic-weight layer. Downgraded P-020 dog-fooding claims from "validation" to "illustration." Produced a prioritized next-steps list: redesign outreach ask, track entry-trust clearance rate, review memo weak claims (Exchanges #7/#12), keep provenance as infrastructure, accelerate Recommendation 4. |
| **Status** | **Synthesized.** Steward decisions recorded. Implementation tracked in a separate plan. |

---

## Dependency graph (visual summary)

```
Core Documents (Principles, Problem Map, Systems Framework)
  │
  ├─► #1 Problem Map Review
  │     │
  │     └─► #2 Systems Framework Review
  │           │
  │           └─► #3 Post-SF Next Steps ──────────────────┐
  │                 │                                      │
  │                 ├─► #6 Housing vs. AI ─► #7 Timescale  │
  │                 │        │                              │
  │                 │        └─► Memo 01 (civicblueprint.org)
  │                 │
  │                 ├─► #8 Voice Synthesis & Accessibility ◄── #7 (fast-feedback)
  │                 │
  │                 └─► Track 2: Computational analysis (not started)
  │
  ├─► #4 Principles Adversarial Review
  │     │
  │     └─► #5 Review Protocol Design
  │           │
  │           ├─► Coherence Audit Protocol ─────────────────────┐
  │           ├─► Historical Parallel Test Protocol ─► #12      │
  │           └─► Adversarial Review Protocol ──────────────────┤
  │                                                             │
  ├─► Roadmap / website-submission lane (via #7 recommendations)│
  │     ├─► #9 Debt Legitimacy & Odious Debt                   │
  │     ├─► #10 Housing Financialization ◄── #6 / Memo 01      │
  │     ├─► #11 AI Commonwealth vs. Governance ◄── #6 / Memo 01│
  │     └─► #17 Practitioner Critique & AI Provenance          │
  │           ◄── #6 + #7 + #8 + P-020 + website memo entry    │
  │                                                             │
  ├─► #12 Memo 01 Housing Parallel Test ◄── #6 / #7 / HPTP    │
  │                                                             │
  └─► #13 Autonomous Proposal Generation Stress Test ◄─────────┐
        ◄── All core docs + all 3 protocols + #7 + #12         │
        (30 rounds, 112 unique proposals, no steward input)    │
                                                                │
        ├─► #14 Permitting Stack Recursive Uplift ◄─────────────┐
        │     ◄── #3 + #7 + #13 + Proposal Catalog              │
        │     (starting from P-004 / P-107 as first candidate)  │
        │     │                                                  │
        │     └─► #16 Starting Proposal Comparative Review       │
        │           ◄── #3 + #7 + #13 + #14 + Proposal Catalog  │
        │           (P-004/P-107 vs. P-053 head-to-head)        │
        │                                                        │
        └─► #15 Steward Feedback Proposal Iteration ◄────────────┘
              ◄── #7 + #13 + #14 + Proposal Catalog
              (second experiment using steward annotations)
```

---

## Cross-repo artifacts

Several exchanges produced or depend on documents in the [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org) repository:

| Exchange | civicblueprint.org artifact |
|---|---|
| #3 (Next Steps) | `docs/WEBSITE_PHASE_1_BRIEF.md` — Phase 1 scope and launch plan |
| #3 (Next Steps) | `docs/HOMEPAGE_COPY_DRAFT.md` — draft homepage copy |
| #6 (Housing vs. AI) | `memos/proof-of-usefulness-memo-01.md` (project-2028) and `website/src/app/docs/[...slug]/page.tsx` (civicblueprint.org renderer) — comparative memo and public docs surface |
| #6 (Housing vs. AI) | `docs/PROOF_OF_USEFULNESS_MEMO_01_HOUSING_PERMITTING.md` — superseded housing-only draft |
| #10 (Housing Financialization) | `memos/proof-of-usefulness-memo-01.md` — public memo whose housing framing this exchange reopens |
| #11 (AI Commonwealth vs. Governance) | `memos/proof-of-usefulness-memo-01.md` — public memo whose AI framing this exchange sharpens |
| #12 (Housing Parallel Test) | `memos/proof-of-usefulness-memo-01.md` — public memo whose housing claims this exchange tests |
| #17 (Practitioner Critique & AI Provenance) | `website/src/components/Hero.tsx`, `website/src/components/MemoFeature.tsx`, `website/src/app/docs/[...slug]/page.tsx` — website orientation and provenance legibility surfaces targeted by this exchange |
