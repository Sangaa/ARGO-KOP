# MUT-2026-08-31-P2-EJR-245-DISPOSITION-AND-422-VACANCY-PROOF-293

Status: OPEN / EVIDENCE EXECUTION AUTHORIZED
Scope: evidence-only disposition confirmation for EJR-245 and complete-history vacancy proof for candidate EJR-422.
Opening main: `6e00c2a0ca138918ae7c2c9bf02fd97da8f57f41`
Pre-write Matrix293: `b5da911147c076ab058b20a5f67d9943a0b09957`

## Disposition under test

- `Memory/Engineering_Journal/EJR-245_2026-08-15_P64_SESSION_CLOSURE.md`: RETAINED first valid historical allocation unless stronger contradictory evidence emerges.
- `EJR/EJR-245_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`: DISPLACED legitimate content if complete-history successor vacancy is proven.
- Memory allocation: `99e8d80c033da324f0e20dcd2b521cf7d0603d88` at 2026-08-15T07:34:09Z.
- Root allocation: `499e90d71a6daadc124b6709910842e24b521795` at 2026-08-17T18:41:14Z.

Both records are preserved unchanged in this lease. Current search absence for EJR-422 is not treated as vacancy proof.

## Required hard gate

Dedicated workflow must use complete checkout history and `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-422`, upload the exact JSON evidence, and fail closed unless `decision == VACANT`.

Identity mutation is explicitly forbidden in Lease293. If the gate succeeds, EJR-422 becomes reserved only for displaced root EJR-245 and a separate governed repair lease is required.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
