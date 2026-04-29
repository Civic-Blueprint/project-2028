---
description: Practitioner feedback records — preserved transcripts and structured notes from real-world interactions with the project.
provenance: "collaborative"
---

# Feedback Records

This directory preserves **practitioner feedback records**: structured artifacts that capture real interactions between the project and people who have engaged with its public surfaces (the website, the memo, outreach messages, conversations). The point is to keep the data — the actual words, in context — so future exchanges can reason from evidence rather than from memory.

Feedback records are **not exchanges**. They do not contain agent-steward discussion. They are reference artifacts, analogous to source digests in `sources/`, but for first-party empirical input rather than external published material.

> **Operational counterpart.** This README defines the *conventions* for feedback records. The mechanical workflow that enforces those conventions at capture time — anonymization checklist, front-matter validation, link-and-register checklist, consent-state transitions — lives in the [`feedback-record-capture` skill](../.cursor/skills/feedback-record-capture/SKILL.md). The README is the source of truth; the skill is how an agent reliably applies it. When the skill and this README disagree, the README wins and the skill is updated to match.

---

## Why this directory exists

Two earlier feedback episodes shaped the project before this directory existed:

- The first practitioner critique recorded in [Exchange #17](../agent/exchanges/first-practitioner-critique-ai-provenance-exchange.md) — a federal-context practitioner who reacted to AI-generated texture and disengaged before evaluating substance.
- A second practitioner — a domain expert in childcare licensing and local-government permitting — who reached the artifact, tried to engage, and reported the project as "too high definition to understand."

The second case made the gap visible: feedback like this is empirical evidence about how the project lands in the world. It deserves to be preserved with the same care the project gives to external source material. Without preservation, the project would be re-deriving lessons from memory each time, with the inevitable distortion that memory introduces.

Preserved feedback records serve three functions:

1. **Preservation.** Capture what the person actually said, in the form they said it, so future exchanges can quote the source rather than paraphrase it.
2. **Pattern recognition.** Multiple records over time make patterns visible — the same friction surfacing across different audiences, or a single record turning out to be idiosyncratic.
3. **Dependency bridging.** Allow exchanges and roadmap updates to reference shared empirical artifacts without each one re-litigating what the practitioner said.

---

## What belongs here

Records that document a real interaction with a real person about the project:

- Outreach messages sent, with the response received.
- Spoken conversations, captured as soon after as possible (with explicit acknowledgment that these are paraphrased).
- Public comments on the project (with attribution per the source's license).
- Survey or structured-prompt responses (when the structured practitioner-critique track of [Roadmap Recommendation 2](../ROADMAP.md) starts producing them).

What does **not** belong here:

- Hypothetical feedback the project imagines a practitioner might give. Use exchanges for that.
- External published commentary not directed at the project specifically. Use `sources/` for that.
- Internal steward notes about feedback. Those belong in exchanges or the roadmap.

---

## Privacy conventions (mandatory)

Practitioner feedback is data about real people. Every record in this directory must:

1. **Default to anonymization.** Use neutral descriptors (e.g., "a practitioner with experience in childcare licensing", "a federal-context practitioner") unless the person has explicitly consented to attribution.
2. **Redact identifying details.** Names, employers, locations more specific than region, and any context that would uniquely identify the person should be redacted unless attribution is consented.
3. **Capture consent state explicitly.** Each record carries a `consent_state` field in the front matter:
   - `not_obtained` (default — anonymize fully)
   - `pending` (steward has asked, awaiting response)
   - `attributed` (consent given for attribution; record names the person)
   - `withdrawn` (was attributed; person has asked to be removed from public record)
4. **Honor withdrawal.** If consent is withdrawn, the record should be re-anonymized in place and the consent_state updated. The historical fact of feedback is preserved; the person's identity is not.
5. **Treat private channels as private.** A text message, DM, or one-on-one conversation is not public commentary. Even if the project preserves the words, they must be anonymized by default.

---

## File naming convention

Feedback record files use lowercase kebab-case with the format:

`feedback-[short-identifier]-[date].md`

Where:

- `[short-identifier]` describes the source neutrally (`childcare-licensing-practitioner`, `federal-hhs-practitioner`)
- `[date]` is `YYYY-MM` of the interaction

Examples:

- `feedback-childcare-licensing-practitioner-2026-04.md`
- `feedback-federal-hhs-practitioner-2026-04.md` (the Exchange #17 anchor case, were it written today)

---

## Front matter schema

Each record opens with the following YAML front matter:

```yaml
---
title: "Feedback Record — [neutral descriptor of source], [date]"
record_type: feedback
interaction_form: text_message | email | spoken_conversation | survey | public_comment
interaction_date: YYYY-MM-DD
domain_expertise: [neutral description of the person's relevant expertise]
consent_state: not_obtained | pending | attributed | withdrawn
provenance: "collaborative"
copyright_notice: "Private communication preserved with privacy protections per feedback/README.md."
---
```

---

## Relationship to exchanges

A feedback record may anchor a single exchange (the way the first practitioner critique anchors [Exchange #17](../agent/exchanges/first-practitioner-critique-ai-provenance-exchange.md)) or may inform multiple exchanges over time. Exchanges should link to feedback records the same way they link to source digests, with full path references.

When a feedback record motivates a new exchange, the exchange's "Why this exchange" section should cite the feedback record and quote the relevant words. The exchange does the analytical work; the feedback record holds the evidence.

---

## Website publication default

Feedback records are **excluded from the public website by default** (the [civicblueprint.org](https://github.com/Civic-Blueprint/civicblueprint.org) content sync excludes the `feedback/` directory). This is a deliberate privacy stance: even when a record is anonymized, the act of publishing it on the project's public site is a separate decision from the act of preserving it in the project repository. Records should be opted-in to website publication explicitly, per record, by removing the directory exclusion or by adding a per-record allow-list — not by default.

The records remain visible to anyone reading the GitHub repo directly, which is consistent with how the project handles its other internal-management artifacts (the Roadmap, the website-submission triage checklist, etc.).

---

## Status (April 2026)

Initial directory. One record present:

- [`feedback-childcare-licensing-practitioner-2026-04.md`](feedback-childcare-licensing-practitioner-2026-04.md) — anchors [Exchange #22 (Entry-Trust Failure with a Domain-Expert Practitioner)](../agent/exchanges/entry-trust-domain-expert-practitioner-exchange.md).

The Exchange #17 anchor case (federal-context practitioner) is not yet retroactively captured here; the original conversation is preserved inline in the exchange itself. If the project later adopts the convention of duplicating those transcripts into `feedback/` for symmetry, that should be a deliberate steward decision rather than an automatic backfill.
