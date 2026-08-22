# EJR-306 — HERMUZ P6 Entrypoint / Adapter Bypass Audit

Date: 2026-08-22
Status: Closed — Audit + Read-back Verified
Scope: P6 evidence ingress boundary

## Trigger

EJR-305 made observation provenance mandatory at the `Evidence` constructor. The next question was whether another repository path could bypass that enforcement and inject evidence into P6 through a separate production entrypoint.

## Prior learning

The repository must be searched for the phenomenon and its possible entrypoints, not only for the expected implementation location. A search miss is not proof of nonexistence outside the searchable surface.

## Audit performed

Searched the repository for:

- `Evidence(` constructors;
- `P6ReconciliationEngine` consumers;
- runtime evidence capture paths;
- verified seam evidence loading;
- CI impact correlation and execution classification.

The current P6 domain model is isolated in `Quality/Integration/p6_reconciliation.py`, and its boundary regression suite is in `Quality/Integration/test_p6_reconciliation_boundaries.py`.

The runtime evidence capture path deliberately produces repository evidence beneath the governed runtime-evidence root and does not implicitly mutate canonical Memory or promote evidence. The CI emitter likewise states that its runtime artifact is not committed or promoted to the canonical registry by that script.

The verified seam registry/loader independently require explicit `verification_status`, contract, test, and materialized execution-trace evidence before registry registration.

## Finding

No separate P6 production constructor/entrypoint was identified through the available repository search surface that bypasses the explicit `Evidence.observation_state` requirement.

This is classified as:

`NO_BYPASS_OBSERVED_ON_AVAILABLE_SEARCH_SURFACE`

It is deliberately NOT classified as:

`NO_BYPASS_EXISTS`

because repository search coverage and connector visibility are bounded observations.

## No Mutation Required

The audit did not produce sufficient evidence of an actual bypass to justify a code change. Creating a speculative adapter or adding defensive machinery without a demonstrated ingress path would violate the smallest-safe-mutation principle.

## Verification

Read-back of the relevant current files confirmed:

- `Evidence.observation_state` is mandatory;
- boundary tests explicitly verify omission failure;
- surface failures cannot collapse into `NO_OBSERVATION`;
- CI/runtime evidence paths remain separate from canonical promotion;
- P6 correlation retains `NO_AUTO_PROMOTION` and separates execution validity from semantic mapping.

The available repository evidence supports the current boundary design but does not constitute canonical CI execution evidence.

## Learning

A useful reusable audit pattern is:

`Enforcement point → search all ingress paths → classify search coverage → only then decide whether a guard mutation is justified.`

This prevents two opposite errors:

1. assuming the constructor guard protects every ingress without checking;
2. adding speculative defenses because a bypass is merely imaginable.

## Closure

Mutation: NONE — NOT JUSTIFIED BY EVIDENCE
Audit: COMPLETE TO AVAILABLE SEARCH SURFACE
Read-back: VERIFIED
Canonical CI execution: NOT CLAIMED
P6 root cause: NOT CLAIMED
Relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — READ-BACK VERIFIED`.
