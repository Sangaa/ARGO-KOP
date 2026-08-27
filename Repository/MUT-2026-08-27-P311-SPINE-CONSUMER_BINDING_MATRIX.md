# MUTATION MATRIX — P315 Connected Spine Consumer Binding

Status: `GOVERNED / ISOLATED / NO-PRODUCTION-PROMOTION`

## Target
`Runtime/Execution/connected_spine_runner.py`

## Evidence Gap
P308/P310 established a callable isolated `RUN-010 → ENG-006` boundary. P314 introduced the connected-spine invocation seam. The remaining gap is proof that the changed protected runtime file is governed by an discoverable mutation matrix.

## Intended Minimal Mutation
Bind an injected ENG-006 consumer after authorization and decision-trace recording; preserve simulation when no consumer is supplied.

## Acceptance
- Unauthorized execution cannot reach ENG-006.
- RUN-010 reaches ENG-006 only after authorization.
- Decision trace ID is preserved.
- ENG-006 result is observable by the spine.
- HOLD/BLOCKED behavior remains unchanged.
- Full Integrity, Integration, Prototype and Matrix Regression suites pass.

## Non-Claims
No REL-009 promotion, registry edit, production deployment, or authority change is authorized by this matrix.

## Rollback
On any gate failure, retain the prior runner behavior and reject promotion; never weaken governance checks.

## Closure Gate
`MUTATION_MATRIX_PREFLIGHT = PASS` is required before promotion consideration, and green CI alone does not establish real ENG-006 → SRV-009 production connectivity.
