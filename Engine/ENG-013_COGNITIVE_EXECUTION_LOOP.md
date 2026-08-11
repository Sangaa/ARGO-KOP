# ENG-013 — COGNITIVE EXECUTION LOOP

Platform: ARGO KOP
Document ID: ENG-013
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Engine Integration
Priority: Critical
Date: 2026-08-11

---

# Purpose

Define the smallest governed end-to-end loop connecting Context, Cognition, Decision, Validation and Execution without granting automatic external-action authority.

This is an integration contract and prototype target, not a claim of existing executable implementation.

# Loop

```text
Event / Request
      ↓
ENG-009 Context Engine
      ↓
COG-010 Reasoning Boundary
      ↓
ENG-002 Decision Engine
      ↓
ENG-004 Validation Engine
      ↓
Authorization Gate
      ↓
ENG-006 Execution Engine
      ↓
Observed Result
      ↓
Learning Candidate
```

# State Contract

```text
CANDIDATE
   ↓
UNDER_REVIEW
   ↓
VALIDATED
   ↓
AUTHORIZED
   ↓
EXECUTING
   ↓
COMPLETED
```

Any applicable failure, uncertainty or authority conflict may transition to `HOLD`, `REJECTED` or `FAILED` according to the controlling component.

# Critical Separation

- Context selection does not decide.
- Cognition does not authorize.
- Decision does not bypass validation.
- Validation does not execute.
- Execution does not create authority.
- Completion does not automatically create learning.

# Minimum Prototype

The first executable proof should operate on a non-destructive action candidate such as generating a draft, producing a structured decision record, or proposing a repository change without applying it.

The prototype must expose:

- input/event;
- selected context;
- reasoning result;
- decision candidate;
- validation result;
- authorization state;
- proposed action;
- final outcome;
- provenance.

# Safety Boundary

No automatic external email, irreversible mutation, production deployment or destructive repository operation is implied by this contract.

Human review may remain the authorization gate for early prototypes.

# Relationship to Existing Contracts

- `Engine/ENG-009_CONTEXT_ENGINE.md`
- `Cognition/COG-010_REASONING_PIPELINE_BOUNDARY.md`
- `Engine/ENG-002_DECISION_ENGINE.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`
- `Engine/ENG-006_EXECUTION_ENGINE.md`
- `Engine/ENG-012_ENGINE_AI_EXECUTION_BOUNDARY.md`

# Integrity Hold

ENG-013 becomes executable only after the referenced contracts and their service/runtime consumers are validated as one path.

# Guiding Statement

**The first proof of ARGO's cognitive architecture should be a safe, traceable, reversible loop—not unrestricted automation.**

---

End of Document
