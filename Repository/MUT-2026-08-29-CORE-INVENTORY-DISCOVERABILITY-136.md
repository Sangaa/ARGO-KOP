# MUT-2026-08-29 — CORE INVENTORY DISCOVERABILITY RECONCILIATION — 136

State: PREWRITE / NOT CLOSED
Role: HERMUZ via Room71
Baseline: `8e3c0d98e81963186ab3e0a2b60cd4178b1c33af`
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

Protected same-change-set mutation will:

- preserve REP-001 Version `1.11.3`;
- preserve REP-002 Version `1.7.4`;
- preserve Core status Version `1.3.1`;
- add CORE-000A and ARGO_KERNEL to REP-001 Core inventory;
- add CORE-000A, CORE-012 and ARGO_KERNEL to REP-002 Core map;
- add CORE-012 to the current Core status baseline list;
- preserve `INTEGRITY HOLD`, cross-layer validation and certification holds;
- add a direct regression asserting synchronized discoverability without treating index membership as promotion.

## Non-Claims

This transaction does NOT:
- certify Core cross-layer relationships;
- prove runtime reachability of ARGO_KERNEL;
- promote any Knowledge artifact;
- close Connected Baseline globally;
- change semantic/version authority merely because inventory is synchronized.

## Required Verification

1. Finalized Matrix + REP-001 + REP-002 + Core status + regression in one Git tree/commit.
2. Read-back exact changed surfaces.
3. Exact-head Runtime/Integration, Full-Stack and M2 CI.
4. Real Mutation Matrix Regression if triggered/applicable.
5. Any failure = HOLD and root-cause repair; do not weaken valid tests.

`INDEX/MAP DISCOVERABILITY != CROSS-LAYER CERTIFICATION`
