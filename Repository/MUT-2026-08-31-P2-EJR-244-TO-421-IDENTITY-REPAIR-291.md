# MUT-2026-08-31-P2-EJR-244-TO-421-IDENTITY-REPAIR-291

Status: OPEN / FUNCTIONAL EXECUTION AUTHORIZED
Scope: bounded identity repair for displaced root EJR-244 using successor EJR-421.
Opening main: `eff63514babc30c3d0805bac18f31316601676c6`
Pre-write Matrix291: `c7731f4530aeea41df4d1133f40d12f51c773d32`
Authority: closed Lease290 + complete-history EJR-421 vacancy proof.

## Hard gate

- retained Memory EJR-244 remains `Memory/Engineering_Journal/EJR-244_2026-08-15_P62_SESSION_CLOSURE.md`, blob `2fe0ad5eabfb708f7fd1c931156f96c250d425cf`;
- displaced root source remains `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`, blob `4c62b2f8b9151255a87d83c87829f3bafe1c0f54`;
- successor path `EJR/EJR-421_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md` is absent at the opening head;
- EJR-421 complete-history vacancy proof is VACANT (`33396768282` / artifact `9759617449`);
- verified census reports zero exact-member-path consumers for the EJR-244 pair.

## Authorized repair

Perform one atomic Git-tree mutation that removes the displaced root EJR-244 path and creates the EJR-421 successor path. Change only the first H1 identity from `EJR-244` to `EJR-421`; preserve every remaining byte of the displaced root record. Retain Memory EJR-244 byte-for-byte. Do not rewrite historical narrative references or any consumers.

Baseline normalization is explicitly out of scope. MEMORY_TO_ROOT expected baseline remains 16 during this repair; expected observed cohort after repair is 15. A separate lease is mandatory if the exact audit artifact proves count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
