import pytest

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


def _materialized_registry(tmp_path):
    for path in ("contract.md", "test.py", "trace.md"):
        (tmp_path / path).write_text("verified evidence", encoding="utf-8")
    return {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "contract.md",
            "test": "test.py",
            "trace": "trace.md",
        }
    }


def test_registry_record_can_promote_only_materialized_verified_seam(tmp_path):
    result = audit(tmp_path, _materialized_registry(tmp_path))
    assert result["evidence"]["Decision -> Authorization"] == "CONNECTED"
    assert result["verified_connection_count"] == 1
    assert all(g["seam"] != "Decision -> Authorization" for g in result["gap_map"]["gaps"])


def test_string_connected_state_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="must be a registry record"):
        audit(tmp_path, {"Decision -> Authorization": "CONNECTED"})


def test_incomplete_verified_registry_record_is_rejected(tmp_path):
    registry = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "Decision/contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
        }
    }
    with pytest.raises(ValueError, match="incomplete verified seam evidence"):
        audit(tmp_path, registry)


def test_nonexistent_registry_evidence_is_rejected(tmp_path):
    registry = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "contract.md",
            "test": "test.py",
            "trace": "trace.md",
        }
    }
    with pytest.raises(ValueError, match="files missing or invalid"):
        audit(tmp_path, registry)


def test_registry_parent_traversal_is_rejected(tmp_path):
    for path in ("contract.md", "test.py"):
        (tmp_path / path).write_text("verified evidence", encoding="utf-8")
    outside = tmp_path.parent / "trace.md"
    outside.write_text("outside evidence", encoding="utf-8")
    registry = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "contract.md",
            "test": "test.py",
            "trace": "../trace.md",
        }
    }
    with pytest.raises(ValueError, match="files missing or invalid"):
        audit(tmp_path, registry)
