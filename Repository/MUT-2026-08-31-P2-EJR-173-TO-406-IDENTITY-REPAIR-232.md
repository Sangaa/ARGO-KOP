# MUT-2026-08-31-P2-EJR-173-TO-406-IDENTITY-REPAIR-232

Status: PREWRITE / ONE-RECORD REPAIR
Authorized by: Lease230 disposition + Lease231 verified vacancy

## Functional scope
- retain `Memory/Engineering_Journal/EJR-173_2026-08-13_REP020_MATRIX_EXPANSION.md` unchanged;
- rename root `EJR/EJR-173_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md` to `EJR/EJR-406_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md`;
- preserve semantic body and chronology; change only H1 identity `EJR-173`→`EJR-406`;
- current deterministic census reports zero exact-ID and zero exact-path consumers for EJR-173, so no consumer rewrite is authorized in this change set;
- preserve `EXPECTED_GROUP_COUNT = 31` inside this repair lease.

## Verification contract
After functional mutation, run/read exact-head Internal-ID plus Full-Stack/Runtime/M2 and applicable Real Matrix. If the census exposes legitimate cohort drift, preserve the repair-head failure and use a separate baseline successor. No detector weakening or same-lease rebaseline.

Priority 2 remains OPEN. Global integrity remains HOLD.
