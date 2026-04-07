# Historical Parallel Test Protocol

> **Status:** Proposed (April 2026). Originated from the [Review Protocol Design Exploration](../exchanges/review-protocol-design-exploration.md), which identified the project's lack of empirical grounding as a structural weakness. The project's reform proposals are currently based on structural reasoning and limited case studies. This protocol provides a repeatable method for testing those proposals against historical evidence.

---

## The problem this protocol addresses

The Systems Framework proposes reform sequences, leverage hypotheses, entry-point conditions, and recursive uplift chains. These proposals are grounded in structural reasoning — the logic of dependencies, feedback loops, and cascading effects. That reasoning is sound as far as it goes, but structural reasoning alone cannot tell you whether a reform will succeed. History can.

The project's current approach to historical evidence is ad hoc. The Systems Framework mentions specific cases (Estonia's digital governance, Singapore's institutional capacity) when they support the analysis, but does not systematically search for cases that might undermine it. This creates a selection bias: the historical evidence in the documents confirms the project's hypotheses because the project selected evidence that confirms them.

This is not deliberate. It is a natural consequence of building an analytical framework first and looking for evidence second. But it means the project's confidence in its proposals rests on structural logic that has not been stress-tested against the record of what has actually happened when similar reforms were attempted.

The historical parallel test addresses this by requiring that the project's highest-confidence reform proposals be accompanied by historical cases — including cases where structurally similar reforms failed.

---

## Protocol

### 1. Trigger

A historical parallel test should be performed when:

- **A reform sequence in the Systems Framework reaches "working hypothesis" confidence.** This is the threshold at which the project begins to treat a proposal as its current best understanding. At that point, the proposal should be grounded in at least some historical evidence beyond the cases already cited in the document.

- **The project proposes a specific entry-point condition or recursive uplift chain.** These are the project's most consequential claims — they determine where the project recommends starting. They deserve the most rigorous empirical check.

- **An adversarial review challenges the feasibility of a proposal.** If the challenge is "this has been tried and it failed," the historical parallel test is the appropriate response: find the cases, understand what happened, and assess whether the project's proposal addresses the failure modes.

### 2. Scope

The test does not require exhaustive historical research. It requires a structured search for **2-3 historical cases** where a reform structurally similar to the one being tested was attempted. "Structurally similar" means the reform tried to solve a similar kind of problem through a similar kind of mechanism — regardless of the specific domain, country, or era.

The test searches for two kinds of cases:

- **Supporting cases:** Reforms that succeeded using a mechanism similar to the one the project proposes. What conditions enabled success? Are those conditions present in the contexts the project is targeting?

- **Challenging cases:** Reforms that failed despite using a similar mechanism, or that produced unintended consequences. What went wrong? Does the project's proposal account for those failure modes?

Finding only supporting cases is a red flag, not a green light. It suggests the search was not broad enough or the structural similarity criterion was too narrow.

### 3. Process

**Step 1: Define the structural claim.**

Before searching for parallels, state precisely what the reform proposes and what mechanism it relies on. Strip away domain-specific details to identify the underlying structure.

Example: The Systems Framework proposes that state-level preemption of local zoning authority is a high-leverage reform for housing production. The structural claim is: "centralizing rule-making authority at a higher level of government, overriding local veto power, will unblock a system that local actors have captured."

**Step 2: Search for historical parallels.**

Search for cases where the same structural mechanism was attempted. The search should span:

- Different domains (not just housing — any case where centralized authority overrode local blocking)
- Different countries and eras (reforms in different governance contexts)
- Different outcomes (successes and failures)

**Prompt framing:**

> The following reform proposal is from Civic Blueprint's Systems Framework:
>
> [Insert the specific proposal, including the mechanism it relies on and the structural claim it makes.]
>
> Identify 2-3 historical cases where a structurally similar reform was attempted — in any country, at any scale, in any era. "Structurally similar" means the reform tried to solve a similar kind of problem through a similar kind of mechanism. Include at least one case where the reform succeeded and at least one where it failed or produced unintended consequences.
>
> For each case:
>
> - **Context:** When and where was the reform attempted? What were the conditions?
> - **Mechanism:** What structural mechanism did the reform rely on? How is it similar to the Civic Blueprint proposal?
> - **Outcome:** What happened? Did the reform achieve its goals? What were the unintended consequences?
> - **Failure modes:** If the reform failed, what caused the failure? Does the Civic Blueprint proposal account for those failure modes?
> - **Preconditions:** What conditions were necessary for the reform to work (or, in failure cases, what conditions were absent)? Are those conditions present in the contexts Civic Blueprint is targeting?
> - **Transfer assessment:** How confident should we be that this historical case is genuinely parallel to the Civic Blueprint proposal? What are the most important differences?

