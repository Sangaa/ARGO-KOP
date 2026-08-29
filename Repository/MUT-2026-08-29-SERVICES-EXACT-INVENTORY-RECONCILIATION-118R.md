# MUT-2026-08-29-SERVICES-EXACT-INVENTORY-RECONCILIATION-118R

Date: 2026-08-29
Parent transaction: `R71-20260829-SERVICES-INVENTORY-118`
Baseline: `main@6b3d1e25526f0af400227a288710576e2a7efaae`
Status: `PREWRITE / CI-FAILURE REPAIR / NOT CLOSED`

## Exact-head failure evidence

At `6b3d1e25526f0af400227a288710576e2a7efaae`:
- Full-Stack run `33258323139` — SUCCESS;
- M2 run `33258323157` — SUCCESS;
- Runtime/Integration run `33258323120` — FAILURE.

Two jobs failed for two distinct reasons.

### Integration failure — test observation surface error

`Quality/Integration/test_services_exact_inventory.py::test_services_exact_current_physical_inventory` asserted that every entry returned by `Path('Services').iterdir()` was a file.

During pytest execution Python creates runtime artifacts such as `Services/__pycache__/`, so the working directory is not equivalent to the committed Git tree. The authoritative enumeration evidence was the non-truncated Git tree, not a mutated test-process filesystem.

Classification:
`TEST-MODEL FAILURE / OBSERVATION-SURFACE CONFUSION`.

Correct repair:
use tracked Git paths (`git ls-files Services`) in the regression, so generated/untracked runtime artifacts cannot falsify repository inventory.

Rule:
`COMMITTED GIT TREE ≠ TEST-RUNTIME WORKING DIRECTORY`.

### Integrity failure — stable semantic contract lost

Existing integrity tests require two still-true clauses in `Services/_FOLDER_STATUS.md`:

- `` `SRV-001` through `SRV-010` `` — the logical SRV catalog remains exactly SRV-001..010;
- `Physical existence of a service artifact does not prove implementation or runtime execution.` — the no-promotion boundary remains valid.

Transaction 118 preserved their meaning but rewrote the wording. That broke tested compatibility without evidence that the old clauses were obsolete.

Classification:
`CONTENT-PRESENTATION REGRESSION / STABLE CONTRACT MUST BE PRESERVED`.

## Authorized repair

1. `Services/_FOLDER_STATUS.md`
   - preserve the exact stable SRV catalog phrase;
   - preserve the exact physical-existence non-proof sentence;
   - retain the new exact 20-file physical inventory and Integrity Hold.
2. `Quality/Integration/test_services_exact_inventory.py`
   - replace runtime filesystem enumeration with tracked Git-path enumeration;
   - continue checking exact 20-file set and status boundary.
3. this Matrix
   - finalize in same protected change set as 1–2.

No service/connector/runtime/provider authority is widened. No REP-001/002 mutation. No existing integrity test is weakened.

## Verification

`PREWRITE → STATUS + CORRECTED TEST + FINALIZED MATRIX SAME CHANGE SET → READ-BACK → EXACT-HEAD CI → CLOSE OR HOLD`.

## Learning

Two independent distinctions emerged:

`LOGICAL SERVICE CATALOG ≠ COMPLETE PHYSICAL SERVICE TREE`

and

`COMMITTED GIT TREE ≠ TEST-RUNTIME WORKING DIRECTORY`.

A correct inventory control must preserve both distinctions at once.
