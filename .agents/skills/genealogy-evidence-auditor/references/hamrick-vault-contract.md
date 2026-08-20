# Hamrick Vault Contract

This reference is derived from the live Hamrick Knowledge Vault structure.

The **live vault remains authoritative**. Re-read its system/project instructions when working in the repository.

## Canonical structure

```text
Hamrick-Knowledge-Vault/
├── 00 System/
│   ├── ChatGPT Work Instructions.md
│   ├── Memory Policy.md
│   ├── Tag Dictionary.md
│   └── Vault Operating Manual.md
├── 10 Projects/
│   └── Aetheling Evidence Project/
│       ├── Project Index.md
│       ├── Vault-First Research Rules.md
│       ├── Modern Selby Stafford Evidence State.md
│       ├── Colonial Selby Source Facts 1701-1790.md
│       ├── Source Material Inventory.md
│       └── ...
├── 20 Knowledge/
│   ├── Claims/
│   ├── People/
│   └── Sources/
├── 30 Tasks/
├── 40 Decisions/
├── 50 Reviews/
├── 60 Templates/
└── 90 Inbox/
```

## Authority order

The live vault defines this order:

1. primary source documents and exact quotations
2. structured evidence notes
3. decision records and approved project-state notes
4. current conversation
5. ChatGPT memory
6. unverified recollection

For Aetheling work, the project policy further distinguishes reviewed originals/primary images as ultimate evidentiary authority.

## Knowledge-note rules

- Markdown + YAML frontmatter.
- Dates: `YYYY-MM-DD`.
- Obsidian wikilinks connect people, projects, claims, and sources.
- One major claim per claim/evidence note.
- Preserve uncertainty.
- State why confidence is assigned.

## Native confidence

- `confirmed`
- `strong`
- `moderate`
- `weak`
- `speculative`
- `contradicted`

These labels attach to the precise claim represented by a note.

## Native workflow status

Separate from confidence:

- `inbox`
- `active`
- `waiting`
- `blocked`
- `complete`
- `archived`

## Native privacy

- `public`
- `internal`
- `confidential`
- `restricted`

Never send `restricted` material to an AI service without explicit review.

## Capture rule

Unclassified material enters `90 Inbox`.

If destination is unambiguous and evidence has been evaluated, create/update the correct Claims/People/Sources note directly.

## Material project-state change

When materially changing Aetheling project state:
- update affected durable note(s);
- update `last-reviewed`;
- update the Project Index/change log;
- update a linked state note if the current evidence map changed.

## No generic status migration

Do not rewrite existing vault confidence labels to another taxonomy simply because the skill uses a different internal analytical vocabulary.
