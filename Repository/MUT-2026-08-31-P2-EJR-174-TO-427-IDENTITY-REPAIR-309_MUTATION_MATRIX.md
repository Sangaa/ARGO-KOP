# Mutation Matrix — Repair 309 — EJR-174 → EJR-427

Date: 2026-08-31
Status: OPEN

## Allowed mutation
One atomic Git-tree identity repair:
- delete root `EJR/EJR-174_2026-08-14_MATRIX_UPDATE_NOTE.md`;
- add root `EJR/EJR-427_2026-08-14_MATRIX_UPDATE_NOTE.md` with preserved substantive content and successor H1.

## Protected boundaries
- Memory EJR-174 must remain byte-identical.
- No historical narrative references are cosmetically rewritten.
- No REP/GOV/Architecture promotion.
- No cohort-baseline normalization in Repair 309.

## Required evidence
1. Live-main re-entry immediately before ref mutation.
2. Atomic tree/commit/ref update; no intermediate duplicate identity state.
3. Exact post-state path checks.
4. Full-Stack SUCCESS.
5. Internal-ID artifact inspection; only expected 10→9 cohort drift is acceptable.

## Closure rule
If the only remaining failure is deterministic cohort-count drift, close the repair evidence and open a separate baseline-normalization lease. Otherwise stop.
