# R71-20260831-P2-EJR-402-REPLACEMENT-VACANCY-PROOF-215

Status: OPEN / VACANCY PROOF ONLY
Baseline: `main@2b9564a1438df809fe119d83c39d5d9e4b2a712d`
Target future repair: `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md`
Replacement candidate: `EJR-402`

## Authority
Supplement214 and Plans 203–204 require selecting one remaining displaced record by lowest rewrite risk, then proving a replacement candidate VACANT through complete locally reachable history before any allocation or identity rewrite.

Two current-main searches for the exact EJR-219 displaced path/name returned only analytical Plans 203/204; no current operational synchronous consumer rewrite was established. EJR-301 and both EJR-302 displaced records carry explicit consumer/provenance obligations, so EJR-219 is the lowest presently established rewrite-risk target.

Current code search returned no EJR-402 claim. This is candidate discovery only, not proof of vacancy.

## Allowed mutation
- Add this lease and mutation matrix atomically.
- Add a dedicated workflow that executes the existing `Quality/Integration/ejr_allocation_vacancy_gate.py` unchanged against `EJR-402` with complete history.
- Record resulting workflow/artifact evidence and close only if decision is `VACANT`.

## Forbidden
No EJR allocation, rename, delete, H1 rewrite, consumer rewrite, census-baseline change, scanner weakening, registry promotion, or global-status promotion.

## Exit gate
`history_complete=true`, `current_claims=[]`, `historical_claims=[]`, `decision=VACANT`, plus applicable regressions. Otherwise STOP and preserve evidence.
