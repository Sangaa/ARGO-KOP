# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 283

Status: PREWRITE / EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-283
Opening repair head: `b584ef39aa9f277d1b552dd4fa631185e5229fc0`
Execution role: HERMUZ

## Trigger evidence

Repair282 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-238 and moving the displaced root allocation to vacancy-proven EJR-418.

Exact repair-head evidence:
- exact compare classifies the functional delta as one rename with +1/-1, H1 only;
- Full-Stack #2452 / run `33388263948`: SUCCESS;
- repair-head census artifact `9756436545`, digest `sha256:89557bff36970c102e875f2ed560817adb355e69f07028e8112156c48458ec0`;
- artifact proves history_complete=true, expected_group_count=19, observed_group_count=18, classification_complete=false, decision=PARTIAL, sole incomplete_group_ids=["__COHORT_COUNT_DRIFT__"].

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 19` → `EXPECTED_GROUP_COUNT = 18`.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation. Internal Document-ID and Full-Stack must succeed; final census must be expected=18, observed=18, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[]. Only then may Repair282 and Lease283 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
