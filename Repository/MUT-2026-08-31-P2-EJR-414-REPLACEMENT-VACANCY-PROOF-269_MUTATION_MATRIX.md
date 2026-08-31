# MUTATION MATRIX — EJR-414 REPLACEMENT VACANCY PROOF 269

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-414-REPLACEMENT-VACANCY-PROOF-269
Opening main: `9c12a6b78f79b4502ae9b7cab46683b6c23048da`
Lease269 closure commit: `772308fcfc2c79094ae3655d1c94a48f1f83cfd2`

## Trigger

Lease268 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and retains the earlier Memory EJR-235 while classifying the later root EJR-235 displaced.

Current code search returned no EJR-414 claim. That signal was treated as candidate discovery only and not vacancy evidence.

## Executed proof reconciliation

| Surface | Pre-write state | Verified Lease269 state |
|---|---|---|
| Candidate | EJR-414 | EJR-414 only |
| Current-tree search | no claim surfaced | signal only; not used as absence proof |
| Complete reachable history | unproven | PROVEN COMPLETE |
| Current claims | unknown | `[]` |
| Historical claims | unknown | `[]` |
| Vacancy decision | unproven | `VACANT` |
| EJR-414 allocation | none authorized | none performed |
| EJR-235 repair | not authorized here | unchanged |
| EJR/Memory content | current | unchanged |
| Census baseline | 23 | unchanged |
| Global integrity | HOLD | HOLD |

Dedicated proof execution:
- workflow commit `e4d1eba1e5755c6a5e4f84b6d6390828e3e2dd63`;
- EJR Replacement Vacancy Proof 269 run `33377329893`: SUCCESS;
- artifact `9752355789`, digest `sha256:f987d0135c46eb83c6b2b039a4e034d5313eb1f753b5b407cbdea2a6398a38e9`;
- artifact proves `candidate=EJR-414`, `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `history_scope=all locally reachable refs`, `occupied=false`, `vacant=true`, `decision=VACANT`;
- M2 run `33377329920`: SUCCESS.

Lease269 closure commit `772308fcfc2c79094ae3655d1c94a48f1f83cfd2` passed Full-Stack Repository Audit #2386 / run `33379785333` with every repository-audit step SUCCESS.

## Disposition

EJR-414 is vacancy-proven and reserved for exactly one bounded replacement allocation for the displaced root EJR-235 identity authorized by Lease268.

No rename, allocation, delete, content rewrite, consumer rewrite, cohort-baseline update, or integrity promotion occurred in Lease269.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Resume

Matrix269 and Lease269 are CLOSED / EXECUTION-VERIFIED / RESUME-SAFE. A separate pre-write identity-repair lease may now evaluate and, only after fresh hard-gate checks, authorize displaced root EJR-235 → EJR-414.