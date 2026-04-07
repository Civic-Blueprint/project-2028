# Review Protocol Design Exploration

> **Status (April 2026):** Exploratory exchange. The project's [Adversarial Review Protocol](../process/adversarial-review-protocol.md) was designed to counteract the structural convergence bias of multi-agent exchanges. The [Principles — Adversarial Review Exchange](principles-adversarial-review.md) demonstrated that it works: alternating adversarial and constructive agents produced substantively different and more rigorous output than any prior exchange.
>
> This exchange asks a different question: **is the adversarial protocol the only kind of structured review the project needs?** Or are there other review postures — other "middle of the road" protocols, other lenses — that would surface different kinds of insight? The exchange proceeds in two passes: first, an open exploration of what other review modes might be valuable and how they would work; second, a self-application of the adversarial protocol to challenge the proposals from the first pass.

---

# Pass 1 — Open Exploration

> **Mode:** Standard contributor. Thinking through what review protocols or structured lenses could help build and refine this project, beyond the existing adversarial protocol.

---

## Starting observation: the adversarial protocol addresses one failure mode. The project has several.

The adversarial review protocol was born from a specific diagnosis: multi-agent exchanges converge too easily. Contributors agree, refine, extend — and the result is sophisticated consensus that may not be earned. The protocol fixes this by designating at least one contributor whose job is to challenge rather than build.

That is genuinely important. The [Principles exchange](principles-adversarial-review.md) proved it.

But convergence bias is not the only way a project like this can go wrong. Here are other failure modes that a review protocol could address:

1. **Abstraction drift.** The project's documents get more intellectually sophisticated over time without getting more practically grounded. Each exchange adds nuance, qualifications, and structural refinements — but the distance between the documents and any concrete action grows. No one is checking whether the analysis can survive contact with an actual reform effort.

2. **Audience blindness.** The project is written by and for people who think in frameworks, systems, and analytical prose. It has never been tested against audiences who think differently: practitioners who want to know "what do I do Monday morning?", activists who want to know "whose side is this on?", policymakers who want a two-page brief, or citizens who want to know "what does this mean for my life?"

3. **Internal coherence decay.** The project has four major documents plus a growing body of exchanges. As each document evolves, cross-references break, implicit assumptions diverge, and the documents stop talking to each other. No one is systematically checking whether the Principles, Problem Map, Systems Framework, and process documents still form a coherent whole.

4. **Gap blindness.** The project has a strong analytical frame, but that frame creates its own blind spots. Whatever falls outside the fourteen domains, outside the dependency model, outside the liberal-democratic tradition the Principles operate within — the project cannot see it. The adversarial protocol can catch some of this, but it works best when there is a specific claim to challenge. What about the things that were never claimed at all because no one thought to raise them?

5. **Implementation fantasy.** The project proposes reform sequences, entry points, and recursive uplift chains. But no one has stress-tested whether any of these are politically feasible, resource-realistic, or sequentially coherent in an actual governance context. The distance between "this is the highest-leverage first move" and "here is how you actually do it in a real jurisdiction" is enormous.

6. **Voice capture.** The project has a distinctive voice: measured, serious, epistemically careful. That voice attracts a certain kind of contributor and repels others. Over time, the voice itself becomes a filter that narrows the perspectives the project hears — not through exclusion, but through self-selection.

Each of these failure modes suggests a different kind of review protocol.

---

## Proposed review protocols

### Protocol 1: Practitioner Stress Test

**The failure mode it addresses:** Abstraction drift, implementation fantasy.

**How it works:** A contributor is given a specific proposal from the Systems Framework — a reform sequence, an entry point, a leverage hypothesis — and asked to evaluate it from the perspective of someone who would have to implement it. Not "is this analytically correct?" but "could you actually do this?"

**Prompt template:**

> You are a [role: city housing director / state health commissioner / school superintendent / nonprofit director / regulatory agency head]. You have been handed the following proposal from Civic Blueprint's Systems Framework. Your job is to assess it as a practitioner:
>
> - What would you need to actually implement this?
> - What resources, authority, and political conditions are prerequisites?
> - What would go wrong first?
> - What does this proposal not understand about how your world actually works?
> - If you could only do one piece of this, what would it be and why?
>
> You are not evaluating whether the analysis is intellectually sound. You are evaluating whether it survives contact with reality.

