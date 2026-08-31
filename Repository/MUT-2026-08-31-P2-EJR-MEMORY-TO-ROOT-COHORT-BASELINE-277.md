# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-277

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair276.
Opening repair head: `652a96b1b4dd123ae38c9f4c43a8dc71e9899eca`
Pre-write Matrix277: `6f98cbd578112cb9c6c46f7e554e4eb7405cbdc1`

## Trigger

Repair276 reduced observed MEMORY_TO_ROOT membership from 21 to 20. Artifact `9754948252`, digest `sha256:2f3512db9400fd8c6fb786572bd89843488c82a04001983010aeff0bf4f0eade`, proves history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Authorized normalization: change only `EXPECTED_GROUP_COUNT = 21` to `EXPECTED_GROUP_COUNT = 20`.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
