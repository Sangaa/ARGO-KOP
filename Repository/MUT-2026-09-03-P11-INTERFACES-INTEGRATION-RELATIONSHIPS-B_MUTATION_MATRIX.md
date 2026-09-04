# P11 Interfaces — Integration Relationship Registration — Transaction B

Transaction ID: `MUT-2026-09-03-P11-INTERFACES-INTEGRATION-RELATIONSHIPS-B`
Priority: `11 — Interfaces`
State: `SECOND STALE HISTORICAL CONSUMER REPAIR / EXACT-HEAD CI PENDING`
Entry HEAD: `62d39ed6ea423f820c224e73a9ada554c473b9ef`
Pre-write HEAD: `0c7c4d10aa91b28b0b3899251a8eb905b6189a32`
Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`
Corrective control-binding HEAD: `78420d9102d1216a9c5005951d92e2e4f5f0cbda`
First semantic-guard repair HEAD: `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-014 / REP-016`

## Legal entry and material gap

Transaction A is `CLOSED / VERIFIED / RESUME-SAFE`; the exact Interfaces inventory is not reopened. Entry `REP-014 v1.2.18` ended at material row `REL-072` and contained no `INTF-*` relationship rows. `Interfaces/INTF-010_INTEGRATIONS.md` directly states that it implements the integration boundary described by `INTF-001`, `INTF-004`, `INTF-005`, `INTF-006`, `ARC-007`, `ARC-006`, `ENG-007`, and `MEM-001`. Current source reads confirmed those targets and resolved `INTF-006` to active canonical `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`, not legacy `INT-006`.

The Priority-9 relationship disposition records a historical proposed `REL-073: ARC-001 → ARC-011 = REFERENCES`, but explicitly states `BASE REGISTRY UNCHANGED`, `No row is added`, and `DO NOT PROMOTE`. Therefore that historical proposal is a non-material candidate label, not a material REP-014 registry row. The P9 safety invariant is the continued absence of the prohibited `ARC-001 → ARC-011 = REFERENCES` row while its hold remains active; the invariant is not the permanent absence of the lexical token `REL-073` from REP-014.

## Relationship matrix

| Candidate | Source | Target | Current identity | Source authority | Target authority | Type | Direction | Material state |
|---|---|---|---|---|---|---|---|---|
| REL-073 | INTF-010 | INTF-001 | canonical | direct INTF-010 implements statement | current INTF-001 | IMPLEMENTS | INTF-010 → INTF-001 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |
| REL-074 | INTF-010 | INTF-004 | canonical | direct INTF-010 implements statement | current INTF-004 | IMPLEMENTS | INTF-010 → INTF-004 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |
| REL-075 | INTF-010 | INTF-005 | canonical | direct INTF-010 implements statement | current INTF-005 | IMPLEMENTS | INTF-010 → INTF-005 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |
| REL-076 | INTF-010 | INTF-006 | active canonical `INTF-006_ENVIRONMENT_SENSING.md` | direct INTF-010 implements statement | current INTF-006 | IMPLEMENTS | INTF-010 → INTF-006 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / ACTIVE-INTF-006 / NON-EXECUTABLE |
| REL-077 | INTF-010 | ARC-007 | canonical/current | direct INTF-010 implements statement | current ARC-007 | IMPLEMENTS | INTF-010 → ARC-007 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |
| REL-078 | INTF-010 | ARC-006 | canonical/current | direct INTF-010 implements statement | current ARC-006 | IMPLEMENTS | INTF-010 → ARC-006 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE / NON-DEPENDENCY |
| REL-079 | INTF-010 | ENG-007 | current Engine artifact | direct INTF-010 implements statement | current ENG-007 | IMPLEMENTS | INTF-010 → ENG-007 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |
| REL-080 | INTF-010 | MEM-001 | current Memory artifact | direct INTF-010 implements statement | current MEM-001 | IMPLEMENTS | INTF-010 → MEM-001 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE |

## Material result

- `REP-014 1.2.18 → 1.2.19` registered only `REL-073..REL-080` plus the bounded P11 evidence section.
- Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`.
- Immutable read-back: `REP-014` blob `39c4aa4fccdc7ff391b0812735ec3c2356113165` contains all eight intended rows.
- No corrective semantic-guard commit is authorized to modify REP-014 material.