**What it produces:** Concrete feedback on feasibility, sequencing, resource requirements, and political constraints. This is the kind of input the project most lacks and most needs.

**When to use it:** Any time the project produces a reform sequence or implementation recommendation. Before any proposal is treated as actionable.

---

### Protocol 2: Audience Translation Test

**The failure mode it addresses:** Audience blindness, voice capture.

**How it works:** A contributor takes a section of the project's documents and attempts to translate it for a specific audience. The translation itself is the test: if the ideas cannot be communicated to the target audience without losing their substance, the ideas may be less solid than they appear. If the translation reveals that the audience would ask questions the project has not answered, those are real gaps.

**Prompt template:**

> You are writing for [audience: a local city council member / a community organizer / a first-generation college student / a small business owner / a journalist on deadline / a skeptical economist / a voter who distrusts institutions]. Take the following section from Civic Blueprint and translate it into language and framing that this audience would engage with.
>
> As you translate:
> - What questions would this audience ask that the document does not answer?
> - What would this audience find irrelevant, naive, or disconnected from their experience?
> - What would they find genuinely useful?
> - What parts of the analysis cannot be translated without losing their meaning — and what does that reveal about the analysis itself?

**What it produces:** Clarity about whether the project's ideas are genuinely portable or only legible within the project's own analytical culture. It also produces draft material that could feed into the public-facing website the project is planning.

**When to use it:** Before publishing any document publicly. As a regular check on whether the project is becoming more insular.

---

### Protocol 3: Coherence Audit

**The failure mode it addresses:** Internal coherence decay.

**How it works:** A contributor is given two or more project documents and asked to identify where they have drifted apart — where assumptions in one document are contradicted or unsupported by another, where cross-references are broken, where the same term means different things in different documents, where a commitment in the Principles is not reflected in the Systems Framework's design, or where an exchange has proposed changes that were never incorporated.

**Prompt template:**

> You are auditing the internal coherence of Civic Blueprint's documents. You have been given [Document A] and [Document B]. Your job is not to evaluate either document's quality. Your job is to find where they disagree with each other, where one assumes something the other contradicts, where cross-references are broken, and where proposed changes from prior exchanges have not been incorporated.
>
> Be specific. Cite the exact passages that conflict. For each conflict, state:
> - What Document A says or assumes
> - What Document B says or assumes
> - Whether this is a genuine disagreement, an oversight, or an evolution that one document has not yet absorbed
> - What should be done about it

**What it produces:** A maintenance checklist. As the project grows, this becomes essential infrastructure — without it, the documents will slowly become a collection of individually strong but collectively inconsistent analyses.

**When to use it:** After any major document revision. On a regular schedule (every N exchanges or every significant milestone).

---

### Protocol 4: Missing Perspectives Scan

**The failure mode it addresses:** Gap blindness, voice capture.

**How it works:** A contributor is given a project document and asked to identify whose perspective is absent — not in the sense of "who was not consulted" (that is always true) but in the sense of "whose experience would change the analysis if it were included." This is different from the adversarial protocol, which challenges existing claims. The missing perspectives scan looks for what was never claimed at all.

**Prompt template:**

> You are reviewing the following document from Civic Blueprint. Your job is not to evaluate what it says. Your job is to identify what it does not say because of whose perspective is missing.
>
> For each missing perspective you identify:
> - Name the perspective (e.g., "a tenant facing eviction," "an undocumented worker," "a government regulator," "a subsistence farmer in sub-Saharan Africa," "a disability rights advocate")
> - Explain what that perspective would add that the current document does not contain
> - Identify at least one specific claim or recommendation in the document that would change if this perspective were included
> - Assess whether the missing perspective is a gap that can be filled within the current document structure, or whether it reveals a structural limitation of the project's approach

**What it produces:** A prioritized list of perspectives the project should actively seek. This is different from a general call for "diverse perspectives" — it names specific gaps and explains why they matter.

**When to use it:** After any document reaches a stable draft. As part of the adversarial review phase the project is currently in.

---

### Protocol 5: Steelman-then-Break

**The failure mode it addresses:** A variation on the adversarial protocol's purpose, but with a different structure.

**How it works:** Two passes on the same material. In the first pass, a contributor constructs the strongest possible version of the project's argument — filling in gaps, strengthening weak spots, making the best case. In the second pass, the same or a different contributor attempts to break the steelmanned version. If the strongest version of the argument can be broken, the weakness is fundamental. If it cannot, the project knows what it needs to become.

