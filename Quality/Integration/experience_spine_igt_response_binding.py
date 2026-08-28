"""Local sealed-export to participant-response binding for Experience Spine IGT.

This module proves only deterministic local attribution of one structured
participant response to one already-verified participant export. It does not
prove external delivery, model execution, provider authenticity, independence,
or cognitive effect.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any

from experience_spine_igt import REQUIRED_RESPONSE_FIELDS, validate_response
from experience_spine_igt_participant_export import verify_participant_export


SCHEMA_VERSION = "IGT-RESPONSE-BINDING-1"
BINDING_STATE = "LOCALLY_BOUND_RESPONSE"
CLAIM_BOUNDARY = "LOCAL_EXPORT_RESPONSE_IDENTITY_ONLY"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _binding_identity_material(binding: dict) -> dict:
    return {
        "schema_version": binding["schema_version"],
        "export_id": binding["export_id"],
        "export_package_digest": binding["export_package_digest"],
        "experiment_id": binding["experiment_id"],
        "case_id": binding["case_id"],
        "condition": binding["condition"],
        "baseline_sha": binding["baseline_sha"],
        "response_digest": binding["response_digest"],
    }


def _package_digest(binding: dict) -> str:
    material = deepcopy(binding)
    material.pop("binding_package_digest", None)
    return _digest(material)


def _validate_response_contract(response: object) -> None:
    missing = validate_response(response)  # type: ignore[arg-type]
    if missing:
        raise ValueError("RESPONSE_CONTRACT_INVALID:" + ",".join(missing))
    assert isinstance(response, dict)
    unexpected = sorted(set(response).difference(REQUIRED_RESPONSE_FIELDS))
    if unexpected:
        raise ValueError("UNEXPECTED_RESPONSE_FIELDS:" + ",".join(unexpected))


def build_response_binding(*, participant_export: dict, participant_response: dict) -> dict:
    """Bind one exact structured response to one exact verified participant export."""
    export_verification = verify_participant_export(participant_export)
    if export_verification.get("state") != "VERIFIED_PARTICIPANT_EXPORT":
        reasons = export_verification.get("reasons", [])
        raise ValueError("PARTICIPANT_EXPORT_INVALID:" + "|".join(str(reason) for reason in reasons))

    _validate_response_contract(participant_response)
    response = deepcopy(participant_response)
    body = {
        "schema_version": SCHEMA_VERSION,
        "binding_state": BINDING_STATE,
        "export_id": participant_export["export_id"],
        "export_package_digest": participant_export["package_digest"],
        "experiment_id": participant_export["experiment_id"],
        "case_id": participant_export["case_id"],
        "condition": participant_export["condition"],
        "baseline_sha": participant_export["baseline_sha"],
        "participant_response": response,
        "response_digest": _digest(response),
        "claim_boundary": CLAIM_BOUNDARY,
    }
    body["binding_id"] = "IGT-BIND-" + _digest(_binding_identity_material(body))[:24]
    body["binding_package_digest"] = _package_digest(body)
    return body


def verify_response_binding(*, binding: object, participant_export: object) -> dict:
    """Verify local attribution and integrity without upgrading external evidence."""
    reasons: list[str] = []
    if not isinstance(binding, dict):
        return {
            "state": "INVALID",
            "reasons": ["BINDING_NOT_MAPPING"],
            "local_attribution": "FAIL",
            "external_delivery": "NOT_PROVEN",
            "model_execution": "NOT_PROVEN",
            "provider_authenticity": "NOT_PROVEN",
            "authority": "NONE",
            "cognitive_effect": "INCONCLUSIVE",
        }
    if not isinstance(participant_export, dict):
        reasons.append("PARTICIPANT_EXPORT_NOT_MAPPING")
        export_verification = {"state": "INVALID", "reasons": ["PACKAGE_NOT_MAPPING"]}
    else:
        export_verification = verify_participant_export(participant_export)
        if export_verification.get("state") != "VERIFIED_PARTICIPANT_EXPORT":
            reasons.append("PARTICIPANT_EXPORT_INVALID")

    required = {
        "schema_version", "binding_state", "binding_id", "export_id",
        "export_package_digest", "experiment_id", "case_id", "condition",
        "baseline_sha", "participant_response", "response_digest",
        "claim_boundary", "binding_package_digest",
    }
    missing = sorted(required.difference(binding))
    if missing:
        reasons.append("MISSING_FIELDS:" + ",".join(missing))

    if binding.get("schema_version") != SCHEMA_VERSION:
        reasons.append("SCHEMA_VERSION_INVALID")
    if binding.get("binding_state") != BINDING_STATE:
        reasons.append("BINDING_STATE_INVALID")
    if binding.get("claim_boundary") != CLAIM_BOUNDARY:
        reasons.append("CLAIM_BOUNDARY_INVALID")

    response = binding.get("participant_response")
    try:
        _validate_response_contract(response)
    except (AssertionError, ValueError) as exc:
        reasons.append(str(exc) or "RESPONSE_CONTRACT_INVALID")

    if isinstance(response, dict):
        expected_response_digest = _digest(response)
        if binding.get("response_digest") != expected_response_digest:
            reasons.append("RESPONSE_DIGEST_MISMATCH")

    if isinstance(participant_export, dict) and export_verification.get("state") == "VERIFIED_PARTICIPANT_EXPORT":
        expected = {
            "export_id": participant_export.get("export_id"),
            "export_package_digest": participant_export.get("package_digest"),
            "experiment_id": participant_export.get("experiment_id"),
            "case_id": participant_export.get("case_id"),
            "condition": participant_export.get("condition"),
            "baseline_sha": participant_export.get("baseline_sha"),
        }
        for field, value in expected.items():
            if binding.get(field) != value:
                reasons.append(field.upper() + "_MISMATCH")

    identity_fields = {
        "schema_version", "export_id", "export_package_digest", "experiment_id",
        "case_id", "condition", "baseline_sha", "response_digest",
    }
    if identity_fields.issubset(binding):
        expected_binding_id = "IGT-BIND-" + _digest(_binding_identity_material(binding))[:24]
        if binding.get("binding_id") != expected_binding_id:
            reasons.append("BINDING_ID_MISMATCH")

    if binding.get("binding_package_digest"):
        if binding.get("binding_package_digest") != _package_digest(binding):
            reasons.append("BINDING_PACKAGE_DIGEST_MISMATCH")

    state = "VERIFIED_LOCAL_BINDING" if not reasons else "INVALID"
    return {
        "state": state,
        "reasons": reasons,
        "local_attribution": "PASS" if not reasons else "FAIL",
        "external_delivery": "NOT_PROVEN",
        "model_execution": "NOT_PROVEN",
        "provider_authenticity": "NOT_PROVEN",
        "authority": "NONE",
        "cognitive_effect": "INCONCLUSIVE",
    }
