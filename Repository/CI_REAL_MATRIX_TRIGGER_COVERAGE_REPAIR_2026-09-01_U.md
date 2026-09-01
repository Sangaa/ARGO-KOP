# CI Real Mutation Matrix Trigger Coverage Repair — U

Date: 2026-09-01
Transaction: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
State: `MATERIAL CANDIDATE PREPARED / SIDE-REPAIR / CI PENDING`
Entry HEAD: `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`
Pre-write Matrix HEAD: `ec4270d4584ce692ab0cb0f3f0ed8bd6d2ecf916`

## Discovery

During exact-head verification of Priority-7 T-C2 candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0`, Runtime, Full-Stack and M2 were triggered, but Real Mutation Matrix Regression was absent from the exact-head run set.

Direct workflow inspection established the cause:

`Repository/*MUTATION_MATRIX*.md`

was the only repository Matrix filename trigger.

T-C2 changed corrective Matrix files named `...CORRECTIVE_MATRIX.md`, which do not contain the literal `MUTATION_MATRIX`. Therefore the Real Matrix regression suite had a workflow-trigger blind spot for corrective Matrix mutations.

## Repair

U adds a second additive path trigger:

`Repository/*CORRECTIVE_MATRIX*.md`

The original `Repository/*MUTATION_MATRIX*.md` trigger and all existing code/workflow triggers remain unchanged.

A focused Integrity regression now requires both naming families and preserves the existing Real Matrix runner command.

## Scope boundary

U changes CI trigger coverage only.

It does not:

- mutate Core state or certification semantics;
- modify T/T-C1/T-C2 evidence;
- modify REP-014, REP-016 or REP-020;
- weaken Matrix semantic checks;
- close Priority 7;
- promote Phase 1 / Connected Baseline / Global PASS.

## Return rule

After U closes resume-safe:

`RETURN TO P7 T-C2 EXACT-HEAD VERIFICATION / CLOSURE PATH`.

## Learning retained

`A VALID REGRESSION SUITE IS NOT EFFECTIVE IF ITS WORKFLOW TRIGGER DOES NOT COVER THE REPOSITORY'S ACTUAL ARTIFACT NAMING FAMILIES.`

No new Governance rule is warranted from this isolated repair.
