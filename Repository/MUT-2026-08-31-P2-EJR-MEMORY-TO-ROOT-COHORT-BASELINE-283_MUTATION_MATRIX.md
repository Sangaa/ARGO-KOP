# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 283

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-283
Opening repair head: `b584ef39aa9f277d1b552dd4fa631185e5229fc0`
Execution role: HERMUZ

## Trigger evidence

Repair282 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-238 and moving the displaced root allocation to vacancy-proven EJR-418. Repair-head artifact `9756436545`, digest `sha256:89557bff36970c102e875f2ed560817adb355e69f07028e8112156c48458ec0`, proved expected=19, observed=18 and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Executed mutation

Changed exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 19` → `EXPECTED_GROUP_COUNT = 18`.

## Final verification

Full-Stack #2455 / run `33388442711`: SUCCESS.
Internal Document-ID Audit #73 / run `33388442676`: SUCCESS.
Final census artifact `9756500240`, digest `sha256:5ebae556714ba7691ae58f0e1732a44a4b25db7878c47170183d21330911b6fa`: expected=18, observed=18, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
