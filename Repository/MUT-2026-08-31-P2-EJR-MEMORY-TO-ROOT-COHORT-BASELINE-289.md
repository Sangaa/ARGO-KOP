# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-289

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair288.
Opening repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`
Pre-write Matrix289: `0ea0f79ab5c132f698af96e255766488af5d1a6d`
Functional normalization head: `166c81d90eb0b15c9f5b171f50fde6a77c66894a`

## Trigger

Repair288 reduced observed MEMORY_TO_ROOT membership from 17 to 16. Repair-head artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`, proved history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Executed normalization

Changed only `EXPECTED_GROUP_COUNT = 17` to `EXPECTED_GROUP_COUNT = 16` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

## Verification

- Full-Stack Repository Audit #2488 / run `33394963239`: SUCCESS.
- Internal Document-ID Audit #80 / run `33394963190`: SUCCESS.
- final census artifact `9758964913`, digest `sha256:02408c5a8883e810d514d3f39da4913f55902d7b346c69be343594ef7995f099`.
- final census: expected_group_count=16, observed_group_count=16, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/Global Integrity mutation occurred under this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
