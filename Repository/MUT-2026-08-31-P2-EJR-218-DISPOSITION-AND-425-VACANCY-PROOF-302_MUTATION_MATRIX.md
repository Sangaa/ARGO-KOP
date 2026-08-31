# Mutation Matrix 302 — EJR-218 Disposition and EJR-425 Vacancy Proof

Status: OPEN / PRE-MUTATION
Date: 2026-08-31
Scope: evidence/disposition/vacancy proof only; no identity mutation.

| Surface | Planned action | Risk | Gate |
|---|---|---|---|
| Memory/Engineering_Journal/EJR-218_2026-08-14_P35_SESSION_CLOSURE.md | retain EJR-218 allocation | identity | first-valid chronology |
| EJR/EJR-218_CURRENT_BUILD_RECONCILIATION_2026-08-17.md | candidate displaced root record | identity | no mutation in this lease |
| EJR-425 | candidate successor | allocation | complete-history vacancy proof mandatory |
| .github/workflows/ejr-replacement-vacancy-proof-302.yml | add bounded proof workflow | CI/evidence | artifact inspection required |

Decision basis:
- current cohort baseline: 12;
- EJR-218 current exact-ID external references: 5;
- exact member-path consumers: 0;
- Memory first seen 2026-08-14T15:35:19+03:00;
- root first seen 2026-08-17T16:47:18+03:00;
- chronology relation: RIGHT_FIRST_SEEN_ANCESTOR (Memory first).

Non-claims: no ownership promotion, no canonicality promotion, no Global Integrity promotion.
