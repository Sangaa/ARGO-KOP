"""Conservatively discover candidate seam evidence from repository artifacts.

This is a candidate-discovery layer only. It must never promote a seam to
CONNECTED and must never infer a relationship from unrelated files merely
because endpoint words occur somewhere in the repository.
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
    """Return seam states plus bounded candidate artifact locations.

    A seam becomes PARTIAL only when both endpoint concepts co-occur in one
    artifact. Candidate locations are provenance hints for the next evidence
    inspection step; they are not evidence of integration and never create
    CONNECTED.
    """
    root = Path(root)
    evidence = {f"{source} -> {destination}": "MISSING" for source, destination in SEAMS}
    candidate_files = {f"{source} -> {destination}": [] for source, destination in SEAMS}

    for path in _repository_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        for source, destination in SEAMS:
            key = f"{source} -> {destination}"
            if _endpoint_seen(text, source) and _endpoint_seen(text, destination):
                if evidence[key] == "MISSING":
                    evidence[key] = "PARTIAL"
                relative = path.relative_to(root).as_posix()
                if relative not in candidate_files[key]:
                    candidate_files[key].append(relative)

    return {"evidence": evidence, "candidate_files": candidate_files}
