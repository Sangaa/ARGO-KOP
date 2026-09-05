# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-2 VERIFIED / UNIT 3 KNW-007 BASELINE-SCOPE REPAIR PREPARED`

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

Entry contradiction: `Repository always prevails.`

Disposition: repaired in Unit 2 by binding authority to governed scope/ownership/evidence/publication state while retaining higher authority and contextual attribution.

### KNW-007

The entry wording treats approved repository knowledge broadly as the baseline/authoritative body.

Conflict: current scope model requires a distinction between platform canonical knowledge and contextual repository-held knowledge. Repository storage/approval does not itself make every item platform baseline authority.

### KNW-008

Absolute statements require complete history and say historical knowledge shall never be deleted.

Conflict: KNW-009 explicitly allows governed deletion and requires retention proportional to traceability, legal, security and operational need while forbidding deletion used to conceal contradictory evidence.

### KNW-010

Absolute maintenance rule: `Delete Approved Knowledge` is never allowed.

Conflict: KNW-009 makes authority/evidence reviewable and allows governed removal with appropriate historical/provenance protection.

## Unit 1 — evidence/control baseline

Authorized exactly three new paths:

1. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_EVIDENCE.tsv`
2. `Quality/Integrity/test_knowledge_p13_relationship_content_evidence.py`
3. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_MUTATION_MATRIX.md`

Applied HEAD: `b72b9537e4e52d844cfa7e8a95ef8392f756a386`

Entry → Unit-1 compare: `1 commit / exactly 3 authorized files / no Knowledge source mutation`.

Exact-head four-family result: `4/4 SUCCESS`.

The Unit-1 TSV is retained as an immutable discovery snapshot. Later repairs do not rewrite the fact that the contradiction existed at the entry checkpoint.

## Unit 2 — KNW-006 scoped authority repair

Authorized exactly three paths:

1. `Knowledge/KNW-006_KNOWLEDGE_QUALITY.md`
2. `Quality/Integrity/test_knowledge_p13_knw006_authority_scope.py`
3. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_MUTATION_MATRIX.md`

Applied HEAD: `eef346f8f80d7e135e920df2f7c0f234830b5373`

Unit-2 compare: `1 commit / exactly 3 authorized files`.

Exact-head four-family result: `4/4 SUCCESS`.

Repair result:

- obsolete repository-absolute authority removed;
- authority now scope/ownership/evidence/publication bounded;
- higher Core/Governance/Architecture/Repository-control authority preserved;
- user/project/deployment attribution and non-silent-overwrite preserved;
- KNW-006 remains `Integrity Hold / Revalidated` at `1.1.1`.

## Unit 3 — KNW-007 baseline-scope repair

Authorized exactly three paths:

1. `Knowledge/KNW-007_KNOWLEDGE_BASELINE.md`
2. `Quality/Integrity/test_knowledge_p13_knw007_baseline_scope.py`
3. `Repository/MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_MUTATION_MATRIX.md`

Repair contract:

- define the baseline as governed canonical `PLATFORM` knowledge, not all approved repository knowledge;
- make repository location/approval/local validation insufficient by itself for baseline membership;
- preserve user/project/deployment attribution until explicit governed promotion/reclassification;
- keep Knowledge baseline subordinate to higher authority contracts;
- make project knowledge a possible evidence/candidate source rather than automatic platform baseline content;
- retain KNW-007 under `Integrity Hold / Revalidated` and bump only `1.1.0 → 1.1.1` for the semantic correction.

No REP-014/016/020 mutation is authorized by Unit 3.

## Planned material sequence

1. Evidence Unit 1 — COMPLETE / 4/4.
2. KNW-006 authority repair — COMPLETE / 4/4.
3. KNW-007 baseline-scope repair — exact-head validation pending.
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
