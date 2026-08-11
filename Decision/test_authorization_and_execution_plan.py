from authorization_gate import authorize
from execution_plan import build_plan


def proposal():
    return {"status": "PROPOSAL_READY", "proposal": "REVIEW_AND_AUTHORIZE_NEXT_ACTION"}


def test_missing_authorization_blocks_execution_path():
    result = authorize(proposal(), None)
    assert result["status"] == "BLOCKED"
    assert result["reason"] == "AUTHORIZATION_REQUIRED"


def test_authorized_proposal_can_create_plan_but_not_execute():
    auth = authorize(proposal(), {"approved": True, "authorized_by": "human", "authorization_id": "AUTH-001"})
    plan = build_plan(auth, action="DRAFT_RESPONSE", target="customer")
    assert auth["status"] == "AUTHORIZED"
    assert plan["status"] == "PLAN_READY"
    assert plan["execution_status"] == "NOT_STARTED"


def test_plan_without_authorization_is_blocked():
    plan = build_plan({"status": "BLOCKED"}, action="SEND_EMAIL", target="customer")
    assert plan["status"] == "BLOCKED"
