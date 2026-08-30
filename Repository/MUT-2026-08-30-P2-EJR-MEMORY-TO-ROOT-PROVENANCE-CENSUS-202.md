# MUT-2026-08-30 — P2 EJR MEMORY→ROOT COHORT PROVENANCE CENSUS — LEASE 202

Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
Baseline: `main@ed0642f9d1fd579f7cf7b39a3c1e5406596a8d8d`
Prewrite head: `b3185e877b0977e79fd744bdaa206372c706b474`
Functional head: `746dbbb111099badc8cf87f1a3e2f747e69a241a`

## Trigger
Leases 199–201 proved that namespace direction is provenance evidence, not ownership authority. The four non-monotonic and four reverse-direction exceptional H1-only ambiguity groups already had independent content/reference/consumer evidence. Lease 202 therefore inspected the remaining dominant cross-surface H1-only cohort classified by Lease 199 as `MEMORY_TO_ROOT_EJR`.

## Functional result
A deterministic evidence-only cohort analyzer was added:

`Quality/Integration/ejr_memory_to_root_provenance_census.py`

with regressions in:

`Quality/Integration/test_ejr_memory_to_root_provenance_census.py`.

The target IDs are not hardcoded. They are derived from the current namespace-lineage report where classification equals `MEMORY_TO_ROOT_EJR`. The established cohort count is 36; count drift fails `PARTIAL`. Incomplete history fails closed.

The analyzer emits current member paths, namespace sequence, first-H1 titles, SHA-256 content fingerprints, exact-ID reference paths, and exact-member-path consumer paths. It contains no owner/canonical/migration/rename/delete/reassignment/suppression/allocation disposition.

## Exact-head verification
At functional head `746dbbb111099badc8cf87f1a3e2f747e69a241a` all observed workflows succeeded:

- Internal Document-ID Audit `33324585936` — `SUCCESS`.
- Full-Stack Repository Audit `33324585916` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33324585952` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33324585921` — `SUCCESS`.
- Real Mutation Matrix Regression `33324585918` — `SUCCESS`.

Artifact:
- ID `9735858989`.
- name `ejr-memory-to-root-provenance-census`.
- digest `sha256:e4f56bde088b1ffd158e415ed807f098b9e0bc711dbd3f171926a64abc6f0aaf`.
- `history_complete = true`.
- `classification_complete = true`.
- `decision = CENSUSED`.
- expected groups = `36`.
- observed groups = `36`.

## Cohort evidence
All 36 groups have distinct content fingerprints across their current members. Thirty-five groups have two members; `EJR-302` has three.

Eighteen groups have at least one current external exact-ID reference. Six groups have at least one exact-member-path consumer:

- `EJR-165`: both current member paths are named only by Lease-184 analytical provenance records. This is self-analytical evidence and is not treated as independent operational authority.
- `EJR-211`: `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md` is explicitly named by `Memory/MEM-009_MEMORY_EVOLUTION.md` and `Repository/REP-020_SESSION_DELTA_2026-08-14_P29.md`.
- `EJR-214`: `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md` is explicitly named by `Memory/MEM-009_MEMORY_EVOLUTION.md` and `Repository/SEMANTIC_EXPERIENCE_AUDIT_PILOT_165_2026-08-29.md`.
- `EJR-219`: `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md` is explicitly named by `Memory/MEM-009_MEMORY_EVOLUTION.md`.
- `EJR-301`: `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md` is explicitly named by `Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md`.
- `EJR-302`: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md` is explicitly named by `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`.

Therefore current exact-path consumers select Memory members in some groups and Root members in others. This directly blocks any blanket rule that interprets the majority `MEMORY_TO_ROOT_EJR` lineage as global canonical ownership or automatic migration direction.

## Search/retrieval evidence
A current repository search for the exact EJR-211 Memory path returned no search result, while the deterministic current-tree census found the exact consumer and a direct current-head read of `Memory/MEM-009_MEMORY_EVOLUTION.md` confirmed the explicit path. The search miss is therefore bounded retrieval/index evidence, not path absence.

## Learned rules
1. `A DOMINANT NAMESPACE LINEAGE MUST NOT BE CONVERTED INTO A GLOBAL OWNER OR MIGRATION POLICY WHEN CURRENT EXACT-PATH CONSUMERS SELECT MEMBERS ON BOTH SIDES OF THAT LINEAGE.`
2. `EXACT-PATH CONSUMER EVIDENCE CAN NARROW A GROUP-SPECIFIC REFERENT, BUT ITS AUTHORITY DEPENDS ON CONSUMER ROLE; ANALYTICAL SELF-REFERENCES MUST BE SEPARATED FROM INDEPENDENT GOVERNED CONSUMERS.`
3. `SEARCH INDEX MISS DOES NOT NEGATE EXACT-PATH CONSUMER EVIDENCE RECOVERED BY DETERMINISTIC CURRENT-TREE SCAN AND DIRECT READ.`
4. `CONTENT DISTINCTNESS ACROSS AN ENTIRE COHORT PROVES THAT THE COHORT IS NOT A BULK BYTE-COPY DUPLICATION PHENOMENON; IT DOES NOT ASSIGN RECORD OWNERSHIP.`
5. `DYNAMIC COHORT MEMBERSHIP SHOULD BE DERIVED FROM THE GOVERNING CLASSIFIER AND FAIL ON COUNT OR MEMBERSHIP DRIFT RATHER THAN FREEZING A HIDDEN ID LIST.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- no owner assignment;
- Internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, and REP-020 unchanged;
- six MIXED explicit-ID ambiguity groups remain separate and unsuppressed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- active indexed canonical uniqueness remains previously `CLOSED/PASS` and is not reopened;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Next legal action
The highest-value next bounded Priority-2 work is group-specific path-bound provenance authority review for the independently consumed groups `EJR-211`, `EJR-214`, `EJR-219`, `EJR-301`, and `EJR-302`. This means reviewing the authority and semantic role of the exact-path consumers and the competing sibling records before any identity decision. Lease 202 itself authorizes no migration or owner assignment.
