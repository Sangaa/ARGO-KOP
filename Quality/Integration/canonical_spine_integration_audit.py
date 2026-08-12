"""Build a conservative canonical-spine integration audit.

Structural scanning establishes only PARTIAL/MISSING plus bounded candidate
artifact provenance. CONNECTED requires a verified seam record whose
contract/test/trace artifacts are real repository files.
"""

from pathlib import Path, PurePosixPath

from canonical_spine_evidence_scanner import scan
from canonical_spine_gap_map import SEAMS, build_gap_map

SEAM_KEYS = {f"{source} -> {destination}" for source, destination in SEAMS}
REQUIRED_EVIDENCE = ("contract", "test", "trace")


def _local_file(root: Path, relative: str) -> bool:
    """Require a repository-relative regular file, never a traversal target."""
    candidate = PurePosixPath(relative)
    if candidate.is_absolute() or ".." in candidate.parts or not candidate.parts:
        return False
    return (root / candidate).is_file()


def _state_from_verified_record(root: Path, seam, record):
    if not isinstance(record, dict):
        raise ValueError(f"verified seam evidence must be a registry record: {seam}")

    state = record.get("state")
    if state != "CONNECTED":
        raise ValueError(f"verified seam record is not CONNECTED: {seam}")
    if not all(record.get(field) for field in REQUIRED_EVIDENCE):
        raise ValueError(f"incomplete verified seam evidence: {seam}")
    missing = [field for field in REQUIRED_EVIDENCE if not _local_file(root, record[field])]
    if missing:
        raise ValueError(f"verified seam evidence files missing or invalid: {seam}: {missing}")
    return state


def audit(root, verified_seams=None):
    root = Path(root)
    scanned = scan(root)
    evidence = scanned["evidence"]
    candidate_files = scanned["candidate_files"]
    verified_seams = verified_seams or {}

    for seam, record in verified_seams.items():
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        evidence[seam] = _state_from_verified_record(root, seam, record)

    report = build_gap_map(evidence)
    return {
        "status": "INTEGRATION_AUDIT_COMPLETE",
        "seam_count": len(SEAMS),
        "evidence": evidence,
        "candidate_files": candidate_files,
        "gap_map": report,
        "verified_connection_count": sum(
            1 for state in evidence.values() if state == "CONNECTED"
        ),
    }
