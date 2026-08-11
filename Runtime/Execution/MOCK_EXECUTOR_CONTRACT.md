# Mock Executor Contract

## Purpose

Test the final execution boundary without creating real external side effects.

## Input

Only a `PLAN_READY` execution plan carrying a valid `authorization_id` may enter simulation.

## Output

```text
SIMULATED
 ├── action
 ├── target
 ├── authorization_id
 └── side_effect = false
```

## Safety Rule

The mock executor must never send email, call an external API, mutate production data, or perform another real-world side effect.

## Boundary

This component validates the orchestration path only. A future real executor must be a separate adapter with its own authorization, policy and safety controls.
