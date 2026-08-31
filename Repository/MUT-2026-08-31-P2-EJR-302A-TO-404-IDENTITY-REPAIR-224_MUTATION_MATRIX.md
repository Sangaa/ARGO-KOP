# MUTATION MATRIX — Lease224 EJR-302A→EJR-404

Status: OPEN / PREWRITE
Baseline: `6639e061fdff9d838a86567b0044e6a75df0dd4f`

| Surface | Authorized change |
|---|---|
| GT-041 root EJR record | remove old EJR-302 path; add EJR-404 path; H1 identity only |
| REP-022 | synchronize exact learning-record path EJR-302→EJR-404 |
| Memory EJR-302 | NONE |
| second root EJR-302 CI Decision Boundary | NONE |
| GOV-013B | NONE |
| census/analyzers/tests/workflows | NONE |

Verification: direct read-back, old-path absence, retained-surface read-back, compare, Internal-ID artifact, Full-Stack, Runtime, M2, Real Mutation Matrix. No rebaseline unless separately proven by successor evidence.
