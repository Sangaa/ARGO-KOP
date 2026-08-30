# ROOM 071 — RECONSTRUCTION SUPPLEMENT 202 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
Functional head: `746dbbb111099badc8cf87f1a3e2f747e69a241a`

## What was resolved
The dominant cross-surface H1-only ambiguity cohort classified as `MEMORY_TO_ROOT_EJR` now has deterministic current content/reference/consumer provenance evidence.

Bounded result:

`36 MEMORY_TO_ROOT GROUPS CENSUSED / ALL MEMBER CONTENT DISTINCT / PATH-BOUND CONSUMERS EXIST ON BOTH NAMESPACE SIDES / GLOBAL OWNER OR MIGRATION RULE REJECTED / GROUP-SPECIFIC AUTHORITY REVIEW REQUIRED`.

This checkpoint authorizes no identity migration or canonical-owner assignment.

## Exact-head functional evidence
At `746dbbb111099badc8cf87f1a3e2f747e69a241a`:
- Internal Document-ID Audit `33324585936` — `SUCCESS`.
- Full-Stack Repository Audit `33324585916` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33324585952` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33324585921` — `SUCCESS`.
- Real Mutation Matrix Regression `33324585918` — `SUCCESS`.

Artifact:
- ID `9735858989`.
- digest `sha256:e4f56bde088b1ffd158e415ed807f098b9e0bc711dbd3f171926a64abc6f0aaf`.
- `history_complete = true`.
- `classification_complete = true`.
- `decision = CENSUSED`.
- expected/observed groups = `36 / 36`.

## Cohort evidence
- all 36 groups have distinct content fingerprints across members;
- 35 groups have cardinality 2; `EJR-302` has cardinality 3;
- 18 groups have external exact-ID references;
- six groups have exact-member-path consumers;
- `EJR-165` exact-path references are Lease-184 analytical self-provenance and are not treated as independent governed authority;
- `EJR-211`, `EJR-214`, and `EJR-219` have exact Memory-member paths named by current governed/canonical memory evidence, including `MEM-009`;
- `EJR-301` and `EJR-302` have exact Root-member paths named by their corresponding current session-delta evidence.

Therefore exact-path consumers do not support one global namespace owner. They select Memory members for some IDs and Root members for others.

## Learned rules
1. `A DOMINANT NAMESPACE LINEAGE MUST NOT BE CONVERTED INTO A GLOBAL OWNER OR MIGRATION POLICY WHEN CURRENT EXACT-PATH CONSUMERS SELECT MEMBERS ON BOTH SIDES OF THAT LINEAGE.`
2. `EXACT-PATH CONSUMER EVIDENCE CAN NARROW A GROUP-SPECIFIC REFERENT, BUT ITS AUTHORITY DEPENDS ON CONSUMER ROLE; ANALYTICAL SELF-REFERENCES MUST BE SEPARATED FROM INDEPENDENT GOVERNED CONSUMERS.`
3. `SEARCH INDEX MISS DOES NOT NEGATE EXACT-PATH CONSUMER EVIDENCE RECOVERED BY DETERMINISTIC CURRENT-TREE SCAN AND DIRECT READ.`
4. `CONTENT DISTINCTNESS ACROSS A COHORT DOES NOT ASSIGN OWNERSHIP; IT ONLY REJECTS SIMPLE BYTE-COPY DUPLICATION AS A COHORT-WIDE EXPLANATION.`
5. `DYNAMIC COHORT MEMBERSHIP SHOULD FAIL ON CLASSIFIER DRIFT RATHER THAN HIDE A STALE FIXED-ID LIST.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- no owner assignment;
- Internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- six MIXED explicit-ID ambiguity groups remain separate and unsuppressed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- active indexed canonical uniqueness remains previously `CLOSED/PASS`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target
Rediscover live `main`, re-enter from this checkpoint, then perform a bounded group-specific path-bound provenance authority review for `EJR-211`, `EJR-214`, `EJR-219`, `EJR-301`, and `EJR-302` before any identity mutation. Inspect each exact-path consumer's authority/semantic role and the competing sibling record(s). Do not infer canonical ownership merely from namespace direction or consumer existence.
