# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-271

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair270.
Opening repair head: `ad7fd5642941a398f915dad5c299e009346c38a7`
Pre-write Matrix271: `84915fe0a7edccf41f6912d34c9f7ad5a47342ee`
Functional baseline commit: `81322fdd20d21dce9b991c374cc60d9102cda1c2`

## Trigger evidence

Repair270 resolved one MEMORY_TO_ROOT ambiguity by retaining the earlier Memory EJR-235 allocation and moving the displaced root allocation to vacancy-proven EJR-414.

At the exact Repair270 head, Full-Stack #2390 / run `33380217985` succeeded. Internal Document-ID Audit #61 / run `33380217984` was clean except for the MEMORY_TO_ROOT census baseline drift. Artifact `9753468588`, digest `sha256:f0897d8869170a12046b836abc5b0ce2c0325402522b41826d455c499e97e6dc`, proved `history_complete=true`, `expected=23`, `observed=22`, `decision=PARTIAL`, with sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Applied normalization

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed, replacing `EXPECTED_GROUP_COUNT = 23` with `EXPECTED_GROUP_COUNT = 22`.

Exact compare from Matrix271 pre-write to functional baseline commit showed exactly one file and one-line replacement. No classifier logic, membership derivation, tests, workflows, EJR, Memory, GOV, REP, consumer, chronology, or Global Integrity state changed.

## Verification

- Internal Document-ID Audit #62 / run `33380575170`: SUCCESS, including MEMORY_TO_ROOT provenance census emission.
- Full-Stack #2392 / run `33380575158`: SUCCESS.
- Final census artifact `9753598303`, digest `sha256:dbf33fba9269544b7f48cbddd32ad19084b68331a0b717b37855ca44cd27bee7`.
- Final census: `expected_group_count=22`, `observed_group_count=22`, `history_complete=true`, `classification_complete=true`, `decision=CENSUSED`, `incomplete_group_ids=[]`.

## Boundary and resume

Baseline 22 is the current deterministic MEMORY_TO_ROOT cohort baseline. Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Repair270 may now be closed as execution-verified. After closure validation, select the next Priority-2 target from the current 22-group census using fresh consumer/risk/chronology evidence; do not infer target order from numeric ID alone.
