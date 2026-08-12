"""Build a conservative repository-wide canonical-spine integration audit.

This audit distinguishes structural evidence from proof. The evidence scanner can
only establish PARTIAL/MISSING; CONNECTED requires explicit seam evidence supplied
by an integration contract or executable test.
"""

from canonical_spine_evidence_scanner import scan
from canonical_spine_gap_map import SEAMS, VALID_STATES, build_gap_map


def audit(root, verified_seams=None):
    evidence = scan(root)
    verified_seams = verified_seams or {}

    for seam, state in verified_seams.items():
        if seam not in {f"{s} -> {d}" for s, d in SEAMS}:
            raise ValueError(f"unknown seam: {seam}")
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
