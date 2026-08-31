# MUT — EJR-174 → EJR-427 Identity Repair — Repair 309

Date: 2026-08-31
Status: OPEN / CONTROLLED REPAIR
Priority: P2 Internal Document-ID Audit

## Authority basis
Lease 308 established:
- Memory EJR-174 is the first valid historical allocation and retains `EJR-174`.
- Root `EJR/EJR-174_2026-08-14_MATRIX_UPDATE_NOTE.md` is the later independent allocation.
- Complete-history vacancy proof returned `EJR-427 = VACANT` with no current or historical claims.
- Full-Stack Repository Audit passed on the proof head.

## Repair
Atomically replace the displaced root record:
- remove `EJR/EJR-174_2026-08-14_MATRIX_UPDATE_NOTE.md`;
- create `EJR/EJR-427_2026-08-14_MATRIX_UPDATE_NOTE.md` with the same substantive content and only the identity-bearing H1 changed from `EJR-174` to `EJR-427`.

The Memory EJR-174 record must remain unchanged.

## Validation
- old root path absent;
- successor root path present with preserved content;
- Memory EJR-174 blob unchanged;
- Full-Stack SUCCESS on exact repair head;
- Internal Document-ID Audit may fail only for deterministic cohort count drift 10→9; any other gap blocks closure.

## Integrity
No global promotion. Priority 2 and Phase 1 remain OPEN; Global Integrity remains HOLD.
