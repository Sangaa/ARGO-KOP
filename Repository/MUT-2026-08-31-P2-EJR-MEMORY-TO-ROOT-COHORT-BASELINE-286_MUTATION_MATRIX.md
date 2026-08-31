# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 286

Status: PREWRITE / EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-286
Opening repair head: `6db3cc4f571cfbb4a6405f0f59d4be7a1e2e155b`
Execution role: HERMUZ

## Trigger evidence

Repair285 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-239 and moving the displaced root allocation to vacancy-proven EJR-419.

Exact repair-head evidence:
- exact compare from Repair285 open head classifies the functional delta as one rename with +1/-1, H1 only after corrective restoration;
- Full-Stack #2469 / run `33390722040`: SUCCESS;
- repair-head census artifact `9757343910`, digest `sha256:84f59b30aa4e3ddc90db470cfa042bd4cb5e411c8dd8e71a2dc3a5fa95a91cf8`;
- artifact proves history_complete=true, expected_group_count=18, observed_group_count=17, classification_complete=false, decision=PARTIAL, sole incomplete_group_ids=["__COHORT_COUNT_DRIFT__"].

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 18` → `EXPECTED_GROUP_COUNT = 17`.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation.

Internal Document-ID and Full-Stack must succeed; final census must be expected=17, observed=17, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[]. Only then may Repair285 and Lease286 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
