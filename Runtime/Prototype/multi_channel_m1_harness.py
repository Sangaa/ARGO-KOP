"""M1 multi-channel training harness.

Read-only, fixture-driven simulation for one user / multiple isolated tasks.
This module never writes canonical repository artifacts.

M1 training invariant: parallel logical work must not imply shared authority.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ChannelContext:
    user_id: str
    session_id: str
    task_id: str
    channel_id: str
    source_id: str
    fixture: Dict[str, Any]
    state: Dict[str, Any] = field(default_factory=dict)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def record(self, event: str, **payload: Any) -> None:
        self.trace.append(
            {
                "user_id": self.user_id,
                "session_id": self.session_id,
                "task_id": self.task_id,
                "channel_id": self.channel_id,
                "event": event,
                **payload,
            }
        )


def build_m1_contexts() -> List[ChannelContext]:
    """Return two independent task/channel contexts for one simulated user."""
    return [
        ChannelContext(
            user_id="USER-001",
            session_id="SESSION-M1-001",
            task_id="TASK-001",
            channel_id="CHANNEL-A",
            source_id="FIXTURE-A",
            fixture={"topic": "alpha", "value": 11},
        ),
        ChannelContext(
            user_id="USER-001",
            session_id="SESSION-M1-001",
            task_id="TASK-002",
            channel_id="CHANNEL-B",
            source_id="FIXTURE-B",
            fixture={"topic": "beta", "value": 22},
        ),
    ]


def process_channel(ctx: ChannelContext, *, force_failure: bool = False) -> Dict[str, Any]:
    """Process one channel without touching canonical state."""
    ctx.record("START", fixture_keys=sorted(ctx.fixture))
    ctx.state["observed_topic"] = ctx.fixture["topic"]
    ctx.record("OBSERVE", topic=ctx.fixture["topic"])
    if force_failure:
        ctx.record("FAIL", classification="SIMULATED_TASK_FAILURE")
        return {"status": "FAILED", "task_id": ctx.task_id, "channel_id": ctx.channel_id}
    result = {"status": "SUCCESS", "task_id": ctx.task_id, "channel_id": ctx.channel_id,
              "observed": dict(ctx.state)}
    ctx.record("COMPLETE", result_status="SUCCESS")
    return result


def run_m1(*, fail_task: str | None = None) -> Dict[str, Any]:
    """Run two logical channels and return deterministic reconciliation evidence."""
    contexts = build_m1_contexts()
    results: List[Dict[str, Any]] = []
    for ctx in contexts:
        results.append(process_channel(ctx, force_failure=(ctx.task_id == fail_task)))

    return {
        "mode": "M1_ONE_USER_MULTI_TASK_READ_ONLY",
        "canonical_mutation": False,
        "results": results,
        "traces": [ctx.trace for ctx in contexts],
        "contexts": [
            {
                "task_id": ctx.task_id,
                "channel_id": ctx.channel_id,
                "source_id": ctx.source_id,
                "state": dict(ctx.state),
            }
            for ctx in contexts
        ],
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_m1(), indent=2, sort_keys=True))
