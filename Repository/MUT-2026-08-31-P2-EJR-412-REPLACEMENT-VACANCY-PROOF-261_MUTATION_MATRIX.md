# MUTATION MATRIX — EJR-412 REPLACEMENT VACANCY PROOF 261

Status: PREWRITE / VACANCY-UNPROVEN
Transaction ID: MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261
Opening main: `d0d1d7a528f14cb3706e7fc3dc6ea642b1835e91`
Candidate: `EJR-412`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`

## Pre-write evidence

- Lease260 is CLOSED / AUTHORIZATION-VERIFIED / RESUME-SAFE.
- Current deterministic MEMORY_TO_ROOT baseline is 25.
- Current `EJR/` directory listing contains no EJR-412 allocation.
- Repository search for `EJR-412` currently surfaces only the Session259 warning not to assume vacancy.
- These current-state signals are candidate-discovery evidence only; they are NOT historical vacancy proof.
- Prior Lease256 is DIRECTLY APPLICABLE: complete checkout history + `ejr_allocation_vacancy_gate.py` + artifact + enforced `VACANT` decision are required before any allocation.

## Mutation specification

| Surface | Action in Lease261 | Expected state before proof | Post-proof |
|---|---|---|---|
| EJR-412 allocation | PROVE ONLY | unknown / unproven | PENDING |
| Complete history | READ/ANALYZE | required | PENDING |
| Vacancy artifact | CREATE BY CI | absent | PENDING |
| Root EJR-232 | KEEP | displaced by Lease260 | PENDING |
| Memory EJR-232 | KEEP | retained by Lease260 | PENDING |
| Identity mutation | NONE | forbidden in Lease261 | PENDING |
| MEMORY_TO_ROOT baseline | KEEP | 25 | PENDING |
| Global integrity | KEEP | HOLD | PENDING |

## Permitted material changes

Lease261 may create only:
1. this pre-write matrix,
2. the Lease261 vacancy-proof record,
3. a dedicated GitHub Actions vacancy-proof workflow adapted from the execution-verified Lease256 pattern for candidate EJR-412.

It MUST NOT rename, delete, move, rewrite either EJR-232 member, allocate EJR-412, rewrite consumers, change the census expected count, expand Plan204, or promote global integrity.

## Pre-write decision

`PREWRITE GATE = PASS`

Next: re-read this matrix from current main and require normal push CI success before creating the Lease261 proof record or dedicated proof workflow.
