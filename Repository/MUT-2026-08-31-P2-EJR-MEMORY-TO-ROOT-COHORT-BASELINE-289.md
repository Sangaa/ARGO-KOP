# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-289

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair288.
Opening repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`
Pre-write Matrix289: `0ea0f79ab5c132f698af96e255766488af5d1a6d`

## Trigger

Repair288 reduced observed MEMORY_TO_ROOT membership from 17 to 16. Artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`, proves history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Authorized normalization: change only `EXPECTED_GROUP_COUNT = 17` to `EXPECTED_GROUP_COUNT = 16`.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
