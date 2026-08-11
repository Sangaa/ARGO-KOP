from decision_pass import propose


def test_unresolved_reasoning_cannot_become_ready_proposal():
    reasoning = {
        "status": "REASONED",
        "observations": {
            "facts": ["shipment pending"],
            "assumptions": [],
            "known_knowledge": ["K-001"],
            "unresolved_questions": ["Which vessel is confirmed?"]
        },
        "evidence_map": [{"type": "FACT", "claim": "shipment pending", "basis": "context"}]
    }
    result = propose(reasoning, rules=["verify before action"])
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["execution_status"] == "NOT_REQUESTED"


def test_complete_reasoning_can_reach_proposal_only():
    reasoning = {
        "status": "REASONED",
        "observations": {
            "facts": ["shipment confirmed"],
            "assumptions": [],
            "known_knowledge": ["K-001"],
            "unresolved_questions": []
        },
        "evidence_map": [{"type": "FACT", "claim": "shipment confirmed", "basis": "context"}]
    }
    result = propose(reasoning, rules=["verify before action"])
    assert result["status"] == "PROPOSAL_READY"
    assert result["execution_status"] == "NOT_REQUESTED"
