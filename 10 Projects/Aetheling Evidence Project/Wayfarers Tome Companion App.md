---
type: project-artifact
status: active
privacy: internal
project: Aetheling Evidence Project
created: 2026-07-28
last-reviewed: 2026-07-31
source: Codex session
app-url: "https://wayfarers-tome.hamrix.chatgpt.site"
local-folder: "tome-companion/"
---

# Wayfarer's Tome Companion App

The Wayfarer's Tome is a public, NFC-friendly companion app for the [[Aetheling Evidence Project]]. It presents sourced historical and genealogical-research facts in a retro pixel tome style while keeping unproved lineage claims visibly separated from documented evidence.

## Purpose

The app is meant to be tied to a physical 3D-printed artifact, keychain, or trinket with an NFC tag inside. When someone taps the artifact, the phone opens a small interactive tome that teaches the Aetheling/Selby/Stafford/Wessex research story.

The experience should feel like discovering an old pixel-art game object, but the substance should remain archival: facts, limits, sources, and next research moves.

## Current public URL

[https://wayfarers-tome.hamrix.chatgpt.site](https://wayfarers-tome.hamrix.chatgpt.site)

Suggested NFC URL:

`https://wayfarers-tome.hamrix.chatgpt.site`

Record-specific NFC URLs can use the fact permalink format:

`https://wayfarers-tome.hamrix.chatgpt.site/#record-013`

## Design direction

- Retro pixel-game aesthetic.
- Pixelated UI borders and carved/tome-like panel frames.
- Ancient burgundy, gold, parchment, midnight blue, and muted green palette.
- UI should match the cover image's level of pixel-art polish.
- It should feel like an artifact cabinet, evidence archive, and lore book rather than a modern database.
- Gamification should stay light: interactive learning, not quests or mandatory completion loops.
- Small text needs high contrast and readability support.

## Core app sections

- Cover screen - opens with the splash artwork and an "Enter the Tome" action.
- Knowledge ledger - summarizes fact counts, documented thread count, open leads, and device read state.
- Start guide - plain-language explanation of how to read facts and limits.
- Artifact cabinet - tap sigils to open themed drawers and learn what each evidence category means.
- Chronicle - browsable record grid.
- Era Map - old-game-style map and chronological record route.
- Lineage - documented historical thread with each relationship kept separate.
- Proof - caution rules, research queue, and evidence-boundary panels.
- Sources - searchable/filterable source desk for public links and vault notes.
- Saved - local bookmarks for returning readers.

## Data model

Each tome record is stored as an entry in `tome-companion/app/page.tsx` with:

- `id` - numeric record id used for `#record-###` permalinks.
- `kind` - category such as TERM, WESSEX, ROYAL LINE, STAFFORD, ORIGINS, RESEARCH, or METHOD.
- `title` - record title.
- `years` - optional date/range label.
- `subtitle` - compact teaching hook.
- `fact` - the supported claim or corrected observation.
- `context` - explanation of why the fact matters and what it does not prove.
- `sources` - source-label array.
- `status` - CONFIRMED, STRONG, or TENTATIVE.

Supporting structures include:

- `sourceLinks` - public URLs or vault fact pointers.
- `sourceLinkRules` - fallback matching rules for grouped/private source labels.
- `dossiers` - evidence readout, audit judgment, boundary, and next archive move.
- `keeperNotes` - personality layer for record modals.
- `mapRegions`, `eraMap`, `proofLedges`, `cautionRules`, and `evidenceQueue` - navigation and teaching scaffolds.

## Evidence statuses

- CONFIRMED - supported historical relationship, term, or record-level fact within a narrow boundary.
- STRONG - strong contextual evidence, often for surname origins or methodological points, but not necessarily an individual pedigree proof.
- TENTATIVE - research lead, correction, hypothesis, unresolved identity question, or source-acquisition target.

## Public/private source behavior

Public sources open outward where a stable URL exists. Vault/internal source labels are shown as vault facts or vault notes rather than pretending to be public citations.

This was an intentional privacy and accuracy choice:

- Public users can inspect public sources.
- Internal vault context remains available for the project.
- Private/living-person FTDNA details are not exposed.
- A source label without a public URL is still visible, but clearly marked as internal/vault context.

## Important feature behaviors

- Bookmarks are stored in browser `localStorage` as `tome-bookmarks`.
- Recently opened records are stored as `tome-recent`.
- Read records are stored as `tome-read-records`.
- Readability mode is stored as `tome-ink-boost`.
- Selected study path is stored as `tome-study-path`.
- Record links use `#record-###`.
- Opening a `#record-###` URL opens the record modal automatically.
- "COPY SOURCE PACK" copies fact, audit summary, limit, evidence notes, next move, and source URLs/record pointers.
- "COPY PUBLIC LINKS" copies the public source URL index.

## Current source counts

- Fact records: 52.
- Unique source labels: 78.
- Public source links: 60.
- Vault/internal source labels: 18.

The July 31 update adds the John Selby tract cluster, Zadock Selby estate case, Parker Selby estate packets, Etheldred Peters land caveat, the exact Frederick Ethelred Selby identity candidate, and William Atkinson Selby's wartime indictment and Townsend-family marriage story. These remain bounded research records rather than lineage conclusions.

See [[Wayfarers Tome Fact and Source Inventory]] for the imported record/source ledger.

## File map

- `tome-companion/app/page.tsx` - fact records, source links, interactions, app screens.
- `tome-companion/app/globals.css` - pixel-art visual system.
- `tome-companion/app/layout.tsx` - app metadata, social description, title.
- `tome-companion/public/og.png` - cover/start-screen art reference.
- `tome-companion/public/maps/evidence-overworld-map.png` - original pixel evidence map.
- `tome-companion/public/icons/` - category/symbol icon set.
- `tome-companion/public/portraits/` - interpretive pixel portraits.
- `tome-companion/public/graphics/proof-compass.svg` - proof/cabinet graphic.
- `tome-companion/tests/rendered-html.test.mjs` - rendered output smoke tests.
- `tome-companion/.openai/hosting.json` - Sites project id.

## Maintenance checklist

- [ ] Keep the public app aligned with the vault's evidence boundaries.
- [ ] Add or revise records only after the vault source note or claim note is updated.
- [ ] Preserve the distinction between public source links and vault-only notes.
- [ ] Keep portraits labeled as interpretive profile art, not proof images.
- [ ] Run the app tests before deployment.
- [ ] After deploying, spot-check the public URL and at least one record permalink.
