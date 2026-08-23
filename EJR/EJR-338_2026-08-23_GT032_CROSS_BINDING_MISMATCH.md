# EJR-338 — GT-032 Cross-Binding Mismatch

Date: 2026-08-23
Status: ANALYSIS COMPLETED / MUTATION BLOCKED BY CONNECTOR VALIDATION
Protocol: GOV-013 + RUN-012
Parent: EJR-337

## Objective

Test the next inference boundary: a real execution identity or a VERIFIED_OCCURRENCE marker must not certify the inspected mutation when its target commit or execution identity does not match the evidence capability being used for correlation.

## Current repository seam

`Quality/Integration/test_evidence_reasoning_classification.py` already requires occurrence evidence to carry execution identity and target commit. The current implementation also checks these bindings when both sides expose them. Read-back confirms the seam is present.

## Truth-eye finding

The required negative cases are:

`same execution identity + different target commit -> UNRESOLVED`

`different execution identity + same target commit -> UNRESOLVED`

A mismatch is not automatically a contradiction because it does not establish two mutually exclusive observations about the same execution claim. It establishes failed correlation / insufficient identity binding.

## Mutation attempt

A minimal update was prepared to add explicit regression tests for both mismatch cases. The connected GitHub update surface rejected the write request at schema validation before any repository mutation occurred. Therefore no claim of mutation success or CI execution is made.

## Boundary classification

`CURRENT SEAM = VERIFIED`
`NEGATIVE TEST DESIGN = VERIFIED BY REVIEW`
`REGRESSION MUTATION = BLOCKED / NOT WRITTEN`
`CURRENT CI EXECUTION = UNRESOLVED`
`PROMOTION = NOT AUTHORIZED`

## Knowledge Delta

**KD-057 — Cross-binding mismatch is not contradiction.**

A valid execution identity bound to a different target commit, or a different execution identity bound to the inspected commit, cannot certify the inspected occurrence. The correct state is `UNRESOLVED` until correlation is repaired.

**KD-058 — Failed mutation is not a repository state change.**

A connector-side schema rejection before the write must not be represented as a repository mutation, test result, or execution failure.

## Closure

`Inspect → Define negative cases → Prepare minimal mutation → Connector rejected write before mutation → Preserve repository state → Document boundary → Close`

Next safe continuation: retry the same minimal mutation only when the connected write surface accepts the required update contract; do not create a parallel fixture or synthetic execution path.
