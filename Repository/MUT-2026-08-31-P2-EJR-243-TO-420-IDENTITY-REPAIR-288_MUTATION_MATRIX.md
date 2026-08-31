# MUTATION MATRIX — EJR-243 → EJR-420 IDENTITY REPAIR 288

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-243-TO-420-IDENTITY-REPAIR-288
Opening main: `e3574912aa3502de7c070d7df084df9b783e8420`
Execution role: HERMUZ
Functional repair head: `05eee1852105156ccd1e3b6528f86073b5ce9141`

## Authority

Lease287 proved EJR-420 VACANT across complete reachable history and reserved it solely for displaced root EJR-243. Earlier Memory EJR-243 remained the retained first valid allocation.

## Executed bounded mutation

- retained Memory EJR-243 byte-for-byte;
- root EJR-243 moved to EJR-420;
- changed only first H1 identity;
- preserved historical body/date/status/evidence;
- zero consumer rewrites.

Exact compare from the Repair288 opening head reported one renamed file with additions=1, deletions=1, changes=2.

## Verification and successor normalization

- repair-head Full-Stack run `33394759702`: SUCCESS.
- repair-head census artifact `9758888056`, digest `sha256:f1d5144382e7da2c08e644bba34a989f5fa09f025c436ea836109fa50b631c7f`: history complete; expected=17, observed=16; sole incompleteness `__COHORT_COUNT_DRIFT__`.
- Lease289 separately changed only `EXPECTED_GROUP_COUNT` 17→16.
- final Full-Stack run `33394963239`: SUCCESS.
- final Internal Document-ID run `33394963190`: SUCCESS.
- final artifact `9758964913`, digest `sha256:02408c5a8883e810d514d3f39da4913f55902d7b346c69be343594ef7995f099`: expected=16, observed=16, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
