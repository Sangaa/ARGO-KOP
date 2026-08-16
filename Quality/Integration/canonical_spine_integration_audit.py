"""Build a conservative canonical-spine integration audit.

Structural scanning establishes only PARTIAL/MISSING plus bounded candidate
artifact provenance. CONNECTED requires a verified seam record whose
contract/test/trace artifacts are real repository files and whose trace is a
materialized canonical execution-trace artifact.
"""

import json
from pathlib import Path, PurePosixPath

from canonical_spine_evidence_scanner import scan
from canonical_spine_gap_map import SEAMS, build_gap_map

SEAM_KEYS = {f"{source} -> {destination}" for source, destination in SEAMS}
REQUIRED_EVIDENCE = ("contract", "test", "trace")
REQUIRED_TRACE_FIELDS = ("record_type", "trace_id", "task_id", "session_id", "final_status")


def _local_file(root: Path, relative: str) -> bool:
    """Require a repository-relative regular file, never a traversal target."""
    candidate = PurePosixPath(relative)
    if candidate.is_absolute() or ".." in candidate.parts or not candidate.parts:
        return False
    return (root / candidate).is_file()


def _valid_trace_artifact(root: Path, relative: str) -> bool:
    """Require the same canonical trace shape emitted by the runtime producer."""
    candidate = PurePosixPath(relative)
    if candidate.is_absolute() or ".." in candidate.parts or not candidate.parts:
        return False
    path = root / candidate
    if not path.is_file() or path.suffix.lower() != ".json":
        return False
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return False
    return (
        isinstance(payload, dict)
        and payload.get("record_type") == "EXECUTION_TRACE"
        and all(isinstance(payload.get(field), str) and payload[field] for field in REQUIRED_TRACE_FIELDS)
    )


def _normalize_verified_records(verified_seams):
    """Normalize one record or seam-keyed registry mapping into record pairs."""
    if not isinstance(verified_seams, dict):
        raise ValueError("verified seam evidence must be a mapping")
    if "seam" in verified_seams:
        return [(verified_seams["seam"], verified_seams)]
    pairs = []
    for seam, record in verified_seams.items():
        if not isinstance(record, dict):
            raise ValueError(f"verified seam evidence must be a registry record: {seam}")
        pairs.append((seam, record))
    return pairs


def _state_from_verified_record(root: Path, seam, record):
    if not isinstance(record, dict):
        raise ValueError(f"verified seam evidence must be a registry record: {seam}")

    state = record.get("state")
    if state != "CONNECTED":
        raise ValueError(f"verified seam record is not CONNECTED: {seam}")
    if record.get("verification_status") != "VERIFIED":
        raise ValueError(f"verified seam record is not VERIFIED: {seam}")
    if not all(record.get(field) for field in REQUIRED_EVIDENCE):
        raise ValueError(f"incomplete verified seam evidence: {seam}")
    missing = [field for field in REQUIRED_EVIDENCE if not _local_file(root, record[field])]
    if missing:
        raise ValueError(f"verified seam evidence files missing or invalid: {seam}: {missing}")
    if not _valid_trace_artifact(root, record["trace"]):
        raise ValueError(f"verified seam trace is not a canonical execution trace: {seam}")
    return state


def audit(root, verified_seams=None):
    root = Path(root)
    scanned = scan(root)
    evidence = scanned["evidence"]
    candidate_files = scanned["candidate_files"]
    candidate_kinds = scanned["candidate_kinds"]
    verified_seams = verified_seams or {}

    for seam, record in _normalize_verified_records(verified_seams) if verified_seams else []:
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        evidence[seam] = _state_from_verified_record(root, seam, record)

    report = build_gap_map(evidence, candidate_files, candidate_kinds)
    return {
        "status": "INTEGRATION_AUDIT_COMPLETE",
        "seam_count": len(SEAMS),
        "evidence": evidence,
        "candidate_files": candidate_files,
        "candidate_kinds": candidate_kinds,
        "gap_map": report,
        "verified_connection_count": sum(
            1 for state in evidence.values() if state == "CONNECTED"
        ),
    }
