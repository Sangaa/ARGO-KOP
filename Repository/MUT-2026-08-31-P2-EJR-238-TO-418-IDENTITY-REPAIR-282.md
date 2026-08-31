# MUT-2026-08-31-P2-EJR-238-TO-418-IDENTITY-REPAIR-282

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: one-record Priority-2 identity repair: displaced root EJR-238 → EJR-418.
Opening main: `b993e0640453c1a433572a86b8f9fe53005f9e28`
Pre-write Matrix282: `68fe711a45e891b4d795863afda6a5e578c579c4`
Functional repair head: `b584ef39aa9f277d1b552dd4fa631185e5229fc0`

## Authority and execution

Lease281 retained the earlier Memory EJR-238, displaced the later root EJR-238, and proved EJR-418 VACANT across complete reachable history. EJR-418 was reserved solely for this repair.

Retained `Memory/Engineering_Journal/EJR-238_2026-08-15_P56_SESSION_CLOSURE.md` unchanged. Replaced root `EJR/EJR-238_2026-08-17_P322_RECONCILIATION_UPDATE.md` with `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md`, changing only the first H1 identity and preserving historical body references unchanged. No consumer rewrite was required.

Exact compare from repair opening to repair head classified exactly one renamed file with +1/-1.
Full-Stack #2452 / run `33388263948`: SUCCESS.
Repair-head census artifact `9756436545` showed expected=19, observed=18, history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Lease283 separately normalized the cohort baseline to 18. Final Internal Document-ID Audit #73 / run `33388442676`: SUCCESS; final artifact `9756500240` is 18/18 CENSUSED with no incomplete IDs. Full-Stack #2455 / run `33388442711`: SUCCESS.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
