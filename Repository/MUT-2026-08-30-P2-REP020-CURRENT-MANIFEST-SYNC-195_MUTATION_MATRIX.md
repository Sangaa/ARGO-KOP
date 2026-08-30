# MUTATION MATRIX — P2 REP-020 CURRENT-MANIFEST SYNC 195

Transaction ID: `MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195`
Lease: `R71-20260830-P2-REP020-MANIFEST-SYNC-195`
State: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Source head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Prewrite head: `33d983a9edb1c09f85277020f915a38829474d2e`
Source REP-020 current-manifest blob: `41fd422abb52ca97471089db0da06fdb14d01991`
Candidate REP-020 current-manifest blob: `fe628c365a932cc1e8847813dbf928d6c9c7e9af`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 195-001 | Verified source baseline | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Rebind evidence baseline to Lease-194 functional head `855089a454ceab145d0c1c7bd0fb31014218c9d9` | Y | N | Candidate blob `fe628c365a932cc1e8847813dbf928d6c9c7e9af` |
| 195-002 | REP-012 current-manifest row | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Version `1.0.9` → `1.0.10`; status and current boundary unchanged | Y | N | Corrective sync for Lease 194 |
| 195-003 | All other manifest content | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | KEEP | Preserve all unrelated rows, closure boundaries, evidence rules, and global holds | Y | N | Zero-touch validated by candidate construction and pre-ref compare |

## Authorized changed paths

1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
2. `Repository/MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195_MUTATION_MATRIX.md`

Unexpected changed paths required result: `0`.

No REP-012 semantic change, test weakening, EJR mutation, REP-016 mutation, authority promotion, Priority-2 closure, Phase-1 closure, or global PASS is authorized.
