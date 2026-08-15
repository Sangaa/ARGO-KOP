"""Direct integration proof for Decision proposal -> explicit Authorization gate."""

from Decision.authorization_gate import authorize
from Decision.decision_pass import propose


def test_proposal_cannot_cross_authorization_without_explicit_approval():
    reasoning = {
        "status": "REASONED",
        "observations": {"unresolved_questions": []},
        "evidence_map": [{"type": "FACT", "claim": "shipment confirmed"}],
    }

    proposal = propose(reasoning, rules=["verify before action"])
    result = authorize(proposal, None)

    assert proposal["status"] == "PROPOSAL_READY"
    assert result == {"status": "BLOCKED", "reason": "AUTHORIZATION_REQUIRED"}


def test_explicit_authorization_reaches_authorized_state_without_starting_execution():
    reasoning = {
        "status": "REASONED",
        "observations": {"unresolved_questions": []},
        "evidence_map": [{"type": "FACT", "claim": "shipment confirmed"}],
    }

    proposal = propose(reasoning, rules=["verify before action"])
    result = authorize(
        proposal,
        {"approved": True, "authorized_by": "human-review", "authorization_id": "AUTH-001"},
    )

    assert result["status"] == "AUTHORIZED"
    assert result["authorized_by"] == "human-review"
    assert result["authorization_id"] == "AUTH-001"
    assert result["execution_status"] == "NOT_STARTED"
