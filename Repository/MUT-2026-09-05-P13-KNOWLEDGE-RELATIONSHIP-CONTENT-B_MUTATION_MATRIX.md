# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-9 VERIFIED / UNIT 10 CROSS-LAYER BRIDGE PREPARED / CANONICAL REP-014 FOLD PENDING`

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`CURRENT PHYSICAL IDENTITY > STALE HISTORICAL PATH`

`STRONGER VERIFIED EDGE > WEAKER DUPLICATE DOCUMENTARY EDGE`

`BRIDGE EVIDENCE != CANONICAL REGISTRATION`

`MATERIAL VALIDITY != TRANSACTION VALIDITY != CLOSURE VALIDITY`

## Completed verified units

| Unit | Scope | Applied HEAD | Exact-head result |
|---|---|---|---|
| 1 | discovery evidence + initial guard + Matrix | `b72b9537e4e52d844cfa7e8a95ef8392f756a386` | `4/4 SUCCESS` |
| 2 | KNW-006 scoped-authority repair | `eef346f8f80d7e135e920df2f7c0f234830b5373` | `4/4 SUCCESS` |
| 3 | KNW-007 baseline-scope repair | `40e5a1207145aed441eaddbf2ec8af702b8f6c42` | `4/4 SUCCESS` |
| 4 | KNW-008 traceability/retention repair | `1a1a59c50d55cca97824bd129fd41e11b652b1b2` | `4/4 SUCCESS` |
| 5 | KNW-010 maintenance/disposition repair | `eeb663ce44d58803c8caa8efbbce33fc00ef849b` | `4/4 SUCCESS` |
| 6 | REL-124..167 internal allocation-plan validation | `cb61f90ef856af682dbd85360b0a337f13b3bdb7` | `4/4 SUCCESS` |
| 7 | canonical internal Knowledge documentary graph + REP-020 manifest rebind | `005a0483d9db73da273032901c19d255138d2ab3` | `4/4 SUCCESS` |
| 8 | KNW-004/006/010 identity-migration residue repair | `2dbea92fc500b33e00ba3b7de18291400a220bd5` | `4/4 SUCCESS` |
| 9 | REL-168..206 cross-layer allocation-plan validation | `bb27b15deca2d268e067805e315250e3838a840b` | `4/4 SUCCESS` |

## Unit 9 verified result

Direct current `Related Documents` review plus target identity reads established exactly 39 missing documentary candidates after excluding five already-represented stronger/equivalent seams:

- `KNW-002 → MOD-011 = CONSUMES` (`REL-010`)
- `KNW-003 → MOD-011 = REFERENCES` (`REL-110`)
- `KNW-004 → MOD-001 = REFERENCES` (`REL-081`)
- `KNW-004 → MOD-011 = REFERENCES` (`REL-111`)
- `KNW-009 → MOD-011 = CONSUMES` (`REL-014`)

Unit 9 proved:

- exactly 39 unique source-target-type rows;
- contiguous vacant IDs `REL-168..REL-206`;
- every row is `REFERENCES`;
- every source directly names the exact current target path;
- every target path exists and matches the planned Document ID;
- no stronger existing seam is duplicated;
- no endpoint maturity/status promotion or reverse edge inference.

## Unit 10 — cross-layer registration bridge

The available GitHub mutation surface currently supports whole-file replacement for existing text files but does not provide safe patch-in-place mutation. REP-014 is a long historical registry with prior content-preservation regressions; therefore Unit 10 must not risk rebuilding it from truncated retrieval.

Repository precedent `REP-020_RELATIONSHIP_ADDENDUM_2026-08-15_P73.md` explicitly allows a temporary auditable relationship addendum while canonical REP-014 synchronization remains pending.

Authorized exactly three paths:

1. `Repository/REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_REGISTRATION_BRIDGE_2026-09-05_D.md`
2. `Quality/Integrity/test_knowledge_p13_cross_layer_registration_bridge.py`
3. this Matrix.

Unit-10 bridge contract:

- preserve exactly the already-verified REL-168..206 allocation and source/target identities;
- classify all 39 entries as documentary `REFERENCES` only;
- explicitly state that the bridge is subordinate to REP-014 and is not canonical registration;
- preserve REP-014 at current v1.2.21 and keep REL-168..206 absent from canonical registry until a safe full-preservation fold is possible;
- keep the current REP-020 manifest bound to REP-014 v1.2.21; no false rebind occurs in Unit 10;
- executable guard must fail if the bridge is interpreted as canonical registration, if any stronger relationship type appears, or if REP-014 silently contains only a partial subset;
- no source artifact mutation and no active-index admission in Unit 10.

Expected Unit-10 change-set: `1 commit / exactly 3 files`.

## Current control-plane debts discovered during P13

Independent from relationship semantics:

- `REP-013` still shows an old five-file Knowledge subset and does not represent the exact 50-leaf physical inventory established by Transaction A;
- `REP-002` does not yet contain an exact reconciled Knowledge physical section;
- `REP-012` has the generic allocation registry and P13 exact-allocation evidence exists separately; whether the canonical REP-012 body needs mutation remains to be determined from current allocation semantics;
- historical P2 classification intentionally kept KNW-001..010 out of REP-001 active canonical admission while Knowledge remained domain-hold;
- support leaves under `Knowledge/Learning`, `Knowledge/Programming`, and `Knowledge/Mathematics` are physical/support artifacts and must not be promoted merely by inventory reconciliation.

## Remaining connected chain

1. Apply Unit 10 bridge and exact-head 4/4.
2. Continue exact Knowledge control-plane reconciliation: determine the smallest safe canonical/addendum updates for REP-013, REP-002 and REP-012 without semantic promotion.
3. Re-read `Knowledge/_FOLDER_STATUS.md` and historical P2 active-index hold after inventory/control-plane reconciliation; only then decide whether KNW-001..010 are eligible for REP-001 active admission.
4. Safely fold REL-168..206 into full REP-014 when a complete content-preserving mutation surface is available; same-change-set rebind the current REP-020 manifest and exact-head validate 4/4.
5. Reconcile REP-016/current manifest only when the material state justifies a new P13 queue/status boundary.
6. Transaction-B closure remains separate: last material head 4/4 → Matrix-only closure → closure-head 4/4.
7. Priority-13 partition closure remains a bounded later decision and does not imply Phase-1 or Global Integrity closure.

## Explicit non-claims

- no Priority-13 closure;
- no Knowledge active-index admission yet;
- no canonical REP-014 registration from Unit 10 bridge alone;
- no dependency/consumer/governance semantics from Related Documents;
- no automatic support-leaf promotion;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix
