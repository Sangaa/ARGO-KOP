from authorization_gate import authorize


def test_authorization_rejects_review_required_proposal():
    proposal = {"status": "REVIEW_REQUIRED"}
    result = authorize(proposal, {"approved": True, "authorized_by": "tester"})
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "PROPOSAL_NOT_READY"


def test_authorization_requires_explicit_approval():
    proposal = {"status": "PROPOSAL_READY"}
    result = authorize(proposal, None)
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "AUTHORIZATION_REQUIRED"


def test_authorization_does_not_start_execution():
    proposal = {"status": "PROPOSAL_READY"}
    authorization = {
        "approved": True,
        "authorized_by": "tester",
        "authorization_id": "AUTH-TEST-001",
    }
    result = authorize(proposal, authorization)
    assert result["status"] == "AUTHORIZED"
    assert result["execution_status"] == "NOT_STARTED"
    assert result["authorization_id"] == "AUTH-TEST-001"
