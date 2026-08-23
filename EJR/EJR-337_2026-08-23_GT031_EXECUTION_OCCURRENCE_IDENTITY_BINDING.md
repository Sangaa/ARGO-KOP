# EJR-337 — GT-031 Execution Occurrence Identity Binding

Date: 2026-08-23
Status: COMPLETED / GOVERNED REGRESSION MUTATION
Protocol: GOV-013 + RUN-012
Parent: EJR-336

## Objective

Prevent an unbound `VERIFIED_OCCURRENCE` marker from certifying a current execution claim. Occurrence evidence must carry both execution identity and target commit.

## Existing insertion point

`Quality/Integration/test_evidence_reasoning_classification.py`

## Mutation

`EvidenceObservation` now carries optional `execution_identity` and `target_commit` fields. `classify_execution_occurrence()` refuses promotion unless the occurrence is explicitly `VERIFIED_OCCURRENCE` and both bindings are present.

Regression coverage:

1. VERIFIED_CAPABILITY + VERIFIED_OCCURRENCE without bindings -> UNRESOLVED.
2. VERIFIED_CAPABILITY + VERIFIED_OCCURRENCE with matching execution identity and target commit -> VERIFIED_OCCURRENCE.

Mutation commit:
`9fecbecafbeb3aa6c3b2a06e3aa3c093dbe2070e`

Content SHA:
`274c6626e30301072c28fed8f5d90a3943d2ba1e`

## Truth-eye result

`VERIFIED_OCCURRENCE` is now a semantic status that still requires identity binding. The label alone is not self-authenticating.

The classifier therefore distinguishes:

`occurrence asserted` -> insufficient

`occurrence asserted + execution identity + target commit` -> verifiable occurrence

## Execution boundary

Repository mutation and read-back are verified. No current CI run was fabricated or inferred.

`REGRESSION WIRING = VERIFIED`
`CURRENT CI EXECUTION = UNRESOLVED`
`PROMOTION = NOT AUTHORIZED`

## Knowledge Delta

**KD-055 — Occurrence claims require execution identity binding.**

**KD-056 — Semantic status is not provenance.**

A `VERIFIED_OCCURRENCE` label cannot substitute for evidence provenance bound to the target execution and commit.

## Closure

`Inspect → Identify missing binding → Minimal mutation → Negative/positive regression → Write → Read-back → Preserve execution boundary → Close`

Next safe continuation:
`GT-032 — test cross-binding mismatch: an occurrence with a valid execution identity but a different target commit must remain UNRESOLVED rather than certify the inspected mutation.`
