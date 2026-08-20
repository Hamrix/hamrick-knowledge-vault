---
name: genealogy-evidence-auditor
description: Audit genealogy and historical-lineage claims inside the Hamrick Knowledge Vault using its native Claims/People/Sources structure, Aetheling project rules, confidence labels, Obsidian wikilinks, and vault-first evidence hierarchy. Use for parentage, identity, marriage, surname/title, medieval or royal descent, conflicting pedigrees, source audits, research planning, or evidence-supported vault updates. Never use GEDCOM, unsourced trees, copied pedigrees, AI reports, or quarantined sites as proof; preserve exact source forms, uncertainty, contradictions, and every unsupported bridge.
---

# Genealogy Evidence Auditor — Hamrick Vault Native

Operate natively inside the **Hamrick Knowledge Vault**.

Do not impose a parallel genealogy database or a generic confidence vocabulary when the vault already defines the structure.

The core rule is:

> Every lineage is a chain of atomic claims. A complete descent is only as strong as its weakest required edge.

## 1. Required startup order

For every Aetheling/family-history task:

1. Locate the active Hamrick Knowledge Vault.
2. Read repository/workspace instructions that apply.
3. Read:
   - `00 System/ChatGPT Work Instructions.md`
   - `00 System/Vault Operating Manual.md`
   - `00 System/Tag Dictionary.md`
   - `10 Projects/Aetheling Evidence Project/Project Index.md`
   - `10 Projects/Aetheling Evidence Project/Vault-First Research Rules.md`
4. Read the current project-state note relevant to the branch under study.
5. Read linked claim notes and source notes before starting new web research.
6. Read `references/hamrick-vault-contract.md`.
7. Read `references/evidence-policy.md`.
8. For medieval/noble/royal work, read `references/medieval-lineage-protocol.md`.
9. Before any mutation, read `references/native-write-protocol.md`.

The live vault files outrank copies bundled with this skill. If the vault changes its conventions, adapt to the live vault.

## 2. Canonical vault locations

Use the actual vault structure:

- Project state: `10 Projects/Aetheling Evidence Project/`
- Atomic claims: `20 Knowledge/Claims/`
- People: `20 Knowledge/People/`
- Sources: `20 Knowledge/Sources/`
- Ambiguous/unclassified capture: `90 Inbox/`
- System policy: `00 System/`
- General templates: `60 Templates/`

Do not create a new genealogy subtree unless the user explicitly requests a schema migration.

## 3. Native confidence vocabulary

For durable claim/person notes, use only the vault confidence labels:

- `confirmed`
- `strong`
- `moderate`
- `weak`
- `speculative`
- `contradicted`

Do not write v3-style statuses such as `verified`, `probable`, `plausible`, or `lead_only` into vault `confidence:` fields.

### Meaning is claim-specific

`confirmed` means the **precise claim written in that note** is confirmed.

It does not mean:
- the person's entire biography is confirmed;
- the identity of every same-name person is confirmed;
- a larger descent depending on the claim is confirmed.

Example pattern:
A note may correctly have `confidence: confirmed` because two sources definitely conflict, while the identity question causing the conflict remains unresolved.

Read `references/native-confidence-rubric.md`.

## 4. Evidence firewall

### 4.1 Source origin beats storage location

A statement copied into the vault retains the quality of its true origin.

- unsourced tree copied into a Markdown file = still unsourced
- AI report copied into project notes = still AI-derived lead
- web transcription copied into a source note = still derivative until original inspected
- exact transcription from reviewed primary image = primary-based evidence if provenance is retained

Never promote trust merely because content is now inside the vault.

### 4.2 GEDCOM boundary

The current GEDCOM is excluded from evidentiary analysis unless the user explicitly requests GEDCOM analysis.

Do not use GEDCOM to:
- support;
- reject;
- reconcile;
- extend;
- merge;
- split;
- raise confidence;
- lower confidence

for a genealogy claim.

A technical GEDCOM task must remain separate from evidence adjudication unless the user explicitly changes the project rule.

### 4.3 Quarantined / weak-source rule

Unsourced public trees, WikiTree/Geni/Geneanet profile relationships, copied pedigrees, search snippets, forum posts, AI narratives, surname matching, heraldry marketing pages, and project-quarantined websites are discovery aids only until traced to evidence.

`lestrangeheritage.com` is specifically quarantined by project policy:
- it may generate leads;
- it may not alter a confirmed or strong vault claim without independent evidence;
- copies of it do not count as independent corroboration.

## 5. Atomic-claim protocol

One major claim per durable claim note.

A claim note should answer one proposition, for example:

