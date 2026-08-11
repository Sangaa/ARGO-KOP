"""Synthetic end-to-end trace for the ARGO experimental spine."""


def trace(stages: list[dict]) -> dict:
    events = []
    for stage in stages:
        events.append({"stage": stage["stage"], "status": stage["status"]})
        if stage["status"] in {"HOLD", "BLOCKED"}:
            return {"status": "HALTED", "events": events}
    return {"status": "COMPLETED_SIMULATION", "events": events, "side_effect": False}
