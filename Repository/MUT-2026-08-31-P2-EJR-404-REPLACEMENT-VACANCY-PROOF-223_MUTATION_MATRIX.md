# MUTATION MATRIX — Lease223 EJR-404 Replacement Vacancy Proof

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Lease: `R71-20260831-P2-EJR-404-REPLACEMENT-VACANCY-PROOF-223`
Baseline: `b1214dcf42c46d641a7d7e58b4727089eb1a121a`
Functional head: `5e2b658262af36b4119cca9ba7c99866107abd03`

| Surface | Mutation | Evidence / result |
|---|---|---|
| Lease223 record | prewrite then closure evidence | direct read-back required |
| Dedicated vacancy workflow | added exact EJR-404 complete-history execution surface | run `33358057935` SUCCESS |
| Vacancy artifact | deterministic proof | ID `9745762164`; digest `sha256:82c35b7cdd1b279609291604aff0dc5f10af2ef3c8b6de6902b95ea09ed0c897`; `decision=VACANT`; `history_complete=true`; no current/historical claims |
| EJR records | NONE | vacancy lease performed no allocation or rename |
| REP-022 consumer | NONE | reserved for separate repair lease |
| Census/analyzers | NONE | guard semantics preserved |

Closure rule satisfied: complete history proved EJR-404 vacant. This authorizes only a future separate repair lease; it does not itself allocate or mutate the identifier.
