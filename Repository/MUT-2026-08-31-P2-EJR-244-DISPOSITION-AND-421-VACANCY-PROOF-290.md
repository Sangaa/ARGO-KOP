# MUT-2026-08-31-P2-EJR-244-DISPOSITION-AND-421-VACANCY-PROOF-290

Status: OPEN / EVIDENCE GATE
Scope: evidence-only disposition confirmation for EJR-244 and complete-history vacancy proof for candidate EJR-421.
Opening main: `34bade3b130d54f827dd4abea99d6c83d4132429`
Pre-write Matrix290: `bbbab98aec1b3d7d71a61ee494614c29e864f2b2`

## Disposition basis

- `Memory/Engineering_Journal/EJR-244_2026-08-15_P62_SESSION_CLOSURE.md`: candidate RETAINED first valid historical allocation; allocation commit `82ccbdda485297ed8a206c5dad960ce44f076cbc` at 2026-08-15T07:27:45Z.
- `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`: candidate DISPLACED legitimate content; allocation commit `1510161a687a336e8efa52b522ed8ea8aea942a4` at 2026-08-17T18:36:56Z.
- Both records were directly read, are semantically legitimate and independent, and the verified current census reports zero exact-member-path consumers.
- Current cohort evidence reports only two external exact-ID references for EJR-244.

Under the first-valid historical allocation rule, Memory EJR-244 is RETAINED and root EJR-244 is DISPLACED unless stronger contrary evidence appears.

## Complete-history vacancy gate

Candidate successor: `EJR-421`.
Current repository search returns no EJR-421 result; this is discovery only and is not vacancy proof.

A dedicated workflow must checkout complete history (`fetch-depth: 0`), verify the checkout is non-shallow, execute `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-421`, upload the exact JSON, and fail closed unless `decision == VACANT`.

No identity mutation is authorized until that proof succeeds. EJR-421, if proven vacant, is reserved solely for displaced root EJR-244.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
