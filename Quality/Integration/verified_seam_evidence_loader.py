"""Load only evidence that exists as local contract/test/trace artifacts.

The loader remains conservative: it rejects incomplete or unverified candidates
instead of silently dropping them, so callers cannot mistake omission for
successful verification.
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
            raise ValueError("seam evidence must be a record")
        seam = candidate.get("seam")
        if candidate.get("verification_status") != "VERIFIED":
            raise ValueError(f"evidence not verified: {seam}")
        contract = candidate.get("contract", "")
        test = candidate.get("test", "")
        trace = candidate.get("trace", "")
        missing = [
            field for field, valid in (
                ("contract", _safe_path(root, contract)),
                ("test", _safe_path(root, test)),
                ("trace", _valid_trace_artifact(root, trace)),
            ) if not valid
        ]
        if missing:
            raise ValueError(f"verified seam evidence files missing or invalid: {seam}: {missing}")
        records.append(candidate)
    return register(records)
