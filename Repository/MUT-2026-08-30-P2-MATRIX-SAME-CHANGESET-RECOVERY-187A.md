# MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187A

Date: 2026-08-30
Parent lease: `R71-20260830-P2-MATRIX-SAME-CHANGESET-REPAIR-187`
Execution role: HERMUZ
Status: `PREWRITE / TWO-STAGE PROTECTED RECOVERY AUTHORIZED`

## Reason

The first Lease 186 protected commit `3cc385c9ae0a509d2c9d18a0070978f5462a9ea9` changed REP-001 and REP-002 without a Mutation Matrix changed in the exact same commit. Full-Stack run `33303097603`, job `99234728687`, correctly failed with `protected_changes=2 / mutation_matrices=0`.

A direct provenance-note rewrite was considered, but the safe connected write surface does not provide a partial-file patch primitive for these large protected files. Reconstructing them again is unnecessary because Git already provides the exact trusted pre-186 and desired post-186 blobs.

## Authorized recovery method

Use Git object identity rather than textual reconstruction:

### Stage A — controlled rollback

From fresh live main, create one commit that changes exactly:

1. `Repository/REP-001_MASTER_INDEX.md` → trusted pre-186 blob `75d01dc51b998b0b839db217afb73e17027d79c4`.
2. `Repository/REP-002_REPOSITORY_MAP.md` → trusted pre-186 blob `93c758eeb7241231f42063313719ce237d1d4181`.
3. `Repository/MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187_MUTATION_MATRIX.md` → Stage-A matrix evidence.

This rollback is not a semantic rejection of the three discoverability paths. It restores the last pre-186 protected state so the rejected transaction can be re-applied under the executable same-change-set contract.

### Stage B — controlled reapply

Only after Stage-A changed-set/read-back and Mutation Matrix preflight evidence are acceptable, create one commit that changes exactly:

1. `Repository/REP-001_MASTER_INDEX.md` → desired discoverability blob `17b432f27426d3692f9067ebf668d41f18e575b0`.
2. `Repository/REP-002_REPOSITORY_MAP.md` → desired discoverability blob `b02d2c1622845e5b9dd46907934ecaad547f050d`.
3. the same 187 Mutation Matrix → Stage-B reapply evidence.

The desired blobs are the additions-only candidates already compared against the pre-186 parent: REP-001 `+10/-0`; REP-002 `+10/-0`.

## Required safeguards

For each stage:

- fresh live-parent discovery;
- create tree from that exact parent;
- final parent recheck;
- `update_ref(main, ..., force=false)` only;
- exact changed-file set = the two protected registries + 187 Matrix;
- read-back;
- no new canonical paths beyond the original three;
- preserve Core/Quality holds and all global holds.

Stage B is not closed until Internal Document-ID Audit, Full-Stack, Runtime/Integration and M2 succeed on the exact Stage-B head.

## Learning

`WHEN EXACT TRUSTED BLOBS EXIST, RECOVERY SHOULD PREFER GIT OBJECT IDENTITY OVER RECONSTRUCTING LARGE PROTECTED TEXT.`

`FAILED SAME-CHANGE-SET BINDING SHOULD BE REPAIRED BY A NEW GOVERNED TRANSACTION, NOT RETROACTIVELY DECLARED VALID.`
