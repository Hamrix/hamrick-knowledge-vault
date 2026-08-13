---
type: project-state
status: active
privacy: internal
project: Aetheling Evidence Project
created: 2026-08-08
last-reviewed: 2026-08-08
release: "0.9"
---
  
# Aetheling Evidence Release 0.9 Integration - 2026-08-08

## Conclusion

The source-first Aetheling audit through release 0.9 is now integrated into the Hamrick Knowledge Vault. The imported canonical snapshot contains 71 atomic claims, 27 accession records, and 21 governed record-request packets. No request, filing, payment, or archive order was submitted.

The new evidence advances the Selby and Atkinson network but does not close either [[William Atkinson Selby to Major Selby remains unproven|William Atkinson Selby → Major Selby]] or [[Major Selby to Benjamin Selby remains unproven|Major Selby → Benjamin Selby]]. No continuous modern-to-medieval descent may be published across those gaps.

## Release snapshot

The exact non-private audit artifacts are preserved in `10 Projects/Aetheling Evidence Project/Release 0.9 Snapshot/`:

- [Canonical evidence ledger](Release%200.9%20Snapshot/evidence-ledger.json)
- [Accession register](Release%200.9%20Snapshot/accession-register.json)
- [Record-request packets](Release%200.9%20Snapshot/record-request-packets.json)
- [Full audit status](Release%200.9%20Snapshot/FULL_AUDIT_STATUS_2026-08-08.md)
- [William Atkinson Selby proof packet](Release%200.9%20Snapshot/WILLIAM_ATKINSON_SELBY_PROOF_PACKET.md)
- [Generation-link status](Release%200.9%20Snapshot/SELBY_GENERATION_LINK_STATUS_2026-08-08.md)
- [Phase 05 report](Release%200.9%20Snapshot/SELBY_PROOF_PHASE_05_REPORT.md)
- [Release manifest](Release%200.9%20Snapshot/RELEASE_0.9_MANIFEST.md)
- [Data model](Release%200.9%20Snapshot/DATA_MODEL.md)
- [Information architecture](Release%200.9%20Snapshot/INFORMATION_ARCHITECTURE.md)

Private identity-cluster files, living-person exports, original record images, and restricted material were not copied into the Git-backed vault.

## Evidence added or reconciled

| Accession | Record | Vault source note | Disposition |
|---|---|---|---|
| ACC-012 | Angelo Atkinson's 1766 proved will | [[FamilySearch - Angelo Atkinson 1766 Worcester County will images]] | Existing claim retained; official-volume hash captured in snapshot |
| ACC-013 | 1929 Headen Bible transcript and Selby notes | [[Headen family Bible transcript and Selby family notes - 1929]] | Marriage sourced but unverified; death date remains tradition |
| ACC-014 | Worcester estate index negative search | [[Maryland State Archives - Worcester estate index 1809 William Atkinson Selby negative search]] | No 1809 estate entry found in the scoped index |
| ACC-015 | 1811 Rhody Selby orphan order | [[FamilySearch - Rhody Selby 1811 Bourbon orphan order]] | Direct William → Rhody proof |
| ACC-016 | 1854 Benjamin Selby–Sophia E. Stone marriage | [[FamilySearch - Benjamin Selby and Sophia E Stone 1854 Shelby County marriage-license images]] | Shelby County record; Benjamin was a Frankfort resident |
| ACC-017 | 1880 Benjamin/Docia/Payne household | [[FamilySearch - Ben Selby 1880 US census image]] | Household and reported parent-birthplace evidence |
| ACC-018 | 1825 Antrobus–Polly file | [[FamilySearch - William Antrobus and Polly Selby 1825 Nicholas marriage file]] | Direct Major → Polly proof; false William attachment corrected |
| ACC-019 | two images indexed for 1820 Nicholas Major Selby | [[FamilySearch - Major Selby 1820 Nicholas census pages 111 and 129]] | Page 111 contains one transcribed Major household; page 129 is a nonmatching or mislinked image |
| ACC-020 | 1811 Bourbon deed to Major Selby | [[FamilySearch - Major Selby 1811 Bourbon deed and index]] | Adult identity proved; kinship unproved |
| ACC-021 | 1840 older Benjamin household | [[FamilySearch - Benjamin Selby 1840 Frankfort census image]] | Younger Benjamin excluded from the household |
| ACC-022 | 1849 Benjamin bar admission | [[FamilySearch - Benjamin Selby 1849 Henry Circuit Court bar admission]] | Occupation and associate anchor; no parentage |
| ACC-023 | 1860 McCracken will and probate | [[FamilySearch - William McCracken 1860 will and probate image]] | Benjamin's professional network; no parentage |
| ACC-024 | Scarborough Parker estate account | [[FamilySearch - Scarborough Parker estate account images]] | William payment proved; Worcester label controls |
| ACC-025 | John Atkinson estate order and appeal bond | [[FamilySearch - John Atkinson 1780 estate order and appeal bond]] | Seven-person legatee group proved; relationships unstated |
| ACC-026 | Joshua Atkinson's 1773 will | [[FamilySearch - Joshua Atkinson 1773 Worcester will images]] | Household and Townsend care proved; second Angelo required |
| ACC-027 | 1874 Roberts Selby birth index | [[FamilySearch - Roberts Selby 1874 Henry County birth index]] | Index only; original image unavailable |
| ACC-002 | Robert C. Selby death certificate | [[FamilySearch - Robert C Selby 1938 Kentucky death certificate image]] | Original reads Docie/Docia; Dora index reading corrected |

