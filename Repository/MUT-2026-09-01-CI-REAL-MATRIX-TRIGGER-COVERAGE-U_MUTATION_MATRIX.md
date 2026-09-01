# MUTATION MATRIX — CI REAL MATRIX TRIGGER COVERAGE — U

Transaction: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
Work Lease: `HERMUZ-CI-U-REAL-MATRIX-TRIGGER-20260901`
State: `MATERIAL CANDIDATE PREPARED / CI PENDING / SIDE-REPAIR / LEASE ACTIVE`
Entry HEAD: `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`
Pre-write Matrix HEAD: `ec4270d4584ce692ab0cb0f3f0ed8bd6d2ecf916`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Trigger gap

T-C2 material candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` changed corrective Matrix paths but the current Real Mutation Matrix workflow triggered only on:

`Repository/*MUTATION_MATRIX*.md`

Corrective paths use the naming family `...CORRECTIVE_MATRIX.md`, so Real Mutation Matrix Regression did not run on T-C2.

Classification:

`CI WORKFLOW TRIGGER COVERAGE GAP / REGRESSION SUITE PRESENT BUT NOT INVOKED FOR CORRECTIVE MATRIX NAMING FAMILY`.

## Authorized material change set — exactly 4 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| U-01 | `.github/workflows/real-matrix-regression.yml` | add `Repository/*CORRECTIVE_MATRIX*.md` while preserving all existing triggers and job semantics | Y | PENDING CI |
| U-02 | `Quality/Integrity/test_real_matrix_workflow_trigger_coverage.py` | add focused trigger-coverage regression | Y | PENDING CI |
| U-03 | `Repository/CI_REAL_MATRIX_TRIGGER_COVERAGE_REPAIR_2026-09-01_U.md` | record discovery, bounded repair and return rule | Y | PENDING CI |
| U-04 | this Matrix | bind candidate in same material change set | Y | PENDING CI |

Candidate must be exactly one commit after `ec4270d4584ce692ab0cb0f3f0ed8bd6d2ecf916` and exactly these four paths. Unexpected path expansion = `0`.

## Preserved workflow semantics

The repair is additive only. The workflow must continue to include:

- `Quality/Integration/run_real_matrix_regression.py` trigger;
- `Quality/Integration/check_mutation_matrix_semantics.py` trigger;
- `Repository/*MUTATION_MATRIX*.md` trigger;
- its own workflow-file trigger;
- runner command `python Quality/Integration/run_real_matrix_regression.py`.

New required trigger:

- `Repository/*CORRECTIVE_MATRIX*.md`.

## Forbidden

- no T/T-C1/T-C2 semantic mutation in U;
- no Core status mutation;
- no REP-014/REP-016/REP-020 mutation;
- no weakening of Matrix semantic validation;
- no Priority-7 promotion or closure;
- no Phase-1 / Connected Baseline / Global PASS claim.

## Return rule

`SIDE-REPAIR CLOSED → RETURN TO PREVIOUS GLOBAL PRIORITY / P7 T-C2 VERIFICATION`.

U is not global NEXT authority.

## Verification contract

`ONE-COMMIT/FOUR-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD FOUR REQUIRED WORKFLOWS → FULL-STACK SHA/MATRIX/AUDIT REVIEW → RUNTIME JOB REVIEW → DOCUMENTATION-ONLY U CLOSURE → CLOSURE-HEAD VERIFICATION → RETURN TO T-C2`.

## Learning retained

`A VALID MATRIX REGRESSION SUITE CAN STILL HAVE A BLIND SPOT AT THE WORKFLOW TRIGGER BOUNDARY.`

`TRIGGER COVERAGE IS PART OF TEST EFFECTIVENESS.`

No new Governance rule is warranted; this is a bounded CI repair.
