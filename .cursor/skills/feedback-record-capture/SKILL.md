---
name: feedback-record-capture
description: Captures and registers practitioner feedback as preserved artifacts in the `feedback/` directory, enforcing the privacy conventions, front-matter schema, naming convention, and link-and-register checklist defined in `feedback/README.md`. Use when the user shares words a real person said about the project, asks to preserve or capture practitioner feedback, paraphrases a conversation about the project's public surfaces, or wants to update the consent state of an existing feedback record.
---

# Feedback Record Capture

## When this skill applies

This skill fires when:

- The user shares verbatim or paraphrased words from a real person responding to the project (a text exchange, an email, a comment from a meeting, a quote from outreach).
- The user asks to "preserve," "capture," "record," or "save" practitioner feedback.
- The user wants to update the `consent_state` of an existing feedback record (most importantly: a withdrawal request).
- The user is about to write or update an exchange whose evidence base is a real practitioner interaction, and the underlying feedback record does not yet exist in `feedback/`.
- The user mentions a quote they'd like a future exchange to be able to cite.

This skill does **not** fire for:

- Hypothetical practitioner reactions the project imagines. Those belong in exchanges, not in `feedback/`.
- External published commentary not directed at the project specifically. Those belong in `sources/` (use no skill — follow `sources/README.md`).
- Internal steward notes about feedback. Those belong in exchanges or the roadmap.

## Capture-first rule (mandatory)

**Always create the `feedback/` record before writing any analysis of the feedback.** The verbatim words are the artifact; the analysis is downstream and gets cited back to the artifact. If the user opens with "let's start an exchange about what so-and-so said," stop and capture the record first, then hand off to `civic-blueprint-exchange`.

This rule exists because once analysis is written, paraphrase tends to drift. The `feedback/` record is the source of truth for what the person actually said. Future rounds of any exchange should quote the record, not the exchange's own paraphrase.

## Source of truth

Follow `feedback/README.md`. This skill enforces the conventions defined there. If `feedback/README.md` and this skill ever disagree, `feedback/README.md` wins; update this skill to match.

## Required workflow

### 1. Confirm the record is appropriate for `feedback/`

Before creating the file, verify with the user (or yourself, if obvious from context):

- Is this a real interaction with a real person? If hypothetical, redirect to an exchange.
- Was the interaction *about* the project, *about* an artifact the project produced, or *about* a topic where the person engaged with the project's framing? If none of these, redirect to `sources/` (if external published) or to a memo (if it's the steward's own observation).
- Is the channel public or private? Private channels (text, DM, one-on-one conversation) require anonymization by default; public commentary may carry attribution per the source's license.

### 2. Decide the consent state

Pick exactly one from the enum in `feedback/README.md`:

- `not_obtained` — default. The steward has not asked the person whether their words can be preserved/attributed. Anonymize fully.
- `pending` — the steward has asked, response not yet received. Anonymize fully until consent resolves.
- `attributed` — the person has consented to attribution. Record names them and identifying context.
- `withdrawn` — the person was previously attributed and has asked to be removed. Re-anonymize the record in place; do not delete history of the interaction.

When in doubt, default to `not_obtained`. Moving to `attributed` is reversible; moving away from `attributed` is the privacy-protective direction. Do not assume consent from the relational warmth of the interaction.

### 3. Anonymization checklist (run line-by-line on any verbatim transcript)

Before saving, walk through the transcript and the surrounding "Source description" block once with anonymization in mind. For each item below, either redact or confirm it is not present:

- [ ] First name, last name, nickname.
- [ ] Employer, agency, organization (more specific than "federal context" / "state government" / "local municipality").
- [ ] Geography more specific than region (no city, no state if the case is small).
- [ ] Job title in a form unique enough to identify the person (e.g., a director-level title in a small office).
- [ ] Project names, contract names, internal program names the person is associated with.
- [ ] Family relationships and shared friends if those would identify the person to anyone in the steward's network.
- [ ] Uniquely identifying anecdotes (a story that only one person could have lived).
- [ ] Time-and-place context that pinpoints the person (a specific meeting, a specific date and venue).
- [ ] Phone numbers, email addresses, social handles, URLs that would resolve to the person.

