# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 289

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-289
Opening repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`
Execution role: HERMUZ
Functional normalization head: `166c81d90eb0b15c9f5b171f50fde6a77c66894a`

## Trigger evidence

Repair288 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-243 and moving the displaced root allocation to vacancy-proven EJR-420.

Repair-head census artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`, proved expected=17, observed=16, history_complete=true, decision=PARTIAL, with sole incomplete group `__COHORT_COUNT_DRIFT__`.

## Executed mutation

Exactly one line changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 17` → `EXPECTED_GROUP_COUNT = 16`.

## Final verification

- Full-Stack run `33394963239`: SUCCESS.
- Internal Document-ID run `33394963190`: SUCCESS.
- final census artifact `9758964913`, digest `sha256:02408c5a8883e810d514d3f39da4913f55902d7b346c69be343594ef7995f099`.
- expected=16, observed=16, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No other mutation was authorized or executed by Matrix289.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
