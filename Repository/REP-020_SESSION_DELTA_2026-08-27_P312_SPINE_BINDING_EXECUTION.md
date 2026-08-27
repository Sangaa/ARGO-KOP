# P312 — Connected Spine Binding Execution

Status: `CLOSED / ISOLATED / IMPLEMENTED / CI-GATED`

## Mutation
`connected_spine_runner.py` now has an explicit optional consumer seam for RUN-010. When an authorized RUN-010 fixture supplies an ENG-006 consumer, the spine dispatches through the governed upstream boundary and preserves the decision trace. Without an injected consumer, the legacy simulation remains, preventing an accidental production capability grant.

## Evidence
A dedicated integration test verifies authorized dispatch and trace continuity, plus a compatibility test verifies that the absent-consumer path remains simulation-only.

## Boundary
This mutation does not itself establish production connectivity to a real ENG-006 implementation. The consumer remains injected at the fixture/caller boundary. Therefore REL-009 must remain open until a real connected caller and end-to-end ENG-006 → SRV-009 evidence are demonstrated.

## Gates
The branch must pass the existing Integrity, Integration, Prototype and Mutation Matrix checks before any promotion review.

`RUN-010 → ENG-006 = ISOLATED CONNECTED-SEAM / NOT PRODUCTION-VERIFIED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
