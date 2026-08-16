# EJR-183 — Runtime Control-Plane Inventory Drift Learning

Date: 2026-08-16

## Trigger
Current-main reconciliation found that the physical Runtime inventory and Runtime folder status used the current `RUN-011..015` artifact names, while both `REP-001_MASTER_INDEX.md` and `REP-002_REPOSITORY_MAP.md` still referenced obsolete Runtime candidate filenames.

## Evidence
Current physical Runtime candidates:

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`

Previous Control-Plane references used obsolete names such as `RUN-011_COGNITIVE_EXECUTION_TARGET.md` and corresponding stale paths for RUN-012..015.

`Runtime/_FOLDER_STATUS.md` and the current artifacts were already aligned; the drift existed specifically in the master index and physical storage map.

## Root Cause
The Runtime candidate artifacts were evolved/rebuilt while the repository Control Plane retained older inventory path declarations. This is a **Control-Plane inventory drift**, distinct from document identity drift or source artifact defects.

## Correction
Updated both:

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

with the current physical Runtime candidate paths and added bounded rules preventing historical candidate names from remaining active inventory.

Added `Quality/Integrity/test_control_plane_runtime_inventory_alignment.py` to compare physical Runtime candidates against both Control-Plane surfaces and reject the known stale paths.

## Verification
- Runtime Prototype / Integration / Integrity run #499: PASS.
- Full-Stack Repository Audit run #712: PASS.

## Learning Rule
**Canonical inventory is multi-surface: physical artifact paths, domain-local status, master index and storage map must be reconciled as a single identity/path chain. A current artifact can be correct while the Control Plane remains stale. Historical candidate paths must be treated as migration evidence, not active inventory.**

This defect class is distinct from filename/document-ID drift and domain-local inventory drift.

## Reuse
Apply to Runtime, Interfaces, Models, Services, Architecture, Plugins, Memory subdomains and any future rebuilt domain whose physical artifacts evolve while control-plane inventories persist.