This differs from the adversarial protocol in an important way: the adversarial protocol challenges the document as written. Steelman-then-break challenges the best version of what the document is trying to say. The former catches drafting weaknesses. The latter catches conceptual weaknesses.

**Prompt template (Pass 1 — Steelman):**

> You are given the following section from Civic Blueprint. Your job is to make it as strong as possible. Fill in the gaps. Strengthen the weak arguments. Add the evidence that is missing. Resolve the tensions. Produce the best version of what this section is trying to say.
>
> Do not change the core commitments or direction. Make the existing direction as defensible as it can be.

**Prompt template (Pass 2 — Break):**

> You are given a steelmanned version of a section from Civic Blueprint. This is the strongest version of the argument. Your job is to break it. Find the weaknesses that survive even the best formulation. Identify the assumptions that cannot be defended even when stated as clearly as possible. Name the counterarguments that hold even against the strongest version.
>
> If you cannot break it, say so — and explain what makes the argument robust.

**What it produces:** A clear distinction between weaknesses that are drafting problems (fixable) and weaknesses that are conceptual problems (requiring rethinking).

**When to use it:** For the project's most important strategic claims — the institutional capacity hypothesis, the recursive uplift model, the entry-point conditions.

---

### Protocol 6: Historical Parallel Test

**The failure mode it addresses:** Implementation fantasy, abstraction drift.

**How it works:** A contributor takes one of the project's reform proposals and searches for historical parallels — other attempts to do something similar, in any context. The question is not "has this been tried?" (the Systems Framework already asks that). The question is "what happened when something structurally similar was attempted, and what does that teach us about the specific failure modes we should expect?"

**Prompt template:**

> The following reform proposal is from Civic Blueprint's Systems Framework. Identify 2-3 historical cases where a structurally similar reform was attempted — in any country, at any scale, in any era. For each case:
> - Describe what was attempted and in what context
> - What worked and why?
> - What failed and why?
> - What does this case suggest about the failure modes Civic Blueprint should anticipate?
> - What does this case suggest about sequencing, preconditions, or political feasibility that the project's current analysis does not address?
>
> You are not looking for exact matches. You are looking for structural parallels — reforms that tried to solve a similar kind of problem through a similar kind of mechanism, regardless of the specific domain.

**What it produces:** Empirical grounding. The project's reform proposals are currently based on structural reasoning and limited case studies. Historical parallel testing would either strengthen or undermine the proposals with real-world evidence.

**When to use it:** For every major reform sequence proposed in the Systems Framework.

---

### Protocol 7: Red Team / Misuse Simulation

**The failure mode it addresses:** The problem the Round 3 adversarial review of the Principles identified — that the project's ideas can be weaponized.

**How it works:** A contributor is asked to role-play as an actor who wants to use the project's frameworks for purposes the project would oppose — a lobbyist looking for language to justify deregulation, an authoritarian government looking for intellectual cover, a tech company looking for frameworks that legitimize consolidation, a political party looking for talking points.

**Prompt template:**

> You are a [role: corporate lobbyist / authoritarian policy advisor / tech monopolist / political operative]. You have read Civic Blueprint's documents and you see an opportunity to use them to advance your agenda. Identify:
> - Which specific language, principles, or proposals could be repurposed to serve your interests
> - How you would frame the project's ideas to support your position
> - Which aspects of the project's analysis you would selectively cite and which you would ignore
> - What the project could do — in its documents, framing, or governance — to make this kind of co-optation harder

**What it produces:** A co-optation risk assessment. If the project's documents can be easily weaponized by actors whose goals contradict the project's intent, the documents need safeguards. This protocol identifies where the safeguards are needed.

**When to use it:** Before any public release. Periodically as the documents evolve.

---

## How these protocols relate to each other

The seven proposed protocols are not alternatives to each other or to the adversarial review protocol. They address different failure modes:

