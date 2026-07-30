---
type: session-log
status: active
privacy: internal
created: 2026-07-30
last-reviewed: 2026-07-30
project: "[[10 Projects/Aetheling Evidence Project/Project Index|Aetheling Evidence Project]]"
branch: audit/aetheling-project-initial
pull-request: 1
---

# Record-correlation phase backup — Robert Selby and Ethelred Stafford

## Scope

This backup records the 2026-07-30 phase that moved from general GEDCOM source auditing to exact nineteenth-century record correlation. The phase concentrated on Robert Benjamin Selby's 1870 and 1880 Kentucky households, his reported 1844 Indiana marriage, and Ethelred R. Stafford's 1873 New Orleans death and address trail.

## Robert Benjamin Selby GEDCOM audit

### Person record

- GEDCOM ID: `@I402@`
- Preferred working name: Robert Benjamin Selby
- Alternate GEDCOM names: Benjamin Selby
- Working birth: 31 January 1826, Kentucky
- Working death: 16 July 1902, New Orleans, Orleans Parish, Louisiana
- Parent family assignment: `@F662@`, Benjamin Selby and Elizab. McClane

### Audit finding

The GEDCOM attaches multiple broad collections that do not prove Robert's reported 1902 death or his parents. Kentucky death records, Indiana marriage collections, school catalogs, census collections, Civil War draft registrations, and Ancestry Family Trees must be separated by event and person. The parent assignment to Benjamin Selby and Elizab. McClane remains unsupported by an inspected original record.

Governing source note:

- [[Robert Benjamin Selby GEDCOM source-attachment audit]]
- Creation commit: `0f34fd2b280b9858ab3d525d40ae6974a5fdda67`

## Exact census-image targets

### 1870

- NARA publication: M593
- Roll: 470
- Coverage: Henry and Hickman Counties, Kentucky
- Census place: Port Royal, Henry County
- Page: 374A
- FamilySearch film: 545969

### 1880

- NARA publication: T9
- Roll: 420
- Census place: Eminence, Henry County, Kentucky
- Enumeration district: 092
- Page: 28C

NARA confirms that the surviving 1870 and 1880 schedules are held on M593 and T9 and are digitally accessible through partner genealogy sites. The actual Selby pages remain uninspected.

### GEDCOM-derived expected household

Expected 1870 occupants:

- Robert Benjamin Selby, approximately 44;
- Docia or Dosea Stone Selby, approximately 33 or 34;
- Frederick Payne Selby, approximately 9.

Expected 1880 occupants:

- Robert Benjamin Selby, approximately 54, transcribed relation self;
- Docia Stone Selby, approximately 43 or 44, transcribed relation wife;
- Frederick Payne Selby, approximately 19, transcribed relation son;
- Robert Carr Selby, approximately 5, transcribed relation son.

These ages and household members are search hypotheses derived from the GEDCOM, not direct census transcriptions.

Governing source note:

- [[Robert Benjamin Selby 1870 and 1880 census household correlation]]
- Creation commit: `c2ccc024cf21a457ff8620197df31a2ae90179b2`

## Robert Selby and Lucy S. Hunter marriage target

### Working marriage lead

- Groom: Robert Selby, possibly Robert Benjamin Selby
- Bride: Lucy S. Hunter
- Reported date: 27 February 1844
- County: Clark County, Indiana

The GEDCOM cites three derivative marriage collections but does not include an original book, page, image, return, bond, officiant, witness, or consent.

### Official access route

- Clark County Clerk maintains county marriage records.
- Indiana judicial guidance directs certificate requests to the county clerk.
- Clark County's current request page lists certified marriage copies at $4, subject to confirmation for historical records.
- Indiana State Library lists Clark County marriage records for 1825–1901.
- A FamilySearch catalog entry for the Ruth M. Slevin compilation identifies volume 1 as Books A–F, 1825–1855; this is a finding aid, not the original record.

### Unsent Gmail request

