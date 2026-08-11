# ENG-015 — LEARNING PROMOTION GATE

Platform: ARGO KOP
Document ID: ENG-015
Version: 1.0.0
Status: Candidate / Integrity Hold
Category: Engine Integration
Priority: High
Date: 2026-08-11

---

# Purpose

Define the governed boundary between a **learning candidate** produced by the cognitive loop and knowledge that ARGO is allowed to retain as a reusable learned pattern.

This prevents successful execution or model output from being treated as learning automatically.

# Pipeline Position

```text
Observed Result
      ↓
Learning Candidate
      ↓
Evidence Check
      ↓
Outcome Verification
      ↓
Pattern Extraction
      ↓
Human / Governance Approval
      ↓
Promoted Learning
```

# Promotion Preconditions

A learning candidate must identify:

- source evidence;
- originating task/session;
- observed outcome;
- expected outcome;
- variance or error where applicable;
- extracted pattern;
- confidence;
- validation status;
- authority for promotion.

# Non-Promotion Conditions

A candidate remains unpromoted when:

- evidence is incomplete;
- the result was not observed;
- the pattern is inferred from one ambiguous example without validation;
- the candidate conflicts with an existing governing rule;
- confidence is insufficient;
- authority is absent.

# Core Invariant

```text
Experience ≠ Learning Candidate
Learning Candidate ≠ Learned Knowledge
Learned Knowledge ≠ Governing Rule
```

Promotion must remain explicit and traceable.

# Relationship to Existing Learning Engine

`Engine/ENG-007_LEARNING_ENGINE.md` remains the canonical learning engine contract. ENG-015 supplies the promotion boundary required by the new cognitive execution loop; it does not replace ENG-007.

# Safety Principle

ARGO must be able to learn from mistakes, but it must never silently convert a mistake, hallucination or unverified pattern into authoritative knowledge.

# Integrity Hold

This contract defines promotion criteria. It does not yet authorize automatic knowledge mutation.

---

End of Document