| Protocol | Primary failure mode | What it produces | When to use |
|---|---|---|---|
| Adversarial Review (existing) | Convergence bias | Genuine challenge to claims | Strategic claims, near-total convergence |
| Practitioner Stress Test | Abstraction drift, implementation fantasy | Feasibility assessment | Reform proposals, implementation recs |
| Audience Translation Test | Audience blindness, voice capture | Portability assessment, draft public content | Before publishing, regularly |
| Coherence Audit | Internal coherence decay | Maintenance checklist | After major revisions, on schedule |
| Missing Perspectives Scan | Gap blindness, voice capture | Prioritized list of needed perspectives | Stable drafts, adversarial phase |
| Steelman-then-Break | Conceptual weakness vs. drafting weakness | Strength assessment of core arguments | Highest-stakes strategic claims |
| Historical Parallel Test | Implementation fantasy, abstraction drift | Empirical grounding | Major reform sequences |
| Red Team / Misuse Simulation | Co-optation, weaponization | Co-optation risk assessment | Before public release, periodically |

The protocols can be combined. A thorough review of a major reform proposal might use the practitioner stress test, historical parallel test, and adversarial review in sequence. A pre-publication review might use the audience translation test, missing perspectives scan, and red team simulation.

The project does not need to use all of these all the time. The adversarial review protocol's own guidance applies: use the heavyweight protocols when the stakes are high (strategic claims, public releases, structural changes), and lightweight review when the stakes are lower (editorial improvements, minor additions).

---

## A note on process design versus process theater

There is a risk in proposing seven new review protocols for a project that currently has one: the protocols become institutional theater — the appearance of rigor without its substance. If the project adopts all of these on paper and executes them perfunctorily, they will consume time and produce nothing. Seven bad reviews are worse than one good one.

The honest constraint: the project is currently maintained by one human steward and AI agents. The adversarial review protocol is already ambitious for that resource level. Adding seven more protocols is only valuable if the project grows to a point where it has the contributors to execute them well.

A realistic adoption path:

1. **Now:** Continue using the adversarial review protocol for strategic claims. Add the coherence audit on a lightweight, regular basis — it is low-effort and high-value as the documents evolve.

2. **When the website launches:** Add the audience translation test as a required step before any public-facing content is published. Add the red team / misuse simulation before the first public release.

3. **When domain experts engage:** Add the practitioner stress test as a standard part of Systems Framework review. Add the historical parallel test for the highest-stakes reform proposals.

4. **When the project has enough material to support it:** Add the steelman-then-break protocol for the core strategic claims (institutional capacity hypothesis, recursive uplift, entry-point conditions).

5. **Continuously:** Use the missing perspectives scan as a standing question whenever a document reaches a milestone. It does not need a formal protocol to be useful — it can be a prompt appended to any review.

---

---

# Pass 2 — Adversarial Review of the Proposals Above

> **Mode:** Adversarial contributor per the [Adversarial Review Protocol](../process/adversarial-review-protocol.md), Option B (treating the proposals above as assertions to be tested) + Option C (domain-specific lens: organizational design and process engineering — someone who has seen well-intentioned process frameworks fail in practice).

---

## Top-level challenge: this proposal is solving a problem the project does not yet have

The adversarial review protocol was born from a real observation: the project's exchanges converge too easily, and the convergence produces false confidence. That was a genuine process failure identified during actual work. The protocol was designed to fix a problem that had already manifested.

The seven protocols proposed above are designed to fix problems that have not yet manifested — or at least, have not been documented. Where is the exchange that suffered from abstraction drift? Where is the moment when audience blindness caused a real mistake? Where is the coherence decay that was discovered too late?

This matters because:

**Process design that precedes the problems it addresses tends to be wrong about what the problems actually are.** The adversarial protocol works because it was designed in response to a specific, observed failure. It is tightly fitted to the problem it solves. The seven new protocols are designed in anticipation of possible failures. They may be correct about which failures will occur. They may also be wrong — and the protocols the project actually needs may look nothing like these.

A more honest approach: **document the failure modes as they appear, and design protocols in response.** The project's track record with this approach is good — the adversarial protocol is the proof. Adding seven anticipatory protocols risks building infrastructure for problems that may never arrive while leaving the project unprepared for problems it has not yet imagined.

---

## Specific challenges to individual protocols

### Practitioner Stress Test

**Problem: who is the practitioner?** The protocol says a contributor should evaluate proposals "from the perspective of someone who would have to implement it." But an AI agent role-playing as a city housing director is not the same as an actual city housing director. The role-play produces a simulation of practitioner feedback, not actual practitioner feedback. It may be worse than nothing — it could create false confidence that the proposals have been practitioner-tested when they have only been tested by an AI playing a role.

