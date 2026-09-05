"""Map governed learning evidence into a promotion-gate candidate.

This Knowledge-owned adapter constructs data only. Promotion-gate evaluation is
owned by Runtime and must be invoked by an integration/runtime consumer rather
than imported upward into the Knowledge layer.
"""

from typing import Any, Dict


def build_candidate(
    evidence: Dict[str, Any],
    *,
    authority: bool = False,
    governing_conflict: bool = False,
) -> Dict[str, Any]:
    """Map an evidence package into the minimal Runtime promotion candidate."""
    return {
        "task_id": evidence["task_id"],
        "session_id": evidence["session_id"],
        "evidence": evidence["evidence"],
        "observed_result": evidence.get("observed_result"),
        "pattern": evidence["pattern"],
        "confidence": evidence["confidence"],
        "validation": evidence["validation"],
        "promotion_authority": authority,
        "governing_conflict": governing_conflict,
    }
