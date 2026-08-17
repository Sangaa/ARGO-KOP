"""M3 deterministic reconciliation training harness.

Simulates multiple isolated proposals converging on one reconciliation object.
No canonical mutation and no automatic merge are permitted.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Proposal:
    task_id: str
    channel_id: str
    target: str
    value: str


def reconcile(proposals: list[Proposal]) -> dict:
    by_target: dict[str, list[Proposal]] = {}
    for proposal in proposals:
        by_target.setdefault(proposal.target, []).append(proposal)

    conflicts = []
    decisions = []
    for target, items in by_target.items():
        values = {item.value for item in items}
        if len(values) > 1:
            conflicts.append({"target": target, "proposals": [i.task_id for i in items]})
        else:
            decisions.append({"target": target, "value": next(iter(values)), "proposals": [i.task_id for i in items]})

    return {
        "canonical_mutation": False,
        "automatic_merge": False,
        "decisions": decisions,
        "conflicts": conflicts,
        "status": "CONFLICT" if conflicts else "RECONCILED",
    }


def main() -> None:
    result = reconcile([
        Proposal("TASK-001", "CH-001", "shipment:A", "VALUE-A"),
        Proposal("TASK-002", "CH-002", "shipment:A", "VALUE-B"),
        Proposal("TASK-003", "CH-003", "shipment:B", "VALUE-C"),
    ])
    assert result["canonical_mutation"] is False
    assert result["automatic_merge"] is False
    assert result["status"] == "CONFLICT"
    assert len(result["conflicts"]) == 1
    assert result["decisions"][0]["target"] == "shipment:B"
    print("M3 deterministic reconciliation: PASS")


if __name__ == "__main__":
    main()
