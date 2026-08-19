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

## Learning
1. Evidence correlation must use exact repository-relative paths; filename similarity is not relationship evidence.
2. CI evidence must carry an explicit execution identity so a historical successful run cannot be mistaken for current-HEAD evidence.
3. A connector's inability to list push-triggered runs is an observability limitation, not proof that no run exists.

## Boundary
No relationship promotion was performed. P6 remains `EXECUTION-VERIFICATION-PENDING` until a run on the exact current HEAD is independently read back.
