"""Experience Spine IGT participant payload, qualification and scoring helpers.

This module evaluates the structure and qualification of IGT evidence. It does
not invoke a model and cannot by itself establish cognitive improvement.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Iterable

from experience_spine_igt_cases import hidden_expectation, participant_case


CONDITIONS = {"B0", "L1", "L2"}
DIMENSIONS = (
    "invariant_identification",
    "authority_selection",
    "scope_preservation",
    "action_selection",
    "evidence_quality",
    "explanation_fidelity",
)
REQUIRED_RESPONSE_FIELDS = (
    "prediction",
    "identified_invariants",
    "selected_authority",
    "scope",
    "action",
    "evidence_refs",
    "non_claims",
)
INDEPENDENCE_FIELDS = (
    "execution_independence",
    "information_independence",
    "state_independence",
    "temporal_independence",
    "mutation_independence",
)
PROVENANCE_ITEM_FIELDS = {
    "evidence",
    "evidence_state",
    "authority_state",
    "source_identity",
    "source_type",
    "evidence_group",
    "consumer_routes",
}
USABLE_PACKET_STATES = {"READY", "REVIEW_REQUIRED"}


def _set(value: Iterable[str] | str | None) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {value}
    return {str(item) for item in value}


def validate_case_separation(case_id: str) -> dict:
    """Verify evaluator-only reasoning keys do not leak into participant data.

    Candidate action labels may be participant-visible by design. Leakage is the
    hidden mapping of which action/authority is correct, plus evaluator-only
    invariants/non-claims—not the mere presence of a choice label.
    """
    visible = participant_case(case_id)
    hidden = hidden_expectation(case_id)
    serialized_visible = repr(visible)
    leaked = []
    for value in list(hidden["target_invariants"]) + list(hidden["required_non_claims"]):
        if str(value) in serialized_visible:
            leaked.append(str(value))
    return {
        "case_id": case_id,
        "separation": "PASS" if not leaked else "FAIL",
        "leaked_hidden_values": sorted(leaked),
    }


def materialize_experience_views(experience_packet: dict) -> tuple[dict, dict]:
    """Derive L1 decision view and L2 provenance envelope from one packet.

    This prevents a caller from accidentally giving L1 the provenance/correlation
    fields whose incremental effect belongs to L2. The source packet is not
    mutated.
    """
    if not isinstance(experience_packet, dict):
        raise ValueError("EXPERIENCE_PACKET_REQUIRED")
    if str(experience_packet.get("status")) not in USABLE_PACKET_STATES:
        raise ValueError("EXPERIENCE_PACKET_NOT_USABLE")
    if not isinstance(experience_packet.get("experience_items"), list):
        raise ValueError("EXPERIENCE_ITEMS_REQUIRED")

    source = deepcopy(experience_packet)
    decision = deepcopy(experience_packet)
    provenance_items = []

    for index, item in enumerate(decision["experience_items"]):
        if not isinstance(item, dict):
            raise ValueError(f"EXPERIENCE_ITEM_NOT_MAPPING:{index}")
        original = source["experience_items"][index]
        provenance = {"knowledge_id": original.get("knowledge_id")}
        for field in PROVENANCE_ITEM_FIELDS:
            if field in original:
                provenance[field] = deepcopy(original[field])
                item.pop(field, None)
        provenance_items.append(provenance)

    correlated = deepcopy(source.get("correlated_evidence_groups", []))
    evidence_boundary = source.get("evidence_boundary")
    decision.pop("correlated_evidence_groups", None)
    decision.pop("evidence_boundary", None)
    decision.pop("authority_boundary", None)

    provenance_envelope = {
        "experience_items": provenance_items,
        "correlated_evidence_groups": correlated,
        "evidence_boundary": evidence_boundary,
        "authority_boundary": source.get("authority_boundary"),
    }
    return decision, provenance_envelope


def build_condition_payload(
    case_id: str,
    condition: str,
    *,
    experience_packet: dict | None = None,
) -> dict:
    """Construct B0/L1/L2 input with deterministic information separation."""
    if condition not in CONDITIONS:
        raise ValueError(f"UNSUPPORTED_CONDITION:{condition}")

    case = participant_case(case_id)
    payload = {
        "case_id": case_id,
        "condition": condition,
        "title": case["title"],
        "context": deepcopy(case["context"]),
        "instruction": case["generic_instruction"],
    }

    if condition in {"L1", "L2"}:
        decision_view, provenance_view = materialize_experience_views(experience_packet)
        payload["experience_packet"] = decision_view
        if condition == "L2":
            payload["provenance_envelope"] = provenance_view

    return payload


def validate_response(response: dict) -> list[str]:
    """Return structurally missing fields; empty/wrong values remain scoreable."""
    if not isinstance(response, dict):
        return ["RESPONSE_NOT_MAPPING"]
    return [field for field in REQUIRED_RESPONSE_FIELDS if field not in response]


def score_response(case_id: str, response: dict) -> dict:
    """Score structured participant output against hidden IGT expectations."""
    missing = validate_response(response)
    if missing:
        return {
            "case_id": case_id,
            "status": "INVALID_RESPONSE",
            "missing": missing,
            "score": 0,
            "max_score": len(DIMENSIONS),
            "dimensions": {dimension: 0 for dimension in DIMENSIONS},
        }

    expected = hidden_expectation(case_id)
    identified = _set(response["identified_invariants"])
    scope = _set(response["scope"])
    evidence = _set(response["evidence_refs"])
    non_claims = _set(response["non_claims"])

    dimensions = {
        "invariant_identification": int(_set(expected["target_invariants"]).issubset(identified)),
        "authority_selection": int(str(response["selected_authority"]) in expected["accepted_authorities"]),
        "scope_preservation": int(scope == _set(expected["required_scope"])),
        "action_selection": int(str(response["action"]) in expected["accepted_actions"]),
        "evidence_quality": int(_set(expected["required_evidence"]).issubset(evidence)),
        "explanation_fidelity": int(_set(expected["required_non_claims"]).issubset(non_claims)),
    }
    total = sum(dimensions.values())
    return {
        "case_id": case_id,
        "status": "PASS" if total == len(DIMENSIONS) else "FAIL",
        "score": total,
        "max_score": len(DIMENSIONS),
        "dimensions": dimensions,
    }


def qualify_run(run: dict) -> dict:
    """Apply MI-IGT independence/leakage quarantine rules to one evidence run."""
    reasons: list[str] = []

    if not run.get("baseline_sha"):
        reasons.append("BASELINE_SHA_MISSING")

    for field in INDEPENDENCE_FIELDS:
        value = str(run.get(field, "UNKNOWN")).upper()
        if value != "YES":
            reasons.append(f"{field.upper()}_{value}")

    if str(run.get("source_conclusion_withheld", "UNKNOWN")).upper() != "YES":
        reasons.append("SOURCE_CONCLUSION_NOT_WITHHELD")
    if str(run.get("leakage_detected", "UNKNOWN")).upper() != "NO":
        reasons.append("LEAKAGE_NOT_CLEARED")
    if not run.get("execution_context_id"):
        reasons.append("EXECUTION_CONTEXT_ID_MISSING")
    if not run.get("independence_attestation_ref"):
        reasons.append("INDEPENDENCE_ATTESTATION_REF_MISSING")
    if str(run.get("participant_kind", "UNKNOWN")) == "MODEL_RUN" and not run.get("participant_evidence_ref"):
        reasons.append("PARTICIPANT_EVIDENCE_REF_MISSING")
    if not run.get("case_id") or not run.get("condition"):
        reasons.append("RUN_IDENTITY_INCOMPLETE")

    qualified = not reasons
    return {
        "evidence_state": "QUALIFIED" if qualified else "QUARANTINED",
        "independence_result": "PASS" if qualified else "INCONCLUSIVE",
        "promotion_outcome": "ELIGIBLE_FOR_BOUNDED_ANALYSIS" if qualified else "INCONCLUSIVE",
        "reasons": reasons,
    }


def evaluate_run(run: dict) -> dict:
    """Combine evidence qualification and response scoring without overclaiming."""
    case_id = str(run.get("case_id", ""))
    condition = str(run.get("condition", ""))
    if condition not in CONDITIONS:
        raise ValueError(f"UNSUPPORTED_CONDITION:{condition}")

    qualification = qualify_run(run)
    scoring = score_response(case_id, run.get("response", {}))

    if qualification["evidence_state"] != "QUALIFIED":
        transfer = "INCONCLUSIVE"
    elif scoring["status"] == "PASS":
        transfer = "PASS"
    elif scoring["status"] == "FAIL":
        transfer = "FAIL"
    else:
        transfer = "INCONCLUSIVE"

    return {
        "run_id": run.get("run_id"),
        "case_id": case_id,
        "condition": condition,
        "participant_kind": run.get("participant_kind", "UNKNOWN"),
        "participant_evidence_ref": run.get("participant_evidence_ref"),
        "independence_attestation_ref": run.get("independence_attestation_ref"),
        "execution_context_id": run.get("execution_context_id"),
        "qualification": qualification,
        "scoring": scoring,
        "invariant_transfer": transfer,
        "cognitive_effect_claim": "NOT_ESTABLISHED_BY_SINGLE_RUN_EVALUATOR",
        "authority": "NONE",
    }


def compare_conditions(evaluated_runs: list[dict]) -> dict:
    """Compare qualified condition scores without silently shadowing duplicate runs."""
    grouped: dict[str, dict[str, list[dict]]] = {}
    for result in evaluated_runs:
        if result["qualification"]["evidence_state"] != "QUALIFIED":
            continue
        grouped.setdefault(result["case_id"], {}).setdefault(result["condition"], []).append(result)

    comparisons = []
    ambiguities = []
    for case_id, conditions in sorted(grouped.items()):
        duplicate_conditions = sorted(condition for condition, runs in conditions.items() if len(runs) > 1)
        if duplicate_conditions:
            ambiguities.append(
                {
                    "case_id": case_id,
                    "duplicate_conditions": duplicate_conditions,
                    "state": "AMBIGUOUS_MULTIPLE_QUALIFIED_RUNS",
                }
            )
            continue

        single = {condition: runs[0] for condition, runs in conditions.items()}
        row = {"case_id": case_id, "conditions_present": sorted(single)}
        if "B0" in single and "L1" in single:
            row["L1_minus_B0"] = single["L1"]["scoring"]["score"] - single["B0"]["scoring"]["score"]
        if "L1" in single and "L2" in single:
            row["L2_minus_L1"] = single["L2"]["scoring"]["score"] - single["L1"]["scoring"]["score"]
        comparisons.append(row)

    return {
        "comparisons": comparisons,
        "ambiguities": ambiguities,
        "interpretation_boundary": (
            "SCORE_DIFFERENCE_IS_DESCRIPTIVE_ONLY; evaluator output does not prove causal cognitive improvement"
        ),
        "cognitive_effect": "INCONCLUSIVE_WITHOUT_QUALIFIED_INDEPENDENT_MODEL_RUN_DESIGN",
    }


def bounded_transfer_readiness(evaluated_runs: list[dict]) -> dict:
    """Check minimum evidence shape for later bounded transfer interpretation."""
    qualified_model_runs = [
        run
        for run in evaluated_runs
        if run["qualification"]["evidence_state"] == "QUALIFIED"
        and run.get("participant_kind") == "MODEL_RUN"
        and bool(run.get("participant_evidence_ref"))
        and bool(run.get("independence_attestation_ref"))
        and run["invariant_transfer"] in {"PASS", "FAIL"}
    ]
    case_ids = {run["case_id"] for run in qualified_model_runs}
    contexts = {run.get("execution_context_id") for run in qualified_model_runs}
    ready = len(case_ids) >= 2 and len(contexts) >= 2
    return {
        "status": "READY_FOR_BOUNDED_TRANSFER_ANALYSIS" if ready else "INSUFFICIENT_INDEPENDENT_MODEL_EVIDENCE",
        "qualified_model_runs": len(qualified_model_runs),
        "materially_distinct_cases": len(case_ids),
        "distinct_execution_contexts": len(contexts),
        "attestation_verification": "REQUIRED_OUTSIDE_STRUCTURAL_EVALUATOR",
        "promotion": "NONE",
        "broad_generalization": "UNPROVEN",
        "model_weight_change": "UNPROVEN",
    }
