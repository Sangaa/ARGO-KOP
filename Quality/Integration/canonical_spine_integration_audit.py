"""Build a conservative repository-wide canonical-spine integration audit.

This audit distinguishes structural evidence from proof. The evidence scanner can
only establish PARTIAL/MISSING; CONNECTED requires explicit seam evidence supplied
by an integration contract or executable test.
"""

from canonical_spine_evidence_scanner import scan
from canonical_spine_gap_map import SEAMS, VALID_STATES, build_gap_map

SEAM_KEYS = {f"{source} -> {destination}" for source, destination in SEAMS}


def _state_from_verified_record(seam, record):
    """Accept either a registry record or a legacy explicit state."""
    if isinstance(record, str):
        return record
    if not isinstance(record, dict):
        raise ValueError(f"invalid verified seam record: {seam}")

    state = record.get("state")
    if state == "CONNECTED":
        required = ("contract", "test", "trace")
        if not all(record.get(field) for field in required):
            raise ValueError(f"incomplete verified seam evidence: {seam}")
    return state


def audit(root, verified_seams=None):
    evidence = scan(root)
    verified_seams = verified_seams or {}

    for seam, record in verified_seams.items():
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        state = _state_from_verified_record(seam, record)
        if state not in VALID_STATES:
            raise ValueError(f"invalid seam state: {state}")
        evidence[seam] = state

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
