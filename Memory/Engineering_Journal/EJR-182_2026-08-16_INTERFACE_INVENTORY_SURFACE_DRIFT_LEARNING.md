# EJR-182 — Interface Inventory Surface Drift Learning

Date: 2026-08-16

## Trigger
Current-main review of Interfaces found `INTF-010_INTEGRATIONS.md` as a canonical artifact while `Interfaces/_FOLDER_STATUS.md` omitted it from the Verified Directory Inventory.

## Evidence
- `Interfaces/INTF-010_INTEGRATIONS.md` is present on current `main`, has Document ID `INTF-010`, Canonical `Yes`, and is validated/revalidated with Integrity Hold.
- `Repository/REP-001_MASTER_INDEX.md` already indexes `Interfaces/INTF-010_INTEGRATIONS.md` as a directly verified current artifact.
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md` explicitly references `INTF-010_INTEGRATIONS.md` as the provider-neutral connector boundary.
- The Interfaces Folder Status inventory previously listed `INTF-001`, `INTF-004`, and `INTF-006`, but not `INTF-010`.

## Root Cause
The canonical artifact and master index were current, while a domain-local inventory surface lagged behind. This was an **inventory-surface drift**, not a source identity defect.

## Correction
Updated `Interfaces/_FOLDER_STATUS.md` to include `INTF-010` with its current identity/status and added an explicit rule that any directly verified canonical Interface artifact represented in the active master index must be reflected in the folder inventory or explicitly dispositioned.

## Verification
- Runtime Prototype / Integration / Integrity run #494: PASS.
- Full-Stack Repository Audit run #707: PASS.

## Learning Rule
**Inventory reconciliation is a multi-surface problem. Canonical artifact correctness does not guarantee folder-status correctness. When an artifact is canonical in the master index and consumed by current contracts, every authoritative domain-local inventory surface must either include it or explicitly explain its exclusion.**

This is distinct from filename/document-ID drift: an artifact may be internally correct while its inventory representation is stale or incomplete.

## Reuse
Apply to Core, Architecture, Interfaces, Models, Services, Runtime and other domains with independent folder inventories, master indexes or registry surfaces.
