from pathlib import Path

from canonical_spine_integration_audit import audit


def test_decision_to_authorization_accepts_complete_verified_evidence():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "Decision/DECISION_PASS_CONTRACT.md",
            "test": "Quality/Integration/test_decision_to_authorization_boundary.py",
            "trace": "Quality/Integration/canonical_evidence/DECISION_TO_AUTHORIZATION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Decision -> Authorization"] == "CONNECTED"
    assert result["verified_connection_count"] >= 1


def test_decision_to_authorization_does_not_promote_authorization_to_execution():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Decision -> Authorization": {
            "state": "CONNECTED",
            "contract": "Decision/DECISION_PASS_CONTRACT.md",
            "test": "Quality/Integration/test_decision_to_authorization_boundary.py",
            "trace": "Quality/Integration/canonical_evidence/DECISION_TO_AUTHORIZATION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Authorization -> Execution"] != "CONNECTED"
