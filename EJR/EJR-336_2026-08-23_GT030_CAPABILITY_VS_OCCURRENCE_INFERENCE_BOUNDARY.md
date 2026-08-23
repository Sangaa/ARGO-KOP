# EJR-336 — GT-030 Capability vs Occurrence Inference Boundary

Date: 2026-08-23
Status: COMPLETED / GOVERNED REGRESSION MUTATION
Protocol: GOV-013 + RUN-012
Parent: EJR-335

## Objective

Turn KD-051 into an executable reasoning boundary: evidence that a GitHub surface can emit execution identity must not promote an unresolved claim that a specific current mutation actually executed.

## Existing insertion point

`Quality/Integration/test_evidence_reasoning_classification.py`

No parallel runtime model was introduced.

## Mutation

Added `classify_execution_occurrence()` and two controlled regressions:

1. `VERIFIED_CAPABILITY` + current occurrence `UNRESOLVED` → `UNRESOLVED`.
2. `VERIFIED_CAPABILITY` + explicit `VERIFIED_OCCURRENCE` → `VERIFIED_OCCURRENCE`.

This establishes that capability evidence is non-promotional: it can describe the evidence channel, but cannot certify a distinct execution occurrence without explicit occurrence evidence.

Mutation commit:
`9e79a2cc8e380b368987d1619facebf2e2c825f1`

Content SHA:
`ab39432ec271d66182bc71b057b5c950e01ad44a`

## Truth-eye classification

`VERIFIED_CAPABILITY != VERIFIED_OCCURRENCE`

A historical run proving that the channel works is not evidence that the current target SHA ran.

Therefore the classifier must preserve `UNRESOLVED` until occurrence evidence is explicitly bound to the claim.

## Execution boundary

Repository mutation and read-back are verified. No current CI run for the mutation was fabricated or inferred from the historical run.

`CURRENT CI EXECUTION = UNRESOLVED`
`REGRESSION WIRING = VERIFIED`
`PROMOTION = NOT AUTHORIZED`

## Knowledge Delta

**KD-053 — Capability evidence is non-promotional.**

Evidence of channel capability cannot promote a separate occurrence claim.

**KD-054 — Occurrence requires explicit occurrence evidence.**

`VERIFIED_OCCURRENCE` must be grounded in evidence bound to the execution claim; capability alone is insufficient.

## Closure

`Inspect existing seam → Add minimal classifier predicate → Add positive/negative regression → Write → Read-back → Preserve CI boundary → Close`

Next safe continuation:
`GT-031 — verify that occurrence evidence itself must bind to the target commit/execution identity, preventing a generic VERIFIED_OCCURRENCE marker from becoming an unbound assertion.`
