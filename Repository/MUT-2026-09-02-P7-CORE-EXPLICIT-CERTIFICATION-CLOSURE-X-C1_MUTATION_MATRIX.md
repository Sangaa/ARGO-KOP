# MUTATION MATRIX — P7 CORE EXPLICIT CERTIFICATION CLOSURE X-C1

Transaction: `MUT-2026-09-02-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X-C1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Preceding blocker side-repair: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
Work Lease: `HERMUZ-P7-X-C1-INTEGRITY-STATE-GUARD-20260902`
Priority: `7 — Core / Transaction X corrective continuation`
State: `PRE-WRITE MATRIX / LEASE ACTIVE / X HARD HOLD / INTEGRITY CORRECTION ONLY`
Entry HEAD: `9758fddafc82ebecb1ff7c8a91f863b48f4711ee`
Original X candidate: `43820d41728e39edbacb5b37de4d2ffc51063dda`
Historical failed X Runtime run: `33542068223`
SR1 exact-head Runtime run: `33607627279`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / applicable Governance / REP-011 / REP-012 + W ADDENDUM / REP-013 / REP-014 / REP-015 / REP-016 + X ADDENDUM`

## Why X-C1 is now legal

Original X candidate `43820d41728e39edbacb5b37de4d2ffc51063dda` failed required Runtime verification in two independently classified jobs.

### Integration failure — already isolated and functionally repaired by SR1

Historical Integration failure:

`Quality/Integration/test_core_p7_status_sync.py::test_priority7_current_state_is_explicit_bounded_closure`

`assert "does not auto-start Priority 8" in queue`

Root cause: the durable queue invariant existed as `does **not** auto-start Priority 8`; raw Markdown emphasis made the unformatted substring assertion fail.

Classification:

`REAL SEMANTIC / IMPLEMENTATION DEFECT — TEST IMPLEMENTATION DEFECT / MARKDOWN-FORMATTING-SENSITIVE SEMANTIC ASSERTION`.

SR1 candidate `9758fddafc82ebecb1ff7c8a91f863b48f4711ee` then produced this exact-head evidence:

- Full-Stack Repository Audit `33607627223` — SUCCESS;
- Real Mutation Matrix Regression `33607627357` — SUCCESS;
- M2 Multi-Channel Proposal Training `33607627283` — SUCCESS;
- Runtime `33607627279` — FAILURE only because Integrity remained red;
  - integration-tests `100175144281` — SUCCESS;
  - prototype-tests `100175144759` — SUCCESS;
  - integrity-tests `100175144669` — FAILURE.

This exact job split proves the SR1 Integration repair functionally removed its classified failure while preserving the historical failed X run. It does not relabel SR1 or X as 4/4.

### Integrity failure — current X-C1 boundary

Historical X Integrity first failure and fresh SR1 Integrity first failure are identical:

`Quality/Integrity/test_core_inventory_consistency.py::test_core_index_inventory_files_exist_without_promoting_folder_status`

`assert "INTEGRITY HOLD" in status`

Historical X result: `1 failed, 147 passed`.
Fresh SR1 result on `9758fddafc82ebecb1ff7c8a91f863b48f4711ee`: `1 failed, 147 passed`.

Classification:

`STALE PRE-CERTIFICATION STATE GUARD`.

Direct source review shows the same test contains two immediately downstream literals after the first failing assertion:

- `assert "Folder Certification" in status`
- `assert "Pending" in status`

They were not reached in the historical or fresh failed run because pytest stopped at the first assertion. They are therefore not recorded as historical failing assertions. They are classified as the same source-proven downstream stale current-state guard cohort because X's own certification record explicitly states that Quality current-state assertions transition from `Folder Certification pending` and pre-certification/open state to bounded Core closure.

The inventory list and file-existence loop preceding this cohort passed and remain durable.

## Prior-learning retrieval

