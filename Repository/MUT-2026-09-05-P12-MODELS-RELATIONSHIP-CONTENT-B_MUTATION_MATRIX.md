# Priority 12 — Models Relationship / Content Reconciliation — Transaction B Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Priority: `12 — Models`

State: `OPEN / UNIT-2 EXACT-HEAD VERIFIED / MATERIAL UNIT 3 APPLIED / EXACT-HEAD CI PENDING`

Entry HEAD: `69af54f26b8799815d049772ebec655c250df9fc`
Material Unit 1 HEAD: `3f80ce66e3d559000efe5a2a5d8cdadf63817d3c`
Corrective Unit 2 HEAD: `cdb9207c5bf231e4545d5209a4477390d844137a`
Material Unit 3 sequence:
- source correction: `44061df91c2d42bca9022c132fdc9570e6ebc73b`
- evidence classification: `8c57d0fd9e3e68618623b1ebabf879686d660733`
- executable guard: `ef1d48e4118dd364466669c49e4862a691023816`

## Entry authority

Transaction A is `CLOSED / VERIFIED / RESUME-SAFE` and its Matrix-only closure HEAD passed Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix on the exact same SHA.

Priority 12 remains open specifically for relationship/content reconciliation and Models partition closure review.

## Governing semantic rule

`TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`

Corollaries established during Transaction B:

- `DIRECT SOURCE DECLARATION != ARCHITECTURALLY QUALIFIED DEPENDENCY`;
- `TARGET EXISTS != DEPENDENCY VALID`;
- `HISTORICAL TEST STRING != CURRENT CONTRACT`;
- `SEMANTIC DEPENDENCY != RELATED AUTHORITY != DOWNSTREAM CONSUMER != REVALIDATION TARGET`;
- a current `Related Documents` declaration supports bounded `REFERENCES`, not automatic dependency;
- an explicit dependency declaration must still satisfy current architecture direction/qualification;
- a reconstruction/process reference explicitly declared non-dependent must not be promoted to `DEPENDS_ON`;
- reverse edges are not manufactured for symmetry;
- physical folder placement never defines architectural layer authority by itself.

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

## Corrective Material Unit 2

Unit 2 replaced the stale A-open assertion with the current A-closed/P12-relationship-open contract, separated direct-source evidence from authority qualification, and prevented premature registration of unqualified dependency claims.

Exact-head `cdb9207c5bf231e4545d5209a4477390d844137a` passed all four required workflow families:

- M2 Multi-Channel Proposal Training — `33973136658` — SUCCESS;
- Real Mutation Matrix Regression — `33973136624` — SUCCESS;
- Full-Stack Repository Audit — `33973136630` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33973136687` — SUCCESS.

Therefore Corrective Unit 2 is `VERIFIED` within its bounded scope.

## Material Unit 3 — Memory Model dependency-boundary reconciliation

Direct content review found that `MOD-004` used one undifferentiated `Dependencies` list for three materially different classes:

1. semantic model-composition dependencies;
2. Architecture decision/evolution review references;
3. downstream Runtime/Engine compatibility and revalidation targets.

Current `ARC-011` defines architectural boundaries independently of repository folders, while `ARC-006` requires qualified dependency direction and states that textual reference alone does not establish architectural dependency.

Unit 3 therefore corrects the source contract rather than encoding the ambiguity into REP-014.

### Unit-3 material sequence

| Change | Target | Result |
|---|---|---|
| P12-B-U3-01 | `Models/MOD-004_MEMORY_MODEL.md` | version 1.2.3; split semantic dependencies, related authority/evolution references, and downstream revalidation targets |
| P12-B-U3-02 | `Repository/REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv` | reclassified the same 18 evidence rows against corrected source semantics |
| P12-B-U3-03 | `Quality/Integrity/test_models_p12_relationship_evidence.py` | executable guard prevents Runtime/Engine ripple targets from returning to `DEPENDS_ON` and binds three semantic-model dependencies |
| P12-B-U3-04 | this Matrix | bind Unit-3 evidence and exact-head gate |

### Current evidence disposition

The 18-row evidence surface now contains:

- 9 bounded `Related Documents → REFERENCES` registration candidates;
- 3 `MOD-004` semantic-model `DEPENDS_ON` registration candidates (`MOD-002`, `MOD-003`, `MOD-011`);
- 2 Architecture review/evolution `REFERENCES` registration candidates (`ARC-009`, `ARC-010`);
- 4 Runtime/Engine ripple/revalidation targets classified `NONE / DO_NOT_REGISTER` (`RUN-004`, `RUN-008`, `RUN-009`, `ENG-007`).

No reverse relationship is inferred from those four ripple targets. A future direct consumer-side review may establish a consumer/affected relationship in its own direction and controlled type, but this Unit does not manufacture it.

## Open stable-ID correction — REL-002

Current REP-014 still records:

`REL-002 = MOD-001 → SRV-004 / CONSUMES`.

Current direct `SRV-004` content states that the Knowledge Service depends on `Models / MOD-001 Knowledge Domain Model` and directly references `Models/MOD-001_KNOWLEDGE_MODEL.md`. Current `MOD-001` identifies SRV-004 as an inspected knowledge-service relationship but does not establish that MOD-001 consumes SRV-004.

Accordingly, the current strongest direct-source representation is a correction candidate:

`REL-002 stable ID: SRV-004 → MOD-001 = DEPENDS_ON`

This correction remains uncommitted until Unit-3 exact-head CI passes and the canonical REP-014 full-content preservation boundary is satisfied.

## Non-claims

Transaction B does not yet close Priority 12 or Models. Unit 3 does not register new `REL-*` IDs, does not mutate REP-014, does not promote model maturity, does not resolve historical MOD-005..010 declarations, does not prove Runtime executable consumption, and does not claim Phase-1, Global Connected Baseline or Global Integrity closure.

## Next gate

1. exact-head four-family CI for the Unit-3 Matrix head;
2. if green, reconcile stable `REL-002` without creating a replacement ID;
3. register only the 14 currently eligible relationship candidates after duplicate/type checks and safe REP-014 content-preserving mutation;
4. re-read Models status, relationship evidence and cross-layer consumers;
5. continue historical missing-declaration/content overlap review before any P12 partition-closure decision.
