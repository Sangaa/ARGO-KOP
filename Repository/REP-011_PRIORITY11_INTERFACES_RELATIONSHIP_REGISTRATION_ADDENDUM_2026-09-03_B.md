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
- `78420d9102d1216a9c5005951d92e2e4f5f0cbda` — current Runtime/Integration run `33787939828` = `FAILURE`, isolated to job/check `100757176133`, step `Run integration quality suite`, command `python -m pytest -q Quality/Integration`.

Direct source inspection identifies the failing consumer as `Quality/Integration/test_architecture_p9_repository_reconciliation.py`. The P9 debt test correctly preserves the disposition:

`REL-073 = LOCAL REGISTRY COMPLETENESS HOLD / NON-BLOCKING FOR BOUNDED ARCHITECTURE PARTITION CLOSURE / DO NOT PROMOTE`

but historically encoded its non-promotion check as:

`assert "| REL-073 |" not in base`

The Priority-9 disposition itself states `BASE REGISTRY UNCHANGED` and `No row is added`; its proposed `REL-073: ARC-001 → ARC-011 = REFERENCES` remained non-material. P11 later used the next material registry ID `REL-073` for the unrelated canonical row `INTF-010 → INTF-001 = IMPLEMENTS`. The P9 relationship remains absent.

Classification: `LEXICAL / HISTORICAL STRING GUARD`.

## Governed semantic-guard repair

The safety invariant is strengthened from historical identifier absence to prohibited relationship absence:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in base`

This preserves the P9 `DO NOT PROMOTE` boundary regardless of future relationship-ID allocation and does not alter REP-014, P9 closure, P11 relationship semantics, or any Interface implementation.

The first repair was committed at `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`. Exact-head Runtime/Integration remained red while the corrected consumer and its tracked source invariants revalidated cleanly.

## Second stale historical consumer

Exact-head `Quality/Integration` inventory then exposed `test_architecture_p9_status_sync.py`. Its `test_local_rel073_hold_remains_unpromoted_and_nonblocking` correctly checks the P9 decision, disposition and `HARD HOLD / PRE-MATERIAL ABORT`, but ends with a second stale lexical guard:

`assert "| REL-073 |" not in registry`

The governing P9 disposition proves the historical proposal was `ARC-001 → ARC-011 = REFERENCES`, was never materialized and remains `DO NOT PROMOTE`. Current REP-014 proves material `REL-073` is instead `INTF-010 → INTF-001 = IMPLEMENTS` and the prohibited historical triple remains absent.

Classification: `SECOND STALE HISTORICAL CONSUMER / LEXICAL IDENTIFIER GUARD`.

The smallest semantic repair is:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in registry`

This changes only how the already-governed P9 safety invariant is enforced. It does not change relationship material or closure authority.

## Atomic corrective scope

The second repair is bound to one corrective change set containing the status-sync test mutation, this REP-011 evidence update and the Transaction-B Matrix update. `REP-014` remains immutable.

## Post-second-repair control-plane diagnosis

Exact Runtime/Integration run `33851006941` at the post-second-repair line completed with `2 failed, 586 passed, 1 warning, 11 subtests passed`. The executable control-plane report identifies a current evidence mismatch:

`REP-014 Version='1.2.19'; manifest='1.2.18'`.

Current source proves `test_control_plane_reconciliation_gate.py` and `test_control_plane_current_manifest.py` both consume the same fail-closed `control_plane_reconciliation_gate.evaluate()` boundary. The gate requires every listed current artifact to match its current manifest identity/version/status.

The mismatch is source-side, not an obsolete assertion. At pre-write HEAD `0c7c4d10aa91b28b0b3899251a8eb905b6189a32`, REP-014 was `1.2.18`. Material commit `b9313ce19f99ffe389f576c25356ae7f501a04f2` changed exactly one path and legally raised REP-014 to `1.2.19`, while the current REP-020 manifest remained `1.2.18`. REP-020's own Refresh rule requires the current manifest to be refreshed after identity/version/status mutation and forbids treating mismatch as permission to downgrade the artifact.

Classification: `CONTROL-PLANE CURRENT-MANIFEST VERSION SYNCHRONIZATION DEFECT`.

Governed invariant:

`CURRENT MANIFEST VERSION == CURRENT LISTED ARTIFACT VERSION; STALE CURRENT EVIDENCE MUST BE REBOUND, NOT USED TO DOWNGRADE VALID MATERIAL.`

Authorized recovery is therefore bounded to the current REP-020 evidence surface plus this evidence addendum and the Transaction-B Matrix in one atomic change set. REP-014 and both executable tests remain unchanged. Historical manifests remain immutable.

## Exact-head closure proof

Control-plane reconciliation commit `43376b5764730ef53b961264230b3bc5ab471dea` changed exactly three authorized paths: this addendum, the Transaction-B Matrix, and `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`. Immutable read-back confirmed the current REP-020 row records REP-014 `1.2.19`; REP-014 remained blob `39c4aa4fccdc7ff391b0812735ec3c2356113165`.

All four required workflow families completed `SUCCESS` on exact HEAD `43376b5764730ef53b961264230b3bc5ab471dea`:

- Full-Stack Repository Audit — run `33866164143` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests — run `33866164162` — `SUCCESS`, including `Run integration quality suite`;
- M2 Multi-Channel Proposal Training — run `33866164062` — `SUCCESS`;
- Real Mutation Matrix Regression — run `33866164105` — `SUCCESS`.

The first closure-binding commit `5f635c395fbde09cd8d0c755460578055c445bdd` correctly changed only the Matrix and this addendum, but its addendum rewrite compressed preserved historical evidence unnecessarily. That presentation loss was detected by parent→head diff before closure CI was accepted as authoritative. This corrective binding restores the detailed evidence and appends closure proof only; it does not alter material semantics or reopen any repaired invariant.

Transaction B is `CLOSED / VERIFIED / RESUME-SAFE` only if this final evidence-preserving closure HEAD itself reaches all four required workflow families GREEN. Until then no successor transaction is authorized.

## Boundaries

- REL-073..REL-080 remain contractual/documentary and non-executable.
- The deferred P9 `ARC-001 → ARC-011 = REFERENCES` relationship remains absent and unpromoted.
- Both test repairs change only how that existing P9 semantic invariant is enforced; neither weakens or removes the invariant.
- The current-manifest repair changes current evidence only; it does not create, reverse, strengthen or promote any relationship.
- It does not establish provider authenticity, credentials, permission, remote read-back, production execution or external trust.
- It does not reopen Transaction A, Priority 9, or Priority 10.
- Priority 11 remains `IN_PROGRESS`; the next legal work must address actual connector/adapter implementation or consumer/runtime evidence rather than restating documentary relationships.
- Phase 1, Global Connected Baseline, repository-wide graph completion and Global Integrity PASS remain open/unclaimed.
