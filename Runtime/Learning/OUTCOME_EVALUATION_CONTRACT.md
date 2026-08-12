# Outcome Evaluation Contract

## Purpose

Classify a recorded decision outcome before any learning promotion is considered, while preserving the provenance relationship between the outcome and the execution trace that produced it.

## Required Chain

```text
Decision
  ↓
Execution
  ↓
Execution Trace
  ↓
Outcome Evidence
  ↓
Outcome Evaluation
  ↓
Learning Eligibility
  ↓
Existing Learning Promotion Gate
```

## Required Provenance

An outcome evaluation MUST retain:

- `decision_id`
- `execution_id`
- `outcome_id`
- at least one `evidence_trace_id`
- at least one `execution_trace_id`

Every `evidence_trace_id` supplied by the outcome MUST belong to the supplied `execution_trace_ids` set.

An outcome with evidence that cannot be tied to the execution trace is rejected as `OUTCOME_PROVENANCE_BROKEN`.

An outcome without an execution trace is rejected as `EXECUTION_TRACE_REQUIRED`.

The execution-trace record itself remains governed by `Memory/Execution_Trace/EXECUTION_TRACE_CONTRACT.md`, where each trace has its canonical `trace_id` and records its historical execution observation.

## Result Classes

- `SUCCESS` — intended result achieved according to the available evaluation evidence.
- `PARTIAL` — meaningful result achieved, but the intended result was only partly achieved.
- `FAILURE` — the evaluated result did not achieve the intended outcome.
- `INCONCLUSIVE` — available evidence is insufficient to classify the outcome reliably.

## Rules

1. Evaluation must retain `decision_id` and `execution_id`.
2. Evaluation must retain `outcome_id`.
3. Evaluation must retain at least one outcome evidence trace.
4. Evaluation must retain at least one execution trace reference.
5. Every outcome evidence trace must be a member of the execution trace reference set.
6. Unknown result classes are rejected.
7. `INCONCLUSIVE` is evaluated but is not learning eligible.
8. `SUCCESS`, `PARTIAL`, and `FAILURE` may become learning eligible for review; they are not automatically promoted.
9. This evaluator does not determine truth outside the supplied evaluation evidence.
10. This evaluator does not replace the existing Learning Promotion Gate.
11. Outcome evaluation must not promote knowledge or mutate active Memory state.

## Boundary

```text
Outcome Classification
        ≠
Knowledge Promotion
```

A failure can be valuable learning material. A success can still contain a bad decision path. Promotion remains a separate governed step.

## Integration Boundary

This contract establishes the provenance shape required for the `Execution → Outcome` seam. It does not claim that a runtime producer actually supplies the required trace relationship. That relationship must be demonstrated by an executable integration path and trace evidence before the canonical seam can be certified.
