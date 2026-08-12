from canonical_spine_integration_audit import audit
from canonical_spine_gap_map import SEAMS


def test_audit_is_conservative_without_verified_seams(tmp_path):
    (tmp_path / "Runtime").mkdir()
    (tmp_path / "Runtime" / "pipeline.py").write_text(
        "memory context cognition reasoning decision authorization execution trace outcome feedback learning pipeline",
        encoding="utf-8",
    )
    result = audit(tmp_path)
    assert result["status"] == "INTEGRATION_AUDIT_COMPLETE"
    assert result["verified_connection_count"] == 0
    assert result["gap_map"]["gap_count"] == len(SEAMS)


def test_explicit_verified_seam_can_be_promoted_to_connected(tmp_path):
    (tmp_path / "Runtime").mkdir()
    (tmp_path / "Runtime" / "pipeline.py").write_text("decision authorization", encoding="utf-8")
    seam = "Decision -> Authorization"
    result = audit(tmp_path, {seam: "CONNECTED"})
    assert result["evidence"][seam] == "CONNECTED"
    assert result["verified_connection_count"] == 1
    assert all(g["seam"] != seam for g in result["gap_map"]["gaps"])


def test_verified_registry_record_can_feed_audit(tmp_path):
    seam = "Decision -> Authorization"
    registry = {
        seam: {
            "state": "CONNECTED",
            "contract": "Decision/contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
            "trace": "Quality/Integration/decision_authorization_trace.md",
        }
    }
    result = audit(tmp_path, registry)
    assert result["evidence"][seam] == "CONNECTED"
    assert result["verified_connection_count"] == 1


def test_incomplete_verified_registry_record_is_rejected(tmp_path):
    seam = "Decision -> Authorization"
    registry = {
        seam: {
            "state": "CONNECTED",
            "contract": "Decision/contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
        }
    }
    try:
        audit(tmp_path, registry)
    except ValueError as exc:
        assert "incomplete verified seam evidence" in str(exc)
        return
    assert False, "incomplete verified seam evidence must be rejected"
