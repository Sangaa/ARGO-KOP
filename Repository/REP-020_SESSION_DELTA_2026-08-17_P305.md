# P305 — CONTROL-PLANE BINDING DELTA

Date: 2026-08-17
Status: Recorded / Priority 1 Reconciliation / Integrity Hold
Checkpoint: P305

## Scope
Current-content identity reconciliation for `REP-011` and `REP-012` after P304.

## Current Evidence
- `REP-011` remains v1.1.2, blob `77ad9a18827099e54ddd8dd16a278535d226abbd`.
- `REP-012` remains v1.0.9, blob `5b51e0b468e479842d7d83468e8e7c20a06ec1b1`.
- Both current blobs were fetched directly and their full content inspected.
- No content mutation to either registry occurred in P304.
- P304 is therefore evidence affecting their reconciliation state, not evidence that their internal registry bindings are already current.

## Classification
`CURRENT_CONTENT_CONFIRMED / INTERNAL_BINDING_LAG`

The files themselves are current repository artifacts, but their internal review/checkpoint sections have not yet been explicitly synchronized to P304.

## Decision
Do not rewrite either large canonical registry until a full-content-preserving mutation path is available and independently verified.
Do not infer closure from their unchanged content or from the existence of P304 elsewhere.

## Learning
A control-plane artifact can be physically current while its own internal evidence binding is stale. Physical currentness and internal registry synchronization are separate dimensions.

## Next Safe Entry
1. Use a guaranteed full-content-preserving write path for `REP-011` and `REP-012`.
2. Add only the minimum P304/P305 evidence required.
3. Re-read both full files.
4. Reconcile `REP-013/014/015/016/020` again.
5. Keep Priority 1 and Integrity Hold until the cross-registry state is explicitly reconciled.

---

End of P305
