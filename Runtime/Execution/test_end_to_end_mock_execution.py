from authorization_gate import authorize
from execution_plan import build_plan
from mock_executor import execute


def test_end_to_end_stops_at_simulation():
    proposal = {"status": "PROPOSAL_READY", "proposal": "REVIEW_AND_AUTHORIZE_NEXT_ACTION"}
    auth = authorize(proposal, {
        "approved": True,
        "authorized_by": "human",
        "authorization_id": "AUTH-E2E-001",
    })
    plan = build_plan(auth, action="DRAFT_RESPONSE", target="customer")
    result = execute(plan)

    assert auth["status"] == "AUTHORIZED"
    assert plan["status"] == "PLAN_READY"
    assert result["status"] == "SIMULATED"
    assert result["side_effect"] is False
    assert result["authorization_id"] == "AUTH-E2E-001"