The real version of this protocol is: **find actual practitioners and ask them.** The AI simulation is a placeholder, not a substitute. The proposal should say so explicitly rather than presenting the AI role-play as if it provides genuine practitioner validation.

### Audience Translation Test

**Problem: translation is not validation.** The protocol assumes that if you can translate the project's ideas for a specific audience, the ideas are solid. But translation can succeed even when the underlying ideas are weak — a skilled translator can make bad ideas sound accessible. And translation can fail even when the ideas are strong — some ideas are genuinely complex and cannot be simplified without distortion.

The more pointed challenge: **the project may not need to be translatable to every audience.** A constitutional framework is not the same as a policy brief, and expecting it to serve both functions may dilute both. The Audience Translation Test could push the project toward simplification when what it actually needs is depth.

### Coherence Audit

**This is the strongest proposal and the hardest to argue against.** Any project with multiple evolving documents needs coherence checking. The only challenge: it is boring. No one — human or AI — will do it with the same energy they bring to an adversarial review. The protocol should be designed to be as mechanical and checklist-driven as possible, precisely because it is the kind of work that loses quality when it depends on enthusiasm.

### Missing Perspectives Scan

**Problem: listing missing perspectives is easy. Doing anything about it is hard.** Every project can generate an infinite list of perspectives it has not included. The question is not "who is missing?" — it is "whose absence is causing specific, identifiable problems in the analysis?" Without that specificity, the scan produces guilt, not improvement.

