# Synthetic Context Retrieval Experiment 001

## Objective

Verify that promoted knowledge is selected through task context rather than repository-wide text similarity.

## Context

```text
Project: ARGO-KOP
Domain: programming
State: learning
Scope: tested_claim_only
Claim: function returns predictable result
```

## Records

Two promoted records are available with identical wording:

- one belongs to ARGO-KOP;
- one belongs to another project.

## Expected Result

Only the ARGO-KOP record is retrieved.

## Missing Context Test

If the allowed scope is missing, retrieval must return no records rather than widening the search.

## Significance

This is the first controlled boundary between a general knowledge repository and task-specific context.
