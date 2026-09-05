# Priority 12 — Models Exact Inventory / Allocation — Transaction A Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-INVENTORY-ALLOCATION-A`

Priority: `12 — Models`

State: `PRE-WRITE / MATERIAL NOT YET APPLIED`

Entry HEAD: `15d94d97e848060aafabe7faa3c369f852b62c35`

## Entry authority

Transaction S and bounded Priority 11 are `CLOSED / VERIFIED / RESUME-SAFE` on exact live HEAD `15d94d97e848060aafabe7faa3c369f852b62c35`, with all four required workflow families successful on that exact SHA.

`Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` identifies Priority 12 as `Models`, with entry authorities `MOD-001/002/003/004/011`. Direct current-main inspection confirms Models remains `INTEGRITY HOLD / STAGED RECONSTRUCTION`; therefore Priority 12 has a real open bounded scope and is not started merely from numbering.

## Observed inventory contradiction

Direct `Models/` contents enumeration on the entry HEAD establishes exactly seven top-level tracked files:

1. `Models/MOD-001_KNOWLEDGE_MODEL.md`
2. `Models/MOD-002_ENTITY_MODEL.md`
3. `Models/MOD-003_DOCUMENT_MODEL.md`
4. `Models/MOD-004_MEMORY_MODEL.md`
5. `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
6. `Models/README.md`
7. `Models/_FOLDER_STATUS.md`

Canonical sorted-path SHA-256: `cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498`.

Current control-plane drift:

- REP-013 lists only README, MOD-001 and MOD-011 and explicitly marks that list partial.
- REP-002 maps MOD-001/002/003/004/011 and `_FOLDER_STATUS.md` but omits `Models/README.md` from the physical map.
- REP-012 has no directly located Models path-level exact allocation set in the current retrieved registry content.
- REP-001 already indexes the five active model artifacts plus `_FOLDER_STATUS.md`; physical inventory reconciliation must not add README merely to manufacture active semantic authority.

## Metadata boundary

Direct current-content inspection establishes:

- MOD-001 — `Canonical: Yes`, `Integrity Hold / Relationship-Revalidated`.
- MOD-002 — `Canonical: Yes`, `Approved / Revalidation Required`.
- MOD-003 — `Canonical: Yes`, `Approved / Revalidation Required`.
- MOD-004 — `Canonical: Yes`, `Approved / Revalidation Required`.
- MOD-011 — `Canonical: Yes`, `Proposed / Future-Ready / Revalidated`; inspected semantic revalidation does not promote its maturity or Models-domain integrity.
- README — domain container/navigation evidence at `INTEGRITY HOLD / STAGED RECONSTRUCTION`.
- `_FOLDER_STATUS.md` — status evidence, not a completion certificate.

`PHYSICAL ALLOCATION != SEMANTIC PROMOTION != RELATIONSHIP VALIDATION != PARTITION CLOSURE`.

## Authorized material set

The material commit must contain this Matrix in the same changed-file set as every protected mutation.

| Change ID | Target | Action | Purpose |
| --- | --- | --- | --- |
| P12-A-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | synchronize exact seven-path Models physical map without semantic promotion |
| P12-A-02 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | bind exact Models allocation manifest/digest and `NONE_BY_ALLOCATION` authority effect |
| P12-A-03 | `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv` | CREATE | one exact non-authoritative allocation row per Models path |
| P12-A-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | replace partial Models representation with exact seven-path physical inventory |
| P12-A-05 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | synchronize P11 closure and P12 exact-inventory entry state from newer verified evidence |
| P12-A-06 | `Models/_FOLDER_STATUS.md` | UPDATE | record exact current inventory/digest and bounded Priority-12 entry without closing Models |
| P12-A-07 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | CREATE | guard exact tree/digest/allocation/non-promotion/queue boundaries |
| P12-A-08 | this Matrix | UPDATE | bind material/read-back/CI evidence in same change set |

No other path is authorized.

## Deliberate non-change

`Repository/REP-001_MASTER_INDEX.md` is not authorized for this transaction because current direct evidence already indexes the five active Models artifacts plus `_FOLDER_STATUS.md`. `Models/README.md` is physical/container evidence, and adding it to REP-001 merely to match the physical tree would improperly conflate physical allocation with active semantic authority.

## Required allocation semantics

Every exact Models path is `ALLOCATED` to domain `Models` with authority effect `NONE_BY_ALLOCATION`.

Suggested artifact classes are bounded record types only:

- MOD-001/002/003/004/011: `MODEL_ARTIFACT_EXISTING_AUTHORITY_UNCHANGED`
- README: `DOMAIN_CONTAINER_EVIDENCE`
- `_FOLDER_STATUS.md`: `STATUS_EVIDENCE`

These labels do not create or upgrade canonical authority.

## Non-claims

This transaction does not:

- close Priority 12 or Models;
- certify Models ↔ Knowledge/Memory/Runtime/Services/Interfaces/AI/Repository/Release relationships;
- reconstruct missing historical MOD-005..010 declarations;
- promote MOD-011 beyond its current Proposed / Future-Ready state;
- resolve duplicate/overlapping semantic definitions;
- establish Runtime consumer execution;
- establish provider authenticity, external trust anchors, Global Connected Baseline or Global Integrity;
- promote HORUS/Governance/learning material.

## Material protocol

`PRE-WRITE MATRIX → EXACT INVENTORY MATERIAL + FINALIZED MATRIX IN SAME CHANGE SET → IMMUTABLE READ-BACK → PARENT→HEAD COMPARE → EXACT-HEAD CI`.

Required exact-head workflow families after material application:

1. Full-Stack Repository Audit
2. ARGO Runtime Prototype and Integration Tests
3. M2 Multi-Channel Proposal Training
4. Real Mutation Matrix Regression

Transaction A may close only if the exact material HEAD passes the required validation and no new contradictory Models-specific evidence appears.
