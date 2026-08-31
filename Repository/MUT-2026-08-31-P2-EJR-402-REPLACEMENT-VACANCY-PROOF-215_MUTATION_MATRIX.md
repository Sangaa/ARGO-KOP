# Mutation Matrix — Lease 215

Status: OPEN
Baseline: `2b9564a1438df809fe119d83c39d5d9e4b2a712d`

| Surface | Authorized action | Boundary |
|---|---|---|
| Lease 215 | create/update closure evidence | authority record only |
| Lease 215 Matrix | create/update in lockstep | no semantic authority expansion |
| `.github/workflows/ejr-replacement-vacancy-proof-215.yml` | create bounded EJR-402 proof workflow | existing vacancy gate unchanged |
| `Quality/Integration/ejr_allocation_vacancy_gate.py` | execute/read only | NO MODIFY |
| EJR records | read only | NO ALLOCATION / NO REWRITE |
| Census baseline | read only | preserve 34 |

Exit: VACANT proof or evidence-preserving STOP.
