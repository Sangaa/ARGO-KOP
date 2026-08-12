"""Run canonical acceptance_scenarios.json against the cognitive harness."""

import json
from pathlib import Path

from cognitive_loop_harness import run

ROOT = Path(__file__).resolve().parent
SCENARIOS = ROOT / "acceptance_scenarios.json"


def payload(*, missing_evidence: bool = False):
    return {
        "task_id": "SCENARIO-RUN",
        "session_id": "SCENARIO-SESSION",
        "active_state": "awaiting_customer_response",
        "evidence": [] if missing_evidence else ["scenario:evidence:001"],
        "knowledge": ["scenario:rule:001"],
        "requested_outcome": "prepare a response draft",
    }


def main() -> int:
    data = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    failures = []
    for scenario in data["scenarios"]:
        item = run(
            payload(missing_evidence=scenario["name"] == "missing_evidence"),
            human_approved=scenario["human_approved"],
        )
        checks = {
            "state": item["state"] == scenario["expected_state"],
            "executed": item["result"]["executed"] == scenario["expected_executed"],
            "external_side_effect": item["result"]["external_side_effect"] == scenario["expected_external_side_effect"],
        }
        if not all(checks.values()):
            failures.append({"id": scenario["id"], "checks": checks, "actual": item})
        else:
            print(f"PASS {scenario['id']}")

    if failures:
        print(json.dumps({"status": "FAIL", "failures": failures}, indent=2))
        return 1

    print(json.dumps({"status": "PASS", "scenarios": len(data["scenarios"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
