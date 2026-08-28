# MUTATION MATRIX — P404
Transaction ID: `MUT-2026-08-28-P404`
Protocol: `GOV-013`

## Scope

Observed P403 CI failure: `ProductionExecutionCandidate(**handoff)` rejected the `authorization_id` field emitted by the governed handoff contract.

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P404-001 | `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py` | UPDATE | Preserve explicit `authorization_id` in the execution candidate and reject an absent authorization identity before dispatch. | Y | N |

## KEEP REQUIREMENT

All other content is `KEEP`.
No changes to `main`, connected-spine wiring, canonical authority, provider selection, or production environment.

## Evidence

- Source failure is observed on exact PR merge execution: `TypeError` for unexpected `authorization_id`.
- Fix is limited to the candidate contract required by the existing P403 test.
- Real repository I/O remains supplied only by the test `FakeConnector`.

## Execution Evidence

- Exact-head CI re-run is required before closure.
- Unexpected Changes = 0 outside the listed target and required session documentation.

## Closure

`TRANSACTION = CONTROLLED`
`PROMOTION = NOT AUTHORIZED`
