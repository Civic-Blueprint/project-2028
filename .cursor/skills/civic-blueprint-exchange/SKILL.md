---
name: civic-blueprint-exchange
description: Manages Civic Blueprint exchange lifecycle — creating new agent exchanges, registering them in the exchange index, enforcing status blocks and dependency declarations. Use when the user starts a new debate, discussion, adversarial review, or exchange in agent/exchanges/, or asks to create a new exchange document.
---

# Civic Blueprint Exchange Management

## When this skill applies

This skill fires when:
- The user asks to start a new exchange, debate, discussion, or adversarial review
- The user asks to create a new file in `agent/exchanges/`
- The user references starting a new round of discussion on any project topic

## Creating a new exchange

Every new exchange file in `agent/exchanges/` requires three things:

### 1. Status block (mandatory)

The file must open with a status block in this exact format:

```markdown
# [Exchange Title]

> **Status ([Month] [Year]):** [Active discussion | Complete exchange | Superseded by [link]]. [One sentence on what this file captures.]
>
> **Why this exchange:** [2-3 sentences explaining what question prompted this exchange and why it matters now. Reference the specific prior exchange or document that raised the question.]
```

The status block must:
- Include the current month and year
- State whether this is active, complete, or superseded
- Explain *why this exchange is happening now* — what changed, what question was raised, what prior decision is being revisited
- Link to the specific prior exchange or document that motivated it

### 2. Dependency declaration

Before writing the exchange content, identify:
- Which prior exchanges does this one depend on? (What must a reader have read to understand the context?)
- Which core documents does it reference? (Principles, Problem Map, Systems Framework, etc.)
- Which cross-repo artifacts are relevant? (docs in civicblueprint.org)

These dependencies will be recorded in the exchange index.

### 3. Exchange index registration

After creating the exchange file, **immediately** update `agent/exchanges/_EXCHANGE_INDEX.md`:

1. Add a new numbered entry in the "Exchanges (chronological)" section, following the existing format:

```markdown
### [N]. [Exchange Title](filename.md)

| | |
|---|---|
| **Question** | [The central question this exchange addresses] |
| **Depends on** | [Links to prior exchanges and documents] |
| **Produced** | [What the exchange has produced so far — decisions, open questions, document changes] |
| **Status** | [Active discussion | Complete exchange | Superseded] |
```

2. Update the "Dependency graph (visual summary)" ASCII diagram to include the new exchange and its dependency links.

3. If the exchange references or produces artifacts in civicblueprint.org, add a row to the "Cross-repo artifacts" table.

## Updating an existing exchange

When an exchange's status changes (e.g., from active to complete, or when its recommendations are incorporated into core documents):

1. Update the status block at the top of the exchange file
2. Update the corresponding entry in `_EXCHANGE_INDEX.md`
3. If the status change affects other exchanges' dependency context (e.g., a decision in this exchange was revisited by a later one), update those entries too

## File naming convention

Exchange files use lowercase kebab-case: `topic-subtopic-type.md`

Common suffixes:
- `-review` for adversarial or structured reviews
- `-exchange` for exploratory discussions
- `-next-steps` for strategic direction discussions

## Relationship to other protocols

- **[Coherence Audit Protocol](agent/process/coherence-audit-protocol.md):** The coherence audit checks whether the exchange index is current and whether exchange recommendations have been tracked. This skill prevents drift by registering exchanges at creation time rather than catching missing entries after the fact.
- **[Adversarial Review Protocol](agent/process/adversarial-review-protocol.md):** If the new exchange involves adversarial review, reference the protocol in the exchange's role declarations and follow its structural requirements (Option A/B/C, reduced context, alternative framing).

## Checklist

Before considering a new exchange complete:

- [ ] Status block present with month/year, status, and "Why this exchange" section
- [ ] Dependencies identified (prior exchanges, core documents, cross-repo artifacts)
- [ ] `_EXCHANGE_INDEX.md` updated with new numbered entry
- [ ] Dependency graph in `_EXCHANGE_INDEX.md` updated
- [ ] Cross-repo artifacts table updated (if applicable)
- [ ] File name follows kebab-case convention
