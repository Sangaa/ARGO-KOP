# Priority 7 — Core REP-001 Control-Plane Reconciliation A

Date: 2026-09-01
State: `P7 PROGRESS / REP-001 CORE DISCOVERABILITY RECONCILED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-REP001-RECONCILIATION-A`

## Finding
P336 established the exact current Core inventory and explicitly recorded that `Core/CORE-000A_PLATFORM_GLOSSARY.md` was missing from the active REP-001 Core list. Direct current-content review confirms CORE-000A is an official/revalidated Core reference. The legacy `Core/CORE-000_PLATFORM_IDENTITY.md` remains noncanonical/superseded and is not eligible for active REP-001 promotion.

## Repair
REP-001 is updated from v1.11.3 to v1.11.4 to register `Core/CORE-000A_PLATFORM_GLOSSARY.md` in the active Core Layer. A direct integration regression binds that discoverability result while explicitly preventing promotion of the legacy CORE-000 identity artifact.

## Manifest-scope verification
The current executable control-plane manifest was read directly before functional mutation. Its rows cover REP-011, REP-012, REP-013, REP-014, REP-015, REP-016 and REP-020; REP-001 is not in that manifest scope. Therefore no manifest mutation is required or authorized for this REP-001 version change. An off-ref candidate that would have expanded the manifest to include REP-001 was rejected before mainline mutation.

## Boundary
This closes only the REP-001 Core discoverability drift for CORE-000A. Priority 7 remains OPEN. REP-002 still requires bounded reconciliation for `CORE-000A` and `CORE-012`. GOV-006 disposition, Core dependency/consumer validation, relationship-registry reconciliation and explicit Core certification remain open. Phase 1 and Global Connected Baseline remain open; no global integrity PASS is claimed.
