# Cognitive Loop Prototype

This directory contains the first safe executable proof of the ARGO cognitive loop.

## Scope

The harness demonstrates:

`Context → Cognition → Decision → Validation → Human Authorization → Safe Proposal`

It intentionally performs **no external side effects**.

## Files

- `cognitive_loop_harness.py` — deterministic pipeline implementation.
- `test_cognitive_loop_harness.py` — acceptance tests for safety, authorization, hold behavior and traceability.

## Run

From this directory:

```bash
python -m pytest -q
```

Or run the harness directly:

```bash
python cognitive_loop_harness.py
```

## Architectural Rule

This prototype is not a replacement for the canonical Engine, Runtime, Governance, Memory or Knowledge contracts. It is an executable probe used to validate their integration assumptions.

The harness must remain side-effect free until the applicable authorization and execution boundaries are implemented and independently validated.
