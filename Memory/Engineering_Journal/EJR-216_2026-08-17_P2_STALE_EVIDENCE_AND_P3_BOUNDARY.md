# EJR-216 — P2 Stale Evidence + P3 Executable Boundary

Date: 2026-08-17
Status: RECORDED / SESSION-CLOSABLE
Baseline: 3.2.1

## Work Completed

1. Re-read current REP-001 and REP-002 against the GOV-014 seven-entry candidate.
2. Detected that the seven-entry candidate was stale; all seven entries were already present in current-main.
3. Refused duplicate mutation and marked `Tools/GOV-014_REP001_INDEX_RECONCILIATION_CANDIDATE.md` stale/superseded.
4. Confirmed current REP-021 already records P2 as reconciled within verified active inventory; the older REP-016 P2-open statement is retained as stale queue evidence pending explicit queue resynchronization.
5. Re-read RUN-010, ENG-006 and SRV-009.
6. Performed independent repository searches for callable SRV-009 consumer evidence; none was established in the inspected scope.
7. Recorded current priority state and executable boundary in `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md`.

## Result

`P1 = CLOSED`

`P2 = RECONCILED within verified active inventory`

`P3 = OPEN / CONTRACTUAL / PARTIALLY VERIFIED / NOT EXECUTABLE-PROMOTED`

## Learning

A candidate built from an earlier evidence snapshot can become stale after repository mutations. The pre-mutation gate must always re-read the current canonical target and reject duplicate work.

Queue state and domain evidence may temporarily diverge. The newer authoritative evidence must drive operational interpretation while the stale queue statement remains visible until explicitly resynchronized.

Contract evidence, callable consumer evidence, test evidence and trace evidence remain distinct states and must not be collapsed into one promotion decision.

## Next Safe Action

Acquire independent callable/test/trace evidence for `RUN-010 → ENG-006 → SRV-009`, while separately resynchronizing the stale P2 state in REP-016 through a full-content-preserving queue mutation.

End of EJR-216
