# MUTATION MATRIX — P2 REP-012 PRE-ALLOCATION VACANCY BINDING 194

Transaction ID: `MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Lease: `R71-20260830-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
State: `PREWRITE / NOT APPLIED`
Source head: `b2eb68d7bb2dd5831ac5009103faba66b4922f6f`
Source REP-012 blob: `876a55ec87ca15d50bdfe4279bb9e0943b48f42b`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 194-001 | REP-012 metadata/version | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | Version advances from `1.0.9` to `1.0.10`; status/baseline and unrelated metadata preserved | N | N | Contract amendment only |
| 194-002 | REP-012 §14 Mutation Protocol | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | UPDATE | For new EJR identity candidates, prove vacancy before `ALLOCATE` across qualified metadata, first H1, filename prefix, and complete locally reachable Git history | N | N | Lease 193 evidence binding |
| 194-003 | REP-012 §14 fail-closed semantics | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | ADD | `OCCUPIED` blocks allocation; `HISTORY_INCOMPLETE` blocks allocation; only `VACANT` permits `ALLOCATE` | N | N | No current-tree-absence shortcut |
| 194-004 | REP-012 all non-target sections | source blob `876a55ec87ca15d50bdfe4279bb9e0943b48f42b` | KEEP | Preserve all unrelated content and ordering | N | N | Zero-touch requirement |

## Authorized changed paths

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
2. `Repository/MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.

No EJR artifact mutation, REP-016 mutation, authority promotion, ambiguity suppression, or Priority-2 closure is authorized.