If any of these are present and `consent_state != attributed`, redact them or replace with a neutral descriptor before saving.

### 4. Front matter (mandatory schema)

Every record opens with this YAML front matter, in this order, with all fields populated:

```yaml
---
title: "Feedback Record — [neutral descriptor of source], [Month Year]"
record_type: feedback
interaction_form: text_message | email | spoken_conversation | survey | public_comment
interaction_date: YYYY-MM-DD
domain_expertise: "[neutral description of the person's relevant expertise]"
consent_state: not_obtained | pending | attributed | withdrawn
provenance: "collaborative"
copyright_notice: "Private communication preserved with privacy protections per feedback/README.md."
---
```

Validation rules:

- `record_type` is always `feedback` (it is the discriminator that distinguishes these from `sources/` digests).
- `interaction_form` must be one of the five enum values.
- `interaction_date` is `YYYY-MM-DD`, the date of the *interaction*, not the date the record was written.
- `consent_state` must be one of the four enum values.
- `provenance` is usually `collaborative` (steward sets framing, AI drafts, steward approves) or occasionally `human` (steward writes the whole record themselves).
- `copyright_notice` should reflect the channel: use the default for private channels; substitute appropriate text for public commentary (e.g., the source's license).

### 5. File naming

Use the format `feedback-[short-identifier]-[YYYY-MM].md`, lowercase kebab-case:

- `[short-identifier]` is a neutral descriptor of the source's relevant expertise or context. Examples: `childcare-licensing-practitioner`, `federal-hhs-practitioner`, `housing-developer-northeast`.
- `[YYYY-MM]` is the month of the interaction.

Do not use the person's name, initials, or any descriptor that would uniquely identify them, even if `consent_state == attributed`. The filename should be stable across consent transitions.

If two records would collide on the same identifier and month, append a numeric suffix: `feedback-childcare-licensing-practitioner-2026-04-2.md`.

### 6. Record body structure

The body should follow this skeleton (drawn from `feedback-childcare-licensing-practitioner-2026-04.md` as the working template):

1. **Status block.** One sentence on what this file is, plus a "Why this record exists" sentence explaining why the project preserved it.
2. **Source description (anonymized).** Domain expertise, relationship to the project, consent state. Avoid identifying details per the checklist.
3. **Interaction context.** What artifact was shared, what entry path was used, what register the relationship is in (professional, friendly, etc.). Be honest about what was *not* documented.
4. **Transcript (verbatim, anonymized).** The actual words, redacted per the anonymization checklist. Quote with `>` blockquotes.
5. **What the person did *not* say.** Explicit absences that matter for interpretation (this is often as informative as what they did say).
6. **What the person *did* say, decoded carefully.** Sentence-by-sentence interpretation of the language they used. This is the only analysis the record itself should carry; deeper analysis belongs in exchanges.
7. **Initial pattern observations (record-level only).** Brief, narrow observations grounded in the record. Do not reach for project-wide implications here; that's an exchange's job.
8. **What this record does *not* prove.** Honesty about the limits of single-data-point evidence.
9. **How to use this record.** A short instruction set for future exchanges that want to cite the record.

### 7. Link-and-register checklist (mandatory)

After saving the record, complete every item:

- [ ] Update `feedback/README.md` "Status" section to list the new record by file path with a one-line description.
- [ ] If the record motivates a *new* exchange: hand off to the `civic-blueprint-exchange` skill. The exchange's "Why this exchange" section must cite the record path and quote at least one verbatim line. Add the record to the exchange's `Dependency context` section as the anchor feedback record.
- [ ] If the record informs an *existing* exchange: add a forward reference to the exchange's status block (similar to the Exchange #17 → Exchange #22 forward reference), and list the record in that exchange's `Dependency context`.
- [ ] If the record is the second or later instance of a pattern across multiple records: cross-link the records to each other in their respective "Initial pattern observations" sections.
- [ ] Confirm the record is excluded from the public website by default (the `civicblueprint.org/website/scripts/setup-content.sh` rsync excludes `feedback/`). No action is needed unless the steward is opting a record in to publication.

### 8. Consent-state transitions

When the user reports that consent has changed, do not delete the record. Update it in place:

- **`not_obtained` → `pending`.** Steward has asked. Anonymization stays fully in place.
- **`pending` → `attributed`.** Consent given. The steward may add identifying details to the "Source description" block and may revise the transcript to restore redactions. Add a brief "Consent log" subsection at the end of the record noting the date and form of consent. Re-evaluate website-publication status (still defaults to excluded, but is now a steward judgment call).
- **`pending` → `not_obtained`.** Consent declined. Stay anonymized. Add a brief "Consent log" entry noting the decline. Do not retry without an explicit steward request.
- **`attributed` → `withdrawn`.** Re-anonymize the record in place using the anonymization checklist. The verbatim words and the historical fact of the interaction are preserved; identifying details are removed. Add a "Consent log" entry. If the record had been opted-in to website publication, opt it back out immediately.
- **Any state → record deletion.** Do not delete. The record's analytical role is preserved through anonymization, and exchanges that cite the record path would otherwise become broken references.

### 9. Website publication is a separate decision

The default in `feedback/README.md` is that `feedback/` is excluded from the public website. Do not opt a record in to website publication implicitly. If the steward asks to publish a specific record, that requires:

- `consent_state == attributed` (or explicit steward sign-off for an anonymized record).
- A deliberate edit to the website's content sync (either lifting the directory exclusion or adding a per-record allow-list).
- A note in the record itself stating that it is published on the website, so future readers know.

This skill should not perform website-publication changes silently.

## Hand-off to other skills

This skill produces and registers the feedback artifact. It does not own analysis. After the record is saved and registered:

- **If the record motivates a new exchange:** hand off to `civic-blueprint-exchange`. That skill enforces the exchange's status block, dependency declaration, and registration in `_EXCHANGE_INDEX.md`. The two skills compose: feedback record first, then exchange.
- **If the record is empirical input for a broader analytical method:** the project's protocols (Adversarial Review, Coherence Audit, Historical Parallel Test, Comparative Alignment) operate inside exchanges. Reach them via the exchange that consumes the record, not directly from the record.

## Output template

When the skill completes, report back to the user with this structure:

```markdown
## Feedback Record Captured

Record: `feedback/feedback-<identifier>-<YYYY-MM>.md`
Source descriptor: <neutral descriptor>
Consent state: <state>
Interaction form: <form>
Interaction date: <YYYY-MM-DD>

Anonymization: <complete | items redacted: list>
Verbatim quotes preserved: <count>

Registration:
- feedback/README.md Status: updated
- Anchor for: <new exchange #N | existing exchange #N | none yet>
- Cross-references added: <list>

Website publication: excluded (default) | opted-in (deliberate steward decision noted in record)

Next step: <hand off to civic-blueprint-exchange | no further action>
```

## Notes

- The skill enforces the README, not the other way around. If the README changes, update this skill.
- Do not treat the relational warmth of the interaction as evidence of consent. A friendly text message is still a private channel.
- Single feedback records cannot prove structural findings. They can motivate exchanges that test for structural findings. Preserve the distinction explicitly in any record you write.
- If the steward says "let's just paraphrase," push back briefly: the verbatim words are the artifact's whole point. Paraphrase belongs in the exchange that cites the record, not in the record itself.
- The Exchange #17 anchor case (federal-context practitioner) is preserved inline in that exchange rather than in `feedback/`. If a future steward decision retroactively backfills it into `feedback/`, that should be a deliberate action, not an automatic backfill triggered by this skill.
