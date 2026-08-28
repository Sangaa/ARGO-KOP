# P405 — Observed CI Failure Repair: Authorization-ID Test Fixtures

Date: 2026-08-28
Protocol: GOV-013
Status: `SOURCE-REPAIRED / EXECUTION-PENDING / NO CANONICAL MUTATION`

## Re-entry and learning review
Resumed from P404. Prior learning applied: repair only observed failures; exact-head attribution; NO RUN is not PASS; authorization is explicit and must be carried through the candidate contract; no mutation from unproven upstream reachability.

## Evidence
Exact-head `2b4d402f3e6611102c4c31c524f144833baac9f4` produced:
- Full-Stack Repository Audit: success.
- Runtime Prototype and Integration: failure.
- 300 passed, 5 failed, 11 subtests passed.
- All five failures were the same concrete constructor error: `ProductionExecutionCandidate.__init__()` missing required `authorization_id`.

## Root cause
P404 made `authorization_id` mandatory in the production candidate contract, but three pre-existing test fixtures were not updated in the same mutation boundary. This is a test-fixture consistency defect, not evidence of a runtime or authorization-policy failure.

## Repair
Added explicit authorization IDs to the three affected test surfaces. The negative authorization fixture uses an empty ID while retaining `authorized=False`, preserving the adapter's fail-closed authorization test.

## Scope control
No production runtime, service, dispatcher, connected spine, registry, governance authority, or `main` was changed.

## Matrix
`Repository/MUTATION_MATRIX_P405_AUTHORIZATION_ID_TEST_REPAIR_2026-08-28.md` was added before close.

## Learning disposition
No new KD claimed. This is direct application of existing repair-only-observed-failure and explicit-authorization lessons.

## Checkpoint
`P405 -> exact-head CI -> inspect full regression -> if green, reconcile B08 isolated execution; if failure, repair only the observed root cause.`

## Close
`P405 CLOSED / SOURCE-REPAIRED / EXECUTION-PENDING / NO PROMOTION`
