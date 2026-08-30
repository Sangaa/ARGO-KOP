# MUT-2026-08-30-P2-DISCOVERABILITY-SYNC-186 — MUTATION MATRIX

Date: 2026-08-30
Lease: `R71-20260830-P2-DISCOVERABILITY-SYNC-186`
Protocol: GOV-014 controlled mutation
State: `CLOSED VIA 187 RECOVERY / ORIGINAL TRANSACTION REJECTED / EXECUTION-VERIFIED`

## Authorized changes

| Change | Protected target | Exact semantic action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 186-A | `Repository/REP-001_MASTER_INDEX.md` | add active discoverability entries for `Core/ARGO_KERNEL.md`, `Core/Core.md`, `Quality/QLT-001_QUALITY_ASSURANCE.md` only; preserve all existing content and holds | three classified active paths discoverable in master index without domain promotion | Y | Y via 187B |
| 186-B | `Repository/REP-002_REPOSITORY_MAP.md` | add corresponding physical mappings for the same three paths only; preserve all existing content and holds | physical map synchronized to REP-001 for the classified scope | Y | Y via 187B |
| 186-C | Mutation Matrix evidence | bind protected mutation to exact same-change-set enforcement | protected transaction accepted by executable GOV-014 preflight | Y | Y via 187A/187B |

## Explicit exclusions

No change was authorized or performed for:
- Knowledge/KNW-001..010
- Architecture/README.md
- Templates/README.md
- any target domain artifact
- REP-014 or REP-016
- Release/VERSION or baseline
- relationship state
- domain certification

## Original execution — rejected

First semantic commit: `3cc385c9ae0a509d2c9d18a0070978f5462a9ea9`.

Its REP-001/REP-002 content was within the authorized semantic scope, but Full-Stack run `33303097603`, job `99234728687`, correctly rejected the protected transaction because the Mutation Matrix was absent from that exact change set:

```text
changed_files=2
protected_changes=2
mutation_matrices=0
MUTATION_MATRIX_PREFLIGHT=FAIL
```

The failed commit remains historical failure evidence and is not retroactively declared valid.

## Governed recovery

Lease 187 / 187A used trusted Git object identity rather than reconstructing large protected documents.

### Stage A — controlled rollback

Commit: `e2c18a18619853fddc3651b0f27afed33ecf64c0`.

Exact changed set:
1. REP-001 → trusted pre-186 blob `75d01dc51b998b0b839db217afb73e17027d79c4`;
2. REP-002 → trusted pre-186 blob `93c758eeb7241231f42063313719ce237d1d4181`;
3. 187 recovery Mutation Matrix created in the same change set.

Unexpected paths: `0`.

Stage-A verification:
- GOV-014 Controlled Document Mutation `33303362401` — SUCCESS
- Real Mutation Matrix Regression `33303362388` — SUCCESS
- Internal Document-ID Audit `33303362399` — SUCCESS
- Full-Stack Repository Audit `33303362384` — SUCCESS
- ARGO Runtime Prototype and Integration Tests `33303362395` — SUCCESS
- M2 `33303362393` — SUCCESS

### Stage B — controlled reapply

Commit: `91c259c04a22f72109fdd9dab75c30be6eebc22b`.

Exact changed set:
1. REP-001 → desired additions-only blob `17b432f27426d3692f9067ebf668d41f18e575b0`;
2. REP-002 → desired additions-only blob `b02d2c1622845e5b9dd46907934ecaad547f050d`;
3. 187 recovery Mutation Matrix updated in the same change set.

Unexpected paths: `0`.

Exact-head verification on `91c259c04a22f72109fdd9dab75c30be6eebc22b`:
- Internal Document-ID Audit `33303432377` — SUCCESS
- Full-Stack Repository Audit `33303432465` — SUCCESS
- ARGO Runtime Prototype and Integration Tests `33303432385` — SUCCESS
- M2 Multi-Channel Proposal Training `33303432378` — SUCCESS
- GOV-014 Controlled Document Mutation `33303432485` — SUCCESS
- Real Mutation Matrix Regression `33303432387` — SUCCESS

## Functional audit impact

Stage-B Internal Document-ID artifact:
- artifact ID `9729674196`
- digest `sha256:8ec9c359cd14c2839c85fcccfdca6df943e21fd4e87376ccf655daf9100a8b40`
- exact head `91c259c04a22f72109fdd9dab75c30be6eebc22b`

Verified result:
- `canonical_unindexed_records: 15 → 12`;
- remaining 12 are exactly `Architecture/README.md`, `Knowledge/KNW-001..010`, and `Templates/README.md`;
- `ambiguous_duplicate_ids = 144`;
- `active_duplicate_pass = true`;
- `filename_alignment_pass = true`;
- metadata conflicts = `[]`;
- Governance heading identity collisions = `{}`;
- unreadable files = `[]`;
- `identity_scope_reconciled = false` remains correctly open.

## Closure

`P2_DISCOVERABILITY_SYNC_186 = CLOSED / EXECUTION-VERIFIED VIA 187B`.

`ORIGINAL_3CC_TRANSACTION = REJECTED / PRESERVED AS FAILURE EVIDENCE`.

`CORE_GLOBAL_CERTIFICATION = NOT_CLOSED`.

`QUALITY_GLOBAL_CERTIFICATION = NOT_CLOSED`.

`PRIORITY_2_GLOBAL_SCOPE = NOT_CLOSED`.

## Learning

`PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING.`

`FAILED PROTECTED EXECUTION MUST BE REPAIRED BY A NEW GOVERNED TRANSACTION, NOT RETROACTIVELY DECLARED VALID.`

`WHEN EXACT TRUSTED BLOBS EXIST, RECOVERY SHOULD PREFER GIT OBJECT IDENTITY OVER RECONSTRUCTING LARGE PROTECTED TEXT.`
