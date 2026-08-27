# P308 — RUN-010 → ENG-006 Upstream Consumer Boundary

Status: `CLOSED / ISOLATED / CONTRACT-IMPLEMENTED / NO-PRODUCTION-MUTATION`

## Evidence
A callable, provider-neutral upstream boundary now exists on the isolated branch. It accepts only RUN-010, requires explicit `AUTHORIZED` status and a non-empty source trace, injects the boundary identity, and delegates to an injected ENG-006 consumer.

## Tests
The isolated test surface covers authorized handoff with trace preservation, unauthorized rejection before consumer invocation, and task-identity rejection.

## Critical limitation
This proves the boundary contract is implementable and testable. It does **not** prove that the connected production spine invokes this boundary. `connected_spine_runner.py` remains unchanged and still builds `SIMULATED_REVIEW`.

## Promotion decision
No merge, no registry update, no REL-009 promotion, and no production authority change are authorized from P308 alone. CI execution of the isolated tests is the next gate.

`RUN-010 → ENG-006 = ISOLATED / TESTABLE / NOT PRODUCTION-VERIFIED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
