# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 11 Matrix Addendum

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-10 EXACT-HEAD VERIFIED / MATERIAL UNIT 11 APPLIED / EXACT-HEAD CI PENDING`

Unit-10 exact-head: `22ea9d9f701c57f49e4cca4f4bb93d2834f1785c`

Unit-10 exact-head workflows:
- M2 `33975440836` — SUCCESS
- Real Mutation Matrix `33975440831` — SUCCESS
- Full-Stack `33975440840` — SUCCESS
- Runtime/Integration `33975440823` — SUCCESS

## Scope

Resolve the canonical-authority ambiguity between `Models/MOD-004_MEMORY_MODEL.md` and `Memory/MEM-001_MEMORY_MODEL.md` without mutating or certifying the Memory partition.

## Finding

Both artifacts used the title `MEMORY MODEL` and both declared `Canonical: Yes`, but current content represented materially different responsibilities:

- `MOD-004` defines memory-object structure, identity-facing fields, provenance, scope and implementation-independent semantic constraints;
- `MEM-001` defines Memory-domain separation among platform/user/project/deployment/session memory and governs promotion into Platform Memory.

Without an explicit source boundary, title equality plus canonical flags created a real duplicate-authority ambiguity.

## Source repair

`MOD-004` v1.2.4 now explicitly states:

- `MOD-004` owns the semantic memory-object/schema contract inside Models;
- `MEM-001` owns Memory-domain scope/promotion semantics;
- MOD-004 does not own the Memory domain's operational taxonomy, promotion policy or MEM-* lifecycle authority;
- `MOD-004 → MEM-001 = REFERENCES / AUTHORITY-BOUNDARY / NON-DEPENDENCY`;
- no reverse edge is inferred because current MEM-001 does not directly name MOD-004.

Invariant:

`SEMANTIC SCHEMA AUTHORITY != MEMORY-DOMAIN OWNERSHIP != PROMOTION AUTHORITY`.

## Evidence and guard

- `Repository/REP-014_PRIORITY12_MOD004_MEM001_AUTHORITY_EVIDENCE_2026-09-05_I.tsv`
- `Quality/Integrity/test_models_p12_mod004_mem001_authority.py`
- `Models/_FOLDER_STATUS.md` v1.3.5 synchronized to current Units 1–11 evidence
- this Matrix addendum

## Non-claims

Unit 11 does not mutate MEM-001, does not close or revalidate the Memory partition, does not register a canonical REL ID, does not promote MOD-004 beyond `Approved / Revalidation Required`, and does not close Models/P12.

## Next gate

1. exact-head four-family CI;
2. if green, review the remaining active Models responsibility set for duplicate/conflicting primary authority;
3. then reconcile Models↔Release and concrete Specifications↔Models consumers;
4. canonical REP-014 write remains a separate full-content-preserving gate.
