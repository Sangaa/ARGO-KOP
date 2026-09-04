# P11 Interfaces — Integration Relationship Registration — Transaction B

Transaction ID: `MUT-2026-09-03-P11-INTERFACES-INTEGRATION-RELATIONSHIPS-B`
Priority: `11 — Interfaces`
State: `CONTROL-PLANE VERSION RECONCILIATION / EXACT-HEAD CI PENDING`
Entry HEAD: `62d39ed6ea423f820c224e73a9ada554c473b9ef`
Pre-write HEAD: `0c7c4d10aa91b28b0b3899251a8eb905b6189a32`
Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`
Corrective control-binding HEAD: `78420d9102d1216a9c5005951d92e2e4f5f0cbda`
First semantic-guard repair HEAD: `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-014 / REP-016`

## Legal entry and material gap

Transaction A is `CLOSED / VERIFIED / RESUME-SAFE`; the exact Interfaces inventory is not reopened. Entry `REP-014 v1.2.18` ended at material row `REL-072` and contained no `INTF-*` relationship rows. `Interfaces/INTF-010_INTEGRATIONS.md` directly states that it implements the integration boundary described by `INTF-001`, `INTF-004`, `INTF-005`, `INTF-006`, `ARC-007`, `ARC-006`, `ENG-007`, and `MEM-001`. Current source reads confirmed those targets and resolved `INTF-006` to active canonical `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`, not legacy `INT-006`.

The Priority-9 relationship disposition records a historical proposed `REL-073: ARC-001 → ARC-011 = REFERENCES`, but explicitly states `BASE REGISTRY UNCHANGED`, `No row is added`, and `DO NOT PROMOTE`. Therefore that historical proposal is a non-material candidate label, not a material REP-014 registry row. The P9 safety invariant is the continued absence of the prohibited `ARC-001 → ARC-011 = REFERENCES` row while its hold remains active; the invariant is not the permanent absence of the lexical token `REL-073` from REP-014.

This is one homogeneous P11 relationship cohort: one explicit source statement, one controlled relationship type, one direction, one evidence class and one failure boundary.

## Relationship matrix

| Candidate | Source | Target | Current identity | Source authority | Target authority | Type | Direction | Material state | Implementation / consumer evidence | External evidence requirement | P11 impact |
|---|---|---|---|---|---|---|---|---|---|---|---|
| REL-073 | INTF-010 | INTF-001 | canonical | direct INTF-010 implements statement | current INTF-001 | IMPLEMENTS | INTF-010 → INTF-001 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | fills active Interface integration graph |
| REL-074 | INTF-010 | INTF-004 | canonical | direct INTF-010 implements statement | current INTF-004 | IMPLEMENTS | INTF-010 → INTF-004 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | fills active Interface integration graph |
| REL-075 | INTF-010 | INTF-005 | canonical | direct INTF-010 implements statement | current INTF-005 | IMPLEMENTS | INTF-010 → INTF-005 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | fills active Interface integration graph |
| REL-076 | INTF-010 | INTF-006 | active canonical `INTF-006_ENVIRONMENT_SENSING.md` | direct INTF-010 implements statement | current INTF-006 | IMPLEMENTS | INTF-010 → INTF-006 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / ACTIVE-INTF-006 / NON-EXECUTABLE | documentary contract only | none | preserves INTF-006 vs legacy INT-006 distinction |
| REL-077 | INTF-010 | ARC-007 | canonical/current | direct INTF-010 implements statement | current ARC-007 | IMPLEMENTS | INTF-010 → ARC-007 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | records Architecture integration boundary |
| REL-078 | INTF-010 | ARC-006 | canonical/current | direct INTF-010 implements statement | current ARC-006 | IMPLEMENTS | INTF-010 → ARC-006 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE / NON-DEPENDENCY | documentary contract only | none | preserves dependency-model boundary without inventing dependency |
| REL-079 | INTF-010 | ENG-007 | current Engine artifact | direct INTF-010 implements statement | current ENG-007 | IMPLEMENTS | INTF-010 → ENG-007 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | records Engine integration boundary |
| REL-080 | INTF-010 | MEM-001 | current Memory artifact | direct INTF-010 implements statement | current MEM-001 | IMPLEMENTS | INTF-010 → MEM-001 | DIRECT-SOURCE-VALIDATED / CONTRACTUAL / NON-EXECUTABLE | documentary contract only | none | records Memory integration boundary |

## Material result

- `REP-014 1.2.18 → 1.2.19` registered only `REL-073..REL-080` plus the bounded P11 evidence section.
- Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`.
- Immutable read-back: `REP-014` blob `39c4aa4fccdc7ff391b0812735ec3c2356113165` contains all eight intended rows.
- Parent→head compare `0c7c4d10... → b9313ce1...`: exactly one changed path, `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`; 45 additions / 1 deletion; no unrelated path.

