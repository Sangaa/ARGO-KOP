# RUN-014 — LEARNING PROMOTION TEST

Platform: ARGO KOP
Document ID: RUN-014
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Runtime Learning Test
Priority: High
Date: 2026-08-11

---

# Purpose

Test that the cognitive loop can produce a learning candidate without silently promoting it to authoritative knowledge.

# Scenarios

| Scenario | Expected State |
| :--- | :--- |
| Verified outcome + evidence + approval | PROMOTION_ELIGIBLE |
| Verified outcome + evidence, no approval | HOLD |
| Missing evidence | HOLD |
| Unobserved outcome | HOLD |
| Conflicting governing rule | HOLD / CONFLICT |
| Low-confidence inferred pattern | HOLD |

# Required Trace

The learning candidate must retain:

- task/session ID;
- evidence references;
- observed result;
- extracted pattern;
- confidence;
- validation result;
- promotion authority.

# Success Criterion

A successful cognitive run may create a candidate, but **no candidate becomes learned knowledge unless the promotion gate is satisfied**.

# Regression Rule

Any future change to the Learning Engine, Memory lifecycle, Cognition loop or Runtime must preserve this invariant.

# Related Contracts

- `Engine/ENG-007_LEARNING_ENGINE.md`
- `Engine/ENG-015_LEARNING_PROMOTION_GATE.md`
- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`

---

End of Document
