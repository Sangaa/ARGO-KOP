"""Binding-aware admission gate for Experience Spine IGT evidence packages.

This module correlates an already-verified sealed participant export and local
response binding with an independently supplied model-run evidence package. It
does not authenticate external execution, provider identity, or independence.
"""
from __future__ import annotations

from typing import Any

from experience_spine_igt_evidence_package import digest_value, validate_package
from experience_spine_igt_participant_export import verify_participant_export
from experience_spine_igt_response_binding import verify_response_binding


ADMISSION_STATE = "BINDING_CORRELATED_EVIDENCE_ADMISSION"
CLAIM_BOUNDARY = "LOCAL_CROSS_ARTIFACT_CORRELATION_ONLY"


def _mismatch(reasons: list[str], condition: bool, code: str) -> None:
    if condition:
        reasons.append(code)


def verify_binding_aware_evidence_admission(
    *,
    participant_export: object,
    response_binding: object,
    evidence_package: object,
) -> dict:
    """Verify exact semantic correlation across export, binding and package."""
    reasons: list[str] = []

    if not isinstance(participant_export, dict):
        export_result = {"state": "INVALID"}
        reasons.append("PARTICIPANT_EXPORT_NOT_MAPPING")
    else:
        export_result = verify_participant_export(participant_export)
        if export_result.get("state") != "VERIFIED_PARTICIPANT_EXPORT":
            reasons.append("PARTICIPANT_EXPORT_INVALID")

    if not isinstance(response_binding, dict):
        binding_result = {"state": "INVALID"}
        reasons.append("RESPONSE_BINDING_NOT_MAPPING")
    elif not isinstance(participant_export, dict):
        binding_result = {"state": "INVALID"}
        reasons.append("RESPONSE_BINDING_UNVERIFIABLE_WITHOUT_EXPORT")
    else:
        binding_result = verify_response_binding(
            binding=response_binding,
            participant_export=participant_export,
        )
        if binding_result.get("state") != "VERIFIED_LOCAL_BINDING":
            reasons.append("RESPONSE_BINDING_INVALID")

    if not isinstance(evidence_package, dict):
        package_result = {"state": "INVALID"}
        reasons.append("EVIDENCE_PACKAGE_NOT_MAPPING")
    else:
        package_result = validate_package(evidence_package)
        if package_result.get("state") != "STRUCTURALLY_QUALIFIED":
            reasons.append("EVIDENCE_PACKAGE_NOT_STRUCTURALLY_QUALIFIED")

    prerequisites_pass = (
        export_result.get("state") == "VERIFIED_PARTICIPANT_EXPORT"
        and binding_result.get("state") == "VERIFIED_LOCAL_BINDING"
        and package_result.get("state") == "STRUCTURALLY_QUALIFIED"
        and isinstance(participant_export, dict)
        and isinstance(response_binding, dict)
        and isinstance(evidence_package, dict)
    )

    if prerequisites_pass:
        _mismatch(
            reasons,
            evidence_package.get("participant_payload") != participant_export.get("participant_payload"),
            "PACKAGE_PAYLOAD_EXPORT_MISMATCH",
        )
        _mismatch(
            reasons,
            evidence_package.get("participant_response") != response_binding.get("participant_response"),
            "PACKAGE_RESPONSE_BINDING_MISMATCH",
        )
        _mismatch(
            reasons,
            evidence_package.get("case_id") != participant_export.get("case_id"),
            "PACKAGE_CASE_EXPORT_MISMATCH",
        )
        _mismatch(
            reasons,
            evidence_package.get("condition") != participant_export.get("condition"),
            "PACKAGE_CONDITION_EXPORT_MISMATCH",
        )
        _mismatch(
            reasons,
            evidence_package.get("repository_baseline_sha") != participant_export.get("baseline_sha"),
            "PACKAGE_BASELINE_EXPORT_MISMATCH",
        )
        _mismatch(
            reasons,
            response_binding.get("export_id") != participant_export.get("export_id"),
            "BINDING_EXPORT_ID_MISMATCH",
        )
        _mismatch(
            reasons,
            response_binding.get("export_package_digest") != participant_export.get("package_digest"),
            "BINDING_EXPORT_DIGEST_MISMATCH",
        )
        _mismatch(
            reasons,
            response_binding.get("response_digest") != digest_value(evidence_package.get("participant_response")),
            "PACKAGE_RESPONSE_DIGEST_BINDING_MISMATCH",
        )
        _mismatch(
            reasons,
            evidence_package.get("payload_digest") != digest_value(participant_export.get("participant_payload")),
            "PACKAGE_PAYLOAD_DIGEST_EXPORT_MISMATCH",
        )

    state = ADMISSION_STATE if not reasons else "INVALID"
    return {
        "state": state,
        "reasons": reasons,
        "correlation": "PASS" if not reasons else "FAIL",
        "claim_boundary": CLAIM_BOUNDARY,
        "export_verification": export_result.get("state", "INVALID"),
        "binding_verification": binding_result.get("state", "INVALID"),
        "package_verification": package_result.get("state", "INVALID"),
        "external_delivery": "NOT_PROVEN",
        "model_execution": "NOT_AUTHENTICATED_BY_CORRELATION",
        "provider_authenticity": "UNVERIFIED",
        "independence": "REQUIRES_EXISTING_PACKAGE_ATTESTATION_AND_EXTERNAL_RESOLUTION",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }
