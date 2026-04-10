# Website Submission Triage Checklist

One-page steward template for `website-submission` issue intake.

---

## 1) Intake Snapshot

- Issue URL: `<paste>`
- Opened by: `<name>`
- Date opened: `<yyyy-mm-dd>`
- Submission type label: `<missing-perspective|historical-case|domain-expertise|challenge|other>`
- Primary domain(s): `<housing|ai|...>`

---

## 2) Acknowledge in Issue

Post a short response that includes:

- confirmation of receipt
- submission type restatement
- next review step
- initial review bucket

Suggested response skeleton:

```text
Thank you for this submission. We have logged it as `<type>` under `website-submission`.
Next step: `<steward review in this cycle | include in synthesis | steward discussion>`.
Initial bucket: `<bucket>`.
```

---

## 3) Score (0-2 per dimension)

| Dimension        | 0                              | 1                           | 2                                                | Score |
| ---------------- | ------------------------------ | --------------------------- | ------------------------------------------------ | ----- |
| Relevance        | weak connection to active work | related but indirect        | directly engages memo/framework/roadmap          |       |
| Specificity      | general opinion/slogan         | clear claim, limited detail | concrete claim or proposed correction            |       |
| Evidence         | no references/examples         | some support                | strong references, cases, or falsification logic |       |
| Novelty          | duplicate/already covered      | partial new angle           | meaningfully new perspective or framing          |       |
| Actionability    | unclear next move              | directional only            | clear review or revision candidate               |       |
| Steward priority | can wait                       | next synthesis cycle        | prompt steward attention                         |       |

Total score (0-12): `<sum>`

Routing bands:

- `0-4`: acknowledge and hold (unless elevated by steward judgment)
- `5-8`: include in next synthesis cycle
- `9-12`: steward review soon

---

## 4) Choose Review Bucket

- [ ] Immediate doc correction or addition
- [ ] Hold for synthesis into memo/framework revision
- [ ] Out-of-scope or duplicate (reason required)

---

## 5) Record Disposition State

Select exactly one:

- [ ] `accepted-for-integration`
- [ ] `accepted-for-review-later`
- [ ] `needs-steward-discussion`
- [ ] `duplicate-or-overlapping`
- [ ] `declined-with-reason`

Disposition note (required):

`<one to three sentences>`

---

## 6) Link Absorbing Artifact (When Closing)

At closure, link one or more:

- PR: `<url>`
- roadmap note: `<url/path>`
- memo revision: `<url/path>`
- synthesis note: `<url/path>`
- follow-up issue: `<url>`

If no integration path is selected, record why in the closure comment.

---

## 7) Cadence Check

- [ ] Included in this week's or biweekly `website-submission` synthesis pass
- [ ] Grouped under the correct memo/framework section
- [ ] Included in published synthesis summary ("what changed, what did not, and why")
