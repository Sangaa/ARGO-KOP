import json
from pathlib import Path

from canonical_spine_integration_audit import audit


def test_learning_readiness_to_learning_pipeline_is_canonically_certifiable():
    root = Path(__file__).resolve().parents[2]
    seam = "Learning Readiness -> Learning Pipeline"
    trace = "Quality/Integration/canonical_evidence/LEARNING_READINESS_TO_LEARNING_PIPELINE_TRACE.json"

    payload = json.loads((root / trace).read_text(encoding="utf-8"))
    assert payload["record_type"] == "EXECUTION_TRACE"
    assert payload["side_effect"] is False
    assert payload["evidence_class"] == "CONTROLLED_SYNTHETIC"

    verified = {
        seam: {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md",
            "test": "Quality/Integration/test_learning_pipeline_to_verified_registry.py",
            "trace": trace,
            "verification_status": "VERIFIED",
        }
    }
    report = audit(root, verified_seams=verified)
    assert report["verified_connection_count"] == 1
    assert report["evidence"][seam] == "CONNECTED"


def test_learning_readiness_pipeline_certificate_rejects_unverified_record():
    root = Path(__file__).resolve().parents[2]
    seam = "Learning Readiness -> Learning Pipeline"
    verified = {
        seam: {
            "state": "CONNECTED",
            "contract": "Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md",
            "test": "Quality/Integration/test_learning_pipeline_to_verified_registry.py",
            "trace": "Quality/Integration/canonical_evidence/LEARNING_READINESS_TO_LEARNING_PIPELINE_TRACE.json",
            "verification_status": "UNVERIFIED",
        }
    }
    try:
        audit(root, verified_seams=verified)
    except ValueError as exc:
        assert str(exc) == f"verified seam record is not VERIFIED: {seam}"
    else:
        raise AssertionError("unverified seam must not become CONNECTED")
