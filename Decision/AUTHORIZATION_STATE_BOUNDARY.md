# Authorization State Boundary

## Purpose

Define the authority boundary between a decision proposal and runtime execution.

## Rules

1. Only `PROPOSAL_READY` may enter authorization.
2. `REVIEW_REQUIRED`, `HOLD`, or any unknown proposal state is blocked.
3. Authorization requires explicit approval; silence or missing authorization is denial.
4. Successful authorization produces `AUTHORIZED` only.
5. Authorization never starts execution by itself.
6. Authorization identity and authorization ID must remain traceable.

## State Flow

```text
PROPOSAL_READY
      ↓
Authorization Check
   ↙           ↘
missing       approved
  ↓              ↓
BLOCKED      AUTHORIZED
                 ↓
          execution NOT_STARTED
```

## Security Boundary

This contract intentionally separates **permission** from **execution**. A future runtime executor must consume the `AUTHORIZED` state through its own execution contract.
