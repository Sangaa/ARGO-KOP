# EJR-304 — GT-043 Runtime Lineage → P6 Identity Bridge

Date: 2026-08-24
Status: CONTROLLED ADAPTER REGRESSION RECORDED / CI EXECUTION PENDING

## Trigger

EJR-307 identified the next safe experiment: an explicit adapter test that accepts P6 evidence only from a VERIFIED runtime lineage result and explicitly sets `observation_state="OBSERVED"`.

## Controlled Boundary

GT-043 implements that experiment in a test-only adapter. It does not create or alter a production promotion path.

The adapter performs this sequence:

`runtime result`
→ `verify_runtime_outcome_evidence`
→ require `VERIFIED`
→ construct P6 `Evidence`
→ reconcile against expected SHA

## Results

A verified runtime lineage result can cross the controlled boundary and produce:

`VALID_CURRENT_EXECUTION`

The execution trace identity remains explicit in the lineage payload, while P6 evidence separately carries its required run/SHA identity and explicit observation state.

An unverified runtime lineage result is rejected before P6 evidence is constructed:

`RUNTIME_LINEAGE_NOT_VERIFIED`

## Important Boundary

This experiment proves compatibility of an explicit adapter contract. It does **not** prove that production runtime evidence should automatically enter P6, and it does not authorize relationship promotion.

This distinction preserves the existing architectural rule:

`verified upstream identity ≠ downstream semantic authority`

## Evidence

Test commit:
`bb5d14c773fb2ab93bcc676fca116facc5cb63b2`

Test file:
`Quality/Integration/test_gt043_runtime_lineage_to_p6_identity_bridge.py`

## Verification Boundary

Repository write succeeded. CI/runtime PASS is not claimed because no workflow execution was exposed for this mutation.

## Learning

A safe ingress bridge must make both boundaries explicit: upstream lineage must first be VERIFIED, and downstream P6 observation provenance must be explicitly declared. The bridge may demonstrate compatibility without becoming a production promotion mechanism.
