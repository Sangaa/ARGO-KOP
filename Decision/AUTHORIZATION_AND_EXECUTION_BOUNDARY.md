# Authorization and Execution Boundary

## Purpose

Separate a proposed decision from permission to execute it.

## States

```text
PROPOSAL_READY
      ↓
Authorization Required
      ├── denied / missing → BLOCKED
      └── approved → AUTHORIZED
                         ↓
                    PLAN_READY
                         ↓
                    NOT_STARTED
```

## Rule

A proposal is not authorization.

Authorization must be explicit and traceable through an authorization identifier and actor.

## Execution Plan

An authorized proposal may produce a side-effect-free execution plan. Creating the plan does not execute the action.

## Current Safety Boundary

The current implementation contains no external side effects. `SEND_EMAIL`, API calls, filesystem mutations and other real actions remain outside this prototype.
