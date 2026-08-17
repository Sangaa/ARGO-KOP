# SESSION STEP CLOSURE — REP-001 WORKFLOW APPLY-GUARD FIX 010

Transaction: `MUT-2026-08-17-REP001-001`

## Intent
Correct the GOV-014 Apply Candidate guard after attempt 010.

## Root Cause
The candidate test created untracked `__pycache__` directories, and the guard counted all `git status --short` lines. The request file itself was already tracked at HEAD, so it was not a working-tree modification before `git rm`.

## Executed
- Changed pre-commit working-tree assertion to `git status --porcelain --untracked-files=no`.
- Required exactly one tracked modification before staging: `REP-001`.
- After `git rm` of the request, required exactly two tracked changes: modified REP-001 and deleted request.

## Safety
No REP-001 mutation persisted in this repair step.

## Decision
Fix 010 CLOSED.

## Next Action
Trigger transaction attempt 4 with unchanged target/source/scope.