## Material corrections

1. [[Robert C Selbys 1938 death certificate reports Benjamin Selby and Dora Stone as parents|The prior Dora Stone manuscript reading]] is contradicted. The original reads Docie/Docia Stone; Dora is the index rendering. The death date is 13 March 1938, not 15 March.
2. The 1854 Benjamin Selby–Sophia E. Stone certificate belongs to the Shelby County series. Benjamin's Frankfort residence was previously mistaken for the record county in the external audit ledger and has been corrected.
3. The 1825 Polly Selby record proves Major Selby was her father. Its online attachment to William Atkinson Selby is not parentage evidence.
4. FamilySearch's Bourbon County discovery label for the Scarborough Parker account conflicts with the original Worcester County heading and parties. The original controls.
5. At least two different men named Angelo Atkinson are required: the older testator deceased by 1766 and Joshua's underage son living in 1773.
6. The two preserved 1820 Nicholas County images do not contain two Major Selby entries. Page 111 contains one household with a male age 26-44, a female age 10-15, and a female age 26-44; page 129 contains no Major Selby entry.

## Current generation-link status

- Angelo Atkinson → John Selby's children William Atkinson and Sarah Selby: `confirmed` from the 1766 will.
- Mary Atkinson → William Atkinson Selby: `moderate`; reported by the Maryland biography but not directly stated in the reviewed will.
- John Selby → William Atkinson Selby: `confirmed` from the 1766 will.
- William Atkinson Selby + Sarah White Townsend: `moderate`; reported in the 1929 Bible transcript, original unavailable.
- William Atkinson Selby → Rhody Selby: `confirmed` from the 1811 orphan order.
- Deceased John Selby → minor Major Selby, about seven in 1785: `confirmed` as a bounded record pair; the father's exact identity and the child's later identity remain open.
- William Atkinson Selby → Major Selby: unproved and in tension with the 1785 guardian record if that minor is the later target.
- Major Selby → Polly Selby: `confirmed` from the 1825 marriage file.
- Major Selby → Benjamin Selby: unproved.
- Benjamin and Docie/Docia Stone → Robert C. Selby: certificate statement `confirmed`; biological accuracy remains informant-supplied.
- Sophia E. Stone = Docie/Docia Stone: `moderate` inference, not an explicit identity statement.

## Uncertainty and conflicts preserved

- [[Early records naming Major Selby cannot yet be merged into one man]]
- [[One Major Selby household appears in the reviewed 1820 Nicholas census images]]
- [[The two 1820 Nicholas County Major Selby entries remain uncorrelated]] (superseded by image review)
- [[William Atkinson Selby to Major Selby remains unproven]]
- [[Major Selby to Benjamin Selby remains unproven]]
- [[The claimed 1809 William Atkinson Selby probate has not been located]]
- [[The underage Angelo Atkinson living in 1773 was not the 1766 testator]]
- [[The 1874 Roberts Selby birth index names Benjamin Selby and Docie Stone]]

## Best immediate proof target

Recover John Atkinson's complete will dated 21 March 1779 and the final disposition of the August 1780 appeal. The two preserved pages place John Selby and William Atkinson Selby together among seven residuary legatees but do not state each relationship.

## Website state

Owner-only research site: [Aetheling Evidence Project](https://aetheling-evidence-project.hamrix.chatgpt.site)

Release 0.9 deployed as Sites version 21 with custom owner-only access and no external visitors. Original images remain offline pending rights review.

## Next actions

1. Retrieve John Atkinson's 1779 will, accounts, legatee receipts, and appeal disposition.
2. Complete the 1779 William Atkinson Selby indictment, recognizance, securities, and final disposition.
3. Reconstruct William's 1808–1812 Bourbon and Worcester death, estate, orphan, tax, and land trail.
4. Trace the single verified 1820 Nicholas County Major household in tax and deed records and correlate it with the 1811 Bourbon deed, the 1785 minor, and the 1825 Polly marriage file.
5. Use Benjamin's 1849 bar cohort and 1860 probate associates to locate obituary, biography, death, probate, and collateral-family evidence.
6. Recover the original 1874 Roberts Selby birth return.
