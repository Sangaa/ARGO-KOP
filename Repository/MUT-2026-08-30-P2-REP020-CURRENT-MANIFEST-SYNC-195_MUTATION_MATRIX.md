# MUTATION MATRIX — P2 REP-020 CURRENT-MANIFEST SYNC 195

Transaction ID: `MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195`
Lease: `R71-20260830-P2-REP020-MANIFEST-SYNC-195`
State: `PREWRITE / NOT APPLIED`
Source head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Source REP-020 current-manifest blob: `41fd422abb52ca97471089db0da06fdb14d01991`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 195-001 | Verified source baseline | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Rebind evidence baseline to Lease-194 functional head `855089a454ceab145d0c1c7bd0fb31014218c9d9` | N | N | Evidence synchronization only |
| 195-002 | REP-012 current-manifest row | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Version `1.0.9` → `1.0.10`; status and current boundary unchanged | N | N | No semantic promotion |
| 195-003 | All other manifest content | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | KEEP | Preserve all unrelated rows, closure boundaries, evidence rules, and global holds | N | N | Zero-touch requirement |

## Authorized changed paths

1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
2. `Repository/MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.

No REP-012 semantic change, test weakening, EJR mutation, REP-016 mutation, authority promotion, Priority-2 closure, Phase-1 closure, or global PASS is authorized.