## Preserved atomicity failure and classification

Initial material exact-head Full-Stack run `33787517479` failed only at `Enforce Mutation Matrix on current change set` after all preceding gates passed. The gate reported:

`changed_files=1 / protected_changes=1 / mutation_matrices=0 / PROTECTED=Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md / MUTATION_MATRIX_PREFLIGHT=FAIL`.

Classification: `TRANSACTION ATOMICITY / CONTROL-PLANE FAILURE`.

This failure was repaired by the corrective control-binding commit `78420d9102d1216a9c5005951d92e2e4f5f0cbda`, which placed this Matrix and the protected REP-011 evidence addendum in the same protected change set. Exact-head Full-Stack, Mutation Matrix and M2 are GREEN at that checkpoint.

## Exact-head Runtime/Integration failure diagnosis

The remaining Transaction-B failure is causally bounded to the REP-014 material addition:

- pre-material HEAD `0c7c4d10aa91b28b0b3899251a8eb905b6189a32`: Runtime/Integration run `33787279598` = `SUCCESS`;
- initial material HEAD `b9313ce19f99ffe389f576c25356ae7f501a04f2`: Runtime/Integration run `33787517604` = `FAILURE`;
- current corrective-binding HEAD `78420d9102d1216a9c5005951d92e2e4f5f0cbda`: Runtime/Integration run `33787939828` = `FAILURE`, isolated to job/check `100757176133`, step `Run integration quality suite`, command `python -m pytest -q Quality/Integration`.

The tracked failing consumer is `Quality/Integration/test_architecture_p9_repository_reconciliation.py`. Its P9 debt test preserved the correct P9 disposition text but used the historical lexical guard:

`assert "| REL-073 |" not in base`

That guard became stale when P11 legally materialized a different relationship under the next available material registry ID `REL-073`. The P9 disposition itself proves the historical ARC-001→ARC-011 proposal was never added to REP-014 and remains `DO NOT PROMOTE`; current REP-014 likewise contains no `ARC-001 → ARC-011 = REFERENCES` row.

Classification: `LEXICAL / HISTORICAL STRING GUARD`.

Semantic invariant to preserve and strengthen:

`P9 ARC-001 → ARC-011 = REFERENCES MUST remain absent from material REP-014 while the P9 local hold remains active.`

The correct executable guard is therefore relationship-semantic rather than historical-ID lexical:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in base`

This is stronger than the old check because it rejects the prohibited P9 relationship regardless of whichever registry ID a future mutation might attempt to assign it, while permitting unrelated later canonical relationships to use material IDs normally.

## Smallest governed repair

The corrective change set MUST contain this Matrix together with:

1. `Repository/REP-011_PRIORITY11_INTERFACES_RELATIONSHIP_REGISTRATION_ADDENDUM_2026-09-03_B.md` updated with the exact-head Runtime causal evidence and semantic-guard repair; and
2. `Quality/Integration/test_architecture_p9_repository_reconciliation.py` updated only from the stale lexical `REL-073` absence guard to the semantic `ARC-001 → ARC-011 = REFERENCES` absence guard.

No REP-014 material rewrite is required. No safety invariant is weakened; the P9 hold becomes ID-independent and therefore stronger.

## Second stale historical consumer — exact-head follow-up

After the first semantic repair at `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`, Runtime/Integration remained red. Exact `Quality/Integration` tree inspection exposed a second P9 consumer in `test_architecture_p9_status_sync.py`:

`assert "| REL-073 |" not in registry`

That test already binds the historical P9 disposition and `HARD HOLD / PRE-MATERIAL ABORT`; only its final lexical identifier guard is stale. Current evidence proves the historical proposal remains `ARC-001 → ARC-011 = REFERENCES`, while material `REL-073` is the unrelated `INTF-010 → INTF-001 = IMPLEMENTS` row.

Classification: `SECOND STALE HISTORICAL CONSUMER / LEXICAL IDENTIFIER GUARD`.

Second semantic repair:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in registry`

The repair preserves the same durable safety invariant, remains ID-independent, and does not mutate REP-014.

## Control-plane version drift — exact-head post-second-repair diagnosis

