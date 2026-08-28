# MUT-2026-08-28-P394 — B08 Dispatch Observation Mutation Matrix

Date: 2026-08-28
Protocol: GOV-013
Scope: isolated PR #64 only

## Purpose
Record the minimum isolated test mutation for the P374 B08 observation contract.

## Mutation
`Quality/Integration/test_b08_run010_srv009_dispatch_observation_p394.py`

## Invariants
- RUN-010 execution identity is preserved into the downstream candidate.
- SRV-009 governed dispatch is reached through the existing ENG-006 adapter.
- Post-write read-back remains mandatory.
- Authorization remains fail-closed.
- No canonical authority or production runtime wiring is changed.

## Evidence target
A governed CI execution must demonstrate an observed dispatch boundary attributable to the same RUN-010 execution context. This matrix itself does not constitute behavioral evidence.

## Safety
- isolated branch: `hermuz/p375-rel009-minimal-b07-b08-20260828`
- no `main` mutation
- no provider credentials or external repository side effects
- fake connector only
- production adapter is exercised, but persistence is confined to the in-memory test connector

## Gate
`SOURCE-VERIFIED / EXECUTION-PENDING`
