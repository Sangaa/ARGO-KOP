"""Correlation gate for external Experience Spine IGT evidence.

Pure correlation can establish whether independently retrieved observations match
a structurally qualified package. It cannot establish that an observation was
actually retrieved by a trusted external adapter. Therefore this module never
returns EXTERNAL_AUTHENTICITY_VERIFIED.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Iterable

from experience_spine_igt_evidence_package import digest_value, validate_package


FOUND = "FOUND"
UNAVAILABLE = "UNAVAILABLE"
PARTIAL = "PARTIAL"
OBSERVATION_STATES = {FOUND, UNAVAILABLE, PARTIAL}

PARTICIPANT_BINDINGS = (
    ("run_id", "run_id"),
    ("case_id", "case_id"),
    ("condition", "condition"),
    ("execution_context_id", "execution_context_id"),
    ("repository_baseline_sha", "repository_baseline_sha"),
    ("source_model", "source_model"),
    ("source_instance_id", "source_instance_id"),
    ("payload_digest", "payload_digest"),
    ("response_digest", "response_digest"),
)
ATTESTATION_BINDINGS = (
    ("run_id", "run_id"),
    ("execution_context_id", "execution_context_id"),
    ("repository_baseline_sha", "repository_baseline_sha"),
)


def observation_digest(observation: dict) -> str:
    """Digest one resolver observation for receipt binding."""
    if not isinstance(observation, dict):
        raise TypeError("OBSERVATION_NOT_MAPPING")
    return digest_value(observation)


def _base_observation_checks(package: dict, observation: object, expected_ref_field: str) -> tuple[str, list[str]]:
    if not isinstance(observation, dict):
        return "MISMATCH", ["OBSERVATION_NOT_MAPPING"]

    status = str(observation.get("status", ""))
    if status not in OBSERVATION_STATES:
        return "MISMATCH", ["OBSERVATION_STATUS_INVALID"]

    expected_ref = package.get(expected_ref_field)
    requested_ref = observation.get("requested_ref")
    if requested_ref != expected_ref:
        return "MISMATCH", ["REQUESTED_REF_MISMATCH"]

    if status == UNAVAILABLE:
        return "UNAVAILABLE", []
    if status == PARTIAL:
        return "INCONCLUSIVE", []

    reasons: list[str] = []
    if observation.get("observed_ref") != expected_ref:
        reasons.append("OBSERVED_REF_MISMATCH")
    if not observation.get("resolution_id"):
        reasons.append("RESOLUTION_ID_MISSING")
    if not observation.get("resolver_id"):
        reasons.append("RESOLVER_ID_MISSING")
    return ("MISMATCH" if reasons else "CORRELATED"), reasons


def correlate_participant_observation(package: dict, observation: object) -> dict:
    """Bind external execution observation to participant package identity/content."""
    base_state, reasons = _base_observation_checks(package, observation, "participant_evidence_ref")
    if base_state != "CORRELATED":
        return {"state": base_state, "reasons": reasons, "kind": "PARTICIPANT"}

    assert isinstance(observation, dict)
    for observed_field, package_field in PARTICIPANT_BINDINGS:
        if observation.get(observed_field) != package.get(package_field):
            reasons.append(f"{observed_field.upper()}_MISMATCH")

    state = "MISMATCH" if reasons else "CORRELATED"
    return {
        "state": state,
        "reasons": reasons,
        "kind": "PARTICIPANT",
        "resolver_id": observation.get("resolver_id"),
        "resolution_id": observation.get("resolution_id"),
        "observation_digest": observation_digest(observation),
    }


def correlate_attestation_observation(package: dict, observation: object) -> dict:
    """Bind external attestation observation to embedded package attestation."""
    base_state, reasons = _base_observation_checks(package, observation, "independence_attestation_ref")
    if base_state != "CORRELATED":
        return {"state": base_state, "reasons": reasons, "kind": "ATTESTATION"}

    assert isinstance(observation, dict)
    embedded = package.get("independence_attestation", {})
    for observed_field, package_field in ATTESTATION_BINDINGS:
        if observation.get(observed_field) != package.get(package_field):
            reasons.append(f"{observed_field.upper()}_MISMATCH")

    expected_attestation_digest = digest_value(embedded)
    if observation.get("attestation_digest") != expected_attestation_digest:
        reasons.append("ATTESTATION_DIGEST_MISMATCH")

    observed_dimensions = observation.get("independence_dimensions")
    if not isinstance(observed_dimensions, dict):
        reasons.append("INDEPENDENCE_DIMENSIONS_MISSING")
    elif observed_dimensions != embedded:
        reasons.append("INDEPENDENCE_DIMENSIONS_MISMATCH")

    state = "MISMATCH" if reasons else "CORRELATED"
    return {
        "state": state,
        "reasons": reasons,
        "kind": "ATTESTATION",
        "resolver_id": observation.get("resolver_id"),
        "resolution_id": observation.get("resolution_id"),
        "observation_digest": observation_digest(observation),
    }


def bind_resolver_receipt(observation: object, receipt: object) -> dict:
    """Check receipt-to-observation binding without authenticating the resolver itself."""
    if not isinstance(observation, dict) or not isinstance(receipt, dict):
        return {
            "state": "RECEIPT_MISMATCH",
            "reasons": ["RECEIPT_OR_OBSERVATION_NOT_MAPPING"],
            "resolver_trust": "UNAUTHENTICATED_BY_PURE_CORRELATION",
        }

    reasons: list[str] = []
    if receipt.get("resolver_id") != observation.get("resolver_id"):
        reasons.append("RECEIPT_RESOLVER_ID_MISMATCH")
    if receipt.get("resolution_id") != observation.get("resolution_id"):
        reasons.append("RECEIPT_RESOLUTION_ID_MISMATCH")
    if receipt.get("source_ref") != observation.get("observed_ref"):
        reasons.append("RECEIPT_SOURCE_REF_MISMATCH")
    if receipt.get("observation_digest") != observation_digest(observation):
        reasons.append("RECEIPT_OBSERVATION_DIGEST_MISMATCH")

    return {
        "state": "RECEIPT_BOUND" if not reasons else "RECEIPT_MISMATCH",
        "reasons": reasons,
        "resolver_id": observation.get("resolver_id"),
        "resolution_id": observation.get("resolution_id"),
        "resolver_trust": "UNAUTHENTICATED_BY_PURE_CORRELATION",
    }


def correlate_external_evidence(
    package: object,
    *,
    participant_observation: object,
    attestation_observation: object,
    participant_receipt: object | None = None,
    attestation_receipt: object | None = None,
) -> dict:
    """Correlate external evidence without laundering trust into authenticity."""
    local = validate_package(package)
    if local.get("state") != "STRUCTURALLY_QUALIFIED":
        return {
            "state": "PACKAGE_NOT_ELIGIBLE",
            "package_state": local.get("state"),
            "participant": None,
            "attestation": None,
            "external_authenticity": "INCONCLUSIVE",
            "production_trusted_adapter": "NOT_ESTABLISHED",
            "authority": "NONE",
            "cognitive_effect": "NOT_ESTABLISHED",
        }

    assert isinstance(package, dict)
    participant = correlate_participant_observation(package, participant_observation)
    attestation = correlate_attestation_observation(package, attestation_observation)

    participant_receipt_result = (
        bind_resolver_receipt(participant_observation, participant_receipt)
        if participant_receipt is not None
        else {"state": "RECEIPT_UNSEEN", "resolver_trust": "UNAUTHENTICATED_BY_PURE_CORRELATION"}
    )
    attestation_receipt_result = (
        bind_resolver_receipt(attestation_observation, attestation_receipt)
        if attestation_receipt is not None
        else {"state": "RECEIPT_UNSEEN", "resolver_trust": "UNAUTHENTICATED_BY_PURE_CORRELATION"}
    )

    states = {participant["state"], attestation["state"]}
    if "MISMATCH" in states:
        state = "EXTERNAL_EVIDENCE_MISMATCH"
        authenticity = "MISMATCH"
    elif states == {"CORRELATED"}:
        receipts_bound = (
            participant_receipt_result["state"] == "RECEIPT_BOUND"
            and attestation_receipt_result["state"] == "RECEIPT_BOUND"
        )
        state = "CORRELATED_AWAITING_TRUSTED_ADAPTER" if receipts_bound else "CORRELATED_UNTRUSTED"
        authenticity = "INCONCLUSIVE"
    elif "UNAVAILABLE" in states:
        state = "EXTERNAL_EVIDENCE_UNAVAILABLE"
        authenticity = "INCONCLUSIVE"
    else:
        state = "EXTERNAL_EVIDENCE_INCONCLUSIVE"
        authenticity = "INCONCLUSIVE"

    return {
        "state": state,
        "package_state": local["state"],
        "participant": participant,
        "attestation": attestation,
        "participant_receipt": participant_receipt_result,
        "attestation_receipt": attestation_receipt_result,
        "external_authenticity": authenticity,
        "production_trusted_adapter": "NOT_ESTABLISHED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }


def detect_duplicate_resolution_identity(observations: Iterable[dict]) -> dict:
    """Prevent repeated resolver records from masquerading as corroboration."""
    resolution_ids: dict[tuple[str, str], int] = {}
    observation_digests: dict[str, int] = {}
    for observation in observations:
        key = (str(observation.get("resolver_id", "")), str(observation.get("resolution_id", "")))
        resolution_ids[key] = resolution_ids.get(key, 0) + 1
        digest = observation_digest(observation)
        observation_digests[digest] = observation_digests.get(digest, 0) + 1

    duplicate_resolution_ids = sorted(key for key, count in resolution_ids.items() if count > 1)
    duplicate_observation_digests = sorted(key for key, count in observation_digests.items() if count > 1)
    return {
        "state": "DUPLICATE_RESOLUTION_EVIDENCE" if duplicate_resolution_ids or duplicate_observation_digests else "UNIQUE",
        "duplicate_resolution_ids": duplicate_resolution_ids,
        "duplicate_observation_digests": duplicate_observation_digests,
        "independent_corroboration": "NOT_ESTABLISHED_BY_DUPLICATION",
    }
