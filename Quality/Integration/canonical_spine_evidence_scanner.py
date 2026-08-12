"""Derive conservative seam evidence from repository text without declaring architecture by naming alone."""

from pathlib import Path

from canonical_spine_gap_map import SEAMS

KEYWORDS = {
    "Memory / Context": ("memory", "context"),
    "Cognition": ("cognition", "reasoning_hold", "conflict"),
    "Reasoning": ("reasoning",),
    "Decision": ("decision",),
    "Authorization": ("authorization", "authorize"),
    "Execution": ("execution", "executor"),
    "Execution Trace": ("trace", "traceability"),
    "Outcome Evaluation": ("outcome", "evaluation"),
    "Feedback Quality": ("feedback", "quality"),
    "Learning Readiness": ("readiness", "learning_ready"),
    "Learning Pipeline": ("learning", "pipeline"),
}


def scan(root) -> dict:
    root = Path(root)
    text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore").lower()
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )
    evidence = {}
    for source, destination in SEAMS:
        source_seen = any(k in text for k in KEYWORDS[source])
        destination_seen = any(k in text for k in KEYWORDS[destination])
        if source_seen and destination_seen:
            evidence[f"{source} -> {destination}"] = "PARTIAL"
        else:
            evidence[f"{source} -> {destination}"] = "MISSING"
    return evidence
