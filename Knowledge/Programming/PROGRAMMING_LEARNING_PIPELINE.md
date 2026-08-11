# Programming Learning Pipeline

## Purpose

Define how ARGO may convert programming books and other authoritative sources into governed, testable knowledge.

## Pipeline

### 1. Source Intake

Record source title, author, edition/version, origin and acquisition date.

### 2. Structural Extraction

Extract chapters, sections, definitions, examples, algorithms, code patterns and stated constraints without yet treating them as ARGO truth.

### 3. Concept Extraction

Convert extracted material into atomic concepts with source references.

### 4. Claim Classification

Classify each claim as definition, rule, example, recommendation, implementation detail, historical/contextual statement, or opinion.

### 5. Evidence Mapping

Every promoted concept must retain a source location and, where applicable, a practical test or demonstration.

### 6. Validation

Validate concepts through one or more of:

- executable tests;
- controlled experiments;
- independent authoritative comparison;
- code review;
- observed project results.

### 7. Experience Formation

A concept becomes experience only when ARGO has a traceable interaction with the concept in practice, including what was attempted, what happened, what was learned and what changed.

### 8. Promotion

Promotion is governed by the Learning Promotion Gate. Source reading alone is insufficient.

## Anti-Shortcut Rule

```text
Book uploaded ≠ Book understood
Book understood ≠ Concept validated
Concept validated ≠ Experience
Experience ≠ Canonical rule until promoted
```

## First Domain Priority

Programming is an initial training domain because it provides unusually strong opportunities for executable verification and therefore measurable learning evidence.
