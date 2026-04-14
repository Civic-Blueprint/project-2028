# Coherence Audit Protocol

> **Status:** Proposed (April 2026). Originated from the [Review Protocol Design Exploration](../exchanges/review-protocol-design-exploration.md), where both the open exploration and adversarial review passes agreed that internal coherence checking is a maintenance need the project cannot afford to leave informal.

---

## The problem this protocol addresses

Civic Blueprint is built on multiple evolving documents: the Principles, the Problem Map, the Systems Framework, CONTRIBUTING.md, a growing body of exchanges, and now a comparative formation-document track that spans two repositories.

Each document is revised independently. Exchanges produce recommendations that may or may not be incorporated. Terms are introduced in one place and reused in another. Cross-references point across files, folders, and repositories. External source texts are retained as reference material while project-authored analysis interprets them.

Over time, this creates coherence decay:

- **Assumption drift.** One document evolves its position on a topic while another still reflects the older position.
- **Broken cross-references.** Links, section references, and dependency references silently go stale.
- **Unincorporated recommendations.** Exchanges produce specific changes that may be implemented, deferred, or forgotten.
- **Terminological inconsistency.** Terms such as "institutional capacity" or "recursive uplift" can drift in meaning across documents.
- **Source-analysis boundary failure.** An external constitution, charter, or declaration can be treated as if it were editable project prose rather than retained reference material.

None of these failures are dramatic. They are slow, cumulative, and often invisible until someone reads multiple artifacts side by side.

The [Adversarial Review Protocol](adversarial-review-protocol.md) does not catch these problems. It is designed to challenge claims, not to check whether the project's documents, indexes, metadata, and external-source handling still agree with each other. A dedicated maintenance protocol is needed.

---

## Document classes

Before auditing, classify each artifact involved. The allowed resolutions depend on the class.

### 1. Core normative documents

These are the project's substantive commitments and design documents, including:

- [PRINCIPLES.md](../../PRINCIPLES.md)
- [PROBLEM_MAP.md](../../PROBLEM_MAP.md)
- [SYSTEMS_FRAMEWORK.md](../../SYSTEMS_FRAMEWORK.md)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [ROADMAP.md](../../ROADMAP.md)

These are fully auditable for contradictions, drift, broken references, and unincorporated recommendations.

### 2. Project-authored analysis and coordination artifacts

These include:

- `formation-docs/analysis/**`
- `formation-docs/ALIGNMENT_FRAMEWORK.md`
- `formation-docs/SOURCE_REGISTRY.md`
- `agent/exchanges/**`
- `agent/process/**`
- `README.md` and similar project-authored guidance files

These are also fully auditable, but the audit should treat them as interpretation layers rather than as foundational commitments.

### 3. Retained external source corpus

This includes the source repository [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs), especially:

- `documents/**`
- `_source-meta.yaml`
- `SOURCING_POLICY.md`
- `TRANSLATION_WORKFLOW.md`
- `_source-meta-template.yaml`

These artifacts are retained reference material plus source-handling metadata. They are **not** project-authored normative text.

**Hard rule:** the coherence audit must never recommend substantive edits to the meaning of an external source text in order to improve project coherence. If a source and the project differ, the analysis or synthesis layer must absorb that difference rather than rewriting the source.

---

## Protocol

### 1. Trigger

Run a **full coherence audit** when:

- any core normative document is substantively revised
- an exchange produces multiple specific recommendations for document changes
- a new exchange is created or an exchange's status changes
- a major synthesis claim is introduced in `formation-docs/analysis/`
- the project reaches a milestone or approximately every 3-5 exchanges

Run a **lightweight corpus-integrity check** when:

- retained source metadata changes in `external-formation-docs`
- a new formation document is added to the external corpus
- a canonical source URL, translation status, or retention mode changes
- an alignment memo is added or updated without broader project-document revisions

The lightweight corpus-integrity check exists because the comparative track can drift even when the core normative documents have not changed.

### 2. Scope

Each audit covers four categories:

**Cross-document consistency**

- Do the core and project-authored documents agree on shared claims?
- Do links, section references, and named concepts still point to the correct content?
- Where a term is used across documents, does it carry the same meaning?

**Recommendation tracking**

- What changes have recent exchanges recommended?
- Which have been incorporated?
- Which have been explicitly deferred or accepted as open?
- Which have not been addressed?

**Exchange index integrity**

- Does the [Exchange Index](../exchanges/_EXCHANGE_INDEX.md) include every exchange file in `agent/exchanges/`?
- Are status fields in the index consistent with the exchange status blocks?
- Are dependency links accurate and current?
- Are cross-repo artifact references still valid?

**Source corpus integrity**

- Do analysis memos point to the correct retained texts in `external-formation-docs`?
- Do `_source-meta.yaml` files point to the correct analysis artifacts in `project-2028`?
- Are translation-status claims consistent between source metadata and project-authored analysis?
- Has a canonical source or excerpt basis drifted without the analysis acknowledging it?

### 3. Issue types

Classify each finding using the narrowest accurate label:

- **Contradiction:** two project-authored documents actively disagree
- **Drift:** one document has evolved past another on a shared topic
- **Broken reference:** a link, section reference, or dependency path is stale or wrong
- **Terminological inconsistency:** a shared term carries different meanings or scopes
- **Unincorporated recommendation:** an exchange recommended a change that has not been adopted, deferred, or explicitly declined
- **Source-handling error:** a retained source is stored, labeled, or linked in a way that violates the sourcing boundary
- **Translation-status error:** metadata, memo text, or synthesis claims overstate translation certainty
- **Interpretive overreach:** an analysis memo or synthesis artifact claims more than the source text supports
- **Source-analysis mismatch:** metadata, retained text, and project-authored analysis no longer describe the same source basis
- **Canonical-source drift:** the cited canonical source, version, or retained excerpt basis has changed or become uncertain without the corpus acknowledging it

