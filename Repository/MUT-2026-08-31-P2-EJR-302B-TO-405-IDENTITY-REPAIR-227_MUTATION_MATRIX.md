# MUTATION MATRIX — Lease227 EJR-302B→EJR-405

Status: CLOSED / SUCCESSOR-VERIFIED
Baseline: `d93c23a8df6d3c09b450aba97f44de0ea33324e7`
Prewrite: `d37219b06403b3420b93991a09d62e3e626a318a`
Functional repair: `a7434269d28c2f4bf5510497091291a2579feb74`
Successor baseline head: `1972ebe9fd5b32e3eaf5703866e671d697e27975`

| Surface | Authorized change | Result |
|---|---|---|
| remaining root EJR-302 | rename to EJR-405; H1 identity only | DONE |
| GOV-013B | Learning Provenance EJR-302/P221→EJR-405/P221 only | DONE |
| Memory EJR-302 | NONE | UNCHANGED |
| GOV-013B policy/status/version | NONE | UNCHANGED |
| REP surfaces | NONE | UNCHANGED |
| census baseline inside Lease227 | NONE | UNCHANGED; handled by Lease228 |
| analyzers/tests/workflows | NONE | UNCHANGED |

Repair-head gates: Runtime/Real Matrix/M2/Full-Stack SUCCESS; Internal-ID failed solely on deterministic cohort drift 32→31, preserved as evidence. Lease228 separately reconciled and verified baseline 31.
