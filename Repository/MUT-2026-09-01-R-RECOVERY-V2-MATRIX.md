# R RECOVERY V2 MUTATION MATRIX

Transaction: `MUT-2026-09-01-R-RECOVERY-V2`
State: `PRE-WRITE RECOVERY V2 / LEASE ACTIVE`
Entry HEAD: `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`
Original incident: `c38783c38962063a7fc38f6c99adad3547e4e6fd`
Recovery V1 Matrix: `671123cc83655bc35e8d07b60e0c416eb5b396e9`

## Why V2 exists

Recovery V1 required removal of the unintended temp file, creation of the incident record, and Matrix update in one material commit. The incident record was instead created alone in commit `86d4ea5c...`. That path was authorized, but the required atomicity sequence was not followed.

Classification: `IMPLEMENTATION_FAILURE / MATRIX-SEQUENCING NON-COMPLIANCE`.

V1 remains historical evidence and is not relabeled as successful.

## Authorized remaining corrective change set — exactly 2 paths

1. `Repository/INVALID_SHOULD_NOT_CREATE.tmp` — REMOVE the unintended empty artifact.
2. This Matrix — UPDATE with recovery candidate and verification state.

The existing incident record and all Transaction-R paths are KEEP and must remain unchanged in the V2 material candidate.

## Preservation boundary

- no history rewrite, reset, or force push;
- preserve original incident commit, V1 Matrix, and incident record;
- preserve R semantic candidate and focused test unchanged;
- preserve REP-014 v1.2.14 and REL-001..072 unchanged;
- preserve Core status v1.3.11 and Priority 7 OPEN;
- no Core/Runtime/Architecture source mutation;
- no certification or Global PASS promotion.

## Verification

`PRE-WRITE V2 MATRIX -> ONE MATERIAL COMMIT / EXACTLY TWO PATHS -> TEMP FILE ABSENT -> MATRIX REBOUND -> REQUIRED CI/INTEGRATION -> JOB/STEP REVIEW -> V2 CLOSURE -> RETURN TO R`.

Unexpected path expansion = `0`.

## Learning

The second failure reinforces the same session-level lesson: authorization is not enough; the required transaction boundary and atomicity must also be checked before invoking a write action. No new governance rule is promoted because GOV-014/014A already express transactional and pre-write discipline.
