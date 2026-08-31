# MUTATION MATRIX — Lease227 EJR-302B→EJR-405

Status: FUNCTIONAL WRITE EXECUTED / VERIFICATION PENDING
Baseline: `d93c23a8df6d3c09b450aba97f44de0ea33324e7`
Prewrite: `d37219b06403b3420b93991a09d62e3e626a318a`

| Surface | Authorized change |
|---|---|
| remaining root EJR-302 record | rename to EJR-405 path; H1 identity only |
| GOV-013B | synchronize Learning Provenance `EJR-302 / P221` → `EJR-405 / P221` only |
| Memory EJR-302 | NONE |
| GOV-013B status/version/policy body | NONE |
| REP surfaces | NONE unless exact dependency is proven before functional write |
| census baseline | NONE inside repair lease |
| analyzers/tests/workflows | NONE |

Verification pending: direct read-back, old-path absence, retained Memory read-back, GOV provenance read-back, compare, Internal-ID artifact, Full-Stack, Runtime, M2, Real Mutation Matrix. Any proven cohort drift is handled only by a separate successor lease.
