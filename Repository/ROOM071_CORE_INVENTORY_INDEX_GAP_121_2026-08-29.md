# ROOM 71 — CORE INVENTORY / INDEX GAP 121

Date: 2026-08-29
Role: HERMUZ
Lease: `R71-20260829-CORE-INVENTORY-INDEX-121`
Baseline SHA: `9435df15ccdd62afdfd2cf45a1ea969fa3decb38`
State: CLOSED_AS_BOUNDED_DIAGNOSIS / REPAIR_OPEN

## Evidence

Direct current Core Git tree `d61b7af1617c54b0945d94d7a0f4ad0e4ccf985f` returned `truncated:false` and establishes the exact top-level physical Core inventory.

Three current canonical Core artifacts expose index/map drift:

1. `Core/CORE-000A_PLATFORM_GLOSSARY.md`
   - Document ID `CORE-000A`
   - Status `Official / Revalidated / Integrity Hold`
   - Classification `Core Reference`
   - purpose explicitly defines canonical repository terminology.
   - listed by `Core/_FOLDER_STATUS.md` as a known canonical Core artifact.
   - absent from the inspected active Core list in REP-001 and REP-002.

2. `Core/ARGO_KERNEL.md`
   - Document ID `CORE-KERNEL`
   - Status `Revalidated / Integrity Hold`
   - Category `Core / Runtime Contract`
   - `Canonical Yes`
   - listed by `Core/_FOLDER_STATUS.md` as independently revalidated.
   - absent from the inspected active Core list in REP-001 and REP-002.

3. `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`
   - Document ID `CORE-012`
   - Status `Canonical / Core / Mandatory`
   - `Canonical Yes`
   - present in REP-001 active Core inventory.
   - absent from the inspected REP-002 Core storage map and absent from the older `Current Core Baseline` list in `Core/_FOLDER_STATUS.md`.

## Classification

`CORE_PHYSICAL_INVENTORY = EXACT_TOP_LEVEL_ENUMERATION_VERIFIED`

`CORE-000A = CANONICAL_PHYSICAL_ARTIFACT / REP001_DISCOVERABILITY_GAP / REP002_MAPPING_GAP`

`CORE-KERNEL = CANONICAL_PHYSICAL_ARTIFACT / REP001_DISCOVERABILITY_GAP / REP002_MAPPING_GAP`

`CORE-012 = REP001_DISCOVERABLE / REP002_MAPPING_GAP / CORE_STATUS_BASELINE_LAG`

## Why repair is not performed in this transaction

REP-001 and REP-002 are serialized protected control surfaces. The current connector read returned bounded sections rather than a safely reconstructed complete document body suitable for whole-file replacement. Rewriting either from partial retrieval would violate content-preservation discipline.

Therefore this transaction closes the diagnosis and exact affected set, but deliberately keeps the protected repair open until a full-content-safe atomic transaction can preserve both documents and its Mutation Matrix.

## Closure boundary

CLOSED:
- exact Core top-level physical inventory subgate;
- exact current affected canonical artifact set for this index/map discrepancy;
- authority classification of the three affected artifacts.

OPEN:
- REP-001 registration of CORE-000A and CORE-KERNEL;
- REP-002 mapping of CORE-000A, CORE-KERNEL and CORE-012;
- Core/_FOLDER_STATUS baseline synchronization for CORE-012;
- Core cross-layer certification.

## Learning

`CANONICAL IN DOMAIN STATUS + PHYSICAL PRESENCE != INDEX/MAP DISCOVERABILITY`.

A protected index repair must not be attempted from a truncated or partial control-file retrieval merely to close a queue item.
