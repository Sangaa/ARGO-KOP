"""Edge-case acceptance tests for the cognitive-loop harness."""

from cognitive_loop_harness import run
from test_cognitive_loop_harness import base_payload


def test_missing_knowledge_holds_validation():
    payload = base_payload()
    payload["knowledge"] = []
    result = run(payload, human_approved=True)
    assert result["validation"]["status"] == "HOLD"
    assert result["result"]["executed"] is False


def test_authorization_cannot_override_failed_validation():
    payload = base_payload()
    payload["evidence"] = []
    result = run(payload, human_approved=True)
    assert result["validation"]["status"] == "HOLD"
    assert result["authorization"]["status"] == "HOLD"
    assert result["action"]["status"] == "NOT_EXECUTED"
