# Priority 12 — Models Relationship / Content Reconciliation — Transaction B Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Priority: `12 — Models`

State: `OPEN / UNIT-5 EXACT-HEAD VERIFIED / MATERIAL UNIT 6 APPLIED / EXACT-HEAD CI PENDING`

Entry HEAD: `69af54f26b8799815d049772ebec655c250df9fc`
Material Unit 1 HEAD: `3f80ce66e3d559000efe5a2a5d8cdadf63817d3c`
Corrective Unit 2 HEAD: `cdb9207c5bf231e4545d5209a4477390d844137a`
Material Unit 3 final HEAD: `853024239bb3452ca64bc13487d017a95fedfac8`
Material Unit 4 final HEAD: `d0e4b45ac1714b076ef97751b0d52e73ef63e162`
Material Unit 5 final HEAD: `9c736567801a18955a2ddff2c5deae3938d83b20`
Material Unit 6 sequence:
- MOD-011 relationship evidence: `3d545e5e8b099a5e9d0afca8e3eddab0bb681da4`
- executable MOD-011 guard: `9d82d97eb63ef2c2d778a87529ca0d890c325e14`

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
- `DISCOVERY ARROW != RELATIONSHIP DIRECTION != CONTROLLED TYPE`;
- `INDEX MEMBERSHIP != SEMANTIC RELATIONSHIP`;
- `PHYSICAL MAPPING != SEMANTIC RELATIONSHIP`;
- `HISTORICAL GROUPED PLAUSIBILITY != CURRENT CONTROLLED TYPE`;
- a current `Related Documents` declaration supports bounded `REFERENCES`, not automatic dependency;
- a downstream artifact whose required output semantics explicitly comply with or adhere to a higher semantic contract may be a qualified semantic dependency when current Architecture direction permits it;
- an explicit dependency declaration must still satisfy current architecture direction/qualification;
- a reconstruction/process reference explicitly declared non-dependent must not be promoted to `DEPENDS_ON`;
- reverse edges are not manufactured for symmetry;
- physical folder placement never defines architectural layer authority by itself;
- canonical long-file preservation outranks convenience of local mutation;
- when a historical guard protects a still-valid semantic invariant at a stable contractual string, preserve that invariant rather than weakening the guard for wording convenience.

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

Direct content review found that `MOD-004` used one undifferentiated `Dependencies` list for three materially different classes: semantic model-composition dependencies, Architecture decision/evolution review references, and downstream Runtime/Engine compatibility/revalidation targets.

Unit 3 corrected the source contract rather than encoding that ambiguity into REP-014.

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

REL-002 remains:

`SEMANTIC CORRECTION VERIFIED / CANONICAL FULL-CONTENT WRITE PENDING`.

No new REL identifier is authorized as a substitute for the stable ID.

## Material Unit 4 — Historical declaration semantic disposition

Earlier P57/P58 source-first audits established that historical `MOD-005..MOD-010` files were not current active Models artifacts and that blind numeric reconstruction risked duplicate or conflicting authority. Unit 4 converted that mature evidence into current Models-domain content without creating historical files.

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

The first Unit-4 Matrix head failed only a still-valid stable sentence guard. The status wording was repaired without weakening the guard or rolling back current dispositions.

Exact-head final Unit-4 HEAD `d0e4b45ac1714b076ef97751b0d52e73ef63e162` passed all four required workflow families:

- Real Mutation Matrix Regression — `33973834280` — SUCCESS;
- M2 Multi-Channel Proposal Training — `33973834019` — SUCCESS;
- Full-Stack Repository Audit — `33973834021` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33973834052` — SUCCESS.

Therefore Material Unit 4 is `VERIFIED` within its bounded semantic-disposition scope.

## Material Unit 5 — MOD-001 current consumer reconciliation

Historical P58 arrows were used only to discover candidate consumers. Current endpoint text and Architecture authority determine direction/type.

Unit 5 created:

- `Repository/REP-014_PRIORITY12_MOD001_CONSUMER_EVIDENCE_2026-09-05_C.tsv`;
- `Quality/Integrity/test_models_p12_mod001_consumers.py`;
- this Matrix binding.

### Unit-5 current-source dispositions

| Candidate | Current direct-source disposition | Registry action |
|---|---|---|
| `SRV-004 → MOD-001` | `DEPENDS_ON`; SRV-004 explicitly declares Models/MOD-001 dependency and direct related document | correct stable `REL-002` when safe full-content registry write is available |
| `SRV-010 ↔ MOD-001` | no direct SRV-010 semantic dependency/consumer contract; only navigation describing SRV-004's inspected relationship | `DO_NOT_REGISTER` |
| `KNW-004 → MOD-001` | `REFERENCES`; KNW-004 directly lists MOD-001 under Related Documents | registration candidate |
| `INT-001 → MOD-001` | `DEPENDS_ON`; Intelligence synthesis output is required to comply with MOD-001 semantics, and current architecture permits downstream Cognition/Engine-class semantics to depend on Knowledge | registration candidate |
| `INT-002 → MOD-001` | `DEPENDS_ON`; pattern-extraction outputs are required to adhere to MOD-001 semantics, with the same downstream architectural direction | registration candidate |
| `REP-001 ↔ MOD-001` | index membership records inventory only and explicitly does not certify relationships | `DO_NOT_REGISTER` |
| `REP-002 ↔ MOD-001` | physical mapping records presence only | `DO_NOT_REGISTER` |

Exact-head Unit-5 HEAD `9c736567801a18955a2ddff2c5deae3938d83b20` passed all four required workflow families:

- M2 Multi-Channel Proposal Training — `33974010878` — SUCCESS;
- Real Mutation Matrix Regression — `33974010896` — SUCCESS;
- Full-Stack Repository Audit — `33974010873` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33974010903` — SUCCESS.

Therefore Material Unit 5 is `VERIFIED` within its bounded MOD-001 consumer scope.

## Material Unit 6 — MOD-011 existing relationship reconciliation

Current REP-014 records `REL-010..014`. Historical EJR-409 shows those five rows were once grouped as plausible `DEPENDS_ON` relationships and intentionally left unpromoted because endpoint authority was not yet sufficient. Later repairs corrected four rows, but `REL-012` retained the historical dependency type.

Unit 6 creates:

- `Repository/REP-014_PRIORITY12_MOD011_RELATIONSHIP_EVIDENCE_2026-09-05_D.tsv`;
- `Quality/Integrity/test_models_p12_mod011_relationships.py`;
- this Matrix binding.

### Unit-6 current dispositions

| Stable/current relationship | Disposition |
|---|---|
| `REL-010 KNW-002 → MOD-011 = CONSUMES` | retain; KNW-002 explicitly states Classification consumes MOD-011 source/evidence semantics |
| `REL-011 MOD-011 → KNW-003 = REFERENCES` | retain; MOD-011 lists KNW-003 under Related Documents |
| `KNW-003 → MOD-011 = REFERENCES` | new registration candidate; KNW-003 directly lists MOD-011 under Related Documents |
| `REL-012 MOD-011 → KNW-004` | stable ID retained but type correction verified: `DEPENDS_ON → REFERENCES`; current MOD-011 evidence is Related Documents/review boundary, not a required dependency contract |
| `KNW-004 → MOD-011 = REFERENCES` | new registration candidate; KNW-004 directly lists MOD-011 and describes source/provenance interaction |
| `REL-013 MOD-011 → KNW-008 = REFERENCES` | retain; direct MOD-011 Related Documents evidence supports the existing one-way reference |
| `REL-014 KNW-009 → MOD-011 = CONSUMES` | retain; KNW-009 explicitly states Knowledge evolution consumes MOD-011 semantics |

Unit 6 intentionally guards that REP-014 is **not yet corrected** for REL-012, preventing evidence readiness from being misreported as canonical registry mutation.

`REL-012 = SEMANTIC TYPE CORRECTION VERIFIED / CANONICAL FULL-CONTENT WRITE PENDING`.

No replacement stable ID is authorized.

## Non-claims

Transaction B does not yet close Priority 12 or Models. Unit 6 does not mutate REP-014, does not allocate final `REL-*` IDs to new candidates, does not promote MOD-011 beyond its current maturity, does not certify all Knowledge consumers and does not claim Phase-1, Global Connected Baseline or Global Integrity closure.

## Next gate

1. exact-head four-family CI for this Unit-6 Matrix head;
2. if green, mark Unit 6 verified;
3. continue current-source consumer reconciliation for MOD-002 / MOD-003 / MOD-004 and additional MOD-011 consumers outside the already reconciled Knowledge cohort;
4. keep REL-002, REL-012 and new registration candidates pending until REP-014 can be changed with guaranteed full-content preservation;
5. reconcile Models status/REP-016 after consumer cohorts before any P12 partition-closure decision.