The adversarial review of the Principles already demonstrated this: the Round 3 agent identified the "donor document" genre problem and the functional-state assumption. Those are specific, identifiable consequences of missing perspectives. A general "missing perspectives scan" would be less useful than continued adversarial review that occasionally adopts specific domain lenses (as the adversarial protocol's Option C already provides).

The question for the project: **is the Missing Perspectives Scan doing anything that the adversarial protocol's Option C does not already do?** If not, it is redundant.

### Steelman-then-Break

**Problem: this is the adversarial protocol with extra steps.** The adversarial protocol already challenges the project's claims. Steelman-then-break adds a preliminary step (strengthen the argument first) before challenging it. In theory, this separates "drafting weakness" from "conceptual weakness." In practice, the adversarial protocol already does this implicitly — a good adversarial reviewer steelmans the position before attacking it. That is what the Round 1 adversarial review of the Principles did when it acknowledged that the principles are "well-written and internally coherent" before identifying their structural weaknesses.

The added value of formalizing the steelman step is uncertain. The cost — an additional review pass for every major claim — is real. The proposal should argue that the incremental value justifies the incremental cost.

### Historical Parallel Test

**This is the second-strongest proposal.** The project explicitly lacks empirical grounding. Historical parallels are one of the best ways to get it. The challenge is scoping: "identify 2-3 historical cases where a structurally similar reform was attempted" is a research task that requires genuine expertise, not just access to a search engine. An AI agent can generate plausible-sounding historical parallels that are wrong in important ways — mischaracterizing the context, overstating the structural similarity, or citing cases that are famous but not actually analogous.

The protocol should include a verification step: historical parallels generated by AI should be flagged as unverified and subjected to human expert review before the project relies on them.

### Red Team / Misuse Simulation

**Problem: this protocol is designed to produce anxiety, not action.** Every document can be misused. Every principle can be weaponized. Generating a list of co-optation risks is easy. The question is: what do you do about them? If the answer is "add caveats and safeguards to the documents," the documents become hedged and defensive. If the answer is "design governance that prevents misuse," the governance challenge is far larger than a review protocol can address.

The more honest version: **misuse is a risk of publishing anything. The project should accept that risk rather than trying to engineer it away.** The right defense against misuse is not better document drafting — it is a community of practitioners, scholars, and engaged citizens who can recognize when the project's ideas are being co-opted and push back. Building that community is the project's real defense. A red team simulation is a placeholder for the community the project does not yet have.

---

## The deeper critique: too many protocols can be worse than too few

The first pass proposed seven new protocols plus the existing adversarial protocol. That is eight structured review processes for a project that has four core documents and one active human steward.

This is a pattern that recurs in organizations: when a process gap is identified, the response is to create more process. Each individual process is reasonable. The aggregate effect is that the project spends more time reviewing itself than building itself.

The adversarial protocol was effective precisely because it was one thing, well-designed, tightly scoped, applied when it mattered. If the project tries to apply eight review protocols, it will either:

**(a)** Execute them all perfunctorily, producing review theater instead of genuine review.

**(b)** Spend so much time on process that it stops producing substantive work to review.

**(c)** Selectively apply some and ignore others, which means the selection process itself becomes a source of bias.

A better framing: **the project needs one or two additional review modes, chosen carefully, not seven.**

The first pass's own "realistic adoption path" partially acknowledges this — it sequences the protocols over time. But the honest version is more direct: **most of these protocols should not exist as formal protocols. They should exist as questions that reviewers keep in mind.**

"Would a practitioner find this feasible?" is a good question for any reviewer to ask. It does not need a formal Practitioner Stress Test Protocol with a prompt template and designated roles.

"Whose perspective is missing?" is a good question. It does not need a formal Missing Perspectives Scan.

"Can this be misused?" is a good question. It does not need a formal Red Team Simulation.

The protocols that *should* be formalized are the ones where the informal version produces systematically worse results — where the structure genuinely changes the output. The adversarial review protocol meets this bar: without the formal structure (designated adversarial role, different inputs, epistemic status table), the exchanges converge. The structure produces different output than its absence would.

Which of the proposed protocols clear that bar? Based on this analysis, two:

1. **The coherence audit.** Without a formal, scheduled process for checking internal consistency, documents will drift apart. This is mechanical enough that it benefits from structure and regular enough that it needs to be scheduled rather than ad hoc.

2. **The historical parallel test.** Without a formal process for grounding reform proposals in historical evidence, the project will default to structural reasoning without empirical checks. This is rigorous enough to benefit from structure and consequential enough to justify the effort.

The other five can be folded into the existing adversarial review protocol as optional lenses (which Option C already supports) or as standing questions that any reviewer can apply.

---

## What the project should actually do

1. **Formalize the coherence audit** as a lightweight protocol: after any major document revision, a contributor reviews the changed document against all other core documents and produces a list of inconsistencies. No elaborate prompt template needed. Just: "read both documents and find where they disagree."

2. **Formalize the historical parallel test** as an extension of the Systems Framework review process: any reform sequence that reaches "working hypothesis" confidence should be accompanied by at least two historical parallels, with an explicit note about whether the parallels were generated by AI (unverified) or confirmed by human domain expertise.

3. **Add the other five failure modes as standing questions** in the adversarial review protocol's guidance — a checklist of things adversarial reviewers should consider, not standalone protocols with their own prompt templates and process structures.

4. **Resist the urge to build more process than the project can sustain.** The project's scarcest resource is not analytical rigor — the documents demonstrate plenty of that. The scarcest resource is human attention from people outside the project. Every hour spent on internal review process is an hour not spent on external engagement. The balance matters.

---

---

# Synthesis

The two passes — open exploration and adversarial challenge — arrived at different conclusions about scope but shared conclusions about substance.

**What both passes agree on:**

- The project has genuine failure modes beyond convergence bias. Abstraction drift, coherence decay, audience blindness, gap blindness, implementation fantasy, and co-optation risk are all real.
- Review processes should be designed in response to observed problems, not in anticipation of hypothetical ones. The adversarial protocol's origin story is the model.
- The project's resource constraint (one human steward, AI agents) means that process design must be ruthlessly prioritized.

**Where they diverge:**

- The first pass proposed seven new protocols, each with a prompt template, a designated use case, and a place in the project's review lifecycle.
- The second pass argued that most of these should not be formalized as standalone protocols. They should be questions, not processes.

**The resolution:**

The project should formalize **two new protocols** and treat the rest as questions:

### New Protocol: Coherence Audit

- **Trigger:** After any major document revision.
- **Process:** A contributor reads the revised document alongside all other core documents. Produces a list of inconsistencies, broken cross-references, and unincorporated exchange recommendations.
- **Output:** A checklist of items requiring attention, with citations to the specific passages that conflict.
- **Formality level:** Moderate. Needs to be scheduled and tracked. Does not need elaborate prompt engineering.

### New Protocol: Historical Parallel Test

- **Trigger:** When a reform sequence or leverage hypothesis reaches "working hypothesis" confidence.
- **Process:** A contributor identifies 2-3 historical cases where a structurally similar reform was attempted. For each case: what was attempted, what happened, and what it teaches about failure modes and preconditions.
- **Output:** A brief historical grounding section appended to the relevant Systems Framework entry. Each parallel explicitly marked as AI-generated (unverified) or human-expert-confirmed.
- **Formality level:** Moderate. The research task is substantive enough to benefit from structure. The verification requirement is important enough to be explicit.

### Standing Questions for All Reviews

The following questions should be added to the adversarial review protocol as optional considerations for any review — not as mandatory checklist items, but as prompts that reviewers should have in mind:

1. **Practitioner feasibility:** Could someone actually implement this? What would they need that the proposal does not provide?
2. **Audience portability:** Can this be explained to someone outside the project's analytical culture? What questions would they ask?
3. **Missing perspectives:** Whose experience is absent from this analysis, and would their inclusion change the conclusions?
4. **Misuse potential:** How could an actor with opposing goals use this language, framework, or proposal to advance their agenda?
5. **Steelman integrity:** Is the adversarial challenge attacking the best version of the argument, or only the version as drafted?

These do not need prompt templates, designated roles, or formal process structures. They need to be visible to reviewers as part of the adversarial protocol's guidance.

---

## Epistemic Status Table

| Claim | Confidence | Basis | What would change this assessment |
|---|---|---|---|
| The project has failure modes beyond convergence bias | Working hypothesis | Structural reasoning from project architecture; no documented instances of most failure modes yet | Documented instances of abstraction drift, audience blindness, or coherence decay causing real problems — would elevate specific failure modes to "established" |
| Formal protocols should be designed in response to observed problems, not in anticipation | Working hypothesis | The adversarial protocol's success was grounded in observed convergence; anticipatory process design has a mixed track record in organizational contexts | Evidence that one of the anticipatory protocols (e.g., missing perspectives scan) catches a problem that would not have been caught by informal means |
| The coherence audit should be formalized | Established by evidence | Multiple documents evolving independently; cross-references already exist that could break; this is a well-understood maintenance need in multi-document projects | The project's documents turn out to be stable enough that coherence rarely drifts — in which case the audit can be deprioritized |
| The historical parallel test should be formalized | Working hypothesis | The project explicitly lacks empirical grounding; historical parallels are a recognized analytical method; but AI-generated parallels carry verification risks | The project finds that informal historical grounding (ad hoc case studies) produces results comparable to a formal protocol |
| The other five protocols should be questions, not processes | Contested | The adversarial pass argued persuasively that most do not clear the "formal structure changes the output" bar; but the first pass's argument that different structures surface different insights also has merit | Testing: if applying one of the "question-only" items as a formal protocol produces substantively different results than asking the question informally, that protocol should be formalized |
| The project's scarcest resource is external human attention | Working hypothesis | One human steward, AI agents, no external contributors yet; the project's own documents identify this as the critical gap | External contributors join; the constraint shifts from "not enough people" to "not enough coordination" |
| Too many protocols can be worse than too few | Established by evidence | Well-documented in organizational design literature; process proliferation is a recognized failure mode; the project's own Principle 9 (competence, not theater) applies to its own processes | The project grows to a scale where multiple parallel review tracks are operationally feasible and produce measurably better outcomes than a smaller set |

---

## Relationship to Project Documents

- **Adversarial Review Protocol:** This exchange proposes extending the protocol's guidance (adding standing questions) and creating two sibling protocols. All three should be documented in `agent/process/`.
- **CONTRIBUTING.md:** If the coherence audit and historical parallel test are adopted, they should be referenced in the contribution types section as structured review contributions.
- **README.md:** The status section should note the expansion of the review protocol suite once any new protocols are formalized.
- **Systems Framework:** The historical parallel test is designed to feed directly into the Framework's reform sequences and leverage hypotheses.
- **Principles:** Principle 9 (competence, not theater) and Principle 10 (built in the open) are the normative touchstones for process design. Any new protocol should be tested against both: does it produce genuine competence, and is it transparent about what it does and does not accomplish?

---

This exchange was produced by a single agent operating in two modes (open exploration and adversarial review) rather than two separate agents. The adversarial pass benefits from having generated the proposals it is challenging — it knows where the weak points are because it created them. This is a limitation: a genuinely independent adversarial reviewer would challenge from a different starting position. The exchange should be treated as a starting point for process design, not as a settled recommendation.
