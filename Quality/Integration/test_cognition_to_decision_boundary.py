"""Direct integration proof for Cognition reasoning -> governed Decision proposal."""

from Cognition.traceable_reasoning import reason
from Decision.decision_pass import propose


def test_cognition_to_decision_preserves_unresolved_review_boundary():
    classified = {
        "facts": ["shipment pending"],
        "assumptions": [],
        "known_knowledge": ["K-001"],
        "unresolved_questions": ["Which vessel is confirmed?"],
    }

    reasoning = reason(classified)
    result = propose(reasoning, rules=["verify before action"])

    assert reasoning["status"] == "REASONED"
    assert reasoning["decision_status"] == "NOT_EVALUATED"
    assert reasoning["execution_status"] == "NOT_REQUESTED"
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["execution_status"] == "NOT_REQUESTED"
    assert result["questions"] == ["Which vessel is confirmed?"]


def test_cognition_to_decision_reaches_proposal_without_execution_request():
    classified = {
        "facts": ["shipment confirmed"],
        "assumptions": [],
        "known_knowledge": ["K-001"],
        "unresolved_questions": [],
    }

    reasoning = reason(classified)
    result = propose(reasoning, rules=["verify before action"])

    assert reasoning["status"] == "REASONED"
    assert result["status"] == "PROPOSAL_READY"
    assert result["execution_status"] == "NOT_REQUESTED"
    assert result["proposal"] == "REVIEW_AND_AUTHORIZE_NEXT_ACTION"
