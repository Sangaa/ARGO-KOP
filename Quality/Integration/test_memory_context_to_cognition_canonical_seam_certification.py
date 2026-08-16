from pathlib import Path

from canonical_spine_integration_audit import audit


def test_memory_context_to_cognition_accepts_complete_verified_evidence():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Memory / Context -> Cognition": {
            "state": "CONNECTED",
            "contract": "Cognition/CONTEXT_MEMORY_SELECTION_CONTRACT.md",
            "test": "Quality/Integration/test_memory_to_context_selection_boundary.py",
            "trace": "Quality/Integration/canonical_evidence/MEMORY_CONTEXT_TO_COGNITION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["seam_count"] == 11
    assert result["evidence"]["Memory / Context -> Cognition"] == "CONNECTED"
    assert result["verified_connection_count"] >= 1


def test_memory_context_to_cognition_does_not_promote_historical_evidence_to_reasoning():
    root = Path(__file__).resolve().parents[2]
    evidence = {
        "Memory / Context -> Cognition": {
            "state": "CONNECTED",
            "contract": "Cognition/CONTEXT_MEMORY_SELECTION_CONTRACT.md",
            "test": "Quality/Integration/test_memory_to_context_selection_boundary.py",
            "trace": "Quality/Integration/canonical_evidence/MEMORY_CONTEXT_TO_COGNITION_TRACE.json",
            "verification_status": "VERIFIED",
        }
    }
    result = audit(root, evidence)
    assert result["evidence"]["Cognition -> Reasoning"] != "CONNECTED"
