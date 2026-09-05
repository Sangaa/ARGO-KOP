# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP / CONTENT B

Transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Priority: `13 — Knowledge`
Entry HEAD: `0beaff41db190cecc757f0d169a5d7174c1578d2`
State: `OPEN / UNITS 1-7 VERIFIED / UNIT 8 KNOWLEDGE IDENTITY-MIGRATION RESIDUE REPAIR PREPARED`

## Governing invariants

`REFERENCE != DEPENDENCY != AUTHORITY TRANSFER`

`RELATED DOCUMENTS != AUTOMATIC CONSUMPTION OR GOVERNANCE`

`CURRENT PHYSICAL IDENTITY > STALE HISTORICAL PATH`

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
| 7 | canonical internal Knowledge documentary graph + REP-020 current-manifest rebind | `005a0483d9db73da273032901c19d255138d2ab3` | `4/4 SUCCESS` |

Unit 7 compare: `1 commit / exactly 4 authorized files`; REP-014 advanced `1.2.20 → 1.2.21`, registered exactly REL-124..167, and retained the broader graph/closure hold.

## Cross-layer scan finding after Unit 7

A direct current-source scan found a homogeneous identity-migration residue class before any new cross-layer registry insertion:

1. `KNW-004` still described `GOV-005` as document-artifact lifecycle authority even though current `GOV-005` is the Review Standard and the document lifecycle identity is `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`.
2. `KNW-006` still referenced retired/non-current `Governance/GOV-006_REVIEW_STANDARD.md`; current Review Standard is `Governance/GOV-005_REVIEW_STANDARD.md`, while GOV-006 is the Naming Convention Standard.
3. `KNW-010` still referenced historical physical path `Repository/REP-010_REPOSITORY_MAINTENANCE.md`; current REP-010 physical identity is `Repository/REP-010_RELEASE_BASELINE.md`. Current REP-010 still has internal Document ID `REP-010` and content title `REPOSITORY MAINTENANCE`; the known title/path coherence gap remains a separate repository concern.

This residue must be repaired before relationship registration so the graph does not canonize stale identities.

## Unit 8 — Knowledge identity-migration residue repair

Authorized exactly five paths:

1. `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
2. `Knowledge/KNW-006_KNOWLEDGE_QUALITY.md`
3. `Knowledge/KNW-010_KNOWLEDGE_MAINTENANCE.md`
4. `Quality/Integrity/test_knowledge_p13_identity_migration_residue.py`
5. this Matrix.

Repair contract:

- KNW-004 `1.3.1 → 1.3.2`: identify `LIF-001` as document-artifact lifecycle; identify GOV-005 only as review authority; do not merge lifecycle and review authority.
- KNW-006 `1.1.1 → 1.1.2`: replace stale GOV-006 Review Standard path with current GOV-005 Review Standard path; no stronger relationship semantics implied.
- KNW-010 `1.1.1 → 1.1.2`: replace stale REP-010 physical filename with current `REP-010_RELEASE_BASELINE.md`; preserve REP-010's known title/path coherence gap as separate and unresolved.
- preserve all three artifacts at `Integrity Hold / Revalidated`; no maturity promotion.
- executable guard must fail if any of the three stale identity strings reappears.
- no REP-014 mutation in Unit 8; relationship registration waits for source identity repair plus exact-head validation.

Expected Unit-8 change-set: `1 commit / exactly 5 files`.

## Remaining connected chain

1. Validate Unit 8 exact-head 4/4.
2. Re-run cross-layer candidate classification against repaired source identities and current REP-014; preserve stronger existing edges such as KNW-002→MOD-011 and KNW-009→MOD-011 instead of adding weaker duplicate REFERENCES.
3. Create validation-first allocation plan for only missing cross-layer edges that survive direct target/authority review.
4. Register bounded cross-layer cohort with REP-014 version bump + same-change-set current-manifest rebind.
5. Reconcile exact 50-leaf Knowledge physical inventory into REP-013/REP-002 and allocation evidence as required, without promoting support leaves.
6. Re-evaluate historical Knowledge active-index hold only after relationship/content/control-plane reconciliation actually resolves its conditions.
7. Closure remains separate and requires exact-head 4/4, Matrix-only closure, then closure-head 4/4.

## Explicit non-claims

- no Priority-13 closure;
- no Knowledge active-index admission yet;
- no automatic promotion of Learning/Programming/Mathematics support leaves;
- no graph edge from a stale or merely historical path;
- no Phase-1 or Global Integrity closure.

---

End of Transaction-B Matrix