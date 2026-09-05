# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-10 VERIFIED / UNIT 11 CONTROL-PLANE RECONCILIATION PLAN PREPARED`

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`CURRENT PHYSICAL IDENTITY > STALE HISTORICAL PATH`

`STRONGER VERIFIED EDGE > WEAKER DUPLICATE DOCUMENTARY EDGE`

`BRIDGE EVIDENCE != CANONICAL REGISTRATION`

`PHYSICAL INVENTORY != ACTIVE INDEX ADMISSION`

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
| 10 | verified cross-layer relationship bridge / canonical REP-014 fold explicitly pending | `b25e3b29239c356bd42c879787e4874bb82df7ec` | `4/4 SUCCESS` |

## Unit 10 bounded result

The verified REL-168..206 cohort is preserved in:

`Repository/REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_REGISTRATION_BRIDGE_2026-09-05_D.md`

This is intentionally a temporary auditable bridge under the established P73 precedent because the current GitHub mutation surface exposes whole-file replacement but not safe patch-in-place for the long REP-014 artifact.

The bridge does **not** alter REP-014 v1.2.21, does not rebind REP-020, and does not claim canonical relationship synchronization. The Unit-10 executable guard enforces that distinction.

## Control-plane reconciliation finding

Priority-12 Models precedent establishes that exact allocation is not fully synchronized merely by keeping an independent exact-inventory TSV. Models exact allocation updated REP-002, REP-012 and REP-013 and bound a path-level allocation manifest.

Priority-13 Transaction A correctly established the exact current Knowledge tree but intentionally stopped after status + immutable inventory evidence. Current re-read therefore finds four different states:

1. `REP-013 v1.1.6` — its `### Knowledge/` content tree remains an old five-file subset and lacks the exact 50-leaf digest.
2. `REP-002 v1.7.8` — no exact Priority-13 Knowledge physical-map binding exists.
3. `REP-012 v1.0.13` — the canonical allocation registry does not yet bind Transaction-A's exact 50-leaf inventory/digest.
4. `REP-001 v1.7.8` — KNW-001..010 active admission remains intentionally held under the historical P2 authority-aware classification; this is a separate semantic admission decision, not a physical-inventory defect.

Exact Priority-13 physical truth remains:

- tracked leaves: `50`;
- sorted-path SHA-256: `8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7`;
- evidence: `Repository/MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv`;
- canonical Knowledge artifact set remains only `KNW-001..010` as declared by `Knowledge/README.md`; support/evidence/executable/test leaves receive no authority from mapping.

## Unit 11 — control-plane reconciliation-plan validation

Authorized exactly three paths:

1. `Repository/P13_KNOWLEDGE_CONTROL_PLANE_RECONCILIATION_PLAN_2026-09-05_E.tsv`
2. `Quality/Integrity/test_knowledge_p13_control_plane_reconciliation_plan.py`
3. this Matrix.

Unit-11 validation contract:

- prove Transaction-A TSV still contains exactly 50 unique paths and recomputes the recorded digest;
- prove Knowledge status still binds the same count/digest;
- prove REP-013 is currently stale in the specific old-subset way and is not silently treated as synchronized;
- prove REP-002 has no current exact P13 Knowledge digest/map binding;
- prove REP-012 has no canonical binding to the P13 Transaction-A inventory/digest;
- preserve REP-001 active-admission hold as a separate decision;
- prohibit any inference that physical mapping/allocation closes Priority 13 or promotes support leaves.

Expected Unit-11 change-set: `1 commit / exactly 3 files`.

## Remaining connected chain

1. Validate Unit 11 exact-head 4/4.
2. Build the smallest content-preserving synchronization units for REP-013, REP-002 and REP-012. If safe canonical whole-file mutation is unavailable, use explicit temporary addenda/bridges and keep canonical synchronization OPEN rather than abbreviating historical files.
3. Re-read `Knowledge/_FOLDER_STATUS.md` after those units and replace obsolete “work not started” language with exact remaining blockers only.
4. Re-evaluate historical P2 `DECLARED-CANONICAL-BUT-DOMAIN-HOLD` disposition for KNW-001..010 only after relationship/content/control-plane blockers are materially resolved; REP-001 admission remains separate from mapping.
5. Safely fold REL-168..206 into full REP-014; same-change-set rebind current REP-020 manifest; exact-head 4/4.
6. Reconcile REP-016/current manifest only when the material state justifies a new P13 boundary.
7. Transaction-B closure remains separate: last material head 4/4 → Matrix-only closure → closure-head 4/4.
8. Priority-13 partition closure remains bounded and does not imply Phase-1 or Global Integrity closure.

## Explicit non-claims

- no Priority-13 closure;
- no Knowledge active-index admission yet;
- no canonical REP-014 cross-layer registration from the bridge alone;
- no canonical REP-002/012/013 synchronization from Unit 11 planning alone;
- no dependency/consumer/governance semantics from Related Documents;
- no automatic support-leaf promotion;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix
