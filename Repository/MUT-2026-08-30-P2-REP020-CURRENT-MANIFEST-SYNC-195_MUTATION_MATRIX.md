# MUTATION MATRIX — P2 REP-020 CURRENT-MANIFEST SYNC 195

Transaction ID: `MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195`
Lease: `R71-20260830-P2-REP020-MANIFEST-SYNC-195`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Source head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Prewrite head: `33d983a9edb1c09f85277020f915a38829474d2e`
Functional head: `6bfd767d436eb29c1812f362035b7cfdaa193544`
Source REP-020 current-manifest blob: `41fd422abb52ca97471089db0da06fdb14d01991`
Candidate REP-020 current-manifest blob: `fe628c365a932cc1e8847813dbf928d6c9c7e9af`

| Change ID | Section ID | Original Hash / Source Identity | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---|---|---|
| 195-001 | Verified source baseline | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Rebind evidence baseline to Lease-194 functional head `855089a454ceab145d0c1c7bd0fb31014218c9d9` | Y | Y | Exact-head verification complete |
| 195-002 | REP-012 current-manifest row | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | UPDATE | Version `1.0.9` → `1.0.10`; status and current boundary unchanged | Y | Y | Corrective consumer synchronization only |
| 195-003 | All other manifest content | source blob `41fd422abb52ca97471089db0da06fdb14d01991` | KEEP | Preserve all unrelated rows, closure boundaries, evidence rules, and global holds | Y | Y | Read-back confirms preserved hold semantics |

## Authorized changed paths

1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
2. `Repository/MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195_MUTATION_MATRIX.md`

Unexpected changed paths result: `0`.

## Verification evidence

At `6bfd767d436eb29c1812f362035b7cfdaa193544`:

- Full-Stack Repository Audit `33314345499` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests `33314345432` — SUCCESS.
- M2 Multi-Channel Proposal Training `33314345448` — SUCCESS.
- Real Mutation Matrix Regression `33314345446` — SUCCESS.

No REP-012 semantic change, test weakening, EJR mutation, REP-016 mutation, authority promotion, Priority-2 closure, Phase-1 closure, or global PASS occurred.
