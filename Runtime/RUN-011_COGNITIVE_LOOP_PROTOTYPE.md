# RUN-011 — COGNITIVE LOOP PROTOTYPE

Platform: ARGO KOP
Document ID: RUN-011
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Runtime Prototype
Priority: Critical
Date: 2026-08-11

---

# Purpose

Define the first safe runtime proof for the cognitive loop without enabling unrestricted external automation.

# Prototype Flow

```text
Input
 ↓
Bounded Context
 ↓
Cognition
 ↓
Decision Candidate
 ↓
Validation
 ↓
Human Authorization
 ↓
Non-destructive Action Proposal
 ↓
Trace / Result
```

# Required Inputs

- task identifier;
- session/thread identifier;
- active state;
- source/evidence references;
- selected knowledge/rules;
- requested outcome.

# Required Outputs

The prototype must expose:

- selected context;
- reasoning result;
- decision candidate;
- validation result;
- authorization state;
- proposed action;
- result status;
- provenance.

# Safety

The first prototype MUST NOT automatically:

- send external email;
- perform irreversible external actions;
- deploy production changes;
- apply destructive repository mutations.

A proposed repository patch or draft response is an acceptable first action output.

# Success Criteria

The prototype passes only when context selection, reasoning, decision, validation, authorization and proposed action remain separately traceable.

# Failure Criteria

Fail the run when:

- context is fabricated;
- provenance is lost;
- reasoning is treated as authorization;
- validation is bypassed;
- a proposal is reported as executed;
- an unknown result is reported as success.

# Related Contracts

- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Cognition/COG-010_REASONING_PIPELINE_BOUNDARY.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-007_RUNTIME_SECURITY.md`
- `Runtime/RUN-008_RUNTIME_STATE.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Engine/ENG-002_DECISION_ENGINE.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`
- `Engine/ENG-006_EXECUTION_ENGINE.md`

# Integrity Hold

This is a runtime target contract, not evidence of implementation.

---

End of Document
