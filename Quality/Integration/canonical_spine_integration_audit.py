"""Build a conservative repository-wide canonical-spine integration audit.

Structural scanning can establish PARTIAL/MISSING only. CONNECTED requires a
verified seam record carrying contract, test and trace evidence.
"""

from canonical_spine_evidence_scanner import scan
from canonical_spine_gap_map import SEAMS, build_gap_map

SEAM_KEYS = {f"{source} -> {destination}" for source, destination in SEAMS}
REQUIRED_EVIDENCE = ("contract", "test", "trace")


def _state_from_verified_record(seam, record):
    if not isinstance(record, dict):
        raise ValueError(f"verified seam evidence must be a registry record: {seam}")

    state = record.get("state")
    if state != "CONNECTED":
        raise ValueError(f"verified seam record is not CONNECTED: {seam}")
    if not all(record.get(field) for field in REQUIRED_EVIDENCE):
        raise ValueError(f"incomplete verified seam evidence: {seam}")
    return state


def audit(root, verified_seams=None):
    evidence = scan(root)
    verified_seams = verified_seams or {}

    for seam, record in verified_seams.items():
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        evidence[seam] = _state_from_verified_record(seam, record)

    report = build_gap_map(evidence)
    return {
        "status": "INTEGRATION_AUDIT_COMPLETE",
        "seam_count": len(SEAMS),
        "evidence": evidence,
        "gap_map": report,
        "verified_connection_count": sum(
            1 for state in evidence.values() if state == "CONNECTED"
        ),
    }
