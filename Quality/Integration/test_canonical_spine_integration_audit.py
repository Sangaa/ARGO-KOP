import json

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
    assert result["candidate_files"]["Decision -> Authorization"] == [
        "Runtime/pipeline.py"
    ]
    assert result["candidate_kinds"]["Decision -> Authorization"]["Runtime/pipeline.py"] == "implementation"


def _materialized_registry(tmp_path, verification_status="VERIFIED", trace_payload=None):
    (tmp_path / "contract.md").write_text("verified evidence", encoding="utf-8")
    (tmp_path / "test.py").write_text("verified evidence", encoding="utf-8")
    payload = trace_payload or {
        "record_type": "EXECUTION_TRACE",
        "trace_id": "trace-001",
        "task_id": "task-001",
        "session_id": "session-001",
        "final_status": "INCONCLUSIVE",
    }
    (tmp_path / "trace.json").write_text(json.dumps(payload), encoding="utf-8")
    return {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "contract.md",
            "test": "test.py",
            "trace": "trace.json",
            "verification_status": verification_status,
        }
    }


def test_registry_record_can_promote_only_materialized_verified_seam(tmp_path):
    result = audit(tmp_path, _materialized_registry(tmp_path))
    assert result["evidence"]["Decision -> Authorization"] == "CONNECTED"
    assert result["verified_connection_count"] == 1
    assert all(g["seam"] != "Decision -> Authorization" for g in result["gap_map"]["gaps"])


def test_candidate_provenance_never_promotes_a_seam(tmp_path):
    (tmp_path / "candidate.md").write_text(
        "decision authorization execution trace verified connected", encoding="utf-8"
    )
    result = audit(tmp_path)
    assert result["verified_connection_count"] == 0
    assert result["evidence"]["Decision -> Authorization"] == "PARTIAL"
    assert "candidate.md" in result["candidate_files"]["Decision -> Authorization"]
    assert result["candidate_kinds"]["Decision -> Authorization"]["candidate.md"] == "documentation"
    assert any(
        gap["seam"] == "Decision -> Authorization"
        for gap in result["gap_map"]["gaps"]
    )


def test_unverified_registry_record_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="not VERIFIED"):
        audit(tmp_path, _materialized_registry(tmp_path, "UNVERIFIED"))


def test_string_connected_state_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="must be a registry record"):
        audit(tmp_path, {"Decision -> Authorization": "CONNECTED"})


def test_incomplete_verified_registry_record_is_rejected(tmp_path):
    registry = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "Decision/contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
            "verification_status": "VERIFIED",
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
            "trace": "trace.json",
            "verification_status": "VERIFIED",
        }
    }
    with pytest.raises(ValueError, match="files missing or invalid"):
        audit(tmp_path, registry)


def test_registry_parent_traversal_is_rejected(tmp_path):
    for path in ("contract.md", "test.py"):
        (tmp_path / path).write_text("verified evidence", encoding="utf-8")
    outside = tmp_path.parent / "trace.json"
    outside.write_text(
        json.dumps({
            "record_type": "EXECUTION_TRACE",
            "trace_id": "trace-outside",
            "task_id": "task-001",
            "session_id": "session-001",
            "final_status": "INCONCLUSIVE",
        }),
        encoding="utf-8",
    )
    registry = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "contract.md",
            "test": "test.py",
            "trace": "../trace.json",
            "verification_status": "VERIFIED",
        }
    }
    with pytest.raises(ValueError, match="files missing or invalid"):
        audit(tmp_path, registry)


def test_noncanonical_trace_shape_is_rejected(tmp_path):
    registry = _materialized_registry(
        tmp_path,
        trace_payload={
            "record_type": "OTHER_RECORD",
            "trace_id": "trace-001",
            "task_id": "task-001",
            "session_id": "session-001",
            "final_status": "INCONCLUSIVE",
        },
    )
    with pytest.raises(ValueError, match="not a canonical execution trace"):
        audit(tmp_path, registry)
