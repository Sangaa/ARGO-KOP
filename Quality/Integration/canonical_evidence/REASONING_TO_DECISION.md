# Canonical Evidence — Reasoning → Decision

Status: VERIFIED / CONTROLLED_SYNTHETIC
Side effect: false

## Contract

`Decision/DECISION_PASS_CONTRACT.md`

The contract defines the Reasoning → Rule Evaluation → `PROPOSAL_READY` boundary and explicitly keeps execution `NOT_REQUESTED` at the Decision layer.

## Test

`Decision/test_decision_pass.py`

The existing tests verify that clear reasoning produces a proposal, unresolved questions produce `REVIEW_REQUIRED`, and invalid reasoning fails closed.

## Trace

`Quality/Integration/canonical_evidence/REASONING_TO_DECISION_TRACE.json`

The controlled synthetic trace records `PROPOSAL_READY` with `execution_status=NOT_REQUESTED` and `side_effect=false`.

## Boundary

This evidence certifies Reasoning → Decision only. It does not imply authorization or execution.
