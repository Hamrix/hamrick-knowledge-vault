---
type: claim
status: active
confidence: confirmed
privacy: internal
last-reviewed: 2026-07-29
---

# The uploaded GEDCOM does not match the evidential GEDCOM described in the legacy bundle

## Claim

The uploaded GEDCOM is not the same file described in the legacy Selby Manor evidence index as an 861-individual, checksum-sealed evidential GEDCOM.

## Evidence supporting

- [[Selby extended GEDCOM file audit]] records 3,026 individual records and SHA-256 `4db84ef930b22e5ebc1c1b38dea4787fdb35ac2f01d468e9d359d96e546dd940` for the uploaded file.
- The legacy evidence index states 861 individuals and SHA-256 `7741c5c3fe8023bd10d8378500808d90ceec52796e787fc6b2c12ca7a3d7561b`.

## Evidence against

No matching checksum or record count has been supplied.

## Analysis

This is a file-identity conflict. It does not establish that either GEDCOM is wholly wrong, but it prevents the uploaded file from being represented as the exact sealed evidential version described in the bundle.

The uploaded GEDCOM remains an unverified research input. Its relationships must be converted into atomic claims and checked against the cited records.

## Confidence rationale

`confirmed`: both the checksum and record count differ materially.

## Next research action

Locate the exact file associated with the legacy checksum, or formally supersede that checksum and document the provenance and revision history of the 3,026-person file.
