# MUTATION MATRIX — P2 SAME-CHANGE-SET RECOVERY 187 STAGE A

Transaction ID: `MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187-A`
Protocol: GOV-014 v1.0.1

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 187A-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | restore trusted pre-186 blob `75d01dc51b998b0b839db217afb73e17027d79c4` for controlled rollback | Y | N |
| 187A-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | restore trusted pre-186 blob `93c758eeb7241231f42063313719ce237d1d4181` for controlled rollback | Y | N |
| 187A-003 | `Repository/MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187_MUTATION_MATRIX.md` | CREATE | same-change-set recovery evidence preserving failed 186 lineage | Y | N |

## KEEP REQUIREMENT

All other content is `KEEP`.

## Execution Evidence

- Parent recovery authorization: `Repository/MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187A.md`.
- Rejected protected transaction: `3cc385c9ae0a509d2c9d18a0070978f5462a9ea9`.
- Failed Full-Stack run: `33303097603`; job `99234728687`.
- Failure: `protected_changes=2 / mutation_matrices=0 / MUTATION_MATRIX_PREFLIGHT=FAIL`.
- Stage A restores exact trusted pre-186 protected blobs so Stage B can reapply the already-classified discoverability change under same-change-set enforcement.
- Unexpected Changes = 0 is required at post-bind compare; verification pending.

## Closure

`STAGE_A = CONTROLLED ROLLBACK / VERIFICATION PENDING`.
