# R RECOVERY V2 MUTATION MATRIX

Transaction: `MUT-2026-09-01-R-RECOVERY-V2`
State: `MATERIAL-RECOVERY-CANDIDATE / CI-PENDING / LEASE ACTIVE`
Entry HEAD: `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`
Pre-write V2 Matrix HEAD: `28ddda52577cbffaa24d0f43ba01f3ac49ea698b`
Original incident: `c38783c38962063a7fc38f6c99adad3547e4e6fd`
Recovery V1 Matrix: `671123cc83655bc35e8d07b60e0c416eb5b396e9`
V1 sequencing deviation: `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`

## Recovery state

The unintended empty file `Repository/INVALID_SHOULD_NOT_CREATE.tmp` is authorized for removal in this V2 material candidate. The existing incident record, V1 Matrix, Transaction-R candidate paths, REP-014, Core status, and all canonical authority sources are KEEP.

## Authorized remaining corrective change set — exactly 2 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| RV2-01 | `Repository/INVALID_SHOULD_NOT_CREATE.tmp` | REMOVE unintended empty artifact | Y | PENDING CI |
| RV2-02 | this Matrix | UPDATE/rebind V2 candidate state | Y | PENDING CI |

Candidate must be exactly one commit after `28ddda52577cbffaa24d0f43ba01f3ac49ea698b` and exactly these two paths. Unexpected path expansion = `0`.

## Preservation boundary

- no history rewrite, reset, or force push;
- preserve original incident commit, V1 Matrix, and incident record;
- preserve all Transaction-R semantic/test/evidence paths unchanged;
- preserve REP-014 v1.2.14 and REL-001..072 unchanged;
- preserve Core status v1.3.11 and Priority 7 OPEN;
- no Core/Runtime/Architecture source mutation;
- no certification, Phase-1, Connected-Baseline, repository-wide-graph, or Global-PASS promotion.

## Failure classification retained

1. Original accidental direct write: `IMPLEMENTATION_FAILURE / ORIGINAL WRITE NON-COMPLIANT`.
2. Recovery V1 split write: `IMPLEMENTATION_FAILURE / MATRIX-SEQUENCING NON-COMPLIANCE`.
3. First recovery-Matrix tool attempt blocked before write: `INFRASTRUCTURE/TOOLING LIMITATION`, no repository mutation.

Existing GOV-014/014A controls are sufficient to classify the execution failures. No new governance rule is promoted from this single incident chain.

## Verification contract

`EXACT-HEAD READ-BACK -> ONE-COMMIT/TWO-PATH DIFF -> TEMP ABSENCE DIRECT CHECK -> FOUR REQUIRED WORKFLOWS WHEN TRIGGERED/APPLICABLE -> JOB/STEP REVIEW -> FAILURE/LEARNING ASSESSMENT -> V2 CLOSURE -> RETURN TO R`.

If workflow trigger count differs because this recovery change does not touch a workflow-specific trigger surface, inspect the workflows that actually trigger and do not invent missing run evidence. Full-Stack and Runtime/Integration remain mandatory checkpoint evidence before returning to R.

## Learning

The current session supports a bounded `SESSION-LEARNING`: before every write-capable invocation, verify both **authorization** and **transaction boundary/atomicity**. This is application/refinement of GOV-014/014A, not a new rule.
