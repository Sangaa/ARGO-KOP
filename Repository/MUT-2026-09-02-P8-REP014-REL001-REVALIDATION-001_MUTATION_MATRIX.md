# P8 — REP-014 REL-001 BOUNDED REVALIDATION MUTATION MATRIX

Transaction ID: `MUT-2026-09-02-P8-REP014-REL001-REVALIDATION-001`
Priority: `8 — Governance`
State: `RESUMED / COMPLETE SOURCE ACQUIRED / MATERIAL MUTATION PENDING`
Entry HEAD: `2c3596691ba501453a8e69ef6769bad61dc41f99`
Pre-write Matrix HEAD: `237a28f3624f86f82a4e4a8fa588b5ae8115b70f`
Hard-Hold checkpoint: `979a394188be157acac6719937b8331fd6eca423`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-014 / CURRENT P8 CLOSURE EVIDENCE`

## Legal-entry proof

Priority 8 is already proven as the first legal open Priority by the immediately preceding P8 transaction. That transaction is `CLOSED / VERIFIED / RESUME-SAFE` but explicitly leaves Priority 8 OPEN because repository-wide relationship integrity remains OPEN and authorizes no queue promotion.

This transaction does not reopen queue reconstruction.

## Smallest material gap selected

`REP-014` still records `REL-001` as `Revalidation Required`:

`SPEC-001-KNOWLEDGE-ORGANIZATION → MOD-001 = DEPENDS_ON`

Current direct source evidence is sufficient for a bounded semantic revalidation:

- `Specifications/01-Knowledge-Organization.md` identifies itself as `SPEC-001-KNOWLEDGE-ORGANIZATION`, states that canonical Models outrank the Specification, and requires reference/dependency authority checking.
- `Models/MOD-001_KNOWLEDGE_MODEL.md` is canonical and explicitly names `Specifications/01-Knowledge-Organization.md` as an active operational specification that provides guidance but does not override the canonical knowledge model.
- The model preserves a bounded evidence caveat: the exact authority relationship remains bounded until the Specifications layer is fully audited. Therefore this transaction MUST NOT promote REL-001 to an unqualified global `Verified` state.

Source checkpoints at entry:

- REP-014 blob: `addee302fad2bf2271b914bc47619392c4ad4509`
- SPEC source blob: `60f2dde6d8632662e411d560f9007dd1eb644965`
- MOD source blob: `7c90c7a8fdcd292237ca1689a8be597d3bd94d23`

## Section Matrix

| Section ID | Semantic section | Action | Preservation rule |
|---|---|---|---|
| S01 | Header / Purpose / Critical Rule / Record schema / controlled types | KEEP | content-equivalent |
| S02 | Current relationship table — REL-001 row only | UPDATE | change only bounded review state |
| S03 | Current relationship table — REL-002..REL-072 | KEEP | byte/content-equivalent |
| S04 | Identity Drift Reconciliation — REL-001 | UPDATE | replace stale unresolved rationale with current bounded source-evidence reconciliation |
| S05 | All other reconciliation/history/evidence sections | KEEP | content-equivalent |
| S06 | This Matrix | UPDATE | finalize material/read-back/test evidence and closure |

## Mutation Matrix

| Change ID | Target | Original evidence | Action | Expected Content | Applied | Verified | Notes |
|---|---|---|---|---|---:|---:|---|
| P8-REL001-01 | `REP-014` REL-001 table row | REP-014 blob `addee302...` | UPDATE | `Revalidated within inspected authority scope` | N | N | no relationship type/direction change |
| P8-REL001-02 | `REP-014` REL-001 reconciliation section | current Identity Drift section | UPDATE | record direct SPEC/MOD identity + authority evidence and bounded disposition | N | N | no global graph claim |
| P8-REL001-03 | all other REP-014 content | REP-014 blob `addee302...` | KEEP | content-equivalent preservation | N | N | complete source now retrievable |
| P8-REL001-04 | this Matrix | current transaction record | UPDATE | record material SHA/read-back/tests/closure | N | N | required before closure |

## HOLD resolution evidence

The earlier HOLD was caused only by response-surface truncation during whole-file retrieval. It is now resolved without changing the governed requirement:

- REP-014 was read in contiguous bounded line ranges through `End of REP-014`, all reporting the same source blob `addee302fad2bf2271b914bc47619392c4ad4509`;
- the same blob was then retrieved directly by blob SHA as one complete source object;
- therefore complete-source candidate reconstruction and Zero-Touch comparison are available before material write.

The semantic evidence and mutation scope are unchanged from the original pre-write Matrix.

## Forbidden boundaries

- no queue promotion;
- no Priority 8 closure claim;
- no repository-wide graph or integrity PASS claim;
- no source mutation to SPEC-001 or MOD-001;
- no new reverse relationship;
- no change from `DEPENDS_ON` without contradictory source evidence;
- no unrelated REP-014 relationship/status edits.

## Verification contract

`COMPLETE SOURCE → MATERIAL COMMIT → EXACT PATH/DIFF CHECK → POST-COMMIT READ-BACK → EXACT-HEAD REQUIRED CI → CLOSE OR HARD HOLD`

Required conditions:

- unexpected changes = `0`;
- REL-001 only is materially altered in REP-014;
- all KEEP sections preserved;
- Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix checks remain green when triggered for the material HEAD.

## Learning

A large-document HOLD caused by response truncation can be resolved safely by stable-blob chunking/direct blob retrieval; the control must be satisfied, not bypassed.