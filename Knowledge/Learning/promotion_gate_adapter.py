"""Adapter between governed learning evidence and the prototype promotion gate."""

from typing import Any, Dict

from Runtime.Prototype.learning_promotion_gate import evaluate


def build_candidate(evidence: Dict[str, Any], *, authority: bool = False) -> Dict[str, Any]:
    """Map an evidence package into the minimal promotion-gate candidate."""
    return {
        "task_id": evidence["task_id"],
        "session_id": evidence["session_id"],
        "evidence": evidence["evidence"],
        "observed_result": evidence.get("observed_result"),
        "pattern": evidence["pattern"],
        "confidence": evidence["confidence"],
        "validation": evidence["validation"],
        "promotion_authority": authority,
    }


def evaluate_evidence(evidence: Dict[str, Any], *, authority: bool = False) -> Dict[str, Any]:
    return evaluate(build_candidate(evidence, authority=authority))
