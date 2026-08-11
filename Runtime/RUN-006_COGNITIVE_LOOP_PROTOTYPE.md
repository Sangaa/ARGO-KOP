# RUN-006 — COGNITIVE LOOP PROTOTYPE

Platform: ARGO KOP
Document ID: RUN-006
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Runtime Prototype
Priority: Critical
Date: 2026-08-11

---

# Purpose

Define a safe first runtime prototype for proving the cognitive execution loop before enabling external or irreversible actions.

# Prototype Flow

```text
Input
 ↓
Load bounded context
 ↓
Reason
 ↓
Generate decision candidate
 ↓
Validate
 ↓
Human authorization
 ↓
Generate proposed action
 ↓
Record result
```

The prototype stops before automatic external execution.

# Input

The prototype accepts one bounded task with:

- task identifier;
- source/evidence;
- session/thread identifier;
- active state;
- applicable knowledge/rules;
- requested outcome.

# Context

Only context selected for the current task is loaded. Full repository hydration is not required.

The context package must preserve source references so every material conclusion can be traced back to evidence.

# Reasoning Output

The reasoning stage returns a structured result containing:

- observations;
- analysis;
- uncertainty;
- hypotheses where applicable;
- decision candidates;
- required clarification;
- evidence references.

# Validation

The validation stage checks:

- required evidence;
- authority boundaries;
- applicable constraints;
- unresolved dependencies;
- output completeness.

A failed or unresolved validation state blocks authorization.

# Authorization

For the first prototype, authorization is human-controlled.

No model-generated statement can implicitly authorize its own action.

# Action

The initial action output is non-destructive:

- draft;
- structured proposal;
- decision record;
- test artifact;
- proposed repository patch.

No external side effect is applied automatically.

# Traceability

The prototype must preserve:

```text
Input → Context → Reasoning → Decision → Validation → Authorization → Action → Result
```

Each stage must remain distinguishable in the resulting trace.

# Success Criteria

The prototype is successful only when it can demonstrate:

1. bounded context selection;
2. traceable reasoning;
3. explicit decision candidate;
4. validation gate;
5. explicit human authorization;
6. safe proposed action;
7. complete execution trace.

# Failure Criteria

The prototype fails if it:

- silently invents missing context;
- bypasses validation;
- treats reasoning as authorization;
- executes external action without authorization;
- loses provenance;
- reports completion when the action was only proposed.

# Related Contracts

- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Engine/ENG-009_CONTEXT_ENGINE.md`
- `Cognition/COG-010_REASONING_PIPELINE_BOUNDARY.md`
- `Engine/ENG-002_DECISION_ENGINE.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`
- `Engine/ENG-006_EXECUTION_ENGINE.md`

# Integrity Hold

This document defines the first safe runtime prototype target. It is not an implementation claim.

---

End of Document
