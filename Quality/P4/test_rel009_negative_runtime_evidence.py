"""Negative evidence gate for REL-009.

This test does not prove absence globally. It verifies that the inspected
connected runtime seam currently records a simulated execution trace rather
than dispatching SRV-009, so simulation evidence cannot be promoted into
callable-consumer evidence.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "Runtime" / "Execution" / "connected_spine_runner.py"
ENTRYPOINT = ROOT / "Runtime" / "Execution" / "execution_entrypoint.py"


def test_connected_spine_is_simulation_only_at_current_boundary() -> None:
    runner = RUNNER.read_text(encoding="utf-8")
    entrypoint = ENTRYPOINT.read_text(encoding="utf-8")

    assert 'action="SIMULATED_REVIEW"' in runner
    assert "side_effect=False" in runner
    assert "record_execution_trace" in entrypoint
    assert "does not" in entrypoint


def test_negative_runtime_evidence_does_not_claim_srv009_dispatch() -> None:
    runner = RUNNER.read_text(encoding="utf-8")
    entrypoint = ENTRYPOINT.read_text(encoding="utf-8")

    # These files are the inspected runtime handoff boundary. They may record
    # traces, but they must not be treated as proof of an SRV-009 invocation.
    assert "SRV-009" not in runner
    assert "SRV-009" not in entrypoint
