# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-283

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair282.
Opening repair head: `b584ef39aa9f277d1b552dd4fa631185e5229fc0`
Pre-write Matrix283: `c996dbdc9e4b06795bd8adc7e20644b5a596f91f`

## Trigger

Repair282 reduced observed MEMORY_TO_ROOT membership from 19 to 18. Artifact `9756436545`, digest `sha256:89557bff36970c102e875f2ed560817adb355e69f07028e8112156c48458ec0`, proves history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Authorized normalization: change only `EXPECTED_GROUP_COUNT = 19` to `EXPECTED_GROUP_COUNT = 18`.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
