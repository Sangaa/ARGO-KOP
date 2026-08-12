# EJR-140 — SAFE-003 Acceptance Contract Repair

Date: 2026-08-12

## Finding

CI run #85 executed the canonical acceptance scenarios. SAFE-001 and SAFE-002 passed, while SAFE-003 failed.

SAFE-003 is named `missing_evidence` and expects `HOLD`, but the scenario runner supplied the same payload used by the evidence-present scenarios. The actual harness therefore correctly reached `PROPOSED` with no external side effect.

## Root Cause

The defect was in the acceptance-test fixture construction, not in the cognitive-loop safety behavior.

`cognitive_loop_harness.reason()` already returns `HOLD` when evidence is absent. The canonical scenario runner was simply not exercising that condition for SAFE-003.

## Repair

Updated `Runtime/Prototype/run_acceptance_scenarios.py` so a scenario named `missing_evidence` receives an empty evidence list.

No runtime safety rule was weakened or bypassed.

## Expected Result

SAFE-003 should now exercise the intended path:

missing evidence → reasoning HOLD → no authorization → no proposal → no execution → no external side effect.

## CI Evidence

Run #85: 50 integration tests passed and 17 failed. Prototype unit tests passed, while the canonical scenario runner failed only SAFE-003 at the acceptance-scenario stage.

The 17 integration failures are a separate existing connectivity/provenance cluster and remain open; they are not marked fixed by this checkpoint.

## Remaining Work

1. Re-run CI on commit `b17222f9a11b0b8421096ecdcc5fe982412ad629`.
2. Confirm SAFE-003 passes.
3. Continue repairing the highest-value integration failure cluster without weakening gates.
4. Keep all changes evidence-backed and resumable.
