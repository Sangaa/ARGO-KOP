from pathlib import Path

from canonical_spine_integration_audit import audit


def test_cognition_to_reasoning_accepts_complete_verified_evidence():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Cognition -> Reasoning": {
            "state": "CONNECTED",
            "contract": "Cognition/TRACEABLE_REASONING_CONTRACT.md",
            "test": "Cognition/test_traceable_reasoning.py",
            "trace": "Quality/Integration/canonical_evidence/COGNITION_TO_REASONING_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Cognition -> Reasoning"] == "CONNECTED"
    assert result["verified_connection_count"] >= 1


def test_cognition_to_reasoning_does_not_promote_reasoning_to_decision():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Cognition -> Reasoning": {
            "state": "CONNECTED",
            "contract": "Cognition/TRACEABLE_REASONING_CONTRACT.md",
            "test": "Cognition/test_traceable_reasoning.py",
            "trace": "Quality/Integration/canonical_evidence/COGNITION_TO_REASONING_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Reasoning -> Decision"] != "CONNECTED"
