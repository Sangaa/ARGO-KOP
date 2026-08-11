# Mock Execution Contract

## Purpose

Validate the final execution boundary without touching external systems.

## Input

A `PLAN_READY` execution plan with `execution_status = NOT_STARTED`.

## Output

```text
SIMULATED
execution_status = SIMULATED_ONLY
side_effect = false
```

## Blocking Rules

- non-ready plans are blocked;
- invalid execution states are blocked;
- the mock executor never sends emails, calls external APIs, mutates production data, or performs irreversible operations.

## Architectural Role

This is a test muscle for the future real executor. It proves the system can traverse the complete logical chain without granting external side effects.
