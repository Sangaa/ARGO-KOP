# MUTATION MATRIX — EJR-232 DISPOSITION AUTHORIZATION 260

Status: PREWRITE / AUTHORIZATION-PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260
Opening main: `6a73fd13f1559380bf537d5ba3a2b73d1d425f42`
Target path: `Repository/MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`

## Pre-write evidence

- Current deterministic MEMORY_TO_ROOT baseline: 25 groups.
- EJR-232 is outside `P2_EJR_CONTROLLED_IDENTITY_REPAIR_PLAN_204.md`; therefore a separate explicit disposition authorization is required before any repair.
- Current census evidence classifies EJR-232 as a two-member Memory→Root ambiguity with distinct semantic bodies and zero external exact-ID / exact-member-path consumer obligations.
- Direct current-main reads confirm both members exist and are semantically distinct.
- Path history establishes the Memory allocation on 2026-08-14 before the root allocation on 2026-08-17.
- Prior EJR-217 Lease255 is DIRECTLY APPLICABLE as the governance pattern: authorize disposition only, then prove a replacement identity vacant in a separate lease before any rename.

## Mutation specification

| Surface | Action | Expected state | Pre-write | Post-write |
|---|---|---|---|---|
| Memory EJR-232 | KEEP | Earlier allocation retained; no content/path/H1 change | VERIFIED | PENDING |
| Root EJR-232 | CLASSIFY ONLY | Later allocation classified displaced; no content/path/H1 change in Lease260 | VERIFIED | PENDING |
| Replacement identity | NONE | No number selected or allocated in Lease260 | VERIFIED | PENDING |
| Consumer rewrites | NONE | Zero direct obligations established; no rewrite in Lease260 | VERIFIED | PENDING |
| MEMORY_TO_ROOT baseline | KEEP | Remains 25 in Lease260 | VERIFIED | PENDING |
| Plan204 scope | KEEP | Original bounded scope is not silently expanded | VERIFIED | PENDING |
| Global integrity | KEEP | HOLD; no global PASS promotion | VERIFIED | PENDING |

## Preservation boundary

Lease260 MUST NOT rename, delete, move, allocate a replacement ID, rewrite either EJR body/H1, alter the census expected count, or promote global integrity. Its only permitted material effect is to record the explicit disposition authorization required for this out-of-Plan204 group.

## Pre-write decision

`PREWRITE GATE = PASS`

The authorization record may now be created as the next single material change. Closure remains pending post-write re-read, commit/blob verification, and matrix reconciliation.
