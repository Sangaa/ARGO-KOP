from pathlib import Path

from canonical_spine_consolidated_audit import build_consolidated_audit


def test_consolidated_audit_preserves_declared_spine_and_governed_execution_boundary():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    assert result["seam_count"] == 11
    assert result["authorization_to_execution_governed"] is True
    assert "Authorization -> Execution" in result["partial"] or "Authorization -> Execution" in result["missing"]


def test_consolidated_audit_only_reports_declared_canonical_seams():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    reported = set(result["connected"]) | set(result["partial"]) | set(result["missing"])
    assert all(" -> " in seam for seam in reported)
    assert "Learning Pipeline -> Verified Registry" not in reported
