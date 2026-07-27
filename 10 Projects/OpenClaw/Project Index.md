---
type: project
status: active
privacy: internal
last-reviewed: 2026-07-27
---

# OpenClaw

## Objective

Use OpenClaw as the local automation layer between ChatGPT Work, Obsidian, GitHub, and Discord.

## Initial automations

- Capture selected ChatGPT summaries into `90 Inbox`
- Create a daily vault activity digest
- Run a weekly stale-project review
- Commit approved vault changes
- Push commits to the private GitHub repository
- Send failures and conflicts to Discord

## Guardrails

- Never auto-commit secrets.
- Never rewrite verified evidence without preserving provenance.
- Never push restricted material.
- Prefer draft notes and review queues over autonomous publication.
