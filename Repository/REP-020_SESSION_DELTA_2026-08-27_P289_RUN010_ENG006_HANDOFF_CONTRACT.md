# P289 — RUN-010 → ENG-006 HANDOFF CONTRACT

Date: 2026-08-27
Status: COMPLETED / CONTRACT-ONLY / NO RUNTIME WIRING
Protocol: GOV-013
Parent: P288

## Purpose

Define the minimum evidence contract required before an existing RUN-010 execution result may be handed to the existing governed ENG-006/SRV-009 callable surface.

## Source-of-truth boundaries

`Runtime/RUN-010_RUNTIME_REFERENCE.md` describes the governed relationship:

`Decision Candidate → Validation → Authorization → ENG-006 Execution → SRV-009 Controlled Mutation → Post-Write Validation / Re-read`

It explicitly states that this is a relationship description, not proof that every runtime operation follows the path.

`Services/ENG006_SRV009_PRODUCTION_ADAPTER.py` is the existing callable downstream surface. It requires an explicitly authorized `ProductionExecutionCandidate`, provenance via `source_trace_id`, repository target/content/purpose/necessity evidence, governed dispatch, and post-write read-back.

## Required handoff fields

A future RUN-010 → ENG-006 handoff must independently establish:

1. `execution_id` — originating execution identity.
2. `task_id` — identity continuity with RUN-010.
3. `session_id` — session continuity.
4. `source_trace_id` — trace continuity into the governed execution entrypoint.
5. `authorized=True` — explicit authorization; connector availability is insufficient.
6. `path` — concrete repository target, if mutation is actually intended.
7. `content` — exact mutation payload, if applicable.
8. `purpose` — declared operation purpose.
9. `necessity_evidence` — evidence supporting why the mutation is necessary.
10. `commit_message` — governed mutation description.

## Gate conditions

The handoff MUST be rejected unless all of the following are independently evidenced:

- RUN-010 execution result is the actual originating execution result, not a reconstructed or inferred object.
- Authorization status is explicit and traceable.
- The originating decision/execution trace remains linked to the handoff.
- The handoff reaches the existing callable ENG-006/SRV-009 adapter without bypassing validation or authorization controls.
- `dispatch_write(...)` remains the only governed mutation dispatcher.
- Post-write read-back remains mandatory for an accepted mutation.
- Downstream `ENG-006 → SRV-009` evidence remains attributable to the actual invocation.

## Negative boundary

The following do NOT establish the handoff:

- the existence of `RUN-010_RUNTIME_REFERENCE.md`;
- a simulated `connected_spine_runner` result;
- existence of the downstream adapter alone;
- an isolated ENG-006/SRV-009 E2E test;
- connector availability;
- a successful CI run that does not execute the complete handoff.

## Implementation gate

No production wiring is authorized by this contract alone. The next mutation is permitted only after a runtime-native test or execution trace demonstrates the complete handoff using the existing callable surface and preserves every listed gate condition.

## Closure

`RE-READ → CONTRACT EXTRACTION → FIELD/TRACE REQUIREMENTS → NEGATIVE BOUNDARY → IMPLEMENTATION GATE → RECORD → CLOSE`

Final state:

`HANDOFF CONTRACT = DEFINED`
`RUN-010 → ENG-006 = NOT EXECUTABLE-VERIFIED`
`PRODUCTION RUNTIME = UNCHANGED`
`AUTHORITY = UNCHANGED`
`SESSION = CLOSED`
