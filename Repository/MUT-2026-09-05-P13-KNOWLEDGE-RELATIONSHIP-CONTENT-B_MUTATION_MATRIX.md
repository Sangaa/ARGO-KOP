# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-6 VERIFIED / UNIT 7 INTERNAL RELATIONSHIP REGISTRATION PREPARED`

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`MATERIAL VALIDITY != TRANSACTION VALIDITY != CLOSURE VALIDITY`

## Completed verified units

| Unit | Scope | Applied HEAD | Exact-head result |
|---|---|---|---|
| 1 | discovery evidence + initial guard + Matrix | `b72b9537e4e52d844cfa7e8a95ef8392f756a386` | `4/4 SUCCESS` |
| 2 | KNW-006 scoped-authority repair | `eef346f8f80d7e135e920df2f7c0f234830b5373` | `4/4 SUCCESS` |
| 3 | KNW-007 baseline-scope repair | `40e5a1207145aed441eaddbf2ec8af702b8f6c42` | `4/4 SUCCESS` |
| 4 | KNW-008 traceability/retention repair | `1a1a59c50d55cca97824bd129fd41e11b652b1b2` | `4/4 SUCCESS` |
| 5 | KNW-010 maintenance/disposition repair | `eeb663ce44d58803c8caa8efbbce33fc00ef849b` | `4/4 SUCCESS` |
| 6 | REL-124..167 allocation-plan validation | `cb61f90ef856af682dbd85360b0a337f13b3bdb7` | `4/4 SUCCESS` |

Unit-6 compare: `1 commit / exactly 3 authorized files`.

Unit 6 proved before canonical registration:

- exactly 44 unique KNW→KNW rows;
- contiguous vacant IDs `REL-124..REL-167`;
- no current duplicate source-target-type row;
- every target filename directly appears in the current source artifact;
- every row type is `REFERENCES`;
- no dependency/consumption/governance/ownership promotion.

## Unit 7 — canonical internal Knowledge relationship registration

Authorized exactly four paths:

1. `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
2. `Quality/Integrity/test_knowledge_p13_internal_relationship_allocation_plan.py`
3. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
4. this Matrix.

Repair/registration contract:

- bump REP-014 only `1.2.20 → 1.2.21`;
- register exactly `REL-124..REL-167` from the already-validated Unit-6 plan;
- classify every row `REFERENCES / P13 DIRECT-SOURCE-REVALIDATED / INTERNAL DOCUMENTARY / NON-DEPENDENCY`;
- preserve all pre-existing REL-001..123 rows and historical reconciliation prose;
- add a bounded P13 registry section that states internal documentary graph is not dependency/authority/closure proof;
- convert the Unit-6 guard from pre-registration vacancy assertions to post-registration exact-presence assertions;
- rebind `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` in the same change-set to REP-014 v1.2.21;
- keep REP-020 impact matrix v0.2.3 unchanged because it is not the current control-plane version/status binding surface;
- do not mutate Knowledge source artifacts in Unit 7;
- do not admit KNW artifacts to REP-001 active canonical inventory in Unit 7.

Expected Unit-7 change-set: `1 commit / exactly 4 files`.

## Remaining connected P13 chain after Unit 7

1. Re-read cross-layer direct candidates from KNW-001..010 against current target semantics; register only source-derived and non-duplicate relationships, separating documentary reference from dependency/consumer/authority semantics.
2. Reconcile exact 50-leaf Knowledge physical inventory into REP-013 and REP-002, with allocation-state evidence in REP-012 as required; physical mapping must not promote support leaves.
3. Re-evaluate the historical P2 `DECLARED-CANONICAL-BUT-DOMAIN-HOLD` disposition for KNW-001..010 only after relationship/content/control-plane reconciliation is materially complete.
4. Synchronize `Knowledge/_FOLDER_STATUS.md`, REP-016 and the current REP-020 manifest only when the material state justifies a new queue/status boundary.
5. Transaction-B closure, if earned, must be a Matrix-only closure commit followed by closure-head exact 4/4.
6. Priority-13/partition closure remains a separate decision after downstream consumer/dependency and index admission review.

## Explicit non-claims

- no Priority-13 closure;
- no Knowledge active-index admission yet;
- no automatic promotion of Learning/Programming/Mathematics support leaves;
- no cross-layer dependency/consumer certification from internal references;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix