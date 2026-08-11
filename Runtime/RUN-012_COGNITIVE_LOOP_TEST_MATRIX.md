# RUN-012 — COGNITIVE LOOP TEST MATRIX

Platform: ARGO KOP
Document ID: RUN-012
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Runtime Test Contract
Priority: High
Date: 2026-08-11

---

# Purpose

Provide a compact acceptance matrix for the first cognitive runtime proof.

| Test | Expected proof | Failure signal |
| :--- | :--- | :--- |
| Context relevance | Only task-relevant state is selected | Irrelevant history dominates |
| Provenance | Material claims retain source references | Unsupported claims |
| Memory recall | Historical state is recovered with evidence | Generic answer without source |
| Fact / hypothesis separation | Uncertainty remains explicit | Hypothesis presented as fact |
| Decision boundary | Decision candidate contains rationale | Direct jump to action |
| Validation gate | Invalid candidate is held/rejected | Candidate proceeds |
| Authorization | Human approval is explicit | Implicit authorization |
| Safe action | Output remains non-destructive | External side effect |
| Failure handling | Missing context produces HOLD/uncertainty | Fabricated completion |
| Traceability | Full stage trace is preserved | Missing stage/provenance |

# Memory Recall Test

Retrieve a historical operational commitment using only bounded context and repository memory, then return:

1. answer;
2. source reference;
3. selected context;
4. confidence / uncertainty.

An answer without provenance does not pass.

# Regression Rule

Any implementation change affecting Context, Cognition, Decision, Validation or Runtime must rerun the applicable cases.

# Related Contracts

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Cognition/COG-010_REASONING_PIPELINE_BOUNDARY.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`

# Integrity Hold

The matrix defines acceptance criteria only; it does not claim that the runtime currently passes them.

---

End of Document
