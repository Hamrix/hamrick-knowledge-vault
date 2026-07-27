# OpenClaw Vault Integration

Begin with read-only and inbox-only permissions.

## Phase 1 — Safe capture

Allowed:
- read Markdown;
- search Markdown;
- create new notes under `90 Inbox`;
- append to automation logs.

Not allowed:
- edit evidence conclusions;
- delete or move files;
- push directly to the default branch;
- access secrets or restricted records.

## Phase 2 — Reviewed synchronization

After successful testing:
- create a branch;
- process inbox items;
- open a pull request or produce a diff;
- wait for approval before merging.

## Phase 3 — Scheduled maintenance

- daily digest;
- weekly project review;
- stale-note detection;
- broken-link report;
- Git status and backup verification.

See `openclaw-policy.yaml`.
