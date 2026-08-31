# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-283

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair282.
Opening repair head: `b584ef39aa9f277d1b552dd4fa631185e5229fc0`
Pre-write Matrix283: `c996dbdc9e4b06795bd8adc7e20644b5a596f91f`
Normalization head: `e8c750f8bbad99000a023fcb0c5e39426a94c4d2`

## Trigger

Repair282 reduced observed MEMORY_TO_ROOT membership from 19 to 18. Artifact `9756436545`, digest `sha256:89557bff36970c102e875f2ed560817adb355e69f07028e8112156c48458ec0`, proved history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Execution and verification

Changed only `EXPECTED_GROUP_COUNT = 19` to `EXPECTED_GROUP_COUNT = 18` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Full-Stack Repository Audit #2455 / run `33388442711`: SUCCESS.
Internal Document-ID Audit #73 / run `33388442676`: SUCCESS.
Final census artifact `9756500240`, digest `sha256:5ebae556714ba7691ae58f0e1732a44a4b25db7878c47170183d21330911b6fa` proves expected_group_count=18, observed_group_count=18, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