### 4. Process

The auditor reads the relevant artifacts side by side. The job is not to evaluate whether the project is correct. The job is to check whether the artifacts agree with each other and whether the project is handling external sources honestly.

**Prompt framing:**

> You are auditing the internal coherence of Civic Blueprint's artifacts.
>
> First classify each artifact as one of:
>
> - core normative document
> - project-authored analysis / coordination artifact
> - retained external source corpus
>
> Then audit only for coherence and boundary handling.
>
> Specifically:
>
> - Identify contradictions, drift, broken references, and terminological inconsistency across project-authored documents.
> - Check whether recommendations from recent exchanges have been incorporated, deferred, or left unaddressed.
> - Check whether source metadata, retained texts, and project-authored analysis still refer to the same source basis.
> - Check whether translation certainty or canonical-source stability is being overstated.
> - If a retained external source differs from project language, do **not** recommend rewriting the source. Instead, classify whether the problem is in metadata, analysis, synthesis, or interpretation.

### 5. Output

The audit produces a **coherence checklist**: a flat list of findings, each with:

- issue type
- artifact class
- the specific artifacts involved
- a brief description of the inconsistency or drift
- a suggested resolution that respects document boundaries

Suggested format:

| # | Type | Class | Artifact A | Artifact B | Issue | Suggested resolution |
|---|---|---|---|---|---|---|
| 1 | Drift | Project-authored analysis | `ROADMAP.md` | `formation-docs/README.md` | Roadmap still treats the corpus as local while the README describes a two-repo split | Update roadmap wording |
| 2 | Broken reference | Project-authored analysis | `formation-docs/analysis/...` | `external-formation-docs` | Retained-text link still points to the old local path | Update memo link |
| 3 | Translation-status error | Retained source corpus + analysis | `_source-meta.yaml` | alignment memo | Memo calls a translation expert-reviewed but metadata still says AI translated | Lower memo confidence or update metadata after verification |
| 4 | Interpretive overreach | Project-authored analysis | alignment memo | retained source text | Memo claims a source encodes a value the cited clause does not clearly support | Revise memo classification or notes |

### 6. Resolution rules

Each finding is resolved as one of:

- **Fix:** correct the inconsistency
- **Defer:** acknowledge it and carry it forward with reasoning
- **Accept:** document that the difference is intentional

For **core normative documents** and **project-authored analysis**, fixing can include substantive edits.

For the **retained external source corpus**, fixes are constrained. Allowed resolutions include:

- correct metadata
- correct canonical URLs
- replace a retained excerpt with a more faithful excerpt set
- revise translation-status labeling
- revise project-authored analysis or synthesis that misread the source
- open an expert-review request

Disallowed resolution:

- editing an external source text to make it agree with Civic Blueprint's preferred formulation

Unresolved items carry forward to the next audit.

---

## When to apply this protocol

**Always apply after:**

- a major revision to any core normative document
- an exchange that produces multiple specific recommendations for document changes
- a substantial comparative synthesis update that may affect principles, roadmap framing, or exchange dependencies

**Apply lightweight corpus-integrity checks after:**

- adding or replacing a retained source in `external-formation-docs`
- changing translation verification status, canonical URLs, or source metadata that affects project-authored analysis

**Skip when:**

- only minor editorial fixes have occurred
- there are no new exchange recommendations and no corpus-integrity changes since the last pass

---

## What this protocol does not do

The coherence audit does not decide whether the project is morally correct, whether a constitution is good, or whether a comparative synthesis claim is ultimately persuasive. It is a maintenance protocol, not an adversarial or normative one.

It also does not authorize rewriting retained external source texts. Its job is to keep the project honest about where its own interpretation ends and where the source corpus begins.

Its value is preventive: it catches the slow accumulation of inconsistencies that would otherwise undermine the project's analytical credibility.

---

## Relationship to other protocols

- **[Adversarial Review Protocol](adversarial-review-protocol.md):** challenges claims. The coherence audit checks whether artifacts agree and whether source handling is honest.
- **[Comparative Alignment Protocol](comparative-alignment-protocol.md):** governs how external formation documents are mapped against the principles. The coherence audit verifies that the resulting memos, registry entries, metadata, and exchanges remain synchronized.
- **[Historical Parallel Test Protocol](historical-parallel-test-protocol.md):** adds new evidence layers to project-authored analysis. Those additions can create drift and should trigger lightweight coherence checks.
- **Exchange Index and Cursor skill:** the `civic-blueprint-exchange` Cursor skill registers new exchanges in the [Exchange Index](../exchanges/_EXCHANGE_INDEX.md) at creation time. The audit still verifies index accuracy afterward.

---

## Relationship to project principles

- **Principle 4 (Power must remain accountable, legible, and reversible):** the project should be able to explain what changed, where, and why.
- **Principle 9 (Institutions should be designed for competence and trust, not theater):** a project whose own artifacts drift out of alignment is not demonstrating competence.
- **Principle 14 (Truth and evidence must be protected as public goods):** overstating what a source says, or hiding source-handling drift, is a form of epistemic failure.
- **CONTRIBUTING.md quality standards:** the project commits to honesty, specificity, and evidence. Those standards apply to document maintenance too.
