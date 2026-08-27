# MI-IGT EXECUTION COORDINATION PROTOCOL v1.0

Status: `GOVERNED / EXECUTION-READY / NOT-AUTHORITY`

## Purpose
Coordinate independent IGT runs across simultaneous windows, platforms, and agents without contaminating evidence or serializing unrelated work.

## Core Rule
The repository is the shared state, but independence is a property of the evidence event. Parallel execution is allowed; evidence qualification remains per-run.

## Before Run
1. Read current repository ref.
2. Record baseline SHA.
3. Declare scope, mutation boundary, invariant, and novel transformation.
4. Complete independence attestation.
5. Capture prediction before receiving source conclusion or observed result.

## During Run
- Do not expose another run's prediction or outcome.
- Do not copy conclusions between runs.
- Detect repository changes before any mutation.
- Prefer read-only execution for IGT.
- If a shared mutation occurs, mark affected runs and re-baseline.

## After Run
Record outcome using the MI-IGT execution template, perform leakage and relationship checks, compare against the run's baseline, and close the run before reporting.

## Concurrency Classification
- `DISJOINT`: scopes do not touch the same artifact/seam; may proceed concurrently.
- `OVERLAP-READ`: shared read surface, no mutation; may proceed with baseline tracking.
- `OVERLAP-MUTATION`: same artifact/seam may mutate; requires coordination/reconciliation and may invalidate independence.
- `UNKNOWN`: treat as unsafe until reconciled.

## Promotion Boundary
Multiple passing runs are evidence accumulation, not automatic promotion. Promotion still requires the applicable learning/governance gate and explicit interpretation of what the evidence proves.

`AUTHORITY = NONE`
