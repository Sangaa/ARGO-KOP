# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 277

Status: PREWRITE / EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-277
Opening repair head: `652a96b1b4dd123ae38c9f4c43a8dc71e9899eca`
Execution role: HERMUZ

## Trigger evidence

Repair276 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-241 and moving the displaced root allocation to vacancy-proven EJR-416.

Exact repair-head evidence:
- Full-Stack #2420 / run `33384236604`: SUCCESS;
- Internal Document-ID Audit #66 / run `33384236577`: all preceding audit/report stages succeeded and MEMORY_TO_ROOT census alone failed as expected;
- census artifact `9754948252`, digest `sha256:2f3512db9400fd8c6fb786572bd89843488c82a04001983010aeff0bf4f0eade`;
- artifact proves history_complete=true, expected_group_count=21, observed_group_count=20, classification_complete=false, decision=PARTIAL, sole incomplete_group_ids=["__COHORT_COUNT_DRIFT__"].

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 21` → `EXPECTED_GROUP_COUNT = 20`.

## Exclusions and verification

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation. Exact compare must show only the one constant replacement plus governed Lease277 evidence. Internal Document-ID and Full-Stack must succeed; final census must be expected=20, observed=20, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[]. Only then may Repair276 and Lease277 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
