# MUTATION MATRIX — CI REAL MATRIX TRIGGER COVERAGE — U

Transaction: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
Work Lease: `HERMUZ-CI-U-REAL-MATRIX-TRIGGER-20260901`
State: `PRE-WRITE MATRIX / LEASE ACTIVE / SIDE-REPAIR / RETURN TO P7 T-C2 AFTER CLOSURE`
Entry HEAD: `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Trigger gap

T-C2 material candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` changed two corrective Matrix paths:

- `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1_CORRECTIVE_MATRIX.md`;
- `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2_CORRECTIVE_MATRIX.md`.

The current Real Mutation Matrix workflow triggers only on:

`Repository/*MUTATION_MATRIX*.md`

Neither corrective filename contains the literal `MUTATION_MATRIX`, so Real Mutation Matrix Regression did not run on the T-C2 candidate even though corrective Matrix semantics materially changed.

This is a CI trigger-coverage defect, not a T-C2 semantic failure.

## Required repair

The Real Mutation Matrix workflow must trigger for both canonical Matrix naming families currently present in repository practice:

- `Repository/*MUTATION_MATRIX*.md`;
- `Repository/*CORRECTIVE_MATRIX*.md`.

A focused Integrity regression must verify both patterns are present so future corrective matrices cannot silently bypass the workflow trigger.

## Authorized material change set — exactly 4 paths

1. `.github/workflows/real-matrix-regression.yml`
   - add `Repository/*CORRECTIVE_MATRIX*.md` to push paths;
   - preserve all existing trigger paths and job semantics.
2. `Quality/Integrity/test_real_matrix_workflow_trigger_coverage.py`
   - new focused regression requiring both Matrix trigger families and preserving the existing runner command.
3. `Repository/CI_REAL_MATRIX_TRIGGER_COVERAGE_REPAIR_2026-09-01_U.md`
   - evidence record for discovery, repair, non-authority and return-to-P7 rule.
4. this Matrix
   - bind U material candidate in the same change set.

## Forbidden

- no T/T-C1/T-C2 semantic mutation in U;
- no Core status mutation;
- no REP-014/REP-016/REP-020 mutation;
- no weakening of Matrix semantic validation;
- no test deletion;
- no Priority-7 promotion or closure;
- no Phase-1 / Connected Baseline / Global PASS claim.

## Atomicity contract

After this pre-write Matrix commit, U candidate must be exactly one commit and exactly the four authorized paths. Unexpected path expansion = `0`.

## Return rule

`SIDE-REPAIR CLOSED → RETURN TO PREVIOUS GLOBAL PRIORITY / P7 T-C2 VERIFICATION`.

U does not become global NEXT authority.

## Verification contract

`ONE-COMMIT/FOUR-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD FOUR REQUIRED WORKFLOWS → FULL-STACK + RUNTIME JOB REVIEW → DOCUMENTATION-ONLY U CLOSURE → CLOSURE-HEAD VERIFICATION → RETURN TO T-C2`.

## Learning candidate

`A VALID MATRIX REGRESSION SUITE CAN STILL HAVE A BLIND SPOT AT THE WORKFLOW TRIGGER BOUNDARY.`

No governance change is authorized; first repair the concrete CI trigger gap and verify it.
