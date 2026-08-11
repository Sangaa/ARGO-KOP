# Execution Adapter Contract

## Purpose

Define the first executable boundary without connecting ARGO to external systems.

## Input Requirements

An executor may accept only a `PLAN_READY` execution plan with:

- a valid authorization identifier;
- `execution_status = NOT_STARTED`.

## Prototype Output

The mock adapter returns:

```text
SIMULATED
execution_status = SIMULATED_ONLY
side_effect = false
```

## Safety Rule

The mock executor must never send an email, call an external API, modify a production resource, or perform any irreversible operation.

## Future Adapter Rule

Real adapters must preserve the same authorization and plan validation boundary. Replacing the mock implementation with a real adapter must be an explicit governed change, not an automatic fallback.
