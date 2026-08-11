# Learning Evidence Schema

## Purpose

Define the minimum traceable structure required before a learning candidate can enter the Promotion Gate.

## Required Fields

- `source_ref` — where the claim came from;
- `concept` — the atomic concept being evaluated;
- `claim_type` — definition, rule, recommendation, example, or observation;
- `evidence` — reproducible support;
- `experiment_ref` — practical test when applicable;
- `observed_result` — what actually happened;
- `validation_status` — PASS, FAIL, or HOLD;
- `generalization_scope` — exact case, bounded class, or broader rule;
- `promotion_status` — candidate, promoted, rejected, or hold.

## Integrity Rules

1. Missing provenance means HOLD.
2. Missing evidence means HOLD.
3. Failed validation means HOLD or REJECTED; never promoted.
4. An observation must not be rewritten as a universal rule without sufficient evidence.
5. Promotion must preserve the evidence chain.

## Design Principle

Learning is not the storage of text. It is a traceable transformation from source claim to validated understanding and, where demonstrated, experience.
