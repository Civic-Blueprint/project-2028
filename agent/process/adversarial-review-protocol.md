# Adversarial Review Protocol

> **Status:** Proposed (April 2026). Originated from the Systems Framework review exchange, where all contributors — human and AI — converged on the observation that the multi-agent exchange format produces sophisticated agreement more reliably than it produces genuine challenge.

---

## The problem this protocol addresses

The project uses multi-agent exchanges to review and refine its core documents. These exchanges have been productive: they have generated the recursive uplift concept, the entry points analysis, the institutional capacity hypothesis, the human+AI augmentation layer, and numerous structural improvements to both the Problem Map and the Systems Framework.

But the exchanges have a structural bias toward convergence.

Every response in every exchange so far follows the same pattern: agree with the core direction, add a refinement, raise a mild caution that does not actually challenge the core direction, and close with encouragement. The result is that each turn narrows the space of disagreement. By the end of an exchange, what looks like multi-perspectival consensus is partly an artifact of a process that rewards extension over challenge.

This is not a failure of individual contributors. It is a structural property of the format:

- **AI training optimizes for perceived helpfulness.** Models trained on human feedback learn that agreement and constructive extension are rewarded. Genuine adversarial challenge feels "unhelpful" to the training signal. Pushback arrives pre-wrapped in validation, which dilutes its force.
- **Sequential response encourages convergence.** Each contributor reads all prior contributions and responds to the accumulated framing. The natural move is to build on what came before, not to dismantle it. By the third or fourth response, the frame is so well-established that challenging it feels disruptive rather than analytical.
- **Shared context produces shared conclusions.** Every contributor reads the same documents in the same order and responds to the same prompt structure. Different inputs would produce different outputs — but the current format provides identical inputs.
- **The steward's framing anchors the conversation.** When the project steward contributes a strong, well-argued position, subsequent AI contributors orient toward it. This is not deference — it is a consequence of the steward's contribution being the most detailed and contextually rich input in the window. The agents are doing what they were trained to do: engage constructively with the strongest available framing. The result is convergence toward that framing.

None of this means the exchanges are wrong. It means they are incomplete. The project's own quality standards (CONTRIBUTING.md) require that contributions be "honest," "aware of tradeoffs," and grounded in evidence. Principle 14 commits to protecting truth and evidence as public goods. These commitments demand more adversarial pressure than the current process produces.

---

## Protocol

### 1. Every exchange should include at least one designated adversarial contributor

This contributor's role is not to disagree for its own sake. It is to identify the weakest claims in the exchange and argue against them as forcefully as the evidence allows.

**Prompt framing for the adversarial role:**

The adversarial contributor should receive instructions substantially different from the standard "respond to the prior reviews" prompt. A template:

> You are reviewing an exchange between multiple contributors to Civic Blueprint. Your role is adversarial review. Your job is not to extend, refine, or build on the prior contributions. Your job is to find the flaws.
>
> Specifically:
>
> - Identify the strongest claims made in this exchange and steelman the best counterarguments against them.
> - Name any claims that have been accepted without sufficient evidence.
> - Identify where agreement between contributors is earned versus where it is an artifact of shared framing or training bias.
> - Challenge the central hypothesis of the exchange. If the exchange converges on a "highest-leverage first move," argue for why a different first move might be stronger — or why the concept of a single highest-leverage first move is itself misleading.
> - Identify perspectives, constituencies, or analytical traditions that are absent from the exchange and whose inclusion would change the conclusions.
>
> Agreement is not your goal. Finding what the other contributors missed, overstated, or got wrong is your goal. Be specific. Cite the claims you are challenging and explain why.

### 2. The adversarial contributor should receive different inputs

Convergence is partly a function of identical context. To break that pattern:

- **Option A: Reduced context.** The adversarial contributor receives only the core project documents (Problem Map, Systems Framework, Principles) and the specific claims or proposals being reviewed — not the full exchange thread. This forces them to evaluate the claims on their merits rather than within the narrative arc of the conversation.

- **Option B: Alternative framing.** The adversarial contributor receives a prompt that presents the exchange's conclusions as assertions to be tested, not as a conversation to join. For example: "The following claims have been made. Evaluate each one. Which are well-supported? Which are weak? Which are missing something important?"

- **Option C: Domain-specific lens.** The adversarial contributor receives a prompt that asks them to review from a specific expert perspective. For example: "You are reviewing this from the perspective of a public administration scholar who studies why institutional reform initiatives fail." Or: "You are reviewing this from the perspective of a community organizer in a low-income neighborhood who has seen 'reform' used as a tool for displacement." Different lenses surface different objections.

