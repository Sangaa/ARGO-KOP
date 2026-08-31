# MUT-2026-08-31-P2-EJR-414-REPLACEMENT-VACANCY-PROOF-269

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Candidate replacement identity EJR-414 only; no identity mutation.
Opening main: `9c12a6b78f79b4502ae9b7cab46683b6c23048da`
Pre-write Matrix269: `08543824e9564c60417336fdd97096cb56e080ff`
Dedicated proof workflow commit: `e4d1eba1e5755c6a5e4f84b6d6390828e3e2dd63`

## Trigger

Lease268 retained the earlier Memory EJR-235 allocation and classified the later root EJR-235 allocation displaced. Current search surfaced no EJR-414 claim, but that result was candidate discovery only.

## Executed complete-history proof

The dedicated `.github/workflows/ejr-replacement-vacancy-proof-269.yml` workflow checked out complete history (`fetch-depth: 0`), verified the checkout was non-shallow, executed `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-414`, uploaded its JSON, and enforced `decision == VACANT`.

Execution evidence:
- EJR Replacement Vacancy Proof 269 run `33377329893`: SUCCESS.
- Artifact `9752355789`, digest `sha256:f987d0135c46eb83c6b2b039a4e034d5313eb1f753b5b407cbdea2a6398a38e9`.
- Artifact result: `candidate=EJR-414`, `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `history_scope=all locally reachable refs`, `occupied=false`, `vacant=true`, `decision=VACANT`.
- M2 run `33377329920`: SUCCESS on the same workflow commit.

## Classification

EJR-414 is VACANT across complete reachable history and is reserved for exactly one bounded replacement allocation for the displaced root EJR-235 identity authorized by Lease268.

## Boundary

No EJR-414 allocation, EJR-235 rename, delete/move, H1/content mutation, consumer rewrite, cohort-baseline update, or Global Integrity promotion occurred in Lease269.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Resume

Lease269 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE. The next bounded step may open a separate pre-write identity-repair lease for displaced root EJR-235 → EJR-414, with fresh source/blob, target-absence, consumer, and live-main checks immediately before mutation.