# MUT-2026-08-31-P2-EJR-293-DISPOSITION-AUTHORIZATION-327 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-293-DISPOSITION-AUTHORIZATION-327
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 327-01 | `Repository/MUT-2026-08-31-P2-EJR-293-DISPOSITION-AUTHORIZATION-327.md` | CREATE | evidence-only disposition for EJR-293 | Y | Y |
| 327-02 | current EJR-293 member files | KEEP | no rename/delete/reassignment/allocation | Y | Y |
| 327-03 | MEMORY_TO_ROOT baseline | KEEP | remain 5 during disposition | Y | Y |
| 327-04 | exact-ID semantic references | KEEP / REVIEW-BOUND | no rewrite in disposition; future repair must classify referent before rewrite | Y | Y |

## KEEP REQUIREMENT
Both EJR-293 members remain byte-for-byte unchanged during disposition. No successor is allocated, no consumer is rewritten, baseline remains 5, REP-016 ordering and Runtime implementation remain unchanged, and Priority 2 is not promoted.

## Execution Evidence
Lease326 closed with deterministic MEMORY_TO_ROOT baseline 5 and exact-head Internal-ID / Full-Stack / Runtime-Integration / M2 success. The current census identifies EJR-293 as two distinct members with MEMORY→ROOT lineage and zero exact-member-path consumers.

Direct Git history proves:
- Memory member first allocation `f5132b888a4f4cd16f24b776dd18d8f0138ea6fb` at 2026-08-21T16:20:20Z;
- root member first allocation `951c2053f201d7bbf58dc4dce0f19a2691688a8f` at 2026-08-22T01:32:13Z.

The later root EJR-293 is the Prior-Learning Retrieval Gate record. Later exact-ID references exist, so `zero exact-member-path consumers` is explicitly not promoted into `zero semantic consumers`. No evidence reviewed invalidates the earlier Memory allocation.

## Closure
Disposition is CLOSED / VERIFIED / RESUME-SAFE. `RETAIN = Memory EJR-293`; `DISPLACEMENT CANDIDATE = root EJR-293`. Next legal action is successor candidate discovery plus a separate complete-history vacancy proof before identity mutation, followed by semantic-referent review before any consumer rewrite.
