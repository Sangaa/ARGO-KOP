"""Represent and validate canonical-spine seam coverage."""

from pathlib import Path

SEAMS = [
    ("Memory / Context", "Cognition"),
    ("Cognition", "Reasoning"),
    ("Reasoning", "Decision"),
    ("Decision", "Authorization"),
    ("Authorization", "Execution"),
    ("Execution", "Execution Trace"),
    ("Execution", "Outcome"),
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


def classify_candidate_path(path: str) -> str:
    """Classify a candidate by repository path without treating it as proof."""
    if not isinstance(path, str) or not path:
        raise ValueError(f"invalid candidate path: {path!r}")
    normalized = Path(path).as_posix()
    suffix = Path(normalized).suffix.lower()
    name = Path(normalized).name.lower()
    parts = {part.lower() for part in Path(normalized).parts}

    if "quality" in parts or name.startswith("test_") or name.endswith("_test.py"):
        return "test"
    if "contract" in name or "contracts" in parts:
        return "contract"
    if "trace" in name or "evidence" in name:
        return "trace"
    if suffix in {".py", ".js", ".ts", ".cpp", ".cc", ".c", ".java", ".kt"}:
        return "implementation"
    if suffix in {".md", ".rst", ".txt"} or "docs" in parts or "documentation" in parts:
        return "documentation"
    return "other"


def _candidate_paths(candidate_files, key):
    """Return bounded repository-relative candidate provenance for one seam."""
    if candidate_files is None:
        return []
    values = candidate_files.get(key, [])
    if not isinstance(values, list):
        raise ValueError(f"candidate files must be a list: {key}")

    normalized = []
    for value in values:
        if not isinstance(value, str) or not value:
            raise ValueError(f"invalid candidate path: {value!r}")
        path = Path(value)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"candidate path must be repository-relative: {value!r}")
        normalized_path = path.as_posix()
        if normalized_path not in normalized:
            normalized.append(normalized_path)
    return normalized


def _candidate_kinds(candidate_kinds, key, candidate_paths):
    """Return validated advisory kinds aligned with candidate provenance."""
    if candidate_kinds is None:
        return {}
    values = candidate_kinds.get(key, {})
    if not isinstance(values, dict):
        raise ValueError(f"candidate kinds must be a mapping: {key}")
    kinds = {}
    for path in candidate_paths:
        if path in values:
            kind = values[path]
            if not isinstance(kind, str) or not kind:
                raise ValueError(f"invalid candidate kind: {path!r}")
            kinds[path] = kind
    return kinds


def build_gap_map(
    evidence: dict,
    candidate_files: dict | None = None,
    candidate_kinds: dict | None = None,
) -> dict:
    """Build an evidence-bounded gap map with optional candidate provenance.

    Candidate provenance and kinds are discovery context only. They never
    change a seam state and never promote a seam to CONNECTED.
    """
    gaps = []
    candidate_kind_counts = {}
    for source, destination in SEAMS:
        key = f"{source} -> {destination}"
        state = evidence.get(key, "MISSING")
        if state not in VALID_STATES:
            raise ValueError(f"invalid seam state: {state}")
        if state != "CONNECTED":
            gap = {"seam": key, "state": state}
            candidates = _candidate_paths(candidate_files, key)
            if candidates:
                gap["candidate_files"] = candidates
                kinds = _candidate_kinds(candidate_kinds, key, candidates)
                if kinds:
                    gap["candidate_kinds"] = kinds
                    for kind in kinds.values():
                        candidate_kind_counts[kind] = candidate_kind_counts.get(kind, 0) + 1
            gaps.append(gap)
    return {
        "status": "GAP_MAP_COMPLETE",
        "seam_count": len(SEAMS),
        "gap_count": len(gaps),
        "candidate_kind_counts": candidate_kind_counts,
        "gaps": gaps,
    }
