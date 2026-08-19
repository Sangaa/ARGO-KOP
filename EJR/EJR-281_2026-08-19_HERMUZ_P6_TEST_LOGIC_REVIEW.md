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
- Added explicit P6 execution classification so a successful historical run with a stale SHA is `VALID_EXECUTION_STALE_BASELINE`, not `EXECUTION_FAILED`.

## Session Results
- Historical Run `32048160297` and its artifacts were verified as stale because they identify SHA `23af947...`, not the current baseline.
- PR #14 was merged successfully with expected head SHA `7cf557588...`; merge result became `main` SHA `5ad6ba62b9d9431439c7457da02eb6bb844bf447`.
- A fresh workflow Run for that exact main SHA was not observable through the available commit-run query surface; therefore no stale run was reused and P6 was not promoted.
- Subsequent documentation moved `main` to `fab362cc...`, then to `4f2001a...`; no current-HEAD execution evidence was assumed from older runs.
- The workflow definition was re-read from the current `main` and confirmed to contain `push: main`, `pull_request: main`, and `workflow_dispatch`, plus the checkout-SHA identity gate and CI identity artifact. A controlled new commit is therefore being used to distinguish a trigger failure from an observability/query limitation.

## Learning
1. Evidence correlation must use exact repository-relative paths; filename similarity is not relationship evidence.
2. CI evidence must carry an explicit execution identity so a historical successful run cannot be mistaken for current-HEAD evidence.
3. Run, artifact, and current HEAD should form one immutable provenance chain for current-baseline promotion: `current HEAD == run SHA == artifact SHA`.
4. Historical successful evidence should be classified `VALID_EXECUTION_STALE_BASELINE` rather than treated as a failed test; it remains ineligible for current-baseline promotion until freshness is restored.
5. A connector's inability to list push-triggered runs is an observability limitation, not proof that no run exists.
6. When a validation trigger is missing, fix the trigger before interpreting missing execution evidence as a test failure.
7. P6 must separate **execution validity** from **evidence freshness/provenance**: a passing old run proves the tested revision passed; it does not prove the current revision passed.
8. A workflow file containing the expected triggers is not sufficient evidence that the trigger executed; trigger behavior must be verified by observing a run whose SHA equals the commit that caused the event.

## Boundary
No relationship promotion was performed. P6 remains `EXECUTION-VERIFICATION-PENDING` for the current baseline until a fresh run on the exact current HEAD is independently read back and its Jobs/Artifacts pass the SHA-chain validation. Historical successful evidence remains auditable and explicitly classified rather than discarded.
