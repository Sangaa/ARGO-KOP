# Priority 12 — Models Exact Inventory / Allocation — Transaction A Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-INVENTORY-ALLOCATION-A`

Priority: `12 — Models`

State: `PARTIAL MATERIAL APPLIED / REP-002 SYNC COMPLETE / REP-012+013+016 SYNC PENDING`

Entry HEAD: `15d94d97e848060aafabe7faa3c369f852b62c35`
Pre-write Matrix HEAD: `109b58043517aeb6c14d204bfe61cee41066c415`
Material Unit 1 HEAD: `bec6f61072607e77aab753fe2eace5eb027df491`

## Entry authority

Priority 11 is `CLOSED / VERIFIED / RESUME-SAFE` on exact entry HEAD. REP-016 identifies Priority 12 as Models, and direct Models evidence establishes a real open staged-reconstruction scope.

## Exact Models physical inventory

Direct entry-HEAD enumeration establishes exactly seven top-level tracked paths:

1. `Models/MOD-001_KNOWLEDGE_MODEL.md`
2. `Models/MOD-002_ENTITY_MODEL.md`
3. `Models/MOD-003_DOCUMENT_MODEL.md`
4. `Models/MOD-004_MEMORY_MODEL.md`
5. `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
6. `Models/README.md`
7. `Models/_FOLDER_STATUS.md`

Sorted-path SHA-256:
`cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498`

## Metadata / authority boundary

- MOD-001: Canonical Yes / Integrity Hold / Relationship-Revalidated.
- MOD-002: Canonical Yes / Approved / Revalidation Required.
- MOD-003: Canonical Yes / Approved / Revalidation Required.
- MOD-004: Canonical Yes / Approved / Revalidation Required.
- MOD-011: Canonical Yes / Proposed / Future-Ready / Revalidated.
- README: domain-container evidence.
- `_FOLDER_STATUS.md`: status evidence.

`PHYSICAL ALLOCATION != SEMANTIC PROMOTION != RELATIONSHIP VALIDATION != PARTITION CLOSURE`.

## Authorized material set and progress

| Change ID | Target | Action | Current state |
| --- | --- | --- | --- |
| P12-A-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | APPLIED IN MATERIAL UNIT 2 |
| P12-A-02 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | SYNC PENDING |
| P12-A-03 | `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | SYNC PENDING |
| P12-A-05 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | SYNC PENDING |
| P12-A-06 | `Models/_FOLDER_STATUS.md` | UPDATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-07 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-08 | this Matrix | UPDATE | SAME-CHANGE-SET BINDING ON EACH PROTECTED UNIT |

No other path is authorized.

## Material Unit 1 evidence

Material Unit 1 established the exact path-level manifest, Models status inventory/digest/open boundary, executable integrity guard and this Matrix in the same changed-file set.

Exact-head regression evidence on `bec6f61072607e77aab753fe2eace5eb027df491`:

- Full-Stack Repository Audit — SUCCESS; run `33949936759`.
- ARGO Runtime Prototype and Integration Tests — SUCCESS; run `33949936748`.
- M2 Multi-Channel Proposal Training — SUCCESS; run `33949936765`.
- Real Mutation Matrix Regression — SUCCESS; run `33949936764`.

These successes are regression evidence only; Transaction A remains open because control-plane synchronization is incomplete.

## Material Unit 2 — REP-002 exact physical map synchronization

REP-002 was retrieved completely from the current Unit-1 HEAD before replacement. Material Unit 2 changes only REP-002 plus this Matrix.

The Models map now contains exactly the seven current top-level paths, adds `Models/README.md` as domain-container/navigation evidence, records digest `cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498`, and explicitly preserves:

`EXACT PHYSICAL INVENTORY != SEMANTIC PROMOTION != RELATIONSHIP VALIDATION != MODELS CLOSURE`.

REP-001 remains deliberately unchanged: current active semantic indexing already covers the five MOD artifacts plus `_FOLDER_STATUS.md`; README physical mapping does not grant active semantic authority.

## Remaining control-plane drift

- REP-012 registry synchronization — pending.
- REP-013 exact content-tree synchronization — pending.
- REP-016 P11-closure/P12-entry queue synchronization — pending.

## Non-claims

Transaction A and Priority 12 remain open. No Models relationship closure, missing historical model reconstruction, MOD-011 maturity promotion, Runtime execution claim, provider authenticity, external trust anchor, Global Connected Baseline, Global Integrity, HORUS promotion or Governance/learning promotion is claimed.

## Next gate

1. Commit/read-back/compare Material Unit 2.
2. Retrieve complete current REP-012 before replacement and bind manifest/digest/`NONE_BY_ALLOCATION` with this Matrix in the same changed-file set.
3. Then repeat the same preservation discipline for REP-013 and REP-016.
4. Only after all four control surfaces are synchronized may the complete Transaction-A material HEAD enter closure-grade exact-head CI.
