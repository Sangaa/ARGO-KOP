from decision_pass import propose


def reasoning(questions=None):
    return {
        "status": "REASONED",
        "observations": {
            "facts": ["shipment is pending"],
            "assumptions": [],
            "known_knowledge": ["K-001"],
            "unresolved_questions": questions or [],
        },
        "evidence_map": [{"type": "FACT", "claim": "shipment is pending", "basis": "context"}],
    }


def test_unresolved_question_blocks_proposal():
    result = propose(reasoning(["connection confirmation"]), rules=["VERIFY_BEFORE_ACTION"])
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["execution_status"] == "NOT_REQUESTED"


def test_clear_reasoning_creates_proposal_not_execution():
    result = propose(reasoning(), rules=["VERIFY_BEFORE_ACTION"])
    assert result["status"] == "PROPOSAL_READY"
    assert result["execution_status"] == "NOT_REQUESTED"
    assert result["proposal"] == "REVIEW_AND_AUTHORIZE_NEXT_ACTION"


def test_invalid_reasoning_fails_closed():
    result = propose({"status": "REASONED"}, rules=[])
    assert result["status"] == "HOLD"
