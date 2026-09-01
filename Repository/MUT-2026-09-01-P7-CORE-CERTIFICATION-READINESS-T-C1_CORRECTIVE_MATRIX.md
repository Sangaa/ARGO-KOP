# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C1 — STATE-TRANSITION CORRECTION

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Work Lease: `HERMUZ-P7-T-C1-CORE-READINESS-20260901`
Priority: `7 — Core`
State: `PRE-WRITE / CORRECTIVE / LEASE ACTIVE`
Entry HEAD: `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C1 exists

Parent T candidate `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d` structurally satisfied its one-commit/five-path authorization and Full-Stack verification succeeded, but exact-head Runtime verification failed.

Runtime integrity reported `8 failed / 134 passed`; the failures converge on one established semantic contract: current Core status must still contain `CROSS-LAYER VALIDATION OPEN` until the separate Explicit Core Certification Review actually closes that gate.

T changed the top status from `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN` to `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CERTIFICATION REVIEW READY`. The readiness conclusion did not itself prove that cross-layer validation had been formally closed. This was therefore a premature state transition.

Classification:

`MATERIAL_CANDIDATE_CI_FAILURE / SEMANTIC STATE-TRANSITION REGRESSION / READINESS EVIDENCE NOT INVALIDATED`.

The failed candidate remains evidence. A green Full-Stack run does not override the failed Runtime verification contract.

## Corrective semantic decision

T-C1 preserves both truths simultaneously:

- `CROSS-LAYER VALIDATION OPEN` remains explicit until the separate certification review closes it;
- `CERTIFICATION REVIEW READY` may also be explicit because the bounded readiness evidence is sufficient to open that review.

Target status semantics:

`INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY`

Certification Readiness may remain `PASS / EXPLICIT CORE CERTIFICATION REVIEW MAY OPEN / CORE STILL INTEGRITY HOLD / NOT CERTIFIED`.

Folder Certification remains Pending and Priority 7 remains OPEN.

## Test disposition

The pre-existing Priority-7 tests that require `CROSS-LAYER VALIDATION OPEN` are retained unchanged. They correctly encode the current state-transition boundary.

Only the new T-focused readiness test may be corrected because its original exact top-status assertion embodied T's premature replacement of the open marker. The corrected T test shall assert independently that both `CROSS-LAYER VALIDATION OPEN` and `CERTIFICATION REVIEW READY` are present while preserving all anti-promotion and direct-source assertions.

## Authorized corrective material change set — exactly 6 paths

| ID | Target | Action |
|---|---|---|
| C1-01 | `Core/_FOLDER_STATUS.md` | restore explicit `CROSS-LAYER VALIDATION OPEN` while retaining readiness PASS / review-ready state |
| C1-02 | `Quality/Integrity/test_core_certification_readiness_boundary.py` | correct only the new T test's premature status-transition assertion; preserve all other checks |
| C1-03 | `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md` | preserve T failure and T-C1 correction provenance |
| C1-04 | `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md` | reconcile operational readiness wording with still-open cross-layer gate |
| C1-05 | `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T_MUTATION_MATRIX.md` | bind failed T candidate to T-C1 |
| C1-06 | this Matrix | update/rebind corrective candidate state in same change set |

Candidate must be exactly one commit after this pre-write Matrix HEAD and exactly these six paths. Unexpected path expansion = `0`.

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

`PRE-WRITE MATRIX → GIT-DATA OBJECT PREPARATION → ONE-COMMIT/SIX-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK SHA/MATRIX/AUDIT STEP REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY T/T-C1 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

## Learning retained

`READINESS MAY OPEN THE NEXT REVIEW WITHOUT CLOSING THE CURRENT VALIDATION GATE.`

`A STATE LABEL MUST NOT REMOVE AN OPEN-GATE MARKER UNTIL THE GOVERNED CLOSURE DECISION HAS ACTUALLY OCCURRED.`

This is an application of existing evidence/state discipline; no new Governance rule is warranted from T-C1 alone.