- A was the child of B.
- A record reports A was the child of B.
- A and B were enumerated in the same household.
- Two reviewed sources contain incompatible auditor chronologies.
- A and B are treated as one correlated identity.
- Parentage of A remains unproven.

Do not combine multiple generational edges into one claim note.

For long pedigrees maintain `assets/link-ledger.md`.

## 6. Claim language discipline

Distinguish:
- **record fact** — what the source actually says;
- **identity correlation** — whether several records refer to one person;
- **relationship conclusion** — what relationship the evidence supports;
- **larger descent conclusion** — whether a continuous chain exists.

Prefer narrow claims.

Examples:

Good:
`The 1785 Worcester guardianship record identifies the recorded Major Selby as the orphan of John Selby, deceased.`

Bad:
`Major Selby was John Selby's son and therefore ancestor of the later Kentucky Selbys.`

The first can be confirmed from the record. The second improperly leaps across an unproved identity bridge.

## 7. Identity-first rule

Before merging people, test:

- exact name forms
- age/chronology
- residence
- spouse
- children
- occupation
- land
- court role
- tax position
- associates
- witnesses
- executors/heirs
- military unit
- migration sequence
- simultaneous conflicting appearances

Same surname is never sufficient.

### Selby / Shelby hazard

Preserve source-exact spelling.

If an index says `Shelby` and an original record says `Selby`:
- preserve both;
- identify which source uses which form;
- search both when useful;
- do not silently normalize;
- do not merge identities solely because the forms are similar.

## 8. Source-note protocol

Durable source notes belong in `20 Knowledge/Sources/`.

Follow nearby native source notes and `references/native-source-note-contract.md`.

At minimum preserve:

Frontmatter:
- `type: source`
- `source-class`
- `repository`
- `reference`
- `date` when known
- `accessed`
- `privacy`

Body:
- `## Citation` or equivalent precise citation section
- `## Record examined` / reported contents
- `## Reliability and limitations`
- `## Claims supported`
- URL/file reference when relevant

Never invent unavailable citation fields.

If a source has not been visually inspected, say so explicitly.

## 9. Claim-note protocol

Durable claim notes belong in `20 Knowledge/Claims/`.

Follow `references/native-claim-note-contract.md`.

Frontmatter should normally contain:
- `type: claim`
- `status: active`
- `confidence: <native label>`
- `privacy: internal` unless another level is required
- `last-reviewed: YYYY-MM-DD`

Body normally contains:
- `# <atomic claim title>`
- `## Claim`
- `## Evidence supporting`
- `## Evidence against` when material
- `## Conflicts` when material
- `## Analysis` or `## Analysis and limit`
- `## Confidence rationale` when the confidence could be misunderstood
- `## Next research action`

Use Obsidian wikilinks to connect source, people, project, and related claim notes.

## 10. Person-note protocol

Durable person notes belong in `20 Knowledge/People/`.

Follow `references/native-person-note-contract.md`.

Preserve:
- preferred research identity;
- source-exact aliases;
- verified/source-reported facts separately;
- relationships with their evidentiary status;
- claims requiring evidence;
- linked sources;
- related claims.

Do not collapse a reported biography into verified facts.

## 11. Research strategy

Search the vault before the web.

Then select the smallest set of records with the highest expected information gain.

Prioritize records that can:
1. explicitly state parentage/relationship;
2. distinguish same-name candidates;
3. resolve an existing contradiction;
4. expose heirs or associates;
5. replace a derivative transcription with the original image;
6. bridge exactly one currently unsupported generation.

Avoid repetitive browsing once results merely repeat the same derivative assertion.

Use `references/research-strategy.md`.

## 12. Source-dependency / circular-sourcing test

For consequential derivative claims ask:

`What is the earliest traceable evidentiary origin of this statement?`

Trace:
current note/site → transmission source → earlier source → underlying record.

Several copies of one assertion are one evidence lineage.

Never count a copied claim as independent corroboration.

## 13. Negative-search rule

Record high-value failed searches, but distinguish:

- `negative search` — no useful result was found;
- `negative evidence` — absence is probative after survival/coverage/expectation checks.

Do not infer nonexistence from one index search.

## 14. Falsification pass

Before raising confidence:

- look for same-name alternatives;
- test chronology;
- test geography/jurisdiction;
- test source circularity;
- inspect contrary probate/deed/court evidence;
- test whether title/property succession was mistaken for kinship;
- test whether a maternal bridge is merely assumed;
- check whether a medieval relationship first appears centuries later;
- check transcription/index errors;
- check whether a favored claim originated from a weak source.

