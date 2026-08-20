# Native Write Protocol

## Before writing

1. Read the live system instructions.
2. Read Aetheling Project Index and Vault-First Research Rules.
3. Read every durable note to be changed.
4. Read linked source/claim notes relevant to the change.
5. Inspect Git status/worktree state when available.
6. Identify unrelated changes.
7. Determine whether project state materially changes.

## Destination logic

### `20 Knowledge/Claims`
Use for a durable atomic proposition with evidence analysis.

### `20 Knowledge/People`
Use for a durable person identity summary.

### `20 Knowledge/Sources`
Use for a durable source record/citation/reliability note.

### `10 Projects/Aetheling Evidence Project`
Use for project indexes, state ledgers, bounded lineage maps, inventories, and project policy.

### `90 Inbox`
Use when useful material exists but:
- destination is ambiguous;
- provenance requires processing;
- claim has not been decomposed;
- the material is still raw/unclassified.

## Minimum patch

Do not perform broad cleanup while researching one genealogical claim.

## Consequential edit checklist

- preserve current claim in Git history;
- use branch/PR when practical if making consequential repository changes;
- never overwrite uncertainty;
- update `last-reviewed`;
- if material project state changed:
  - update Project Index;
  - update relevant state note;
  - append concise change-log entry.

## Frontmatter integrity

Do not:
- remove required fields accidentally;
- replace native confidence values with foreign vocabulary;
- convert dates away from `YYYY-MM-DD`;
- drop privacy labels.

## Wikilinks

Use `[[Note title]]` and aliased form `[[Target|Display]]` where appropriate.

Do not create links to nonexistent notes merely to make the graph look complete.

## Git

Never:
- `git reset --hard`
- `git clean`
- discard unrelated edits
- force-push
- commit
- push
- create PR

unless explicitly authorized for that action.

## Post-write

1. inspect diff;
2. re-read changed notes;
3. confirm citations/provenance;
4. confirm confidence rationale;
5. confirm no unsupported bridge was created;
6. confirm project-state notes are synchronized if needed;
7. list changed paths in the response.
