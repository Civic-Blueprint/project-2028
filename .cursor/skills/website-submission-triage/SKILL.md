---
name: website-submission-triage
description: Complete the Project 2028 website submission triage workflow. Use when a steward wants to triage a `website-submission` issue, fill out the Website Submission Triage Checklist, post the acknowledgment comment on the GitHub issue, or provide an issue ID plus a six-number score array for Relevance, Specificity, Evidence, Novelty, Actionability, and Steward priority.
---

# Website Submission Triage

Use this skill when the user asks to triage a `website-submission` issue in `project-2028`.

## Required inputs

- issue ID, such as `8` or `#8`
- six-number score array in this exact order:
  - `Relevance`
  - `Specificity`
  - `Evidence`
  - `Novelty`
  - `Actionability`
  - `Steward priority`
- optional `post-as` value:
  - `bot` (default)
  - `steward` (or `me`)

Example:

```text
Issue: #9
Scores: [1, 2, 0, 2, 1, 1]
```

If the array is missing, not length 6, or contains values outside `0-2`, stop and ask the user to correct it.

## Source of truth

Follow `WEBSITE_SUBMISSION_TRIAGE_CHECKLIST.md`.

Treat all `website-submission` issues as **organic feedback** by default.

Do not reclassify an unsolicited website issue as structured practitioner critique.

## Workflow

1. Read the issue details with GitHub CLI.

Use:

```bash
gh issue view <id> --repo Civic-Blueprint/project-2028 --json number,title,body,url,labels,author
```

2. Read `WEBSITE_SUBMISSION_TRIAGE_CHECKLIST.md` if it is not already in context.

3. Map the user-provided array to the rubric dimensions exactly in this order:

```text
[Relevance, Specificity, Evidence, Novelty, Actionability, Steward priority]
```

4. Independently score the same issue yourself using the same six dimensions.

This agent score is a **recommendation**, not a replacement for the steward score.

5. Compare the two score sets:

- report both arrays
- report both totals
- call out any dimension where the difference is `2` points
- call out any total-score difference of `3+`

6. Choose the review bucket:

- `Immediate doc correction or addition`
- `Hold for synthesis into memo/framework revision`
- `Out-of-scope or duplicate`

7. Choose exactly one disposition:

- `accepted-for-integration`
- `accepted-for-review-later`
- `needs-steward-discussion`
- `duplicate-or-overlapping`
- `declined-with-reason`

8. Post the acknowledgment comment on the issue.

Default behavior: post as the bot.

Use this posting rule:

- if `post-as` is `bot` or omitted, run:

```bash
scripts/post-as-bot.sh <id> "<comment_body>"
```

- if `post-as` is `steward` or `me`, run:

```bash
gh issue comment <id> --repo Civic-Blueprint/project-2028 --body "<comment_body>"
```

Use this template:

```text
Thank you for this submission. We have logged it as `<type>` under `website-submission`.

Next step: `<steward review in this cycle | include in synthesis | steward discussion>`.
Initial bucket: `<bucket>`.
Disposition: `<disposition>`.
```

Keep the public comment short. Do not post the full score breakdown unless the user explicitly asks for that to be public.

9. In your response to the user, provide:

- issue title and URL
- steward-provided score array and total
- agent-recommended score array and total
- any significant scoring differences
- selected review bucket
- selected disposition
- the exact acknowledgment text you posted

## Default routing guidance

Use the checklist routing bands:

- `0-4`: acknowledge and hold unless steward judgment elevates it
- `5-8`: include in next synthesis cycle
- `9-12`: steward review soon

Map likely outcomes:

- high-actionability framing changes usually point to `needs-steward-discussion`
- well-supported but not immediately actionable historical material often points to `accepted-for-review-later`
- obvious duplicates point to `duplicate-or-overlapping`

## Output template

Use this structure in your response to the user:

````markdown
## Triage Result

Issue: `#<id> <title>`
URL: <url>

Steward score:

- Array: `[r, s, e, n, a, p]`
- Total: `<n>/12`

Agent recommendation:

- Array: `[r, s, e, n, a, p]`
- Total: `<n>/12`

Differences:

- `<none>` or list the dimensions that differ materially

Decision:

- Review bucket: `<bucket>`
- Disposition: `<disposition>`

Acknowledgment posted:

```text
<exact comment text>
```
````

```

## Notes

- Use `gh` for GitHub operations.
- Bot posting requires `.env` to include `CB_APP_ASSISTANT_APP_ID`, `CB_APP_ASSISTANT_INSTALLATION_ID`, and `CB_APP_ASSISTANT_PRIVATE_KEY_PATH`.
- Bot posting also requires the private key file to exist at the configured `CB_APP_ASSISTANT_PRIVATE_KEY_PATH`.
- Do not edit the checklist file unless the user explicitly asks.
- If the issue is missing the `website-submission` label, mention that clearly in your response, but still continue the triage if the user asked for it.
- For copy-paste steward prompts, see [examples.md](examples.md).
```
