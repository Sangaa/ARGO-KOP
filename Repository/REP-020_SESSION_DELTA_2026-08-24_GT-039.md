# REP-020 Session Delta — GT-039

Date: 2026-08-24
Checkpoint: GT-039
State: BUILD CONTINUATION / CONTROLLED REGRESSION RECORDED / CI EXECUTION PENDING

## Current Build Point

GT-039 — Provenance Root/Parent Consistency.

## Evidence

Current test artifact:
`Quality/Integration/test_evidence_reasoning_classification.py`

Test mutation commit:
`8ba54980c0e8eb684d00c6be739b109d0deb5a58`

Learning record:
`EJR/EJR-300_2026-08-24_GT-039_PROVENANCE_ROOT_PARENT_CONSISTENCY.md`

## Result

The controlled provenance invariant is now:

`child.provenance_root` must agree with the provenance root of `child.provenance_parent` when both are declared.

The case:

- Root = `ROOT-A`
- Child `provenance_parent = ROOT-A`
- Child `provenance_root = ROOT-B`

is classified as:

`INVALID PROVENANCE`

and dependent evidence comparison remains:

`UNRESOLVED`

It is not classified as `CONTRADICTION`, because the conflict is in lineage structure rather than conflicting observed values of the same claim.

## Verification Boundary

The modified test file was re-read after mutation. A bounded local semantic execution of the GT-039 invariant returned:

- mismatch case → `INVALID PROVENANCE`
- matched root/parent case → `VALID PROVENANCE`

The repository's runtime integration workflow is configured to run `Quality/Integration`, but no workflow run was exposed for commit `8ba54980c0e8eb684d00c6be739b109d0deb5a58`; therefore CI/runtime PASS is not claimed.

## Next Safe Continuation

Continue with the next provenance consistency boundary only after preserving the GT-039 rule as regression evidence. Do not promote this result to a broader canonical rule outside the tested provenance boundary without additional evidence.