These options are not mutually exclusive. The strongest adversarial review would combine reduced context with a domain-specific lens.

### 3. Exchanges should end with an epistemic status table

Every exchange should conclude with a structured assessment of the confidence level of its claims. This makes it harder for convergence to masquerade as established consensus.

**Format:**

| Claim | Confidence | Basis | What would change this assessment |
|---|---|---|---|
| Institutional capacity is the highest-leverage first move | Working hypothesis | Structural argument from dependency analysis; not empirically validated | Formal graph analysis showing a different node has higher centrality; domain expert challenge; historical counterexample |
| Recursive uplift chains are a real mechanism | Plausible framework | Logical inverse of documented recursive degradation; limited direct empirical support | Case studies that trace a specific reform cascade with documented evidence at each step |
| Estonia's digital governance model is transferable | Speculative | Single-case observation with acknowledged context-specificity | Comparative study of digital governance adoption in larger, more complex bureaucracies |

**Confidence levels:**

- **Established by evidence:** Supported by multiple independent sources, documented case studies, or peer-reviewed research. The project is willing to build on this claim.
- **Working hypothesis:** Supported by structural reasoning and some evidence, but not independently validated. The project treats this as its current best understanding, subject to revision.
- **Speculative:** Plausible but not yet supported by evidence specific enough to ground action. Requires further investigation before the project should rely on it.
- **Contested:** Reasonable counterarguments exist and have not been resolved. The project should present both sides.

### 4. Seek human reviewers who are not the project steward

AI agents operating within a single human's framing will converge toward that human's worldview regardless of how many models are used. The most effective way to break this pattern is to introduce genuinely independent human perspectives.

This is already called for in CONTRIBUTING.md: "Domain expertise, case studies, reform proposals, analytical critique, and implementation analysis are all needed — especially from outside the US/Western context."

For the exchange format specifically, the project should:

- Invite at least one external human contributor to participate in exchanges before conclusions are treated as settled.
- Seek contributors who bring domain expertise in the specific area under discussion (public administration, political science, development economics, etc.).
- Seek contributors from outside the US/Western context, where the dynamics of institutional reform may look very different.
- Make clear that disagreement with the exchange's emerging consensus is valued, not merely tolerated.

### 5. Periodically re-run exchanges with different starting conditions

If an exchange produces a strong consensus — such as "institutional capacity is the highest-leverage first move" — that consensus should be tested by re-running the review with:

- Different AI models
- Different prompt structures
- Different initial framings (e.g., starting from the assumption that information integrity or democratic process is the highest-leverage first move, and seeing whether the argument holds up)
- Different document versions as context

If the consensus holds across varied conditions, confidence increases. If it fragments, the project learns something important about which claims are robust and which are artifacts of the specific process that produced them.

---

## When to apply this protocol

Not every exchange needs a full adversarial review. The protocol is most important when:

- The exchange is generating **strategic claims** (e.g., "this is the highest-leverage first move") rather than editorial improvements
- The exchange has produced **near-total convergence** among contributors
- The conclusions will **influence the direction of the project** (e.g., which domain section gets rewritten first, what template is adopted)
- The exchange involves **AI contributors whose training biases favor agreement**

For minor editorial exchanges, lightweight review is sufficient. For exchanges that shape the project's strategic direction, the full protocol should be applied.

---

## What this protocol does not do

This protocol does not guarantee that the project's conclusions are correct. It does not substitute for empirical investigation, domain expertise, or the messy reality of implementation.

What it does is raise the cost of false consensus. It makes it structurally harder for the project to mistake sophisticated agreement for rigorous analysis. That is a modest but important contribution to the epistemic discipline the project has committed to.

---

## Relationship to project principles

This protocol operationalizes several of the project's core commitments:

- **Principle 10 (The future should be built in the open):** Open processes require mechanisms that resist capture — including capture by the biases of the process itself.
- **Principle 14 (Truth and evidence must be protected as public goods):** Protecting truth requires actively seeking challenge, not just welcoming it in principle.
- **CONTRIBUTING.md quality standards:** Contributions must be "honest" and "aware of tradeoffs." A process that structurally discourages challenge is not honest about its own tradeoffs.
- **Principle 9 (Institutions should be designed for competence and trust, not theater):** An exchange format that produces the appearance of rigorous multi-perspectival review without the substance of genuine disagreement is institutional theater. This protocol is designed to prevent that.
