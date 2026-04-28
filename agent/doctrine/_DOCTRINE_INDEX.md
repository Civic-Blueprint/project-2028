---
description: Index of adopted operational frameworks (project doctrine) — the HOW layer between Foundational Commitments and concrete proposals.
---

# Doctrine Index

> **Status (April 2026):** Directory created; no doctrine notes adopted yet. The first planned entry is the **bounded-governance doctrine** from [Exchange #21 Round 5](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-5), via [Roadmap follow-up F3](../../ROADMAP.md). F3 is gated on TR1 (transferability + perspective-gap research sweep) and TR2 (external human reviewer participation); see [Roadmap TODOs #9–#11](../../ROADMAP.md#high-priority).

---

## What this directory is for

`agent/doctrine/` houses **adopted operational frameworks** — multi-element design packages, taxonomies, or doctrines that the project has stress-tested through an adversarial exchange and elevated to a standing reference for proposal evaluation. Doctrine notes sit between [Foundational Commitments](../../FOUNDATIONAL_COMMITMENTS.md) and the [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md):

| Layer | Specifies | Where it lives |
|---|---|---|
| [Principles](../../PRINCIPLES.md) | WHAT the project commits to | Top-level repo |
| [Foundational Commitments](../../FOUNDATIONAL_COMMITMENTS.md) | What it takes to meet each commitment | Top-level repo |
| [Systems Framework](../../SYSTEMS_FRAMEWORK.md) + **`agent/doctrine/`** | The space of HOWs — mechanism tradeoffs and adopted operational frameworks | Top-level + this directory |
| [Proposal Catalog](../../proposals/PROPOSAL_CATALOG.md) | Concrete instances of HOW | `proposals/` |

A document belongs in `agent/doctrine/` when **all** of the following are true:

1. **It is operational, not principle-level.** It specifies a multi-element design package, taxonomy, or feature set — not a normative commitment. Normative commitments belong in [PRINCIPLES.md](../../PRINCIPLES.md) or [FOUNDATIONAL_COMMITMENTS.md](../../FOUNDATIONAL_COMMITMENTS.md).
2. **It has survived adversarial review.** A v2 (post-adversarial) version exists, produced via the [Adversarial Review Protocol](../process/adversarial-review-protocol.md). Pre-adversarial drafts stay inside their originating exchange.
3. **It carries reference-class limits and authenticity conditions.** The doctrine names the conditions under which it applies and the conditions under which adoption would be hollow.
4. **It is referenced from at least one Foundational Commitment or Systems Framework section.** Doctrine notes that nothing in the WHAT layer points to are orphans — either lift them into Systems Framework or leave them inside their exchange.

Documents that do **not** belong here:

- Single-exchange working drafts (those stay in [`agent/exchanges/`](../exchanges/)).
- Process protocols — adversarial, coherence audit, historical parallel test, comparative alignment, reviewer-as-a-round (those live in [`agent/process/`](../process/) or [`docs/`](../../docs/)).
- Source digests (those live in [`sources/`](../../sources/)).
- Concrete reform proposals (those live in [`proposals/`](../../proposals/)).

---

## Adopted doctrine

*None yet.* The directory is intentionally empty pending the first F-track follow-up that completes its TR1/TR2 prerequisites.

---

## Planned doctrine notes

### Bounded-governance doctrine (planned)

|  |  |
|---|---|
| **Source** | [Exchange #21 Round 5 Deliverable 3 (v2)](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-5) — the ten-feature doctrine under specific conditions. |
| **Roadmap track** | [F3 — Bounded-governance doctrine → public artifact](../../ROADMAP.md). |
| **Prerequisites** | [TR1](../../ROADMAP.md#high-priority) (transferability + perspective-gap research sweep) and [TR2](../../ROADMAP.md#high-priority) (external human reviewer participation under the [Reviewer Packet Template](../../docs/REVIEWER_PACKET_TEMPLATE.md) and [Reviewer-as-a-Round Convention](../../docs/REVIEWER_AS_A_ROUND_CONVENTION.md)). |
| **Will house** | The ten-feature design package; the seven-category ownership taxonomy (or that may move to Systems Framework via F2); the reference-class limit; the authenticity conditions; the *replacement-over-addition* default. |
| **Cross-references it must carry** | [Foundational Commitment 5](../../FOUNDATIONAL_COMMITMENTS.md), [PRINCIPLES.md Principle 5](../../PRINCIPLES.md), [Roadmap TODO #12](../../ROADMAP.md). |

Other F-track outputs (F2 ownership taxonomy, F4 frontier-AI governance, F6 distributional-incidence protocol) may produce additional doctrine notes once their adversarial review and reviewer cycles complete. Whether each F-track output lands here, in [Systems Framework](../../SYSTEMS_FRAMEWORK.md), or in [`agent/process/`](../process/) is a per-output judgment captured in the relevant exchange's "What comes next" section.

---

## How to add a doctrine note

1. **Confirm the four conditions above.** If any are missing, the document is not yet doctrine.
2. **Create `agent/doctrine/<short-name>-doctrine.md`** following the structure used by adopted-framework documents elsewhere in the project (front matter with `description`, status block citing the originating exchange + round, the doctrine itself, reference-class limit, authenticity conditions, anti-misuse clauses, companion references).
3. **Register the entry in this index** under "Adopted doctrine" with the same five-row table used in "Planned doctrine notes" above.
4. **Wire the cross-references**:
   - Add the doctrine to the relevant section of [FOUNDATIONAL_COMMITMENTS.md](../../FOUNDATIONAL_COMMITMENTS.md) ("Companion references" subsection of the affected commitment).
   - Add the doctrine to [SYSTEMS_FRAMEWORK.md](../../SYSTEMS_FRAMEWORK.md) where mechanism tradeoffs reference it.
   - Update the originating exchange's status block to reflect that the doctrine has been promoted out.
   - If a [Roadmap](../../ROADMAP.md) follow-up was tracking the promotion, mark it complete and move the entry to [ROADMAP_ARCHIVE.md](../../ROADMAP_ARCHIVE.md).
5. **Run a [Coherence Audit](../process/coherence-audit-protocol.md)** on the affected documents.

---

## Maintenance

This index is updated whenever a doctrine note is added, revised, retired, or superseded. The [Coherence Audit Protocol](../process/coherence-audit-protocol.md) includes `agent/doctrine/**` in its scope (Document class 2 — project-authored analysis and coordination artifacts).