## Preserved atomicity failure

Initial material exact-head Full-Stack run `33787517479` failed only at `Enforce Mutation Matrix on current change set`: `protected_changes=1 / mutation_matrices=0`. Classification: `TRANSACTION ATOMICITY / CONTROL-PLANE FAILURE`.

The corrective control-binding commit `78420d9102d1216a9c5005951d92e2e4f5f0cbda` restored the Matrix/evidence binding without changing valid relationship semantics.

## First stale historical consumer

The first tracked Runtime/Integration failure was `Quality/Integration/test_architecture_p9_repository_reconciliation.py`, which encoded the historical P9 hold as `assert "| REL-073 |" not in base`. That consumer was stale once P11 legally allocated material ID `REL-073` to an unrelated Interface relationship.

Safety invariant:

`P9 ARC-001 → ARC-011 = REFERENCES MUST remain absent from material REP-014 while the P9 local hold remains active.`

First repair at `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8` changed the consumer to:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in base`

No REP-014 rewrite occurred.

## Second stale historical consumer

After the first repair, exact-head Runtime/Integration remained red. Exact source inventory identified `Quality/Integration/test_architecture_p9_status_sync.py` as a second P9 consumer carrying the same obsolete identifier assumption. Its `test_local_rel073_hold_remains_unpromoted_and_nonblocking` correctly verifies the historical decision/disposition/abort evidence, but its final guard is:

`assert "| REL-073 |" not in registry`

Governing evidence proves:

- historical proposed P9 relation = `ARC-001 → ARC-011 = REFERENCES`;
- P9 disposition = `BASE REGISTRY UNCHANGED / No row is added / DO NOT PROMOTE`;
- current material `REL-073` = `INTF-010 → INTF-001 = IMPLEMENTS`;
- current REP-014 contains no `ARC-001 → ARC-011 = REFERENCES` row.

Classification: `SECOND STALE HISTORICAL CONSUMER / LEXICAL IDENTIFIER GUARD`.

Smallest governed repair:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in registry`

The new guard is ID-independent and therefore stronger with respect to the actual P9 safety invariant.

## Authorized corrective material set

| ID | Target | Action | Required result |
|---|---|---|---|
| P11-B-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | NO CHANGE / IMMUTABLE MATERIAL | retain `1.2.19`; REL-073..080 and blob `39c4aa4fccdc7ff391b0812735ec3c2356113165` |
| P11-B-02 | this Matrix | UPDATE | bind second stale-consumer evidence, semantic invariant and atomic corrective scope |
| P11-B-03 | `Repository/REP-011_PRIORITY11_INTERFACES_RELATIONSHIP_REGISTRATION_ADDENDUM_2026-09-03_B.md` | UPDATE | bind second consumer diagnosis and repair without relationship/priority promotion |
| P11-B-04 | `Quality/Integration/test_architecture_p9_status_sync.py` | UPDATE | replace only historical-ID lexical final guard with semantic prohibited-relationship guard |

The corrective commit MUST contain P11-B-02, P11-B-03 and P11-B-04 together. No Interface source artifact, implementation, provider configuration or credential mutation is authorized by Transaction B.

## Explicit semantic and trust boundaries

- `IMPLEMENTS` is documentary/contractual relationship evidence, not executable implementation proof.
- No `DEPENDS_ON`, `CONSUMES`, reverse edge, provider relationship, runtime reachability or authority transfer is inferred.
- Local documentary proof does not establish provider authenticity, authenticated provider identity, credentials, permission, remote read-back or production execution.
- Legacy `INT-006` remains distinct and is not targeted.
- P9 remains closed for its bounded partition; the deferred ARC-001→ARC-011 registry row remains unpromoted.
- P11 remains open until Transaction B earns exact-head closure and later connector/implementation evidence is assessed.

Validation: `atomic Matrix + REP-011 evidence + semantic guard → immutable read-back → parent/path proof → exact-head Full-Stack + Mutation Matrix + M2 + Runtime/Integration → close B only at 4/4 GREEN, otherwise HOLD / RESUME-SAFE`.
