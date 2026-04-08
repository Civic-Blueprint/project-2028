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

| | |
|---|---|
| **Question** | What are the highest-priority gaps in the Problem Map, and how should the map's architecture evolve? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (original version) |
| **Produced** | Democratic process added as a core domain (PM §15, SF §14). Core bottleneck summaries added. Recursive uplift section added. Dependency map updated with recursive loops and network framing. |
| **Status** | Incorporated. Open items: full web/graph model, three-map split, failure vs. stability mechanism distinction. |

---

### 2. [Systems Framework Review — In Light of the Problem Map](iniital-systems-framework-review.md)

| | |
|---|---|
| **Question** | Now that the Problem Map models interdependencies and recursive uplift, how must the Systems Framework evolve to match? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (post-review), [Exchange #1](#1-problem-map-review--priority-follow-up) |
| **Produced** | Consensus that the Framework must evolve from parallel domain analyses into a connected dependency/leverage/uplift system. Proposed proof-of-concept rewrite of institutional capacity domain. Introduced failure-mode modeling. Raised sycophancy concern that led to the Adversarial Review Protocol. |
| **Status** | Active exchange. Framework has been substantially revised (dependency mapping, leverage hypotheses, failure modes, sequencing section added). |

---

### 3. [Post-Systems Framework Revision — Next Steps](post-systems-framework-next-steps.md)

| | |
|---|---|
| **Question** | The analytical architecture is in place. What does the project need next to start earning its claims empirically? |
| **Depends on** | [Exchange #1](#1-problem-map-review--priority-follow-up), [Exchange #2](#2-systems-framework-review--in-light-of-the-problem-map), all core documents |
| **Produced** | Two-track strategy: (1) public website as entry point for outside contributors, (2) computational dependency analysis. Identified the central gap: all claims produced by one human + AI agents from the same context window. Includes adversarial challenge of the two-track strategy itself. |
| **Status** | Active discussion. Track 1 work is underway in [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org). Track 2 not yet started. |

---

### 4. [Principles — Adversarial Review Exchange](principles-adversarial-review.md)

| | |
|---|---|
| **Question** | Do the project's foundational principles withstand structured adversarial challenge? |
| **Depends on** | [Principles](../../PRINCIPLES.md), [Adversarial Review Protocol](../process/adversarial-review-protocol.md) |
| **Produced** | Identified structural gaps (justice, legitimate coercion, prioritization), internal contradictions (Principle 13 vs. substantive commitments), unacknowledged philosophical tradition (liberal-democratic welfare-state). Epistemic status table classifying confidence levels across principle categories. |
| **Status** | Complete exchange. Findings documented; some revisions incorporated into Principles, others deferred. |

---

### 5. [Review Protocol Design Exploration](review-protocol-design-exploration.md)

| | |
|---|---|
| **Question** | Is the adversarial protocol the only kind of structured review the project needs? What other failure modes exist, and what protocols address them? |
| **Depends on** | [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Exchange #4](#4-principles--adversarial-review-exchange) (demonstrated the adversarial protocol works) |
| **Produced** | Seven candidate protocols proposed, then subjected to adversarial self-challenge. Two formalized: [Coherence Audit Protocol](../process/coherence-audit-protocol.md), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md). Five others folded into the adversarial protocol as standing questions. |
| **Status** | Complete exchange. Protocols formalized in `agent/process/`. |

---

### 6. [Proof-of-Usefulness Memo — Housing vs. AI Exchange](proof-of-usefulness-housing-vs-ai.md)

| | |
|---|---|
| **Question** | Should the project's first public artifact focus on housing permitting, AI governance, or bridge the two? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (established the proof-of-usefulness strategy), [Website Phase 1 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_1_BRIEF.md) |
| **Produced** | Decision to write a comparative memo pairing housing permitting with AI governance, demonstrating the framework's cross-domain method. The housing-only draft was superseded. Memo produced in [civicblueprint.org/docs/PROOF_OF_USEFULNESS_MEMO_01.md](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/PROOF_OF_USEFULNESS_MEMO_01.md). |
| **Status** | Active discussion. Comparative memo drafted. The timescale objection raised in Exchange #7 reopens part of this decision. |

---

### 7. [Proof-of-Usefulness Memo — Feedback Timescale Review](proof-of-usefulness-feedback-timescale-review.md)

| | |
|---|---|
| **Question** | The comparative memo optimized for explanatory legibility. Should the project also optimize for learning velocity — and does the current approach learn fast enough to stay relevant as AI timescales compress? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange) (the decision this exchange re-examines), [Proof-of-Usefulness Memo 01](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/PROOF_OF_USEFULNESS_MEMO_01.md) |
| **Produced** | Active. Distinguishes between the memo as public explanation vs. the memo as empirical learning instrument. Proposes separating these functions. Challenges whether housing can generate decision-relevant feedback fast enough. |
| **Status** | Active discussion. |

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
  │                 └─► Track 2: Computational analysis (not started)
  │
  ├─► #4 Principles Adversarial Review
  │     │
  │     └─► #5 Review Protocol Design
  │           │
  │           ├─► Coherence Audit Protocol
  │           └─► Historical Parallel Test Protocol
  │
  Adversarial Review Protocol ◄── (originated from #2, formalized before #4)
```

---

## Cross-repo artifacts

Several exchanges produced or depend on documents in the [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org) repository:

| Exchange | civicblueprint.org artifact |
|---|---|
| #3 (Next Steps) | `docs/WEBSITE_PHASE_1_BRIEF.md` — Phase 1 scope and launch plan |
| #3 (Next Steps) | `docs/HOMEPAGE_COPY_DRAFT.md` — draft homepage copy |
| #6 (Housing vs. AI) | `docs/PROOF_OF_USEFULNESS_MEMO_01.md` — comparative memo |
| #6 (Housing vs. AI) | `docs/PROOF_OF_USEFULNESS_MEMO_01_HOUSING_PERMITTING.md` — superseded housing-only draft |
