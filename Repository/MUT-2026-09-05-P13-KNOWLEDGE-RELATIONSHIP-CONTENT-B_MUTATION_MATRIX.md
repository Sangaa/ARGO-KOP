# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-5 VERIFIED / UNIT 6 INTERNAL-RELATIONSHIP ALLOCATION PLAN PREPARED`

## Entry condition

Transaction A exact physical allocation is `CLOSED / VERIFIED / RESUME-SAFE`. Priority 13 remains open for identity, authority, content, dependency, consumer, relationship and control-plane reconciliation.

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`MATERIAL VALIDITY != TRANSACTION VALIDITY != CLOSURE VALIDITY`

## Stable registry rows retained from prior review

- `REL-010 KNW-002 → MOD-011 = CONSUMES`
- `REL-014 KNW-009 → MOD-011 = CONSUMES`
- `REL-081 KNW-004 → MOD-001 = REFERENCES`
- `REL-110 KNW-003 → MOD-011 = REFERENCES`
- `REL-111 KNW-004 → MOD-011 = REFERENCES`

No duplicate or reverse relationship is manufactured from conceptual symmetry.

## Unit 1 — evidence/control baseline

Applied HEAD: `b72b9537e4e52d844cfa7e8a95ef8392f756a386`

Scope: immutable discovery TSV + evidence guard + Matrix.

Result: `1 commit / exactly 3 authorized files / 4/4 exact-head SUCCESS`.

The discovery snapshot records the four entry content contradictions and direct-source relationship candidates. Later repairs do not rewrite the fact that the contradictions existed at entry.

## Unit 2 — KNW-006 scoped-authority repair

Applied HEAD: `eef346f8f80d7e135e920df2f7c0f234830b5373`

Result: `1 commit / exactly 3 authorized files / 4/4 exact-head SUCCESS`.

Repair: removed repository-absolute authority; authority now remains governed by scope, ownership, evidence, publication/promotion state and higher applicable authority. KNW-006 remains `Integrity Hold / Revalidated`, version `1.1.1`.

## Unit 3 — KNW-007 baseline-scope repair

Applied HEAD: `40e5a1207145aed441eaddbf2ec8af702b8f6c42`

Result: `1 commit / exactly 3 authorized files / 4/4 exact-head SUCCESS`.

Repair: platform baseline is governed canonical `PLATFORM` knowledge, not all repository-held/approved knowledge. Contextual scopes remain separately attributable absent explicit promotion. KNW-007 remains `Integrity Hold / Revalidated`, version `1.1.1`.

## Unit 4 — KNW-008 traceability/retention repair

Applied HEAD: `1a1a59c50d55cca97824bd129fd41e11b652b1b2`

Result: `1 commit / exactly 3 authorized files / 4/4 exact-head SUCCESS`.

Repair: unlimited complete-history and never-delete absolutes replaced by sufficient material traceability plus governed proportional retention; removal may not erase contradictory evidence or required provenance. KNW-008 remains `Integrity Hold / Revalidated`, version `1.1.1`.

## Unit 5 — KNW-010 maintenance/disposition repair

Applied HEAD: `eeb663ce44d58803c8caa8efbbce33fc00ef849b`

Result: `1 commit / exactly 3 authorized files / 4/4 exact-head SUCCESS`.

Repair: removed permanent immunity of Approved Knowledge; governed correction, supersession, reclassification, archival or removal is allowed only under applicable authority while preserving required provenance, contradictory evidence and retention obligations. Stable semantic invariants:

`APPROVED != IMMUTABLE`

`CANONICAL != SACRED`

`REMOVAL != ERASURE OF REQUIRED EVIDENCE`

KNW-010 remains `Integrity Hold / Revalidated`, version `1.1.1`.

## Post-repair content sweep

Direct re-read/search after Unit 5 found no additional contradiction of the same repository-absolute / baseline-absolute / never-delete class.

The current Knowledge README still correctly preserves scoped validation and does not make the repository an automatic truth store.

Control-plane review discovered separate deferred debts:

- REP-013 still shows an old five-file Knowledge subset rather than the exact 50-leaf inventory;
- REP-002 has no reconciled exact Knowledge section yet;
- REP-001 intentionally withheld KNW-001..010 from active canonical admission under the earlier P2 domain-hold classification.

Those are not repaired in Unit 6 because relationship registration and domain admission must remain separate decisions.

## Unit 6 — internal Knowledge relationship allocation plan

Current REP-014 ends at `REL-123`. Direct current-source review of `KNW-001..010` establishes exactly 44 unique KNW→KNW documentary `Related Documents` edges not currently present in REP-014.

Unit 6 authorizes exactly three paths:

1. `Repository/REP-014_PRIORITY13_KNOWLEDGE_INTERNAL_RELATIONSHIP_ALLOCATION_PLAN_2026-09-05_B.tsv`
2. `Quality/Integrity/test_knowledge_p13_internal_relationship_allocation_plan.py`
3. this Matrix.

The plan reserves exactly `REL-124..REL-167` in deterministic source-order and classifies every row as:

`REFERENCES / DIRECT_RELATED_DOCUMENTS / P13_INTERNAL_KNOWLEDGE_DOCUMENTARY_NON_DEPENDENCY`

Unit 6 is validation-first only. It does **not** mutate REP-014.

The guard must prove before registration:

- 44 rows exactly;
- contiguous IDs `REL-124..REL-167`;
- no ID collision in current REP-014;
- no existing duplicate source-target-type row;
- every target filename is directly named by the current source artifact;
- every planned type is `REFERENCES`;
- no `DEPENDS_ON`, `CONSUMES`, `GOVERNS` or `OWNS` promotion is manufactured.

After Unit-6 exact-head 4/4, canonical registry insertion may proceed only in a separate material unit with same-change-set REP-020 rebinding for the REP-014 version change.

## Planned continuation

1. Unit 6 allocation-plan validation → exact-head 4/4.
2. Register `REL-124..REL-167` in REP-014 + update registration guard + same-change-set REP-020 rebind → exact-head 4/4.
3. Re-read cross-layer candidate targets (Memory / Engine / Repository / Architecture / Core / Lifecycle) and classify direct reference vs stronger semantic contract without automatic reverse edges.
4. Reconcile exact Knowledge physical inventory into REP-013/REP-002/REP-012 as current evidence requires.
5. Review active-index admission for KNW-001..010 only after relationship/content/domain-hold conditions are satisfied; indexing must not imply Global Integrity or broader platform authority.
6. Synchronize Knowledge status + REP-016/REP-020 only after material completion supports it.
7. Closure review remains separate; any Transaction-B closure must be Matrix-only followed by closure-head 4/4.

## Explicit non-claims

- no Priority-13 closure;
- no active-index admission yet;
- no relationship insertion from Unit 6 alone;
- no canonical promotion of Learning/Programming/Mathematics support leaves;
- no cross-layer dependency/consumer certification;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix
