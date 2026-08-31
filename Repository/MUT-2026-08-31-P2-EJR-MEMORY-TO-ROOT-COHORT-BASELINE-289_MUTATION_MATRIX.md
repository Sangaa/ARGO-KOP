# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 289

Status: PREWRITE / EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-289
Opening repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`
Execution role: HERMUZ

## Trigger evidence

Repair288 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-243 and moving the displaced root allocation to vacancy-proven EJR-420.

Exact repair evidence:
- exact compare from Repair288 opening head classifies the functional delta as one rename with +1/-1, H1 only;
- Full-Stack run `33394759702`: SUCCESS;
- repair-head census artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`;
- artifact proves history_complete=true, expected_group_count=17, observed_group_count=16, classification_complete=false, decision=PARTIAL, sole incomplete_group_ids=["__COHORT_COUNT_DRIFT__"].

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 17` → `EXPECTED_GROUP_COUNT = 16`.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation.

Internal Document-ID and Full-Stack must succeed; final census must be expected=16, observed=16, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[]. Only then may Repair288 and Lease289 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
