from pathlib import Path

from canonical_spine_consolidated_audit import build_consolidated_audit


def test_consolidated_audit_loads_materialized_verified_registry_evidence():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    assert result["seam_count"] == 11
    assert result["verified_registry_records_loaded"] >= 1
    assert result["authorization_to_execution_governed"] is True
    assert "Authorization -> Execution" in result["connected"]


def test_consolidated_audit_only_reports_declared_canonical_seams():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    reported = set(result["connected"]) | set(result["partial"]) | set(result["missing"]) | set(result["governed_or_isolated"])
    assert all(" -> " in seam for seam in reported)
    assert "Learning Pipeline -> Verified Registry" not in reported
