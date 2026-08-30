# MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-REPAIR-187

Date: 2026-08-30
Lease: `R71-20260830-P2-MATRIX-SAME-CHANGESET-REPAIR-187`
Execution role: HERMUZ
Entry baseline: `main@3cc385c9ae0a509d2c9d18a0070978f5462a9ea9`
Status: `CLOSED / EXECUTION-VERIFIED / 186 RECOVERED`

## Trigger

Lease 186 first executed the classified REP-001/REP-002 discoverability synchronization at commit `3cc385c9ae0a509d2c9d18a0070978f5462a9ea9` after complete-source reconstruction, additions-only candidate comparison, final live-parent recheck and `force=false` fast-forward.

The protected content itself matched the authorized semantic scope, but Full-Stack Repository Audit run `33303097603`, job `99234728687`, correctly rejected the transaction at `Enforce Mutation Matrix on current change set` because the Matrix was not modified in the exact same protected commit:

```text
changed_files=2
protected_changes=2
mutation_matrices=0
MUTATION_MATRIX_PREFLIGHT=FAIL
```

Classification:

`PROTECTED CONTENT SEMANTICS = WITHIN AUTHORIZED SCOPE`

`ORIGINAL TRANSACTION EVIDENCE BINDING = FAILED / SAME-CHANGE-SET CONTRACT VIOLATION`

The original commit is preserved as failure evidence and is not retroactively promoted.

## Recovery method

Lease 187A authorized a two-stage Git-object recovery using exact trusted blobs rather than reconstructing large protected text.

### Stage A — controlled rollback

Commit:
`e2c18a18619853fddc3651b0f27afed33ecf64c0`

The exact changed set was:

1. REP-001 restored to trusted pre-186 blob `75d01dc51b998b0b839db217afb73e17027d79c4`;
2. REP-002 restored to trusted pre-186 blob `93c758eeb7241231f42063313719ce237d1d4181`;
3. the 187 recovery Mutation Matrix created in that same change set.

Unexpected paths: `0`.

Stage-A gates:

- Full-Stack `33303362384` — SUCCESS;
- Internal Document-ID `33303362399` — SUCCESS;
- Runtime/Integration `33303362395` — SUCCESS;
- M2 `33303362393` — SUCCESS;
- GOV-014 Controlled Document Mutation `33303362401` — SUCCESS;
- Real Mutation Matrix Regression `33303362388` — SUCCESS.

### Stage B — controlled reapplication

Commit:
`91c259c04a22f72109fdd9dab75c30be6eebc22b`

The exact changed set was:

1. REP-001 → desired classified discoverability blob `17b432f27426d3692f9067ebf668d41f18e575b0`;
2. REP-002 → desired classified discoverability blob `b02d2c1622845e5b9dd46907934ecaad547f050d`;
3. the 187 recovery Mutation Matrix updated in that same change set.

Unexpected paths: `0`.

Stage-B exact-head verification:

- Internal Document-ID Audit `33303432377` — SUCCESS;
- Full-Stack Repository Audit — SUCCESS on exact Stage-B head;
- Runtime/Integration `33303432385` — SUCCESS;
- M2 — SUCCESS on exact Stage-B head;
- Real Mutation Matrix Regression — SUCCESS;
- GOV-014 mutation enforcement — SUCCESS.

The closed recovery Matrix on current main preserves the exact run identifiers for all Stage-B channels.

## Functional result

The Stage-B Internal Document-ID artifact is:

- artifact `9729674196`;
- exact head `91c259c04a22f72109fdd9dab75c30be6eebc22b`;
- digest `sha256:8ec9c359cd14c2839c85fcccfdca6df943e21fd4e87376ccf655daf9100a8b40`.

It proves:

- `tracked_files_scanned = 2066`;
- `document_id_records = 1099`;
- `active_duplicate_pass = true`;
- `filename_alignment_pass = true`;
- `canonical_unindexed_records = 12`, down from 15;
- the three Lease-186 paths are no longer canonical-unindexed;
- `ambiguous_duplicate_ids = 144`, down from 145 after the separate EJR-013 reconciliation;
- metadata conflicts = `[]`;
- Governance heading identity collisions = `{}`;
- unreadable = `[]`;
- `identity_scope_reconciled = false` remains outside this bounded repair.

## Closed scope

The following discoverability gaps are execution-verified closed:

- `Core/ARGO_KERNEL.md`;
- `Core/Core.md`;
- `Quality/QLT-001_QUALITY_ASSURANCE.md`.

Core and Quality global certification remain unchanged.

Priority 2 global identity reconciliation remains open because the remaining raw population contains already-classified non-admitted canonical claims and non-authoritative historical/provenance ID reuse that require separate disposition, not silent suppression.

## Learning promoted within execution method scope

`PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING.`

`A PROTECTED MUTATION IS NOT EXECUTION-VERIFIED UNTIL THE MATRIX IS VISIBLE IN THE EXACT CHANGE SET ENFORCED BY CI.`

`WHEN EXACT TRUSTED BLOBS EXIST, RECOVERY SHOULD PREFER GIT OBJECT IDENTITY OVER RECONSTRUCTING LARGE PROTECTED TEXT.`

`FAILED SAME-CHANGE-SET BINDING SHOULD BE REPAIRED BY A NEW GOVERNED TRANSACTION, NOT RETROACTIVELY DECLARED VALID.`

## Closure

`P2_MATRIX_SAME_CHANGESET_REPAIR_187 = CLOSED / EXECUTION-VERIFIED`.

`P2_DISCOVERABILITY_SYNC_186 = CLOSED VIA 187 RECOVERY`.

`PRIORITY_2_GLOBAL_SCOPE = OPEN`.
