# MUTATION MATRIX — EJR-413 REPLACEMENT VACANCY PROOF 265

Status: PREWRITE / PROOF-PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-413-REPLACEMENT-VACANCY-PROOF-265
Opening main: `9abec7dff2799bb28dcf0708bbb59079bbb2758e`
Candidate: `EJR-413`
Source disposition: `MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264.md`

## Candidate discovery boundary

A current repository search for `EJR-413` returned no result. This is candidate-screening evidence only and is NOT a vacancy proof.

## Authorized proof-only scope

| Surface | Authorized action | Required proof boundary |
|---|---|---|
| EJR-413 allocation | PROVE ONLY | no allocation or mutation |
| Complete history | READ/ANALYZE | checkout must be non-shallow |
| Vacancy gate | EXECUTE | `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-413` |
| Vacancy artifact | CREATE BY CI | preserve current/historical claim evidence |
| Memory EJR-233 | KEEP | retained unchanged |
| Root EJR-233 | KEEP | displaced but unchanged |
| Identity mutation | NONE | forbidden in Lease265 |
| Consumer rewrite | NONE | forbidden |
| MEMORY_TO_ROOT baseline | KEEP | 24 |
| Global integrity | KEEP | HOLD |

## Hard acceptance

Lease265 may authorize EJR-413 for one bounded future replacement allocation only if dedicated complete-history execution proves all of:
- `current_claims=[]`
- `historical_claims=[]`
- `history_complete=true`
- `occupied=false`
- `vacant=true`
- `decision=VACANT`

Any occupied, incomplete-history, unknown, or non-VACANT result is a HARD HOLD for this candidate and authorizes no fallback mutation inside this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.