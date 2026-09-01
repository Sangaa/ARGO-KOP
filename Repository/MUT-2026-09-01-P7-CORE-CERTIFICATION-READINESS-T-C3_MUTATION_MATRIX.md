# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C3 — POST-CI-REPAIR VERIFICATION BINDING

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C3`
Root Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Corrective predecessors: `T-C1`, `T-C2`
Dependent side-repair: `MUT-2026-09-01-CI-REAL-MATRIX-TRIGGER-COVERAGE-U`
Work Lease: `HERMUZ-P7-T-C3-READINESS-VERIFY-20260901`
Priority: `7 — Core`
State: `VERIFICATION-BINDING CANDIDATE PREPARED / CI PENDING / LEASE ACTIVE`
Entry HEAD: `663565bbca94a5dbda4a4f7c7f6d93d33cfbab00`
Pre-write Matrix HEAD: `26edd336a67ae236537f2b08f1384723023bfab3`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C3 exists

T-C2 semantic candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` restored Runtime integrity/prototype/integration and passed Full-Stack and M2. Real Mutation Matrix Regression did not run on that exact SHA because the then-current workflow trigger did not cover corrective Matrix filenames.

Side-repair U repaired that trigger gap and passed all four required workflows on both material candidate `f2bab15f36a32f7251df9800aec44581af540add` and closure HEAD `663565bbca94a5dbda4a4f7c7f6d93d33cfbab00`.

T-C3 therefore binds the unchanged readiness semantics to a fresh exact HEAD under the repaired CI environment. It does not backfill T-C2 retroactively.

## Semantic invariance rule

T-C3 does not modify:

- `Core/_FOLDER_STATUS.md`;
- readiness/integration tests;
- canonical Core sources;
- REP-014 or REP-020;
- relationship rows;
- certification or Priority-7 state.

State under verification remains:

`INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY / CERTIFICATION READINESS PASS / NOT CERTIFIED / FOLDER CERTIFICATION PENDING / PRIORITY 7 OPEN`.

`RUN-002 → CORE-003 = REFERENCES` remains `VALIDATED-NOT-REGISTERED / NON-DEPENDENCY`.

## Authorized verification-binding change set — exactly 4 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| C3-01 | `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md` | bind full failure/repair/verification provenance | Y | PENDING CI |
| C3-02 | `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md` | bind operational readiness to T-C3 exact-head verification | Y | PENDING CI |
| C3-03 | `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2_CORRECTIVE_MATRIX.md` | preserve T-C2 result and non-retroactive handoff | Y | PENDING CI |
| C3-04 | this Matrix | bind T-C3 candidate in same change set | Y | PENDING CI |

Candidate must be exactly one commit after `26edd336a67ae236537f2b08f1384723023bfab3`, exactly these four paths, and have unexpected path expansion = `0`.

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

## Exact-head verification contract

T-C3 candidate must produce and pass on the same exact SHA:

- Full-Stack Repository Audit;
- ARGO Runtime Prototype and Integration Tests;
- Real Mutation Matrix Regression;
- M2 Multi-Channel Proposal Training.

Full-Stack must pass exact checkout-SHA binding, Matrix preflight, Matrix semantic enforcement, current-change-set Matrix enforcement and repository-wide audit. Runtime integrity/prototype/integration jobs must all succeed.

Only then may a documentation-only closure mark the readiness chain `FUNCTIONAL-CLOSED / CI-VERIFIED / CORE CERTIFICATION READINESS PASS / PRIORITY 7 OPEN`, followed by closure-head verification before Resume-Safe is operationally true.

## Learning retained

`MISSING VERIFICATION MUST BE REBOUND TO A FRESH EXACT HEAD AFTER THE VERIFICATION MECHANISM IS REPAIRED; IT MUST NOT BE BACKFILLED RETROACTIVELY.`
