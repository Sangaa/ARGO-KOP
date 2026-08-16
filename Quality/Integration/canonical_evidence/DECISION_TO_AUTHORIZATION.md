# Canonical Evidence — Decision → Authorization

Status: VERIFIED / CONTROLLED_SYNTHETIC
Side effect: false

## Contract

`Decision/DECISION_PASS_CONTRACT.md`

The Decision Pass converts a traceable reasoning result into `PROPOSAL_READY` and explicitly states that a proposal is not authorization and execution remains not requested at this layer.

## Test

`Quality/Integration/test_decision_to_authorization_boundary.py`

The existing integration test proves both rejection without explicit authorization and transition to `AUTHORIZED` with an explicit authorization record while preserving `execution_status=NOT_STARTED`.

## Trace

`Quality/Integration/canonical_evidence/DECISION_TO_AUTHORIZATION_TRACE.json`

The controlled synthetic trace records the authorized boundary with `execution_status=NOT_STARTED` and `side_effect=false`.

## Boundary

This evidence certifies the Decision → Authorization seam only. It does not certify Authorization → Execution and does not create execution authority.
