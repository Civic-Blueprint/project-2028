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
| --- | --- |
| **Question** | What are the highest-priority gaps in the Problem Map, and how should the map's architecture evolve? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (original version) |
| **Produced** | Democratic process added as a core domain (PM §15, SF §14). Core bottleneck summaries added. Recursive uplift section added. Dependency map updated with recursive loops and network framing. |
| **Status** | Incorporated. Open items: full web/graph model, three-map split, failure vs. stability mechanism distinction. |

---

### 2. [Systems Framework Review — In Light of the Problem Map](iniital-systems-framework-review.md)

|  |  |
| --- | --- |
| **Question** | Now that the Problem Map models interdependencies and recursive uplift, how must the Systems Framework evolve to match? |
| **Depends on** | [Problem Map](../../PROBLEM_MAP.md) (post-review), [Exchange #1](#1-problem-map-review--priority-follow-up) |
| **Produced** | Consensus that the Framework must evolve from parallel domain analyses into a connected dependency/leverage/uplift system. Proposed proof-of-concept rewrite of institutional capacity domain. Introduced failure-mode modeling. Raised sycophancy concern that led to the Adversarial Review Protocol. |
| **Status** | Active exchange. Framework has been substantially revised (dependency mapping, leverage hypotheses, failure modes, sequencing section added). |

---

### 3. [Post-Systems Framework Revision — Next Steps](post-systems-framework-next-steps.md)

|  |  |
| --- | --- |
| **Question** | The analytical architecture is in place. What does the project need next to start earning its claims empirically? |
| **Depends on** | [Exchange #1](#1-problem-map-review--priority-follow-up), [Exchange #2](#2-systems-framework-review--in-light-of-the-problem-map), all core documents |
| **Produced** | Two-track strategy: (1) public website as entry point for outside contributors, (2) computational dependency analysis. Identified the central gap: all claims produced by one human + AI agents from the same context window. Includes adversarial challenge of the two-track strategy itself. |
| **Status** | Synthesized. The two-track strategy was adopted: Track 1 (public website) is live in [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org); Track 2 (computational dependency analysis) is carried as a [Roadmap](../../ROADMAP.md) item rather than a live exchange thread. Disposed June 9, 2026 per Roadmap TODO #5a. |

---

### 4. [Principles — Adversarial Review Exchange](principles-adversarial-review.md)

|  |  |
| --- | --- |
| **Question** | Do the project's foundational principles withstand structured adversarial challenge? |
| **Depends on** | [Principles](../../PRINCIPLES.md), [Adversarial Review Protocol](../process/adversarial-review-protocol.md) |
| **Produced** | Identified structural gaps (justice, legitimate coercion, prioritization), internal contradictions (Principle 13 vs. substantive commitments), unacknowledged philosophical tradition (liberal-democratic welfare-state). Epistemic status table classifying confidence levels across principle categories. |
| **Status** | Complete exchange. Findings documented; some revisions incorporated into Principles, others deferred. |

---

### 5. [Review Protocol Design Exploration](review-protocol-design-exploration.md)

|  |  |
| --- | --- |
| **Question** | Is the adversarial protocol the only kind of structured review the project needs? What other failure modes exist, and what protocols address them? |
| **Depends on** | [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Exchange #4](#4-principles--adversarial-review-exchange) (demonstrated the adversarial protocol works) |
| **Produced** | Seven candidate protocols proposed, then subjected to adversarial self-challenge. Two formalized: [Coherence Audit Protocol](../process/coherence-audit-protocol.md), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md). Five others folded into the adversarial protocol as standing questions. |
| **Status** | Complete exchange. Protocols formalized in `agent/process/`. |

---

### 6. [Proof-of-Usefulness Memo — Housing vs. AI Exchange](proof-of-usefulness-housing-vs-ai.md)

|  |  |
| --- | --- |
| **Question** | Should the project's first public artifact focus on housing permitting, AI governance, or bridge the two? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (established the proof-of-usefulness strategy), [Website Phase 1 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_1_BRIEF.md) |
| **Produced** | Decision to write a comparative memo pairing housing permitting with AI governance, demonstrating the framework's cross-domain method. The housing-only draft was superseded. Canonical memo now maintained in [memos/proof-of-usefulness-memo-01.md](../../memos/proof-of-usefulness-memo-01.md). |
| **Status** | Superseded by [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review). The comparative memo shipped as [Memo 01](../../memos/proof-of-usefulness-memo-01.md); the live thread (timescale objection) moved to Exchange #7. Disposed June 9, 2026 per Roadmap TODO #5a. |

---

### 7. [Proof-of-Usefulness Memo — Feedback Timescale Review](proof-of-usefulness-feedback-timescale-review.md)

|  |  |
| --- | --- |
| **Question** | The comparative memo optimized for explanatory legibility. Should the project also optimize for learning velocity — and does the current approach learn fast enough to stay relevant as AI timescales compress? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange) (the decision this exchange re-examines), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Synthesized. Six recommendations produced: (1) ship Memo 01 (done), (2) launch structured practitioner critique, (3) formally separate three kinds of "first," (4) design a fast-feedback validation case, (5) commit to transparent evidence integration, (6) revise the internal description of recursive uplift. Three-layer decomposition of recursive uplift (execution, trust, sequence) established. Key finding: the visible-competence-to-trust cascade has no direct empirical support. Full recommendations tracked in [Roadmap](../../ROADMAP.md). |
| **Status** | Synthesized. Recommendations adopted by steward. Recommendation 1 complete. Remaining recommendations tracked in [Roadmap](../../ROADMAP.md). |

---

### 8. [Voice Synthesis, Accessibility, and Engagement — Feature Exploration](voice-synthesis-accessibility-engagement-exchange.md)

|  |  |
| --- | --- |
| **Question** | Are synthesized voice narration, multi-level text presentation, and more intentional communication design substantive engagement and accessibility features — and does communication itself function as a hidden cross-cutting variable in reform capacity — or is this cosmetic work that drains resources from higher-priority needs? |
| **Depends on** | [Principles](../../PRINCIPLES.md) (§1 dignity, §2 essential needs, §3 AI augmenting agency, §4 accountable power), [Problem Map](../../PROBLEM_MAP.md) (§3 information ecosystems), [Exchange #3](#3-post-systems-framework-revision--next-steps) (website as public entry point), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (learning velocity and fast-feedback validation) |
| **Produced** | Six rounds plus steward synthesis. Separated accessibility (mandatory) from voice features (deferred). Adopted a falsifiable legibility hypothesis. Adopted "Engagement is part of the reform chain; manipulation is engagement that breaks faith with the reader" as a working tension statement. Adopted a transparency-about-prosody design principle. Deferred the communication stack, plain-language companions, and voice features pending real user data and practitioner feedback. Declined treating voice A/B testing as framework validation per [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review). Identified a candidate unnamed tension (truth-preserving mobilization vs. attention-capturing persuasion) for future consideration. No changes to Roadmap dependency ordering. |
| **Status** | **Synthesized.** Steward decisions recorded. No open action items; adopted formulations are carried in the exchange for future reference. |

---

### 9. [Debt Legitimacy and Odious Debt — Exchange](debt-legitimacy-odious-debt-exchange.md)

|  |  |
| --- | --- |
| **Question** | Should the project's analysis explicitly name debt legitimacy and odious-debt doctrine as part of its account of institutional capture, and if so, where does that material belong? |
| **Depends on** | [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (created the website-feedback lane), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md) |
| **Produced** | Exchange opened. Initial classification questions captured: example vs. mechanism, domain placement, competence vs. repudiation, and scope discipline for sovereign-debt analysis. |
| **Status** | Synthesized (folded June 9, 2026). Disposition: folded into the capital-allocation / ownership workstream rather than advanced standalone — the odious-debt / illegitimate-obligation mechanism is a [Problem Map Domain 2](../../PROBLEM_MAP.md#2-money-credit-and-capital-allocation-steer-the-economy-in-ways-most-people-cannot-see-or-influence) capture pattern (minimum claim: audit / restructure / prevent over repudiation), already feeding Exchange #21 and to be carried by the F2 Domain 2 work in [Exchange #28](#28-ownership-taxonomy--systems-framework--exchange-f2). No standalone rounds planned. |

---

### 10. [Housing Financialization as Upstream Capture — Exchange](housing-financialization-upstream-capture-exchange.md)

|  |  |
| --- | --- |
| **Question** | Should the framework explicitly treat housing financialization as a distinct upstream-capture mechanism alongside housing permitting and zoning, or widen the existing housing analysis without a separately named frame? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Exchange opened, then **Round 1 (June 9, 2026 — same-lineage agent synthesis).** Resolves the framing as *widen-and-name*: housing capture has a **supply face** (permitting/zoning, already canonical) and an **asset face** (financialization). Institutional SFR concentration is promoted to a canonical structural mechanism (an ownership-form shift, cross-linked to [Exchange #28](#28-ownership-taxonomy--systems-framework--exchange-f2)); securitization / zero-rate / rate-trap are kept as supporting macro-conditions. Falsifiable claim set E10-C1…C4 with falsification tests; narrowest-revision recommendation (one paragraph + a Memo 01 companion, not a rewrite). Concrete output: permitting-stack pilots ([Exchange #16](#16-starting-proposal-comparative-review--p-004p-107-vs-p-053)) should be sited where supply is the binding constraint. |
| **Status** | Active; Round 1 complete; Rounds 2–N reserved (adversarial Round 2 reserved for an independent lineage). |

---

### 11. [AI Commonwealth vs. AI Governance — Exchange](ai-commonwealth-vs-governance-exchange.md)

|  |  |
| --- | --- |
| **Question** | Should the framework explicitly shift from an "AI governance" frame to an "AI commonwealth" frame centered on ownership, access, and public infrastructure, or preserve governance as the primary frame and incorporate these ideas more narrowly? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md), [Source Digest — Stewart/Acemoglu/Autor (Weekly Show)](../../sources/source-weekly-show-stewart-ai-future-of-work-digest.md), [AI Governance Practice digest](../../sources/source-ai-governance-practice-digest.md) |
| **Produced** | Exchange opened. Initial questions captured around governance vs. commonwealth framing, timeline urgency, what counts as commonwealth infrastructure in AI, and whether existing public artifacts need reframing. **April 2026:** External evidence base added — the Stewart/Acemoglu/Autor digest provides the pro-worker AI directional frame, the data-extraction-economy critique, and a concrete commonwealth-style policy package (UBC + labor/capital tax rebalance + pro-worker R&D + wage insurance) ready to feed Round 1. |
| **Status** | Active; Round 1 complete; Rounds 2–N reserved. Round 1 (June 9, 2026 — same-lineage agent synthesis on the curated Stewart/Acemoglu/Autor base) recommends *commonwealth as a layer on top of governance*, maps the [Exchange #28](#28-ownership-taxonomy--systems-framework--exchange-f2) ownership taxonomy onto AI instruments (public compute = civic-commons; UBC = collective-dividend), and produces claim set E11-C1…C4; a companion note on AI ownership/access is recommended (feeds F4), Memo 01 not rewritten. Adversarial Round 2 reserved for an independent lineage. |

---

### 12. [Memo 01 Housing Claims — Historical Parallel Test Exchange](memo-01-housing-parallel-test-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does the published housing-domain practitioner and research literature confirm, challenge, or complicate Memo 01's core structural claims about institutional capacity, recursive uplift, infrastructure coordination, and reform-as-extraction trust failure? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md), [Roadmap](../../ROADMAP.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | First application of the Historical Parallel Test Protocol. Four structural claims from Memo 01 tested against published housing literature. Claim 2 (recursive uplift) identified as the project's most vulnerable housing claim — no published confirmation of the positive cascade. Claim 3 (infrastructure coordination) identified as the strongest. Sharpened practitioner prompt questions proposed for Recommendation 2. |
| **Status** | Active discussion. |

---

### 13. [Autonomous Proposal Generation — Agent Stress Test](autonomous-proposal-generation-stress-test.md)

|  |  |
| --- | --- |
| **Question** | Can AI agents, working autonomously across multiple models and protocols, generate concrete proposals that bridge the gap between the project's analytical framework and real-world reform — and what does the output reveal about the framework's generativity, its gaps, and the structural constraints on translating diagnosis into action? |
| **Depends on** | All core documents ([Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md)), all three process protocols ([Adversarial Review](../process/adversarial-review-protocol.md), [Coherence Audit](../process/coherence-audit-protocol.md), [Historical Parallel Test](../process/historical-parallel-test-protocol.md)), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (recursive uplift decomposition), [Exchange #12](#12-memo-01-housing-claims--historical-parallel-test-exchange) (housing evidence) |
| **Produced** | 135 proposals (112 unique after de-duplication) across all 15 Problem Map domains. Adversarial review from 4 perspectives identified political durability, displacement protection, and coalition math as critical gaps. Historical parallel testing on 4 clusters (institutional capacity, housing, democracy, capital). Four integrated reform sequences. Epistemic status assessment. Key finding: the framework is generative but political feasibility — not analytical quality — is the binding constraint. |
| **Status** | Active exchange. No steward input yet. Proposals are AI-generated hypotheses, not endorsed positions. All proposals individually cataloged in [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) for steward review. |

---

### 14. [Permitting Stack Recursive Uplift — Exchange](permitting-stack-recursive-uplift-exchange.md)

|  |  |
| --- | --- |
| **Question** | If `P-004` / `P-107` is the strongest candidate for initiating a recursive-uplift sequence, what would it take to turn the permitting-stack idea from an AI-generated proposal into a serious project hypothesis that is scoped clearly enough to analyze, critique, prototype, or eventually test in the real world? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (empirical-validation need), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (fast-feedback and recursive-uplift decomposition), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (proposal generation and uplift-chain ranking), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Frames `P-004` / `P-107` as the first candidate proposal for deeper development. Captures the initial case for why the permitting stack is the strongest recursive-uplift starting point, identifies core tensions (standardization vs. local variation, software vs. institutional reform, execution vs. trust claims), and defines starter questions for the next round. |
| **Status** | Active discussion. |

---

### 15. [Steward Feedback Proposal Iteration — Exchange](steward-feedback-proposal-iteration-exchange.md)

|  |  |
| --- | --- |
| **Question** | When steward feedback is added to a subset of proposals in the catalog, does that human input materially change what a new proposal-development round produces — in specificity, originality, prioritization, coalition awareness, or recursive-uplift logic? |
| **Depends on** | [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (argument for faster, iterative learning), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (original proposal generation), [Exchange #14](#14-permitting-stack-recursive-uplift--exchange) (single-proposal deep dive on `P-004` / `P-107`), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Frames a second experiment: steward-in-the-loop proposal iteration using annotations on 35 proposals from the catalog. Records the experiment's rationale, its relationship to the focused permitting-stack exchange, the likely output types, and the key methodological tensions. At exchange opening, the exact 35 annotated proposals are not yet visible in the saved catalog state available to the agent and remain to be incorporated in the next round. |
| **Status** | Active discussion. |

---

### 16. [Starting Proposal Comparative Review — P-004/P-107 vs. P-053](starting-proposal-comparative-review.md)

|  |  |
| --- | --- |
| **Question** | The project needs to commit development effort to a starting proposal. Between the Open-Source Permitting Stack (`P-004` / `P-107`) and Federal Skills-First Hiring (`P-053`), which better serves the project's goals of testing recursive uplift, producing visible results, building credibility, and generating empirical learning? |
| **Depends on** | [Exchange #3](#3-post-systems-framework-revision--next-steps) (empirical-validation need), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (fast-feedback and recursive-uplift decomposition), [Exchange #13](#13-autonomous-proposal-generation--agent-stress-test) (proposal generation and uplift-chain ranking), [Exchange #14](#14-permitting-stack-recursive-uplift--exchange) (initial P-004/P-107 development), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Roadmap](../../ROADMAP.md) |
| **Produced** | New exchange opened. Structured comparative framework across six dimensions (recursive uplift potential, learning velocity, visibility, political durability, project credibility, informative failure). Identifies open questions including whether the comparison is actually a sequencing question rather than either/or. **Steward decision (June 9, 2026):** develop `P-004` / `P-107` as the **primary** recursive-uplift target, `P-053` held as an **optional fast parallel early win**. |
| **Status** | Synthesized. Steward decision recorded (June 9, 2026): `P-004` / `P-107` primary, `P-053` optional parallel early win — resolving the comparison as a sequencing question. Development routes to [Exchange #14](#14-permitting-stack-recursive-uplift--exchange); pressure-tested by the [Exchange #10](#10-housing-financialization-as-upstream-capture--exchange) Round 1. Resolves Roadmap TODO #2. |

---

### 17. [First Practitioner Critique and AI Content Provenance — Exchange](first-practitioner-critique-ai-provenance-exchange.md)

|  |  |
| --- | --- |
| **Question** | What does the project's first practitioner feedback reveal about memo credibility, AI-content legibility, and orientation design — and how should the project operationalize content provenance standards in response? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange) (created the memo artifact), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (Recommendation 2 practitioner-critique lane), [Exchange #8](#8-voice-synthesis-accessibility-and-engagement--feature-exploration) (communication and engagement design), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) (`P-020`) |
| **Produced** | Six rounds (four constructive, one adversarial, one coherence audit) plus steward interstitial. Rounds 1–5 adopted a four-level content provenance standard, established that provenance labeling is necessary hygiene but not a trust strategy (Principle 9, PM §13), identified effort calibration and AI-sensitivity as compounding outreach barriers, concluded outreach-embedded relational disclosure matters more than website labels, reweighted the three-layer critique model with entry trust as highest-strategic-weight layer, downgraded P-020 dog-fooding claims from "validation" to "illustration," and produced a five-priority next-steps list. Round 6 identified a structural gap: all five priorities address input collection but none address practitioner retention. Added two priorities: design the post-critique practitioner pathway before feedback arrives, and connect the critique pipeline to the proposal development pipeline ([Exchange #14](#14-permitting-stack-recursive-uplift--exchange), [Exchange #16](#16-starting-proposal-comparative-review), [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md)). |
| **Status** | **Reopened.** Round 6 added. Steward decision pending on Priorities 6–7. |

---

### 18. [Formation Document Comparative Analysis — Exchange](formation-document-comparative-analysis-exchange.md)

|  |  |
| --- | --- |
| **Question** | How should Civic Blueprint use constitutions, charters, declarations, and organizational founding texts to test, sharpen, or challenge its own principles without collapsing meaningful difference into false consensus? |
| **Depends on** | [Principles](../../PRINCIPLES.md), [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md), [External Formation Documents README](https://github.com/Civic-Blueprint/external-formation-docs/blob/main/README.md), [Alignment Framework](../../formation-docs/ALIGNMENT_FRAMEWORK.md), [United States Constitution alignment memo](../../formation-docs/analysis/principle-maps/us-constitution-alignment.md) |
| **Produced** | New comparative-analysis track launched. Added a two-repo corpus workflow, with retained source texts in `external-formation-docs` and analysis/synthesis artifacts in `project-2028`, plus a proof-of-concept memo comparing the original U.S. Constitution against the 17 principles. Frames key methodological questions: structural constitutions vs. rights charters, overlap vs. asymmetry, and what should count as a principles-level gap. |
| **Status** | Active discussion. |

---

### 19. [Formation Document Initial Findings — Adversarial Review](formation-document-initial-findings-adversarial-review.md)

|  |  |
| --- | --- |
| **Question** | What are the strongest counterarguments against the early synthesis emerging from the formation-document corpus, and which current findings are robust versus artifacts of source selection, translation, or interpretive generosity? |
| **Depends on** | [Exchange #18](#18-formation-document-comparative-analysis--exchange), [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Alignment Matrix](../../formation-docs/analysis/synthesis/alignment-matrix.md), [Gap Analysis](../../formation-docs/analysis/synthesis/gap-analysis.md), [Uniqueness Report](../../formation-docs/analysis/synthesis/uniqueness-report.md) |
| **Produced** | **Round 1 (April 2026)** opened the first structured challenge to the comparative corpus, identifying source-selection bias, genre mismatch, false-overlap inflation, modernity bias, and translation risk as the main failure modes to test. **Round 2 (June 2026 — constructive response)** answered the challenge against the now-20-source corpus (no longer the 5 rights-forward texts Round 1 named — it now includes the structural/pre-modern/power-skeptical texts the challenge said were missing: US Constitution, Bill of Rights, Declaration, France 1789, Massachusetts, Texas, plus UN Charter and the African Union). Headline finding: adding those texts produced systematic **asymmetry**, not higher alignment — so the dignity/rights overlap is **concentrated in the rights-forward modern subset**, and the synthesis reads as *modern rights-constitutionalism convergence*, not *cross-tradition convergence* (a temper on the [#18](#18-formation-document-comparative-analysis--exchange) convergence claim and the [#20](#20-social-slop-and-information-integrity--exchange) alignment thesis). Reclassified the four early synthesis claims; downgraded expression→truth-infrastructure and sovereignty→open-design mappings to `implicit`/`different-resolution`; ruled organizational texts (Mondragon/ICA/B Corp) governance-form evidence rather than convergence evidence; and routed the gap candidates — **peace/anti-war** (UN Charter, Japan, AU) is the only one that cleared the bar for a principles-level discussion, the other three are articulation/subprinciple work. Cross-reference notes added to the [Alignment Matrix](../../formation-docs/analysis/synthesis/alignment-matrix.md), [Gap Analysis](../../formation-docs/analysis/synthesis/gap-analysis.md), and [Uniqueness Report](../../formation-docs/analysis/synthesis/uniqueness-report.md). **Round 3 (June 2026 — cross-lineage adversarial pass)** ran the hand-off packet on two clean independent lineages (Grok 4.3, GPT-5.5); a third (Gemini 3.1 Pro) was **discarded as contaminated** (run as a file-writing agent that read/wrote the exchange, defeating the reduced-context discipline — its points were independently raised by the clean two, so no signal lost; recorded as a reusable lesson and a candidate Protocol §2 addition). **Result: synthesis wounded, not falsified** — R3-2 (concentration) and R3-3 (modern-not-cross-tradition) → *contested*; R3-5 ("peace is the *only* gap") → *contested/weakened* (education-civic-formation is now a co-candidate); R3-1 and R3-6 narrowed (P3/P15 robust, P9/P11 have functional analogues); **R3-4 (expression→truth-infrastructure over-read) confirmed and safe to enact.** Three robust cross-cutting findings: the absent non-liberal/pre-modern/Indigenous families (Iran, PRC, Saudi, a Confucian order, Ecuador/Bolivia rights-of-nature) are **load-bearing** (corpus expansion is now the gating move); functional-vs-textual is the deepest unexamined seam (new required discipline); the convergence framing needs a constitutional-borrowing/influence lens. |
| **Status** | Active; **Rounds 1–3 complete**; Round 4 (response/v2, after corpus expansion) reserved. Round 3 cross-lineage pass (Grok + GPT clean; Gemini discarded-contaminated) **wounded but did not falsify** the synthesis (R3-2/R3-3 contested, R3-5 weakened, R3-4 confirmed); corpus expansion into the named non-liberal / pre-modern / Indigenous families is now the **gating move**. Steward decision (June 12, 2026): the **peace** discussion is **held** until that expansion — reinforced by Round 3 and widened to include education/civic-formation as a co-candidate. |

---

### 20. [Social Slop and Information Integrity — Exchange](social-slop-information-integrity-exchange.md)

|  |  |
| --- | --- |
| **Question** | Is "Social Slop" — engagement-optimized decontextualization that inflates method-level disagreements into apparent values-level conflicts — a named pattern the project should formally recognize, and how does it interact with Principle 14 (truth and evidence as public goods) and the alignment thesis? |
| **Depends on** | [Principles](../../PRINCIPLES.md) (§14 truth and evidence), [Problem Map](../../PROBLEM_MAP.md) (§3 information ecosystems), [Exchange #18](#18-formation-document-comparative-analysis--exchange) (convergence claim), [Exchange #19](#19-formation-document-initial-findings--adversarial-review) (adversarial challenge to convergence), [Phase 2 Website Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_2_BRIEF.md) |
| **Produced** | Exchange opened (April 2026): proposed definition of Social Slop as an information-integrity phenomenon; anchor case (WEF natural capital accounting repackaged as "monetize breathing") documented with full source-to-post transformation analysis; core mechanism identified (fragment extraction → threat reframing → outcome erasure → method-as-values substitution → engagement packaging); six open questions framed. **Round 1 (June 2026 — analytical synthesis)** works the six questions and reaches a recommended disposition on the three project-level decisions: **(a) adopt as terminology — No** (retain as internal shorthand only; the "slop" label reads as dismissive of a needed audience and the anchor case is one-directional); **(b) edit Principle 14 / Problem Map §3 — No** (the structural mechanism is already in P14's in-practice note and PM §3; the two genuinely-additive insights — method-as-values substitution, and context-restoration-not-fact-checking — are already carried, and held, by [#25](#25-shared-mirror-as-the-upstream-see-coordination-layer--exchange) M2; replacement-over-addition not cleared); **(c) public-facing artifact — No (for now)** (front-runs the on-hold #25 work; Q6 partisan-credibility risk). The decisive context: Social Slop was already generalized by **#25 (Shared Mirror, "one instance of mirror failure")** and subsumed by **#26**, and that coordination thread is on **hold**, so promoting the narrow instance now would front-run an unvalidated, parked generalization. Net: **subsume into #25**; harvest the five-step mechanism, the method-as-values insight, the context-restoration countermeasure, and the cross-partisan-symmetry requirement into the #25 M-claim set; record a re-promotion trigger (#25/#26 coming off hold *and* a symmetric cross-partisan evidence base). Also tempered by [#19 Round 2](#19-formation-document-initial-findings--adversarial-review), which narrowed the convergence thesis Social Slop was meant to support to *modern rights-constitutionalism convergence*. |
| **Status** | **Synthesized — disposition ratified by the steward June 12, 2026.** Round 1 (analytical synthesis) complete; disposition = **subsume into [Exchange #25](#25-shared-mirror-as-the-upstream-see-coordination-layer--exchange)** — adopted no standalone terminology, no Principle 14 / PM §3 edit, no public artifact; durable contributions harvested into #25's M-claim set; re-promotion trigger recorded. [Roadmap](../../ROADMAP.md) TODO #6 closed and archived. (In-lineage analytical round; no adversarial pass owed since nothing is promoted.) |

---

### 21. [Government Overreach, Ownership as Transition, and the Ratchet Problem — Exchange](government-overreach-ownership-ratchet-exchange.md)

|  |  |
| --- | --- |
| **Question** | Is public-interest governance inherently expansionary (the "ratchet problem"), is private ownership a transitional mechanism to abundance or a permanent feature, and can democratic process become a capture mechanism when a majority of voters are net beneficiaries of government spending? |
| **Depends on** | [Source Digest — Modern Wisdom #1084: Friedberg](../../sources/source-modern-wisdom-1084-friedberg-digest.md) (Clusters 3–7 + Steward Observation 1), [Source Index](../../sources/SOURCE_INDEX.md) (50 curated digests across 8 sub-debates: 43 from the first sweep used in Round 2 + 7 from the second sweep closing the Round 2 data gaps), [Principles](../../PRINCIPLES.md) (§2, §4, §5, §6), [Problem Map](../../PROBLEM_MAP.md) (Domains 2, 9, 13, 15), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) (recursive uplift decomposition), [Exchange #9](#9-debt-legitimacy-and-odious-debt--exchange) (debt/fiscal capture), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md) |
| **Produced** | Exchange opened. Adversarial challenge distilled from verified Friedberg claims. Three central questions framed (ratchet problem, ownership as transition, democracy as capture). Round 1 constructive analysis reframed the ratchet as a broader capture dynamic rather than a state-only phenomenon, argued ownership likely persists under abundance with differentiated moral weight, and named bounded-governance design as the unresolved crux. Round 2 stress-tested that thesis against 43 new source digests across the eight sub-debates, producing: a five-ratchet typology (scope / commitment / cascade / drift / concentration), a four-category ownership taxonomy (civic-commons / innovation / ecological-ceiling / transitional productive), a five-mechanism democratic-capture inventory (Caplan / Gilens-Page / Hacker-Pierson / Bartels / Kuran-Sunstein), an institutional-inclusiveness reframing of Principle 5 (Acemoglu-Robinson-Rodrik rather than state-vs-market), a sector-specific Perry-chart decomposition (concede housing, reform-concentration-not-retreat healthcare, mixed education), and a nine-element bounded-governance design package grounded in the Swiss debt brake, OECD/IMF fiscal-rules evidence, Buchanan-Tullock constitutional framework, and Ostrom polycentricity. Round 2 also flagged five residual data gaps. A targeted second research sweep (April 2026) closed all five gaps with seven new digests (Argentina / Milei; historical fiscal-consolidation cases — Canada 1990s, Sweden 1990s, NZ 1984; AI catastrophic-risk literature — Bengio/Russell/Bostrom/IDAIS; AI governance practice — EU AI Act/SB 1047/SB 53/U.S. EO sequence/NIST AI RMF; cooperative and platform-cooperative ownership — Mondragón; sovereign wealth funds — Norway GPFG/Alaska Permanent Fund; Swiss direct democracy). A Round 2 addendum in the exchange records what the new evidence shifts: the ownership taxonomy expands to five categories (adds collective-dividend); the bounded-governance design package is empirically grounded in at least five working national instances; democratic contraction is empirically possible but requires a fiscal-crisis enabling condition; direct democracy is a useful entrenchment mechanism but not a universal policy instrument; distributional incidence matters decisively for political sustainability. **Round 3 synthesis (April 2026)** produced the five commissioned deliverables against the full 51-digest corpus: (D1) a proposed revised text for Principle 5 reframing the principle as "inclusive institutions with bounded rules" and separating ownership from governance; (D2) a six-category ownership taxonomy (personal-autonomy / civic-commons / innovation / ecological-ceiling / transitional-productive / collective-dividend) with formal definitions, test questions, moral-weight reasoning, and policy implications; (D3) a nine-element bounded-governance doctrine with canonical precedents (Swiss debt brake, Swedish rules architecture, Norway GPFG, Alaska PFD, EU AI Act, California SB 53, NIST AI RMF); (D4) a frontier-AI worked example applying the doctrine element-by-element to 2024–2026 AI governance, identifying structural gaps (missing compensation/accounting, sunset, distributional-incidence review) and producing specific project-voice recommendations; (D5) a distributional-incidence addendum elevating distributional review from addendum to constitutive element, with operational guidance (incidence table, incidence explanation, compensatory-design note). Round 3 closed with a six-item follow-up exchange menu (F1–F6: Principle 5 revision, ownership taxonomy into SYSTEMS_FRAMEWORK, doctrine as public artifact, frontier-AI framework, housing-reform position, distributional-incidence protocol) and an epistemic-status table for the synthesis claims. |
| **Status** | **Adversarially-tested synthesis.** Rounds 1–5 complete. Round 4 applied the [Adversarial Review Protocol](../process/adversarial-review-protocol.md) to Round 3's five deliverables; Round 5 integrated the wins and produced v2 versions (revised Principle 5 text with ownership-governance interaction + named tradition + form-list + reference-class limit; seven-category taxonomy adding communal-stewardship; ten-feature doctrine under specific conditions, with guarded-technocratic-layer element and authenticity conditions; ratchet-acknowledged capability-indexed AI package; anti-theater distributional-incidence protocol with worst-off-protection column). Residual debt: no external human reviewer; recorded as the largest structural gap, with F1–F6 follow-up exchanges conditioned on closing it. Steward decision pending on which follow-ups (F1–F6) to open; follow-ups now operate on v2 deliverables. |

---

### 22. [Entry-Trust Failure with a Domain-Expert Practitioner — Exchange](entry-trust-domain-expert-practitioner-exchange.md)

|  |  |
| --- | --- |
| **Question** | What would have made a domain-expert practitioner — whose attempt to open a childcare center was nearly bankrupted by municipal-permitting failure — say _"yes, I see what this is, here's what I'd add"_ instead of _"no clue what any of it says... too high definition to understand"_ — and what does answering that imply for the project's communication architecture, its outreach design, and its first-stop public surfaces? |
| **Depends on** | [Feedback Record — Childcare Licensing Practitioner, April 2026](../../feedback/feedback-childcare-licensing-practitioner-2026-04.md) (anchor), [Exchange #8](#8-voice-synthesis-accessibility-and-engagement--feature-exploration) (deferred plain-language work pending real-user data; this exchange supplies that data), [Exchange #17](#17-first-practitioner-critique-and-ai-content-provenance--exchange) (entry-trust as highest-strategic-weight layer; Priority 6/7 post-critique pathway), [Exchange #14](#14-permitting-stack-recursive-uplift--exchange) and [Exchange #16](#16-starting-proposal-comparative-review--p-004p-107-vs-p-053) (the practitioner's domain is structurally adjacent to the housing permitting stack the project's lead proof-of-usefulness work targets), [Principles](../../PRINCIPLES.md) (§1, §2, §10, §14), [Problem Map](../../PROBLEM_MAP.md) (§3, §13), [Roadmap](../../ROADMAP.md) (Recommendations 2 and 4), [Friedberg digest Steward Observation 3](../../sources/source-modern-wisdom-1084-friedberg-digest.md), [Stewart/Acemoglu/Autor digest Cluster 8](../../sources/source-weekly-show-stewart-ai-future-of-work-digest.md). |
| **Produced** | Exchange opened. Anchor feedback record preserved with privacy protections in new `feedback/` directory. Central question framed in terms of practitioner experience rather than steward-preferred solutions. Six initial tensions captured: artifact vs. entry path, lexical vs. architectural fix, reconciliation with Exchange #8 deferral, manipulation guardrail, generic vs. domain-specific entry, re-engagement ethics. Round 1 added a constructive diagnosis of the outreach prompt: relationship layer and trust posture worked, recognition layer was missing or too weak, and the memo was too deep as a first stop. Recommended a small domain-specific recognition-layer test before any broad memo rewrite, plus a Pass 0 comprehension check for practitioner critique. Round 2 narrowed the diagnosis after reading the live `Hero` and `MemoFeature` components: the project already has a competent evaluator surface and a substantial entry-trust infrastructure (provenance standard, Exchange #17 priorities 1–7, Reviewer Packet, Reviewer-as-a-Round convention) — what is missing is a parallel non-evaluator first-encounter path for warm-relationship referrals. Refined Exchange #17's seven priorities against this episode and proposed a small three-variant recognition-paragraph experiment (childcare-specific, permitting-specific, cross-domain) routed through the Reviewer Packet to also satisfy ROADMAP TODO #11 first-use. Round 3 applied the Adversarial Review Protocol (Options A/B/C) and challenged that emerging consensus: argued the exchange may be overstating target-audience fit, overreading the phrase "too high definition," preserving unwarranted confidence in the current memo/evaluator path, and treating the recognition-paragraph experiment as more decisive than the evidence supports. Proposed a harsher alternative hypothesis that the stronger next test may be a bounded useful childcare-licensing artifact rather than a better introduction to the current memo. Cumulative epistemic-status table downgraded several Round 1/2 claims from working-hypothesis confidence to contested/speculative. Round 4 (constructive synthesis, requested after the steward reported agreeing most with the adversarial round and feeling honest confusion about next steps) separated what the four rounds agree on from the five live disagreements, then converted the disagreement into a five-move parallel work plan: (1) draft a one-page bounded useful childcare-licensing flow artifact, (2) treat recognition paragraphs as operational copy paired with the artifact rather than as a standalone test, (3) run a low-formality test in the warm channel without the Reviewer Packet, (4) sharpen Exchange #17 Priority 2's clearance-rate metric to record failure mode and channel, (5) only re-engage this practitioner after Move 1 exists, in the warm channel, with an explicit out. Reviewer Packet first-use is explicitly deferred to a different, non-warm-channel recruitment under ROADMAP TODO #11. Round 2's standalone recognition-paragraph experiment is recorded as superseded by Round 4 in the cumulative epistemic-status table. Round 4 execution (April 2026): the four steward-independent artifacts called for at the end of Round 4 now exist — Move 1 as [`civicblueprint.org/docs/CHILDCARE_LICENSING_FLOW_DENVER.md`](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/CHILDCARE_LICENSING_FLOW_DENVER.md) (a one-page Denver childcare-licensing flow grounded in primary `denvergov.org` and `cdec.colorado.gov` sources, with Move 2's three recognition paragraphs as its inline cover section), Move 4 as an in-place [Priority 2 amendment](first-practitioner-critique-ai-provenance-exchange.md) to Exchange #17 capturing per-bounce `failure_mode` / `channel` / `artifact_tested`, and Move 5 as a drafted-but-unsent [re-engagement template](../../docs/RE_ENGAGEMENT_TEMPLATE_CHILDCARE_2026_04.md). Move 3 (sending the artifact in the warm channel) is steward-owned and pending. Round 5 (May 2026) records an _unsolicited_ substantive follow-up from the same practitioner — Katelynn, attributed at first-name level only by steward decision after she volunteered broader attribution — who re-engaged the steward on 2026-05-07 _without_ the project executing Move 5 and _without_ Move 1 being shown to her. She supplied a five-issue enumeration of the original childcare-center licensing failure plus a documented sign-permitting episode (verbatim in the [feedback record](../../feedback/feedback-childcare-licensing-practitioner-2026-04.md)). Round 5 commits Move 6 — a friction-pattern addendum to the Denver flow capturing scope-creep at inspection, multi-track approval inconsistency, heritage-review meeting cadence as rate-limiter, and code-asymmetry between institutional and private actors, source-anchored to Denver primary materials, with no verbatim practitioner language and no location-bearing detail. Round 5 also sharpens the Move 3 recipient question: Move 3 should now be addressed to a _different_ comparable practitioner to avoid conflating the entry-trust test with reciprocity to Katelynn's substantive contribution; Katelynn is separately owed a steward-voice reciprocity reply in the warm channel acknowledging what she sent and what the project did with it. The exchange remains open. |
| **Status** | Active discussion; Rounds 1–5 complete. Round 5 (May 2026) records an unsolicited substantive practitioner follow-up (no Move 5 sent), commits Move 6 (friction-pattern addendum to the Denver flow), and sharpens the Move 3 recipient question (a *different* comparable practitioner). Move 3 still pending steward action; Move 6 awaiting steward go-ahead. Practitioner attribution updated to first-name only with location redacted by steward decision; see [feedback record Consent log](../../feedback/feedback-childcare-licensing-practitioner-2026-04.md). |

---

### 23. [Principle 5 Revision — Exchange (F1)](principle-5-revision-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does the [Exchange #21 Round 5 v2 Principle 5 text](government-overreach-ownership-ratchet-exchange.md#deliverable-1--revised-principle-5-text-v2) survive one more adversarial pass and one external human reviewer round, and what is the v3 text that should replace [PRINCIPLES.md §5](../../PRINCIPLES.md#5-critical-systems-require-public-interest-governance) and reconcile it with [FOUNDATIONAL_COMMITMENTS.md §5](../../FOUNDATIONAL_COMMITMENTS.md#5-critical-systems-require-inclusive-institutions-with-bounded-rules)? |
| **Depends on** | [Exchange #21](#21-government-overreach-ownership-as-transition-and-the-ratchet-problem--exchange) (the v2 text under review), [PRINCIPLES.md §5 (current)](../../PRINCIPLES.md#5-critical-systems-require-public-interest-governance) and [FOUNDATIONAL_COMMITMENTS.md §5 (v2-derived)](../../FOUNDATIONAL_COMMITMENTS.md#5-critical-systems-require-inclusive-institutions-with-bounded-rules) (the drift this exchange resolves), [April 2026 Coherence Audit Pass 2 (finding P2-2)](../process/audits/coherence-audit-2026-04.md#pass-2--problem_mapmd-hallucinations-and-principlesmd--foundational_commitmentsmd-5-drift), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Reviewer Packet Template](../../docs/REVIEWER_PACKET_TEMPLATE.md), [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md), [filled F1 reviewer package](../../docs/REVIEWER_PACKAGE_PRINCIPLE_5_F1_2026_04.md), [ROADMAP TODOs #1, #10, #11](../../ROADMAP.md). |
| **Produced** | Round 1 complete: input under review reproduced verbatim; what the v2 text was responding to (the four Round 4 axes integrated in Round 5); the §5 drift to be resolved; round plan (R2 adversarial under Options A+C; R3 external review per the Reviewer Packet; R4 response round producing v3 text and clause-by-clause changelog; R5 steward voice edit + integration into PRINCIPLES.md and FOUNDATIONAL_COMMITMENTS.md at the same commit). Round 2 complete: adversarial review found v2 directionally stronger than current §5 but not integration-ready; central finding is that v2 overburdens `PRINCIPLES.md` by trying to carry principle, doctrine, tradition genealogy, examples, and research debt in one section. Round 2 recommends a shorter and more modular v3; an artifact-boundary rule before drafting; converting the reference-class caveat into an operational constraint; naming inclusive/bounded tradeoffs; guarding against hollow oversight/participation theater; and using Round 3 to test audience portability or hollow-adoption risk. Filled Round 3 reviewer packet prepared for a politically engaged, community-rooted reviewer as perspective-gap + audience-portability review. |
| **Status** | Active; Round 2 complete; Rounds 3–5 reserved. Round 3 packet prepared; awaiting reviewer acceptance and submitted response. |

---

### 24. [Coordination Architecture Reframe — Exchange (Path β)](coordination-architecture-reframe-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does the candidate reframe from the [Constitutional Ecology and Coordination Architecture Riff](../explorations/constitutional-ecology-and-coordination-architecture-riff.md) (*Project 2028 as coordination architecture for pluralistic societies under accelerating complexity* rather than *blueprint for civic systems*) survive structured adversarial pressure well enough to warrant Path γ doctrine drafting — and what is the project's current epistemic-status on the five testable claims (C1 coordination primitives, C2 diffuse-sovereignty layers, C3 metabolization-as-failure-mode, C4 procedural-legitimacy-under-deconstruction, C5 sequencing-inversion of reciprocity-riff OQs)? |
| **Depends on** | [Constitutional Ecology and Coordination Architecture Riff (v2)](../explorations/constitutional-ecology-and-coordination-architecture-riff.md) (the reframe under test), especially [§7.ter](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#work-item-c1--the-35-testable-claims-for-path-β-adversarial-review) (the five claims) and [§5.1.bis](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#51bis-coherence-check--principles-and-problem-map-domains-as-coordination-primitives-v2) (coherence check); [Reciprocity and Decolonial Frame Riff (v5)](../explorations/reciprocity-and-decolonial-frame-riff.md) (downstream per riff §6.2); [Phase 3 Front Door Riff](../explorations/phase-3-front-door-riff.md) (depends on the outcome); [Adversarial Review Protocol](../process/adversarial-review-protocol.md) (Round 2 applies Options A + C); [PRINCIPLES.md](../../PRINCIPLES.md), [PROBLEM_MAP.md](../../PROBLEM_MAP.md); indicator sources for C4 (V-Dem 2026, Freedom House 2026, Bright Line Watch Feb–Mar 2026, Little & Meng 2024 contrarian read). |
| **Produced** | Round 1 complete: five testable claims (C1–C5) stated with explicit falsification conditions; round plan with Rounds 2–5 reserved. Round 2 complete (first-pass adversarial under Options A + C with coordination-domain-skeptic lens): claim-by-claim adversarial findings; four cross-cutting findings (agent-self-coherence confounder; Disability Justice engagement as the riff's most exposed present-tense metabolization risk; named-thinker engagement too thin on Mouffe / Cover / Graeber-Wengrow; legitimacy as the central unsolved problem); epistemic-status table per Protocol §3 (C4 empirical premise *established by evidence*; C2 layer-identification weak version and C4 plus C1 weak version at *working hypothesis*; C5 *contested*; C3 metabolization operationalization *speculative* — the reframe's weakest claim); agent recommendation to commission Round 3 with a Disability Justice-grounded reviewer before Path γ. The reframe survived Round 2 in that it was not falsified, but it did not pass cleanly; steward holds the decision on Round 3 vs. hold-at-β vs. proceed-to-γ-while-carrying-unsolved-questions. |
| **Status** | Active; Rounds 1–2 complete; Rounds 3–5 reserved. **v2.1 (May 27 PM)** amended §2.5 recommendation to Option E hybrid (new §2.5.bis): Lane 1 — recruit one warm-channel generalist reviewer immediately for audience-portability and steelman-integrity check; Lane 2 — open slow cold-outreach lane to Disability Justice / reciprocity-tradition reviewers without hard deadline; default after ~3–6 months if Lane 2 produces nothing — proceed to Path γ-with-named-debt. Original recommendation preserved verbatim in §2.5 for the record. Steward actions D1 (Lane 1 recruitment, 1–2 hours) and D2 (Lane 2 posture-setting, ~30 minutes) captured as ROADMAP TODOs #3a and #3b. |

---

### 25. [Shared Mirror as the Upstream "See" Coordination Layer — Exchange](shared-mirror-see-layer-exchange.md)

|  |  |
| --- | --- |
| **Question** | Is *collective self-perception* — a society's capacity to see itself accurately, "the shared mirror" — a distinct upstream coordination layer ("see," ahead of decide/act) the project should name and design for, and do the shared-mirror riff's central claims survive structured adversarial pressure (M1 see-is-upstream; M2 mirror ≠ fact-checker; M3 the values-lens does non-redundant work on true-but-framed cases; M4 it is a distinct coordination primitive, not a relabel of Principle 14 / PM §3 / #20 / #24; M5 it is testable at small N inside the project)? |
| **Depends on** | [Shared Mirror and Collective Self-Perception Riff](../explorations/shared-mirror-collective-self-perception-riff.md) (source exploration; §4 the bet, §4.5 mirror ≠ fact-checker, §3.3 three assumptions, §6 rings, §8 open questions), [Exchange #20 (Social Slop)](social-slop-information-integrity-exchange.md) (generalized — one instance of mirror failure), [Exchange #24 (Coordination Architecture Reframe)](coordination-architecture-reframe-exchange.md) (this exchange feeds #24's C1/C2 with a concrete "see" primitive and is downstream of its framing), [Phase 3 Front Door Riff](../explorations/phase-3-front-door-riff.md) (downstream — a surviving mirror is a candidate front-door surface), [Principles](../../PRINCIPLES.md) (§14, §13, §4), [Problem Map](../../PROBLEM_MAP.md) (§3, §15), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md), [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md) |
| **Produced** | New exchange opened (graduated from the shared-mirror riff). Round 1 restates the riff's content as five falsifiable claims (M1–M5), each with a stated falsification condition, mapped to the riff's §8 open questions. **Round 2** applied first-pass adversarial review (Options A + C) plus a Research-Protocol T2 source-tiering pass (Community Notes / bridging — Nature Communications 2026; Polis / vTaiwan — Chen 2024 + Noveck 2023; Moral Foundations Theory replication critiques), producing an epistemic-status table. Headline finding: the frame survives but is not clean — lead claim downgraded from **M1-strong** to **M1-weak** (the "see" layer stalls without parallel decide/act, per vTaiwan's "isegoria evaporated at the threshold" and Madrid Decide's 1-of-28,000); M2's reflect-don't-adjudicate distinction is the most defensible claim while its "break the millions" scale ambition is the least (Community Notes works once shown — −61.2% spread — but is slow, low-coverage, gameable); M3's values-lens needs a vocabulary reframe (MFT's five-factor model fails to replicate); M4's distinctness vs. #24 and the M5 Ring-1 test are the open joints. Recommends Round 3 external review + a pre-registered Ring-1 test before any promotion to #24 doctrine or a Phase 3 brief; that Ring-1 test is now pre-registered in the exchange's **Appendix A** (the buried-structure-delta metric, a stated null, and a symmetric anti-narrowing guard with an expect-disagreement probe — registered June 2, 2026 against Exchange #24's nine-claim epistemic-status table as the item set). **Run 1 complete June 2, 2026 (§A.12):** D = 4 ≥ τ with both SCA (items 1/4/7) and EMA (item 9, a reversal) present and the probe (item 8, C5) preserved → M5 to a *provisional* working hypothesis; an agent-persona pass only (correlated base model, agent-run), pending human-panel replication, with no promotion to #24 doctrine or a Phase 3 brief following from it. **Run 2 (cross-model on `composer-2.5-fast`, §A.13):** the divergence-detection core replicated (D = 5; SCA items 1/4 and the EMA reversal item 9 robust across two models and the human anchor) but the anti-narrowing probe (C5) leaned to collapse under the second model — so M5's *clean* pass is contested (the safety guard is model-dependent), reinforcing the "do not promote" stance and narrowing the remaining human ask to a practitioner check on the standpoint-dependent item (C5). **Runs 3–4 (own-voice GPT + Grok, §A.14):** two more frontier models judged the nine in their own voice (not personas); they agreed with each other 9/9, the core findings (item 1 fails; item 9 "not ready for doctrine" reversal) held across four model lineages + the human anchor, and both read the probe (C5) as `split` — re-strengthening the anti-narrowing guard and recasting Run 2's probe-collapse as a likely persona-instantiation artifact, leaving a real practitioner on C5 as the one irreducible check. **Runs 5–6 (cross-model persona panels — Grok, GPT-5.5, §A.15):** the bridging mechanism was re-run end-to-end on two more base models — D ≥ τ in 4/4 panel runs (Claude/Composer/Grok/GPT-5.5), the probe held in 3/4 (Composer the lone outlier), and two findings recur in every panel — item 4 (SCA: "7 layers sufficient" fails) and item 9 (EMA reversal: reframe not ready for doctrine). M5 → well cross-model-replicated working hypothesis; Run 2 clean-pass downgrade reversed; still provisional (shared training corpus → reliability ≠ validity, Ring 1, no practitioner) and no promotion. Positioned to consolidate the coordination thread — generalizes #20, feeds #24, informs Phase 3 — rather than fragment it. |
| **Status** | Active — at rest pending a promotion trigger; Rounds 1–2 complete; Ring-1 test complete (6 runs, §A.12–A.16); routing decision = hold (no promotion); Round 3 (external human) deferred, Rounds 4–5 contingent. |

---

### 26. [Coordination Triad (See / Decide / Act) — Combined Exchange (Path C)](coordination-triad-combined-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does the See / Decide / Act coordination triad, taken as **one object**, survive structured adversarial pressure as a combined claim set — i.e., do the triad-level claims (above all **T2 interdependence** and **T3 distinctness-over-#24**), carried with the per-leg claims, hold up well enough *together* to justify treating coordination as a single three-function design target rather than three separate problems (Path A)? |
| **Depends on** | [Coordination Triad — See / Decide / Act Riff (v2.8)](../explorations/coordination-triad-see-decide-act-riff.md) (source; §10 combined claim set, §10.1 design principle, §10.5 T-series, §10.6 readiness bar, §10.8/§10.12/§10.13 evidence + the two rigor tests, §6 sequencing, §7 triad × layers matrix); [Exchange #25 (Shared Mirror — the "see" leg)](#25-shared-mirror-as-the-upstream-see-coordination-layer--exchange) (M1–M5 imported at status; the #25 *hold* governs; M1-weak seeds T2 — **not** re-litigated); [Exchange #24 (Coordination Architecture Reframe)](#24-coordination-architecture-reframe--exchange-path-β) (the diffuse-sovereignty layers; T3 tests distinctness *over* it); [Exchange #20 (Social Slop)](#20-social-slop-and-information-integrity--exchange) (one see-layer failure mechanism, subsumed); [Principles](../../PRINCIPLES.md) §14/§17/§4/§13; [Problem Map](../../PROBLEM_MAP.md) §3/§15; [Adversarial Review Protocol](../process/adversarial-review-protocol.md) (R2, Options A + C), [Research Protocol](../process/research-protocol.md) (evidence tiering), [Historical Parallel Test Protocol](../process/historical-parallel-test-protocol.md) (model for the §10.12 T2-systematic test); [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md) (R3) |
| **Produced** | New exchange opened (graduated from the coordination-triad riff once its §10.6 readiness bar was *substantially met / steward-callable*). **Round 1** restates the §10 combined claim set as falsifiable claims in **two tiers** — per-leg *components* (see M1–M5 imported from #25 at status; decide D1–D5; act A1–A4) and the triad-level *T-series* (T1–T4b) — each with a falsification condition and its honest status carried from the riff, not upgraded. States the **design principle** (a combined exchange earns its existence only by testing the T-series — claims about the *interaction* of the three legs that separate single-leg exchanges cannot test). The combine-rationale entered resting on T2 (interdependence — *supported* by the §10.12 systematic test) and T3 (distinctness over #24 — *lean-supportive*), explicitly **not** on strong T4b (the "single unifying object," *falsified* by the §10.13 corpus test; weak T4b retained), with honest residuals carried (D3b/D4b owe their own evidence; the T2 single-leg cell is thin / ProZorro on the coding seam; the T4b control under-powered). **Round 2** applied first-pass adversarial review (Options A + C — reduced context + a coordination-skeptic lens), concentrating on the T-series and the *"does combining add value over Path A?"* question. **The frame survived but did not pass cleanly:** T2 downgraded *supported → working hypothesis* (~0.55 upper bound — the §10.12 single-leg cell is confounded by a deliberation-catalogue sampling frame; named disconfirmers — secret ballot, central-bank independence, RTI/FOIA — unadjudicated; the "act must bind" sharpening reads as an act-upstream sequence, not co-equal interdependence); T3 downgraded *lean-supportive → contested* (~0.4 — its distinctness lives in the thin corporate/AI/financial rows while the grounded rows collapse toward "everything bottlenecks at act/enforcement"); the central combine-vs-Path-A claim is *contested → leaning weak* (~0.4 — the one-object warrant T4-strong is falsified, T2 was already produced by the cheaper path/the riff, and decide + act enter un-adversarially-tested). **Deepest finding (directional):** three independent threads point at **act/enforcement as a candidate *upstream* leg** — a near-inversion of the original see-first bet and a *sequence* claim the triad was built to supersede. **No promotion:** the #25 *hold* stands, reinforced. Round 2 recommends Round 3 external review (commons-governance / social-choice / deliberation reviewer) framed around the disconfirming-search and T3-prediction questions, and/or giving decide + act their own first-pass adversarial passes before pressing the T-series. Rounds 3–5 reserved (R3 external human review; R4 response → v2; R5 synthesis + steward routing). |
| **Status** | Active; Rounds 1–2 complete; Rounds 3–5 reserved |

---

### 27. [Discovery Principle and Moral Architecture — Develop-Leg Exchange](discovery-principle-develop-leg-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does moral architecture develop primarily from *discovered* framework-inadequacy rather than instruction — and, if so, can civic architecture support *graceful repair at collective scale* without (a) manufacturing the crisis or (b) rebuilding authority-coupling at group scale — well enough to justify an independent artifact over *hold*? |
| **Depends on** | [Discovery Principle and Moral Architecture Riff (v1.2)](../explorations/discovery-principle-moral-architecture-riff.md) (source; §1.4 hub/coupling/corridor, §2.1 discovery, §2.4 cross-scale discipline, §2.5 authority-coupling, §4.2 dose-response, §5/§5.3 civic + community, §6 placement, §8 guardrail, §9 open questions); [Develop-Leg Research-Grounding Digest](discovery-principle-develop-leg-research-grounding.md) (the shared evidence base — Clusters A/B/C incl. the dose-response gap-close; same-lineage, pending cross-lineage verification); [Exchange #25 (Shared Mirror — "see" leg)](#25-shared-mirror-as-the-upstream-see-coordination-layer--exchange) (the Round-1→reserved-adversarial model; the *hold* governs); [Exchange #26 (Coordination Triad)](#26-coordination-triad-see--decide--act--combined-exchange-path-c) and [Exchange #24 (Coordination Architecture Reframe)](#24-coordination-architecture-reframe--exchange-path-β) (S19's placement target); [Exchange #20 (Social Slop)](#20-social-slop-and-information-integrity--exchange) (one moral exercise, subsumed); [Comparative Alignment Protocol](../process/comparative-alignment-protocol.md) (the cross-lineage Round-1 method); [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md); [Principles](../../PRINCIPLES.md) §3/§4/§10/§13/§14/§15/§17, [Problem Map](../../PROBLEM_MAP.md) §3/§7/§13/§15 |
| **Produced** | New exchange opened (graduated from the discovery-principle riff). **Round 1** is a **cross-lineage synthesis** — the riff was decomposed independently by three model families (an Opus same-lineage *baseline*/control, **GPT 5.5**, and **Gemini 3.1**), each given the same packet + research-grounding digest, and the steward-approved union (medium grain) is a 24-claim set (S1–S24) with falsification conditions and per-claim lineage provenance — a 21-claim tri-lineage synthesis (S1–S21) plus a same-lineage coverage-scan addendum (S22–S24, flagged †, defensive/refining; *not* tri-lineage). Load-bearing tier: **S17 cross-scale transfer** (the decisive claim), **S6/S7 dose-response make-or-break**, **S18 relabel gate**, **S21 reflexive guardrail**. Two cross-lineage findings shaped the synthesis: (a) all three independents named **cross-scale transfer + the dose-response gap** as the first adversary targets (strong non-same-lineage signal); (b) the §2.5 **collapse-dynamics (S13) was demoted to non-load-bearing** (2 of 3 lineages treated it as peripheral) while **pluralism-as-non-correlation (S12) was kept** load-bearing. The same-lineage research from a [rolled-back in-lineage attempt](discovery-principle-develop-leg-exchange.md#standing-items) was preserved and cleaned into the research-grounding digest; a June 2026 T2 **gap-close** then grounded the dose-response conditions as digest **Cluster C** (Edmondson, Pettigrew & Tropp, Tedeschi & Calhoun, Frazier et al., Yerkes–Dodson). **No promotion** (the #25 *hold* governs). **Round 2 (adversarial) has since run cross-lineage** — GPT, Grok, and Gemini, blind to each other, returned a **unanimous HOLD**: no load-bearing claim survives as a supported positive finding, with **S17** (cross-scale transfer) and **S18** (relabel) the decisive failures, plus unanticipated attacks (Haidt post-hoc misapplication, supply-creates-demand, privilege-of-readiness, grievance-builds-architecture). The Round 1 claim statuses are left unrewritten; the response is carried in **Round 4 (§4)**. **Round 4 (response/v2) then converted the HOLD into a live test rather than a dead end** — at steward direction, prompted by a "three-utilities" reframe (*"no evidence yet" ≠ proof of impossibility*): conceding the theory is a relabel, it relocates novelty to a **testable civic design hypothesis** (institutions engineered for non-correlated inputs + psychological safety + post-break consolidation repair better than answer-transmission bodies, without manufacturing crises or recentralizing authority) and recasts **S17 as a test design with a pre-registered falsifier** (behavioral measurement to defuse the Haidt post-hoc attack; process-level unit of analysis to beat the ecological fallacy; the project's own cross-lineage review named as the smallest, already-running test rung, n=1 caveat). Attack-driven refinements: S3 (drop strict demand→supply ordering), S15 (consent/agency over one's own tension), S16 (grievance/practice → **revisable/fused**). The develop-leg is now a **live hold** — a research program whose §4.6 **[test-design memo](discovery-principle-develop-leg-test-design-memo.md) is drafted (June 2026)**: the measurement instrument (collective repair capacity, behavioral, ecological-fallacy-guarded), matched comparison, an **F1–F6 pre-registered falsifier set**, ethics/stop conditions, the staged rungs (project as Rung 0 → multi-site), and an **agent-automation architecture** (persona × model-lineage roles with an instrument↔subject firewall — a persona-sim is red-team/instrument-validation only, never evidence). It is **design only — not run, no results, no promotion, S17 still on hold**. The eight reviewer-surfaced sources (Kahan, Bandura, Piaget, Latané, Durkheim, Rogers, Kohlberg/Rest, Buchanan & Powell) have since been **T2-grounded** as [digest Cluster D](discovery-principle-develop-leg-research-grounding.md) (June 2026) — most cut against or bound the claims, supplying named relabel antecedents for S18 and a competing structural account of collective moral change for S17; the external-human Round 3 remains deferred. **No promotion** (the #25 *hold* governs). |
| **Status** | Active; **Rounds 1, 2, and 4 complete** (Round 2 = cross-lineage HOLD; Round 4 = response/v2 reframe to a testable civic design hypothesis, run ahead of the deferred external-human Round 3); **live hold** — the §4.6 [test-design memo](discovery-principle-develop-leg-test-design-memo.md) is at **v0.2 (design only, not run)**, hardened by cross-lineage [Pipeline Run 001](discovery-principle-develop-leg-pipeline-run-001.md) (verdict REVISE, 5 BLOCKING fixes folded in, 3 divergences open for v0.3); Round 5 reserved |

### 28. [Ownership Taxonomy → Systems Framework — Exchange (F2)](ownership-taxonomy-systems-framework-exchange.md)

|  |  |
| --- | --- |
| **Question** | How should the v2 seven-category ownership taxonomy from [Exchange #21](#21-government-overreach-ownership-as-transition-and-the-ratchet-problem--exchange) be formalized in the [Systems Framework](../../SYSTEMS_FRAMEWORK.md), and what does it imply for [Problem Map](../../PROBLEM_MAP.md) Domain 2 (capital allocation) and Domain 10 (wealth/power concentration)? |
| **Depends on** | [Exchange #21](#21-government-overreach-ownership-as-transition-and-the-ratchet-problem--exchange) (source — Deliverable 2 v2 seven-category taxonomy; Round 4 communal-stewardship win), [Exchange #23](#23-principle-5-revision--exchange-f1) (revised §5 must stay consistent with the ownership-form vocabulary), [Systems Framework](../../SYSTEMS_FRAMEWORK.md) (integration target), [Problem Map](../../PROBLEM_MAP.md) Domains 2 and 10, [Principles §5](../../PRINCIPLES.md#5-critical-systems-require-public-interest-governance), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md) |
| **Produced** | New exchange opened — the F2 follow-up from Exchange #21, spawned per [Roadmap TODO #1](../../ROADMAP.md) (June 9, 2026) as the one #21 follow-up not gated on external-reviewer recruitment. **Round 1** frames the integration: carries the seven-category taxonomy, proposes placement in `SYSTEMS_FRAMEWORK.md` as an *analytical tool* (not in Principles), and states five falsifiable claims — F2-C1 (tool placement), F2-C2 (Domain 2 ownership-type leverage), F2-C3 (Domain 10 counter-forms: collective-dividend + communal-stewardship), F2-C4 (disjointness discipline travels), F2-C5 (completeness on the policy-relevant range) — each with a falsification condition. Carries #21's residual debt (cultural parochialism; empirical thinness on hybrid forms). An adversary packet is produced for an independent-lineage Round 2; Round 3 reserved for the response plus the actual SF / PM edits under a coherence-audit pass. **Anchor case (June 9, 2026):** the Taylor, TX park-deed → data-center conversion ([404 Media](https://www.404media.co/a-farmer-donated-land-to-turn-into-a-park-the-city-is-building-a-massive-data-center-instead)) is added to Round 1 as a real-world test — it evidences the communal-stewardship category and surfaces a carried refinement (the enforceability fragility of category 7) plus a sixth adversary probe for Round 2. A self-contained, copy-paste **Round 2 hand-off packet** is included in the exchange for the independent-lineage run. **Round 2 (June 9, 2026 — cross-lineage adversarial; GPT-5.5, Gemini 3.1 Pro, Grok 4.3, blind to each other)** returned a strong, convergent **revise-before-integrate** verdict: F2-C2/C4/C5 + the enforceability probe **falsified**, F2-C1/C3 **wounded→falsified-leaning**. Unanimous load-bearing findings — enforceability/robustness must be a *constitutive axis* (not optional metadata; the Taylor case is dispositive), the taxonomy classifies moral *form* rather than *control-rights*, it is skewed toward "nice"/reformable forms and omits dominant concentrating forms, and collective-dividend is *redistributive, not structural*. Convergent missing categories: corporate-fiduciary/shareholder-primacy, rentier-absentee/financial-speculative, restricted-purpose/dedication, state-security/sovereign-monopoly, open-access, operational/use-right. **Net: HOLD on integration** — the v1 taxonomy goes to a Round 3 revision (v3, control-rights + enforceability re-axis) before any SF/PM placement, then a confirmatory Round 4 adversarial pass; this supersedes-in-part [Exchange #21](#21-government-overreach-ownership-as-transition-and-the-ratchet-problem--exchange) Deliverable 2. **Round 3 (June 9, 2026 — response/redesign, same-lineage)** delivers **taxonomy v3**: it replaces the flat seven-box menu with a **three-axis descriptor** — Axis A *control-rights bundle* (use / withdrawal / management / exclusion / alienation / residual / override; the Domain-2 steering + conversion loci), Axis B *enforceability/robustness profile* (Ostrom design principles + conversion-pressure resistance; now constitutive), and Axis C an *acknowledged-normative form overlay* owned by Principles (de-skewed to name corporate-fiduciary, rentier-absentee, state-security, open-access, use-right; collective-dividend demoted to redistributive; "dedication" dissolves into A+B+C). v3 answers all six Round 2 falsifications, re-diagnoses the Taylor case (post-dicts the conversion via retained alienation/override + low B), and ships a six-claim set (v3-C1…C6). Placement: A+B → Systems Framework, C → Principle 5. **Integration is gated on a confirmatory cross-lineage Round 4.** **Round 4 (June 9, 2026 — confirmatory cross-lineage; Grok 4.3, Gemini 3.1 Pro, GPT-5.5, blind; 3/3) FALSIFIED v3:** all three falsified the leverage / durability / neutrality / determinacy claims (A2/A3/A4/A6), left A1/A5 falsified-leaning, and judged the three-axis split itself an *immunizing / anti-falsifiability* move — with the bundle-of-rights spine found parochial and low-leverage (GPT-5.5 grounding it in Hohfeld + Henry Smith's "property is not just a bundle of rights"). **Integration BLOCKED;** the falsification reaches back to #21 Deliverable 2 (do NOT annotate #21 as "superseded by v3" — v3 is dead). Survivors harvested for Problem-Map Domains 2/10: a transparency / standing / immunity rights cluster (= Domain 2's core), a negative/regulatory-control lever, "durability is political economy, not a checklist," and opacity as the live mechanism. **Round 5 (June 9, 2026 — Disposition: harvest & pivot, CLOSED):** steward chose branch (1); the taxonomy line is closed and the project adopts no ownership taxonomy. The survivors were folded into Problem Map [Domain 2](../../PROBLEM_MAP.md#2-money-credit-and-capital-allocation-steer-the-economy-in-ways-most-people-cannot-see-or-influence) and [Domain 10](../../PROBLEM_MAP.md#10-wealth-and-power-are-concentrating-faster-than-governance-can-respond); the method lesson became [Adversarial Review Protocol](../process/adversarial-review-protocol.md#5-standing-questions-for-all-reviewers) standing question 6 (falsifiability under revision); and a content guardrail (no bundle-of-rights master frame for relational/customary tenure) was recorded. #21's Deliverable 2 taxonomy is left un-validated/not adopted; #21 not reopened. |
| **Status** | **CLOSED (harvested) — June 9, 2026.** Rounds 1–4 complete; **v3 FALSIFIED** on the confirmatory cross-lineage pass (Grok 4.3 + Gemini 3.1 Pro + GPT-5.5, blind; **3/3**) — all three judged the three-axis split an **immunizing / anti-falsifiability move**, falsified A2/A3/A4/A6 (A1/A5 falsified-leaning), and found the bundle-of-rights spine itself parochial (GPT-5.5 grounding it in Hohfeld + Henry Smith). **Disposition (Round 5): branch (1) — harvest & pivot.** The project adopts **no** ownership taxonomy; nothing is integrated into SF/PM as a taxonomy. Survivors landed: Problem Map [Domain 2](../../PROBLEM_MAP.md#2-money-credit-and-capital-allocation-steer-the-economy-in-ways-most-people-cannot-see-or-influence) (engineered opacity / fragmented control; the transparency-standing-immunity rights cluster = Domain 2's core) + [Domain 10](../../PROBLEM_MAP.md#10-wealth-and-power-are-concentrating-faster-than-governance-can-respond) (durability is political economy, not legal robustness; portfolio-scale concentration); [Adversarial Review Protocol](../process/adversarial-review-protocol.md#5-standing-questions-for-all-reviewers) standing question 6 (falsifiability under revision); and a recorded guardrail (no bundle-of-rights master frame for relational/customary tenure). #21's Deliverable 2 taxonomy left **un-validated / not adopted**; #21 not reopened. |

---

### 29. [Principle 2 and the Solvable-vs-Perennial Boundary — Exchange](principle-2-solvable-vs-perennial-boundary-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does hammering the Brooks / communitarian challenge to Principle 2 yield *competing principles* or *sharpen the existing ones* — specifically: should P2 name both the incumbent's fatalism error and the reformer's overreach error; can "avoidable" ([Foundational Commitment 2](../../FOUNDATIONAL_COMMITMENTS.md#2-essential-needs-should-not-be-held-hostage-to-avoidable-scarcity)) be operationalized with the three-flavor sort; should dignity (P1) be split from flourishing with an agency-preservation clause; is meaning/belonging an under-weighted first-order civic good; and is the "navigated vs. solved" fork irreducible? |
| **Depends on** | [Meaning Crisis, Scientism, and Structural Accountability riff §3 / §3.bis](../explorations/meaning-crisis-scientism-and-structural-accountability-riff.md#3bis-the-anti-structural-view-as-a-competing-principle-set-steelman-and-what-it-sharpens), [Modern Wisdom #1109: Brooks digest](../../sources/source-modern-wisdom-1109-brooks-digest.md), [Principle 2](../../PRINCIPLES.md#2-essential-needs-should-not-be-held-hostage-to-avoidable-scarcity) + [Principle 1](../../PRINCIPLES.md#1-dignity-is-inherent-and-unconditional) + [Foundational Commitment 2](../../FOUNDATIONAL_COMMITMENTS.md#2-essential-needs-should-not-be-held-hostage-to-avoidable-scarcity) + [Problem Map](../../PROBLEM_MAP.md), [Verifiers for Reality riff (three-flavor sort)](../explorations/verifiers-for-reality-riff.md#7-three-flavors-of-no-verifier), [Sandel](../../sources/source-sandel-market-morality-digest.md) / [Lindert](../../sources/source-lindert-growing-public-digest.md) / [Argentina-Milei](../../sources/source-argentina-milei-reforms-digest.md) digests, [Exchange #21](government-overreach-ownership-ratchet-exchange.md) + [#23](principle-5-revision-exchange.md) (bounded-governance consistency), [Exchange #27](discovery-principle-develop-leg-exchange.md) (belonging frontier), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md) |
| **Produced** | New exchange opened (graduated from the Meaning Crisis riff §3.bis). Round 1 states the falsifiable claim set **E29-C1…C5** with falsification conditions and five reserved candidate adopt-targets (P2 two-sided boundary clause; FC2 three-flavor avoidability note; P1 dignity-vs-flourishing + agency-preservation clause; a Problem-Map belonging articulation; a named standing tension), and produces an Option A/B/C adversary packet (communitarian + welfare-economist + structural-left lenses) for an independent-lineage Round 2. Nothing adopted; same-lineage, not adversarially tested. |
| **Status** | Active; Round 1 complete; Rounds 2–N reserved. |

---

### 30. [Demand-Side Misinformation: Meaning Deficit as a Driver of Conspiracy Belief — Exchange](demand-side-misinformation-meaning-deficit-exchange.md)

|  |  |
| --- | --- |
| **Question** | Does the **demand-side** theory of misinformation (people reach for conspiracy to answer an unmet *coherence/meaning* need, so "throwing data" fails) survive contact with the project's **supply-side** account ([Principle 14](../../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods), [Problem Map §3](../../PROBLEM_MAP.md#3-information-ecosystems-are-fragmented-and-easily-manipulated), [Social Slop #20](social-slop-information-integrity-exchange.md)), is it distinct from generic motivated reasoning, and does it earn any corpus change beyond a note? |
| **Depends on** | [Meaning Crisis riff §6.1](../explorations/meaning-crisis-scientism-and-structural-accountability-riff.md#6-what-survives-the-adversary) (the portable idea) + [§3 guardrail](../explorations/meaning-crisis-scientism-and-structural-accountability-riff.md#3-the-structural-collision-anti-structural-individualism-vs-principle-2), [Modern Wisdom #1109: Brooks digest, Cluster 2](../../sources/source-modern-wisdom-1109-brooks-digest.md), [Principle 14](../../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods) + [Problem Map §3](../../PROBLEM_MAP.md#3-information-ecosystems-are-fragmented-and-easily-manipulated), [Exchange #20 (Social Slop)](social-slop-information-integrity-exchange.md) (supply-side; subsumed into #25), [Exchange #25 (Shared Mirror)](shared-mirror-see-layer-exchange.md) (M2 mirror ≠ fact-checker; its hold governs), [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md) |
| **Produced** | New exchange opened (graduated from the Meaning Crisis riff §6.1). Round 1 states claim set **E30-C1…C5** with falsification conditions (demand side real and non-negligible; complement-not-substitute and distinct from motivated reasoning; laundering guardrail required; intervention changes — context-restoration over fact-checking; modest "note, not doctrine" placement mirroring #20), with reserved adopt-targets (a P14 / PM §3 demand-side note; harvest into #25's M-claim set) and an Option A/B/C adversary packet. Nothing adopted; same-lineage, not adversarially tested. |
| **Status** | Active; Round 1 complete; Rounds 2–N reserved. |

---

### 31. [Abundance vs. "Discipline Capital" — Which Bottleneck Binds?](abundance-vs-discipline-capital-bottleneck-exchange.md)

|  |  |
| --- | --- |
| **Question** | Are the *Abundance* (Klein & Thompson) "proceduralism / veto points" diagnosis and the Slobodian (*Muskism*) "discipline capital, don't clear veto points" diagnosis **rival** explanations of one bottleneck, **complementary** constraints that bind at different points in the value chain (build-side vs. allocation-side), or **nested** — and does the project's bounded-governance doctrine over-weight the proceduralist lever and under-weight the capital-allocation lever? |
| **Depends on** | [Muskism digest](../../sources/source-weekly-show-stewart-slobodian-muskism-digest.md) (Cluster 8 discipline-capital; the tension flag) + [*Abundance* digest](../../sources/source-klein-thompson-abundance-digest.md) (proceduralist diagnosis + its own "silence on power" note), [Exchange #21](#21-government-overreach-ownership-as-transition-and-the-ratchet-problem--exchange) (the bounded-governance doctrine under pressure), [Exchange #28](#28-ownership-taxonomy--systems-framework--exchange-f2) (the Domain 2/10 capital-side survivors that C3 turns on), [Exchange #11](#11-ai-commonwealth-vs-ai-governance--exchange) (downstream consumer), [Suits digest constitutionalism thread](../../sources/source-suits-grasshopper-digest.md#the-lusory-attitude-constitutionalism-and-the-better-game-interpretive--added-june-14-2026) (who-holds-the-pen discipline for C4), [Acemoglu & Autor digest](../../sources/source-weekly-show-stewart-ai-future-of-work-digest.md), [Problem Map](../../PROBLEM_MAP.md) Domains 2/10/15/5/1/4 + [Principles](../../PRINCIPLES.md) §2/§4/§5/§13/§17, [Adversarial Review Protocol](../process/adversarial-review-protocol.md), [Research Protocol](../process/research-protocol.md). |
| **Produced** | New exchange opened (graduated from the [Muskism digest](../../sources/source-weekly-show-stewart-slobodian-muskism-digest.md) interpretive notes). Round 1 states claim set **E31-C1…C5** with falsification conditions (C1 two distinct constraints not rivals — build-side proceduralism vs. allocation-side capital-indiscipline; C2 which binds is sector-dependent — housing→proceduralism, frontier-financialized sectors→capital discipline; C3 the #21 doctrine is lopsided toward the proceduralist lever; C4 the two are mutually corrective and "discipline capital" is inert/dangerous without bounded-governance — the Suits who-holds-the-pen trapdoor; C5 disposition = a synthesis note, not a new principle or rewrite) + four reserved adopt-targets, and produces an Option A/B/C adversary packet for an independent-lineage Round 2. **Round 2 (cross-lineage adversarial review, June 24, 2026):** four blind lineages (Gemini C(i) / GPT C(ii) / Grok C(iii)+verifier / Kimi adversary) + non-author Gemini synthesizer; **outcome — E31-C1…C5 does NOT survive:** firm BLOCKING on C1/C2/C5, C3 lopsidedness *descriptively* confirmed by all four but valence-contested (the crux), C4 most defensible (MAJOR); synthesizer **NO-GO**. **Steward disposition (June 24, 2026): REVISE — rebuild, not patch**, keeping round numbers incrementing. **Round 3 (same-lineage reframe):** from-scratch claim set **E31-C6…C10** — power-agnostic P4 test (C6), the one-sided capital-power lever gap (C7, the survivor sharpened), structural-vs-allocative discipline split (C8), a per-blockage binding-constraint diagnostic replacing sector labels (C9), and an operational-commitment-plus-deciding-test disposition replacing the cosmetic note (C10); China existence-proof explicitly de-weighted. **Round 4 (same-lineage pre-mortem, confidence = upper bound):** ran the four R2 lenses against C6…C10 and hardened to **v2** (scope+scale bound on C6; capture-resistant design constraint on C7; bright-lined (a)/(b) with allocative steering kept open behind an extraordinary P4 bar on C8; pre-registered counterfactual + procedural-first default on C9; triggered decision rule replacing the open fork on C10). **Round 5 (cross-lineage adversarial review of the v2 set, June 24, 2026):** roles rotated to fresh families + non-author OpenAI synthesizer (arm's-length); **outcome — E31-C6…C10 v2 also does NOT survive: consolidated BLOCKING on all five (A1…A5); second consecutive NO-GO.** Every hardening move was cut through (one-test framing collapses across mechanisms; "capture-resistant" reads as an unfalsifiable shield; the structural-vs-allocative bright line is gerrymanderable; the counterfactual's procedural-first default is "default-rigged"). The cruxes have narrowed to two substantive open questions — can structural discipline bind concentrated capital without becoming allocative steering (C8), and are capture-resistant levers buildable (C7). **⚠️ Nothing in the exchange has been human-reviewed; all rounds are AI-generated.** Steward disposition pending (options: harvest as a preserved standing tension; route the two cruxes to external human review / evidence-gathering; or one narrowed rewrite). Nothing adopted; non-evidence for any core-document edit. |
| **Status** | Active; Rounds 1–5 complete (June 24, 2026 — two cross-lineage adversarial rounds, two NO-GOs: original E31-C1…C5 failed Round 2, rebuilt E31-C6…C10 v2 failed Round 5); steward disposition pending; not yet human-reviewed (all rounds are AI-generated); Rounds 6–8 reserved. |

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
  │     ├─► #17 Practitioner Critique & AI Provenance          │
  │           ◄── #6 + #7 + #8 + P-020 + website memo entry    │
  │     ├─► #18 Formation Document Comparative Analysis        │
  │     │     ◄── Principles + comparative corpus + protocol   │
  │     │
  │     ├─► #19 Formation Document Initial Findings Adv. Rev.  │
  │     │     ◄── #18 + comparative corpus synthesis + ARP     │
  │     │
  │     └─► #20 Social Slop & Information Integrity            │
  │           ◄── #18 + #19 + Principles §14 + PM §3          │
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

  Source Digest: Modern Wisdom #1084 (Friedberg)
        │
        └─► #21 Government Overreach, Ownership & Ratchet Problem
              ◄── Source Digest + Principles §2/4/5/6 + PM §2/13/15
              ◄── #7 (recursive uplift) + #9 (debt legitimacy)
              ◄── ARP + HPTP
              (adversarial challenge to Principle 5 + ownership question)
              │
              ├─► #23 Principle 5 Revision (F1)
              │     ◄── #21 Round 5 v2 deliverable + Coherence Audit P2-2
              │     ◄── ARP + Reviewer Packet + Reviewer-as-a-Round Convention
              │     ◄── ROADMAP TODOs #1, #10, #11
              │     (adversarial pass + first live external-review round
              │      → v3 text → integration into PRINCIPLES.md §5
              │        and FOUNDATIONAL_COMMITMENTS.md §5)
              │
              └─► #28 Ownership Taxonomy → Systems Framework (F2)
                    ◄── #21 Round 5 Deliverable 2 (v2 seven-category taxonomy)
                    ◄── ARP + Research Protocol + ROADMAP TODO #1 (F2)
                    (Round 1 framing + claims F2-C1…C5; adversarial Round 2
                     reserved for independent lineage → SF / PM edits)

  Source Digest: The Weekly Show (Stewart / Acemoglu / Autor)
        │
        ├─► #11 AI Commonwealth vs. AI Governance (Round 1 input)
        │     ◄── Source Digest + AI Governance Practice digest
        │     ◄── Principles §3/§6/§10 + PM §6/§12/§14
        │     (pro-worker AI; data-extraction economy; UBC + tax rebalance)
        │
        └─► #21 F2 / F4 follow-ups (when opened)
              ◄── reinforces direction-of-technology framing,
                  collective-dividend ownership category, frontier-AI worked example

  Feedback Record: Childcare Licensing Practitioner (April 2026)
        │
        └─► #22 Entry-Trust Failure with a Domain-Expert Practitioner
              ◄── Anchor feedback record + #8 (deferred plain-language work)
              ◄── #17 (entry-trust layer + Priority 6/7 pathway)
              ◄── #14 / #16 (permitting-domain practitioner adjacency)
              ◄── Principles §1/§2/§10/§14 + PM §3/§13
              ◄── Friedberg digest Steward Observation 3
                  + Stewart/Acemoglu/Autor digest Cluster 8 (meritocracy critique)
              (cognitive-resolution mismatch as a distinct entry-trust failure mode)

  Exploration: Constitutional Ecology and Coordination Architecture Riff (v2)
        │
        └─► #24 Coordination Architecture Reframe — Exchange (Path β)
              ◄── Riff v2 §7.ter (the five testable claims)
              ◄── Riff v2 §5.1.bis (coherence check)
              ◄── Riff v2 §2.3, §2.5, §3.5, §5.4, §11.6 (sourced support)
              ◄── Reciprocity riff v5 (downstream per riff §6.2)
              ◄── Adversarial Review Protocol (Options A + C)
              ◄── V-Dem 2026 / Freedom House 2026 / Bright Line Watch
                  + Little & Meng 2024 contrarian (claim C4 evidence)
              (Path β of the reframe; first structured adversarial test
               of the candidate constitutional-ecology framing)

  Exploration: Shared Mirror and Collective Self-Perception Riff
        │
        └─► #25 Shared Mirror as the Upstream "See" Coordination Layer — Exchange
              ◄── Shared-mirror riff §4 (the bet) + §4.5 (mirror ≠ fact-checker)
              ◄── #20 Social Slop (generalized) + #24 coordination architecture
                  (feeds a concrete "see" coordination primitive; downstream of #24)
              ◄── Principles §14/§13/§4 + PM §3/§15
              ◄── Adversarial Review Protocol (R2) + Research Protocol (tiering)
              (tests whether collective self-perception is a distinct upstream
               coordination layer feeding the Phase 3 front door)
              │
              └─► #26 Coordination Triad (See / Decide / Act) — Combined Exchange (Path C)
                    ◄── Triad riff §10 (combined claim set) + §10.1 (design principle)
                        + §10.5 T-series + §10.12 (T2-systematic) + §10.13 (T4b-corpus)
                    ◄── #25 (see leg M1–M5 imported at status; the #25 hold governs)
                    ◄── #24 (diffuse-sovereignty layers; T3 tests distinctness over it)
                    ◄── #20 Social Slop (one see-layer failure mechanism, subsumed)
                    ◄── Principles §14/§17/§4/§13 + PM §3/§15
                    ◄── Adversarial Review + Research + Historical Parallel Test
                        + Reviewer-as-a-Round Convention
                    (tests the See/Decide/Act triad as ONE object — combine vs. Path A;
                     combine-rationale on T2 supported + T3 lean-supportive, NOT
                     strong T4b falsified; no doctrine / Phase 3 promotion; #25 hold)

  Exploration: Discovery Principle and Moral Architecture Riff (v1.2)
        │
        └─► #27 Discovery Principle / Develop-Leg — Exchange
              ◄── Riff v1.2 §1.4/§2.1/§2.4/§2.5/§4.2/§5/§5.3/§6/§8/§9
              ◄── Develop-leg research-grounding digest (same-lineage, pending verification)
              ◄── #25 (Round-1→reserved-adversarial model; the #25 hold governs)
              ◄── #26 / #24 (placement target: develop beneath/beside see/decide/act)
              ◄── #20 Social Slop (one moral exercise, subsumed)
              ◄── Comparative Alignment Protocol (cross-lineage Round 1)
                  + Adversarial Review Protocol (R2 run cross-lineage, Options A+C+D)
              (Round 1 = synthesis of 3 lineages: Opus baseline + GPT 5.5 + Gemini 3.1;
               24 claims S1–S24 (S22–S24 = same-lineage coverage scan);
                      cross-scale transfer + dose-response = crux;
               §2.5 collapse-dynamics demoted, pluralism-as-non-correlation kept;
               Round 2 = 3-lineage adversarial HOLD (GPT/Grok/Gemini); S17+S18 decisive fails;
               Round 4 = response/v2: HOLD → live test (claim → testable civic design hypothesis;
                      S17 recast with a pre-registered falsifier; project's own review = first rung);
               no promotion; #25 hold; LIVE hold; §4.6 test-design memo DRAFTED (design only, not run)
                      — F1–F6 pre-registered falsifiers + agent-automation architecture (persona × lineage);
               external-human Round 3 deferred)

  Exploration: Meaning Crisis, Scientism, and Structural Accountability Riff
        │  (Source Digest: Modern Wisdom #1109 — Arthur Brooks)
        │
        ├─► #29 Principle 2 and the Solvable-vs-Perennial Boundary — Exchange
        │     ◄── Meaning Crisis riff §3 + §3.bis (steelman → rival principle-set R1–R5)
        │     ◄── Principle 2 + Principle 1 + Foundational Commitment 2 + Problem Map
        │     ◄── Verifiers riff (three-flavor sort) + Sandel/Lindert/Argentina digests
        │     ◄── #21 / #23 (bounded-governance consistency) + #27 (belonging frontier)
        │     ◄── Adversarial Review Protocol (R2 reserved for independent lineage)
        │     (Round 1 claims E29-C1…C5 + adopt-targets; adversarial Round 2 reserved)
        │
        └─► #30 Demand-Side Misinformation (Meaning Deficit) — Exchange
              ◄── Meaning Crisis riff §6.1 (the portable idea) + §3 guardrail
              ◄── Principle 14 + Problem Map §3
              ◄── #20 Social Slop (supply-side; subsumed) + #25 Shared Mirror (M2; hold governs)
              ◄── Adversarial Review + Research Protocol (T2 balanced sourcing)
              (Round 1 claims E30-C1…C5; adversarial Round 2 reserved)

  Source Digest: The Weekly Show (Stewart × Slobodian — Muskism)
        │
        └─► #31 Abundance vs. "Discipline Capital" — Which Bottleneck Binds?
              ◄── Muskism digest (Cluster 8 discipline-capital) + Abundance digest (proceduralism + "silence on power")
              ◄── #21 (bounded-governance doctrine — lopsidedness test) + #28 (Domain 2/10 capital-side survivors)
              ◄── #11 (downstream: discipline capital + SWF caveat)
              ◄── Suits digest (who-holds-the-pen discipline for C4) + Acemoglu/Autor (China-as-existence-proof)
              ◄── Problem Map §2/§10/§15/§5/§1/§4 + Principles §2/§4/§5/§13/§17
              ◄── Adversarial Review (R2 Options A+C) + Research Protocol
              (Round 1 claims E31-C1…C5: rival vs. complementary vs. nested bottlenecks;
               adversarial Round 2 reserved — abundance-liberal + public-choice + structural-left lenses)
```

---

## Cross-repo artifacts

Several exchanges produced or depend on documents in the [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org) repository:

| Exchange | civicblueprint.org artifact |
| --- | --- |
| #3 (Next Steps) | [Website Phase 1 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_1_BRIEF.md) — Phase 1 scope and launch plan |
| #3 (Next Steps) | [Homepage Copy Draft](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/HOMEPAGE_COPY_DRAFT.md) — draft homepage copy |
| #6 (Housing vs. AI) | [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) (project-2028) and `website/src/app/docs/[...slug]/page.tsx` (civicblueprint.org renderer) — comparative memo and public docs surface |
| #6 (Housing vs. AI) | `docs/PROOF_OF_USEFULNESS_MEMO_01_HOUSING_PERMITTING.md` — superseded housing-only draft |
| #10 (Housing Financialization) | [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) — public memo whose housing framing this exchange reopens |
| #11 (AI Commonwealth vs. Governance) | [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) — public memo whose AI framing this exchange sharpens |
| #12 (Housing Parallel Test) | [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) — public memo whose housing claims this exchange tests |
| #17 (Practitioner Critique & AI Provenance) | `website/src/components/Hero.tsx`, `website/src/components/MemoFeature.tsx`, `website/src/app/docs/[...slug]/page.tsx` — website orientation and provenance legibility surfaces targeted by this exchange |
| #20 (Social Slop & Information Integrity) | [Website Phase 2 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_2_BRIEF.md), [Homepage Copy Draft Phase 2](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/HOMEPAGE_COPY_DRAFT_PHASE_2.md) — Phase 2 alignment narrative whose convergence claim this exchange stress-tests from the information-integrity angle |
| #22 (Entry-Trust Failure — Domain-Expert Practitioner) | [Website Phase 2 Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_2_BRIEF.md), [Homepage Copy Draft Phase 2](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/HOMEPAGE_COPY_DRAFT_PHASE_2.md) — exchange's findings will likely feed Phase 2 layer-zero / layer-one design once produced |
