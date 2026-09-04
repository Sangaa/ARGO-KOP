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
The material compare changed only `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` and preserved the active `INTF-006` versus legacy `INT-006` distinction.

## Preserved atomicity failure and recovery boundary

Full-Stack exact-head run `33787517479` failed at the Mutation Matrix enforcement gate because the protected REP-014 material commit did not include a Matrix path in the same push delta (`protected_changes=1 / mutation_matrices=0`). Earlier Full-Stack steps passed. This was classified as `TRANSACTION ATOMICITY / CONTROL-PLANE FAILURE`, not relationship-semantic failure.

The corrective control-binding commit `78420d9102d1216a9c5005951d92e2e4f5f0cbda` placed this evidence addendum and the Transaction-B Matrix in the same protected change set. At that exact head Full-Stack, Mutation Matrix and M2 are GREEN.

## First Runtime/Integration stale-consumer repair

The first post-material Runtime/Integration failure was traced to `Quality/Integration/test_architecture_p9_repository_reconciliation.py`. Its P9 debt test preserved the correct historical disposition but encoded non-promotion lexically as:

`assert "| REL-073 |" not in base`

P9 proves the historical proposal was `REL-073: ARC-001 → ARC-011 = REFERENCES`, was never materialized, and remains `DO NOT PROMOTE`. P11 later legally used the next material ID `REL-073` for the unrelated canonical row `INTF-010 → INTF-001 = IMPLEMENTS`.

At `4d1a2f5f11eca725786bf0c5d6e7fce2d1eb02e8`, that consumer was repaired to enforce the durable semantic invariant:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in base`

The exact-head Runtime/Integration workflow still failed, while prototype/integrity and the other required families remained green. Source-level revalidation of the repaired P9 reconciliation test found its semantic guard and remaining assertions consistent with current tracked sources.

## Second stale historical consumer

Exact-head inventory of `Quality/Integration` exposed a second P9 consumer: `test_architecture_p9_status_sync.py`. Its function `test_local_rel073_hold_remains_unpromoted_and_nonblocking` correctly binds the same historical P9 disposition and `HARD HOLD / PRE-MATERIAL ABORT`, but ends with another lexical assertion:

`assert "| REL-073 |" not in registry`

Current source evidence proves that assertion no longer represents the safety invariant:

- P9 disposition: proposed `REL-073: ARC-001 → ARC-011 = REFERENCES`; `BASE REGISTRY UNCHANGED`; `No row is added`; `DO NOT PROMOTE`.
- Current REP-014: material `REL-073 = INTF-010 → INTF-001 = IMPLEMENTS`; no `ARC-001 → ARC-011 = REFERENCES` row.

Classification: `SECOND STALE HISTORICAL CONSUMER / LEXICAL IDENTIFIER GUARD`.

The smallest governed repair changes only that final consumer assertion to:

`assert "| ARC-001 | ARC-011 | REFERENCES |" not in registry`

This preserves and strengthens the P9 hold by making enforcement independent of future registry-ID allocation. No relationship material, P9 closure state, Interface contract, provider boundary or runtime implementation is changed.

## Atomic corrective scope

This second repair is authorized only as one Git commit containing:

1. `Quality/Integration/test_architecture_p9_status_sync.py` — replace only the stale lexical final assertion with the semantic prohibited-relationship assertion;
2. this REP-011 addendum — bind the exact second-consumer diagnosis and repair;
3. `Repository/MUT-2026-09-03-P11-INTERFACES-INTEGRATION-RELATIONSHIPS-B_MUTATION_MATRIX.md` — extend Transaction-B corrective authority/evidence for the same semantic invariant.

`REP-014` is immutable in this corrective set.

## Boundaries

- REL-073..REL-080 remain contractual/documentary and non-executable.
- The deferred P9 `ARC-001 → ARC-011 = REFERENCES` relationship remains absent and unpromoted.
- Both test repairs change only how the existing P9 semantic invariant is enforced; neither weakens or removes the invariant.
- This addendum does not create, reverse, strengthen or promote any relationship.
- It does not establish provider authenticity, credentials, permission, remote read-back, production execution or external trust.
- It does not reopen Transaction A, Priority 9, or Priority 10.
- Priority 11 remains `IN_PROGRESS` pending Transaction-B exact-head verification and subsequent connector/implementation/external-trust assessment.
- Phase 1, Global Connected Baseline, repository-wide graph completion and Global Integrity PASS remain open/unclaimed.

Closure remains forbidden until all required workflow families are GREEN on one exact HEAD.
