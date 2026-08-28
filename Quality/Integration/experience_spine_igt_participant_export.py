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
    "hidden_expectation", "target_invariants", "accepted_authorities", "accepted_actions",
    "required_scope", "required_evidence", "required_non_claims", "dimensions", "max_score",
    "invariant_transfer", "cognitive_effect", "promotion_outcome", "independence_attestation_ref",
    "execution_context_id", "provider_request_id", "provider_response_id", "provider_execution_id",
    "external_authenticity",
}
ALLOWED_PROVENANCE_PREFIX = ("participant_payload", "provenance_envelope")


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


def _walk_strings(value: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], str]]:
    found: list[tuple[tuple[str, ...], str]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            found.extend(_walk_strings(item, path + (str(key),)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(_walk_strings(item, path + (str(index),)))
    elif isinstance(value, str):
        found.append((path, value))
    return found


def _hidden_groups(case_id: str) -> tuple[set[str], set[str]]:
    hidden = hidden_expectation(case_id)
    targets = {str(v) for v in hidden.get("target_invariants", []) if str(v)}
    nonclaims = {str(v) for v in hidden.get("required_non_claims", []) if str(v)}
    return targets, nonclaims


def _assert_blind(case_id: str, package_without_digest: dict) -> None:
    present_forbidden = sorted(FORBIDDEN_KEYS.intersection(_walk_keys(package_without_digest)))
    if present_forbidden:
        raise ValueError("FORBIDDEN_EXPORT_KEYS:" + ",".join(present_forbidden))

    targets, nonclaims = _hidden_groups(case_id)
    leaked: list[str] = []
    for path, value in _walk_strings(package_without_digest):
        if value in targets:
            leaked.append(f"TARGET@{'/'.join(path)}={value}")
        if value in nonclaims and path[:2] != ALLOWED_PROVENANCE_PREFIX:
            leaked.append(f"NONCLAIM@{'/'.join(path)}={value}")
    if leaked:
        raise ValueError("HIDDEN_EVALUATOR_VALUE_LEAK:" + "|".join(sorted(leaked)))


def _identity_material(package: dict) -> dict:
    return {
        "export_version": package["export_version"],
        "experiment_id": package["experiment_id"],
        "case_id": package["case_id"],
        "condition": package["condition"],
        "baseline_sha": package["baseline_sha"],
        "participant_payload": package["participant_payload"],
        "response_contract": package["response_contract"],
    }


def build_participant_export(*, experiment_id: str, case_id: str, condition: str, baseline_sha: str,
                             experience_packet: dict | None = None) -> dict:
    experiment_id = str(experiment_id).strip()
    if not experiment_id:
        raise ValueError("EXPERIMENT_ID_REQUIRED")
    baseline_sha = str(baseline_sha).lower().strip()
    if not FULL_SHA_RE.fullmatch(baseline_sha):
        raise ValueError("FULL_BASELINE_SHA_REQUIRED")

    participant_payload = build_condition_payload(case_id, condition, experience_packet=deepcopy(experience_packet))
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
    blindness_view = deepcopy(body)
    blindness_view["execution_evidence"] = {"state": "NOT_YET_EXECUTED"}
    _assert_blind(case_id, blindness_view)
    body["export_id"] = "IGT-EXP-" + _digest(_identity_material(body))[:24]
    body["package_digest"] = _digest(body)
    return body


def verify_participant_export(package: dict) -> dict:
    reasons: list[str] = []
    if not isinstance(package, dict):
        return {"state": "INVALID", "reasons": ["PACKAGE_NOT_MAPPING"]}

    required = {
        "export_version", "export_state", "experiment_id", "export_id", "case_id", "condition",
        "baseline_sha", "participant_payload", "response_contract", "execution_evidence",
        "claim_boundary", "package_digest",
    }
    missing = sorted(required.difference(package))
    if missing:
        reasons.append("MISSING_FIELDS:" + ",".join(missing))
    if not FULL_SHA_RE.fullmatch(str(package.get("baseline_sha", ""))):
        reasons.append("BASELINE_SHA_INVALID")
    if package.get("export_version") != EXPORT_VERSION:
        reasons.append("EXPORT_VERSION_INVALID")
    if package.get("export_state") != EXPORT_STATE:
        reasons.append("EXPORT_STATE_INVALID")
    if package.get("claim_boundary") != "PARTICIPANT_INPUT_ONLY":
        reasons.append("CLAIM_BOUNDARY_INVALID")

    execution = package.get("execution_evidence")
    if not isinstance(execution, dict):
        reasons.append("EXECUTION_EVIDENCE_BOUNDARY_INVALID")
    else:
        if execution.get("state") != "NOT_YET_EXECUTED": reasons.append("EXECUTION_STATE_PREMATURE")
        if execution.get("participant_evidence_ref") is not None: reasons.append("PARTICIPANT_EVIDENCE_PREMATURE")
        if execution.get("provider_receipt") is not None: reasons.append("PROVIDER_RECEIPT_PREMATURE")

    identity_fields = ("export_version", "experiment_id", "case_id", "condition", "baseline_sha", "participant_payload", "response_contract")
    if all(field in package for field in identity_fields):
        expected = "IGT-EXP-" + _digest(_identity_material(package))[:24]
        if package.get("export_id") != expected:
            reasons.append("EXPORT_ID_MISMATCH")

    if package.get("case_id") and package.get("condition"):
        try:
            blindness_view = deepcopy(package)
            blindness_view.pop("package_digest", None)
            blindness_view.pop("export_id", None)
            blindness_view["execution_evidence"] = {"state": "NOT_YET_EXECUTED"}
            _assert_blind(str(package["case_id"]), blindness_view)
        except (KeyError, ValueError) as exc:
            reasons.append(str(exc))

    supplied = package.get("package_digest")
    if supplied:
        body = deepcopy(package)
        body.pop("package_digest", None)
        if supplied != _digest(body):
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
