# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C3 — POST-CI-REPAIR VERIFICATION BINDING

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C3`
Root Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Corrective predecessors: `T-C1`, `T-C2`
Dependent side-repair: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
Work Lease: `HERMUZ-P7-T-C3-READINESS-VERIFY-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX / VERIFICATION-BINDING ONLY / LEASE ACTIVE`
Entry HEAD: `663565bbca94a5dbda4a4f7c7f6d93d33cfbab00`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C3 exists

T-C2 semantic candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` restored all Runtime jobs and also passed Full-Stack and M2. Real Mutation Matrix Regression did not run on that exact SHA because the then-current workflow trigger covered `Repository/*MUTATION_MATRIX*.md` but not corrective Matrix filenames `...CORRECTIVE_MATRIX.md`.

Side-repair U repaired that CI trigger gap and then passed both its material candidate and closure-head verification with all four required workflows.

The original T-C2 SHA cannot retroactively acquire a workflow that was never triggered. T-C3 therefore creates a fresh documentation/verification-binding HEAD carrying the unchanged Core readiness semantics under the repaired CI trigger environment.

## Semantic invariance rule

T-C3 MUST NOT modify:

- `Core/_FOLDER_STATUS.md`;
- the T-focused readiness Integrity test;
- `Quality/Integration/test_core_p7_status_sync.py`;
- any canonical Core source;
- REP-014 or REP-020;
- any relationship row;
- any certification or Priority-7 status.

The semantic state under verification remains exactly:

`INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY / CERTIFICATION READINESS PASS / NOT CERTIFIED / FOLDER CERTIFICATION PENDING / PRIORITY 7 OPEN`.

`RUN-002 → CORE-003 = REFERENCES` remains `VALIDATED-NOT-REGISTERED / NON-DEPENDENCY`.

## Authorized material change set — exactly 4 documentation/control paths

1. `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md`
   - bind the T/T-C1/T-C2 failure chain, U side-repair and T-C3 verification purpose.
2. `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md`
   - bind operational readiness to fresh T-C3 exact-head verification without changing Priority-7 authority.
3. `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2_CORRECTIVE_MATRIX.md`
   - preserve T-C2 result and hand off the missing fourth-workflow proof to T-C3.
4. this T-C3 Matrix
   - bind verification candidate in the same change set.

## Explicitly forbidden

- no Core semantic/status mutation;
- no test mutation;
- no REP-014/REP-020 mutation;
- no REL-073 or forced RUN-002→CORE-003 registration;
- no Core certification;
- no closure of `CROSS-LAYER VALIDATION OPEN`;
- no Priority-7 closure;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim;
- no statement that T-C2 itself was 4/4.

## Atomicity contract

After this pre-write Matrix commit, T-C3 verification candidate must be exactly one commit and exactly the four authorized paths above. Unexpected path expansion = `0`.

## Exact-head verification contract

T-C3 must produce and pass all four required workflows on the same exact HEAD:

- Full-Stack Repository Audit;
- ARGO Runtime Prototype and Integration Tests;
- Real Mutation Matrix Regression;
- M2 Multi-Channel Proposal Training.

Full-Stack must prove exact checkout-SHA binding, Matrix preflight/semantic/current-change-set enforcement and repository-wide audit. Runtime must prove integrity/prototype/integration jobs all success.

Only after that may T/T-C1/T-C2/T-C3 be closed as `CORE CERTIFICATION READINESS PASS / RESUME-SAFE / PRIORITY 7 OPEN`.

## Learning retained

`MISSING VERIFICATION MUST BE REBOUND TO A FRESH EXACT HEAD AFTER THE VERIFICATION MECHANISM IS REPAIRED; IT MUST NOT BE BACKFILLED RETROACTIVELY.`
