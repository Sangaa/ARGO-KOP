# P405 — Mutation Matrix — Authorization-ID Test Repair

Date: 2026-08-28
Status: `PREFLIGHT-READY / ISOLATED / NO CANONICAL MUTATION`

## Observed failure
Exact-head integration CI for `2b4d402f3e6611102c4c31c524f144833baac9f4` failed with five `TypeError` cases because `ProductionExecutionCandidate` now requires `authorization_id` and three existing test surfaces still constructed the candidate without it.

## Repair boundary
Only test fixtures were repaired. No runtime, service, dispatcher, connected-spine, registry, governance, or canonical files were changed.

## Files
- `Quality/Integration/test_b08_run010_srv009_dispatch_observation_p394.py`
- `Quality/Integration/test_eng006_srv009_production_adapter.py`
- `Quality/Integration/test_run010_eng006_handoff_contract.py`

## Invariants
1. Authorized candidates carry an explicit authorization identifier.
2. Unauthorized candidates remain fail-closed before connector I/O.
3. Existing B08 identity and read-back assertions remain unchanged.
4. No production side effect is introduced by the repair itself.

## Verification
Required exact-head checks:
- Full-Stack Repository Audit
- Runtime Prototype and Integration Tests
- `Quality/Integration` regression suite

## Promotion
No promotion or merge is justified by source repair alone. Canonical `main` remains unchanged.
