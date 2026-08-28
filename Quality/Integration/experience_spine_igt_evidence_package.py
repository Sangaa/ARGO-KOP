"""Portable evidence package gate for independently produced Experience Spine IGT runs.

This module verifies local structure, deterministic content integrity, condition
isolation and MI-IGT qualification surfaces. It cannot authenticate an external
model execution and never promotes cognitive-effect claims by itself.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import re
from typing import Iterable

from experience_spine_igt import (
    CONDITIONS,
    INDEPENDENCE_FIELDS,
    PROVENANCE_ITEM_FIELDS,
    REQUIRED_RESPONSE_FIELDS,
)


SCHEMA_VERSION = "IGT-MODEL-RUN-PACKAGE-1.0"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_TOP_LEVEL = (
    "schema_version",
    "package_id",
    "run_id",
    "case_id",
    "condition",
    "participant_kind",
    "repository_baseline_sha",
    "execution_context_id",
    "source_model",
    "source_instance_id",
    "execution_surface",
    "execution_started_at",
    "execution_completed_at",
    "participant_payload",
    "participant_response",
    "independence_attestation",
    "participant_evidence_ref",
    "independence_attestation_ref",
    "payload_digest",
    "response_digest",
    "package_digest",
)
FORBIDDEN_EVALUATOR_KEYS = {
    "hidden_expectation",
    "hidden_expectations",
    "accepted_authorities",
    "accepted_actions",
    "target_invariants",
    "required_scope",
    "required_evidence",
    "required_non_claims",
    "correct_action",
    "correct_answer",
    "expected_answer",
    "evaluator_expectation",
    "evaluator_expectations",
}
CONDITION_STRUCTURAL_INVALID_REASONS = {
    "L1_EXPERIENCE_PACKET_MISSING",
    "L1_EXPERIENCE_ITEMS_NOT_LIST",
    "L2_EXPERIENCE_PACKET_MISSING",
    "L2_PROVENANCE_ENVELOPE_MISSING",
}


def canonical_json(value: object) -> str:
    """Stable UTF-8 JSON representation used only for local integrity checks."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest_value(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def package_digest(package: dict) -> str:
    if not isinstance(package, dict):
        raise TypeError("PACKAGE_NOT_MAPPING")
    material = deepcopy(package)
    material.pop("package_digest", None)
    return digest_value(material)


def seal_package(package: dict) -> dict:
    """Return a copy with deterministic payload/response/package digests."""
    if not isinstance(package, dict):
        raise TypeError("PACKAGE_NOT_MAPPING")
    sealed = deepcopy(package)
    sealed["payload_digest"] = digest_value(sealed.get("participant_payload"))
    sealed["response_digest"] = digest_value(sealed.get("participant_response"))
    sealed.pop("package_digest", None)
    sealed["package_digest"] = package_digest(sealed)
    return sealed


