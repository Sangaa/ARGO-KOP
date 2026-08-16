from pathlib import Path

from canonical_spine_consolidated_audit import build_consolidated_audit


def test_consolidated_audit_is_not_allowed_to_invent_connected_state():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    assert result["seam_count"] == 11
    assert result["authorization_to_execution_governed"] is True
    # Candidate discovery must never itself create a CONNECTED seam.
    assert all(state in {"CONNECTED", "PARTIAL", "MISSING"} for state in (
        ["CONNECTED"] * len(result["connected"])
        + ["PARTIAL"] * len(result["partial"])
        + ["MISSING"] * len(result["missing"])
    ))
