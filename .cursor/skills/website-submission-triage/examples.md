# Website Submission Triage Prompt Snippets

Use these prompts to invoke the `website-submission-triage` skill consistently.

## Minimal prompt

```text
Triage website submission issue #9 with steward scores [1, 2, 0, 2, 1, 1].
```

## Prompt with explicit request for acknowledgment

```text
Use the website-submission-triage skill to triage issue #9 with steward scores [1, 2, 0, 2, 1, 1], post the acknowledgment comment on the issue, and give your own recommended score array as a comparison.
```

## Prompt with expected output structure

```text
Use the website-submission-triage skill for issue #10 with steward scores [2, 2, 2, 2, 2, 2]. Post the acknowledgment comment, then report:
- the issue title and URL
- my score array and total
- your recommended score array and total
- any significant scoring differences
- the selected review bucket
- the selected disposition
- the exact acknowledgment text you posted
```

## Prompt with caution about public scoring

```text
Triage website submission issue #8 with steward scores [1, 2, 2, 2, 1, 1]. Post only the short acknowledgment publicly on GitHub. Keep the detailed score comparison in your reply to me.
```

## Score order reminder

Always supply the array in this order:

```text
[Relevance, Specificity, Evidence, Novelty, Actionability, Steward priority]
```