def _walk_forbidden_keys(value: object, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            key_text = str(key)
            child = f"{path}.{key_text}"
            if key_text in FORBIDDEN_EVALUATOR_KEYS:
                findings.append(child)
            findings.extend(_walk_forbidden_keys(nested, child))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            findings.extend(_walk_forbidden_keys(nested, f"{path}[{index}]"))
    return findings


def _missing_keys(mapping: object, required: Iterable[str]) -> list[str]:
    if not isinstance(mapping, dict):
        return list(required)
    return [key for key in required if key not in mapping]


def _validate_condition_payload(package: dict) -> list[str]:
    reasons: list[str] = []
    payload = package.get("participant_payload")
    if not isinstance(payload, dict):
        return ["PARTICIPANT_PAYLOAD_NOT_MAPPING"]

    case_id = package.get("case_id")
    condition = package.get("condition")
    if payload.get("case_id") != case_id:
        reasons.append("PAYLOAD_CASE_ID_MISMATCH")
    if payload.get("condition") != condition:
        reasons.append("PAYLOAD_CONDITION_MISMATCH")

    if condition == "B0":
        if "experience_packet" in payload:
            reasons.append("B0_EXPERIENCE_PACKET_LEAK")
        if "provenance_envelope" in payload:
            reasons.append("B0_PROVENANCE_LEAK")
    elif condition == "L1":
        experience = payload.get("experience_packet")
        if not isinstance(experience, dict):
            reasons.append("L1_EXPERIENCE_PACKET_MISSING")
        if "provenance_envelope" in payload:
            reasons.append("L1_PROVENANCE_ENVELOPE_LEAK")
        if isinstance(experience, dict):
            for forbidden_top in (
                "correlated_evidence_groups",
                "evidence_boundary",
                "authority_boundary",
            ):
                if forbidden_top in experience:
                    reasons.append(f"L1_{forbidden_top.upper()}_LEAK")
            items = experience.get("experience_items", [])
            if not isinstance(items, list):
                reasons.append("L1_EXPERIENCE_ITEMS_NOT_LIST")
            else:
                for index, item in enumerate(items):
                    if not isinstance(item, dict):
                        reasons.append(f"L1_ITEM_{index}_NOT_MAPPING")
                        continue
                    leaked = sorted(PROVENANCE_ITEM_FIELDS.intersection(item))
                    for field in leaked:
                        reasons.append(f"L1_ITEM_{index}_{field.upper()}_LEAK")
    elif condition == "L2":
        if not isinstance(payload.get("experience_packet"), dict):
            reasons.append("L2_EXPERIENCE_PACKET_MISSING")
        if not isinstance(payload.get("provenance_envelope"), dict):
            reasons.append("L2_PROVENANCE_ENVELOPE_MISSING")
    else:
        reasons.append("UNSUPPORTED_CONDITION")

    return reasons


def _validate_independence(package: dict) -> list[str]:
    reasons: list[str] = []
    attestation = package.get("independence_attestation")
    if not isinstance(attestation, dict):
        return ["INDEPENDENCE_ATTESTATION_NOT_MAPPING"]

    for field in INDEPENDENCE_FIELDS:
        if str(attestation.get(field, "UNKNOWN")).upper() != "YES":
            reasons.append(f"{field.upper()}_NOT_ESTABLISHED")
    if str(attestation.get("source_conclusion_withheld", "UNKNOWN")).upper() != "YES":
        reasons.append("SOURCE_CONCLUSION_NOT_WITHHELD")
    if str(attestation.get("leakage_detected", "UNKNOWN")).upper() != "NO":
        reasons.append("LEAKAGE_NOT_CLEARED")
    if attestation.get("run_id") != package.get("run_id"):
        reasons.append("ATTESTATION_RUN_ID_MISMATCH")
    if attestation.get("execution_context_id") != package.get("execution_context_id"):
        reasons.append("ATTESTATION_CONTEXT_ID_MISMATCH")
    if attestation.get("baseline_sha") != package.get("repository_baseline_sha"):
        reasons.append("ATTESTATION_BASELINE_MISMATCH")
    return reasons


def validate_package(package: object) -> dict:
    """Validate a package without claiming external execution authenticity."""
    if not isinstance(package, dict):
        return {
            "state": "INVALID",
            "structural_validity": "FAIL",
            "internal_integrity": "FAIL",
            "external_authenticity": "UNVERIFIED",
            "reasons": ["PACKAGE_NOT_MAPPING"],
            "authority": "NONE",
        }

    reasons: list[str] = []
    missing = _missing_keys(package, REQUIRED_TOP_LEVEL)
    reasons.extend(f"MISSING_{key.upper()}" for key in missing)

    if package.get("schema_version") != SCHEMA_VERSION:
        reasons.append("SCHEMA_VERSION_MISMATCH")
    if package.get("participant_kind") != "MODEL_RUN":
        reasons.append("PARTICIPANT_KIND_NOT_MODEL_RUN")
    if package.get("condition") not in CONDITIONS:
        reasons.append("UNSUPPORTED_CONDITION")
    if not package.get("participant_evidence_ref"):
        reasons.append("PARTICIPANT_EVIDENCE_REF_MISSING")
    if not package.get("independence_attestation_ref"):
        reasons.append("INDEPENDENCE_ATTESTATION_REF_MISSING")

    response = package.get("participant_response")
    if not isinstance(response, dict):
        reasons.append("PARTICIPANT_RESPONSE_NOT_MAPPING")
    else:
        for field in REQUIRED_RESPONSE_FIELDS:
            if field not in response:
                reasons.append(f"RESPONSE_MISSING_{field.upper()}")

    contamination = _walk_forbidden_keys(package.get("participant_payload"))
    contamination.extend(_walk_forbidden_keys(package.get("participant_response")))
    reasons.extend(f"EVALUATOR_CONTAMINATION:{path}" for path in sorted(set(contamination)))

    reasons.extend(_validate_condition_payload(package))
    reasons.extend(_validate_independence(package))

    payload_digest = package.get("payload_digest")
    response_digest = package.get("response_digest")
    recorded_package_digest = package.get("package_digest")
    if not isinstance(payload_digest, str) or not SHA256_RE.match(payload_digest):
        reasons.append("PAYLOAD_DIGEST_FORMAT_INVALID")
    elif payload_digest != digest_value(package.get("participant_payload")):
        reasons.append("PAYLOAD_DIGEST_MISMATCH")
    if not isinstance(response_digest, str) or not SHA256_RE.match(response_digest):
        reasons.append("RESPONSE_DIGEST_FORMAT_INVALID")
    elif response_digest != digest_value(package.get("participant_response")):
        reasons.append("RESPONSE_DIGEST_MISMATCH")
    if not isinstance(recorded_package_digest, str) or not SHA256_RE.match(recorded_package_digest):
        reasons.append("PACKAGE_DIGEST_FORMAT_INVALID")
    elif recorded_package_digest != package_digest(package):
        reasons.append("PACKAGE_DIGEST_MISMATCH")

    invalid_markers = (
        "MISSING_",
        "SCHEMA_VERSION_MISMATCH",
        "PARTICIPANT_KIND_NOT_MODEL_RUN",
        "UNSUPPORTED_CONDITION",
        "NOT_MAPPING",
        "MISMATCH",
        "FORMAT_INVALID",
        "_LEAK",
        "EVALUATOR_CONTAMINATION",
    )
    invalid = (
        any(reason in CONDITION_STRUCTURAL_INVALID_REASONS for reason in reasons)
        or any(any(marker in reason for marker in invalid_markers) for reason in reasons)
    )
    if invalid:
        state = "INVALID"
    elif reasons:
        state = "QUARANTINED"
    else:
        state = "STRUCTURALLY_QUALIFIED"

    return {
        "state": state,
        "structural_validity": "PASS" if state != "INVALID" else "FAIL",
        "internal_integrity": "PASS" if not any("DIGEST" in reason for reason in reasons) else "FAIL",
        "external_authenticity": "UNVERIFIED",
        "eligible_for_external_resolution": state == "STRUCTURALLY_QUALIFIED",
        "reasons": reasons,
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }


def detect_duplicate_identity(packages: Iterable[dict]) -> dict:
    """Detect package/run identity reuse without treating duplicates as corroboration."""
    package_ids: dict[str, int] = {}
    run_keys: dict[tuple[str, str, str, str], int] = {}
    for package in packages:
        package_id = str(package.get("package_id", ""))
        if package_id:
            package_ids[package_id] = package_ids.get(package_id, 0) + 1
        key = (
            str(package.get("run_id", "")),
            str(package.get("case_id", "")),
            str(package.get("condition", "")),
            str(package.get("execution_context_id", "")),
        )
        run_keys[key] = run_keys.get(key, 0) + 1

    duplicate_package_ids = sorted(key for key, count in package_ids.items() if count > 1)
    duplicate_run_keys = sorted(key for key, count in run_keys.items() if count > 1)
    return {
        "state": "DUPLICATE_IDENTITY_DETECTED" if duplicate_package_ids or duplicate_run_keys else "UNIQUE",
        "duplicate_package_ids": duplicate_package_ids,
        "duplicate_run_keys": duplicate_run_keys,
        "independent_confirmation": "NOT_ESTABLISHED_BY_MULTIPLICITY",
    }
