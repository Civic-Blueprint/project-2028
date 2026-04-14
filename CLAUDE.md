# Project 2028 — Agent Instructions

## Do NOT run Prettier in this repository

This is a markdown-only repository. Prettier reformats markdown tables into
fixed-width padded columns that are harder to read in source and produce noisy
diffs. A `.prettierignore` file is present to block it, but agents should also
avoid invoking `prettier`, `npx prettier`, or any format-on-save equivalent
against files in this repo.

## Repository purpose

Project 2028 is the analytical backbone of Civic Blueprint. It contains
foundational documents (Principles, Problem Map, Systems Framework), a proposal
catalog, structured agent-steward exchanges, and process protocols. All content
is markdown.

## Key conventions

- Exchanges live in `agent/exchanges/` and must be registered in `_EXCHANGE_INDEX.md`.
- Process protocols live in `agent/process/`.
- Proposals live in `proposals/PROPOSAL_CATALOG.md`.
- The `docs/` directory holds project-level policy documents (e.g. Content Provenance Standard).
- Content provenance labels (`human`, `collaborative`, `ai-generated, steward-curated`, `ai-generated`) are defined in `docs/CONTENT_PROVENANCE.md` and should appear on all public-facing documents.
