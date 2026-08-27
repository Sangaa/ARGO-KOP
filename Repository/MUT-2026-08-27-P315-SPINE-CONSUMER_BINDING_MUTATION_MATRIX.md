# MUTATION MATRIX — P315 Connected Spine Consumer Binding

Status: `GOVERNED / ISOLATED / NO-PRODUCTION-PROMOTION`

Target: `Runtime/Execution/connected_spine_runner.py`

Evidence Gap: P308 established the isolated RUN-010 → ENG-006 consumer; P314 added the connected-spine invocation seam. The protected runtime change requires an explicitly discoverable mutation matrix.

Intended Minimal Mutation: invoke an injected ENG-006 consumer after authorization and decision-trace recording; preserve simulation when no consumer is supplied.

Acceptance:
- unauthorized execution cannot reach ENG-006;
- RUN-010 reaches ENG-006 only after authorization;
- decision trace ID is preserved;
- ENG-006 result is observable by the spine;
- HOLD/BLOCKED paths remain unchanged;
- Integrity, Integration, Prototype and Matrix Regression remain green.

Non-Claims: no REL-009 promotion, registry edit, production deployment, or authority change.

Rollback: on any gate failure, reject promotion and retain prior runner behavior; never weaken governance checks.

Closure Gate: `MUTATION_MATRIX_PREFLIGHT = PASS` is required before promotion consideration. Green CI alone does not prove real ENG-006 → SRV-009 production connectivity.
