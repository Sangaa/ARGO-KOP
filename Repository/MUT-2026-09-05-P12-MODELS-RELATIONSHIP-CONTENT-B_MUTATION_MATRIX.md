# Priority 12 — Models Relationship / Content Reconciliation — Transaction B Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Priority: `12 — Models`

State: `OPEN / UNIT-1 FAILURE CLASSIFIED / CORRECTIVE UNIT 2 APPLIED / EXACT-HEAD CI PENDING`

Entry HEAD: `69af54f26b8799815d049772ebec655c250df9fc`
Material Unit 1 HEAD: `3f80ce66e3d559000efe5a2a5d8cdadf63817d3c`

## Entry authority

Transaction A is `CLOSED / VERIFIED / RESUME-SAFE` and its Matrix-only closure HEAD passed Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix on the exact same SHA.

Priority 12 remains open specifically for relationship/content reconciliation and Models partition closure review.

## Governing semantic rule

`TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`

Corollaries established during Transaction B:

- `DIRECT SOURCE DECLARATION != ARCHITECTURALLY QUALIFIED DEPENDENCY`;
- `TARGET EXISTS != DEPENDENCY VALID`;
- `HISTORICAL TEST STRING != CURRENT CONTRACT`;
- a current `Related Documents` declaration supports bounded `REFERENCES`, not automatic dependency;
- a current explicit `Dependencies` declaration remains a source claim until dependency direction, ownership, necessity and architecture compatibility are qualified;
- a reconstruction/process reference explicitly declared non-dependent must not be promoted to `DEPENDS_ON`;
- reverse edges are not manufactured for symmetry.

## Material Unit 1

Unit 1 removed the stale Transaction-A-open statement from Models status, bound verified A closure, created an 18-row direct-source evidence surface and added an executable evidence guard.

Authorized paths were only:

- `Models/_FOLDER_STATUS.md`;
- `Repository/REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv`;
- `Quality/Integrity/test_models_p12_relationship_evidence.py`;
- this Matrix.

### Unit-1 exact-head failure classification

Exact-head Runtime/Integration run `33972869827` failed only in the integrity job. Prototype and integration jobs succeeded. The repository integrity suite reported `196 passed, 1 failed`.

The sole failure was `test_p12_models_status_preserves_open_relationship_boundary`, whose historical assertion still required the now-false string that REP-002/012/013/016 "remains part of the same open transaction". Transaction A had already been closed and exact-head verified before Unit 1. Therefore the failure is classified as:

`STALE HISTORICAL GUARD / CURRENT STATUS CORRECT / NO TRANSACTION-A REOPEN`.

Unit 1 is not promoted to verified merely because the failure is classified. A corrected exact head must pass all required workflow families.

## Corrective Material Unit 2 authorized set

| Change ID | Target | Action | Purpose |
|---|---|---|---|
| P12-B-C02-01 | `Quality/Integrity/test_models_p12_exact_inventory_allocation.py` | UPDATE | replace stale Transaction-A-open string assertion with current verified A-closed / P12-relationship-open contract |
| P12-B-C02-02 | `Repository/REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv` | UPDATE | separate direct source/target verification from authority qualification and registry eligibility |
| P12-B-C02-03 | `Quality/Integrity/test_models_p12_relationship_evidence.py` | UPDATE | fail closed against premature dependency promotion; bind ARC-006 direction/qualification rules |
| P12-B-C02-04 | this Matrix | UPDATE | preserve Unit-1 failure classification and authorize corrective Unit 2 |

No model source document and no REP-014 canonical registry row is mutated in Corrective Unit 2.

## Relationship evidence disposition after Unit 2

The 18 direct-source rows remain evidence, but they are no longer treated homogeneously:

- nine internal `Related Documents` rows are bounded documentary `REFERENCES` registration candidates;
- all nine `MOD-004` `Dependencies` declarations are held from REP-014 registration pending architectural dependency qualification;
- specifically, `MOD-004 → RUN-004/RUN-008/RUN-009/ENG-007` require both dependency-direction and qualification review under current ARC-006;
- `Models` is a repository domain/grouping rather than an independently established architectural layer, so folder location alone is not used to accept or reject a dependency claim.

This preserves the current source text while preventing source wording from being mistaken for validated graph authority.

## Additional content finding — REL-002

Current REP-014 records `REL-002 = MOD-001 → SRV-004 / CONSUMES`. Current direct `SRV-004` content instead explicitly declares `Models / MOD-001 Knowledge Domain Model` under its Dependencies and also names `Models/MOD-001_KNOWLEDGE_MODEL.md` under Related Documents.

Therefore REL-002 is now a bounded correction candidate requiring stable-ID direction/type reconciliation before new Models relationship rows are appended to REP-014. No REL-002 mutation is authorized in Unit 2.

## Non-claims

This unit does not register new canonical `REL-*` IDs, does not modify REP-014, does not promote any model maturity/status, does not delete unresolved source dependency declarations, does not resolve historical missing MOD-005..010 declarations, does not prove Runtime executable consumption, and does not close Priority 12, Models, Phase 1, Global Connected Baseline or Global Integrity.

## Next gate

1. exact-head four-family CI for Corrective Unit 2;
2. re-read evidence/status/Matrix;
3. reconcile REL-002 against current MOD-001 and SRV-004 direct sources plus historical provenance;
4. qualify or disposition held MOD-004 dependency claims through current Architecture authority;
5. only then register supported new relationships into REP-014.
