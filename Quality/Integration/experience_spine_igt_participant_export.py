"""Deterministic blind participant export boundary for Experience Spine IGT.

This module prepares participant-facing experiment input. It does not invoke a
model, authenticate delivery, or establish participant/cognitive evidence.
"""
from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from typing import Any

from experience_spine_igt import REQUIRED_RESPONSE_FIELDS, build_condition_payload
from experience_spine_igt_cases import hidden_expectation


FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
EXPORT_VERSION = "IGT-PARTICIPANT-EXPORT-1"
EXPORT_STATE = "READY_FOR_EXTERNAL_DELIVERY"
FORBIDDEN_KEYS = {
    "hidden_expectation",
    "target_invariants",
    "accepted_authorities",
    "accepted_actions",
    "required_scope",
    "required_evidence",
    "required_non_claims",
    "dimensions",
    "score",
    "max_score",
    "invariant_transfer",
    "cognitive_effect",
    "promotion_outcome",
    "participant_evidence_ref",
    "independence_attestation_ref",
    "execution_context_id",
    "provider_request_id",
    "provider_response_id",
    "provider_execution_id",
    "provider_receipt",
    "external_authenticity",
}


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(str(key))
            keys.update(_walk_keys(item))
    elif isinstance(value, list):
        for item in value:
            keys.update(_walk_keys(item))
    return keys


def _hidden_values(case_id: str) -> list[str]:
    hidden = hidden_expectation(case_id)
    values: list[str] = []
    for key in (
        "target_invariants",
        "accepted_authorities",
        "accepted_actions",
        "required_scope",
        "required_evidence",
        "required_non_claims",
    ):
        raw = hidden.get(key, [])
        if isinstance(raw, (list, tuple, set)):
            values.extend(str(item) for item in raw if str(item))
        elif raw:
            values.append(str(raw))
    return values


def _assert_blind(case_id: str, package_without_digest: dict) -> None:
    present_forbidden = sorted(FORBIDDEN_KEYS.intersection(_walk_keys(package_without_digest)))
    if present_forbidden:
        raise ValueError("FORBIDDEN_EXPORT_KEYS:" + ",".join(present_forbidden))

    serialized = _canonical(package_without_digest)
    leaked = sorted({value for value in _hidden_values(case_id) if value in serialized})
    if leaked:
        raise ValueError("HIDDEN_EVALUATOR_VALUE_LEAK:" + "|".join(leaked))


def build_participant_export(
    *,
    experiment_id: str,
    case_id: str,
    condition: str,
    baseline_sha: str,
    experience_packet: dict | None = None,
) -> dict:
    """Build one sealed participant-facing export package.

    The package stops at external delivery readiness. Execution identity and
    provider receipts belong to later evidence surfaces and are never fabricated.
    """
    experiment_id = str(experiment_id).strip()
    if not experiment_id:
        raise ValueError("EXPERIMENT_ID_REQUIRED")
    baseline_sha = str(baseline_sha).lower().strip()
    if not FULL_SHA_RE.fullmatch(baseline_sha):
        raise ValueError("FULL_BASELINE_SHA_REQUIRED")

    participant_payload = build_condition_payload(
        case_id,
        condition,
        experience_packet=deepcopy(experience_packet),
    )

    body = {
        "export_version": EXPORT_VERSION,
        "export_state": EXPORT_STATE,
        "experiment_id": experiment_id,
        "case_id": case_id,
        "condition": condition,
        "baseline_sha": baseline_sha,
        "participant_payload": participant_payload,
        "response_contract": {
            "format": "JSON_OBJECT",
            "required_fields": list(REQUIRED_RESPONSE_FIELDS),
            "instruction": "Return only one JSON object containing every required field.",
        },
        "execution_evidence": {
            "state": "NOT_YET_EXECUTED",
            "participant_evidence_ref": None,
            "provider_receipt": None,
        },
        "claim_boundary": "PARTICIPANT_INPUT_ONLY",
    }

    # The execution-evidence placeholders are intentionally present only as null
    # boundary markers. They must not become claims or identities at export time.
    forbidden_for_blind_check = deepcopy(body)
    forbidden_for_blind_check["execution_evidence"] = {"state": "NOT_YET_EXECUTED"}
    _assert_blind(case_id, forbidden_for_blind_check)

    identity_material = {
        "export_version": body["export_version"],
        "experiment_id": experiment_id,
        "case_id": case_id,
        "condition": condition,
        "baseline_sha": baseline_sha,
        "participant_payload": participant_payload,
        "response_contract": body["response_contract"],
    }
    body["export_id"] = "IGT-EXP-" + _digest(identity_material)[:24]
    body["package_digest"] = _digest(body)
    return body


def verify_participant_export(package: dict) -> dict:
    """Verify local export integrity and participant blindness only."""
    reasons: list[str] = []
    if not isinstance(package, dict):
        return {"state": "INVALID", "reasons": ["PACKAGE_NOT_MAPPING"]}

    required = {
        "export_version",
        "export_state",
        "experiment_id",
        "export_id",
        "case_id",
        "condition",
        "baseline_sha",
        "participant_payload",
        "response_contract",
        "execution_evidence",
        "claim_boundary",
        "package_digest",
    }
    missing = sorted(required.difference(package))
    if missing:
        reasons.append("MISSING_FIELDS:" + ",".join(missing))

    baseline = str(package.get("baseline_sha", ""))
    if not FULL_SHA_RE.fullmatch(baseline):
        reasons.append("BASELINE_SHA_INVALID")
    if package.get("export_state") != EXPORT_STATE:
        reasons.append("EXPORT_STATE_INVALID")
    if package.get("claim_boundary") != "PARTICIPANT_INPUT_ONLY":
        reasons.append("CLAIM_BOUNDARY_INVALID")

    execution = package.get("execution_evidence")
    if not isinstance(execution, dict):
        reasons.append("EXECUTION_EVIDENCE_BOUNDARY_INVALID")
    else:
        if execution.get("state") != "NOT_YET_EXECUTED":
            reasons.append("EXECUTION_STATE_PREMATURE")
        if execution.get("participant_evidence_ref") is not None:
            reasons.append("PARTICIPANT_EVIDENCE_PREMATURE")
        if execution.get("provider_receipt") is not None:
            reasons.append("PROVIDER_RECEIPT_PREMATURE")

    if not reasons and package.get("case_id") and package.get("condition"):
        try:
            blindness_view = deepcopy(package)
            blindness_view.pop("package_digest", None)
            blindness_view["execution_evidence"] = {"state": "NOT_YET_EXECUTED"}
            _assert_blind(str(package["case_id"]), blindness_view)
        except (KeyError, ValueError) as exc:
            reasons.append(str(exc))

    supplied_digest = package.get("package_digest")
    if supplied_digest:
        body = deepcopy(package)
        body.pop("package_digest", None)
        if supplied_digest != _digest(body):
            reasons.append("PACKAGE_DIGEST_MISMATCH")

    return {
        "state": "VERIFIED_PARTICIPANT_EXPORT" if not reasons else "INVALID",
        "reasons": reasons,
        "external_delivery": "NOT_PROVEN",
        "model_execution": "NOT_PROVEN",
        "provider_authenticity": "NOT_PROVEN",
        "cognitive_effect": "INCONCLUSIVE",
        "authority": "NONE",
    }
