# Coherence Audit Protocol

> **Status:** Proposed (April 2026). Originated from the [Review Protocol Design Exploration](../exchanges/review-protocol-design-exploration.md), where both the open exploration and adversarial review passes agreed that internal coherence checking is a maintenance need the project cannot afford to leave informal.

---

## The problem this protocol addresses

Civic Blueprint is built on multiple evolving documents: the Principles, the Problem Map, the Systems Framework, CONTRIBUTING.md, and a growing body of exchanges that propose changes to all of the above. Each document is revised independently. Exchanges produce recommendations that may or may not be incorporated. Terms are introduced in one document and referenced in another. Cross-references link specific sections that may move or change.

Over time, this creates coherence decay:

- **Assumption drift.** One document evolves its position on a topic while another document still reflects the older position. The Principles exchange proposed revising Principle 13 (self-determination) to clarify that self-determination operates within the bounds of the substantive commitments. If the Principles are revised but the Systems Framework still references self-determination as unconstrained, the documents contradict each other.

- **Broken cross-references.** The Problem Map references specific Systems Framework sections. The Systems Framework references specific Principles. The README references specific exchanges. When any document is restructured, these references can break silently — no linter catches a Markdown link that points to a section heading that no longer exists.

- **Unincorporated recommendations.** Exchanges produce specific, numbered recommendations for changes to project documents. Some are implemented; some are deferred; some are forgotten. Without tracking, the project loses visibility into what has been proposed versus what has been adopted.

- **Terminological inconsistency.** The project uses terms like "institutional capacity," "recursive uplift," "leverage hypothesis," and "entry-point conditions" across multiple documents. If the definition or scope of a term shifts in one document, other documents may use the term with a meaning that no longer matches.

None of these failures are dramatic. They are slow, cumulative, and invisible until someone reads two documents side by side and notices the gap. By that point, the inconsistency may have been influencing analysis for multiple exchange cycles.

The [Adversarial Review Protocol](adversarial-review-protocol.md) does not catch these problems. It is designed to challenge claims, not to check whether documents agree with each other. A dedicated, lightweight protocol is needed.

---

## Protocol

### 1. Trigger

A coherence audit should be performed:

- **After any major document revision.** If the Principles, Problem Map, Systems Framework, or CONTRIBUTING.md is substantively revised (not typo fixes or minor clarifications), the revised document should be audited against all other core documents.

- **After an exchange produces specific recommendations for document changes.** The audit tracks whether those recommendations have been incorporated or explicitly deferred.

- **On a regular schedule.** Even without a triggering revision, a coherence check should be performed approximately every 3-5 exchanges or at any significant project milestone. Documents can drift even when no single revision causes the drift.

### 2. Scope

Each audit covers two categories:

**Cross-document consistency:**

- Do the core documents agree on their shared claims? Where one document makes an assumption that another document addresses, are the assumptions aligned?
- Do cross-references (links, section references, term usage) still point to the correct content?
- Where a term is used across documents, does it carry the same meaning in each?

**Recommendation tracking:**

- What specific changes have been recommended in exchanges since the last audit?
- Which have been incorporated into the relevant documents?
- Which have been explicitly deferred (with reasoning)?
- Which have not been addressed?

### 3. Process

The auditor reads the revised document (or, for a scheduled audit, each core document in turn) alongside all other core documents. The auditor is not evaluating quality, challenging claims, or proposing improvements. The auditor is checking whether the documents agree with each other.

**Prompt framing:**

