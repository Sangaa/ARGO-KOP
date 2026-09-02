# P8 — REP-014 REL-001 BOUNDED REVALIDATION MUTATION MATRIX

Transaction ID: `MUT-2026-09-02-P8-REP014-REL001-REVALIDATION-001`
Priority: `8 — Governance`
State: `BOUNDARY REPAIR / ATOMIC REVERT TO SOURCE`
Entry HEAD: `2c3596691ba501453a8e69ef6769bad61dc41f99`
Pre-write Matrix HEAD: `237a28f3624f86f82a4e4a8fa588b5ae8115b70f`
Hard-Hold checkpoint: `979a394188be157acac6719937b8331fd6eca423`
Hold-resolution checkpoint: `937f4c7fa3a4df7958f223cc3991c9ae5e3ed5fc`
Failed material checkpoint: `a1c0857fef8f6b8330442c19567bef214bcf9c36`
Failed Full-Stack run: `33637504242`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-014 / CURRENT P8 CLOSURE EVIDENCE`

## Legal-entry proof

Priority 8 remains OPEN. This is the same bounded REL-001 transaction; queue reconstruction is not reopened.

## Selected material gap

`REP-014` REL-001 is the only governed target:

`SPEC-001-KNOWLEDGE-ORGANIZATION → MOD-001 = DEPENDS_ON`

Expected bounded state: `Revalidated within inspected authority scope`.

Source checkpoints:

- REP-014 source blob: `addee302fad2bf2271b914bc47619392c4ad4509`
- desired bounded candidate blob already materialized once: `4e52e20d70c44244ad13acd7ebf139b64dc1ded4`
- SPEC source blob: `60f2dde6d8632662e411d560f9007dd1eb644965`
- MOD source blob: `7c90c7a8fdcd292237ca1689a8be597d3bd94d23`

## Section / Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---:|---:|---|
| P8-REL001-01 | `REP-014` REL-001 table row | UPDATE | bounded revalidation state | N | N | desired blob `4e52e20...` |
| P8-REL001-02 | `REP-014` REL-001 reconciliation section | UPDATE | direct SPEC/MOD authority evidence + bounded disposition | N | N | desired blob `4e52e20...` |
| P8-REL001-03 | all other REP-014 content | KEEP | content-equivalent preservation | N | N | Zero-Touch required |
| P8-REL001-04 | this Matrix | UPDATE | travel with protected change in same change set | Y | Y | boundary repair |

## Failure diagnosis

The semantic material commit `a1c0857...` changed exactly one protected path and the diff was confined to REL-001, but Full-Stack preflight failed because the push change set contained `mutation_matrices=0`.

The Matrix existed on the parent, but the current CI contract requires a Mutation Matrix path in the same protected change set. The test is correct; the transaction boundary was wrong.

## Atomic boundary repair

This commit intentionally returns REP-014 to its exact source blob `addee302...` while updating this Matrix in the same commit. It is not a semantic rollback of the decision; it restores a clean governed base so the identical desired candidate blob can be reapplied atomically with this Matrix in the next commit.

Forbidden: changing semantic scope, weakening CI, skipping Matrix enforcement, queue promotion, or claiming P8 closure.

## Verification contract

`ATOMIC SOURCE RESTORE + MATRIX → VERIFY → ATOMIC CANDIDATE + MATRIX → EXACT DIFF → READ-BACK → REQUIRED CI → CLOSE OR HOLD`

## Learning

Pre-write Matrix existence and same-change-set Matrix visibility are distinct controls. A valid Matrix on the parent does not satisfy a CI contract that explicitly verifies protected mutation and Matrix together in one change set.