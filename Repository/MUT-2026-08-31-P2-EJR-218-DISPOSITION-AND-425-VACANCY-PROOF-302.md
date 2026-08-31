# Lease 302 — EJR-218 Disposition and EJR-425 Vacancy Proof

Status: OPEN / EVIDENCE GATE
Date: 2026-08-31

## Disposition Candidate
Under the first-valid historical allocation rule, current evidence supports retaining EJR-218 on `Memory/Engineering_Journal/EJR-218_2026-08-14_P35_SESSION_CLOSURE.md` and treating `EJR/EJR-218_CURRENT_BUILD_RECONCILIATION_2026-08-17.md` as the later root allocation, subject to vacancy proof for a successor.

Chronology evidence:
- Memory first seen: `551694caa2ada1a82c8e777fd7d33e03adae8cb9` at 2026-08-14T15:35:19+03:00.
- Root first seen: `b9b2de77f61d589a6c6c76086400e70f13da3d30` at 2026-08-17T16:47:18+03:00.
- Relation: `RIGHT_FIRST_SEEN_ANCESTOR`.

Current exposure:
- exact-ID external references: 5;
- exact member-path references: 0.

## Hard Gate
Candidate successor `EJR-425` MUST be proven vacant against complete repository history before any rename/reassignment. Current search absence is not vacancy proof.

## Allowed Mutation
This lease may add only the evidence/matrix/workflow needed to prove vacancy. Identity mutation is prohibited until the workflow artifact explicitly returns `VACANT` and the proof-head CI is inspected.

Global Integrity remains HOLD.
