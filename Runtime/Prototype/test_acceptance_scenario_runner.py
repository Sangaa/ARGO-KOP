"""Acceptance tests for the canonical scenario runner."""

import json
from pathlib import Path

from cognitive_loop_harness import run

ROOT = Path(__file__).resolve().parent


def test_all_canonical_scenarios_match_expected_behavior():
    scenarios = json.loads((ROOT / "acceptance_scenarios.json").read_text(encoding="utf-8"))["scenarios"]
    for scenario in scenarios:
        result = run(
            {
                "task_id": scenario["id"],
                "session_id": "SCENARIO-TEST",
                "active_state": "awaiting_customer_response",
                "evidence": [] if scenario["name"] == "missing_evidence" else ["scenario:evidence"],
                "knowledge": ["scenario:rule"],
                "requested_outcome": "prepare a response draft",
            },
            human_approved=scenario["human_approved"],
        )
        assert result["state"] == scenario["expected_state"]
        assert result["result"]["executed"] == scenario["expected_executed"]
        assert result["result"]["external_side_effect"] == scenario["expected_external_side_effect"]


def test_missing_human_authorization_is_reversible_hold():
    result = run(
        {
            "task_id": "AUTH-HOLD-001",
            "session_id": "SCENARIO-TEST",
            "active_state": "awaiting_customer_response",
            "evidence": ["scenario:evidence"],
            "knowledge": ["scenario:rule"],
            "requested_outcome": "prepare a response draft",
        },
        human_approved=False,
    )
    assert result["authorization"]["status"] == "HOLD"
    assert result["state"] == "HOLD"
    assert result["result"]["executed"] is False
