"""Derive conservative seam evidence from repository text.

The scanner is a candidate-discovery layer only. It must never promote a seam
to CONNECTED and must avoid declaring a relationship merely because unrelated
files somewhere in the repository mention both endpoint concepts.
"""

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


def _repository_files(root: Path):
    return (
        path
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )


def _endpoint_seen(text: str, endpoint: str) -> bool:
    return any(keyword in text for keyword in KEYWORDS[endpoint])


def scan(root) -> dict:
    """Return PARTIAL only when both endpoint concepts co-occur in one file.

    Repository-wide co-occurrence is intentionally not treated as relationship
    evidence because it produces false positives from unrelated documents.
    CONNECTED remains impossible at this layer.
    """
    root = Path(root)
    evidence = {f"{source} -> {destination}": "MISSING" for source, destination in SEAMS}

    for path in _repository_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        for source, destination in SEAMS:
            key = f"{source} -> {destination}"
            if evidence[key] == "PARTIAL":
                continue
            if _endpoint_seen(text, source) and _endpoint_seen(text, destination):
                evidence[key] = "PARTIAL"

    return evidence
