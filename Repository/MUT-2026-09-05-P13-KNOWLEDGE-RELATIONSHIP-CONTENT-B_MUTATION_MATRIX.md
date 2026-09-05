# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / EVIDENCE UNIT 1 PREPARED / SOURCE REPAIRS PENDING`

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

## Content contradictions requiring repair

### KNW-006

Absolute statement: `Repository always prevails.`

Conflict: current KNW-001/002/005/009 distinguish repository location, declared scope, ownership, evidence and canonical authority. Repository presence or a transient repository representation does not automatically override user/project/deployment ownership or higher authority layers.

### KNW-007

The old baseline wording treats approved repository knowledge broadly as the baseline/authoritative body.

Conflict: current scope model requires a distinction between platform canonical knowledge and contextual repository-held knowledge. Repository storage/approval does not itself make every item platform baseline authority.

### KNW-008

Absolute statements require complete history and say historical knowledge shall never be deleted.

Conflict: KNW-009 explicitly allows governed deletion and requires retention proportional to traceability, legal, security and operational need while forbidding deletion used to conceal contradictory evidence.

### KNW-010

Absolute maintenance rule: `Delete Approved Knowledge` is never allowed.

Conflict: KNW-009 makes authority/evidence reviewable and allows governed removal with appropriate historical/provenance protection.

## Unit 1 authorization

Exactly three new evidence/control paths are authorized:

1. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_EVIDENCE.tsv`
2. `Quality/Integrity/test_knowledge_p13_relationship_content_evidence.py`
3. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_MUTATION_MATRIX.md`

Unit 1 changes no Knowledge source artifact and no relationship registry row. Its purpose is to make the discovered contradictions and candidate relationships executable review evidence before repairs.

## Planned material sequence

1. Evidence Unit 1 → exact-head 4/4.
2. Repair KNW-006 scoped authority wording → exact-head 4/4.
3. Repair KNW-007 baseline scope/authority wording → exact-head 4/4.
4. Repair KNW-008 traceability/retention absolutes → exact-head 4/4.
5. Repair KNW-010 maintenance/deletion absolute → exact-head 4/4.
6. Re-read all KNW-001..010 after repairs and evaluate remaining identity/content drift.
7. Validate candidate relationship targets/consumer semantics.
8. Register only non-duplicate relationships whose source, target, type and direction survive direct review; any REP-014 version change requires same-change-set REP-020 rebinding.
9. Reconcile status/queue only after material relationship/content state actually advances.
10. Closure review remains separate from material validity.

## Non-claims

- no Priority-13 closure;
- no automatic status promotion for KNW-006/007/008/010;
- no relationship insertion from Related Documents alone;
- no promotion of Learning/Programming/Mathematics support leaves;
- no Knowledge ↔ Memory or Knowledge ↔ Engine executable certification;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix
