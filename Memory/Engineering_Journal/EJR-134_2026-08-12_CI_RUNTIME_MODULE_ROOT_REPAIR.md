# EJR-134 — CI Runtime Module-Root Repair

**Date:** 2026-08-12  
**Status:** Repair applied / awaiting re-run evidence  
**Scope:** GitHub Actions integration environment

## Trigger

Workflow run `31598292372` (run #76) failed during test collection.

## Verified failure

The integration suite could not import runtime dependencies:

- `authorization_gate` was imported by `Runtime/Execution/connected_spine_runner.py` but its current repository location is `Decision/authorization_gate.py`.
- `runtime_result_persistence_adapter` was imported by `Quality/Integration/runtime_evidence_capture.py` but its current repository location is `Memory/Execution/runtime_result_persistence_adapter.py`.

The workflow exposed `Runtime/Execution`, `Runtime/Learning`, `Quality/Integration` and `Runtime/Prototype`, but not the two dependency roots above.

## Evidence

Run #76:

- prototype acceptance suite: passed;
- canonical acceptance scenarios: failed;
- integration quality suite: failed during collection;
- repeated import errors were `ModuleNotFoundError: authorization_gate` and `ModuleNotFoundError: runtime_result_persistence_adapter`.

This was treated as a real repository-to-CI relationship gap, not CI noise.

## Repair

Updated `.github/workflows/runtime-prototype-tests.yml` to expose:

- `Decision/`
- `Memory/Execution/`

in `PYTHONPATH`, and expanded workflow path triggers to rerun when those dependency domains change.

No runtime source file was rewritten and no import-local workaround was introduced.

## Boundary

This repair restores the environment needed to execute the existing dependency graph. It does **not** certify any seam and does not authorize `CONNECTED` promotion.

## Next deterministic step

Inspect the next GitHub Actions run. Classify any remaining failure from actual logs, repair only verified blockers, then re-run before making any connectivity claim.
