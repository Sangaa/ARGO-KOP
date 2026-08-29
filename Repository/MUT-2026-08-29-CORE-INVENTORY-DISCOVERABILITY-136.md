# MUT-2026-08-29 — CORE INVENTORY DISCOVERABILITY RECONCILIATION — 136

State: HOLD / PROTECTED SURFACES UNCHANGED
Role: HERMUZ via Room71
Original baseline: `8e3c0d98e81963186ab3e0a2b60cd4178b1c33af`
Scope: protected Core inventory/index/map/status synchronization only

## Current Gap

Current exact Core tree and artifact metadata establish three canonical/revalidated Core artifacts whose discoverability is inconsistent across current control surfaces:

1. `Core/CORE-000A_PLATFORM_GLOSSARY.md`
   - Document ID: `CORE-000A`
   - Status: `Official / Revalidated / Integrity Hold`
   - Classification: `Core Reference`
   - listed in `Core/_FOLDER_STATUS.md`
   - missing from REP-001 and REP-002 Core inventories.

2. `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`
   - Document ID: `CORE-012`
   - Status: `Canonical / Core / Mandatory`
   - Canonical: Yes
   - present in REP-001
   - missing from REP-002 and from the current Core status baseline list.

3. `Core/ARGO_KERNEL.md`
   - Document ID: `CORE-KERNEL`
   - Status: `Revalidated / Integrity Hold`
   - Category: `Core / Runtime Contract`
   - Canonical: Yes
   - listed in `Core/_FOLDER_STATUS.md`
   - missing from REP-001 and REP-002 Core inventories.

## Intended Mutation

A future protected same-change-set mutation must:

- preserve REP-001 Version `1.11.3` unless separate version authority changes it;
- preserve REP-002 Version `1.7.4` unless separate version authority changes it;
- preserve Core status Version `1.3.1` unless separate version authority changes it;
- add CORE-000A and ARGO_KERNEL to REP-001 Core inventory;
- add CORE-000A, CORE-012 and ARGO_KERNEL to REP-002 Core map;
- add CORE-012 to the current Core status baseline list;
- preserve `INTEGRITY HOLD`, cross-layer validation and certification holds;
- include a direct regression in the same final changed set.

## Execution Deviation / Hold Reason

During assembly, tool-selection discipline became unstable before any protected surface was changed:

1. `Quality/Integration/test_core_inventory_discoverability.py` was accidentally staged in a standalone commit instead of the required final same-change-set and was immediately removed.
2. Two non-authoritative temporary/assembly marker artifacts were accidentally created and immediately removed before protected mutation.
3. A separate provenance record preserves the staging-deviation history.

No REP-001, REP-002, Core status, canonical Core artifact, or authority surface was modified by those deviations.

After the repeated tool-selection pattern, HERMUZ stopped the protected mutation under fail-closed discipline rather than risk a partial or malformed control-plane rewrite.

Root classification:

`EXECUTION_TOOL_SELECTION_INSTABILITY / PROTECTED_TRANSACTION ABORTED BEFORE PROTECTED WRITE`

## Learning

`PREWRITE AUTHORIZATION != OBLIGATION TO CONTINUE AFTER EXECUTION CONTROL DEGRADES`

`FAIL-CLOSED BEFORE PROTECTED WRITE > FORCING A PARTIAL CONTROL-PLANE REPAIR`

Repeated low-level tool-selection deviations are themselves sufficient evidence to halt a protected multi-file transaction, even when the semantic repair is well understood.

## Non-Claims

This transaction does NOT:
- close Core discoverability;
- certify Core cross-layer relationships;
- prove runtime reachability of ARGO_KERNEL;
- promote any Knowledge artifact;
- close Connected Baseline globally;
- claim CI for a protected mutation that never occurred.

## Resume Requirements

Before resuming 136:
1. re-enter current `main` and verify no concurrent Core repair superseded this transaction;
2. re-read complete current REP-001, REP-002 and Core status blobs;
3. construct all replacement blobs before any protected write;
4. commit finalized Matrix + REP-001 + REP-002 + Core status + regression in one atomic Git tree/commit;
5. read back exact surfaces;
6. require exact-head Runtime/Integration, Full-Stack, M2, and applicable Mutation Matrix Regression success.

`INDEX/MAP DISCOVERABILITY != CROSS-LAYER CERTIFICATION`