> You are auditing the internal coherence of Civic Blueprint's documents. You have been given [Document A] and [Document B]. Your job is not to evaluate either document's quality or challenge its claims. Your job is to find where they disagree with each other.
>
> Specifically:
>
> - Identify passages where Document A states or assumes something that Document B contradicts or does not support.
> - Identify cross-references (links, section references, named concepts) that are broken or point to content that has changed.
> - Identify terms that are used in both documents with different meanings or scopes.
> - Check whether recommendations from recent exchanges have been incorporated into the documents or explicitly deferred.
>
> For each finding, cite the exact passages in both documents and classify the issue:
>
> - **Contradiction:** The documents actively disagree.
> - **Drift:** One document has evolved past the other on a shared topic.
> - **Broken reference:** A cross-reference no longer points to the correct content.
> - **Terminological inconsistency:** A shared term carries different meanings.
> - **Unincorporated recommendation:** An exchange recommended a specific change that has not been adopted or explicitly deferred.

### 4. Output

The audit produces a **coherence checklist** — a flat list of findings, each with:

- The issue type (contradiction, drift, broken reference, terminological inconsistency, unincorporated recommendation)
- The specific passages in each document, cited by document name and section
- A brief description of the inconsistency
- A suggested resolution (not required, but helpful)

The checklist is not a narrative document. It is a maintenance artifact. It should be concise enough to act on directly.

**Example format:**

| # | Type | Document A | Document B | Issue | Suggested resolution |
|---|---|---|---|---|---|
| 1 | Drift | Principles §13 | Systems Framework §14.3 | Principles exchange proposed constraining self-determination within substantive commitments; SF still references self-determination as unconstrained | Revise SF §14.3 to align with the proposed Principle 13 revision, or note that the revision has not yet been adopted |
| 2 | Broken reference | README, Status section | agent/exchanges/ | README references "Post-Systems Framework Next Steps" but the exchange file was renamed | Update the README link |
| 3 | Unincorporated | Principles exchange, rec #3 | Principles | Exchange recommended adding a principle on justice; Principles document has not been revised | Decide whether to adopt, defer, or decline; document the decision |

### 5. Resolution

The coherence checklist is reviewed by the project steward (or, when domain stewards exist, by the relevant steward). Each item is resolved in one of three ways:

- **Fix:** The inconsistency is corrected in one or both documents.
- **Defer:** The inconsistency is acknowledged but deferred to a future revision, with reasoning documented.
- **Accept:** The inconsistency is intentional (e.g., two documents deliberately present different framings of the same topic) and is documented as such.

Unresolved items carry forward to the next audit.

---

## When to apply this protocol

**Always apply after:**

- A major revision to any core document (Principles, Problem Map, Systems Framework, CONTRIBUTING.md)
- An exchange that produces three or more specific recommendations for document changes

**Apply on schedule:**

- Every 3-5 exchanges, or at any named project milestone

**Skip when:**

- The only changes since the last audit are minor editorial fixes (typos, formatting, clarifications that do not change meaning)
- No exchanges have produced document-change recommendations since the last audit

---

## What this protocol does not do

The coherence audit does not evaluate whether the documents are correct, complete, or well-argued. It does not challenge claims or propose improvements. It is a maintenance protocol, not an analytical one.

Its value is preventive: it catches the slow accumulation of inconsistencies that, if left unchecked, would undermine the project's analytical credibility. A project that advocates for institutional competence (Principle 9) should demonstrate it in its own document management.

---

## Relationship to other protocols

- **Adversarial Review Protocol:** The adversarial protocol challenges what the documents say. The coherence audit checks whether the documents agree with each other. They are complementary, not overlapping.
- **Historical Parallel Test Protocol:** The historical parallel test adds new content to the Systems Framework. Each addition is a potential source of coherence drift and should trigger a lightweight coherence check against the relevant Principles and Problem Map sections.

---

## Relationship to project principles

- **Principle 9 (Institutions should be designed for competence and trust, not theater):** A project whose documents contradict each other is not competent. The coherence audit is basic hygiene.
- **Principle 14 (Truth and evidence must be protected as public goods):** Internal inconsistency is a form of misinformation — not deliberate, but corrosive. Catching it early protects the integrity of the project's analysis.
- **CONTRIBUTING.md quality standards:** Contributions must be "honest" and "specific." A project that does not track whether its own recommendations have been implemented is not being honest with itself about its own state.
