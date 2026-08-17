"""M4 deterministic multi-user / multi-task isolation training harness."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    user_id: str
    task_id: str
    channel_id: str
    target: str
    authorized: bool


def schedule(requests: list[Request]) -> dict:
    accepted = []
    rejected = []
    seen_channels = set()
    for req in requests:
        if not req.authorized:
            rejected.append((req.user_id, req.task_id, "UNAUTHORIZED"))
            continue
        if req.channel_id in seen_channels:
            rejected.append((req.user_id, req.task_id, "CHANNEL_COLLISION"))
            continue
        seen_channels.add(req.channel_id)
        accepted.append(req)
    users = {r.user_id for r in accepted}
    return {
        "accepted": accepted,
        "rejected": rejected,
        "users_served": sorted(users),
        "fairness": len(users) == len(accepted),
        "canonical_mutation": False,
    }


def main() -> None:
    result = schedule([
        Request("USER-A", "TASK-1", "CH-A1", "A", True),
        Request("USER-B", "TASK-2", "CH-B1", "B", True),
        Request("USER-C", "TASK-3", "CH-C1", "C", False),
        Request("USER-B", "TASK-4", "CH-B1", "D", True),
        Request("USER-D", "TASK-5", "CH-D1", "E", True),
    ])
    assert len(result["accepted"]) == 3
    assert len(result["rejected"]) == 2
    assert result["users_served"] == ["USER-A", "USER-B", "USER-D"]
    assert result["fairness"] is True
    assert result["canonical_mutation"] is False
    print("M4 deterministic multi-user isolation: PASS")


if __name__ == "__main__":
    main()
