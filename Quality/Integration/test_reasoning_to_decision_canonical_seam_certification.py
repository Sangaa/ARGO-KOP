from pathlib import Path

from canonical_spine_integration_audit import audit


def test_reasoning_to_decision_accepts_complete_verified_evidence():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Reasoning -> Decision": {
            "state": "CONNECTED",
            "contract": "Decision/DECISION_PASS_CONTRACT.md",
            "test": "Decision/test_decision_pass.py",
            "trace": "Quality/Integration/canonical_evidence/REASONING_TO_DECISION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Reasoning -> Decision"] == "CONNECTED"
    assert result["verified_connection_count"] >= 1


def test_reasoning_to_decision_does_not_promote_decision_to_authorization():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Reasoning -> Decision": {
            "state": "CONNECTED",
            "contract": "Decision/DECISION_PASS_CONTRACT.md",
            "test": "Decision/test_decision_pass.py",
            "trace": "Quality/Integration/canonical_evidence/REASONING_TO_DECISION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Decision -> Authorization"] != "CONNECTED"
