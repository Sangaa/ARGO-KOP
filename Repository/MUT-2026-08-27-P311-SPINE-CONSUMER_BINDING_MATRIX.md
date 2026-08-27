# P312 — Connected Spine Consumer Binding Mutation Matrix

Status: `GOVERNED / ISOLATED / NO-PRODUCTION-PROMOTION`

## Target
`Runtime/Execution/connected_spine_runner.py`

## Evidence Gap
P308/P310 established a callable isolated `RUN-010 → ENG-006` boundary, while the connected spine still executes `SIMULATED_REVIEW`. The missing relationship is the actual upstream invocation.

## Intended Minimal Mutation
Replace only the hard-coded simulated execution selection with an injected/explicit ENG-006 consumer handoff after authorization and decision-trace recording. Authorization remains owned by the existing authorization gate. No registry or authority changes are part of this mutation.

## Preconditions
1. P308 isolated consumer boundary exists and is tested.
2. P310 mutation governance exists.
3. All current CI gates remain green before mutation.
4. Existing decision-trace and outcome paths remain intact.

## Acceptance
- Unauthorized execution cannot reach ENG-006.
- RUN-010 reaches ENG-006 only after authorization.
- Decision trace ID is preserved across the handoff.
- ENG-006 result is observable by the connected spine.
- Downstream ENG-006 → SRV-009 evidence remains intact.
- Existing HOLD/BLOCKED paths remain unchanged.
- Full Integrity, Integration, Prototype and Matrix Regression suites pass.

## Non-Claims
This matrix does not authorize REL-009 promotion by itself, registry edits, production deployment, or bypassing existing gates.

## Rollback
If any acceptance or governance gate fails, retain the prior simulated runner and reject promotion; do not weaken the guards.
