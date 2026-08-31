# MUTATION MATRIX — Repair 312 EJR-248 → EJR-428

Transaction ID: MUT-2026-08-31-P2-EJR-248-TO-428-312
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 312-A | Root EJR-248 path | DELETE/REPLACE ATOMICALLY | No intermediate duplicate identity | N | N |
| 312-B | Root EJR-428 path | CREATE ATOMICALLY | Same journal content under successor identity | N | N |
| 312-C | Memory EJR-248 | KEEP | First-valid allocation unchanged | N | N |

## KEEP REQUIREMENT
Memory EJR-248 content and all unrelated repository artifacts must remain unchanged. Historical narrative references remain historical unless executable/canonical consumers prove otherwise.

## Execution Evidence
Lease 311 complete-history artifact returned EJR-428 = VACANT with no current or historical claims.

## Closure
Close only after post-state read-back, Internal Document-ID evidence, Full-Stack success, and provenance-artifact inspection. Any deterministic cohort-count drift is handled in a separate lease.
