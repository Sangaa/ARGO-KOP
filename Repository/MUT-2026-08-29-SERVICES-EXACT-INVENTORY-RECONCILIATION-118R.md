# MUT-2026-08-29-SERVICES-EXACT-INVENTORY-RECONCILIATION-118R

Date: 2026-08-29
Parent transaction: `R71-20260829-SERVICES-INVENTORY-118`
Prewrite baseline: `main@6b3d1e25526f0af400227a288710576e2a7efaae`
Protected-change parent: `main@9e0f17dbe3d1a4bd5b7a54b98344ca05fbd4fc8e`
Status: `FINALIZED / CI-FAILURE REPAIR / SAME-CHANGE-SET / CI PENDING`

## Exact-head failure evidence

At `6b3d1e25526f0af400227a288710576e2a7efaae`:
- Full-Stack run `33258323139` — SUCCESS;
- M2 run `33258323157` — SUCCESS;
- Runtime/Integration run `33258323120` — FAILURE.

### Failure A — observation-surface confusion

The new regression used `Path('Services').iterdir()` and asserted every runtime working-directory entry was a file. During pytest, generated `__pycache__/` directories can appear. That surface is not the committed Git inventory proven by Git tree `94088ae4ae54699ae267a32dda033463591573c8` (`truncated:false`).

Repair: regression now measures tracked repository paths using `git ls-files Services` and requires the exact 20-file set.

`COMMITTED GIT TREE ≠ TEST-RUNTIME WORKING DIRECTORY`.

### Failure B — stable semantic wording lost

Existing integrity contracts correctly require:
- `` `SRV-001` through `SRV-010` `` for the logical active service catalog;
- `Physical existence of a service artifact does not prove implementation or runtime execution.` for the no-promotion boundary.

Both meanings remained true but were reworded by 118. Repair restores both exact stable clauses while retaining the new physical-tree evidence.

## Repair changed set

| Change | Target | Action | Result |
|---|---|---|---|
| R1 | `Services/_FOLDER_STATUS.md` | UPDATE | restore exact stable catalog and no-proof clauses; preserve exact 20-file tracked inventory and Integrity Hold |
| R2 | `Quality/Integration/test_services_exact_inventory.py` | UPDATE | inspect tracked Git paths, not generated working-directory entries |
| R3 | this Matrix | UPDATE | finalized with R1/R2 in same Git tree/commit |

No existing integrity test is weakened. No service, connector, Runtime, provider-authentication, REP-001/002 or relationship authority is widened.

## Verification gate

Required exact-head CI:
- ARGO Runtime Prototype and Integration Tests;
- Full-Stack Repository Audit;
- M2 Multi-Channel Proposal Training;
- Real Mutation Matrix Regression if emitted.

Until green CI, transaction 118 remains open.

## Learning

A robust domain-inventory test must keep three evidence surfaces separate:

`LOGICAL CATALOG / TRACKED GIT TREE / RUNTIME WORKING DIRECTORY`.

They may overlap, but they are not interchangeable.
