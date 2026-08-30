# MUTATION MATRIX — P2 REP-012 PRE-ALLOCATION VACANCY BINDING 194

Transaction ID: `MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Lease: `R71-20260830-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
State: `CLOSED / FUNCTIONAL ACCEPTED VIA CORRECTIVE SUCCESSOR 195`
Source head: `b2eb68d7bb2dd5831ac5009103faba66b4922f6f`
Prewrite head: `2d83b27c7056b974973f1dea04d7a57f8e31a9f8`
Functional head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Corrective successor functional head: `6bfd767d436eb29c1812f362035b7cfdaa193544`
Source REP-012 blob: `876a55ec87ca15d50bdfe4279bb9e0943b48f42b`
Candidate REP-012 blob: `3e87704439759eca533ae118e36facc51e3eb5eb`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 194-001 | REP-012 metadata/version | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | Version advances from `1.0.9` to `1.0.10`; status/baseline and unrelated metadata preserved | Y | Y | Functional source retained; successor 195 synchronized manifest consumer |
| 194-002 | REP-012 §14 Mutation Protocol | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | For new EJR identity candidates, prove vacancy before `ALLOCATE` across qualified metadata, first H1, filename prefix, and complete locally reachable Git history | Y | Y | Runtime/Integration passed at corrective successor head |
| 194-003 | REP-012 §14 fail-closed semantics | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | ADD | `OCCUPIED` blocks allocation; `HISTORY_INCOMPLETE` blocks allocation; only `VACANT` permits `ALLOCATE` | Y | Y | Gate semantics preserved; no weakening |
| 194-004 | REP-012 all non-target sections | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | KEEP | Preserve all unrelated content and ordering | Y | Y | Functional compare limited to authorized paths |

## Authorized changed paths

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
2. `Repository/MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194_MUTATION_MATRIX.md`

Unexpected changed paths result: `0`.

## Verification note

Original functional head had a correct fail-closed integration failure because the current control-plane manifest remained at REP-012 `1.0.9`. Lease 195 synchronized that consumer, after which Full-Stack `33314345499`, Runtime/Integration `33314345432`, M2 `33314345448`, and Real Matrix `33314345446` all succeeded at `6bfd767d436eb29c1812f362035b7cfdaa193544`.

No EJR artifact mutation, REP-016 mutation, authority promotion, ambiguity suppression, or Priority-2 closure occurred.
