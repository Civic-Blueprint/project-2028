# /decorrelate

Run the **cross-lineage-decorrelation-check** skill on the claim or recommendation currently on the table in this chat.

Do this now:

1. Restate the live claim as 3–6 falsifiable assertions and show them with the lineage panel (treat my running this command as the steward GO/freeze).
2. Spawn the reviewer panel **blind, in parallel, reduced context** via the Task tool — independent lineages only (`gemini-3.1-pro`, `gpt-5.5-medium`, `grok-4.3`, `kimi-k2.5`), never Claude as a judgment role, adversary blind and rotated off the family that ran adversary last time.
3. Synthesize a per-assertion × per-lineage detection matrix, convergence, open divergence, and a severity-ranked revise-list.
4. Give me a verdict + recommended disposition. Nothing is promoted; I dispose.

If the live claim is ambiguous, ask me to confirm the assertions in one line before spawning. State the honest limit (shared training → mitigation, not cure) in the result.

If $ARGUMENTS is provided, treat it as the specific claim/scope to decorrelate.
