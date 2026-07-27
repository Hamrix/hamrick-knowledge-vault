# ChatGPT Work Instructions

You are operating against the Hamrick Knowledge Vault.

## Authority order

1. Primary source documents and exact quotations
2. Structured evidence notes in the vault
3. Decision records and approved project-state notes
4. Current conversation context
5. ChatGPT native memory
6. Unverified recollection

Never silently promote a claim from one authority level to a higher one.

## Required workflow

When working on a vault-backed task:

1. Locate the relevant project index and current-state note.
2. Read linked evidence and decision records before proposing changes.
3. Distinguish:
   - verified fact;
   - supported inference;
   - family tradition or user recollection;
   - hypothesis;
   - disproven or superseded claim.
4. Cite the note paths or source records used.
5. Place new information in `90 Inbox` unless its destination is unambiguous.
6. Update `Last reviewed` and the project change log when materially changing project state.
7. Never overwrite uncertainty. Preserve competing interpretations.
8. Never commit passwords, API keys, private tokens, medical records, financial records, or identity documents.

## Writing conventions

- Markdown files use YAML frontmatter.
- Dates use `YYYY-MM-DD`.
- Link people, projects, sources, and claims with Obsidian wikilinks.
- One major claim per evidence note.
- Use confidence labels: `confirmed`, `strong`, `moderate`, `weak`, `speculative`, `contradicted`.
- Use status labels: `inbox`, `active`, `waiting`, `blocked`, `complete`, `archived`.
- State why confidence was assigned.

## Change policy

For consequential edits:
- summarize the proposed change;
- identify affected notes;
- preserve the previous claim in Git history;
- use a branch or pull request when practical.

## Default response format

Return:
1. conclusion;
2. evidence used;
3. uncertainty or conflicts;
4. recommended next action;
5. proposed vault updates.
