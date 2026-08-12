import pytest

from verified_seam_evidence_registry import register


def test_complete_evidence_promotes_seam():
    result = register([{
        "seam": "Decision -> Authorization",
        "contract": "decision-authorization-contract",
        "test": "test_decision_authorization",
        "trace": "synthetic-trace-001",
    }])
    assert result["Decision -> Authorization"]["state"] == "CONNECTED"


def test_missing_evidence_is_rejected():
    with pytest.raises(ValueError):
        register([{
            "seam": "Decision -> Authorization",
            "contract": "decision-authorization-contract",
            "test": "",
            "trace": "synthetic-trace-001",
        }])
