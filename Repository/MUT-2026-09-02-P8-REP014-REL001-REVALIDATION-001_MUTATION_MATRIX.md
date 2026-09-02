# P8 — REP-014 REL-001 BOUNDED REVALIDATION MUTATION MATRIX

Transaction ID: `MUT-2026-09-02-P8-REP014-REL001-REVALIDATION-001`
Priority: `8 — Governance`
State: `MATERIAL APPLIED / READ-BACK + EXACT-HEAD CI PENDING`
Entry HEAD: `2c3596691ba501453a8e69ef6769bad61dc41f99`
Pre-write Matrix HEAD: `237a28f3624f86f82a4e4a8fa588b5ae8115b70f`
Hard-Hold checkpoint: `979a394188be157acac6719937b8331fd6eca423`
Hold-resolution checkpoint: `937f4c7fa3a4df7958f223cc3991c9ae5e3ed5fc`
Failed split-boundary material checkpoint: `a1c0857fef8f6b8330442c19567bef214bcf9c36`
Failed Full-Stack run: `33637504242`
Atomic source-restore checkpoint: `e8bf25a456fd843beb5802581de0809e07bafe66`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-014 / CURRENT P8 CLOSURE EVIDENCE`

## Legal-entry proof

Priority 8 remains OPEN. This is the same bounded REL-001 transaction; queue reconstruction is not reopened.

## Selected material gap

`REP-014` REL-001 only:

`SPEC-001-KNOWLEDGE-ORGANIZATION → MOD-001 = DEPENDS_ON`

Expected bounded state: `Revalidated within inspected authority scope`.

Source/candidate checkpoints:

- REP-014 source blob: `addee302fad2bf2271b914bc47619392c4ad4509`
- REP-014 desired candidate blob: `4e52e20d70c44244ad13acd7ebf139b64dc1ded4`
- SPEC source blob: `60f2dde6d8632662e411d560f9007dd1eb644965`
- MOD source blob: `7c90c7a8fdcd292237ca1689a8be597d3bd94d23`

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---:|---:|---|
| P8-REL001-01 | `REP-014` REL-001 table row | UPDATE | `Revalidated within inspected authority scope` | Y | N | same desired blob previously diff-checked |
| P8-REL001-02 | `REP-014` REL-001 reconciliation section | UPDATE | direct SPEC/MOD authority evidence + bounded disposition | Y | N | no reverse/global claim |
| P8-REL001-03 | all other REP-014 content | KEEP | content-equivalent preservation | Y | N | source/candidate differ only in governed REL-001 scope |
| P8-REL001-04 | this Matrix | UPDATE | accompany protected mutation in same change set | Y | N | fixes CI transaction-boundary failure |

## Failure diagnosis and repair

The first semantic material commit `a1c0857...` was content-bounded but failed Full-Stack because the protected change set contained no Matrix path. The pre-existing Matrix on its parent did not satisfy current CI same-change-set enforcement.

The transaction was returned exactly to source in `e8bf25a...`, with REP-014 restored to blob `addee302...` and this Matrix included in that protected change set. This material retry now reapplies the already inspected desired candidate blob `4e52e20...` while updating this Matrix in the same atomic tree/commit.

No semantic scope changed during repair.

## Forbidden boundaries

- no queue promotion;
- no Priority 8 closure claim before exact-head verification;
- no repository-wide graph or integrity PASS claim;
- no source mutation to SPEC-001 or MOD-001;
- no new reverse relationship;
- no relationship-type change;
- no unrelated REP-014 edits;
- no weakening/bypass of Matrix CI.

## Verification contract

`ATOMIC CANDIDATE + MATRIX → EXACT TWO-PATH COMPARE → REP-014 + MATRIX READ-BACK → EXACT-HEAD REQUIRED CI → CLOSE OR HARD HOLD`

Required:

- unexpected changes = `0`;
- protected semantic diff confined to REL-001;
- Matrix visible in same change set;
- Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix checks green when triggered.

## Learning

The governed unit is not merely the document mutation; it is the mutation plus its pre-existing specification made visible to the verifier under the verifier's actual comparison boundary.