Exact post-second-repair Runtime/Integration run `33851006941`, job `100953540301`, completed with `2 failed, 586 passed, 1 warning, 11 subtests passed`. The reconciliation gate reports the concrete mismatch:

`Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md: Version='1.2.19'; manifest='1.2.18'`.

Source-level inspection shows both `test_control_plane_reconciliation_gate.py::test_current_control_plane_boundary_is_consistent` and `test_control_plane_current_manifest.py::test_current_control_plane_manifest_matches_current_repository` consume the same `control_plane_reconciliation_gate.evaluate()` result. The gate intentionally fails closed on current-manifest identity/version/status drift.

Causal proof is direct: pre-write REP-014 at `0c7c4d10aa91b28b0b3899251a8eb905b6189a32` was version `1.2.18`; material commit `b9313ce19f99ffe389f576c25356ae7f501a04f2` changed exactly one path, REP-014, to version `1.2.19`; the current REP-020 manifest remained at `1.2.18`. The manifest's own Refresh rule requires current-manifest reconciliation whenever a listed artifact materially changes identity, version, or status, and explicitly says mismatch is not permission to downgrade the artifact.

Classification: `CONTROL-PLANE CURRENT-MANIFEST VERSION SYNCHRONIZATION DEFECT`.

Safety invariant:

`Every artifact listed in REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST must match the listed current identity/version/status; material artifact authority is not downgraded to satisfy a stale manifest.`

Smallest governed source repair: refresh only the current REP-020 manifest row for REP-014 from `1.2.18` to `1.2.19`, rebind its current checkpoint/evidence metadata to this recovery, preserve all historical manifests, preserve REP-014 blob `39c4aa4fccdc7ff391b0812735ec3c2356113165`, and do not weaken either executable control-plane test.

## Authorized material set

| ID | Target | Action | Required result |
|---|---|---|---|
| P11-B-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | NO CHANGE / IMMUTABLE MATERIAL | retain `1.2.19`; REL-073..080 and blob `39c4aa4fccdc7ff391b0812735ec3c2356113165` |
| P11-B-02 | this Matrix | UPDATE | preserve prior failure evidence; add current-manifest drift classification, invariant and recovery binding |
| P11-B-03 | `Repository/REP-011_PRIORITY11_INTERFACES_RELATIONSHIP_REGISTRATION_ADDENDUM_2026-09-03_B.md` | UPDATE | bind exact post-second-repair failure and manifest recovery without relationship/priority promotion |
| P11-B-04 | `Quality/Integration/test_architecture_p9_repository_reconciliation.py` | ALREADY REPAIRED / NO CHANGE | retain first semantic prohibited-relationship guard |
| P11-B-05 | `Quality/Integration/test_architecture_p9_status_sync.py` | ALREADY REPAIRED / NO CHANGE | retain second semantic prohibited-relationship guard |
| P11-B-06 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE CURRENT EVIDENCE SURFACE | reconcile only current REP-014 version `1.2.18 → 1.2.19` plus bounded current recovery/checkpoint metadata; historical manifests untouched |

No Interface source artifact, implementation, provider configuration or credential mutation is authorized by Transaction B. The integration-test mutations remain limited to preserving the already-governed P9 non-promotion invariant; the current repair changes the stale current evidence surface, not the tests or REP-014 material.

## Explicit semantic and trust boundaries

- `IMPLEMENTS` is the direct documentary/contractual relationship asserted by INTF-010; it is not executable implementation proof.
- No `DEPENDS_ON`, `CONSUMES`, reverse edge, provider relationship, runtime reachability or authority transfer is inferred.
- Local documentary proof does not establish provider authenticity, authenticated provider identity, credentials, permission, remote read-back or production execution.
- No endpoint status or authority is promoted.
- Legacy `INT-006` remains distinct and is not targeted.
- P9 remains closed for its bounded partition; the deferred ARC-001→ARC-011 registry row remains unpromoted and is not reopened by this repair.
- P11 remains open after Transaction B for connector/implementation evidence and external-trust boundary assessment.
- Priority 10 remains closed; Phase 1, Global Connected Baseline, repository-wide graph and Global Integrity PASS remain open/unclaimed.

Validation: `atomic Matrix + REP-011 evidence + current REP-020 manifest refresh → immutable read-back → parent/path proof → exact-head Full-Stack + Mutation Matrix + M2 + Runtime/Integration → close B only at 4/4 GREEN, otherwise HOLD / RESUME-SAFE`.
