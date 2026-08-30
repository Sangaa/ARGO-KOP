# MUTATION MATRIX — P2 SAME-CHANGE-SET RECOVERY 187 STAGE B

Transaction ID: `MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187-B`
Protocol: GOV-014 v1.0.1
State: `CLOSED / VERIFIED / RECOVERY COMPLETE`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 187B-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | reapply exact classified discoverability blob `17b432f27426d3692f9067ebf668d41f18e575b0` | Y | Y |
| 187B-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | reapply exact classified discoverability blob `b02d2c1622845e5b9dd46907934ecaad547f050d` | Y | Y |
| 187B-003 | `Repository/MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-RECOVERY-187_MUTATION_MATRIX.md` | UPDATE | bind reapplication to same-change-set Matrix evidence | Y | Y |

## KEEP REQUIREMENT

All other content is `KEEP`. Core and Quality holds remain unchanged. The twelve intentionally unindexed Knowledge/Architecture/Templates paths remain excluded.

## Rejected source transaction

The first semantic commit `3cc385c9ae0a509d2c9d18a0070978f5462a9ea9` is retained as failed lineage only. Full-Stack run `33303097603`, job `99234728687`, correctly rejected it at `Enforce Mutation Matrix on current change set` with:

`protected_changes=2 / mutation_matrices=0 / MUTATION_MATRIX_PREFLIGHT=FAIL`.

It is not retroactively declared valid.

## Controlled recovery

### Stage A — rollback with Matrix

Commit: `e2c18a18619853fddc3651b0f27afed33ecf64c0`.

Exact changed set:
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- this Matrix

Unexpected changes: `0`.

Stage-A exact-head verification:
- Full-Stack `33303362384` — SUCCESS
- Internal Document-ID `33303362399` — SUCCESS
- Runtime/Integration `33303362395` — SUCCESS
- M2 `33303362393` — SUCCESS
- GOV-014 Controlled Document Mutation `33303362401` — SUCCESS
- Real Mutation Matrix Regression `33303362388` — SUCCESS

### Stage B — classified reapply with Matrix

Commit: `91c259c04a22f72109fdd9dab75c30be6eebc22b`.

Exact changed set:
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- this Matrix

Unexpected changes: `0`.

Post-write protected blobs:
- REP-001 = `17b432f27426d3692f9067ebf668d41f18e575b0`
- REP-002 = `b02d2c1622845e5b9dd46907934ecaad547f050d`

Stage-B exact-head verification:
- Real Mutation Matrix Regression `33303432387` — SUCCESS
- M2 `33303432378` — SUCCESS
- Runtime/Integration `33303432385` — SUCCESS
- Full-Stack `33303432465` — SUCCESS
- GOV-014 Controlled Document Mutation `33303432485` — SUCCESS
- Internal Document-ID Audit `33303432377` — SUCCESS

Internal-ID artifact:
- artifact ID `9729674196`
- digest `sha256:8ec9c359cd14c2839c85fcccfdca6df943e21fd4e87376ccf655daf9100a8b40`
- head `91c259c04a22f72109fdd9dab75c30be6eebc22b`
- `canonical_unindexed_records = 12`
- `ambiguous_duplicate_ids = 144`
- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `identity_scope_reconciled = false`

## Closure

`P2_MATRIX_SAME_CHANGESET_RECOVERY_187 = CLOSED / EXECUTION-VERIFIED`.

The recovery closes the transaction-governance failure only. It does not close repository-wide Priority 2 or any broader domain/global hold.
