# Programming Source Intake Contract

## Purpose

Define the minimum evidence captured when a programming book or other learning source is introduced into ARGO.

## Intake Record

```text
Source ID:
Title:
Author / Creator:
Edition / Version:
Source Type:
Origin / Location:
Acquisition Date:
Primary Language / Domain:
Intended Scope:
```

## Intake Status

- `REGISTERED` — source identity recorded.
- `AVAILABLE` — source is accessible to the learning pipeline.
- `EXTRACTING` — structural/concept extraction in progress.
- `VALIDATING` — extracted claims being tested.
- `PROMOTION_REVIEW` — candidates awaiting promotion gate.
- `PROMOTED` — selected concepts became governed knowledge.
- `REJECTED` — source or claim failed a defined validation condition.

## Provenance Rule

Every extracted concept must point back to a source location. A summary without provenance is not sufficient evidence for promotion.

## Conflict Rule

If two sources disagree, ARGO must preserve the disagreement and evaluate evidence; it must not silently overwrite one source with another.

## Practical Rule

For programming sources, prefer concepts that can be converted into executable tests or controlled experiments. This creates measurable evidence for learning.

## Non-Claim

Registration proves only source availability. It does not prove reading, understanding, validation, experience or promotion.
