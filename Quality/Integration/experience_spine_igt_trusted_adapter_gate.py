"""Governed execution boundary for external evidence resolver adapters.

This layer invokes an approved adapter itself and then delegates semantic
comparison to the existing pure correlation gate. Registry membership and
protocol conformance do not establish upstream provider authenticity.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Mapping

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import (
    EvidenceResolverAdapter,
    EvidenceResolverAdapterError,
    ResolverAcquisition,
    ResolverAdapterIdentity,
)
from experience_spine_igt_external_resolver import (
    correlate_external_evidence,
    observation_digest,
)


RESERVED_OBSERVATION_KEYS = {"resolver_id", "resolution_id", "requested_ref"}


@dataclass(frozen=True)
class ApprovedResolverAdapter:
    adapter_id: str
    adapter_kind: str
    implementation_id: str


def _identity_snapshot(adapter: EvidenceResolverAdapter) -> ResolverAdapterIdentity:
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
) -> dict:
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
            "OBSERVATION_RESERVED_IDENTITY_INJECTION:" + ",".join(sorted(injected))
        )

    observation = dict(acquisition.observation)
    observation["resolver_id"] = identity.adapter_id
    observation["resolution_id"] = acquisition.acquisition_id
    observation["requested_ref"] = acquisition.requested_ref
    return observation


def _receipt(identity: ResolverAdapterIdentity, acquisition: ResolverAcquisition, observation: dict) -> dict:
    return {
        "resolver_id": identity.adapter_id,
        "resolution_id": acquisition.acquisition_id,
        "source_ref": observation.get("observed_ref"),
        "observation_digest": observation_digest(observation),
    }


def execute_registered_adapter_correlation(
    package: dict,
    *,
    adapter: EvidenceResolverAdapter,
    approved_registry: Mapping[str, ApprovedResolverAdapter],
) -> dict:
    """Invoke one registered adapter path without laundering it into authenticity."""
    try:
        identity_before = _identity_snapshot(adapter)
    except Exception as exc:  # adapter boundary must fail closed
        return {
            "state": "ADAPTER_IDENTITY_REJECTED",
            "reason": str(exc),
            "external_authenticity": "INCONCLUSIVE",
            "provider_backed_authenticity": "NOT_ESTABLISHED",
            "authority": "NONE",
        }

    approved, reason = _approved_identity(identity_before, approved_registry)
    if not approved:
        return {
            "state": "ADAPTER_NOT_APPROVED",
            "reason": reason,
            "adapter_identity": identity_before,
            "external_authenticity": "INCONCLUSIVE",
            "provider_backed_authenticity": "NOT_ESTABLISHED",
            "authority": "NONE",
        }

    participant_ref = package.get("participant_evidence_ref") if isinstance(package, dict) else None
    attestation_ref = package.get("independence_attestation_ref") if isinstance(package, dict) else None
    if not participant_ref or not attestation_ref:
        return {
            "state": "PACKAGE_REFERENCE_PRECONDITION_FAILED",
            "adapter_identity": identity_before,
            "external_authenticity": "INCONCLUSIVE",
            "provider_backed_authenticity": "NOT_ESTABLISHED",
            "authority": "NONE",
        }

    try:
        participant_acquisition = adapter.acquire_participant(str(participant_ref))
        identity_mid = _identity_snapshot(adapter)
        if identity_mid != identity_before:
            raise EvidenceResolverAdapterError("ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION")
        attestation_acquisition = adapter.acquire_attestation(str(attestation_ref))
        identity_after = _identity_snapshot(adapter)
        if identity_after != identity_before:
            raise EvidenceResolverAdapterError("ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION")

        participant_observation = _normalize_acquisition(
            participant_acquisition,
            identity=identity_before,
            expected_ref=str(participant_ref),
        )
        attestation_observation = _normalize_acquisition(
            attestation_acquisition,
            identity=identity_before,
            expected_ref=str(attestation_ref),
        )
        if participant_acquisition.acquisition_id == attestation_acquisition.acquisition_id:
            raise EvidenceResolverAdapterError("ACQUISITION_CHANNEL_ID_COLLISION")
    except Exception as exc:  # explicit fail-closed acquisition boundary
        return {
            "state": "ADAPTER_EXECUTION_FAILED",
            "reason": str(exc),
            "adapter_identity": identity_before,
            "external_authenticity": "INCONCLUSIVE",
            "provider_backed_authenticity": "NOT_ESTABLISHED",
            "authority": "NONE",
        }

    correlation = correlate_external_evidence(
        package,
        participant_observation=participant_observation,
        attestation_observation=attestation_observation,
        participant_receipt=_receipt(identity_before, participant_acquisition, participant_observation),
        attestation_receipt=_receipt(identity_before, attestation_acquisition, attestation_observation),
    )

    if correlation["state"] == "CORRELATED_AWAITING_TRUSTED_ADAPTER":
        state = "APPROVED_ADAPTER_PATH_CORRELATED"
    elif correlation["state"] == "EXTERNAL_EVIDENCE_MISMATCH":
        state = "APPROVED_ADAPTER_PATH_MISMATCH"
    else:
        state = "APPROVED_ADAPTER_PATH_INCONCLUSIVE"

    return {
        "state": state,
        "adapter_identity": identity_before,
        "participant_acquisition_id": participant_acquisition.acquisition_id,
        "attestation_acquisition_id": attestation_acquisition.acquisition_id,
        "correlation": correlation,
        "registry_path": "APPROVED_IDENTITY_MATCH",
        "adapter_execution": "OBSERVED_BY_GOVERNED_GATE",
        "external_authenticity": "INCONCLUSIVE",
        "provider_backed_authenticity": "NOT_ESTABLISHED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }
