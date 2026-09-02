# P7 X — Integrity State-Guard Correction X-C1

Date: 2026-09-02
Transaction: `MUT-2026-09-02-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X-C1`
Parent: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Preceding side-repair: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
State: `MATERIAL CANDIDATE PREPARED / CI PENDING / X HARD HOLD UNTIL EXACT-HEAD 4/4`
Original X candidate: `43820d41728e39edbacb5b37de4d2ffc51063dda`
SR1 candidate / X-C1 entry HEAD: `9758fddafc82ebecb1ff7c8a91f863b48f4711ee`
X-C1 pre-write Matrix HEAD: `344b3546342e36ef7a0eb00e0b18ece1d435c8ce`
Historical failed X Runtime run: `33542068223`
SR1 Runtime run: `33607627279`

## Failure provenance retained

Original X Runtime verification failed both Integration and Integrity.

The Integration failure was independently classified as a Markdown-format-sensitive test implementation defect and repaired by SR1. Fresh exact-head SR1 evidence proved:

- Full-Stack `33607627223` — SUCCESS;
- Real Mutation Matrix `33607627357` — SUCCESS;
- M2 `33607627283` — SUCCESS;
- Runtime `33607627279` — FAILURE;
  - integration-tests `100175144281` — SUCCESS;
  - prototype-tests `100175144759` — SUCCESS;
  - integrity-tests `100175144669` — FAILURE.

SR1 therefore functionally repaired the Integration defect but is not relabeled 4/4. Historical X run `33542068223` also remains failed evidence.

## Exact Integrity failure

The first meaningful Integrity failure is identical in historical X and fresh SR1 verification:

`Quality/Integrity/test_core_inventory_consistency.py::test_core_index_inventory_files_exist_without_promoting_folder_status`

`assert "INTEGRITY HOLD" in status`

Both runs report exactly `1 failed, 147 passed` at this boundary.

Classification:

`STALE PRE-CERTIFICATION STATE GUARD`.

## Downstream same-cohort source evidence

Direct current source review shows two assertions immediately after the first failing assertion:

- `assert "Folder Certification" in status`
- `assert "Pending" in status`

They are not claimed as historical runtime failures because execution stopped at `INTEGRITY HOLD`. They are source-proven downstream members of the same stale current-state guard cohort.

X's explicit certification record independently defines the governed Quality transition from:

- Priority 7 open;
- Cross-Layer Validation open;
- Folder Certification pending;
- readiness not consumed;

to the bounded closure state.

The current Core status is explicitly:

`CLOSED_FOR_PHASE_1 — CONTROL PLANE RECONCILED / BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE / CORE CERTIFIED`.

## Bounded correction

X-C1 preserves the entire durable inventory proof:

- exact expected Core names;
- every `name in index` assertion;
- every physical `is_file()` assertion.

Only the stale three-literal current-state tail is replaced with current bounded state and anti-overpromotion assertions:

- `CLOSED_FOR_PHASE_1`;
- `CORE CERTIFIED`;
- `CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED`;
- `CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE`.

This makes the test follow the governed Core state transition without converting Core certification into global repository certification.

## Non-authority preserved

X-C1 does not:

- change `Core/_FOLDER_STATUS.md`;
- change Core inventory or index membership;
- mutate SR1's Integration correction;
- change REP-012/REP-013/REP-014/REP-016;
- fabricate or promote relationships;
- close Phase 1;
- start Priority 8;
- close Connected Baseline;
- claim repository-wide graph completion;
- claim Global `BOOTED / INTEGRITY PASS`.

Global integrity remains HOLD independently of this Core-local stale assertion correction.

## Verification requirement

The X-C1 candidate is not complete until the same exact material HEAD passes all four required workflows and the Runtime job set is reviewed with integrity/prototype/integration all successful.

If exact-head 4/4 is achieved, the next action is documentation-only X closure followed by closure-head 4/4. No next Priority is selected before that closure path finishes.

## Learning candidate

`DURABLE INVENTORY PROOF AND TRANSIENT FOLDER-STATE PROOF MUST BE SEPARATED DURING A GOVERNED CERTIFICATION TRANSITION; UPDATE THE TRANSIENT COHORT WITHOUT WEAKENING INVENTORY OR GLOBAL ANTI-OVERPROMOTION.`

No Governance promotion is made by X-C1 itself.
