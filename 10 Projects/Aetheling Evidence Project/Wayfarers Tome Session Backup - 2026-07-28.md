---
type: session-backup
status: active
privacy: internal
project: Aetheling Evidence Project
created: 2026-07-28
source: Codex session
related-app: "[[Wayfarers Tome Companion App]]"
related-inventory: "[[Wayfarers Tome Fact and Source Inventory]]"
---

# Wayfarer's Tome Session Backup - 2026-07-28

This note backs up the working decisions, product direction, research boundaries, deployment details, and evidence inventory created during the Codex session that produced the public Wayfarer's Tome companion app.

This is a curated session capture, not a verbatim transcript. The canonical app source remains in `tome-companion/`, and the fact/source ledger has been imported into [[Wayfarers Tome Fact and Source Inventory]].

## Live artifact

- Public app: [The Wayfarer's Tome](https://wayfarers-tome.hamrix.chatgpt.site)
- Local app folder: `tome-companion/`
- Sites project id: `appgprj_6a6892b3f8b48191b211678f3d01838f`
- Current app commit recorded during backup: `801649a366fda81866100a004d9353f8ba2d8fd7`
- Latest recorded commit message: `Refine source index and deep links`
- Test command used during development: `npm.cmd test`
- App framework: Next/Vinext React app with local static assets

## User direction captured from the session

- Build a companion app as an interactive "tome of knowledge" in a retro pixel-game style.
- Make it easy to run and appropriate for a physical 3D-printed object with an embedded NFC tag.
- The intended object is a keychain, trinket, or artifact that can be given to people; they tap it and access the tome.
- Move beyond a static splash image into a working prototype.
- Match the pixel style of `public/og.png`.
- Make the app public.
- Make the whole app's UI match the splash/start screen level of pixel aesthetic.
- Scale back gamification: keep the experience fun and interactive, but make it about learning facts from the Aetheling history rather than completing quests.
- Improve small text readability, including brighter/highlighted text treatment.
- Make borders and UI panels more pixelated for realism.
- Replace plain red square text boxes with more ancient, refined, tome-like panels.
- Add character and personality to the tome.
- Add pixelated historical-style profile portraits, while labeling them as interpretive rather than evidentiary portraits.
- Add more portraits so records do not repeat icons too often.
- Add more icons, favicon symbols, graphics, and polish.
- Add an old-video-game-style map similar in spirit to classic Zelda overworld maps.
- Improve the artifact cabinet because clicked icons were difficult to see.
- Audit facts and add as much factual detail as possible.
- Add source links and fact links.
- Back up and import the session into Obsidian.

## Product outcome

The public app became a sourced, interactive evidence tome rather than a quest game. The tone is "archive companion" rather than "game to complete." It uses pixel-art atmosphere, a start screen, portraits, icons, a map, and interaction loops to invite learning while preserving proof boundaries.

Current app state:

- 46 fact records.
- 71 unique source labels.
- 54 public outbound source links.
- 17 vault/internal source labels.
- Deep links for individual records using `#record-###`.
- Source pack copying for individual facts.
- Public source list copying.
- Bookmark/read state stored locally on device.
- Readability toggle (`INK+`) for small text.
- Public/private evidence boundary labels.

## Major features implemented during the session

- Cover/start screen using the pixel-art splash image aesthetic.
- Entry flow from splash screen into the archive.
- Knowledge ledger with counts for facts, royal thread, open leads, and read records.
- Plain-language "How to Read the Tome" guide.
- Refined artifact cabinet with clearer selected-drawer behavior.
- Featured fact card and "show another fact" interaction.
- Chronicle grid for all records.
- Era Map tab with an original pixel overworld map.
- Lineage tab for documented historical relationships.
- Proof tab for evidence boundaries, caution rules, and research queue.
- Source Desk tab with source search, public/vault/all filters, source counts, and source actions.
- Saved/bookmarks tab backed by local storage.
- Modal record view with:
  - interpretive profile portrait,
  - record id,
  - confidence/status ribbon,
  - source-depth meter,
  - Keeper's Note,
  - supported fact,
  - context/limit,
  - Fact Audit Dossier,
  - linked sources,
  - share/copy/bookmark actions.
- Fact permalinks and copy-link support.
- Hash-change listener so opening `#record-###` opens the matching record.
- More robust icon and favicon set.
- Pixelated panel borders and more ancient/tome-like UI framing.

## Evidence policy preserved

The public app separates documented historical facts from unproved modern descent. It intentionally avoids presenting the medieval royal and Stafford material as a proven modern family line.

Important limits preserved:

- `Ætheling` is historical terminology, not proof of a modern surname or bloodline.
- Surname-origin sources for Selby, Stafford, and Haskins provide context, not individual pedigree proof.
- The Edward III to Stafford bridge is a documented medieval relationship only.
- Major Selby Sr. remains an active research target with unproven parents.
- Selby Y-DNA is useful for paternal-line comparison but does not replace documentary parent-child proof.
- Thomas Selby Sr. is strong Eastern Shore context but not yet a proven ancestor of Major Selby Sr.
- Etheldred Peters research includes corrections and open leads, not a proved royal-origin narrative.
- Private or living-person FTDNA details are not exposed in the public app.

## Fact expansion added late in the session

The app was expanded beyond the original historical baseline with research/audit records for:

- Selby-Atkinson network.
- Choice tract audit.
- Major Selby 1797 chancery lead.
- Major Selby service-citation caution.
- Thomas Selby Sr. timeline.
- Thomas Selby Sr. will.
- Thomas Selby Sr. verification queue.
- Etheldred Peters tax-list correction.
- Etheldred Peters estate-file target.
- William Peters hypothesis.
- Lancashire-origin caution.
- Mary Peters Bible lead.

See [[Wayfarers Tome Fact and Source Inventory]] for the imported 46-record ledger.

## Visual asset inventory

The app now includes:

- Pixel-style cover/splash art from `public/og.png`.
- Original old-game-style evidence map: `tome-companion/public/maps/evidence-overworld-map.png`.
- Portrait assets in `tome-companion/public/portraits/`.
- Icon assets in `tome-companion/public/icons/`.
- Proof compass graphic in `tome-companion/public/graphics/proof-compass.svg`.
- Favicon/app icons in `tome-companion/public/`.

Portraits are decorative and interpretive. They should not be treated as evidence for the historical appearance of any named person.

## Useful app/source files

- `tome-companion/app/page.tsx` - main app UI and record data.
- `tome-companion/app/globals.css` - pixel/tome visual system.
- `tome-companion/app/layout.tsx` - metadata and public app description.
- `tome-companion/public/og.png` - splash/start-screen reference image.
- `tome-companion/public/maps/evidence-overworld-map.png` - map graphic.
- `tome-companion/tests/rendered-html.test.mjs` - build/render checks.
- `tome-companion/.openai/hosting.json` - Sites project configuration.

## Deployment notes

The app is public at [https://wayfarers-tome.hamrix.chatgpt.site](https://wayfarers-tome.hamrix.chatgpt.site). NFC tags for a 3D-printed trinket can point either to the app root or directly to a specific record permalink such as `https://wayfarers-tome.hamrix.chatgpt.site/#record-013`.

Recommended NFC default:

- Root URL for general artifacts: `https://wayfarers-tome.hamrix.chatgpt.site`
- Specific-topic artifacts: use a record permalink from the app's "COPY FACT LINK" action.

## Open next actions

- [ ] Create or attach a separate NFC production note covering tag type, print cavity size, and write/protect workflow.
- [ ] Continue converting app fact records into atomic vault claim notes where appropriate.
- [ ] Retrieve the 1797 Worcester chancery packet for Major Selby Sr.
- [ ] Reconstruct the Choice tract chain of title from patents, deeds, surveys, tax lists, estate files, and releases.
- [ ] Obtain original/certified Thomas Selby Sr. record images before extending any generational chain.
- [ ] Retrieve Etheldred Peters's 1788 Craven County estate file and 1787-1801 court-minute targets.
- [ ] Keep public app copy aligned with vault evidence boundaries after every research update.

