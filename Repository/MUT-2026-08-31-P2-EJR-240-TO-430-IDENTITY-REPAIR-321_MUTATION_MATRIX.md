# MUT-2026-08-31-P2-EJR-240-TO-430-IDENTITY-REPAIR-321 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-240-TO-430-IDENTITY-REPAIR-321
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 321-01 | `EJR/EJR-430_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md` | CREATE | displaced root content with first H1 identity EJR-430; semantic body preserved | N | N |
| 321-02 | `EJR/EJR-240_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md` | DELETE | old root identity absent in same atomic tree | N | N |
| 321-03 | `EJR/EJR-416_2026-08-17_MATRIX_VARIANT_REPEAT_VALIDATION.md` | UPDATE | rewrite both live semantic-provenance mentions whose referent is the displaced root semantic-validation record from EJR-240 to EJR-430; preserve unrelated text | N | N |
| 321-04 | `Memory/Engineering_Journal/EJR-240_2026-08-15_P58_SESSION_CLOSURE.md` | KEEP | retained earlier allocation byte-for-byte | N | N |
| 321-05 | census expected baseline | KEEP | remain 7 during repair; drift failure must be preserved for separate rebaseline | Y | Y |

## KEEP REQUIREMENT
Preserve semantic content/date/chronology of the displaced root record; only first-H1 identity/path changes. Preserve the Memory EJR-240 blob. Do not rewrite historical P2 census/baseline records merely because they contain EJR-240. In EJR-416 change only the two semantic-provenance references that identify the displaced root semantic-validation record. Do not change the expected cohort baseline under this repair. Do not touch 317/318.

## Execution Evidence
Lease319 disposition retains Memory EJR-240 and classifies root EJR-240 displaced. Lease320 run `33422684323` proves EJR-430 VACANT with complete history. Current census reports zero exact-member-path consumers. EJR-416 contains two live semantic references to the root semantic-validation evidence (`EJR-240 established...` and `...passed...in EJR-240`); both referents move with the displaced root identity and must be rewritten atomically.

## Closure
After one atomic functional tree require: old root path absent; successor present; Memory blob unchanged; EJR-416 semantic provenance self-consistent; Full-Stack success; Internal-ID failure, if any, must be inspected and preserved rather than hidden. Expected cohort drift 7→6 must be handled only by a separate rebaseline lease after deterministic artifact evidence.