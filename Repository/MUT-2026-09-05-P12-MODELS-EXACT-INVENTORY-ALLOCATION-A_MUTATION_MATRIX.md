# Priority 12 — Models Exact Inventory / Allocation — Transaction A Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-INVENTORY-ALLOCATION-A`

Priority: `12 — Models`

State: `MATERIAL COMPLETE / EXACT-HEAD CI PENDING`

Entry HEAD: `15d94d97e848060aafabe7faa3c369f852b62c35`
Pre-write Matrix HEAD: `109b58043517aeb6c14d204bfe61cee41066c415`
Material Unit 1 HEAD: `bec6f61072607e77aab753fe2eace5eb027df491`
Material Unit 2 HEAD: `1b98df1cbb1f57a681924827191bf72bc05b955a`
Material Unit 3 HEAD: `adc2c6d6808cd33bed5b4a2adb59eb094136e964`
Material Unit 4 HEAD: `b20330bb55ff85da6fed69604c90b3909a29e89a`

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

## Authorized material set and completion

| Change ID | Target | Action | Final material state |
| --- | --- | --- | --- |
| P12-A-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | APPLIED / VERIFIED BY COMPARE |
| P12-A-02 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | APPLIED / VERIFIED BY COMPARE |
| P12-A-03 | `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv` | CREATE | APPLIED / READ-BACK VERIFIED |
| P12-A-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | APPLIED / VERIFIED BY COMPARE |
| P12-A-05 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | APPLIED IN MATERIAL UNIT 5 |
| P12-A-06 | `Models/_FOLDER_STATUS.md` | UPDATE | APPLIED / READ-BACK VERIFIED |
| P12-A-07 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | CREATE | APPLIED / EXECUTABLE GUARD PRESENT |
| P12-A-08 | this Matrix | UPDATE | SAME-CHANGE-SET BINDING ON EACH PROTECTED UNIT |

No other path is authorized.

## Material evidence

Material Unit 1 established the exact seven-row manifest, Models status exact inventory/digest/open boundary, executable integrity guard and Matrix binding. Exact-head regression evidence on `bec6f61072607e77aab753fe2eace5eb027df491` was green across Full-Stack `33949936759`, Runtime `33949936748`, M2 `33949936765`, and Real Mutation Matrix `33949936764`.

Material Unit 2 synchronized REP-002 to the exact seven-path Models physical map, including README as domain-container/navigation evidence, without semantic promotion. Candidate compare showed only REP-002 plus this Matrix changed.

Material Unit 3 appended the exact seven-row Models allocation binding to REP-012 while preserving all historical registry content. Candidate compare showed only REP-012 plus this Matrix changed.

Material Unit 4 synchronized the REP-013 Models section from the stale partial three-path representation to the exact seven-path inventory with digest/manifest binding. Candidate compare showed only REP-013 plus this Matrix changed; REP-013 itself changed by 22 lines, with historical content preserved.

Material Unit 5 synchronizes REP-016 queue freshness only: Priority 11 records its verified bounded closure; Priority 12 records exact inventory/allocation reconciliation as complete while relationship validation and Models partition closure remain OPEN. This does not auto-promote downstream priorities.

## Deliberate non-change

REP-001 remains unchanged because it already represents the five active model artifacts plus `_FOLDER_STATUS.md`; physical README presence does not grant active model semantic authority.

REP-014 remains unchanged because Transaction A registers no new semantic relationship and physical allocation alone must not manufacture relationship authority.

## Non-claims

Transaction A does not close Priority 12 or Models. It does not certify Models ↔ Knowledge/Memory/Runtime/Services/Interfaces/AI/Repository/Release relationships; reconstruct missing historical MOD identities; promote MOD-011 beyond Proposed / Future-Ready; establish Runtime consumer execution; establish provider authenticity, external trust anchors, Global Connected Baseline or Global Integrity; or promote HORUS/Governance/learning material.

## Exact-head validation gate

The complete material HEAD must pass all four workflow families on the exact same SHA:

1. Full-Stack Repository Audit
2. ARGO Runtime Prototype and Integration Tests
3. M2 Multi-Channel Proposal Training
4. Real Mutation Matrix Regression

If any family fails, Transaction A remains open and the failure must be classified before repair. If all four succeed and no new contradictory Models-specific evidence appears, a Matrix-only final closure commit may set Transaction A to `CLOSED / VERIFIED / RESUME-SAFE`; that final closure SHA must itself pass all four workflow families before closure is declared.
