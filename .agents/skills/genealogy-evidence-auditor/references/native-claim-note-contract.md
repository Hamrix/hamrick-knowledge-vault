# Native Claim Note Contract

Location:

`20 Knowledge/Claims/<descriptive atomic claim>.md`

## Frontmatter

Typical:

```yaml
---
type: claim
status: active
confidence: confirmed
privacy: internal
last-reviewed: YYYY-MM-DD
---
```

Use only native confidence labels.

## Title

Prefer a sentence-like atomic proposition.

Examples:

- `1785 Worcester guardianship record identifies Major Selby as orphan of John Selby`
- `1878 Kentucky biography auditor chronology conflicts with official Kentucky Auditor history`
- `Lingan Wilson Selby as father of Hon Benjamin Selby remains unproven`

Titles should be specific enough that an Obsidian wikilink communicates the proposition.

## Body

Use sections as applicable:

```markdown
# <atomic claim>

## Claim

## Subjects

## Evidence supporting

## Evidence against

## Conflicts

## Analysis and limit

## Confidence rationale

## Next research action
```

Do not mechanically add empty sections.

## Required discipline

- one major proposition per note;
- source facts linked to `20 Knowledge/Sources`;
- people linked with wikilinks where stable notes exist;
- explain what the source does **not** establish;
- name the next decisive record;
- preserve exact source name forms where identity is disputed.

## Narrow-confirmation pattern

If a source directly states a narrow relationship but not a larger identity:
- the narrow claim may be confirmed;
- the broader bridge remains separate and lower-confidence/unproven.

Never bundle them.
