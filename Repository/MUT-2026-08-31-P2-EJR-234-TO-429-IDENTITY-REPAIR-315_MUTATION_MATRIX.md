# MUTATION MATRIX — Repair 315 EJR-234 → EJR-429

Transaction ID: MUT-2026-08-31-P2-EJR-234-TO-429-IDENTITY-REPAIR-315
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 315-01 | `EJR/EJR-429_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md` | CREATE | displaced root content with H1 changed to EJR-429 only | N | N |
| 315-02 | `EJR/EJR-234_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md` | DELETE | old root identity absent in same atomic tree | N | N |
| 315-03 | `Memory/Engineering_Journal/EJR-234_2026-08-14_P52_SESSION_CLOSURE.md` | KEEP | byte-for-byte unchanged | N | N |

## KEEP REQUIREMENT
Preserve the Memory EJR-234 blob and all historical narrative inside the displaced root record. Only the root document's first H1 identity is changed. No intermediate Git state may contain both root EJR-234 and root EJR-429.

## Execution Evidence
Lease314 complete-history artifact established EJR-429 = VACANT and Full-Stack on the proof head succeeded. Current root blob before repair: `55aa55f6d1c59368b16e958f9e01a602bbc631c6`. Current Memory blob: `a37eac099f38c2d0dba29e760ecef83d2079eae4`.

## Closure
Close only after atomic move, post-state read-back, Full-Stack validation, Internal Document-ID evidence, and any required separate cohort-baseline normalization.
