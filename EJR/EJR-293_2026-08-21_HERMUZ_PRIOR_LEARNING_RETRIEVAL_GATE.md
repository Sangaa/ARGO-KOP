# EJR-293 — HERMUZ Prior-Learning Retrieval Gate

Date: 2026-08-21
Status: CLOSED / GOVERNANCE INTEGRATED

## Trigger

A blind-search investigation of the GitHub Actions evidence boundary rediscovered EJR-279, which had already established the same boundary and corrected an earlier over-strong negative conclusion.

## Finding

The issue was not only technical discovery. It exposed a process gap: prior ARGO learning existed and was authoritative enough to materially constrain the current reasoning, but it was not recovered before new solution paths were explored.

## Decision

GOV-013 is strengthened with a mandatory Prior-Learning Retrieval Gate before proposing or implementing a new solution to a material problem.

Required sequence:

Problem Definition → Prior-Learning Retrieval → Prior-Evidence Review → Solution Simulation → New-Learning Search only if required.

The gate requires retrieval across Engineering Journal/lessons/mistakes, canonical protocols/matrices/contracts, and prior implementations/tests/checkpoints/issues. Recovered learning must be classified as directly applicable, transferable, historical/superseded, contradictory/unresolved, or not found.

## Architectural Learning

ARGO must distinguish:

- world unknown;
- memory unknown;
- tool unobservable;
- world absent.

Failure to retrieve prior knowledge is not evidence that prior knowledge does not exist.

## Control Effect

A new solution must not be treated as necessary until relevant prior learning has been searched, reviewed and bounded through simulation. If prior learning fails, the remaining gap must be identified before new research/experimentation begins.

## Provenance

- Prior boundary learning: EJR-279
- Canonical protocol updated: GOV-013 v1.1.1
- Governing commit: 3d2d35bee04bdaaea4d71994e2a6e97ad6d39cc2

## Closure

Post-change re-read is required before treating this governance mutation as complete.

End of EJR-293
