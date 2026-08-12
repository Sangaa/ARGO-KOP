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
