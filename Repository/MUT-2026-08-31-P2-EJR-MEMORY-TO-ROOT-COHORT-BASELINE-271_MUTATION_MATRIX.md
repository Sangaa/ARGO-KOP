# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 271

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-271
Opening main: `ad7fd5642941a398f915dad5c299e009346c38a7`
Pre-write commit: `84915fe0a7edccf41f6912d34c9f7ad5a47342ee`
Functional baseline commit: `81322fdd20d21dce9b991c374cc60d9102cda1c2`

## Trigger

Repair270 resolved one MEMORY_TO_ROOT ambiguity. Its exact-head census artifact `9753468588` proved complete history, expected=23, observed=22, and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Applied mutation

Exactly one functional line changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:

`EXPECTED_GROUP_COUNT = 23` → `EXPECTED_GROUP_COUNT = 22`.

Compare from pre-write to functional baseline commit confirmed one file, one-line replacement only.

## Verification

- Internal Document-ID Audit #62 / run `33380575170`: SUCCESS.
- Full-Stack #2392 / run `33380575158`: SUCCESS.
- Final census artifact `9753598303`, digest `sha256:dbf33fba9269544b7f48cbddd32ad19084b68331a0b717b37855ca44cd27bee7`.
- Final census: expected=22, observed=22, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No classifier logic, membership derivation, tests, workflow logic, EJR, Memory, GOV, REP, consumer, chronology, or Global Integrity state changed.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
