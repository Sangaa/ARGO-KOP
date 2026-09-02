# MUTATION MATRIX — P7 CORE EXPLICIT CERTIFICATION CLOSURE X-C1

Transaction: `MUT-2026-09-02-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X-C1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Preceding blocker side-repair: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
Work Lease: `HERMUZ-P7-X-C1-INTEGRITY-STATE-GUARD-20260902`
Priority: `7 — Core / Transaction X corrective continuation`
State: `MATERIAL CANDIDATE PREPARED / CI PENDING / X HARD HOLD`
Entry HEAD: `9758fddafc82ebecb1ff7c8a91f863b48f4711ee`
Pre-write Matrix HEAD: `344b3546342e36ef7a0eb00e0b18ece1d435c8ce`
Original X candidate: `43820d41728e39edbacb5b37de4d2ffc51063dda`
Historical failed X Runtime run: `33542068223`
SR1 exact-head Runtime run: `33607627279`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / applicable Governance / REP-011 / REP-012 + W ADDENDUM / REP-013 / REP-014 / REP-015 / REP-016 + X ADDENDUM`

## Legal entry into X-C1

Original X had two independently classified Runtime failures.

Integration classification:

`REAL SEMANTIC / IMPLEMENTATION DEFECT — TEST IMPLEMENTATION DEFECT / MARKDOWN-FORMATTING-SENSITIVE SEMANTIC ASSERTION`.

SR1 candidate `9758fddafc82ebecb1ff7c8a91f863b48f4711ee` proved the Integration repair by exact-head job split:

- Full-Stack `33607627223` — SUCCESS;
- Real Mutation Matrix `33607627357` — SUCCESS;
- M2 `33607627283` — SUCCESS;
- Runtime `33607627279` — FAILURE only at Integrity;
  - integration-tests `100175144281` — SUCCESS;
  - prototype-tests `100175144759` — SUCCESS;
  - integrity-tests `100175144669` — FAILURE.

No run is retroactively relabeled.

Integrity first failure, both historically and after SR1:

`assert "INTEGRITY HOLD" in status`

at `Quality/Integrity/test_core_inventory_consistency.py::test_core_index_inventory_files_exist_without_promoting_folder_status`.

Classification:

`STALE PRE-CERTIFICATION STATE GUARD`.

Direct source review identifies the immediately downstream `Folder Certification` and `Pending` assertions as the same source-level transient guard cohort; they are not claimed as executed historical failures.

## Prior-learning disposition

- T-C1 — DIRECTLY APPLICABLE exact-head job-split proof and handoff discipline.
- T-C2 — DIRECTLY APPLICABLE stale state-contract correction while retaining durable semantics.
- U/SR1 — DIRECTLY APPLICABLE pre-write Matrix, atomic repair, failed-evidence preservation and fresh verification sequence.

## Material correction

The inventory proof remains unchanged. X-C1 changes only the stale state tail.

Removed obsolete current-state requirements:

- `INTEGRITY HOLD`;
- `Folder Certification`;
- `Pending`.

Required current bounded-state guards after correction:

- `CLOSED_FOR_PHASE_1`;
- `CORE CERTIFIED`;
- `CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED`;
- `CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE`.

Global integrity HOLD remains an independent repository-level state; this Core-local test does not assert or clear it.

## Authorized material change set — exactly 3 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| X-C1-01 | `Quality/Integrity/test_core_inventory_consistency.py` | preserve exact inventory checks; replace only stale pre-certification state cohort with bounded closure/anti-overpromotion guards | Y | PENDING CI |
| X-C1-02 | `Repository/P7_X_INTEGRITY_STATE_GUARD_CORRECTION_2026-09-02_X-C1.md` | bind failure provenance, cohort classification, correction and non-authority | Y | PENDING CI |
| X-C1-03 | this Matrix | bind material candidate and exact-head verification | Y | PENDING CI |

Candidate binding: `THIS MATERIAL COMMIT`.

Required atomicity: exactly one commit after `344b3546342e36ef7a0eb00e0b18ece1d435c8ce`, exactly these three authorized paths, unexpected path expansion `0`.

## Durable boundaries preserved

- exact Core expected-name list unchanged;
- index membership assertions unchanged;
- physical file existence assertions unchanged;
- Core closure does not imply Phase-1 closure;
- Core certification does not imply repository-wide graph completion;
- SR1 no-auto-start-P8 invariant remains unchanged;
- REP-014 remains not a complete-graph claim;
- no relationship or provenance promotion;
- historical X/SR1 failed evidence remains preserved.

## Forbidden

- no `Core/_FOLDER_STATUS.md` mutation;
- no inventory list or file-existence mutation;
- no test deletion;
- no SR1 Integration-test mutation;
- no REP-012/REP-013/REP-014/REP-016 mutation;
- no Phase-1 closure;
- no Priority-8 start;
- no Connected Baseline closure;
- no repository-wide graph completion claim;
- no Global `BOOTED / INTEGRITY PASS`;
- no relabeling historical X or SR1 candidates as 4/4.

## Verification contract

`ONE-COMMIT/THREE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → ONLY IF 4/4: DOCUMENTATION-ONLY X CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION → REDISCOVER MAIN → RECOMPUTE GLOBAL QUEUE`.

## Preserved global limits

- Phase 1 overall OPEN;
- repository-wide graph not independently closed;
- Global Connected Baseline not independently proved;
- global integrity remains HOLD;
- Global `BOOTED / INTEGRITY PASS` NOT CLAIMED;
- Priority 8 not automatically started.

## Learning candidate

`WHEN A TEST COMBINES DURABLE INVENTORY CHECKS WITH TRANSIENT FOLDER-STATE ASSERTIONS, A GOVERNED STATE TRANSITION MUST UPDATE ONLY THE TRANSIENT COHORT AND LEAVE THE INVENTORY PROOF INTACT.`

No Governance promotion is authorized before exact-head verification.
