# MUTATION MATRIX — Lease223 EJR-404 Replacement Vacancy Proof

Lease: `R71-20260831-P2-EJR-404-REPLACEMENT-VACANCY-PROOF-223`
Baseline: `b1214dcf42c46d641a7d7e58b4727089eb1a121a`

| Surface | Planned mutation | Authority / evidence | Verification |
|---|---|---|---|
| Lease223 record | create prewrite and later closure evidence | Supplement222 + Plan204 | direct read-back |
| Dedicated vacancy workflow | add exact candidate EJR-404 complete-history execution surface | Lease193/Plan204 vacancy rule; existing vacancy gate unchanged | exact-head workflow + artifact |
| EJR records | NONE | forbidden in vacancy lease | no EJR diff |
| REP-022 consumer | NONE | belongs only to separate repair lease after vacancy proof | no consumer diff |
| Census/analyzers | NONE | guard semantics preserved | no quality-code diff |

Failure semantics: any `OCCUPIED`, `HISTORY_INCOMPLETE`, incomplete history, current claim, historical claim, or non-`VACANT` result blocks replacement allocation and closes this lease without repair.
