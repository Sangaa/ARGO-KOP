# P323 — REL-009 Reverse-Evidence Reconciliation Matrix

Status: `GOVERNED / ISOLATED / NO-PROMOTION`

## Gap
P4 canonical evidence classified `REL-009` as one-way because `SRV-009` did not independently name `RUN-010`. P314/P320/P321 subsequently established an implemented connected-spine path in which RUN-010 dispatches through ENG-006 to the existing SRV-009 adapter.

## Minimal Mutation
Update only the canonical `SRV-009` relationship position and related-document list to describe the bounded RUN-010 path through ENG-006. Do not claim that every SRV-009 operation originates in RUN-010.

## Acceptance
- Reverse endpoint explicitly names RUN-010.
- The relationship remains bounded through ENG-006.
- No authority transfer is implied.
- Existing validation/authorization/post-write controls remain unchanged.
- P4 remains limited to its listed critical edge set.
- CI and repository integrity gates pass.

## Non-Claims
No production deployment, live canonical mutation, REL-009 release promotion, or generalized RUN-010 ownership of SRV-009 is authorized by this matrix.

## Revalidation
After mutation, re-read SRV-009, re-read P4, verify both directions and affected consumer evidence, then run CI.
