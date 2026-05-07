# Project 2028 — Agent Instructions

## Do NOT run Prettier (or any markdown table formatter) in this repository

This is a markdown-only repository. Prettier — and any other markdown
table formatter (e.g. VS Code "Markdown Table" extensions, `markdownlint --fix`,
`mdformat`, `prettier-plugin-markdown`) — reformats markdown tables into
fixed-width padded columns. The padded form is harder to read in source, makes
long-text cells span thousands of characters per row, and produces noisy diffs
on every edit.

The repository uses two layers of protection:

1. **`.prettierignore` ignores everything** (`*`). Prettier should never touch
   any file here.
2. **House style is compact tables.** Use single-space padding around `|`
   pipes, and use `---` (three dashes) for every separator-row column,
   regardless of the column header width. Example:

   ```markdown
   | Column A | Column B | Column C |
   | --- | --- | --- |
   | short | a much longer cell | another cell |
   ```

   Do **not** pad cells with spaces to align columns visually. Do **not**
   widen separator dashes to match column content. If a table looks "ugly"
   in raw source because of unequal column widths, that is the correct
   appearance — readers consume the rendered form, and writers consume diffs.

If you find an existing padded table, reformat it to compact form rather than
preserving the padding. Do **not** add `<!-- prettier-ignore -->` markers per
table — `.prettierignore *` already handles that globally.

Agents must not invoke `prettier`, `npx prettier`, `markdownlint --fix`,
`mdformat`, or any format-on-save equivalent against files in this repo.

## Repository purpose

Project 2028 is the analytical backbone of Civic Blueprint. It contains
foundational documents (Principles, Problem Map, Systems Framework), a proposal
catalog, structured agent-steward exchanges, and process protocols. All content
is markdown.

## Key conventions

- Exchanges live in `agent/exchanges/` and must be registered in `_EXCHANGE_INDEX.md`.
- Process protocols live in `agent/process/`.
- Adopted operational frameworks (project doctrine) live in `agent/doctrine/` and must be registered in `_DOCTRINE_INDEX.md`. The directory is currently empty by design — see the index for the criteria a document must meet to be promoted into it.
- Proposals live in `proposals/PROPOSAL_CATALOG.md`.
- The `docs/` directory holds project-level policy documents (e.g. Content Provenance Standard).
- Content provenance labels (`human`, `collaborative`, `ai-generated, steward-curated`, `ai-generated`) are defined in `docs/CONTENT_PROVENANCE.md` and should appear on all public-facing documents.
