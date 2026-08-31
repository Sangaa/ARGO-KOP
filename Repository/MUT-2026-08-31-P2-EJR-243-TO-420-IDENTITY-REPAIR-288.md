# MUT-2026-08-31-P2-EJR-243-TO-420-IDENTITY-REPAIR-288

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: one-record Priority-2 identity repair: displaced root EJR-243 → EJR-420.
Opening main: `e3574912aa3502de7c070d7df084df9b783e8420`
Pre-write Matrix288: `8fb0a43c361592431ee6d29f455814e11d088193`
Functional repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`

## Authority and execution

Lease287 retained the earlier Memory EJR-243, displaced the later root EJR-243, and proved EJR-420 VACANT across complete reachable history. EJR-420 was reserved solely for this repair.

Memory `EJR-243` remained unchanged. Root `EJR-243_2026-08-17_GENERATIVE_KNOWLEDGE_TEST_CONTRACT.md` was moved to `EJR-420_2026-08-17_GENERATIVE_KNOWLEDGE_TEST_CONTRACT.md` with only its first H1 identity changed.

Exact compare from Repair288 opening head to functional repair head classified exactly one file as renamed, additions=1, deletions=1, changes=2. No consumer rewrites were required.

## Verification

- repair-head Full-Stack run `33394759702`: SUCCESS.
- repair-head census artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`, proved expected=17, observed=16, history_complete=true, and sole incompleteness `__COHORT_COUNT_DRIFT__`.
- separate Lease289 normalized only the deterministic cohort baseline 17→16.
- final Full-Stack run `33394963239`: SUCCESS.
- final Internal Document-ID run `33394963190`: SUCCESS.
- final census artifact `9758964913`, digest `sha256:02408c5a8883e810d514d3f39da4913f55902d7b346c69be343594ef7995f099`, proves expected=16, observed=16, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
