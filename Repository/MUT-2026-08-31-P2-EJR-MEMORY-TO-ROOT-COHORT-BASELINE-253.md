# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-253

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair252.

## Trigger evidence
Repair252 artifact `9748220566` proved a legitimate expected=27 / observed=26 drift with complete history and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Functional successor
Prewrite: `27b42d1a8009ecb6253a077cf93b38152d61db1e`.
Functional successor: `210b805e1c35496679ecd0fa45b9654c196596f4`.

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:
`EXPECTED_GROUP_COUNT = 27` → `EXPECTED_GROUP_COUNT = 26`.
Compare proved one file / one addition / one deletion. No classifier logic, tests, workflow, EJR, Memory, GOV, REP, or history mutation occurred.

## Exact-head execution evidence
At `210b805e1c35496679ecd0fa45b9654c196596f4`:
- Internal-ID `33365938857`: SUCCESS
- Full-Stack `33365938873`: SUCCESS
- Runtime `33365938869`: SUCCESS
- M2 `33365938854`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to the census-only diff; no artificial trigger was introduced.

Final census artifact `9748292997`, digest `sha256:565d4af481c37351895d22e56f1fb24cc102c7bc8356342d0eecc34857d983bd`, proved expected_group_count=26, observed_group_count=26, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], with EJR-215 and EJR-410 absent from target_ids.

Current MEMORY_TO_ROOT baseline is 26. Priority 2 remains OPEN; Phase 1 remains OPEN; Global Integrity remains HOLD.
