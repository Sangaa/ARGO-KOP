# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C1 — STATE-TRANSITION CORRECTION

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Work Lease: `HERMUZ-P7-T-C1-CORE-READINESS-20260901`
Priority: `7 — Core`
State: `CORRECTIVE MATERIAL CANDIDATE PREPARED / CI PENDING / LEASE ACTIVE`
Entry HEAD: `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d`
Pre-write Matrix HEAD: `110eab997d9027f575cb306d9175565834098e82`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C1 exists

Parent T candidate `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d` structurally satisfied its one-commit/five-path authorization and passed Full-Stack, Real Mutation Matrix and M2, but exact-head Runtime verification failed.

Exact T workflow evidence:

- Full-Stack Repository Audit `33534072084` — `SUCCESS`;
- Real Mutation Matrix Regression `33534071888` — `SUCCESS`;
- M2 Multi-Channel Proposal Training `33534072032` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests `33534072160` — `FAILURE`.

Runtime job evidence:

- `integrity-tests` — `FAILURE`;
- `prototype-tests` — `SUCCESS`;
- `integration-tests` — `FAILURE`.

The failures converge on one established semantic contract: current Core status must still contain `CROSS-LAYER VALIDATION OPEN` until the separate Explicit Core Certification Review actually closes or redirects that gate.

T changed the top status from `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN` to `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CERTIFICATION REVIEW READY`. The readiness conclusion did not itself prove that cross-layer validation had been formally closed. This was a premature state transition.

Classification:

`MATERIAL_CANDIDATE_CI_FAILURE / SEMANTIC STATE-TRANSITION REGRESSION / READINESS EVIDENCE NOT INVALIDATED`.

The failed candidate remains evidence. A green Full-Stack run does not override failed Runtime verification.

## Corrective semantic decision

T-C1 preserves both truths simultaneously:

- `CROSS-LAYER VALIDATION OPEN` remains explicit until the separate certification review closes or redirects it;
- `CERTIFICATION REVIEW READY` remains explicit because bounded evidence is sufficient to open that review.

Target status semantics:

`INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY`

Certification Readiness remains:

`PASS / EXPLICIT CORE CERTIFICATION REVIEW MAY OPEN / CORE STILL INTEGRITY HOLD / NOT CERTIFIED`.

Folder Certification remains Pending and Priority 7 remains OPEN.

## Test disposition

The pre-existing Priority-7 tests that require `CROSS-LAYER VALIDATION OPEN` are retained unchanged. They correctly encode the current state-transition boundary.

Only the new T-focused readiness test is corrected because its original exact top-status assertion embodied T's premature replacement. The corrected T test asserts independently that both `CROSS-LAYER VALIDATION OPEN` and `CERTIFICATION REVIEW READY` are present while preserving all anti-promotion and direct-source assertions.

## Authorized corrective material change set — exactly 6 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| C1-01 | `Core/_FOLDER_STATUS.md` | restore explicit `CROSS-LAYER VALIDATION OPEN` while retaining readiness PASS / review-ready state | Y | PENDING CI |
| C1-02 | `Quality/Integrity/test_core_certification_readiness_boundary.py` | correct only the new T test's premature status-transition assertion; preserve all other checks | Y | PENDING CI |
| C1-03 | `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md` | preserve T failure and T-C1 correction provenance | Y | PENDING CI |
| C1-04 | `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md` | reconcile operational readiness wording with still-open cross-layer gate | Y | PENDING CI |
| C1-05 | `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T_MUTATION_MATRIX.md` | bind failed T candidate to T-C1 | Y | PENDING CI |
| C1-06 | this Matrix | update/rebind corrective candidate state in same change set | Y | PENDING CI |

Candidate must be exactly one commit after pre-write Matrix HEAD `110eab997d9027f575cb306d9175565834098e82` and exactly these six paths. Unexpected path expansion = `0`.

## Explicitly forbidden

- no modification of any pre-existing test that detected the T failure;
- no mutation of canonical Core source files;
- no REP-014 or REP-020 mutation;
- no REL-073 or other relationship registration;
- no removal/weakening of readiness direct-source evidence;
- no Core certification;
- no Priority-7 closure;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim;
- no rerun-only bypass of the failed candidate.

## Verification contract

`GIT-DATA OBJECT PREPARATION → ONE-COMMIT/SIX-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK SHA/MATRIX/AUDIT STEP REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY T/T-C1 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

## Learning retained

`READINESS MAY OPEN THE NEXT REVIEW WITHOUT CLOSING THE CURRENT VALIDATION GATE.`

`A STATE LABEL MUST NOT REMOVE AN OPEN-GATE MARKER UNTIL THE GOVERNED CLOSURE DECISION HAS ACTUALLY OCCURRED.`

This is an application of existing evidence/state discipline; no new Governance rule is warranted from T-C1 alone.
