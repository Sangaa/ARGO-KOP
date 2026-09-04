# REP-011 Priority-11 Interfaces Relationship Registration Addendum — Transaction B

Date: 2026-09-03
Priority: `11 — Interfaces`
Transaction: `MUT-2026-09-03-P11-INTERFACES-INTEGRATION-RELATIONSHIPS-B`
State: `SECOND STALE HISTORICAL CONSUMER REPAIR / EXACT-HEAD CI PENDING`

## Material checkpoint

Priority-11 Transaction B registered the direct documentary integration cohort asserted by canonical `Interfaces/INTF-010_INTEGRATIONS.md`:

`INTF-010 → INTF-001 / INTF-004 / INTF-005 / INTF-006 / ARC-007 / ARC-006 / ENG-007 / MEM-001 = IMPLEMENTS`.

Initial material HEAD: `b9313ce19f99ffe389f576c25356ae7f501a04f2`.
Corrective control-binding HEAD: `78420d9102d1216a9c5005951d92e2e4f5f0cbda`.
First semantic-guard repair HEAD: `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`.
Current `REP-014` material blob: `39c4aa4fccdc7ff391b0812735ec3c2356113165`.
The parent→head material compare changed only `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` and preserved the active `INTF-006` versus legacy `INT-006` distinction.

## Preserved atomicity failure and recovery boundary

Full-Stack exact-head run `33787517479` failed at the Mutation Matrix enforcement gate because the protected REP-014 material commit did not include a Matrix path in the same push delta (`protected_changes=1 / mutation_matrices=0`). Earlier Full-Stack steps passed. This was classified as `TRANSACTION ATOMICITY / CONTROL-PLANE FAILURE`, not relationship-semantic failure.

The corrective control-binding commit `78420d9102d1216a9c5005951d92e2e4f5f0cbda` placed this evidence addendum and the Transaction-B Matrix in the same protected change set. At that exact head Full-Stack, Mutation Matrix and M2 are GREEN.

## Runtime/Integration causal boundary

The remaining failure is independently bounded to the material REP-014 change:

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

Exact-head CI must reach all four required workflow families GREEN before Transaction B can close.

## Boundaries

- REL-073..REL-080 remain contractual/documentary and non-executable.
- The deferred P9 `ARC-001 → ARC-011 = REFERENCES` relationship remains absent and unpromoted.
- Both test repairs change only how that existing P9 semantic invariant is enforced; neither weakens or removes the invariant.
- This addendum does not create, reverse, strengthen or promote any relationship.
- It does not establish provider authenticity, credentials, permission, remote read-back, production execution or external trust.
- It does not reopen Transaction A, Priority 9, or Priority 10.
- Priority 11 remains `IN_PROGRESS` pending Transaction-B exact-head verification and subsequent connector/implementation/external-trust assessment.
- Phase 1, Global Connected Baseline, repository-wide graph completion and Global Integrity PASS remain open/unclaimed.
