# REP-011 Priority-11 Interfaces Relationship Registration Addendum — Transaction B

Date: 2026-09-04
Priority: `11 — Interfaces`
Transaction: `MUT-2026-09-03-P11-INTERFACES-INTEGRATION-RELATIONSHIPS-B`
State: `CLOSED / VERIFIED / RESUME-SAFE`

## Material checkpoint

Priority-11 Transaction B registered the direct documentary integration cohort asserted by canonical `Interfaces/INTF-010_INTEGRATIONS.md`:

`INTF-010 → INTF-001 / INTF-004 / INTF-005 / INTF-006 / ARC-007 / ARC-006 / ENG-007 / MEM-001 = IMPLEMENTS`.

Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`.
Corrective control-binding HEAD: `78420d9102d1216a9c5005951d92e2e4f5f0cbda`.
First semantic-guard repair HEAD: `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`.
Control-plane reconciliation HEAD: `43376b5764730ef53b961264230b3bc5ab471dea`.
Current `REP-014` material blob: `39c4aa4fccdc7ff391b0812735ec3c2356113165`.
The parent→head material compare changed only `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` and preserved the active `INTF-006` versus legacy `INT-006` distinction.

## Preserved atomicity failure and recovery boundary

Full-Stack exact-head run `33787517479` failed at the Mutation Matrix enforcement gate because the protected REP-014 material commit did not include a Matrix path in the same push delta (`protected_changes=1 / mutation_matrices=0`). Earlier Full-Stack steps passed. This was classified as `TRANSACTION ATOMICITY / CONTROL-PLANE FAILURE`, not relationship-semantic failure.

The corrective control-binding commit `78420d9102d1216a9c5005951d92e2e4f5f0cbda` placed this evidence addendum and the Transaction-B Matrix in the same protected change set. At that exact head Full-Stack, Mutation Matrix and M2 are GREEN.

## Runtime/Integration causal boundary

The remaining failure was independently bounded to the material REP-014 change:

- `0c7c4d10aa91b28b0b3899251a8eb905b6189a32` — pre-material Runtime/Integration run `33787279598` = `SUCCESS`;
- `b9313ce19f99ffe389f576c25356ae7f501a04f2` — initial material Runtime/Integration run `33787517604` = `FAILURE`;
- `78420d9102d1216a9c5005951d92e2e4f5f0cbda` — Runtime/Integration run `33787939828` = `FAILURE`, isolated to `python -m pytest -q Quality/Integration`.

Direct source inspection identified `Quality/Integration/test_architecture_p9_repository_reconciliation.py` as a stale historical-ID consumer. Its P9 invariant was strengthened from lexical `REL-073` absence to semantic absence of `ARC-001 → ARC-011 = REFERENCES` without changing REP-014 or weakening P9.

The first repair was committed at `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`. Exact-head Runtime/Integration remained red, exposing a second stale historical consumer in `test_architecture_p9_status_sync.py`; its final lexical guard was likewise repaired to the same semantic prohibited-relationship guard.

## Post-second-repair control-plane diagnosis

Exact Runtime/Integration run `33851006941`, job `100953540301`, completed with `2 failed, 586 passed, 1 warning, 11 subtests passed`. The executable control-plane report identified:

`REP-014 Version='1.2.19'; manifest='1.2.18'`.

Both `test_control_plane_reconciliation_gate.py` and `test_control_plane_current_manifest.py` consume the same fail-closed `control_plane_reconciliation_gate.evaluate()` current boundary. The mismatch was therefore source-side current-evidence drift, not an obsolete assertion.

Pre-write REP-014 at `0c7c4d10aa91b28b0b3899251a8eb905b6189a32` was version `1.2.18`. Material commit `b9313ce19f99ffe389f576c25356ae7f501a04f2` changed exactly one path and legally raised REP-014 to `1.2.19`, while `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` remained `1.2.18`. REP-020's own Refresh rule requires a current-manifest refresh whenever a listed artifact's identity/version/status changes and explicitly forbids downgrading the artifact to satisfy stale evidence.

Classification: `CONTROL-PLANE CURRENT-MANIFEST VERSION SYNCHRONIZATION DEFECT`.

Governed invariant:

`CURRENT MANIFEST VERSION == CURRENT LISTED ARTIFACT VERSION; STALE CURRENT EVIDENCE MUST BE REBOUND, NOT USED TO DOWNGRADE VALID MATERIAL.`

The bounded atomic recovery at `43376b5764730ef53b961264230b3bc5ab471dea` updated only this evidence addendum, the Transaction-B Matrix and the current REP-020 manifest. REP-014 and executable tests remained unchanged; historical manifests remained immutable.

## Exact-head closure proof

Parent→head proof for `88bbce26014299728a33871fe7b85111870b038b → 43376b5764730ef53b961264230b3bc5ab471dea` shows exactly three authorized paths changed. Immutable read-back confirms the current REP-020 row now records REP-014 `1.2.19`, while REP-014 remains blob `39c4aa4fccdc7ff391b0812735ec3c2356113165`.

All four required workflow families completed `SUCCESS` on exact HEAD `43376b5764730ef53b961264230b3bc5ab471dea`:

- Full-Stack Repository Audit — `33866164143` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests — `33866164162` — `SUCCESS`, including the integration quality suite;
- M2 Multi-Channel Proposal Training — `33866164062` — `SUCCESS`;
- Real Mutation Matrix Regression — `33866164105` — `SUCCESS`.

Transaction B is therefore `CLOSED / VERIFIED / RESUME-SAFE` subject to exact-head revalidation of this closure evidence commit itself. If that closure HEAD is not 4/4 GREEN, the transaction returns to `HOLD / RESUME-SAFE` and no successor transaction is authorized.

## Boundaries

- REL-073..REL-080 remain contractual/documentary and non-executable.
- The deferred P9 `ARC-001 → ARC-011 = REFERENCES` relationship remains absent and unpromoted.
- Both historical-consumer repairs preserve and strengthen the existing P9 semantic invariant.
- The current-manifest repair changed current evidence only; it did not create, reverse, strengthen or promote any relationship.
- It does not establish provider authenticity, credentials, permission, remote read-back, production execution or external trust.
- It does not reopen Transaction A, Priority 9, or Priority 10.
- Priority 11 remains `IN_PROGRESS`; the next legal work must address actual connector/adapter implementation or consumer/runtime evidence rather than restating documentary relationships.
- Phase 1, Global Connected Baseline, repository-wide graph completion and Global Integrity PASS remain open/unclaimed.
