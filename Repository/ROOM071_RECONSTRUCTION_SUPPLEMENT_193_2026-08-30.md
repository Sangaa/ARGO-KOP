# ROOM 071 RECONSTRUCTION SUPPLEMENT 193 — 2026-08-30

Session state: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Entry head: `cb9dd60f2d910958c792ccb53d2db15bee077786`
Prewrite head: `804660b573af97ba4752393bfd8e7ea7696873a0`
Functional head: `2c6507ee6fced85a2c56eb17befadbd36ae1665f`

## Completed

- Re-entered from Lease 192 after independently rediscovering current `main`.
- Confirmed Lease 192 had already completed the six-group EJR provenance census and identified allocation/discovery failure as the next bounded P2 defect.
- Re-read REP-012 and confirmed its material mutation sequence begins at `ALLOCATE` without an explicit pre-allocation vacancy proof.
- Re-read the current Internal-ID scanner and established that it proves current-tree metadata/H1 identity but does not itself prove historical vacancy.
- Re-read the Internal-ID workflow and found the default checkout was not sufficient for a historical vacancy proof.
- Opened Lease 193 before functional mutation.
- Created `Quality/Integration/ejr_allocation_vacancy_gate.py`.
- Created `Quality/Integration/test_ejr_allocation_vacancy_gate.py`.
- Updated Internal Document-ID workflow to `fetch-depth: 0`, explicitly verify non-shallow history, and execute the new gate regressions alongside the existing audit suite.
- Functional compare proved exactly four authorized changed paths and no unexpected paths.
- Exact-head CI passed across Internal-ID, Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix.
- Read-back matched exact candidate blobs.
- No EJR, REP-012, REP-016, detector ambiguity membership or authority state was mutated.

## Execution evidence

Functional head: `2c6507ee6fced85a2c56eb17befadbd36ae1665f`.

- Internal Document-ID Audit `33310451501` — SUCCESS.
- Full-Stack Repository Audit `33310451462` — SUCCESS.
- Runtime/Integration `33310451475` — SUCCESS.
- M2 `33310451492` — SUCCESS.
- Real Mutation Matrix Regression `33310451464` — SUCCESS.

Internal-ID artifact:

- ID `9731811306`;
- digest `sha256:8c1e8b89b6f5d10edd187f569e057327ac95869cff0cef6390008faee249ac7d`;
- exact head `2c6507ee6fced85a2c56eb17befadbd36ae1665f`.

## Verified decision semantics

`OCCUPIED` — qualifying current or historical identity evidence exists.

`HISTORY_INCOMPLETE` — no visible occupancy was found, but history is shallow; vacancy is not proven.

`VACANT` — no qualifying claim exists in the current tree or all locally reachable history and the repository is non-shallow.

The gate's historical authority is bounded to all locally reachable refs. It does not claim knowledge of unreachable external history.

## New learning

`VACANCY IS A PROVEN NEGATIVE CLAIM, NOT THE ABSENCE OF A CURRENT-TREE MATCH.`

`A VACANCY CHECK WITH INCOMPLETE HISTORY MUST FAIL CLOSED, NOT RETURN UNUSED.`

## Resume point

Next bounded work:

`P2 REP-012 PRE-ALLOCATION VACANCY BINDING`

Use Lease 193 execution evidence to amend REP-012 in a separate protected transaction so candidate identity vacancy is proven before `ALLOCATE`.

Do not combine the REP-012 binding with an EJR migration. Do not reopen Release Priority 20. Do not suppress the 121 EJR ambiguity groups. Do not allocate a replacement EJR merely because its number looks unused.

## Preserved holds

- Priority 2 historical/provenance identity scope: OPEN.
- Phase 1 overall: OPEN.
- Global Connected Baseline: OPEN.
- Provider Authentication: HARD HOLD where real trust anchor is absent.
- Global `BOOTED / INTEGRITY PASS`: NOT CLAIMED.

Session is CLOSED / RESUME-SAFE.