1. T-C1 — DIRECTLY APPLICABLE: exact-head job split may prove one corrective failure class repaired while a distinct failure remains, without relabeling the overall candidate successful.
2. T-C2 — DIRECTLY APPLICABLE: stale current-state test contracts may be updated only when new verified state evidence exists and durable semantics remain preserved.
3. Side-repair U / SR1 — DIRECTLY APPLICABLE sequencing: preserve failure provenance, use pre-write Matrix and atomic bounded repair, then fresh exact-head verification.

## X-C1 semantic decision

X-C1 changes only the obsolete current-state tail of `test_core_inventory_consistency.py`.

The exact inventory list and loop remain unchanged.

The obsolete pre-certification cohort:

- `INTEGRITY HOLD`;
- `Folder Certification`;
- `Pending`;

is replaced by explicit current bounded closure markers that also retain anti-overpromotion:

- `CLOSED_FOR_PHASE_1`;
- `CORE CERTIFIED`;
- `CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED`;
- `CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE`.

This does not make global integrity pass. It only stops this Core-local inventory test from requiring a superseded Core folder state after X's explicit certification decision.

## Authorized material change set — exactly 3 paths

1. `Quality/Integrity/test_core_inventory_consistency.py`
   - preserve imports, expected inventory list, index-membership checks and physical-file checks;
   - replace only the three stale pre-certification current-state literals with four explicit bounded closure/anti-overpromotion assertions.
2. `Repository/P7_X_INTEGRITY_STATE_GUARD_CORRECTION_2026-09-02_X-C1.md`
   - record historical/fresh failure provenance, cohort classification, repair boundary, non-authority and verification evidence.
3. this Matrix
   - bind X-C1 candidate and verification state in the same atomic material commit.

## Forbidden

- no mutation to `Core/_FOLDER_STATUS.md`;
- no change to the inventory list or file-existence loop;
- no deletion of inventory integrity coverage;
- no SR1 Integration-test mutation in X-C1;
- no REP-016 queue-addendum mutation;
- no REP-014/REP-012/REP-013 mutation;
- no relationship/provenance/authority weakening;
- no Phase-1 closure;
- no Priority-8 start;
- no Connected Baseline closure;
- no repository-wide graph completion claim;
- no Global `BOOTED / INTEGRITY PASS` claim;
- no reinterpretation of historical failed run `33542068223` or SR1 3/4 candidate as 4/4.

## Atomicity contract

After this pre-write Matrix commit, X-C1 material candidate MUST be exactly one commit changing exactly the three authorized paths. Unexpected path expansion = `0`.

## Verification contract

`PRE-WRITE MATRIX → LIVE-PARENT RECHECK → ONE-COMMIT/THREE-PATH MATERIAL CANDIDATE → EXACT-HEAD READ-BACK/COMPARE → FOUR REQUIRED WORKFLOWS → RUNTIME JOB REVIEW → IF 4/4 SUCCESS, PREPARE DOCUMENTATION-ONLY X CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION → REDISCOVER MAIN → RECOMPUTE GLOBAL QUEUE`.

X-C1 is not complete merely because the Integrity test becomes green. All four required workflows must succeed on the same exact material candidate HEAD before X may enter documentation-only closure.

## Preserved global limits

- Phase 1 overall remains OPEN;
- repository-wide relationship graph remains not independently closed;
- Global Connected Baseline remains not independently proved;
- global integrity remains HOLD;
- Global `BOOTED / INTEGRITY PASS` is NOT CLAIMED;
- Priority 8 is not automatically started.

## Learning candidate

`WHEN A TEST COMBINES DURABLE INVENTORY CHECKS WITH TRANSIENT FOLDER-STATE ASSERTIONS, A GOVERNED STATE TRANSITION MUST UPDATE ONLY THE TRANSIENT COHORT AND LEAVE THE INVENTORY PROOF INTACT.`

No Governance promotion is authorized before exact-head verification.