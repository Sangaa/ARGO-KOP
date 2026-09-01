# CI Real Mutation Matrix Trigger Coverage Repair — U

Date: 2026-09-01
Transaction: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / SIDE-REPAIR CLOSED / RETURN TO P7 T-C2`
Entry HEAD: `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`
Pre-write Matrix HEAD: `ec4270d4584ce692ab0cb0f3f0ed8bd6d2ecf916`
Verified material candidate: `f2bab15f36a32f7251df9800aec44581af540add`

## Discovery

During exact-head verification of Priority-7 T-C2 candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`, Runtime, Full-Stack and M2 were triggered, but Real Mutation Matrix Regression was absent from the exact-head run set.

Direct workflow inspection established the cause: the Real Matrix workflow covered only `Repository/*MUTATION_MATRIX*.md`, while corrective artifacts use the distinct naming family `...CORRECTIVE_MATRIX.md`.

Classification:

`CI WORKFLOW TRIGGER COVERAGE GAP / REGRESSION SUITE PRESENT BUT NOT INVOKED FOR CORRECTIVE MATRIX NAMING FAMILY`.

## Repair

U added the additive trigger:

`Repository/*CORRECTIVE_MATRIX*.md`

while preserving the original Matrix trigger, code triggers, self-trigger, and runner command.

Focused regression:

`Quality/Integrity/test_real_matrix_workflow_trigger_coverage.py`

requires both Matrix naming families and the existing Real Matrix runner semantics.

## Atomicity

U material candidate was exactly one commit after the pre-write Matrix HEAD and changed exactly four authorized paths:

1. `.github/workflows/real-matrix-regression.yml`;
2. `Quality/Integrity/test_real_matrix_workflow_trigger_coverage.py`;
3. this evidence record;
4. `Repository/MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U_MUTATION_MATRIX.md`.

Unexpected path expansion: `0`.

## Exact-head verification — material candidate

Candidate `f2bab15f36a32f7251df9800aec44581af540add` produced all four required workflows, including the previously missing Real Matrix workflow:

- Real Mutation Matrix Regression — run `33536474491` — `SUCCESS`;
- M2 Multi-Channel Proposal Training — run `33536474498` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests — run `33536474494` — `SUCCESS`;
- Full-Stack Repository Audit — run `33536474568` — `SUCCESS`.

Runtime job split:

- integrity-tests — `SUCCESS`;
- prototype-tests — `SUCCESS`;
- integration-tests — `SUCCESS`.

Full-Stack `repository-audit` succeeded, including exact checkout-SHA binding, Mutation Matrix preflight, Mutation Matrix semantic regression, current-change-set Matrix enforcement, repository-wide audit, and runtime-evidence emission.

Result:

`U MATERIAL CANDIDATE = 4/4 REQUIRED WORKFLOWS SUCCESS`.

## Scope boundary preserved

U changed CI trigger coverage only. It did not mutate Core status/certification semantics, T/T-C1/T-C2 semantics, REP-014, REP-016 or REP-020, and did not close Priority 7 or promote Phase 1 / Connected Baseline / Global PASS.

## Learning retained

`A VALID REGRESSION SUITE IS NOT EFFECTIVE IF ITS WORKFLOW TRIGGER DOES NOT COVER THE REPOSITORY'S ACTUAL ARTIFACT NAMING FAMILIES.`

`TRIGGER COVERAGE IS PART OF TEST EFFECTIVENESS.`

No new Governance rule was required; the concrete CI blind spot was repaired directly.

## Closure / return rule

U is functionally closed and may become resume-safe only after this documentation-only closure HEAD itself passes the required exact-head workflow verification.

After closure-head verification:

`SIDE-REPAIR CLOSED → RETURN TO PREVIOUS GLOBAL PRIORITY / P7 T-C2 VERIFICATION`.
