---
title: State of the Project — What We Claim, What Broke, What We Don't Know
description: A public honesty register for Civic Blueprint — the project's headline claims at explicit confidence, the claims that adversarial review has broken or wounded, what remains unreviewed, and how to challenge the work. A live demonstration of the shared-mirror discipline pointed at the project itself.
provenance: "ai-generated"
---

# State of the Project — What We Claim, What Broke, What We Don't Know

> **Provenance:** `ai-generated` — AI-drafted from the project's own records, **pending steward review**. On steward curation this label becomes `collaborative` per the [Content Provenance Standard](CONTENT_PROVENANCE.md). Until then, read it as a draft, not an endorsed project position.
>
> **Status:** Draft, July 2026. This is a repo-first artifact; a [civicblueprint.org](https://civicblueprint.org) page is the intended second home once the steward has reviewed it and a cross-lineage pass has run (see [Honest limits](#honest-limits-of-this-page-itself)).

---

## Why this page exists

Most projects publish their wins. This one publishes its falsifications too, on purpose.

Civic Blueprint's own analysis argues that a society coordinates badly when it cannot see itself accurately — the "shared mirror" idea developed in the [Shared Mirror riff](../agent/explorations/shared-mirror-collective-self-perception-riff.md) and tested in [Exchange #25](../agent/exchanges/shared-mirror-see-layer-exchange.md). The cheapest place to practice that discipline is on the project itself. This page is the mirror pointed inward: what we actually claim, at what confidence; what our own adversarial review has broken; and what we still do not know. It is the "Ring 1" move the riff describes — make the internal honesty machinery legible before pointing it anywhere else.

It exists for one audience above all: the skeptical domain expert deciding whether this project is worth their time. The fastest way to earn that person's attention is to show them we already know where our weak points are.

---

## What we claim, at explicit confidence

The project's four core documents — [Principles](../PRINCIPLES.md), [Foundational Commitments](../FOUNDATIONAL_COMMITMENTS.md), [Problem Map](../PROBLEM_MAP.md), [Systems Framework](../SYSTEMS_FRAMEWORK.md) — are steward-curated working syntheses, not settled consensus (the [README](../README.md#how-these-documents-were-built) says this plainly). The headline analytical claims, with self-estimated confidence stated as an upper bound to be discounted:

| Claim | Where it lives | Confidence | Basis / main caveat |
| --- | --- | --- | --- |
| Many civic failures are not isolated; they are symptoms of interdependent systems that persist because specific actors benefit from the dysfunction | [Problem Map](../PROBLEM_MAP.md) | ~0.8 | Structural argument, broadly supported by existing scholarship; the specific dependency wiring is a working synthesis, not measured |
| Institutional capacity is a high-leverage upstream constraint across many domains | [Problem Map §4](../PROBLEM_MAP.md#4-institutional-capacity-is-too-weak-for-the-demands-placed-on-it), [Memo 01](../memos/proof-of-usefulness-memo-01.md) | ~0.55 | Directional; the "highest-leverage" version is stronger than the evidence supports |
| Recursive uplift — a visible reform in one domain lowers the difficulty of the next | [Problem Map: recursive uplift](../PROBLEM_MAP.md#what-happens-after-the-opening-recursive-uplift) | ~0.4 | The project's most load-bearing and least-tested claim; housing literature offered no clear support in [Exchange #12](../agent/exchanges/memo-01-housing-parallel-test-exchange.md) |
| Repairing collective self-perception ("the shared mirror") is a real, neglected coordination layer | [Exchange #25](../agent/exchanges/shared-mirror-see-layer-exchange.md) | ~0.65 (weak form) | The strong form was downgraded under adversarial review — see below |
| The project's own multi-agent review process is a partial mitigation for AI convergence, not a fix | [Cross-Lineage Review Harness](../agent/process/cross-lineage-review-harness-protocol.md) | ~0.6 | Self-referential; the mitigation shares the failure mode it mitigates |

These are hypotheses and design directions offered for challenge, not positions the project asks anyone to adopt on trust.

---

## What adversarial review has broken or wounded

The project runs structured adversarial and [cross-lineage review](../agent/process/adversarial-review-protocol.md). It has produced real casualties. These are the ones worth knowing:

- **A whole taxonomy was falsified before it shipped.** The project built a seven-category, then three-axis, ownership taxonomy intended for the Systems Framework. A blind cross-lineage adversarial pass (three independent model families) judged the three-axis version an "immunizing / anti-falsifiability" move and falsified its leverage, durability, and neutrality claims. The project adopted **no** ownership taxonomy; only narrow survivors were kept. See [Exchange #28, Round 5 disposition](../agent/exchanges/ownership-taxonomy-systems-framework-exchange.md#round-5--disposition-harvest--pivot-closed-june-9-2026). This is the machinery working: the design was killed before it reached a core document.
- **A convergence finding was wounded, not confirmed.** The formation-document comparative analysis initially read like cross-tradition convergence on dignity and rights. Expanding the corpus and running a [cross-lineage adversarial pass](../agent/exchanges/formation-document-initial-findings-adversarial-review.md#round-3-results--cross-lineage-adversarial-pass-june-2026) showed the overlap concentrates in the *modern rights-forward subset* — "modern rights-constitutionalism convergence," not a universal one. The headline claim was demoted to "contested."
- **The shared-mirror lead claim was downgraded.** [Exchange #25](../agent/exchanges/shared-mirror-see-layer-exchange.md) set out to test whether "see-together" is *the* upstream coordination layer (M1-strong). The strongest real-world evidence (vTaiwan/Pol.is, Madrid's Decide — where a functioning "see" layer produced almost no downstream action) cut *against* the strong claim. The project retired M1-strong and now leads with M1-weak: the mirror is a real, neglected layer that stalls without parallel "decide" and "act" mechanisms.
- **A second bet failed cross-lineage review twice.** [Exchange #31](../agent/exchanges/abundance-vs-discipline-capital-bottleneck-exchange.md) (whether procedural "veto points" or "discipline capital" is the binding constraint) had its claim set fail a blind cross-lineage pass, was rebuilt, and [failed again](../agent/exchanges/abundance-vs-discipline-capital-bottleneck-exchange.md#round-5--results-june-24-2026) — two consecutive NO-GO verdicts. The question is now parked for external human review rather than resolved in the project's favor.
- **A methodological failure became a documented lesson.** During one cross-lineage audit, a reviewer sub-agent contaminated the exchange it was supposed to review (it wrote into the file). That run was discarded and the contamination recorded as a reusable process lesson rather than quietly dropped. See the [June 2026 coherence audit](../agent/process/audits/coherence-audit-2026-06.md).

---

## What remains unknown or unreviewed

The honest gaps, stated without softening:

- **Almost no external human review has happened.** The project's largest structural weakness is that its adversarial pressure is overwhelmingly self-generated. The external-reviewer lane has been open since April 2026 and remains, as of this writing, essentially unused — it is the named bottleneck under [ROADMAP TODO #11](../ROADMAP.md#new-tracks-introduced-by-exchange-21-round-5), blocking several major threads at once.
- **The corpus is single-lineage.** Most of the analysis was drafted and reviewed by one model family (Claude). Cross-lineage passes (other model families) are a *stronger but still partial* mitigation, because the models share training data and the author lineage still frames the round. External human review remains necessary before anything is promoted.
- **Reality contact is thin.** The project has preserved exactly two [feedback records](../feedback/README.md) from real people who engaged its public surfaces — a [childcare-licensing practitioner](../feedback/feedback-childcare-licensing-practitioner-2026-04.md) and a [grassroots-movement contact](../feedback/feedback-grassroots-movement-contact-2026-06.md). The single most encouraging signal in the whole project (a practitioner returning unprompted with a detailed operational critique) came from the least theoretical artifact. There is not yet enough contact to know how the framework lands with the experts it most needs.
- **The recursive-uplift thesis is under-tested.** It is the structural spine of the Problem Map and the claim with the weakest empirical footing (~0.4 above). Its internal specification is still an open ROADMAP item.
- **Known documentation gaps are catalogued, not closed.** The Problem Map names domains it does not yet cover (criminal justice, immigration, geopolitics, digital identity, social cohesion, anti-corruption institutional design). These are acknowledged invitations, not deferrals.

---

## How to challenge us

The project wants disagreement more than agreement. The most useful challenges:

- **Falsify a claim in the table above** — especially recursive uplift and institutional-capacity-as-upstream. A single well-documented counter-case (a reform that cascaded without institutional-capacity gains, or an institutional-capacity gain that cascaded nowhere) is worth more than broad agreement.
- **Bring a perspective the corpus is missing** — non-US/Western institutional traditions, practitioner knowledge from inside the systems the Problem Map describes, or a domain it admits it has not mapped.
- **Attack the method, not just the claims.** If the cross-lineage review process is a comfortable simulation of disagreement rather than the real thing, that critique goes to the root.
- **Point at drift.** If site copy or a document overstates what the underlying analysis supports, that is exactly the mirror-failure the project claims to be guarding against.

Entry points: open an issue on [the repositories](../README.md#how-to-contribute), or read the [Exchange Index](../agent/exchanges/_EXCHANGE_INDEX.md) to see the argument history before engaging. Honest, specific disagreement is treated as a contribution, not an attack.

---

## Honest limits of this page itself

This page is subject to the discipline it describes. It was drafted by the same model lineage that wrote most of the corpus, so its selection of "what broke" is itself a single-lineage judgment and may flatter the project by choosing failures that are safe to admit. It has not yet had external human review or a cross-lineage pass. Treat it as a starting inventory, not a settled or complete account — and if you find a broken claim or a hidden weakness it omits, that omission is the most useful thing you could point out.

This expresses [Principle 4 (power must remain accountable, legible, and reversible)](../PRINCIPLES.md#4-power-must-remain-accountable-legible-and-reversible) and [Principle 14 (truth and evidence must be protected as public goods)](../PRINCIPLES.md#14-truth-and-evidence-must-be-protected-as-public-goods), applied to the project's own claims.
