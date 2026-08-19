# EJR-281 — HERMUZ P6 Test / Execution Logic Review

Date: 2026-08-19
Status: OPEN / INTEGRITY HOLD

## Finding
The P6 correlation helper used a basename fallback after exact-path matching. This could falsely map unrelated files sharing the same filename, violating the fail-closed / no-guessing rule.

## Correction
- Removed basename-only correlation.
- Added regression coverage proving same-basename paths remain `UNMAPPED`.
- Added a CI execution-identity gate asserting `git rev-parse HEAD == github.sha`.
- Added an execution-identity artifact containing workflow/run/event/ref/SHA/before metadata.
- Added `pull_request -> main` triggering to ensure the validation workflow is exercised on PRs; the workflow-only correction was merged as PR #14.

## Session Results
- Historical Run `32048160297` and its artifacts were verified as stale because they identify SHA `23af947...`, not the current baseline.
- PR #14 was merged successfully with expected head SHA `7cf557588...`; merge result became `main` SHA `5ad6ba62b9d9431439c7457da02eb6bb844bf447`.
- A fresh workflow Run for that exact main SHA is not currently observable through the available commit-run query surface; therefore no stale run was reused and P6 was not promoted.

## Learning
1. Evidence correlation must use exact repository-relative paths; filename similarity is not relationship evidence.
2. CI evidence must carry an explicit execution identity so a historical successful run cannot be mistaken for current-HEAD evidence.
3. Run, artifact, and current HEAD must form one immutable evidence chain: `current HEAD == run SHA == artifact SHA`.
4. Historical successful evidence should be marked `SUPERSEDED/STALE`, not deleted, so it remains auditable without being reusable.
5. A connector's inability to list push-triggered runs is an observability limitation, not proof that no run exists.
6. When a validation trigger is missing, fix the trigger before interpreting missing execution evidence as a test failure.

## Boundary
No relationship promotion was performed. P6 remains `EXECUTION-VERIFICATION-PENDING` until a fresh run on the exact current HEAD is independently read back and its Jobs/Artifacts pass the same SHA-chain validation.
