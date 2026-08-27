# P314 — Connected Spine Consumer Binding

Status: `ISOLATED / CI-IN-FLIGHT / NO-PROMOTION`

## Mutation
`Runtime/Execution/connected_spine_runner.py` now invokes the injected `RUN-010 → ENG-006` consumer after authorization and decision-trace recording, while preserving simulation when no consumer is supplied.

## Evidence
- Consumer boundary: `RUN-010→ENG-006`.
- Authorization is required before dispatch.
- `source_trace_id` is passed from the decision trace into the consumer and returned.
- Existing HOLD/BLOCKED paths are unchanged.
- Existing simulation fallback remains explicit.

## Governance
P312 mutation matrix applies. No registry, authority, or production deployment change is included.

## CI
CI was observed in progress for commit `01e49b572dec764c60ba8e4f66c7d84d7e5d16af`; no final result is claimed in this record.

## Promotion Gate
Even with green CI, this proves only connected-spine invocation of an injected consumer. `REL-009` remains unverified until the injected consumer is bound to the real governed ENG-006 → SRV-009 production adapter and full end-to-end evidence is captured.

`RUN-010 → ENG-006 = CONNECTED-SPINE BOUND / REAL PROVIDER NOT YET VERIFIED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
