"""Normalize the connectivity audit into actionable gap classes."""

from full_stack_connectivity_audit import audit


def classify_audit(root):
    result = audit(root)
    gaps = []
    for path in result["orphan_candidates"]:
        gaps.append({"path": path, "gap": "ORPHAN_CANDIDATE", "severity": "REVIEW"})
    for path in result["untested_candidates"]:
        gaps.append({"path": path, "gap": "UNTESTED_CANDIDATE", "severity": "HIGH"})
    return {**result, "gap_count": len(gaps), "gaps": gaps}
