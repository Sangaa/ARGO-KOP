# Priority 12 — Models Relationship / Content Reconciliation — Transaction B Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Priority: `12 — Models`

State: `OPEN / UNIT-3 EXACT-HEAD VERIFIED / MATERIAL UNIT 4 APPLIED / EXACT-HEAD CI PENDING`

Entry HEAD: `69af54f26b8799815d049772ebec655c250df9fc`
Material Unit 1 HEAD: `3f80ce66e3d559000efe5a2a5d8cdadf63817d3c`
Corrective Unit 2 HEAD: `cdb9207c5bf231e4545d5209a4477390d844137a`
Material Unit 3 final HEAD: `853024239bb3452ca64bc13487d017a95fedfac8`
Material Unit 4 sequence:
- historical semantic disposition: `aa6e3d33cca03510566ac9449150659dbb22ae18`
- folder-status synchronization: `8c8b1c33cb3a667f92ee8e1a12a0698a14218fe3`
- executable historical-disposition guard: `b50175d2db0f40e753433c91ca5c5ae97c11fbf0`

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
- `MISSING HISTORICAL FILE != MISSING CURRENT CONCEPT`;
- `HISTORICAL IDENTIFIER != CURRENT AUTHORITY`;
- a current `Related Documents` declaration supports bounded `REFERENCES`, not automatic dependency;
- an explicit dependency declaration must still satisfy current architecture direction/qualification;
- a reconstruction/process reference explicitly declared non-dependent must not be promoted to `DEPENDS_ON`;
- reverse edges are not manufactured for symmetry;
- physical folder placement never defines architectural layer authority by itself;
- canonical long-file preservation outranks convenience of local mutation.

## Material Unit 1

Unit 1 removed the stale Transaction-A-open statement from Models status, bound verified A closure, created an 18-row direct-source evidence surface and added an executable evidence guard.

### Unit-1 exact-head failure classification

Exact-head Runtime/Integration run `33972869827` failed only in the integrity job. Prototype and integration jobs succeeded. The sole failing assertion required a now-false Transaction-A-open string after A had already closed and passed exact-head validation.

Classification:

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

Unit 3 corrected the source contract rather than encoding the ambiguity into REP-014.

Current 18-row evidence disposition after Unit 3:

- 9 bounded `Related Documents → REFERENCES` registration candidates;
- 3 `MOD-004` semantic-model `DEPENDS_ON` registration candidates (`MOD-002`, `MOD-003`, `MOD-011`);
- 2 Architecture review/evolution `REFERENCES` registration candidates (`ARC-009`, `ARC-010`);
- 4 Runtime/Engine ripple/revalidation targets classified `NONE / DO_NOT_REGISTER` (`RUN-004`, `RUN-008`, `RUN-009`, `ENG-007`).

Exact-head `853024239bb3452ca64bc13487d017a95fedfac8` passed all four required workflow families:

- Real Mutation Matrix Regression — `33973389095` — SUCCESS;
- M2 Multi-Channel Proposal Training — `33973389140` — SUCCESS;
- Full-Stack Repository Audit — `33973389152` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33973389132` — SUCCESS.

Therefore Material Unit 3 is `VERIFIED` within its bounded source/evidence scope.

## Stable-ID correction finding — REL-002

Current REP-014 still records:

`REL-002 = MOD-001 → SRV-004 / CONSUMES`.

Current direct `SRV-004` content states that the Knowledge Service depends on `Models / MOD-001 Knowledge Domain Model` and directly references `Models/MOD-001_KNOWLEDGE_MODEL.md`. Current `MOD-001` identifies SRV-004 as an inspected knowledge-service relationship but does not establish that MOD-001 consumes SRV-004.

Historical `EJR-203` already recorded the stronger SRV-004 dependency evidence but deferred canonical mutation.

Current strongest direct-source correction candidate is:

`REL-002 stable ID: SRV-004 → MOD-001 = DEPENDS_ON`.

A fail-closed guard was briefly introduced after Unit-3 verification to require this canonical correction, then removed immediately when the available GitHub write surface was confirmed to provide full-file replacement only for the long REP-014 registry. The guard was not retained because leaving main intentionally red while a safe full-content-preserving canonical write remained unresolved would violate the repository's own preservation discipline.

REL-002 therefore remains:

`SEMANTIC CORRECTION VERIFIED / CANONICAL FULL-CONTENT WRITE PENDING`.

No new REL identifier is authorized as a substitute for the stable ID.

## Material Unit 4 — Historical declaration semantic disposition

Earlier P57/P58 source-first audits had already established that historical `MOD-005..MOD-010` files were not current active Models artifacts and that blind numeric reconstruction risked duplicate or conflicting authority. Those checkpoints deliberately stopped at assessment.

Unit 4 converts that mature evidence into current Models-domain content without creating historical files.

### Unit-4 dispositions

| Historical declaration | Current bounded disposition |
|---|---|
| `MOD-001_MODEL_ARCHITECTURE.md` | `DO_NOT_RECREATE_BY_NAME`; historical namespace conflicts with active MOD-001 while Architecture ownership is already explicit |
| `MOD-005_KNOWLEDGE_MODEL.md` | current semantic coverage exists; `NO DISTINCT GAP PROVEN` |
| `MOD-006_RUNTIME_MODEL.md` | Runtime domain owns current runtime contracts; `NO RECREATE` without a distinct implementation-independent semantic gap |
| `MOD-007_SERVICE_MODEL.md` | Services domain owns current service architecture/reference responsibilities; `NO RECREATE` without distinct model need |
| `MOD-008_RELATIONSHIP_MODEL.md` | overlaps active model semantics and REP-014 relationship control; `NO DISTINCT MODEL GAP PROVEN` |
| `MOD-009_VERSION_MODEL.md` | would risk collision with Release/version authority; `NO RECREATE` |
| `MOD-010_MODEL_REFERENCE.md` | navigation/reference responsibility covered by Models container plus repository index/map/relationship controls; `NO RECREATE` |

This resolves the numeric-restoration question, not every historical consumer or concept. Historical provenance remains preserved. A future model remains possible only if a distinct current semantic responsibility, owner, authority boundary and material consumer need are independently demonstrated.

### Unit-4 material set

- `Models/README.md` — v1.3.2; current semantic dispositions and reconstruction rule;
- `Models/_FOLDER_STATUS.md` — v1.3.4; marks numeric restoration disposition resolved while preserving P12/Models hold;
- `Quality/Integrity/test_models_p12_historical_disposition.py` — prevents silent historical file recreation and binds non-promotion/semantic-gap rules;
- this Matrix — evidence binding and exact-head gate.

## Non-claims

Transaction B does not yet close Priority 12 or Models. Unit 4 does not register new `REL-*` IDs, does not mutate REP-014, does not promote model maturity, does not prove Runtime executable consumption, does not certify all model consumers and does not claim Phase-1, Global Connected Baseline or Global Integrity closure.

## Next gate

1. exact-head four-family CI for Unit 4;
2. re-read Unit-4 README/status/guard;
3. continue current consumer reconciliation beginning with the concrete MOD-001 consumer cohort established by P58;
4. complete safe full-content-preserving REL-002 correction and eligible REP-014 registration when the canonical long-file write can preserve all registry history;
5. reconcile remaining MOD-002/003/004/011 consumer cohorts and status/queue surfaces before any P12 partition-closure decision.
