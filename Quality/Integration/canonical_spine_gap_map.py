"""Represent and validate canonical-spine seam coverage."""

SEAMS = [
    ("Memory / Context", "Cognition"),
    ("Cognition", "Reasoning"),
    ("Reasoning", "Decision"),
    ("Decision", "Authorization"),
    ("Authorization", "Execution"),
    ("Execution", "Execution Trace"),
    ("Execution Trace", "Outcome Evaluation"),
    ("Outcome Evaluation", "Feedback Quality"),
    ("Feedback Quality", "Learning Readiness"),
    ("Learning Readiness", "Learning Pipeline"),
]

VALID_STATES = {
    "CONNECTED",
    "PARTIAL",
    "MISSING",
    "BLOCKED_BY_GOVERNANCE",
    "INTENTIONALLY_ISOLATED",
}


def build_gap_map(evidence: dict) -> dict:
    gaps = []
    for source, destination in SEAMS:
        key = f"{source} -> {destination}"
        state = evidence.get(key, "MISSING")
        if state not in VALID_STATES:
            raise ValueError(f"invalid seam state: {state}")
        if state != "CONNECTED":
            gaps.append({"seam": key, "state": state})
    return {
        "status": "GAP_MAP_COMPLETE",
        "seam_count": len(SEAMS),
        "gap_count": len(gaps),
        "gaps": gaps,
    }
