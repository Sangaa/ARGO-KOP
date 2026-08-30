# MUTATION MATRIX — P2 REP-012 PRE-ALLOCATION VACANCY BINDING 194

Transaction ID: `MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Lease: `R71-20260830-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
State: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Source head: `b2eb68d7bb2dd5831ac5009103faba66b4922f6f`
Prewrite head: `2d83b27c7056b974973f1dea04d7a57f8e31a9f8`
Source REP-012 blob: `876a55ec87ca15d50bdfe4279bb9e0943b48f42b`
Candidate REP-012 blob: `3e87704439759eca533ae118e36facc51e3eb5eb`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 194-001 | REP-012 metadata/version | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | Version advances from `1.0.9` to `1.0.10`; status/baseline and unrelated metadata preserved | Y | N | Candidate blob `3e87704439759eca533ae118e36facc51e3eb5eb` |
| 194-002 | REP-012 §14 Mutation Protocol | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | For new EJR identity candidates, prove vacancy before `ALLOCATE` across qualified metadata, first H1, filename prefix, and complete locally reachable Git history | Y | N | Lease 193 evidence binding |
| 194-003 | REP-012 §14 fail-closed semantics | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | ADD | `OCCUPIED` blocks allocation; `HISTORY_INCOMPLETE` blocks allocation; only `VACANT` permits `ALLOCATE` | Y | N | No current-tree-absence shortcut |
| 194-004 | REP-012 all non-target sections | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | KEEP | Preserve all unrelated content and ordering | Y | N | Zero-touch validation required before ref update |

## Authorized changed paths

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
2. `Repository/MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.

No EJR artifact mutation, REP-016 mutation, authority promotion, ambiguity suppression, or Priority-2 closure is authorized.
