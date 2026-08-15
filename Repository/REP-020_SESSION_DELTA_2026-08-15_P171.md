# REP-020 — SESSION DELTA — 2026-08-15 — P171

Platform: ARGO KOP
Checkpoint: P171
Status: Active / Integrity Hold
Predecessor: P170

## Work Completed

- Advanced the GAP-MAP from manually supplied candidate kinds to deterministic, path-bounded candidate classification.
- Added `classify_candidate_path()` to classify discovery candidates as `implementation`, `test`, `contract`, `trace`, `documentation`, or `other`.
- Added regression coverage for representative classifications and for the non-promotional rule.
- Preserved the existing safety boundary: candidate classification is discovery metadata only; it cannot change a seam state or promote a seam to `CONNECTED`.

## Why This Is the Smallest Useful Build

The remaining candidate queue needs triage by evidence-bearing role. Path classification provides a deterministic first filter without inspecting arbitrary content and without conflating a file's existence with architectural connectivity.

## Validation Boundary

The changes are committed to `main`, but no CI PASS is claimed until an observable workflow execution confirms the new tests. Static inspection alone is not treated as runtime evidence.

## Next Highest-Value Work

Observe CI for this commit. If PASS, run the resulting GAP-MAP classification against the current candidate set and prioritize only implementation-bearing candidates that have a plausible Producer -> Consumer relationship.

## Checkpoint Classification

`GAP_TRIAGE_CAPABILITY_ADDED / CI_PENDING`

P171 does not close the Connected Baseline gate.
