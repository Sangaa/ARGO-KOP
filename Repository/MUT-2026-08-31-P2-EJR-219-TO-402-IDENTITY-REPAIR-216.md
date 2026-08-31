# R71-20260831-P2-EJR-219-TO-402-IDENTITY-REPAIR-216

Status: CLOSED / SUCCESSOR-VERIFIED / ONE-RECORD REPAIR / RESUME-SAFE
Baseline: `main@fc1661ad027954b2d6bc462e8089a777fcbb683c`
Prewrite: `c645f7a616560a0a0110ffedb8bb899cf6841089`
Functional head: `0b67b706de7b7a8d54b7f4decc0fa51820e6add6`
Source: `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md`
Replacement: `EJR-402` — proven VACANT by Lease215 / run `33355086518` / artifact `9744861014`.

## Executed repair
Exactly one displaced root record was re-identified:
- old root path removed;
- `EJR/EJR-402_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md` created;
- semantic body/chronology preserved and first H1 identity changed from EJR-219 to EJR-402;
- Memory EJR-219 retained unchanged;
- no unrelated consumer, analyzer, census baseline, or REP authority mutation occurred inside this lease.

## Repair-head evidence preserved
At exact repair head `0b67b706...`:
- Full-Stack `33355206168` — SUCCESS;
- Runtime/Integration `33355206228` — SUCCESS;
- M2 `33355206208` — SUCCESS;
- Real Mutation Matrix `33355206117` — SUCCESS;
- Internal Document-ID Audit `33355206134` — FAILURE only at memory-to-root census.

The failed census artifact `9744912199` proved expected=34, observed=33, history_complete=true, sole incomplete=`__COHORT_COUNT_DRIFT__`; artifact `9744909922` showed `EJR-219` and `EJR-402` no longer ambiguous. The failure is retained as evidence, not rewritten.

## Successor closure
Lease217 separately rebaselined the proven post-repair cohort 34→33. Its exact functional head `f026243...` passed Internal-ID, Full-Stack, Runtime, and M2, and deterministic artifact `9745333997` proves 33/33 CENSUSED with incomplete=[]. Therefore Lease216 closes VERIFIED-THROUGH-SUCCESSOR without conflating identity repair with baseline maintenance.

## Learned rule
A correct bounded repair may intentionally expose a count-drift guard. Preserve that failure, prove the post-repair state, and close through a separate successor; never normalize the baseline inside the repair transaction.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No global PASS claim.
