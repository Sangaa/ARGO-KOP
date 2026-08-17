from pathlib import Path

from control_plane_reconciliation_gate import evaluate


def test_current_control_plane_boundary_is_consistent():
    report = evaluate(Path(__file__).resolve().parents[2])
    assert report["boundary_pass"], report
