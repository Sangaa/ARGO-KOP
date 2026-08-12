import pytest

from verified_seam_evidence_registry import register


def test_complete_evidence_promotes_seam():
    result = register([{
        "seam": "Decision -> Authorization",
        "contract": "Decision/contract.md",
        "test": "Quality/Integration/test_decision_authorization.py",
        "trace": "Quality/Integration/decision_authorization_trace.md",
        "verification_status": "VERIFIED",
    }])
    assert result["Decision -> Authorization"]["state"] == "CONNECTED"


def test_missing_evidence_is_rejected():
    with pytest.raises(ValueError):
        register([{
            "seam": "Decision -> Authorization",
            "contract": "Decision/contract.md",
            "test": "",
            "trace": "Quality/Integration/decision_authorization_trace.md",
            "verification_status": "VERIFIED",
        }])


def test_duplicate_seam_evidence_is_rejected():
    record = {
        "seam": "Decision -> Authorization",
        "contract": "Decision/contract.md",
        "test": "Quality/Integration/test_decision_authorization.py",
        "trace": "Quality/Integration/decision_authorization_trace.md",
        "verification_status": "VERIFIED",
    }
    with pytest.raises(ValueError, match="duplicate seam evidence"):
        register([record, record.copy()])


def test_absolute_evidence_reference_is_rejected():
    with pytest.raises(ValueError, match="invalid or incomplete evidence"):
        register([{
            "seam": "Decision -> Authorization",
            "contract": "/tmp/contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
            "trace": "Quality/Integration/decision_authorization_trace.md",
            "verification_status": "VERIFIED",
        }])


def test_parent_traversal_evidence_reference_is_rejected():
    with pytest.raises(ValueError, match="invalid or incomplete evidence"):
        register([{
            "seam": "Decision -> Authorization",
            "contract": "Decision/../contract.md",
            "test": "Quality/Integration/test_decision_authorization.py",
            "trace": "Quality/Integration/decision_authorization_trace.md",
            "verification_status": "VERIFIED",
        }])
