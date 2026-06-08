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
| **Status** | Active discussion. Track 1 work is underway in [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org). Track 2 not yet started. |

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
| **Status** | Active discussion. Comparative memo drafted. The timescale objection raised in [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review) reopens part of this decision. |

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
| **Status** | Active discussion. |

---

### 10. [Housing Financialization as Upstream Capture — Exchange](housing-financialization-upstream-capture-exchange.md)

|  |  |
| --- | --- |
| **Question** | Should the framework explicitly treat housing financialization as a distinct upstream-capture mechanism alongside housing permitting and zoning, or widen the existing housing analysis without a separately named frame? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md) |
| **Produced** | Exchange opened. Initial questions captured around mechanism naming, balance between permitting and finance, metro vs. national claims, and whether the current public memo needs revision or a companion artifact. |
| **Status** | Active discussion. |

---

### 11. [AI Commonwealth vs. AI Governance — Exchange](ai-commonwealth-vs-governance-exchange.md)

|  |  |
| --- | --- |
| **Question** | Should the framework explicitly shift from an "AI governance" frame to an "AI commonwealth" frame centered on ownership, access, and public infrastructure, or preserve governance as the primary frame and incorporate these ideas more narrowly? |
| **Depends on** | [Exchange #6](#6-proof-of-usefulness-memo--housing-vs-ai-exchange), [Exchange #7](#7-proof-of-usefulness-memo--feedback-timescale-review), [Roadmap](../../ROADMAP.md), [Principles](../../PRINCIPLES.md), [Problem Map](../../PROBLEM_MAP.md), [Systems Framework](../../SYSTEMS_FRAMEWORK.md), [Proof-of-Usefulness Memo 01](../../memos/proof-of-usefulness-memo-01.md), [Source Digest — Stewart/Acemoglu/Autor (Weekly Show)](../../sources/source-weekly-show-stewart-ai-future-of-work-digest.md), [AI Governance Practice digest](../../sources/source-ai-governance-practice-digest.md) |
| **Produced** | Exchange opened. Initial questions captured around governance vs. commonwealth framing, timeline urgency, what counts as commonwealth infrastructure in AI, and whether existing public artifacts need reframing. **April 2026:** External evidence base added — the Stewart/Acemoglu/Autor digest provides the pro-worker AI directional frame, the data-extraction-economy critique, and a concrete commonwealth-style policy package (UBC + labor/capital tax rebalance + pro-worker R&D + wage insurance) ready to feed Round 1. |
| **Status** | Active discussion. External evidence curated; Round 1 not yet conducted. |

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
| **Produced** | New exchange opened. Structured comparative framework across six dimensions (recursive uplift potential, learning velocity, visibility, political durability, project credibility, informative failure). Identifies open questions including whether the comparison is actually a sequencing question rather than either/or. |
| **Status** | Active discussion. |

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
| **Produced** | Opened the first structured challenge to the comparative corpus. Identifies source-selection bias, genre mismatch, false-overlap inflation, modernity bias, and translation risk as the main failure modes to test before treating the corpus as evidence of broad values alignment. |
| **Status** | Active discussion. |

---

### 20. [Social Slop and Information Integrity — Exchange](social-slop-information-integrity-exchange.md)

|  |  |
| --- | --- |
| **Question** | Is "Social Slop" — engagement-optimized decontextualization that inflates method-level disagreements into apparent values-level conflicts — a named pattern the project should formally recognize, and how does it interact with Principle 14 (truth and evidence as public goods) and the alignment thesis? |
| **Depends on** | [Principles](../../PRINCIPLES.md) (§14 truth and evidence), [Problem Map](../../PROBLEM_MAP.md) (§3 information ecosystems), [Exchange #18](#18-formation-document-comparative-analysis--exchange) (convergence claim), [Exchange #19](#19-formation-document-initial-findings--adversarial-review) (adversarial challenge to convergence), [Phase 2 Website Brief](https://github.com/Civic-Blueprint/civicblueprint.org/blob/main/docs/WEBSITE_PHASE_2_BRIEF.md) |
| **Produced** | Exchange opened. Proposed definition of Social Slop as a distinct information-integrity phenomenon. Anchor case (WEF natural capital accounting repackaged as "monetize breathing") documented with full source-to-post transformation analysis. Core mechanism identified: fragment extraction → threat reframing → outcome erasure → method-as-values substitution → engagement packaging. Six open questions framed for next rounds. |
| **Status** | Active discussion. |

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
| **Status** | Active; **Rounds 1, 2, and 4 complete** (Round 2 = cross-lineage HOLD; Round 4 = response/v2 reframe to a testable civic design hypothesis, run ahead of the deferred external-human Round 3); **live hold** — the §4.6 [test-design memo](discovery-principle-develop-leg-test-design-memo.md) is **drafted (design only, not run)**; Round 5 reserved |

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
              └─► #23 Principle 5 Revision (F1)
                    ◄── #21 Round 5 v2 deliverable + Coherence Audit P2-2
                    ◄── ARP + Reviewer Packet + Reviewer-as-a-Round Convention
                    ◄── ROADMAP TODOs #1, #10, #11
                    (adversarial pass + first live external-review round
                     → v3 text → integration into PRINCIPLES.md §5
                       and FOUNDATIONAL_COMMITMENTS.md §5)

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
