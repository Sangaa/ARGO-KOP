# Priority 12 — Models Exact Inventory / Allocation — Transaction A Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-INVENTORY-ALLOCATION-A`

Priority: `12 — Models`

State: `PARTIAL MATERIAL APPLIED / EXACT INVENTORY + MANIFEST GUARDED / CONTROL-PLANE SYNC PENDING`

Entry HEAD: `15d94d97e848060aafabe7faa3c369f852b62c35`
Pre-write Matrix HEAD: `109b58043517aeb6c14d204bfe61cee41066c415`

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

Current control-plane drift remains bounded and explicit:

- REP-013 represents only README, MOD-001 and MOD-011 and marks the representation partial.
- REP-002 represents the five MOD artifacts plus `_FOLDER_STATUS.md` but omits README from its physical map.
- REP-012 has no directly located Models path-level exact allocation set in the inspected current registry content.
- REP-016 predates the verified P11 closure and still requires queue synchronization.
- REP-001 already indexes the five active model artifacts plus `_FOLDER_STATUS.md`; no REP-001 change is authorized by physical inventory alone.

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
| P12-A-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | SYNC PENDING |
| P12-A-02 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | SYNC PENDING |
| P12-A-03 | `Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | SYNC PENDING |
| P12-A-05 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | SYNC PENDING |
| P12-A-06 | `Models/_FOLDER_STATUS.md` | UPDATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-07 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | CREATE | APPLIED IN MATERIAL UNIT 1 |
| P12-A-08 | this Matrix | UPDATE | APPLIED / SAME-CHANGE-SET BINDING |

No other path is authorized.

## Material Unit 1 rationale

The connector exposes safe whole-file replacement and Git tree commits but no semantic patch writer for large Markdown blobs. REP-002/012/013/016 responses are large and tool presentation may truncate them. Replacing any such control surface from incomplete visible content would risk a content-preservation regression.

Therefore this transaction persists the independently safe exact-inventory unit first:

- exact path-level allocation manifest;
- Models status exact inventory/digest/open-state binding;
- executable integrity guard;
- governing Matrix in the same changed-file set.

The remaining authorized control-plane synchronization stays open in this same transaction and must use complete current content before replacement. This is bounded execution, not a waiver of the synchronization requirement.

## Deliberate non-change

REP-001 remains unchanged because it already represents the five active model artifacts plus `_FOLDER_STATUS.md`; README physical presence does not grant it active semantic authority.

## Non-claims

Transaction A and Priority 12 remain open. No Models relationship closure, missing historical model reconstruction, MOD-011 maturity promotion, Runtime execution claim, provider authenticity, external trust anchor, Global Connected Baseline, Global Integrity, HORUS promotion or Governance/learning promotion is claimed.

## Next gate

1. Commit and immutable-read Material Unit 1.
2. Parent→HEAD compare must show exactly manifest + Models status + P12 integrity guard + this Matrix.
3. Re-read complete current REP-002/012/013/016 content before any replacement.
4. Synchronize those four surfaces with this Matrix in the same protected-change set.
5. Re-run exact-head four-family CI only after the complete Transaction-A material set is applied; Unit 1 alone is not closure evidence.
