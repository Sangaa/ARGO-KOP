# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-8 VERIFIED / UNIT 9 CROSS-LAYER ALLOCATION PLAN PREPARED`

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`CURRENT PHYSICAL IDENTITY > STALE HISTORICAL PATH`

`STRONGER VERIFIED EDGE > WEAKER DUPLICATE DOCUMENTARY EDGE`

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

Unit 8 corrected three stale source identities before graph registration:

- KNW-004 now distinguishes `LIF-001` document lifecycle from `GOV-005` review authority;
- KNW-006 uses current `GOV-005_REVIEW_STANDARD` instead of stale GOV-006 Review path;
- KNW-010 uses current REP-010 physical path `REP-010_RELEASE_BASELINE.md` while preserving the separate REP-010 title/path coherence gap.

## Cross-layer candidate classification

Direct current `Related Documents` review plus target identity reads establish 39 missing documentary candidates after excluding five already-represented stronger/equivalent seams.

Excluded existing seams:

- `KNW-002 → MOD-011 = CONSUMES` (`REL-010`)
- `KNW-003 → MOD-011 = REFERENCES` (`REL-110`)
- `KNW-004 → MOD-001 = REFERENCES` (`REL-081`)
- `KNW-004 → MOD-011 = REFERENCES` (`REL-111`)
- `KNW-009 → MOD-011 = CONSUMES` (`REL-014`)

The remaining unique targets were directly identity-checked across Memory, Engine, Repository, Architecture, Lifecycle, Governance and Core. Endpoint maturity varies and several remain Integrity Hold/Revalidation Required; therefore target existence/identity supports documentary registration only, not endpoint certification.

## Unit 9 — cross-layer allocation-plan validation

Authorized exactly three paths:

1. `Repository/REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_ALLOCATION_PLAN_2026-09-05_C.tsv`
2. `Quality/Integrity/test_knowledge_p13_cross_layer_allocation_plan.py`
3. this Matrix.

Allocation contract:

- reserve exactly contiguous vacant IDs `REL-168..REL-206`;
- exactly 39 unique source-target-type rows;
- every row type = `REFERENCES`;
- every row source must directly contain the exact current target path in its Related Documents declaration;
- every target path must exist and its internal Document ID must match the planned target identity;
- the five stronger/equivalent existing seams above must be absent from the plan;
- REP-014 remains unchanged in Unit 9; vacancy must be proven before registration;
- no endpoint maturity/status promotion and no reverse edge inference.

Expected Unit-9 change-set: `1 commit / exactly 3 files`.

## Remaining connected chain

1. Validate Unit 9 exact-head 4/4.
2. Register REL-168..206 in REP-014 only from the verified plan; bump REP-014 one patch version and same-change-set rebind the current REP-020 boundary manifest; convert the plan guard to exact post-registration assertions.
3. Reconcile exact 50-leaf Knowledge physical inventory into REP-013 and REP-002; determine whether REP-012 needs direct versioned mutation or whether the existing P13 allocation manifest already satisfies allocation evidence.
4. Re-read Knowledge/_FOLDER_STATUS and historical P2 active-index hold; update REP-001 only if current material evidence actually resolves domain-level admission conditions.
5. Reconcile REP-016/current manifest only when the material state justifies a new P13 boundary.
6. Transaction-B closure remains separate: last material head 4/4 → Matrix-only closure → closure-head 4/4.
7. Priority-13 partition closure remains a later bounded decision requiring downstream/consumer and active-index admission review.

## Explicit non-claims

- no Priority-13 closure;
- no Knowledge active-index admission yet;
- no dependency/consumer/governance semantics from Related Documents;
- no automatic support-leaf promotion;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix