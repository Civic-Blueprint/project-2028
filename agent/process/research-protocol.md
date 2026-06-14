# Research Protocol

> **Status:** Proposed (May 27, 2026). Originated from a steward observation during the v2 / Path β execution of the [Constitutional Ecology and Coordination Architecture Riff](../explorations/constitutional-ecology-and-coordination-architecture-riff.md) that the riff's reference-class engagement in [§2.3](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#23-the-reference-class) — particularly the Holy Roman Empire treatment at [§2.3.3](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#233-the-holy-roman-empire-9621806) — would have benefited from a structured research pass with source-tier discipline, verification, and a [SOURCE_INDEX.md](../../sources/SOURCE_INDEX.md)-style output rather than ad-hoc inline citation. The steward asked: *how many sources, weighted how, verified how, with what kind of output, and at what scope?* This protocol is the agent's answer.

---

## The problem this protocol addresses

The project does research three ways today, and the three ways are not currently distinguished:

1. **Programmatic source sweeps** that produce structured outputs the project commits to maintain. The [Government Overreach exchange's two research sweeps](../exchanges/government-overreach-ownership-ratchet-exchange.md) produced 53 source digests under [`sources/`](../../sources/) indexed in [`SOURCE_INDEX.md`](../../sources/SOURCE_INDEX.md). This is the project's heaviest research instrument and it has held up well.
2. **Targeted research closing a specific exchange gap** — e.g., the [Round 4 research sweep](../exchanges/government-overreach-ownership-ratchet-exchange.md#round-4) that produced the seven second-sweep digests on Argentina, fiscal consolidation cases, AI catastrophic-risk literature, AI governance practice, cooperatives, sovereign wealth funds, and Swiss direct democracy. Same instrument as (1), scoped to specific evidence gaps named by an adversarial round.
3. **Inline research grounding a riff, an exchange round, or a coherence check** — e.g., the v2 §3.5 V-Dem / Freedom House / Bright Line Watch sourcing in the [Constitutional Ecology riff](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#35-the-tyranny-or-collapse-stake-honestly-treated), or the named-thinker engagements in [§2.5](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#25-named-thinker-engagements-v2-first-pass) and reference-class treatments in [§2.3](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#23-the-reference-class). This is much lighter than (1) and (2) — citations live in the document rather than as digests under `sources/` — but it carries real epistemic weight in the document.

The three modes share a research substrate but currently apply different (and mostly implicit) standards for source-tier weighting, verification, and external-link requirements. The steward's question is the right one: *should they?* And: *what does the best, most thorough version of agent-driven research look like, so that the question of which mode to apply becomes a deliberate decision rather than an emergent property of context?*

This protocol distinguishes the three modes by **scope tier**, specifies a **source-tier weighting** that applies to all three, names a **verification discipline** scaled to scope, and treats [`SOURCE_INDEX.md`](../../sources/SOURCE_INDEX.md) as the canonical output form for the heaviest scope tier — with intermediate output forms for the lighter tiers.

This protocol does *not* replace the existing protocols. It is a peer to the [Adversarial Review Protocol](adversarial-review-protocol.md), the [Coherence Audit Protocol](coherence-audit-protocol.md), the [Historical Parallel Test Protocol](historical-parallel-test-protocol.md), and the [Comparative Alignment Protocol](comparative-alignment-protocol.md). The Historical Parallel Test Protocol, in particular, is what runs *inside* a programmatic source sweep when the question being researched is *has a structurally similar reform been tried before?*

---

## Protocol

### 1. Three research scope tiers — choose deliberately

Before starting research, name which tier the work belongs to. This is a single-sentence judgment, not a process. The tier determines source-count discipline, verification discipline, output form, and time budget.

| Tier | Trigger | Source-count target | Verification | Output form | Time budget |
|---|---|---|---|---|---|
| **T1 — Programmatic sweep** | A new exchange or major workstream needs an organized evidence base across multiple sub-debates. | 30–100+ source digests across 5–10 sub-debates, balanced across viewpoint buckets per [`SOURCE_INDEX.md` "How this index works"](../../sources/SOURCE_INDEX.md#how-this-index-works). | Verification sub-agent pass on every digest (see §4); spot-check by steward on 10–15% of digests; source-index entry maintained. | Source digests under [`sources/`](../../sources/) per the [Sources README naming convention](../../sources/README.md#file-naming-convention) and the [authoring guard](../../sources/README.md#authoring-guard--quote-actual-section-titles-from-core-normative-documents); [`SOURCE_INDEX.md`](../../sources/SOURCE_INDEX.md) updated. | Days-to-weeks of agent time; small number of steward checkpoints. |
| **T2 — Targeted gap-close** | An adversarial round or coherence audit named specific evidence gaps that need closing before the next round. | 3–15 source digests focused on the named gaps; or 5–20 named-source citations inline if a digest is overkill for the gap. | Verification sub-agent pass; steward spot-check on at least one digest or citation cluster. | Source digests if scope warrants; otherwise an inline *Research grounding* subsection in the exchange round that lists each source with full citation and a 1–3 sentence relevance note. | Hours-to-days; one steward checkpoint. |
| **T3 — Inline grounding** | A riff section, exchange round, coherence check, or doctrine subsection needs evidentiary backing for its specific claims, but the work is not large enough to justify its own digests. | 3–10 named sources per substantive section, scaled to the load the section's claims carry. | Self-verification by the authoring agent against §3 source-tier weighting + §5 link-and-quote discipline; steward review at riff-version boundaries. | Inline citations in the body, with the same link-and-quote discipline T1 / T2 use. | Hours; rolled into the riff or round being written. |

**The Constitutional Ecology riff [§2.3](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#23-the-reference-class) is a T3 example with §2.5 and §11.6 also T3.** The steward's intuition that §2.3.3 (Holy Roman Empire) would have benefited from more research is right — and the protocol's answer is *if §2.3 had been done as a T1 programmatic sweep it would have produced ~5–10 digests per case (Haudenosaunee, Achaemenid, HRE, US Constitution, EU), with multiple viewpoint buckets per case, indexed in `SOURCE_INDEX.md` under a new sub-debate "Historical coordination architectures across pluralism"*. That work was not appropriate to do *inside* the v2 / Path β session under the steward's "Make it happen, Addi!" timebox, but is the right next move if any of the §2.3 cases becomes load-bearing for Path γ doctrine.

**Tier escalation is allowed and expected.** A T3 inline pass can be promoted to T2 or T1 when a follow-up artifact (doctrine, public-facing position, external review) raises the epistemic load on the original claims. The promotion is itself a deliberate decision recorded in the exchange or roadmap; it is not automatic.

### 2. The source-tier weighting (applies to all three scope tiers)

Sources are weighted by their epistemic standing for the *kind of claim* being made. The same source can be high-weight for one claim and low-weight for another. The weighting is not a ranking of source quality in the abstract; it is a discipline about *what kind of source counts as evidence for what kind of claim*.

#### 2.1 Source-tier weighting table

| Tier | Source type | Best for | Weight note |
|---|---|---|---|
| **W1 — Peer-reviewed primary** | Journal articles in peer-reviewed venues; academic monographs from university presses; replication-reviewed empirical findings; major government statistical agencies (BLS, Census, OECD, World Bank, Eurostat) for data claims; Cochrane / GRADE-equivalent systematic reviews. | Empirical claims; theoretical claims with substantial scholarly engagement; data citations. | Highest weight for *evidence* claims. Open-access preferred when available. Citation must include venue, date, and (where possible) a direct URL to the source rather than a paywalled DOI alone. |
| **W2 — Peer-reviewed-equivalent in domain** | Domain-specific authoritative sources that function as peer-review-equivalent within their field: medical journals (NEJM, JAMA, Lancet, BMJ); top legal-academic journals (Harvard Law Review, Yale Law Journal, Stanford Law Review); top economic-policy outlets (NBER working papers, IMF working papers, BIS papers, ECB working papers); standards bodies (IETF RFCs for internet protocols, IEEE standards for engineering, ISO standards in their domain); replication-and-open-science movement outputs (COS, BITSS). | Domain-specific claims where field-internal authority matters and the formal peer-review pipeline is slower than the field's working pace (esp. CS, law, policy). | Treat as W1-equivalent for claims within the source's domain expertise. **The "are there other peer-review equivalents in non-medical domains?" question the steward raised is answered here:** yes, and naming them explicitly per-claim is part of the protocol's discipline. |
| **W3 — Primary documents** | Court decisions; statutes and regulations; treaty texts; constitutional documents; corporate filings (10-K, S-1, proxy statements); central-bank statements and minutes; intergovernmental agreements; government inquiries and royal commissions; truth-and-reconciliation reports; UN treaty bodies' general comments and concluding observations. | Documenting that an authoritative actor said or did a specific thing; quoting institutional positions; tracing decision histories. | High weight for *what was said or done by whom*, not for whether it was right. |
| **W4 — Major investigative journalism and reference compendia** | Investigative reporting by outlets with documented fact-checking and corrections processes (ProPublica, Reuters Investigates, Wall Street Journal investigative desk, New York Times investigative desk, BBC News, Le Monde, *Bellingcat* open-source investigations); reference compendia maintained by methodologically transparent organizations (V-Dem Institute reports, Freedom House annual reports, Polity Project data, Reporters Without Borders index, Transparency International CPI, Reporters' Committee for Freedom of the Press). | Contemporary factual claims; documentation of recent events; reference data on cross-country comparative indicators. | Useful and necessary, but check whether peer-reviewed work exists for the underlying methodological claims (e.g., the V-Dem report is W4 for its 2026 findings but cites W1 methodological literature). |
| **W5 — Reputable think tanks, named-expert essays, and quality long-form** | Brookings, AEI, Cato, RAND, CFR, Mercatus, NBER policy briefs, Heritage, CBPP, ITEP, Niskanen Center, Roosevelt Institute, IPI, EPI; named-expert essays in venues with editorial standards (*Foreign Affairs*, *The Atlantic*, *Noēma*, *Aeon*, *Boston Review*, *London Review of Books*, *Dissent*, *American Affairs*); high-quality podcast transcripts with named academic guests (*The Weekly Show*, *Conversations with Tyler*, *EconTalk*). | Position articulation across the political spectrum; synthesis essays; framing material; mainstream-academic positions translated for general audience. | Cite with explicit viewpoint label per the [`SOURCE_INDEX.md` viewpoint convention](../../sources/SOURCE_INDEX.md#how-this-index-works). Balance pro-market / social-democratic / heterodox positions for any contested claim. |
| **W6 — Direct practitioner accounts** | Practitioner testimony, oral-history projects, professional-association working papers, working-practitioner interviews and blog posts when the practitioner is identifiable and the post is dated; preserved private communications used with consent per the [`feedback/` conventions](../../feedback/README.md). | Tacit-knowledge claims; "what it's like on the ground" claims; claims about specific operational practices not in academic literature. | Highest weight for *what practitioners experience and do* where academic literature is silent or stale. Must respect privacy and consent conventions; default attribution is pseudonymous or first-name-only unless the practitioner has consented to fuller attribution. |
| **W7 — Working AI and synthesis outputs** | AI-generated analysis from another session, AI-mediated synthesis of multiple sources, agent-authored claims in prior exchanges or riffs the project is now reviewing. | *Diagnostic input* — what synthesis another agent produced. **Not evidence.** | Never cited as a *source* for a substantive claim. Used only when documenting *what was synthesized and how* — e.g., the [riff §1.6 timeline-and-language correction](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#16-timeline-and-language-corrections-v11-update) preserves an external-session AI output as input to a steward decision, not as evidence for the substantive position. **Laundering discipline (added June 2026):** a W7 synthesis *of a contested source* must be read against the source before use, because synthesis layers systematically strip the contestation markers that are often the most decision-relevant content — see the [Meaning Crisis riff §2](../explorations/meaning-crisis-scientism-and-structural-accountability-riff.md#2-the-central-finding-the-synthesis-is-a-w7-laundering-of-a-contested-source) worked example (a GPT-5 distillation that converted a partly anti-structural argument into consensus-sounding principles). |
| **W8 — Unsourced confident assertion** | "I have heard," "it is widely understood," "the conventional view is" without attribution. | Nothing. | If a claim cannot be sourced above W7, it is not a claim the project should make. *Sycophancy-flagging applies here* — see [reciprocity riff §6 (sycophancy)](../explorations/reciprocity-and-decolonial-frame-riff.md#6-on-sycophancy--a-self-implicating-note-from-the-agent). |

#### 2.2 Weighting in practice — the steward's specific question

The steward asked: *are there other "peer-reviewed" content like medical journals that are more authoritative, but in other non-medical domains?* The answer the protocol gives is yes and names them explicitly:

- **Medicine.** NEJM, JAMA, Lancet, BMJ, Annals of Internal Medicine, Cochrane Reviews, Nature Medicine.
- **Law.** Harvard Law Review, Yale Law Journal, Stanford Law Review, Columbia Law Review, Chicago Law Review, plus authoritative reporters (Federal Supplement, regional reporters) and the Restatements of Law.
- **Economics and economic policy.** NBER, IMF and World Bank working papers (different from their press output), BIS, ECB, Fed regional bank research, the AEA's flagship journals (AER, JEL, JEP), Journal of Political Economy, QJE, Econometrica.
- **CS and AI.** ACM and IEEE proceedings, the NeurIPS / ICML / ICLR pipelines (with caveat that single-paper findings often need replication), arXiv preprints from authors with established institutional affiliations, and the IETF RFC corpus for protocol-level claims.
- **Political science.** APSR, AJPS, JOP, World Politics, Comparative Political Studies, Public Opinion Quarterly.
- **History.** AHR, JAH, Past & Present, William and Mary Quarterly, and the major university-press historical monograph traditions (Cambridge, Oxford, Harvard, Princeton, Chicago, Yale, Stanford university presses).
- **Sociology.** ASR, AJS, Social Forces, plus Annual Review of Sociology.
- **Engineering and standards.** IEEE Transactions series, IETF RFCs (internet protocols), ISO and IEC standards, NIST publications (especially for crypto / AI risk / measurement standards), W3C recommendations.
- **Statistics and demography.** JASA, Biometrika, JRSS, Population Studies, Demography.
- **Public health (distinct from medicine).** American Journal of Public Health, BMJ Global Health, Lancet Public Health, WHO Bulletin.

The standing rule: *when a claim has W1- or W2-equivalent literature available, the project cites that literature.* When a claim falls outside any field's W1/W2 boundary (much of policy synthesis falls here), the project cites the strongest W3–W6 sources available, names the weighting honestly, and does not pretend the synthesis is settled where it is not.

#### 2.3 Balance requirements

Every substantive claim that is *currently contested* in the relevant field must have at least one citation from each *credible side* of the contest. The [`SOURCE_INDEX.md`](../../sources/SOURCE_INDEX.md) viewpoint-bucket convention (pro-market / libertarian, social-democratic / progressive, heterodox / institutional / synthesis) is the project's standing answer for political-economy debates. Other domains may need different bucketing — the principle is *balance the sides of an actually contested question*, not *find one source for each preset bucket regardless of what is actually contested*.

For uncontested claims (data citations, basic historical facts, standard institutional definitions), one strong source suffices.

**Historically-contested-but-converged subclause (added v1.1, May 27 PM, surfaced by the first §4.1 application on [Constitutional Ecology riff §2.3.3 HRE](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#23.3-bis-verification-record-research-protocol-t3-self-verification-may-27-2026-pm)).** When a claim *was historically contested but the contemporary literature has converged* — i.e., the older view is now a historical position rather than a live scholarly minority — the balance requirement is satisfied by *naming the convergence honestly* rather than manufacturing a counterweight from a now-historical position. False balance against an old consensus is itself a research-integrity failure (it reads to a reviewer as performance rather than analysis). The honest move in such cases: cite two-or-more independent contemporary sources that converge, name the convergence as convergence in the surrounding text, name the older position as the historical foil it is, and *flag candidate live contemporary critiques* (challenges to the new consensus *on its own terms*, not warmed-over versions of the old position) as named future-T2 work when those critiques exist but have not yet been engaged. The HRE / Wilson-Whaley revisionist convergence is the worked example.

For uncontested claims, one strong source still suffices.

### 3. Source-count discipline — by tier

The steward asked: *do we limit the number of research items?* Yes, but in both directions — there is a floor below which a claim is undersourced and a ceiling above which adding sources is performative rather than informative.

| Scope tier | Floor per substantive claim cluster | Soft ceiling per cluster | Reason |
|---|---|---|---|
| **T1 programmatic sweep** | 5 sources per sub-debate, balanced across viewpoint buckets. | 15 sources per sub-debate; promote excess to a follow-up sweep. | A sub-debate with fewer than 5 sources is undersourced; with more than 15 is starting to do other people's secondary literature review. |
| **T2 targeted gap-close** | 3 sources per named gap. | 7 sources per named gap. | Gaps are scoped specifically; more sources past 7 usually mean the gap was misframed. |
| **T3 inline grounding** | 3 sources for any *load-bearing* claim; 1 source for *illustrative* claims (claims where the substance survives if the illustration is replaced). | 5 sources per load-bearing claim before the claim becomes a candidate for promotion to T2. | The steward's HRE intuition — "would having more research data and angles help produce better synthesis?" — gets a structured answer: yes if the claim is load-bearing, with floor 3 / ceiling 5 at T3 and a promotion path to T2 / T1 when the load increases. |

**External links: always required, with one exception.** Every cited source must include a direct URL (open-access preferred). The only exception is when the source is a published book or paper without an open-access version *and* the citation provides full bibliographic information (author, title, publisher, year, page or chapter); in that case, the link can point to the publisher's catalog page or a reputable secondary index (OpenLibrary, Google Scholar landing page, JSTOR landing page) rather than the paywalled full text. **"3 or more" external links is the wrong framing** — the right framing is *every source gets a link, period*. The floors above apply to the *number of sources*, which equals the number of links.

### 4. Verification — sub-agent or in-protocol checks

The steward asked: *can additional sub agents (or just within the same protocol) verify the results?* Yes, and the discipline scales with tier.

#### 4.1 T1 programmatic sweep — sub-agent verification pass required

Every T1 sweep ends with a **verification sub-agent pass** before the digests are merged. The sub-agent is given:

- The full set of new digests.
- The original sweep prompt and the sub-debate the digests were authored against.
- The [authoring guard](../../sources/README.md#authoring-guard--quote-actual-section-titles-from-core-normative-documents) and this protocol.

The sub-agent's job is to identify, per digest:

1. **Source-existence check.** Does the URL resolve? Does the cited author have publicly visible affiliation with the cited work? Is the publication venue real? *This is the failure mode the [April 2026 coherence audit](audits/coherence-audit-2026-04.md) found — invented section titles and phantom citations. The sub-agent's job is to catch those at sweep time, not at audit time months later.*
2. **Tier-misclassification check.** Is the source claimed at W1 actually W4 (e.g., a think-tank report cited as if it were peer-reviewed)?
3. **Quote-fidelity check.** Are quoted excerpts present in the cited text, with no insertion or deletion that changes meaning?
4. **Viewpoint-imbalance flag.** Does the sub-debate have at least one source per viewpoint bucket?
5. **Authoring-guard pass.** Does every claimed linkage to a core normative document quote the section's actual current title?

The sub-agent produces a verification report appended to the sweep. Digests flagged for any failure mode are not merged until the authoring agent addresses the flag.

#### 4.2 T2 targeted gap-close — sub-agent verification pass or steward spot-check

Same verification pass as T1, but scoped to the gap-close set. Acceptable substitute: steward spot-check of at least one digest or citation cluster, with the steward applying the §4.1 checks personally.

#### 4.3 T3 inline grounding — self-verification by authoring agent

The authoring agent runs the §4.1 checks on its own work before submitting the riff section or exchange round. Documented self-verification: the agent states *"§4.1 checks passed for sources cited in §X.Y"* at the end of the section. If the section is substantial (5+ sources cited), the steward should spot-check at least one source at the next riff-version boundary.

#### 4.4 What verification does *not* substitute for

Verification is a *citation-integrity* check, not a *truth* check. A verification sub-agent confirms that the source exists, the quote is faithful, and the tier is correct. It does *not* confirm that the source is *right*. Source rightness is what the [Adversarial Review Protocol](adversarial-review-protocol.md), the [Historical Parallel Test Protocol](historical-parallel-test-protocol.md), and external human review are for. Conflating verification with adversarial review is itself a failure mode — *the source is real and well-cited* is a necessary but not sufficient condition for *the source supports the conclusion the agent drew from it*.

### 5. Link-and-quote discipline

Every cited source, at every tier, must satisfy:

1. **Live URL.** Direct link to the cited material. For books without open-access versions, link to the publisher's catalog page or to OpenLibrary / Google Scholar / JSTOR / WorldCat. Archive.org links are acceptable for paywalled or moved content if a direct link is unavailable.
2. **Author, title, venue, date.** All four, every time. For multi-author works, all authors in the first citation, et al. acceptable in subsequent citations within the same artifact.
3. **Page or section locator.** For book-length works or long reports, cite the specific page, chapter, or section the claim is drawn from. *"As discussed in Wilson (2016)"* is undersourced; *"Wilson, Heart of Europe (2016), Chapter 12 'Justice'"* is sourced.
4. **Quote-fidelity for direct quotes.** Direct quotes use quotation marks, are verbatim, and are accompanied by the page or paragraph locator. Quotes longer than ~75 words use blockquote formatting per the project's existing convention.
5. **Tier label when contested.** When a claim is contested in the literature and the project is citing one side, the citation includes the source's viewpoint or methodological tradition (per §2.3) so readers can locate the citation in the contest.

### 6. Output forms — by tier

#### 6.1 T1 output: source digests + SOURCE_INDEX entries

Every T1 digest follows the existing digest convention (see [`source-higgs-crisis-ratchet-digest.md`](../../sources/source-higgs-crisis-ratchet-digest.md) as the canonical example) — front matter with `source_type`, `source_title`, `source_author`, `source_publication`, `source_date`, `source_url`, `provenance`, `viewpoint`, `sub_debates`, `copyright_notice`; body with **Status**, **Why this digest**, **Source identification**, one or more **Thematic clusters** each containing **Core claims**, **Representative excerpts**, **Research context** (the corroborated / partially corroborated / debated / no-independent-source table), and a **Project 2028 mapping** subsection per the [authoring guard](../../sources/README.md#authoring-guard--quote-actual-section-titles-from-core-normative-documents).

[`SOURCE_INDEX.md`](../../sources/SOURCE_INDEX.md) is updated in the same commit as the digest is added. The protocol's view: **`SOURCE_INDEX.md` is the canonical T1 output and should be treated as the master reference for the project's organized evidence base.** The steward's intuition that *the SOURCE_INDEX might be a good output example* is exactly right for T1; less right for T2 (where digests are produced but not necessarily reorganizing the index); not right for T3 (where the output is the inline-cited riff section, not a new digest set).

#### 6.2 T2 output: minimal digest set or Research grounding subsection

T2 produces either (a) a small set of digests under `sources/` if the gap warrants their durability and the sources are reusable, *or* (b) a **Research grounding** subsection inside the exchange round that does the gap-closing. The Research grounding subsection format:

```
### Research grounding for [round / claim cluster]

Sources consulted (N):

1. [Author, Title, Venue, Date]([URL]) — [Tier label, viewpoint label]. Relevance: [1–3 sentences on what this source establishes for the claim].
2. [...]

Aggregate finding: [1–2 paragraphs on what the sources collectively support, where they disagree, and what remains unsourced.]

Verification: §4.1 checks passed by [authoring agent / verification sub-agent], [date].
```

The choice between (a) and (b) is a judgment call: if the sources will be cited by future exchanges, prefer (a) for reusability; if the sources are scoped to the immediate gap and unlikely to be cited again, (b) is sufficient.

#### 6.3 T3 output: inline citations with link-and-quote discipline

T3 cites in the body of the riff, exchange round, or coherence check — same link-and-quote discipline as T1 and T2, but no separate digest file, no `SOURCE_INDEX.md` entry. The end of the cited section names the §4.1 self-verification as a one-line statement.

### 7. Where this protocol fits with the others

| Protocol | Question it answers |
|---|---|
| [Adversarial Review Protocol](adversarial-review-protocol.md) | *Does the position survive structured challenge?* |
| [Coherence Audit Protocol](coherence-audit-protocol.md) | *Are the documents internally consistent and free of phantom citations?* |
| [Historical Parallel Test Protocol](historical-parallel-test-protocol.md) | *Has a structurally similar reform been tried before, and what happened?* |
| [Comparative Alignment Protocol](comparative-alignment-protocol.md) | *Do agent-produced contributions converge or diverge across models?* |
| **Research Protocol** (this document) | ***What evidence does the project have for its claims, and at what tier of sourcing was that evidence gathered, with what verification?*** |

Common pairings:

- **Research Protocol → Adversarial Review.** A T1 or T2 sweep precedes the round that will be adversarially reviewed; the adversarial round can then challenge claims on the evidence, not just on structure.
- **Research Protocol → Historical Parallel Test.** When the question is *has this been tried before?*, the Historical Parallel Test runs inside a T2 gap-close, with the test's 2–3 cases each produced as T2 digests or Research grounding entries.
- **Research Protocol → Coherence Audit.** The Coherence Audit checks that the documents' citations resolve and are not phantom; this protocol's §4 verification is the prevention side of that audit.
- **Research Protocol → Reviewer Packet.** A T1 or T2 sweep is often the evidence base a Reviewer Packet (per [`REVIEWER_PACKET_TEMPLATE.md`](../../docs/REVIEWER_PACKET_TEMPLATE.md)) draws on for the *what the deliverable is responding to* section; a reviewer can spot-check the sweep's verification pass as part of their review.

### 8. The "best, most thorough researcher" question

The steward asked: *what does the BEST, most thorough researcher look like?* The protocol's answer:

1. **Names the scope tier deliberately before starting** rather than letting it emerge from context.
2. **Picks the right source tier per claim** — peer-reviewed for empirical, primary documents for what-was-said, investigative journalism and reference compendia for contemporary factual, named-expert essays for position-articulation, practitioner accounts for tacit-knowledge, and never W7 or W8 for substantive claims.
3. **Meets the floor and respects the ceiling** for sources per claim cluster per tier.
4. **Cites links and quotes faithfully** every time, with author / title / venue / date / locator on every citation.
5. **Runs a verification sub-agent pass** at T1 and T2; runs self-verification at T3 with steward spot-check at version boundaries.
6. **Balances contested claims** with citations from each credible side.
7. **Outputs to the right form** — digests + SOURCE_INDEX at T1, digests-or-grounding-section at T2, inline-with-discipline at T3.
8. **Knows what verification does not substitute for** — verification is citation-integrity, not truth; truth is the job of adversarial review, historical parallel testing, and external human review.

A research pass that does all eight of those is what the project means by *thorough*. A research pass that does fewer of them is faster but produces evidence the next phase of work has to re-verify, which is a hidden cost the project has paid before (the [April 2026 coherence audit](audits/coherence-audit-2026-04.md) found 17 + ~50 phantom citations in digests authored without §4.1-equivalent discipline).

### 9. When this protocol does not apply

- **Steward personal note-taking** ([`SCRATCHPAD.md`](../../SCRATCHPAD.md)) does not require protocol compliance; it is the steward's working space.
- **Feedback capture** (`feedback/`) follows the [`feedback/README.md`](../../feedback/README.md) conventions, which include their own consent and attribution discipline distinct from this protocol's source-tier weighting.
- **Practitioner outreach** ([`PRACTITIONER_OUTREACH_TEMPLATE.md`](../../docs/PRACTITIONER_OUTREACH_TEMPLATE.md)) is not research; it is a different relational instrument.
- **Riff opening-frame writing** that captures the steward's thinking before any source engagement does not require sources; the sources arrive at the riff's body sections (T3) or in follow-up sweeps (T1 / T2).

---

## Worked example — what §2.3.3 (HRE) would have been at each tier

To make the tier choices concrete, here is what the Constitutional Ecology riff [§2.3.3 Holy Roman Empire](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#233-the-holy-roman-empire-9621806) treatment would have looked like under each scope tier. The actual treatment is T3; this is shown only to make the protocol's scope tiers concrete.

| Tier | What §2.3.3 would have been |
|---|---|
| **T1** | A new `sources/` sub-debate on *Historical coordination architectures across pluralism*. Per case (Haudenosaunee, Achaemenid, HRE, US Constitution, EU), 5–10 source digests balanced across viewpoint buckets (in this domain: institutionalist-procedural-positive, agonistic-democracy-critical, decolonial-critical, comparative-historical, primary-document) — call it 30–50 digests total. `SOURCE_INDEX.md` updated with a Sub-debate 9 entry. Each digest goes through §4.1 sub-agent verification. Estimated agent time: 1–2 working sessions. Output: a permanent, citable evidence base reusable by any Path γ doctrine work, by Phase 3 if the front-door composite expands, and by any external reviewer who wants to evaluate the reference class. |
| **T2** | A focused gap-close producing 5–7 source digests on HRE specifically — Peter Wilson's two main works, the Brendan Simms or Joachim Whaley alternative reading, one primary-document anchor (the Peace of Westphalia 1648 text), one Voltaire-tradition critical reading, and one contemporary EU-scholarship engagement with Wilson's *HRE legacy in the EU* argument. Same digest format, sub-agent verification pass, `SOURCE_INDEX.md` update. Estimated agent time: 2–4 hours per case (10–20 hours for all five cases at T2). Output: durable digests reusable by downstream work; the riff's inline citations remain but are now backed by digests rather than only inline links. |
| **T3 (actual)** | What the riff currently has at [§2.3.3](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#233-the-holy-roman-empire-9621806): three citations (Wilson's two main works plus a journal review of Wilson) embedded in three paragraphs of structural analysis. Floor met (3 sources for a load-bearing claim); ceiling not exceeded (3 ≤ 5); link-and-quote discipline satisfied for the Wilson 2016 citation; the Oetzel review citation is W4 rather than W1 and is not labeled as such (a §2 weighting failure the protocol would have caught). Self-verification was implicit rather than stated. Estimated agent time: ~15 minutes per case, embedded in the riff-writing session. Output: defensible T3 inline citations; not a reusable evidence base; would need promotion to T2 or T1 before Path γ doctrine work treats §2.3.3 as load-bearing. |

The protocol's view: the actual T3 work was the right tier choice for v2 of the riff under the "Make it happen, Addi!" timebox. **A future promotion to T2 for the HRE case specifically would be triggered when the [Exchange #24 Round 3 reviewer](../exchanges/coordination-architecture-reframe-exchange.md#25bis-revised-recommendation-v21-may-27--option-e-hybrid) (under Option E Lane 1 or Lane 2) flags the reference-class engagement as needing more sourcing, or when Path γ doctrine begins drafting.** That is the *deliberate* promotion path the protocol is designed to make legible.

---

## Open questions for the protocol itself

1. **Do T1 sweeps need formal Round-style structure inside `sources/`, or is the existing digest + `SOURCE_INDEX.md` form sufficient?** Current view: existing form is sufficient; the structure lives in `SOURCE_INDEX.md`'s sub-debate organization rather than in a Round protocol inside the sweep.
2. **Should the verification sub-agent be a different model than the authoring agent by default?** Current view: yes when feasible, per the [Comparative Alignment Protocol](comparative-alignment-protocol.md)'s logic — different models catch different failures. When only one model is available, the sub-agent should at minimum operate in a fresh session with §4.1 as the entire context.
3. **How are W6 practitioner accounts integrated when the practitioner is on the project's pseudonymity discipline?** Current view: cite per the [`feedback/` conventions](../../feedback/README.md), with the consent state visible in the citation.
4. **Does this protocol apply to the `external-formation-docs/` repository?** Current view: external-formation-docs is itself a research output; this protocol applies to *the project's use of external-formation-docs as a source*, not to the external-formation-docs repository's own internal organization.
5. **Does T3 self-verification need a structured artifact, or is the one-line statement sufficient?** Current view: one-line statement is sufficient at T3; if structured artifact is needed, the work is probably T2.

---

## Changelog

- **2026-05-27 (PM, v1.1)** — Added §2.3 *historically-contested-but-converged* subclause after first §4.1 application on [Constitutional Ecology riff §2.3.3 HRE](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#23.3-bis-verification-record-research-protocol-t3-self-verification-may-27-2026-pm) surfaced that the original §2.3 standing rule would have demanded a false-balance counterweight against a now-historical position. The subclause is the protocol's first revision from real application; it is also the first instance of the protocol's design assumption (that protocols revise in response to use) actually playing out.
- **2026-05-27** — Initial draft. Originated from a steward observation during the Constitutional Ecology riff v2 / Path β execution that [§2.3.3 HRE](../explorations/constitutional-ecology-and-coordination-architecture-riff.md#233-the-holy-roman-empire-9621806) would have benefited from structured research. The protocol is provisional until first applied to a research pass; first application is most likely on either (a) a T1 or T2 sweep for the Constitutional Ecology reference class if Round 3 surfaces the need, or (b) a future Exchange #21 follow-up (F3, F4) that requires fresh sourcing. Steward review pending.
