# Reasoning Context Bridge Contract

## Purpose

Define the boundary between Runtime Context/Knowledge Retrieval and Cognition.

## Input

The bridge accepts:

- validated task context;
- retrieved promoted knowledge.

## Output

The bridge emits a reasoning packet containing:

- task/session identity;
- the complete bounded context;
- retrieved knowledge;
- `reasoning_status`;
- `decision_status`;
- `execution_status`.

## Safety Boundary

The bridge does **not**:

- make a decision;
- modify knowledge;
- execute an action;
- call an external service.

Its job is to prepare a clean, traceable input for Cognition.

## State Contract

```text
READY
  ↓
Cognition may reason

NOT_EVALUATED
  ↓
Decision layer has not acted

NOT_REQUESTED
  ↓
Runtime execution has not been requested
```

## Fail-Closed Rule

Incomplete context is rejected. The bridge must never manufacture missing project, scope, task or session information.
