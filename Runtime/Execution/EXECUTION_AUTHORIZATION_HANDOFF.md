# Execution Authorization Handoff

## Purpose

Make the final handoff from Authorization to the execution adapter explicit and non-implicit.

## Required Handoff

```text
AUTHORIZED
   +
PLAN_READY
   +
execution_status = NOT_STARTED
   +
authorization_id
        ↓
Execution Adapter
```

## Rejection Rules

The adapter must reject the handoff when:

- the plan is not `PLAN_READY`;
- execution is not `NOT_STARTED`;
- authorization identity is absent;
- the request attempts to bypass the authorization state.

## Prototype Boundary

The current adapter is mock-only. A successful handoff produces `SIMULATED` and `SIMULATED_ONLY`, with `side_effect=false`.

No external email, API call, production mutation, or irreversible action is permitted by this prototype boundary.

## Governance

A future real adapter requires an explicit governed implementation change. It must not be activated by replacing configuration alone.
