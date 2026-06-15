# Distributional-Incidence Protocol

> **Status:** Proposed (June 2026). Formalizes [Exchange #21](../exchanges/government-overreach-ownership-ratchet-exchange.md) Round 5 Deliverable 5 (v2, anti-theater) as a project-wide review protocol, alongside [Adversarial Review](adversarial-review-protocol.md), [Coherence Audit](coherence-audit-protocol.md), [Historical Parallel Test](historical-parallel-test-protocol.md), and [Comparative Alignment](comparative-alignment-protocol.md). Spawned per [ROADMAP TODO #1 / F6](../../ROADMAP.md) (the steward's June 14, 2026 "build F6 now" decision). **Carries an un-closed debt:** the bounded-governance doctrine this protocol serves is grounded in an [unrepresentative reference class](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-4) (small/high-trust/wealthy polities); transferability to large heterogeneous polities is unresolved (research debt under [TR1](../../ROADMAP.md#new-tracks-introduced-by-exchange-21-round-5)).

---

## The problem this protocol addresses

A reform proposal can be **arithmetically correct and still fail** — fiscally sound, technically defensible, and yet so regressive in its distribution that it cannot survive its first political cycle, or so silently regressive that it should not. [Exchange #21](../exchanges/government-overreach-ownership-ratchet-exchange.md) established this twice over: the [Argentina case](../../sources/source-argentina-milei-reforms-digest.md) (a successful fiscal consolidation whose approval collapsed because the adjustment was regressive) and the comparative-cases cluster (Canada's consolidation survived on broad distribution; New Zealand's reformers paid the largest political cost on concentrated distribution).

But the obvious fix — "require a distributional analysis" — has a known failure mode. The U.S. regulatory-impact-analysis regime (OMB Circular A-4, CBO scoring, Regulatory Flexibility Act small-business analyses) has produced incidence analyses for decades and has **not** prevented regressive outcomes. It has largely become a **compliance layer** that organizations with regulatory counsel can satisfy and others cannot. [Exchange #21 Round 4](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-4) judged this "procedural theater" risk *real and already realized in a close comparator.*

This protocol exists to get the benefit (distribution made visible and binding) **without** producing one more layer of theater. The discipline is in the anti-theater conditions (§3–§5), not in the table itself.

---

## Protocol

### 1. Ask the upstream question first — *should this rule exist?* — symmetrically for adoption and repeal

Before measuring a rule's incidence, engage the prior question: **should this rule exist at all?** Apply it with **equal weight to rule adoption and to rule repeal.** Distributional-incidence review is *not* a tool for preserving status-quo rules any more than for adopting new ones; a review that only ever scrutinizes new rules is a status-quo-bias engine. Naming the upstream question symmetrically is what keeps the protocol from becoming a one-directional ratchet ([§21 Round 4 challenge 5c](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-4)).

### 2. Build the incidence table — including a separate worst-off-protection row

Produce, at minimum:

- An **incidence table** — who bears the **direct, secondary, and long-run** costs of the rule, measured across **income quintiles** and at least one other policy-relevant grouping where it matters (age, geography, race/ethnicity, sector of employment).
- A separate **worst-off-protection row** — impact on the **least-advantaged specifically** (not the bottom quintile used as a summary stand-in), following the Rawlsian commitment the justification invokes. This row is distinct from quintile incidence and is read on its own.

### 3. Make the findings binding, not advisory

Incidence findings must be **binding on rule design to a specified degree**, not merely published. Concretely: if bottom-quintile (or worst-off) incidence is negative and unmitigated, the rule **must** carry either an explicit compensating mechanism or an explicit, on-the-record justification for the distribution it accepts. "We analyzed it" is not a pass; "we analyzed it and here is what we did about it, or why we did not" is.

### 4. Trigger remediation on defined thresholds

Specify, in advance, the **thresholds that trigger remediation** (not just disclosure). A finding that crosses a pre-registered threshold obligates a defined response — a compensating mechanism, a redesign, a sunset acceleration, or a documented decision to proceed with named accountability. Thresholds set after the analysis can be drawn to clear the result; set them first.

### 5. Subject the incidence review itself to adversarial review (the anti-theater keystone)

The incidence review is **itself subject to [adversarial review](adversarial-review-protocol.md)**: a separate reviewer commissions a **counter-incidence analysis using a different methodology or assumption set.** This is the single condition the RIA comparator most lacks and the one most responsible for keeping the protocol honest — a self-produced incidence table that no adversary has tried to overturn is the theater this protocol is built to avoid. Where the harness is available, this step is a natural [Cross-Lineage Review Harness](cross-lineage-review-harness-protocol.md) target (the counter-analysis run on an independent lineage).

### 6. Publish and feed the ledger

Publish the review (and its counter-analysis) through the rule's [transparency element](../exchanges/government-overreach-ownership-ratchet-exchange.md#integration-with-the-other-eight-elements); the findings become part of the rule's ongoing public record. Where a compensation/accounting ledger exists (bounded-governance Element 3), incidence findings feed it, so the rule's political-economic trajectory is tracked alongside its fiscal-arithmetic trajectory.

### 7. Carry the reference-class limitation explicitly

State, in any artifact that uses this protocol, that the bounded-governance doctrine it serves is **grounded in an unrepresentative reference class** and that its transfer to large heterogeneous polities is **unresolved**. The protocol disciplines *how* a rule's distribution is examined; it does not, by itself, establish that the rule transfers. Do not let a completed incidence table read as a transferability proof.

---

## When to apply this protocol

Use this protocol when:

- a **bounded-governance rule or reform proposal** with distributional consequences is being specified, adopted, or repealed
- a proposal moves from the [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) toward development, or an [F-track](../../ROADMAP.md#new-tracks-introduced-by-exchange-21-round-5) public artifact (especially F3/F4/F5) approaches publication
- a claim is being made that a rule is "fiscally sound" or "technically correct" without yet asking *who pays*

Lightweight commentary does not require the full protocol. Any proposal intended to influence the project's public positions, the Problem Map, or a real-world reform recommendation does.

---

## What this protocol does not do

- It is **not a veto.** A rule with regressive incidence may still be adopted — but only with an explicit compensating mechanism or an on-the-record justification (§3). The protocol forces the choice into the open; it does not make it.
- It is **not a substitute for political legitimacy** or for the missing practitioner / Global-South / beneficiary voices ([Exchange #21](../exchanges/government-overreach-ownership-ratchet-exchange.md)'s largest residual debt). A clean table is not consent.
- It does **not close the transferability question** (§7). That is research debt under TR1, not something an incidence table resolves.
- It does **not** by itself defeat capture: an adversarial counter-analysis (§5) reduces theater but does not guarantee the reviewer pool is decorrelated. Where it matters, pair §5 with the [decorrelation discipline](../../memos/decorrelation-independent-ai-evaluation-memo.md) (different methodology *and* different lineage/institutional priors).

---

## Relationship to sibling protocols

This is the **fifth** structured review protocol the project uses. Each addresses a different failure mode:

- **[Adversarial Review Protocol](adversarial-review-protocol.md):** Challenges claims — tests whether strong conclusions are defensible.
- **[Coherence Audit Protocol](coherence-audit-protocol.md):** Checks internal consistency across the corpus.
- **[Historical Parallel Test Protocol](historical-parallel-test-protocol.md):** Grounds reform claims in historical evidence.
- **[Comparative Alignment Protocol](comparative-alignment-protocol.md):** Compares external formation documents to the project's principles.
- **Distributional-Incidence Protocol (this document):** Asks **"who pays, and is that acceptable and acted upon?"** of any rule with distributional consequences.

The protocols compose: §5 of this protocol *is* an invocation of Adversarial Review (and, where available, the Cross-Lineage Review Harness), turned on the incidence analysis itself.

---

## Relationship to project principles

- **[Principle 2 (essential needs should not be held hostage to avoidable scarcity)](../../PRINCIPLES.md#2-essential-needs-should-not-be-held-hostage-to-avoidable-scarcity):** a reform that relieves aggregate scarcity while concentrating its costs on the least-advantaged is not the kind of correction Principle 2 calls for; the worst-off-protection row makes that visible.
- **[Principle 5 (critical systems require public-interest governance)](../../PRINCIPLES.md#5-critical-systems-require-public-interest-governance):** distributional incidence is constitutive of a durable bounded-governance rule, not an external addendum — the protocol operationalizes that.
- **[Principle 4 (power must remain accountable, legible, and reversible)](../../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible):** binding findings + triggered remediation + published counter-analysis are the accountability-and-legibility mechanisms; the symmetric adoption/repeal step is the reversibility mechanism.
- **[Principle 16 (justice mediates between competing claims)](../../PRINCIPLES.md#16-justice-mediates-between-competing-claims):** the protocol is a structured way to surface who wins and who loses under a rule, rather than hiding the trade behind aggregate arithmetic.
