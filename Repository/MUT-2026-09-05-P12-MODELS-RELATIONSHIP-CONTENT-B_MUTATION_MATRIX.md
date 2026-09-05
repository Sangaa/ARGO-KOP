# Priority 12 — Models Relationship / Content Reconciliation — Transaction B Mutation Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Priority: `12 — Models`

State: `OPEN / MATERIAL UNIT 1 APPLIED / EXACT-HEAD CI PENDING`

Entry HEAD: `69af54f26b8799815d049772ebec655c250df9fc`

## Entry authority

Transaction A is `CLOSED / VERIFIED / RESUME-SAFE` and its Matrix-only closure HEAD passed Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix on the exact same SHA.

Priority 12 remains open specifically for relationship/content reconciliation and Models partition closure review.

## Governing semantic rule

`TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`

For this bounded cohort:

- a current `Related Documents` declaration supports `REFERENCES`, not an automatic dependency;
- a current explicit `Dependencies` declaration supports candidate `DEPENDS_ON` only after current target identity/path verification;
- a reconstruction/process reference explicitly declared non-dependent must not be promoted to `DEPENDS_ON`;
- reverse edges are not manufactured for symmetry;
- historical declarations do not override current direct-source semantics.

## Material Unit 1 authorized set

| Change ID | Target | Action | Purpose |
|---|---|---|---|
| P12-B-01 | `Models/_FOLDER_STATUS.md` | UPDATE | remove stale Transaction-A-open statement; bind verified A closure and B entry without closing Models |
| P12-B-02 | `Repository/REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv` | CREATE | record bounded direct-source relationship cohort without prematurely allocating canonical REL IDs |
| P12-B-03 | `Quality/Integrity/test_models_p12_relationship_evidence.py` | CREATE | executable guard for source/target existence and controlled-type/source-section semantics |
| P12-B-04 | this Matrix | CREATE | authorize and bind Transaction-B material unit 1 |

No other path is authorized by Material Unit 1.

## Direct-source cohort

Material Unit 1 records 18 bounded candidate relationships:

- six internal `MOD-002/MOD-003` `Related Documents` references;
- nine explicit `MOD-004` dependencies, including three Models dependencies and six verified Architecture/Runtime/Engine targets;
- three `MOD-011` internal Models `Related Documents` references.

`MOD-001` is intentionally not expanded in this unit because its current “Active Relationships Verified” section uses richer relationship language whose controlled REP-014 type must be classified independently rather than guessed.

Existing REP-014 `REL-010..014` Knowledge ↔ MOD-011 rows remain untouched pending their own direct-source/current-target comparison.

## Non-claims

This unit does not register canonical `REL-*` IDs, does not modify REP-014, does not promote any model maturity/status, does not certify reverse edges, does not resolve historical missing MOD-005..010 declarations, does not prove Runtime executable consumption, and does not close Priority 12, Models, Phase 1, Global Connected Baseline or Global Integrity.

## Next gate

1. exact-head four-family CI for this Material Unit 1;
2. re-read manifest/status/Matrix;
3. duplicate/type check against current REP-014;
4. direct target/authority verification for any additional cohort;
5. only then register supported relationships into REP-014 in a protected later material unit.
