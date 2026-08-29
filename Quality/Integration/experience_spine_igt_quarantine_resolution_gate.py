"""Governed resolution gate for untrusted external-evidence quarantine.

This layer performs one narrow transition:

    UNTRUSTED_QUARANTINED -> RESOLVED_UNAUTHENTICATED

only when the gate itself invokes an explicitly approved generic resolver and
re-acquires the exact source reference with content identical to the sealed
quarantine artifact. Technical re-acquisition does not authenticate a provider,
prove external delivery/model execution, establish independence, grant
authority, or establish cognitive effect.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime
from typing import Any, Mapping

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import (
    EvidenceResolverAdapterError,
    QuarantineEvidenceResolverAdapter,
    ResolverAcquisition,
    ResolverAdapterIdentity,
)
from experience_spine_igt_external_evidence_intake import verify_external_evidence_intake
from experience_spine_igt_trusted_adapter_gate import ApprovedResolverAdapter


SUCCESS_STATE = "RESOLVED_UNAUTHENTICATED"
QUARANTINE_STATE = "UNTRUSTED_QUARANTINED"
ALLOWED_RESOLUTION_STATUSES = {"FOUND", "UNAVAILABLE", "PARTIAL"}
RESERVED_OBSERVATION_KEYS = {
    "resolver_id",
    "resolution_id",
    "requested_ref",
    "trust_state",
    "external_authenticity",
    "provider_authenticity",
    "external_delivery",
    "model_execution",
    "model_execution_authenticity",
    "independence",
    "authority",
    "cognitive_effect",
}


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _identity_snapshot(adapter: QuarantineEvidenceResolverAdapter) -> ResolverAdapterIdentity:
    identity = adapter.identity
    if not isinstance(identity, ResolverAdapterIdentity):
        raise EvidenceResolverAdapterError("ADAPTER_IDENTITY_NOT_CANONICAL")
    if not identity.adapter_id or not identity.adapter_kind or not identity.implementation_id:
        raise EvidenceResolverAdapterError("ADAPTER_IDENTITY_INCOMPLETE")
    return identity


def _approved_identity(
    identity: ResolverAdapterIdentity,
    registry: Mapping[str, ApprovedResolverAdapter],
) -> tuple[bool, str | None]:
    approved = registry.get(identity.adapter_id)
    if approved is None:
        return False, "ADAPTER_NOT_REGISTERED"
    if not isinstance(approved, ApprovedResolverAdapter):
        return False, "REGISTRY_RECORD_NOT_CANONICAL"
    if approved.adapter_kind != identity.adapter_kind:
        return False, "ADAPTER_KIND_MISMATCH"
    if approved.implementation_id != identity.implementation_id:
        return False, "ADAPTER_IMPLEMENTATION_MISMATCH"
    return True, None


def _parse_timestamp(value: str, field: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise EvidenceResolverAdapterError(f"{field}_MISSING")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceResolverAdapterError(f"{field}_INVALID") from exc


def _normalize_acquisition(
    acquisition: ResolverAcquisition,
    *,
    identity: ResolverAdapterIdentity,
    expected_ref: str,
) -> dict[str, Any]:
    if not isinstance(acquisition, ResolverAcquisition):
        raise EvidenceResolverAdapterError("ACQUISITION_NOT_CANONICAL")
    if acquisition.adapter_id != identity.adapter_id:
        raise EvidenceResolverAdapterError("ACQUISITION_ADAPTER_ID_MISMATCH")
    if acquisition.adapter_kind != identity.adapter_kind:
        raise EvidenceResolverAdapterError("ACQUISITION_ADAPTER_KIND_MISMATCH")
    if not acquisition.acquisition_id:
        raise EvidenceResolverAdapterError("ACQUISITION_ID_MISSING")
    if not acquisition.acquisition_surface:
        raise EvidenceResolverAdapterError("ACQUISITION_SURFACE_MISSING")
    if acquisition.requested_ref != expected_ref:
        raise EvidenceResolverAdapterError("ACQUISITION_REQUESTED_REF_MISMATCH")

    started = _parse_timestamp(acquisition.started_at, "ACQUISITION_STARTED_AT")
    completed = _parse_timestamp(acquisition.completed_at, "ACQUISITION_COMPLETED_AT")
    if completed < started:
        raise EvidenceResolverAdapterError("ACQUISITION_TIME_ORDER_INVALID")

    if not isinstance(acquisition.observation, dict):
        raise EvidenceResolverAdapterError("ACQUISITION_OBSERVATION_NOT_MAPPING")
    injected = RESERVED_OBSERVATION_KEYS.intersection(acquisition.observation)
    if injected:
        raise EvidenceResolverAdapterError(
            "OBSERVATION_RESERVED_CONTROL_INJECTION:" + ",".join(sorted(injected))
        )

    observation = dict(acquisition.observation)
    status = observation.get("status")
    if status not in ALLOWED_RESOLUTION_STATUSES:
        raise EvidenceResolverAdapterError("RESOLUTION_STATUS_INVALID")

    observation["resolver_id"] = identity.adapter_id
    observation["resolution_id"] = acquisition.acquisition_id
    observation["requested_ref"] = acquisition.requested_ref
    observation["acquisition_surface"] = acquisition.acquisition_surface
    observation["acquisition_started_at"] = acquisition.started_at
    observation["acquisition_completed_at"] = acquisition.completed_at
    return observation


def _boundary(*, state: str, trust_state: str, **extra: Any) -> dict[str, Any]:
    result = {
        "state": state,
        "trust_state": trust_state,
        "provider_authenticity": "UNVERIFIED",
        "external_authenticity": "NOT_ESTABLISHED_BY_RESOLUTION",
        "external_delivery": "NOT_PROVEN",
        "model_execution_authenticity": "NOT_PROVEN",
        "independence": "UNVERIFIED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
        "next_required_stage": "PROVIDER_BACKED_AUTHENTICATION_OR_OTHER_GOVERNED_AUTHENTICITY_EVIDENCE",
    }
    result.update(extra)
    return result


def execute_quarantine_resolution(
    intake_envelope: object,
    *,
    adapter: QuarantineEvidenceResolverAdapter,
    approved_registry: Mapping[str, ApprovedResolverAdapter],
) -> dict[str, Any]:
    """Invoke one approved resolver and bind exact re-acquisition to quarantine.

    The input quarantine envelope is never mutated. A successful result proves
    that the approved technical acquisition path returned the same JSON value
    at the same source reference. It deliberately stops before authenticity.
    """
    try:
        intake_result = verify_external_evidence_intake(intake_envelope)
    except Exception as exc:
        return _boundary(
            state="INTAKE_NOT_ELIGIBLE",
            trust_state=QUARANTINE_STATE,
            reason=f"INTAKE_VERIFICATION_FAILED:{exc}",
            adapter_execution="NOT_INVOKED",
        )

    if intake_result.get("state") != "VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE":
        return _boundary(
            state="INTAKE_NOT_ELIGIBLE",
            trust_state=QUARANTINE_STATE,
            intake_verification=intake_result,
            adapter_execution="NOT_INVOKED",
        )
    if not isinstance(intake_envelope, dict):
        return _boundary(
            state="INTAKE_NOT_ELIGIBLE",
            trust_state=QUARANTINE_STATE,
            reason="INTAKE_NOT_MAPPING",
            adapter_execution="NOT_INVOKED",
        )

    try:
        identity_before = _identity_snapshot(adapter)
    except Exception as exc:
        return _boundary(
            state="ADAPTER_IDENTITY_REJECTED",
            trust_state=QUARANTINE_STATE,
            reason=str(exc),
            adapter_execution="NOT_INVOKED",
            intake_id=intake_envelope.get("intake_id"),
        )

    approved, reason = _approved_identity(identity_before, approved_registry)
    if not approved:
        return _boundary(
            state="ADAPTER_NOT_APPROVED",
            trust_state=QUARANTINE_STATE,
            reason=reason,
            adapter_identity=identity_before,
            adapter_execution="NOT_INVOKED",
            intake_id=intake_envelope.get("intake_id"),
        )

    source_ref = str(intake_envelope["source_ref"])
    try:
        acquisition = adapter.acquire_external(source_ref)
        identity_after = _identity_snapshot(adapter)
        if identity_after != identity_before:
            raise EvidenceResolverAdapterError("ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION")
        observation = _normalize_acquisition(
            acquisition,
            identity=identity_before,
            expected_ref=source_ref,
        )
    except Exception as exc:
        return _boundary(
            state="RESOLUTION_EXECUTION_FAILED",
            trust_state=QUARANTINE_STATE,
            reason=str(exc),
            adapter_identity=identity_before,
            adapter_execution="FAILED",
            intake_id=intake_envelope.get("intake_id"),
        )

    common = {
        "intake_id": intake_envelope["intake_id"],
        "source_ref": source_ref,
        "adapter_identity": identity_before,
        "acquisition_id": acquisition.acquisition_id,
        "acquisition_surface": acquisition.acquisition_surface,
        "adapter_execution": "OBSERVED_BY_GOVERNED_GATE",
        "registry_path": "APPROVED_IDENTITY_MATCH",
        "resolution_observation": observation,
    }

    status = observation["status"]
    if status == "UNAVAILABLE":
        if observation.get("observed_ref") is not None or "evidence_content" in observation:
            return _boundary(
                state="RESOLUTION_MISMATCH",
                trust_state=QUARANTINE_STATE,
                reasons=["UNAVAILABLE_OBSERVATION_CONTRADICTS_CONTENT"],
                technical_resolution="MISMATCH",
                **common,
            )
        return _boundary(
            state="RESOLUTION_UNAVAILABLE",
            trust_state=QUARANTINE_STATE,
            technical_resolution="UNAVAILABLE_BY_THIS_APPROVED_ADAPTER_PATH",
            **common,
        )

    if status == "PARTIAL":
        return _boundary(
            state="RESOLUTION_INCONCLUSIVE",
            trust_state=QUARANTINE_STATE,
            technical_resolution="PARTIAL",
            **common,
        )

    reasons: list[str] = []
    if observation.get("observed_ref") != source_ref:
        reasons.append("OBSERVED_REF_MISMATCH")
    if "evidence_content" not in observation:
        reasons.append("EVIDENCE_CONTENT_MISSING")
        acquired_digest = None
    else:
        acquired_digest = _digest(observation["evidence_content"])
        if acquired_digest != intake_envelope.get("raw_evidence_digest"):
            reasons.append("RAW_EVIDENCE_DIGEST_MISMATCH")
        if observation["evidence_content"] != intake_envelope.get("raw_evidence"):
            reasons.append("RAW_EVIDENCE_CONTENT_MISMATCH")

    if reasons:
        return _boundary(
            state="RESOLUTION_MISMATCH",
            trust_state=QUARANTINE_STATE,
            reasons=sorted(set(reasons)),
            acquired_evidence_digest=acquired_digest,
            sealed_evidence_digest=intake_envelope.get("raw_evidence_digest"),
            technical_resolution="MISMATCH",
            **common,
        )

    return _boundary(
        state=SUCCESS_STATE,
        trust_state=SUCCESS_STATE,
        acquired_evidence_digest=acquired_digest,
        sealed_evidence_digest=intake_envelope["raw_evidence_digest"],
        technical_resolution="EXACT_CONTENT_REACQUIRED_FROM_EXACT_REF",
        **common,
    )
