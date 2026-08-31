# Repair 312 — EJR-248 → EJR-428 Identity Repair

Status: OPEN / AUTHORIZED BY LEASE 311
Date: 2026-08-31
Scope: Priority 2 MEMORY_TO_ROOT_EJR identity reconciliation

## Authorization evidence
Lease 311 established that the Memory EJR-248 allocation predates the later root allocation and that candidate successor EJR-428 is VACANT under complete-history proof.

## Authorized mutation
- KEEP: `Memory/Engineering_Journal/EJR-248_2026-08-15_P67_SESSION_CLOSURE.md` as EJR-248.
- MOVE atomically: `EJR/EJR-248_2026-08-18_TODAY_BUILD_PLAN_AND_SESSION_CLOSURE.md` → `EJR/EJR-428_2026-08-18_TODAY_BUILD_PLAN_AND_SESSION_CLOSURE.md`.
- Change only the displaced root journal H1 from EJR-248 to EJR-428 if content identity requires it; preserve all other semantic content.

## Validation
After mutation, run Internal Document-ID Audit and Full-Stack Repository Audit. Inspect the MEMORY_TO_ROOT provenance artifact. A cohort count change 9→8 must be treated as a separate deterministic baseline-normalization lease, not folded into this repair.

## Non-claims
No global integrity promotion. Historical narrative references are not cosmetically rewritten.
