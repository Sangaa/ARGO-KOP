# Priority 7 — ARC-006 → CORE-003 REL-067 Reconciliation — Transaction K

Date: 2026-09-01
State: `CANDIDATE / PROTECTED MUTATION APPLIED / EXACT-HEAD VERIFICATION PENDING`
Transaction: `MUT-2026-09-01-P7-ARC006-CORE003-REL067-K`
Work Lease: `HERMUZ-P7-K-REL067-20260901`
Entry HEAD: `f5f6719c848123b7d2f07c27010efafbcae71af4`
Pre-write Matrix HEAD: `6aa15e2fb9e2d5da2da1933ee1b04901fe9f6629`

## Reconstructed decision

Priority 7 remains the first globally open Phase-1 partition. Transaction J independently validated the ARC-006→CORE-003 documentary boundary and closed resume-safe without modifying REP-014. Current Core status explicitly requires REP-014 reconciliation where evidence requires it.

K therefore closes only the synchronization gap created by J:

`REL-067 = ARC-006 → CORE-003 = REFERENCES / INTENTIONAL ONE-WAY / CONSTITUTION-AUTHORITY-ALIGNED / NON-DEPENDENCY`.

## Source evidence boundary

- ARC-006 explicitly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents.
- ARC-006 permits Architecture to depend on Core/Governance but explicitly warns that a textual path reference alone does not establish dependency.
- CORE-003 does not directly name ARC-006.
- J validated the one-way documentary direction and stronger/reverse negative boundary under exact-head CI before K.

## Protected mutation scope

K changes only:

1. REP-014 v1.2.10→1.2.11 with REL-067 and bounded evidence section.
2. Current control-plane manifest REP-014 row 1.2.10→1.2.11 and K refresh binding.
3. Core folder status v1.3.7→1.3.8, adding the fifth bounded seam while retaining Integrity Hold and pending certification.
4. Focused ARC-006/CORE-003 regression so REL-067 must exist exactly once while unsupported stronger/reverse semantics remain forbidden.
5. This transaction evidence record.
6. The pre-existing K Matrix rebound in the same changed-file set.

ARC-006 and CORE-003 source content remain unchanged.

## Non-claims

K does not establish `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, `CONSUMES`, runtime reachability, or executable coupling. It does not create a reverse CORE-003→ARC-006 edge. It does not certify Core or Architecture, close Priority 7, close Phase 1, close the Connected Baseline, or claim Global PASS.

## Verification state

Exact-head read-back and required CI are pending at candidate construction time. K may become resume-safe only after the protected candidate diff, target read-back, control-plane manifest gate and required workflows are reconciled on the exact candidate HEAD.
