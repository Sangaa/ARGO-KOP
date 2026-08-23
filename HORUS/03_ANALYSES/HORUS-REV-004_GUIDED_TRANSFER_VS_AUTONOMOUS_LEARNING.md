# HORUS-REV-004 — Guided Transfer vs Autonomous Learning

Date: 2026-08-23
Status: ANALYSIS / BEHAVIORAL EVIDENCE REVIEW
Owner: HORUS
Branch: horus/meta-learning-foundation-v6

## Question
Does the existing ARGO/HERMUZ record demonstrate that the candidate evidence-boundary principle is being transferred into new situations, or only that it can be followed when explicitly instructed?

## Case reviewed
EJR-293 established a Prior-Learning Retrieval Gate after a blind-search investigation rediscovered already-known learning. It explicitly distinguishes world unknown, memory unknown, tool unobservable, and world absent.

EJR-294 then applied the gate and deliberately widened the investigation beyond the previously assumed GitHub Actions boundary. The investigation used prior evidence, multiple discovery surfaces, exact known IDs, downstream readers, and a public control experiment. It revised the earlier broad statement "Actions are unavailable" into the narrower model `Actions Observation = ID-Dependent`, while preserving the unresolved ARGO run-discovery boundary.

## Behavioral interpretation

This is strong evidence of **guided cross-case transfer**:

- prior learning changed investigation order;
- the evidence-boundary concept changed the interpretation of a negative result;
- exact-ID evidence was separated from discovery evidence;
- an external control was used to distinguish connector capability from ARGO-specific observability;
- the final conclusion was narrowed rather than forced into a binary available/unavailable claim.

## What this proves

It supports that the ARGO/HERMUZ process can operationalize the candidate principle across a new investigation after the principle was explicitly made available through governance and prior learning.

## What it does NOT prove

It does not prove autonomous discovery of the principle. EJR-294 explicitly states that the investigation followed EJR-293 and was instructed to search beyond the assumed boundary. Therefore the behavior may be retrieval-and-application of an available rule rather than spontaneous abstraction.

## Learning distinction

`Rule Recall` = the agent retrieves an explicit prior rule and applies it.

`Guided Transfer` = the rule is applied correctly in a materially different context after the task is framed to use it.

`Spontaneous Transfer` = the agent independently recognizes that the same principle applies in a new context without the principle being supplied or signposted.

`Meta-Learning` = the agent not only transfers the principle but extracts a more general principle from the successful transfer and changes how it learns future cases.

Current evidence supports **Guided Transfer**, not yet Spontaneous Transfer or Meta-Learning.

## Important positive signal

The most valuable behavior is not merely that the rule was followed. The system refined a prior conclusion when new evidence changed the model:

`Actions unavailable` → `Actions observation is ID-dependent; discovery remains unestablished`.

That is evidence of **boundary refinement under evidence**, a stronger behavioral property than simple rule repetition.

## HORUS assessment

Candidate state:
`CROSS-DOMAIN SUPPORTED + GUIDED TRANSFER OBSERVED`

Promotion to `WORLD-FACING KNOWLEDGE`:
`NO`

Promotion to `ARGO META-LEARNING`:
`NO`

## Next experiment

A clean spontaneous-transfer test should introduce a new problem from a different domain with no explicit reference to the evidence-boundary principle. The evaluator should inspect whether ARGO independently:

1. retrieves relevant prior experience;
2. identifies the boundary of the current observation;
3. refuses to over-generalize from a negative or partial result;
4. seeks an independent evidence channel;
5. updates its conclusion when the new evidence conflicts with the first model;
6. records the newly generalized lesson.

The test must distinguish retrieval of a memorized phrase from genuine structural transfer by changing terminology and surface conditions.

## Routing

Source: `HORUS-ANALYSIS`
Consumers: `ARGO`, `HERMUZ`
Current handoff: `ANALYTICAL REFERENCE ONLY`
Canonical promotion: `NOT AUTHORIZED`
