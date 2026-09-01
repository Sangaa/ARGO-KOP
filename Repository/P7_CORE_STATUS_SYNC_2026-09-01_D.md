# Priority 7 — Core Status Synchronization D

Date: 2026-09-01
State: `P7 PROGRESS / STATUS SURFACE SYNCHRONIZED / CI RECOVERED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-STATUS-SYNC-D`

## Finding

`Core/_FOLDER_STATUS.md` lagged behind current Priority-7 repository reality: it still described REP-001, REP-002 and GOV-006 reconciliation as open even though those bounded transactions are now closed and execution-verified.

## Repair

The status surface is synchronized to distinguish:

- closed local/control-plane factual reconciliation;
- still-open Core dependency/consumer validation;
- REP-014 reconciliation where evidence requires;
- explicit Core certification review.

## CI hard-hold and root cause

Initial candidate HEAD `49bd59b85ec7a7eae6da2dab1c65ceb509d24c55` triggered Runtime/Integration run `33476015492` and failed in `integration-tests` job `99755316869`, step `Run integration quality suite`.

Source-level diagnosis found `Quality/Integration/test_core_local_inventory_reconciliation.py` still required the transient P336 status prefix `LOCAL INVENTORY RECONCILED / CROSS-LAYER VALIDATION OPEN` even though that regression's declared scope is local physical inventory synchronization only. Transaction D validly advanced the broader status prefix to `CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN` while preserving exact local inventory, cross-layer hold and pending certification.

Root-cause classification: `STALE REGRESSION / SEMANTIC-BOUNDARY OVERREACH`.

Prior learning: `EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md` — `TRANSFERABLE`. The reused rule is that regression assertions must target the semantic authority boundary they protect rather than freeze transient or historical wording outside that boundary.

## Minimal recovery

The mutation matrix was expanded before touching the pre-existing P336 regression. The repair changed only its status-boundary assertion:

- exact 18-file local inventory remains required;
- `CORE-012` remains required;
- `CROSS-LAYER VALIDATION OPEN` remains required;
- Folder Certification remains pending;
- legacy CORE-000 noncanonical provenance checks remain unchanged.

Recovery HEAD: `46f63940775ea719d402104d052642e825f9930a`.

## Recovery verification

Exact recovery HEAD `46f63940775ea719d402104d052642e825f9930a`:

- Runtime/Integration run `33478793256` = `SUCCESS`; prototype, integrity and integration jobs all succeeded, including `Run integration quality suite`;
- Full-Stack run `33478793257` = `SUCCESS`;
- M2 run `33478793244` = `SUCCESS`.

Matrix-expansion HEAD `3697fa44d9b2f0922cb9f7904b0bf200447d2248`:

- Real Mutation Matrix Regression run `33478763215` = `SUCCESS`.

## Boundary

This is a status/control-surface synchronization and regression-boundary repair only. It does not create, strengthen or certify any Core relationship and does not close Priority 7, Phase 1 or Global Connected Baseline.

## Next legal engineering target

After this transaction's documentation/closure HEAD is itself revalidated, continue with:

`Material Core authority dependency/consumer validation → REP-014 reconciliation where required → Core certification review`.
