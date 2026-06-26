# /decorrelate

Run the **cross-lineage-decorrelation-check** skill on the claim or recommendation currently on the table in this chat.

Do this now:

1. Restate the live claim as 3–6 falsifiable assertions and show them with the lineage panel (treat my running this command as the steward GO/freeze).
2. Spawn the reviewer panel **blind, in parallel, reduced context** via the Task tool — independent lineages only (`gemini-3.1-pro`, `gpt-5.5-medium`, `grok-4.3`, `kimi-k2.5`), never Claude as a judgment role; adversary blind and rotated off the family that ran adversary last time. Enforce the skill's hard rules: **balanced stances** (≥1 evidence-weighing reviewer + ≥1 prosecutorial reviewer), the shared **severity codebook + honesty floor** ("a false kill is a failure") and **"evaluate only this prompt; do not read the workspace"** pasted into every role prompt, and include the **framing reviewer** (checks the assertion *set* for author-side selection bias).
3. Synthesize a per-assertion × per-reviewer matrix with **lineage and stance both labeled**; report **cross-stance × cross-lineage convergence** (a lone BLOCKING from a single role/lineage is weak), open divergence, framing gaps, and a severity-ranked revise-list.
4. Give me a verdict + recommended disposition. Default to a **non-author synthesizer** for anything consequential. Nothing is promoted; I dispose.

If the live claim is ambiguous, ask me to confirm the assertions in one line before spawning. State the honest limit (shared training → mitigation, not cure) in the result.

If $ARGUMENTS is provided, treat it as the specific claim/scope to decorrelate.