Record the strongest surviving alternative explanation.

## 15. Long-lineage dependency rule

For each required edge track:

- claim-note path
- child/subject
- claimed parent/relationship
- native confidence
- primary anchor
- identity status
- conflicts
- next target
- downstream lineage conclusions

A full lineage cannot be described as confirmed when a required bridge is only strong/moderate/weak/speculative or contradicted.

Do not average confidence.

If one edge fails:
- retain valid people;
- retain valid sources;
- retain confirmed segments on both sides;
- mark the larger descent blocked/unproven at that edge.

## 16. Medieval / noble / royal rule

For pre-modern lines:
- separate existence, identity, title, land tenure, witness association, kinship, parentage, marriage, inheritance, and biological descent;
- do not treat `de X` automatically as a hereditary modern surname;
- do not infer kinship from charter witness lists;
- do not infer parentage from title succession;
- distinguish documented relationship from scholarly reconstruction and later pedigree tradition;
- stop at the first unsupported bridge.

When necessary state exactly:

`No evidentiary bridge established at this point.`

## 17. Ambiguous capture rule

If useful new material does not have an unambiguous durable destination:

- create a capture in `90 Inbox`;
- follow `60 Templates/Capture.md`;
- preserve origin;
- capture date;
- project;
- privacy;
- raw material;
- key facts;
- interpretations/hypotheses;
- suggested destination;
- follow-up.

Do not prematurely create a person or confirmed claim merely to file a lead.

## 18. Native vault write transaction

Before editing:
1. inspect relevant live notes;
2. inspect Git/worktree state when available;
3. identify unrelated changes;
4. identify exact notes affected;
5. determine whether project state changes;
6. prepare minimum patch.

During editing:
- preserve YAML frontmatter;
- use `YYYY-MM-DD`;
- use Obsidian wikilinks;
- preserve source-exact names;
- use native confidence labels;
- keep one major claim per claim note;
- preserve uncertainty/conflicts;
- do not rewrite unrelated notes.

After editing:
1. re-read changed notes;
2. review diff when available;
3. ensure every factual upgrade is source-backed;
4. update `last-reviewed`;
5. if project state materially changed, update:
   - `10 Projects/Aetheling Evidence Project/Project Index.md`
   - relevant project-state note
   - project change log
6. report exact changed paths.

Do not commit, push, reset, clean, discard unrelated changes, or create a PR unless explicitly authorized.

## 19. Publication boundary

The public Wayfarer's Tome or other presentation layer may be synchronized only after underlying vault claim/source notes are reviewed.

Do not upgrade public lineage language ahead of vault evidence.

## 20. Default response format

For a vault-backed genealogy task return:

1. **Conclusion**
2. **Evidence used** — include vault note/source paths
3. **Uncertainty or conflicts**
4. **Recommended next action**
5. **Proposed/completed vault updates**

For long-lineage audits include the link ledger.

## 21. Completion gate

Before completing a substantive genealogy audit:

- [ ] Vault searched first.
- [ ] Project Index/current-state note read.
- [ ] Exact atomic claim defined.
- [ ] Linked source notes inspected.
- [ ] Source origin distinguished from storage location.
- [ ] GEDCOM excluded unless explicitly requested.
- [ ] Identity tested before relationship merge.
- [ ] Exact historical name forms preserved.
- [ ] Source independence/circularity checked.
- [ ] Contradictions considered.
- [ ] Negative search not overstated.
- [ ] Preferred theory received a falsification pass.
- [ ] Native confidence label matches the precise claim.
- [ ] Long-lineage weakest-edge rule applied.
- [ ] Ambiguous leads quarantined/inboxed.
- [ ] Any write follows native YAML/wikilink conventions.
- [ ] `last-reviewed` updated when appropriate.
- [ ] Project state/change log updated when materially changed.
- [ ] Diff reviewed when a repository write occurred.
- [ ] Final wording does not imply a bridge the evidence does not establish.

If one of these cannot be completed, say so and preserve the lower confidence state.

## 22. v5 integrity preflight

For consequential vault writes, read these references first:

- `references/schema-drift-and-integrity.md`
- `references/project-state-synchronization.md`
- `references/source-origin-firewall.md`

When local filesystem access is available, run these read-only checks before writing:

- `scripts/profile_vault_contract.py`
- `scripts/validate_genealogy_integrity.py`
- `scripts/check_project_sync.py`

These checks do not adjudicate genealogy. They detect schema drift, invalid native-note structure, unresolved dependencies, and project-state synchronization hazards.

If they report unrelated pre-existing issues, preserve those issues and do not broaden the current patch.
