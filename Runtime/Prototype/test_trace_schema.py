"""Contract checks for the cognitive-loop trace shape.

These tests intentionally use only the standard library so the prototype can
be checked without introducing a runtime dependency.
"""

import json
from pathlib import Path

from cognitive_loop_harness import run


ROOT = Path(__file__).resolve().parent


def test_trace_matches_required_contract():
    schema = json.loads((ROOT / "trace_schema.json").read_text(encoding="utf-8"))
    result = run(
        {
            "task_id": "SCHEMA-001",
            "session_id": "SESSION-SCHEMA",
            "active_state": "awaiting_customer_response",
            "evidence": ["email:test:001"],
            "knowledge": ["rule:test-response"],
            "requested_outcome": "prepare a draft",
        },
        human_approved=True,
    )

    for key in schema["required"]:
        assert key in result

    assert result["state"] in schema["properties"]["state"]["enum"]
    assert result["result"]["executed"] is False
    assert result["result"]["external_side_effect"] is False
