# MUTATION MATRIX — EJR-413 REPLACEMENT VACANCY PROOF 265

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-413-REPLACEMENT-VACANCY-PROOF-265
Opening main: `9abec7dff2799bb28dcf0708bbb59079bbb2758e`
Pre-write matrix commit: `f2038d02c2776c477818aa79aad1bb1159b4a6fd`
Lease opening commit: `e37ee1a3508a7ed538e838063bdd5a51e8adac99`
Workflow commit: `2e657a7458f0f835ddb1c27b73d46ef96a9dc0c9`
Candidate: `EJR-413`
Source disposition: `MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264.md`

## Proof result

Dedicated complete-history run `33374040160` completed SUCCESS. Artifact `9751158049`, digest `sha256:f127a8d668f2eb1fa2b24081f0c04be22251855109765d21c3ac448fb7b5b48d`, proved:
- `candidate=EJR-413`
- `current_claims=[]`
- `historical_claims=[]`
- `history_complete=true`
- `history_scope=all locally reachable refs`
- `occupied=false`
- `vacant=true`
- `decision=VACANT`

The proof workflow verified a non-shallow checkout and enforced `VACANT` as a hard condition.

## Mutation reconciliation

| Surface | Action in Lease265 | Final verified state |
|---|---|---|
| EJR-413 allocation | PROVE ONLY | VERIFIED VACANT; one bounded future allocation authorized |
| Complete history | READ/ANALYZE | VERIFIED COMPLETE |
| Vacancy artifact | CREATE BY CI | VERIFIED artifact `9751158049` |
| Memory EJR-233 | KEEP | retained unchanged |
| Root EJR-233 | KEEP | displaced but unchanged |
| Identity mutation | NONE | none |
| Consumer rewrite | NONE | none |
| MEMORY_TO_ROOT baseline | KEEP | 24 |
| Global integrity | KEEP | HOLD |

## CI / integration evidence

- Pre-write Matrix265 passed Full-Stack #2365 / `33373910461`, Runtime #2140 / `33373910383`, Real Mutation Matrix #203 / `33373910446`, and M2 #1022 / `33373910426`.
- Lease opening commit passed Full-Stack #2366 / `33373975043`, Runtime #2141 / `33373975079`, and M2 #1023 / `33373975075`.
- Workflow commit passed dedicated vacancy run `33374040160`, Full-Stack #2367 / `33374040106`, and M2 #1024 / `33374040153`.

## Closure

`LEASE265 = CLOSED / EJR-413 VACANT / EXECUTION-VERIFIED / RESUME-SAFE`

EJR-413 is reserved for exactly one bounded replacement allocation for the displaced root EJR-233 record under the next separate identity-repair lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next legal action: open a separate EJR-233 → EJR-413 identity-repair lease with a pre-write Mutation Matrix; re-read the current source and enumerate current consumer obligations before atomic identity mutation.