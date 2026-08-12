# EJR-135 — CI Cognition Module-Root Repair

**Date:** 2026-08-12  
**Status:** Repair applied / awaiting re-run evidence  
**Scope:** GitHub Actions integration environment

## Trigger

The EJR-134 repair caused the next workflow run to progress past the previous missing modules, exposing the next actual dependency gap.

## Verified failure

Run #77 (`31598823050`) failed during integration test collection with:

`ModuleNotFoundError: No module named 'reasoning_packet_classifier'`

Direct repository inspection verified the implementation exists at:

`Cognition/reasoning_packet_classifier.py`

The runtime orchestrator imports it as a top-level module. The workflow did not expose `Cognition/` in `PYTHONPATH`.

## Repair

Updated `.github/workflows/runtime-prototype-tests.yml` to:

- expose `Cognition/` in `PYTHONPATH`;
- rerun on `Cognition/**` changes.

No runtime import was rewritten and no duplicate module was created.

## Interpretation

This is a real cross-domain environment relationship gap discovered by executing the repository, not an application-logic failure.

The staged CI failures are useful evidence that the repository's actual module graph is broader than the previous workflow declaration.

## Boundary

This repair restores another verified dependency root. It does not certify the canonical seam and does not authorize `CONNECTED` promotion.

## Next deterministic step

Inspect the next workflow result and continue resolving only dependencies demonstrated by actual CI logs. Once collection succeeds, analyze test failures as application/integration evidence rather than continuing to expand `PYTHONPATH` speculatively.
