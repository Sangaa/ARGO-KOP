# Decision Explanation Completeness Contract

## Purpose

Validate that a Decision Explanation can be audited without inventing missing provenance.

## Required Links

```text
Context
Evidence
Ruleset
Decision
Authorization
Execution
```

Each link must have an explicit identifier in the recorded explanation.

## Rule

A missing link makes the explanation `EXPLANATION_INCOMPLETE`.

The validator must report the missing link. It must not infer, reconstruct, or silently substitute an identifier.

## Boundary

Completeness is not correctness.

A complete explanation proves that the recorded chain is present and addressable. It does not prove that the evidence was true, that the decision was optimal, or that execution was successful.
