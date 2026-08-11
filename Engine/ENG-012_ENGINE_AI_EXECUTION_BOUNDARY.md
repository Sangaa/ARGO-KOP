# ENG-012 — ENGINE / AI EXECUTION BOUNDARY

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: ENG-012
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Engine
Canonical: Candidate
Priority: Critical
Last Audit Date: 2026-08-11

---

# Purpose

Define the boundary between ARGO's governed Engine layer and an AI model used to perform reasoning or generation.

This artifact is intentionally a boundary contract, not an implementation claim.

# Core Principle

The AI model performs computation, interpretation, generation and bounded reasoning.

The Engine layer controls the governed execution context around that model.

```text
Repository Reality
       ↓
Context / Evidence
       ↓
Engine Orchestration
       ↓
AI Model Execution
       ↓
Validation / Decision Gates
       ↓
Runtime Execution
       ↓
Persistence / Memory / Knowledge
```

# Separation of Responsibilities

## Engine

The Engine is responsible for:

- preparing the task context;
- resolving applicable dependencies;
- selecting or invoking the permitted AI capability;
- enforcing input/output boundaries;
- routing results to validation;
- preserving provenance and traceability;
- preventing model output from becoming authority by itself;
- handing validated outcomes to the appropriate Runtime, Memory, Knowledge or Decision path.

## AI Model

The AI model is responsible for:

- interpreting supplied context;
- generating analysis or candidate outputs;
- performing model-level reasoning within its capability;
- identifying uncertainty or limitations when detectable;
- returning results without claiming repository or governance authority.

The AI model does not independently determine canonical repository truth.

# Required Execution Envelope

Every governed Engine → AI execution should conceptually carry:

- task identity;
- session/context identity;
- repository baseline when repository work is involved;
- evidence scope;
- authority scope;
- applicable constraints;
- expected output type;
- validation requirement;
- persistence destination if any;
- provenance metadata;
- execution status.

Missing critical context must produce a bounded failure or explicit uncertainty rather than fabricated context.

# Output Classes

AI output must be classified before downstream use:

1. Observation
2. Analysis
3. Hypothesis
4. Proposal
5. Decision Candidate
6. Executable Action Candidate
7. Validated Result
8. Rejected / Superseded Result
9. Unknown / Unverified Result

Only an applicable authority and validation process may promote an output into a stronger class.

# Execution Boundary

The following are separate transitions:

```text
AI Generated
     ↓
Engine Classified
     ↓
Validated
     ↓
Authorized
     ↓
Executed
     ↓
Observed Result
     ↓
Persisted / Learned
```

Successful generation is not successful execution.

Successful execution is not validated correctness.

Validated correctness is not automatic authorization for future use.

# External Model Boundary

When the AI provider is external to ARGO:

- provider/model identity must remain attributable where available;
- provider output is evidence/input, not ARGO authority;
- provider refusal or policy must not silently become ARGO policy;
- unavailable provider capabilities must be represented as unavailable;
- claims about repository coverage must be evidence-backed;
- external output must pass the same relevant validation boundaries as internal model output.

# Learning Boundary

AI outputs may become learning candidates only through the governed Learning Engine.

```text
AI Output
   ↓
Learning Candidate
   ↓
Scope + Provenance
   ↓
Validation
   ↓
Correct Memory Domain
   ↓
Optional Promotion
```

The Engine must not directly convert model output into Platform Canonical Memory.

# Failure Handling

The Engine should preserve diagnosable states including:

- context unavailable;
- dependency unresolved;
- model unavailable;
- model response incomplete;
- validation failed;
- authorization unavailable;
- execution failed;
- execution unknown;
- persistence failed.

Recoverable technical failures may become learning candidates. They must not be silently represented as successful execution.

# Authority Boundary

This artifact does not grant the Engine authority over Governance, Constitution, Architecture, Repository or protected system changes.

Technical capability, model capability and repository write access do not independently establish authorization.

# Relationship to Existing Contracts

Primary intended relationships:

- `AI/AI-001_AI_MODEL.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Memory/MEM-005_MEMORY_GOVERNANCE.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`

These are references to existing contracts, not proof that every relationship has been validated.

# Integrity Hold

ENG-012 is a candidate boundary specification. It must not be treated as active canonical authority until its relationships are reviewed against the Engine, AI, Runtime, Architecture, Knowledge and Memory contracts.

# Guiding Statement

**The AI performs bounded reasoning; the Engine governs the execution context; validation determines whether the result is trustworthy; authorization determines whether protected action is permitted; Runtime determines execution flow; Memory and Knowledge determine what may be retained and promoted.**

---

End of Document
