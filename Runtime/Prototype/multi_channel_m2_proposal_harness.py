"""M2 proposal-write simulation.

One simulated user, multiple isolated task channels. Each channel may write only
inside its own proposal workspace. Canonical repository mutation is forbidden.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ProposalWorkspace:
    task_id: str
    channel_id: str
    source_snapshot: Dict[str, Any]
    proposal: Dict[str, Any] = field(default_factory=dict)

    def propose(self, key: str, value: Any) -> None:
        self.proposal[key] = value

    def read_back(self) -> Dict[str, Any]:
        return deepcopy(self.proposal)


@dataclass
class M2Context:
    user_id: str
    session_id: str
    task_id: str
    channel_id: str
    workspace: ProposalWorkspace
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def record(self, event: str, **payload: Any) -> None:
        self.trace.append({
            "user_id": self.user_id,
            "session_id": self.session_id,
            "task_id": self.task_id,
            "channel_id": self.channel_id,
            "event": event,
            **payload,
        })


def build_m2_contexts() -> List[M2Context]:
    return [
        M2Context(
            user_id="USER-001",
            session_id="SESSION-M2-001",
            task_id="TASK-001",
            channel_id="CHANNEL-A",
            workspace=ProposalWorkspace("TASK-001", "CHANNEL-A", {"topic": "alpha", "value": 11}),
        ),
        M2Context(
            user_id="USER-001",
            session_id="SESSION-M2-001",
            task_id="TASK-002",
            channel_id="CHANNEL-B",
            workspace=ProposalWorkspace("TASK-002", "CHANNEL-B", {"topic": "beta", "value": 22}),
        ),
    ]


def run_m2(*, collide: bool = False) -> Dict[str, Any]:
    contexts = build_m2_contexts()
    for ctx in contexts:
        ctx.record("START", source_snapshot=dict(ctx.workspace.source_snapshot))
        value = ctx.workspace.source_snapshot["value"] + 1
        ctx.workspace.propose("value", value)
        if collide:
            ctx.workspace.propose("shared_target", "same-target")
        else:
            ctx.workspace.propose("shared_target", ctx.channel_id)
        ctx.record("PROPOSAL_WRITE", proposal=ctx.workspace.read_back())
        ctx.record("READ_BACK", proposal=ctx.workspace.read_back())

    proposals = [
        {
            "task_id": c.task_id,
            "channel_id": c.channel_id,
            "proposal": c.workspace.read_back(),
        }
        for c in contexts
    ]
    conflicts = []
    if collide and proposals[0]["proposal"].get("shared_target") == proposals[1]["proposal"].get("shared_target"):
        conflicts.append({"type": "SHARED_TARGET_OVERLAP", "task_ids": ["TASK-001", "TASK-002"]})

    return {
        "mode": "M2_ONE_USER_MULTI_TASK_PROPOSAL_WRITE",
        "canonical_mutation": False,
        "proposal_workspaces": proposals,
        "conflicts": conflicts,
        "traces": [c.trace for c in contexts],
    }
