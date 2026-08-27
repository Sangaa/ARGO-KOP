# P348 — Regression Test Write Failure / Integrity Hold

Status: `CLOSED / WRITE-FAILED / NO-COMPENSATING-MUTATION`

## Re-entry
Current `main` was verified before the attempted mutation. `PROJECT_STATUS.md` states the active objective is connected-baseline stabilization and that integration evidence must precede completion claims.

## Prior-Learning Retrieval
Existing canonical-spine integration audit, registry, gap-map, and prior seam-evidence learning were inspected before proposing the regression addition.

## Intended Work
Add focused regression tests for `canonical_spine_integration_audit._state_from_verified_record`, specifically:
- accept a materialized canonical execution trace;
- reject non-trace JSON;
- reject parent-traversal evidence references.

## Tool Failure
The GitHub create-file operation was attempted once and rejected with HTTP 422: `"sha" wasn't supplied`.

No retry of the same write was performed, and no Canonical artifact was modified to compensate for the failed write.

## Evidence Interpretation
The failure proves only that the selected write operation did not execute under the current connector contract. It does NOT prove a repository defect, test defect, or inability to write generally.

## Decision
Keep the intended regression test uncommitted. The write failure itself is preserved as operational evidence. Before retrying, obtain/confirm the correct write contract or use a verified existing-file update/creation path; do not infer that a different write mechanism is safe without evidence.

`WRITE = FAILED`
`TEST ADDITION = NOT COMMITTED`
`CANONICAL COMPENSATION = NONE`
`RUNTIME = UNCHANGED`
`AUTHORITY = UNCHANGED`
`SESSION = CLOSED`
