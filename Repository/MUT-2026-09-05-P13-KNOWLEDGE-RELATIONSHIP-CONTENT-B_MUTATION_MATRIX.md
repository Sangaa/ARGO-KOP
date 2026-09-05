# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-4 VERIFIED / UNIT 5 KNW-010 MAINTENANCE-DISPOSITION REPAIR PREPARED`

## Entry condition

Transaction A exact physical allocation is closed and closure-head validated 4/4. Priority 13 remains open for identity, authority, content, dependency, consumer and relationship reconciliation.

## Direct-source findings

Current direct reads of `KNW-001..010` establish two different work classes that must not be conflated:

1. relationship evidence, where `Related Documents` is documentary evidence only unless a stronger semantic contract exists;
2. internal content contradictions, where older Knowledge artifacts contain absolute authority/retention statements incompatible with the newer scoped model.

Current KNW relationship semantics explicitly preserve:

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

and current lifecycle semantics explicitly state that a path/text reference alone is insufficient to prove a relationship.

## Stable registry rows retained

The current REP-014 registry already contains bounded direct-source relationships that remain valid at entry:

- `REL-010 KNW-002 → MOD-011 = CONSUMES`
- `REL-014 KNW-009 → MOD-011 = CONSUMES`
- `REL-081 KNW-004 → MOD-001 = REFERENCES`
- `REL-110 KNW-003 → MOD-011 = REFERENCES`
- `REL-111 KNW-004 → MOD-011 = REFERENCES`

No duplicate/reverse relationship is authorized merely to increase graph density.

## Content contradiction dispositions

### KNW-006

Entry contradiction: `Repository always prevails.`

Disposition: repaired in Unit 2 by binding authority to governed scope/ownership/evidence/publication state while retaining higher authority and contextual attribution.

### KNW-007

Entry contradiction: approved repository knowledge broadly treated as baseline/authoritative body.

Disposition: repaired in Unit 3 by restricting baseline membership to governed canonical `PLATFORM` knowledge and preserving contextual scopes outside the baseline absent explicit promotion.

### KNW-008

Entry contradiction: unlimited complete-history and never-delete rules.

Disposition: repaired in Unit 4 by using sufficient material traceability plus proportional governed retention, while prohibiting removal used to conceal contradictory evidence or break required provenance.

### KNW-010

Absolute maintenance rule at entry: `Delete Approved Knowledge` is never allowed.

Conflict: KNW-009 makes knowledge and its rules reviewable, explicitly allows governed disposition, and forbids only evidence-erasing or authority-bypassing removal rather than all deletion.

## Unit 1 — evidence/control baseline

Applied HEAD: `b72b9537e4e52d844cfa7e8a95ef8392f756a386`

Authorized exactly three evidence/control paths. Entry → Unit-1 compare: `1 commit / exactly 3 authorized files / no Knowledge source mutation`.

Exact-head four-family result: `4/4 SUCCESS`.

The Unit-1 TSV remains the immutable discovery snapshot.

## Unit 2 — KNW-006 scoped authority repair

Applied HEAD: `eef346f8f80d7e135e920df2f7c0f234830b5373`

Authorized exactly KNW-006 + dedicated guard + this Matrix.

Exact-head four-family result: `4/4 SUCCESS`.

KNW-006 remains `Integrity Hold / Revalidated` at `1.1.1`.

## Unit 3 — KNW-007 baseline-scope repair

Applied HEAD: `40e5a1207145aed441eaddbf2ec8af702b8f6c42`

Authorized exactly KNW-007 + dedicated guard + this Matrix.

Exact-head four-family result: `4/4 SUCCESS`.

KNW-007 remains `Integrity Hold / Revalidated` at `1.1.1`.

## Unit 4 — KNW-008 traceability / retention repair

Applied HEAD: `1a1a59c50d55cca97824bd129fd41e11b652b1b2`

Authorized exactly:

1. `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md`
2. `Quality/Integrity/test_knowledge_p13_knw008_retention_scope.py`
3. this Matrix.

Unit-4 compare: `1 commit / exactly 3 authorized files`.

Exact-head four-family result: `4/4 SUCCESS`.

Repair result:

- unlimited complete-history requirement removed;
- absolute never-delete rule removed;
- retention is governed and proportional;
- destructive deletion is not automatically prohibited;
- removal may not erase contradictory evidence, conceal failure or break required provenance;
- retained history does not become current authority by retention;
- KNW-008 remains `Integrity Hold / Revalidated` at `1.1.1`.

## Unit 5 — KNW-010 maintenance / disposition repair

Authorized exactly three paths:

1. `Knowledge/KNW-010_KNOWLEDGE_MAINTENANCE.md`
2. `Quality/Integrity/test_knowledge_p13_knw010_maintenance_disposition.py`
3. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_MUTATION_MATRIX.md`

Repair contract:

- remove the absolute prohibition on deleting Approved Knowledge;
- make approved/canonical knowledge reviewable, correctable, supersedable, reclassifiable, archivable or removable under applicable authority and impact/retention review;
- preserve required provenance, material traceability, contradictory evidence and failure lessons;
- preserve legal/security/confidentiality/retention obligations;
- prevent silent scope broadening or contextual overwrite;
- preserve repository-freeze authority rather than hard-code a universal maintenance exception set;
- state the stable semantic invariants `APPROVED != IMMUTABLE`, `CANONICAL != SACRED`, and `REMOVAL != ERASURE OF REQUIRED EVIDENCE`;
- retain KNW-010 under `Integrity Hold / Revalidated`, bumping only `1.1.0 → 1.1.1`.

No REP-014, REP-016, REP-020 or other KNW mutation is authorized by Unit 5.

## Planned material sequence

1. Evidence Unit 1 — COMPLETE / 4/4.
2. KNW-006 authority repair — COMPLETE / 4/4.
3. KNW-007 baseline-scope repair — COMPLETE / 4/4.
4. KNW-008 traceability/retention repair — COMPLETE / 4/4.
5. KNW-010 maintenance/disposition repair — exact-head validation pending.
6. Re-read all `KNW-001..010` after repairs and evaluate remaining identity/content drift.
7. Validate candidate relationship targets/consumer semantics and executable Learning boundaries.
8. Register only non-duplicate relationships whose source, target, type and direction survive direct review; any REP-014 version change requires same-change-set REP-020 rebinding.
9. Reconcile status/queue only after material relationship/content state actually advances.
10. Closure review remains separate from material validity.

## Non-claims

- no Priority-13 closure;
- no automatic maturity promotion for repaired KNW artifacts;
- no relationship insertion from Related Documents alone;
- no promotion of Learning/Programming/Mathematics support leaves;
- no Knowledge ↔ Memory or Knowledge ↔ Engine executable certification;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix
