# MUT-2026-08-29 — INTERFACES FOLDER STATUS RECONCILIATION — 170

Status: PREWRITE / NOT CLOSED
Date: 2026-08-29
Baseline SHA: `2ccdbebeae78774a1ff2b30b9d4fc7cc86877cec`
Target: `Interfaces/_FOLDER_STATUS.md`
Regression: `Quality/Integrity/test_interfaces_folder_status_reconciliation.py`

## Trigger

Current exact Git-tree enumeration of `Interfaces/` returned `truncated:false` with 12 tracked files and no subdirectories, while the current folder status inventories only five files.

The same tree contains both `INTF-006_ENVIRONMENT_SENSING.md` and `INTF-006_WEB.md`. Direct content review establishes that the former declares `Document ID: INTF-006`, `Canonical: Yes`, `Status: Proposed / Integrity Hold`, while the latter declares internal legacy ID `INT-006`, `Legacy / Noncanonical / Integrity Hold`, `Canonical: No`, and explicitly denies ownership of active `INTF-006`.

## Intended bounded mutation

1. Reconcile the folder status to the exact 12-file physical inventory.
2. Separate physical presence from authority/canonical promotion.
3. Record the `INTF-006` filename duplication as legacy provenance rather than active authority collision.
4. Preserve `INTEGRITY HOLD` and all provider-authentication / connector-runtime / cross-layer holds.
5. Add a cwd-independent regression that verifies the bounded status claims.

## Non-claims

- No provider authentication capability is established.
- No external connector implementation is certified.
- No repository-wide Connected Baseline is closed.
- No legacy artifact is renamed, archived, promoted or deleted.
- No Interface document is promoted merely because it appears in the physical inventory.

## Closure gate

This mutation is not closed until the target status and regression are committed, read back, and applicable exact-head CI is observed.
