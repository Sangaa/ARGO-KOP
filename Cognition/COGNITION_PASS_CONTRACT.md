# Cognition Pass Contract

## Purpose

Define the first executable boundary of Cognition.

## Input

A prepared reasoning packet containing:

- task context;
- retrieved promoted knowledge.

## Output

The cognition pass must explicitly expose:

- Facts;
- Assumptions;
- Known Knowledge references;
- Unresolved Questions.

## Non-Authority Rule

The cognition pass does **not** make a decision and does **not** execute an action.

```text
Cognition
   ↓
Decision = NOT_EVALUATED
Execution = NOT_REQUESTED
```

## Fail-Closed Rule

An incomplete reasoning packet produces `HOLD` and must not be interpreted as a successful cognition result.
