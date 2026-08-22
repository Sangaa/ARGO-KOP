# EJR-308 — HERMUZ Controlled Runtime-to-P6 Adapter Test

Date: 2026-08-22
Status: Closed — Mutation + Read-back Verified
Scope: Controlled integration experiment only

## Trigger

EJR-307 identified an unresolved semantic boundary between verified runtime lineage and P6 Evidence. The next safe experiment was to test compatibility without introducing a production promotion path.

## Experiment

Added `Quality/Integration/test_p6_runtime_lineage_adapter.py`.

The test:

1. Builds a controlled runtime result with matching execution trace lineage.
2. Requires `verify_runtime_outcome_evidence` to return `VERIFIED`.
3. Constructs P6 `Evidence` only with explicit `observation_state="OBSERVED"`.
4. Requires P6 reconciliation to preserve the current execution identity.
5. Proves a trace identity mismatch remains `HOLD` upstream.
6. Proves P6 Evidence cannot omit observation provenance.

## Boundary

This is NOT a production adapter and does NOT promote runtime evidence into canonical Memory or Relationship Authority. It is a controlled compatibility/provenance experiment.

## Verification

The new test file was read back after creation.

Blob SHA: `7209d835a41c9aed3d144249d26c8d79ed80fc15`
Commit: `5977021c265347f6f91e4a27312abd846e288f79`

The connector did not provide a live local Python execution surface in this step, so no claim of test execution is made from this mutation alone. The test is classified as `CONTROLLED_SYNTHETIC` until executed through an available test runner.

## Learning

The explicit adapter experiment demonstrates the intended semantic boundary: upstream runtime lineage must first be `VERIFIED`; only then may a controlled bridge construct P6 Evidence, and it must explicitly declare observation provenance. Upstream verification still does not confer downstream canonical or relationship authority.

## Closure

Mutation: COMPLETE
Read-back: VERIFIED
Test execution: NOT CLAIMED — pending available runner
Canonical CI execution: NOT VERIFIED
P6 root cause: NOT CLAIMED
Relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — READ-BACK VERIFIED`.
