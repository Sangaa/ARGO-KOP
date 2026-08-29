# Branch Disposition — hermuz/p234-safe-gate

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-058`
Baseline inspected: `main@98d78edab9cac1ab14b0e831d1c1c3ed0e585a61`
Branch: `hermuz/p234-safe-gate`

## Evidence

The branch diverges with 11 branch-only commits and carries a non-production `Runtime/Prototype/exact_blob_adapter.py` plus KRS Pilot-3 matrices/session deltas.

The adapter explicitly identifies itself as a non-production exact-blob verification seam. The branch's own P238 closure states that exact-SHA execution could not be verified because no workflow run was bound to the corrected consumer commit, and explicitly records: `No mutation. No fabricated execution evidence. No merge or promotion.`

Current main now contains the later read-only GitHub immutable-artifact resolver boundary. It requires an exact 40-character commit SHA, reads an exact path at that immutable ref, records the returned GitHub blob SHA, performs no repository writes, and does not upgrade provider/model authenticity.

## Disposition

`HISTORICAL_NONPRODUCTION_EXACT_BLOB_PILOT / OWN_CLOSURE_NO_MERGE_NO_PROMOTION / LATER_IMMUTABLE_ARTIFACT_RESOLVER_ON_MAIN / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

The historical prototype is not promoted merely because it demonstrates an exact-blob technique. Its exact-head execution claim remained unverified at its own checkpoint, and current main implements a later governed immutable-artifact evidence boundary.

## Learning

A useful prototype can be superseded at the architectural boundary without claiming that its original unexecuted checkpoint became execution-verified. Preserve the historical failure-to-observe as evidence; do not retroactively promote it.
