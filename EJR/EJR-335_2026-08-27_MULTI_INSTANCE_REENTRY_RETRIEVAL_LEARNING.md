# EJR-335 — Multi-Instance Repository-First Re-entry Learning

Date: 2026-08-27
Status: `REUSABLE-LEARNING / PROMOTION-CANDIDATE`

## Observation
A continuation session can hold a stale project narrative after another instance has changed the repository. Treating session memory as current state can cause duplicate work or false completion claims.

## Root Cause
The execution context and the shared repository state were implicitly treated as equivalent.

## Corrective Pattern
Every continuation begins from current repository evidence, reconciles recent changes and relevant checkpoints, then scopes the next mutation. Repository evidence outranks session memory.

## General Rule
`REPOSITORY = SHARED OPERATIONAL MEMORY`
`SESSION = EXECUTION CONTEXT`

## Existing Authority Check
GOV-013 already requires repository-first continuation, prior-learning retrieval, evidence discipline, safe mutation and closure. GOV-016 requires reusable learning to be evidenced and validated before governance promotion. Therefore this record does not create new authority by itself.

## Validation
The rule was operationally validated by detecting a contradiction between a prior session claim and current repository state during P334 re-entry. The current repository state was accepted as authoritative and the stale claim was corrected.

## Transfer
`Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` remains the governed proposal for explicit multi-instance rules. Promotion to canonical governance requires the applicable governance/learning gate.

## Limits
This learning does not grant concurrent mutation authority, bypass branch protections, or authorize runtime/production side effects.
