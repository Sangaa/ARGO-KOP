# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 12 Matrix Addendum

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-11 EXACT-HEAD VERIFIED / MATERIAL UNIT 12 APPLIED / EXACT-HEAD CI PENDING`

Unit-11 final exact-head: `8aa291d6ab097a244667440c35e1400b2ca6e5b7`

Unit-11 exact-head workflows:
- M2 `33976333022` — SUCCESS
- Real Mutation Matrix `33976333024` — SUCCESS
- Full-Stack `33976333010` — SUCCESS
- Runtime/Integration `33976333006` — SUCCESS

## Scope

Resolve the active canonical-authority ambiguity between `Models/MOD-001_KNOWLEDGE_MODEL.md` and `Knowledge/KNW-001_KNOWLEDGE_MODEL.md` without mutating or certifying the Knowledge partition.

## Finding

Both artifacts are canonical and both use knowledge-model terminology, but current content represents distinct responsibilities:

- `MOD-001` defines knowledge-object structure, entity/relationship schema, traceability fields and implementation-independent structural semantics;
- `KNW-001` defines Knowledge-domain scope (`SESSION`, `USER`, `PROJECT`, `DEPLOYMENT`, `SHARED_CANDIDATE`, `PLATFORM`), operational lifecycle, states, ownership and cross-domain promotion.

Without an explicit authority boundary, both canonical artifacts could be misread as competing definitions of one knowledge-model authority.

## Source repair

`MOD-001` v1.1.3 now explicitly states:

- `MOD-001` owns the semantic knowledge-object/schema contract inside Models;
- `KNW-001` owns Knowledge-domain scope/lifecycle/promotion semantics;
- MOD-001 does not own Knowledge-domain storage/ownership, cross-domain promotion or the operational `KNW-*` lifecycle;
- `MOD-001 → KNW-001 = REFERENCES / AUTHORITY-BOUNDARY / NON-DEPENDENCY`;
- no reverse edge is inferred because current KNW-001 does not directly name MOD-001.

Invariant:

`SEMANTIC KNOWLEDGE SCHEMA AUTHORITY != KNOWLEDGE-DOMAIN OWNERSHIP != LIFECYCLE/PROMOTION AUTHORITY`.

Generalized pattern now supported by two independently inspected pairs:

`MODELS SEMANTIC SCHEMA AUTHORITY != DOMAIN OWNERSHIP/LIFECYCLE/PROMOTION AUTHORITY`.

This generalization is bounded to pairs whose current source content actually supports the separation; it is not inferred from folder names alone.

## Evidence and guard

- `Repository/REP-014_PRIORITY12_MOD001_KNW001_AUTHORITY_EVIDENCE_2026-09-05_J.tsv`
- `Quality/Integrity/test_models_p12_mod001_knw001_authority.py`
- `Models/MOD-001_KNOWLEDGE_MODEL.md` v1.1.3
- this Matrix addendum

## Non-claims

Unit 12 does not mutate KNW-001, does not revalidate or close the Knowledge partition, does not register a canonical REL ID, does not promote MOD-001 beyond `Integrity Hold / Relationship-Revalidated`, and does not close Models/P12.

## Status-write discipline

`Models/_FOLDER_STATUS.md` is intentionally not rewritten in the same material unit. Unit 11 demonstrated that broad status rewrites can accidentally drop still-valid stable representations protected by existing guards. Status synchronization therefore follows only after this source/evidence unit passes exact-head validation, preserving all stable markers explicitly.

## Next gate

1. exact-head four-family CI;
2. if green, synchronize Models status with a bounded marker-preserving update;
3. finish active-model responsibility-set review (`MOD-002`, `MOD-003`, `MOD-011`) for any remaining primary-authority collision;
4. continue Models↔Release and concrete Specifications↔Models reconciliation.