**Step 3: Assess the evidence.**

After gathering the cases, assess what they collectively tell the project:

- Do the cases support the proposal's feasibility, challenge it, or produce mixed evidence?
- Do the failure cases reveal failure modes that the proposal does not address?
- Do the success cases depend on conditions that the proposal assumes but does not verify?
- Does the historical evidence change the project's confidence in the proposal? If so, in which direction?

### 4. Output

The test produces a **historical grounding section** that is appended to (or cross-referenced from) the relevant Systems Framework entry. The section includes:

- The structural claim being tested
- The 2-3 historical cases, each summarized in the format above
- A collective assessment of what the cases teach
- An updated confidence level for the proposal, citing the historical evidence as basis

**Each case must be explicitly marked with its verification status:**

- **AI-generated (unverified):** The case was identified and summarized by an AI contributor. The factual claims have not been independently verified by a human with domain expertise. The project should not rely on the specific details until they are verified.
- **Human-expert-confirmed:** The case has been reviewed by a human contributor with relevant domain knowledge who confirms that the factual claims are accurate and the structural parallel is valid.
- **Published source confirmed:** The case is drawn from a specific, citable published source (academic paper, government report, journalistic investigation) that can be independently checked.

This verification requirement exists because AI agents can generate plausible-sounding historical narratives that are wrong in important ways — mischaracterizing context, overstating structural similarity, or conflating distinct events. Historical evidence that has not been verified is better than no historical evidence, but the project must be transparent about the difference.

### 5. Integration with the Systems Framework

Historical parallel sections are not standalone documents. They attach to specific proposals in the Systems Framework:

- Each reform sequence that reaches "working hypothesis" confidence should have a corresponding historical grounding section, either inline or as a linked appendix.
- The epistemic status table for the relevant exchange should cite the historical evidence and adjust confidence levels accordingly.
- If historical cases reveal unaddressed failure modes, those failure modes should be added to the Systems Framework's failure-mode analysis for the relevant domain.

---

## When to apply this protocol

**Always apply when:**

- A reform sequence is being promoted from "speculative" to "working hypothesis" confidence
- The project is making a specific recommendation about where to start (entry points, first moves, sequencing)
- An adversarial review challenges feasibility with "this has been tried and it failed"

**Consider applying when:**

- A case study is cited in the Systems Framework and treated as strong evidence — the parallel test checks whether the case is genuinely parallel or whether the structural similarity has been overstated
- The project is preparing material for public release — historical grounding increases credibility

**Skip when:**

- The proposal is still at "speculative" confidence and is being explored rather than advocated
- The structural mechanism is so novel that historical parallels are unlikely to exist (in which case, say so explicitly — the absence of precedent is itself informative)

---

## What this protocol does not do

The historical parallel test does not prove that a reform will succeed or fail. Historical cases are not controlled experiments. Context matters enormously, and no two reform situations are identical.

What the test does is raise the empirical bar. It forces the project to look beyond structural logic and ask: "When something like this has been tried, what actually happened?" That question disciplines the project's proposals in a way that pure analytical reasoning cannot.

The test also does not substitute for domain expertise. An AI agent can identify plausible historical parallels, but assessing whether the parallel is genuinely valid — whether the structural similarity holds at the level of detail that matters — requires someone who knows the domain. The verification requirement exists to make this limitation explicit.

---

## Relationship to other protocols

- **Adversarial Review Protocol:** The adversarial protocol challenges claims. The historical parallel test grounds claims in evidence. An adversarial reviewer who argues "this will fail" should be met with historical evidence, not just structural rebuttal. The two protocols are natural complements.
- **Coherence Audit Protocol:** Each historical parallel section added to the Systems Framework is new content that could introduce coherence drift. The coherence audit should check that historical grounding sections are consistent with the Principles and Problem Map.

---

## Relationship to project principles

- **Principle 14 (Truth and evidence must be protected as public goods):** The project's reform proposals should be grounded in the best available evidence, not just the best available reasoning. Historical grounding is a direct application of this commitment.
- **Principle 9 (Institutions should be designed for competence and trust, not theater):** Reform proposals that are not empirically grounded risk being institutional theater — intellectually impressive but practically unmoored. Historical testing is a competence check.
- **CONTRIBUTING.md quality standards:** Contributions must be "evidenced" and "aware of tradeoffs." The historical parallel test operationalizes both requirements for the project's most consequential claims.
- **CONTRIBUTING.md, Case studies section:** "Documented examples of what has worked, what has failed, and why. Real-world evidence is the backbone of credible system design." The historical parallel test is a structured method for seeking that evidence.
