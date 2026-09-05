# Priority 12 — Models Exact Inventory / Allocation — Transaction A Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-INVENTORY-ALLOCATION-A`

Priority: `12 — Models`

State: `PARTIAL MATERIAL APPLIED / REP-002+012 SYNC COMPLETE / REP-013+016 SYNC PENDING`

Entry HEAD: `15d94d97e848060aafabe7faa3c369f852b62c35`
Pre-write Matrix HEAD: `109b58043517aeb6c14d204bfe61cee41066c415`
Material Unit 1 HEAD: `bec6f61072607e77aab753fe2eace5eb027df491`
Material Unit 2 HEAD: `1b98df1cbb1f57a681924827191bf72bc05b955a`

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

`PHYSICAL ALLOCATION != SEMANTIC PROMOTION != RELATIONSHIP VALIDATION != PARTITION CLOSURE`.

## Authorized material set and progress

| Change ID | Target | Action | Current state |
| --- | --- | --- | --- |
| P12-A-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | APPLIED IN MATERIAL UNIT 2 |
| P12-A-02 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | APPLIED IN MATERIAL UNIT 3 |
| P12-A-03 | `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | SYNC PENDING |
| P12-A-05 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | SYNC PENDING |
| P12-A-06 | `Models/_FOLDER_STATUS.md` | UPDATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-07 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-08 | this Matrix | UPDATE | SAME-CHANGE-SET BINDING ON EACH PROTECTED UNIT |

No other path is authorized.

## Material Unit 1 evidence

Material Unit 1 established the exact manifest, Models status inventory/digest/open boundary, executable integrity guard and this Matrix in the same changed-file set.

Exact-head regression evidence on `bec6f61072607e77aab753fe2eace5eb027df491`:

- Full-Stack Repository Audit — SUCCESS; run `33949936759`.
- ARGO Runtime Prototype and Integration Tests — SUCCESS; run `33949936748`.
- M2 Multi-Channel Proposal Training — SUCCESS; run `33949936765`.
- Real Mutation Matrix Regression — SUCCESS; run `33949936764`.

These successes are regression evidence only; Transaction A remains open because control-plane synchronization is incomplete.

## Material Unit 2 evidence

REP-002 was completely retrieved before replacement. It now maps the exact seven-path Models tree, including README as domain-container/navigation evidence, binds digest `cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498`, and preserves the no-promotion/no-closure boundary. The Unit-2 candidate compare showed only REP-002 plus this Matrix changed.

## Material Unit 3 — REP-012 allocation binding

REP-012 was completely retrieved in bounded ranges from Unit-2 HEAD before replacement. Prior historical sections remain preserved. A current append-only P12 Transaction-A section binds:

- exact manifest `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv`;
- exact path count `7`;
- digest `cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498`;
- allocation effect `NONE_BY_ALLOCATION`;
- no semantic promotion, relationship certification, missing-history reconstruction or P12 closure.

## Remaining control-plane drift

- REP-013 exact content-tree synchronization — pending.
- REP-016 P11-closure/P12-entry queue synchronization — pending.

REP-001 remains deliberately unchanged because physical README/status evidence is not a reason to manufacture active semantic authority.

## Non-claims

Transaction A and Priority 12 remain open. No Models relationship closure, missing historical model reconstruction, MOD-011 maturity promotion, Runtime execution claim, provider authenticity, external trust anchor, Global Connected Baseline, Global Integrity, HORUS promotion or Governance/learning promotion is claimed.

## Next gate

1. Commit/read-back/compare Material Unit 3.
2. Retrieve complete REP-013 before replacement and synchronize exact seven-path Models physical inventory with this Matrix in the same change set.
3. Retrieve complete REP-016 and synchronize verified P11 closure + P12 exact-inventory entry state with this Matrix in the same change set.
4. Only after both remaining surfaces are synchronized may the complete Transaction-A material HEAD enter closure-grade exact-head CI.
