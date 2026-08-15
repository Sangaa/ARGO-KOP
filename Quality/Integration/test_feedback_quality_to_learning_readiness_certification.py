import json
from pathlib import Path

from canonical_spine_integration_audit import audit


def test_feedback_quality_to_learning_readiness_is_canonically_certifiable():
    root = Path(__file__).resolve().parents[2]
    seam = "Feedback Quality -> Learning Readiness"
    trace = "Quality/Integration/canonical_evidence/FEEDBACK_QUALITY_TO_LEARNING_READINESS_TRACE.json"

    payload = json.loads((root / trace).read_text(encoding="utf-8"))
    assert payload["record_type"] == "EXECUTION_TRACE"
    assert payload["side_effect"] is False
    assert payload["evidence_class"] == "CONTROLLED_SYNTHETIC"

    verified = {
        seam: {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/FEEDBACK_QUALITY_GATE_CONTRACT.md",
            "test": "Quality/Integration/test_feedback_quality_readiness_registry_evidence.py",
            "trace": trace,
            "verification_status": "VERIFIED",
        }
    }
    report = audit(root, verified_seams=verified)
    assert report["verified_connection_count"] == 1
    assert report["evidence"][seam] == "CONNECTED"

    unrelated = [key for key in report["evidence"] if key != seam and report["evidence"][key] == "CONNECTED"]
    assert unrelated == []


def test_feedback_quality_readiness_certificate_cannot_promote_unverified_record():
    root = Path(__file__).resolve().parents[2]
    seam = "Feedback Quality -> Learning Readiness"
    verified = {
        seam: {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/FEEDBACK_QUALITY_GATE_CONTRACT.md",
            "test": "Quality/Integration/test_feedback_quality_readiness_registry_evidence.py",
            "trace": "Quality/Integration/canonical_evidence/FEEDBACK_QUALITY_TO_LEARNING_READINESS_TRACE.json",
            "verification_status": "UNVERIFIED",
        }
    }
    try:
        audit(root, verified_seams=verified)
    except ValueError as exc:
        assert str(exc) == f"verified seam record is not VERIFIED: {seam}"
    else:
        raise AssertionError("unverified seam must not be accepted as CONNECTED")
