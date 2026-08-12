# Feedback Quality Gate Contract

## Purpose

Prevent weakly supported outcome evaluations from becoming learning-ready material.

## Required Inputs

```text
Evaluated Outcome
Outcome Evidence
Evaluation Confidence
```

## Quality States

- `ACCEPTABLE` — evaluation is complete, evidence exists, and confidence is HIGH or MEDIUM.
- `INSUFFICIENT` — evidence/evaluation quality is not strong enough for learning readiness.

## Rules

1. Only `EVALUATED` outcomes enter this gate.
2. Outcome evidence is mandatory.
3. Confidence must be explicitly classified as HIGH, MEDIUM, LOW, or UNKNOWN.
4. LOW and UNKNOWN confidence are not learning-ready.
5. `INCONCLUSIVE` outcomes are never learning-ready.
6. Quality assessment does not promote knowledge.

## Boundary

```text
Evaluated
   ↓
Quality Assessed
   ↓
Learning Ready
   ↓
Existing Promotion Gate
```

`learning_ready` is an eligibility signal, not a promotion decision.
