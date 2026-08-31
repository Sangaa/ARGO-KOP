# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 280

Status: PREWRITE / EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-280
Opening repair head: `84409b606d24c3a9d6ee5ad04efcff72116c2c57`
Execution role: HERMUZ

## Trigger evidence

Repair279 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-236 and moving the displaced root allocation to vacancy-proven EJR-417.

Exact repair-head evidence:
- exact compare classifies the functional delta as one rename with +1/-1, H1 only;
- Full-Stack #2436 / run `33386572852`: SUCCESS;
- Internal Document-ID Audit #69: all preceding audit/report stages succeeded and MEMORY_TO_ROOT census alone failed as expected;
- census artifact `9755813652`, digest `sha256:f16e386eec759e34757099271ab50f04dfca4d5c0b01bb008b2107b04ff2fad2`;
- artifact proves history_complete=true, expected_group_count=20, observed_group_count=19, classification_complete=false, decision=PARTIAL, sole incomplete_group_ids=["__COHORT_COUNT_DRIFT__"].

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 20` → `EXPECTED_GROUP_COUNT = 19`.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation. Internal Document-ID and Full-Stack must succeed; final census must be expected=19, observed=19, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[]. Only then may Repair279 and Lease280 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
