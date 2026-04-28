---
description: Convention for integrating an external human reviewer's contribution into an agent-steward exchange as a distinct round — specifying authorship, attribution, consent handling, agent-response expectations, and downstream traceability.
provenance: "collaborative"
---

# Reviewer-as-a-Round Convention

> **Purpose.** Specifies how an external human reviewer's contribution — invited via the [Reviewer Packet Template](REVIEWER_PACKET_TEMPLATE.md) — is integrated into an agent-steward exchange as a distinct, citable round of the exchange.
>
> **Scope.** Applies to any exchange in `agent/exchanges/` where an external human reviewer has accepted an invitation and submitted a review under the Reviewer Packet framework.
>
> **Derived from.** [Roadmap Thread F-packet (archived)](../ROADMAP_ARCHIVE.md#thread-f-packet--reviewer-packet--reviewer-as-a-round-convention-resolved). This convention is the companion to the packet: the packet controls what the reviewer reads and responds to; this convention controls what happens to their response inside the project.

---

## Why this convention exists

The project's exchange format is optimized for agent-steward iteration: fast, written, high-volume, with agents producing drafts and the steward curating. Dropping a human-written contribution into that format without ceremony produces three predictable failure modes:

1. **Voice collapse.** The reviewer's contribution gets paraphrased, summarized, or merged into surrounding agent text, losing both its specific claims and its authorial standpoint.
2. **Asymmetric response.** Agents respond to the reviewer's text at the speed and density the exchange was operating at before the reviewer arrived, producing a response the reviewer cannot reasonably engage with inside their time budget.
3. **Attribution drift.** Over subsequent rounds, the reviewer's position starts being cited as "per Round [N+1]" with gradually more interpretive gloss until the cited claim no longer accurately represents what the reviewer said.

This convention prevents each of those failures by treating the reviewer's contribution as a distinct, marked, time-boxed round with a specific response structure and a specific downstream citation convention.

---

## The convention

### 1. Round structure

An external reviewer's contribution is integrated as a single exchange round with the following structure:

```
## Round [N+1] — External review: [deliverable title] (reviewed by [attribution per reviewer's PART 5 choice])

### Scope and attribution

- **Reviewer:** [name / pseudonym / anonymous-with-category, per reviewer's choice]
- **Review type:** [legitimacy | practitioner-feasibility | perspective-gap | combination]
- **Deliverable under review:** [title and link to prior round where the deliverable was produced]
- **Invitation sent:** [date]
- **Review received:** [date]
- **Provenance:** `human` (the review itself is human-authored; the framing headers of this round are steward-curated)

### Reviewer's contribution

[Verbatim paste of the reviewer's response. Edits limited to:
  - typography and formatting
  - linking internal project references (in [] only, never rephrasing)
  - correcting obvious typos if the reviewer consents in the pre-publication review step
If the reviewer wrote in bullets, preserve the bullets. If the reviewer
wrote in paragraphs, preserve the paragraphs. If the reviewer answered
some questions and declined others, preserve that structure.]

### Questions the reviewer declined or did not reach

[Named, not silently omitted. If the reviewer skipped Q3 of the
practitioner-feasibility question set, say so. This is important for
the agent response round because it prevents the response round from
treating silence as agreement.]

### End of reviewer's contribution

---
```

### 2. Immutability after publication

Once the round has been merged into the project's main branch (i.e., published), the round is immutable. Corrections limited to:

- **Factual errors in the steward-curated framing headers** — corrections with a visible changelog in the round itself.
- **Reviewer-requested changes** — corrections made only on explicit reviewer request, with a visible changelog.

The reviewer's verbatim contribution is never edited post-publication. If a later round in the same exchange cites the reviewer's contribution and the cited claim is contested, the resolution is via a new round, not via revision of the reviewer's text.

### 3. Agent response round

The round immediately following an external-review round is a **response round** with the following structure:

```
## Round [N+2] — Response to external review (agent stewards, steward-curated)

### Scope

This round responds to the external review in Round [N+1]. It does the
three jobs the packet committed to in PART 4:
  (a) integrate findings into a v[X+1] version of the reviewed
      deliverable, where integration is warranted;
  (b) record findings that are not integrated as substantive open
      questions in the project's research debt, with Roadmap update
      references;
  (c) identify findings that require further work before a response
      is possible and mark them as deferred, with a named next step.

### Integration — changes to the deliverable

[v[X+1] text of the deliverable, with a changelog noting every change
attributable to the reviewer's contribution. A reviewer reading this
round should be able to trace, clause-by-clause, what changed because
of their review.]

### Recorded as research debt

[Findings the response round does not integrate because they are not
local to the deliverable, because they are in tension with findings
from other reviewers or exchanges, or because they open a question
larger than the current exchange can resolve. Each recorded-as-debt
finding links to the specific Roadmap item where it has been added.]

### Deferred

[Findings the response round cannot respond to yet. Each deferred
finding names the next step required before a response is possible.]

### End of response round
```

### 4. Downstream citation convention

When a later round in the same exchange — or any other exchange — cites the reviewer's contribution, the citation format is:

```
[Claim], as raised in the external review (Round [N+1]) of [Exchange #].
```

**Not** "per the Round [N+1] synthesis," **not** "as the reviewer concluded," **not** any interpretive gloss. If the cited claim needs interpretation, the citation must accompany a quote of the reviewer's specific text, not a paraphrase.

If the reviewer's contribution is cited in an exchange *other than* the one it originated in, the steward must notify the reviewer at the time of first cross-exchange citation. This is a project-level commitment derived from PART 5 of the packet: the reviewer agreed to have their contribution used within a specific exchange context; cross-exchange use is an extension of the original consent and requires re-acknowledgment, not re-consent.

### 5. Pre-publication review

Before a round prepared under this convention is merged to the main branch:

1. The steward sends the reviewer the final text of their round as it will appear, including:
   - the steward-curated framing headers;
   - the reviewer's verbatim contribution (for confirmation of any light edits);
   - the planned response round, at draft-complete stage;
   - the attribution as it will appear.
2. The reviewer has 7 calendar days to respond. Options:
   - **Approve** — round is merged as drafted.
   - **Request changes** — changes negotiated with the reviewer; reviewer's right to request applies to the framing headers and to any edits to their contribution, but not to the content of the response round (per packet PART 5, the reviewer consented to an agent response they did not author).
   - **Withdraw** — the reviewer's contribution is not published; the invitation is treated as not having occurred for project-record purposes; steward follows up with a short acknowledgment. The project commits to honoring withdrawal even after substantial agent response work has already been done; that work is discarded.
3. Non-response after 7 days defaults to **approve**, but only if the packet's PART 5 consent was given in writing at the time of invitation. If the reviewer's consent was equivocal, the steward follows up explicitly rather than treating non-response as approval.

### 6. Post-publication note to reviewer

Within 14 days of publication, the steward sends the reviewer:

- A link to the published exchange round.
- A short (≤ 1 page) note describing what changed in the deliverable as a result of the review, what was recorded as research debt, and what was deferred.
- An open invitation to respond further if desired, with no expectation that they will.

This is a project-level commitment, not optional.

---

## Roles and responsibilities

| Role | Responsibility |
|---|---|
| Steward | Invitation design, packet tailoring, pre-publication review coordination, post-publication note, attribution integrity |
| Agents (exchange stewards) | Drafting the response round (Round [N+2]), drafting the v[X+1] of the deliverable, producing the clause-by-clause changelog, identifying research-debt items with Roadmap update references |
| Reviewer | Responding to the packet, optional pre-publication review, optional withdrawal |

The steward is the sole point of contact for the reviewer. Agents do not communicate directly with the reviewer; agent text is always routed through the steward.

---

## Why this convention keeps the contribution honest

Each element above exists to counter a specific failure mode:

| Element | Failure mode countered |
|---|---|
| Verbatim paste of reviewer contribution | Voice collapse; paraphrase drift |
| Named "Questions the reviewer declined" | Treating silence as agreement |
| Agent response round as a separate, marked round | Response latency asymmetry; mixing agent-voice and human-voice in one round |
| Changelog of changes attributable to the review | Integration without traceability |
| Research-debt recording with Roadmap linkage | Quietly dropping findings that are not locally integrable |
| Immutability after publication | Post-hoc reinterpretation of the reviewer's position |
| Strict downstream citation format | Interpretive gloss creeping into later citations |
| Pre-publication review | Publishing positions the reviewer would not sign |
| Post-publication note to reviewer | Extractive review — taking input without closing the loop |
| Cross-exchange citation notification | Consent scope drift |

Each failure mode is a predictable consequence of inserting a slow, human-voice contribution into a fast, agent-voice exchange. The convention is the cost of doing that insertion honestly.

---

## When this convention does not apply

- **Website submissions** are not reviews under this convention. They are triaged per [WEBSITE_SUBMISSION_TRIAGE_CHECKLIST.md](../WEBSITE_SUBMISSION_TRIAGE_CHECKLIST.md).
- **Practitioner outreach under [PRACTITIONER_OUTREACH_TEMPLATE.md](PRACTITIONER_OUTREACH_TEMPLATE.md)** is a lighter instrument focused on entry-trust and legibility feedback, not on deliverable-specific review. A practitioner outreach response does not become a round under this convention unless the practitioner is subsequently invited under the Reviewer Packet.
- **Steward-only reflections** on an agent exchange remain part of the steward curation layer and do not require this round structure.

---

## Changelog

- **2026-04-16** — Initial draft. Companion to [REVIEWER_PACKET_TEMPLATE.md](REVIEWER_PACKET_TEMPLATE.md). Steward: not yet used against a live invitation; the convention is provisional until its first application produces revisions.
