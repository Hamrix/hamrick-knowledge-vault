---
type: project-snapshot
status: archived
privacy: internal
project: Aetheling Evidence Project
release: "0.9"
imported: 2026-08-08
---

# Canonical research data model

## Core entities

- `source`: immutable filename, hash, media type, origin, date obtained, custody, public-access rule, extraction status.
- `citation`: source ID, page/paragraph/record locator, quoted fragment (private), normalized transcription, access date.
- `claim`: atomic proposition, subject, predicate, object/value, date range, place, status, confidence, privacy class, steward note.
- `claim_evidence`: claim ID, citation ID, role (`supports`, `contradicts`, `context`, `mentions`), independence group, assessment.
- `person`: canonical ID, names, life dates, living status, privacy class, notes.
- `relationship`: person A, relationship type, person B, date range, claim ID.
- `event`: type, date range, place, participants, claim ID.
- `place`: canonical name, alternate names, coordinates, jurisdiction.
- `estate`: place ID, historic names, property identity, title references, tenure/manorial-right claims.
- `title_style`: name/style, jurisdiction, type, grant/creation basis, claimant, status.
- `archive_reference`: repository, collection, reference, description, verification state, access URL/request history.
- `legal_assertion`: proposition, jurisdiction, date tested, authority cited, counsel-review state.
- `contradiction`: competing claim IDs, issue, severity, resolution state, decision note.
- `research_task`: question, priority, owner, next action, target repository, dependencies, status.
- `submission`: contributor, consent, evidence description, file quarantine status, review decision.
- `change_event`: actor, timestamp, entity, before/after, rationale.

## Required rules

1. Every public factual sentence resolves to one or more claim IDs.
2. Every verified claim has at least one citation with a precise locator.
3. Derivative project documents sharing the same underlying assertion belong to one independence group.
4. Confidence is categorical and reasoned; numeric probability scores are prohibited.
5. Living-person and restricted-document fields are denied by default at the publication layer.
6. Status and confidence are separate. A sourced claim may still have low confidence.
7. Legal assertions cannot become verified historical facts merely because a filing was submitted.
---
type: project-snapshot
status: archived
privacy: internal
project: Aetheling Evidence Project
release: "0.9"
imported: 2026-08-08
---