- Recipient: `rlynch@clarkcounty.in.gov`
- Subject: `Historical marriage-record request — Robert Selby and Lucy S. Hunter, February 27, 1844`
- Gmail draft ID: `r-3372921303538267643`
- Status: unsent; requires user review.

The request asks for the complete underlying historical record, including license application or bond, register entry, return, reverse, officiant, witnesses, bondsman, consent, guardian information, signatures, marks, and exact book/page citation.

Governing source note:

- [[Robert Selby and Lucy S Hunter 1844 Clark County marriage acquisition target]]
- Creation commit: `4c0e770720e766fb73b6a9d4ebf1ff8e0d30d1a1`

## Ethelred R. Stafford phase findings

### GEDCOM identity

- GEDCOM ID: `@I103@`
- Working name: Ethelred R. Stafford
- Variant: Etheldred R. Stafford
- Working birth: 28 August 1795, North Carolina or Tennessee
- Working death: 12 April 1873
- Working death address: 9 Annunciation Street, New Orleans
- Family assignment: son of Stephen Stafford and Betsey or Elizabeth Peters in family `@F317@`

### Missing media

Four Ancestry media identifiers are attached without filenames or images:

- 259254346
- 259254452
- 259254497
- 259254563

These identifiers are not evidence until the actual media files and provenance are recovered.

Governing source note:

- [[Ethelred R Stafford GEDCOM media and address audit]]
- Creation commit: `7a3de67c53ab8b31d09caf9c9997d63fec508711`

### Unsent New Orleans archive request

- Recipient: `archivist@nolalibrary.org`
- Subject: `Research request — Ethelred R. Stafford, died April 12, 1873, 9 Annunciation Street`
- Gmail draft ID: `r-7950326484317278063`
- Status: unsent; requires user review.

The request asks for obituary-index cards, newspaper notices, city directories, succession or probate files, cemetery and undertaker material, death-register entries, address history, and any biographical references.

## Current evidence classification

- Robert's Henry County residence in 1870 and 1880: **supported lead; images uninspected**.
- Docia Stone as Robert's wife: **supported hypothesis**.
- Frederick Payne and Robert Carr as Robert's sons: **supported hypotheses; 1880 relationship fields may document them when inspected**.
- Robert and Lucy Hunter marriage: **supported derivative lead**.
- Robert as son of Benjamin Selby and Elizab. McClane: **unresolved**.
- Robert's 1902 New Orleans death: **unresolved**.
- Ethelred R. Stafford's 1873 death address: **GEDCOM lead; original source absent**.
- Ethelred R. Stafford as son of Stephen Stafford and Elizabeth Peters: **unresolved**.

## Next actions

1. Obtain the 1870 page M593 roll 470, page 374A, including adjacent pages.
2. Obtain the 1880 page T9 roll 420, ED 092, page 28C, including adjacent pages.
3. Review and send the Clark County marriage-record request.
4. Review and send the New Orleans Ethelred Stafford request.
5. Correlate occupations, property values, birthplaces, parental birthplaces, household relationships, neighbors, and addresses.
6. Locate Lucy Hunter after 1844 and determine whether the marriage ended by death, divorce, separation, or identity error.
7. Locate Docia Stone before 1870 and identify the beginning of her relationship with Robert.
8. Do not upgrade any parent-child or marriage claim until original images are inspected.

## Recovery checklist

- [x] Robert GEDCOM source-attachment audit saved.
- [x] Ethelred Stafford missing-media and address audit saved.
- [x] Census household correlation target saved.
- [x] Clark County marriage acquisition target saved.
- [x] Ethelred Stafford New Orleans request drafted.
- [x] Robert–Lucy Hunter Clark County request drafted.
- [x] Record-correlation phase backed up in Obsidian.
- [ ] Original census images acquired.
- [ ] Original Indiana marriage image acquired.
- [ ] Original New Orleans death or succession record acquired.
- [ ] Returned records correlated and atomic claims updated.
