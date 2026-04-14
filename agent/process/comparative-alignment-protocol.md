# Comparative Alignment Protocol

> **Status:** Proposed (April 2026). Originated from the constitutional and formation-document analysis initiative, which needs a disciplined way to compare external founding texts against Civic Blueprint's principles without collapsing difference into superficial overlap.

---

## The problem this protocol addresses

Civic Blueprint's [Principles](../../PRINCIPLES.md) are now mature enough to be tested against other formation documents: constitutions, charters, declarations, and organizational founding texts.

That comparison is valuable, but it is easy to do badly.

Without a shared protocol, contributors will drift toward one of three failure modes:

- **False overlap:** reading a vague liberty or justice clause as if it fully matches Civic Blueprint's much more specific commitments
- **False novelty:** treating Civic Blueprint as uniquely insightful when comparable values are already encoded elsewhere under different language
- **False disagreement:** marking a source as opposed to the project when it is actually silent, historically narrow, or working from a different level of abstraction

The project already has protocols for adversarial challenge, coherence maintenance, and historical grounding. What it does not yet have is a protocol for comparative constitutional and formation-document analysis itself.

This protocol supplies that missing layer.

---

## Protocol

### 1. Define the unit of analysis before mapping

Do not map entire documents in one move.

The analyst should identify the relevant units first:

- preamble clauses
- articles
- sections
- chapters
- explicit value statements
- mission or identity statements in organizational texts

The right unit is the smallest one that still carries a coherent value claim.

### 2. Record sourcing and language status before making interpretive claims

Every alignment memo should begin by naming:

- the canonical source
- whether the retained text lives in [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs), and if so whether it is full text, curated excerpts, or metadata only
- whether the analysis relies on the original language, an official translation, an unofficial public translation, or an AI working translation
- whether a native-language expert review is still needed

This slows down a common failure mode: treating a translated or excerpted text as if it were frictionless.

### 3. Use the shared alignment rubric

Each principle-to-source comparison should receive one primary label:

- **Explicit alignment:** the source directly states a substantively similar value or obligation
- **Implicit alignment:** the principle is not stated directly, but a nearby provision or structural pattern clearly points toward it
- **Different resolution:** the source addresses a related tension or value but resolves it differently than Civic Blueprint does
- **Absent:** the source does not materially address the principle
- **Contrary:** the source encodes a conflicting position

These labels should be accompanied by a confidence level:

- **High**
- **Medium**
- **Low**

The confidence rating should reflect textual clarity, translation reliability, and interpretive burden.

### 4. Distinguish text from practice

This protocol analyzes formation documents, not the real-world success of the institutions they created.

If a constitution promises dignity, equality, or participation, the alignment memo should record that textual commitment even if the country routinely violates it in practice.

Practice notes are welcome, but they should be clearly marked as secondary context rather than smuggled into the textual judgment.

### 5. Track source-to-principle alignment and source-specific additions separately

A good memo does two different things:

1. maps the source against the 17 Civic Blueprint principles
2. identifies meaningful source commitments that do **not** map cleanly onto those principles

The second task matters most when the project is trying to discover what it might be missing.

Unmapped but important commitments should be tagged as:

- **Candidate new principle**
- **Candidate subprinciple**
- **Candidate tension note**
- **Candidate implementation note**

### 6. Make tensions explicit rather than forcing resolution

If a source protects liberty strongly but says little about material provision, that may not be mere absence. It may reflect a different theory of freedom.

If a source protects social rights strongly but permits broad emergency power, it may align on substantive ends while diverging on institutional safeguards.

Do not flatten these into "mostly aligned." Name the tension.

### 7. Produce a standard output memo

Each source should generate one file in `formation-docs/analysis/principle-maps/` with the following structure:

1. Source summary
2. Sourcing and language status
3. Alignment table
4. Distinctive commitments and gaps
5. Tensions with Civic Blueprint's current principles
6. Open questions

Suggested table:

| Principle | Alignment | Confidence | Source provisions | Notes |
|---|---|---|---|---|

### 8. Update synthesis artifacts after each completed memo

Once a source memo reaches draft quality, update:

- `formation-docs/analysis/synthesis/alignment-matrix.md`
- `formation-docs/analysis/synthesis/gap-analysis.md`
- `formation-docs/analysis/synthesis/uniqueness-report.md`

This prevents the corpus from becoming a pile of isolated source notes with no cumulative view.

### 9. Escalate consequential findings into exchanges

If multiple sources expose the same missing value, recurring tension, or possible weakness in the current principles, the finding should not remain buried in a memo.

Open or extend an exchange when:

- a likely new principle is emerging
- a current principle appears internally unstable under comparison
- a strong synthesis claim is being made about what "most formation documents" do or do not support

That exchange should then be testable under the [Adversarial Review Protocol](adversarial-review-protocol.md).

---

## When to apply this protocol

Use this protocol when:

- a new formation document is added to [`external-formation-docs`](https://github.com/Civic-Blueprint/external-formation-docs)
- the project wants to compare a source systematically against [PRINCIPLES.md](../../PRINCIPLES.md)
- a contributor wants to argue that a current principle is widely shared, weakly grounded, unusually novel, or missing a common counterpart
- synthesis files are being updated from multiple source memos

Lightweight citation or casual comparison does not require the full protocol. Claims intended to influence the Principles document, roadmap, or project narrative do.

---

## What this protocol does not do

This protocol does not decide whether a source is morally correct.

It does not resolve jurisprudential disputes about how a constitution should be interpreted.

It does not tell the project whether to imitate a source.

What it does is make comparison more disciplined. It helps the project say, with some rigor, "Here is where this source overlaps with us, where it diverges, what it adds, and how confident we are in that reading."

---

## Relationship to sibling protocols

This protocol is one of four structured review protocols the project now uses. Each addresses a different failure mode:

- **Comparative Alignment Protocol (this document):** Compares external formation documents to Civic Blueprint's principles. Surfaces overlap, divergence, silence, and missing values.
- **[Adversarial Review Protocol](adversarial-review-protocol.md):** Challenges claims. Tests whether strong conclusions drawn from the comparative corpus are actually defensible.
- **[Coherence Audit Protocol](coherence-audit-protocol.md):** Checks internal consistency. Ensures synthesis findings, roadmap entries, and principles updates remain aligned.
- **[Historical Parallel Test Protocol](historical-parallel-test-protocol.md):** Grounds reform or institutional claims in historical evidence rather than textual aspiration alone.

The four protocols are complementary:

- Comparative alignment asks: **"What values and design commitments are encoded here?"**
- Adversarial review asks: **"Are our conclusions from that comparison too confident?"**
- Coherence audit asks: **"Have we integrated the findings consistently?"**
- Historical parallel test asks: **"What happened when these commitments were operationalized?"**

---

## Relationship to project principles

This protocol operationalizes several of Civic Blueprint's existing commitments:

- **Principle 10 (The future should be built in the open):** Comparative analysis should be explicit about sources, translation status, and interpretive uncertainty.
- **Principle 13 (Pluralism and self-determination are strengths, not obstacles):** The protocol treats difference as analytically valuable rather than as noise to be normalized away.
- **Principle 14 (Truth and evidence must be protected as public goods):** Comparative claims should rest on cited provisions, not vibes or prestige.
- **Principle 16 (Justice mediates between competing claims):** Many of the most important source comparisons involve competing rights or institutional tradeoffs. This protocol is designed to surface those tensions rather than hide them.
