from pathlib import Path

from control_plane_reconciliation_gate import MANIFEST, evaluate


def test_control_plane_gate_uses_current_manifest_not_historical_checkpoint() -> None:
    assert MANIFEST == "Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md"
    assert "SESSION_DELTA" not in MANIFEST


def test_current_control_plane_manifest_matches_current_repository() -> None:
    root = Path(__file__).resolve().parents[2]
    result = evaluate(root)
    assert result["expected_artifacts"] >= 7
    assert result["missing"] == []
    assert result["mismatches"] == []
    assert result["boundary_pass"] is True
