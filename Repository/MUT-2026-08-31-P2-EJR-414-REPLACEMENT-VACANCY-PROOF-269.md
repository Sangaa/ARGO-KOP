# MUT-2026-08-31-P2-EJR-414-REPLACEMENT-VACANCY-PROOF-269

Status: OPEN / EXECUTION PENDING
Scope: Candidate replacement identity EJR-414 only; no identity mutation.
Opening main: `9c12a6b78f79b4502ae9b7cab46683b6c23048da`
Pre-write Matrix269: `08543824e9564c60417336fdd97096cb56e080ff`

## Trigger

Lease268 retained the earlier Memory EJR-235 allocation and classified the later root EJR-235 allocation displaced. Current search surfaced no EJR-414 claim, but that result is candidate discovery only.

## Authorized proof

Create one dedicated complete-history workflow for EJR-414. It must use `fetch-depth: 0`, verify `git rev-parse --is-shallow-repository` is false, execute `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-414`, upload its JSON, and fail unless `decision == VACANT`.

## Boundary

No EJR-414 allocation, EJR-235 rename, delete/move, H1/content mutation, consumer rewrite, cohort-baseline update, or Global Integrity promotion is authorized here.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Next

After this opening commit passes repository gates, add the dedicated proof workflow and classify only from its complete-history artifact.