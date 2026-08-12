"""Load only evidence that exists as local contract/test/trace artifacts.

The loader remains conservative: it may reject a candidate for malformed trace
materialization, but it never upgrades a candidate because of names or keyword
co-occurrence alone.
"""

import json
from pathlib import Path, PurePosixPath

from verified_seam_evidence_registry import register

_REQUIRED_TRACE_FIELDS = ("record_type", "trace_id", "task_id", "session_id", "final_status")


def _safe_path(root: Path, relative: str):
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        return None
    candidate = root / path
    return candidate if candidate.is_file() else None


def _valid_trace_artifact(root: Path, relative: str) -> bool:
    """Require a materialized JSON execution-trace artifact with core identity."""
    path = _safe_path(root, relative)
    if path is None or path.suffix.lower() != ".json":
        return False
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return False
    return (
        isinstance(payload, dict)
        and all(isinstance(payload.get(field), str) and payload[field] for field in _REQUIRED_TRACE_FIELDS)
        and payload.get("record_type") == "EXECUTION_TRACE"
    )


def load_records(root, candidates):
    root = Path(root)
    records = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        contract = candidate.get("contract", "")
        test = candidate.get("test", "")
        trace = candidate.get("trace", "")
        if _safe_path(root, contract) and _safe_path(root, test) and _valid_trace_artifact(root, trace):
            records.append(candidate)
    return register(records)
