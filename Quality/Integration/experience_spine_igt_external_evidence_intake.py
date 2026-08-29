"""Fail-closed first-entry boundary for externally supplied IGT evidence.

This module preserves and seals external evidence without authenticating it.
It does not perform transport, provider verification, resolver acquisition,
correlation, attestation validation, authority promotion, or cognitive scoring.
"""
from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from typing import Any

FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
INTAKE_VERSION = "IGT-EXTERNAL-EVIDENCE-INTAKE-1"
TRUST_STATE = "UNTRUSTED_QUARANTINED"
ALLOWED_ARTIFACT_TYPES = {
    "DELIVERY_RECEIPT",
    "MODEL_EXECUTION_RECEIPT",
    "PROVIDER_ATTESTATION",
    "PARTICIPANT_RESPONSE",
    "OTHER_EXTERNAL_EVIDENCE",
}
FORBIDDEN_CLAIM_STATES = {
    "AUTHENTICATED",
    "VERIFIED_PROVIDER",
    "PROVIDER_VERIFIED",
    "EXTERNAL_AUTHENTICITY_VERIFIED",
    "EXECUTION_VERIFIED",
    "DELIVERY_VERIFIED",
    "AUTHORIZED",
    "PROMOTED",
}


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _normalize_nonempty(name: str, value: Any) -> str:
    normalized = str(value).strip()
    if not normalized:
        raise ValueError(f"{name}_REQUIRED")
    return normalized


def _walk_strings(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for item in value.values():
            found.extend(_walk_strings(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_walk_strings(item))
    elif isinstance(value, str):
        found.append(value)
    return found


def _assert_no_prepromoted_claims(claims: dict) -> None:
    values = {item.strip().upper() for item in _walk_strings(claims)}
    blocked = sorted(values.intersection(FORBIDDEN_CLAIM_STATES))
    if blocked:
        raise ValueError("PREPROMOTED_EXTERNAL_CLAIM:" + ",".join(blocked))


def _identity_material(envelope: dict) -> dict:
    return {
        "intake_version": envelope["intake_version"],
        "repository_baseline_sha": envelope["repository_baseline_sha"],
        "source_channel": envelope["source_channel"],
        "source_ref": envelope["source_ref"],
        "artifact_type": envelope["artifact_type"],
        "external_claims": envelope["external_claims"],
        "raw_evidence_digest": envelope["raw_evidence_digest"],
    }


def build_external_evidence_intake(
    *,
    repository_baseline_sha: str,
    source_channel: str,
    source_ref: str,
    artifact_type: str,
    raw_evidence: Any,
    external_claims: dict | None = None,
) -> dict:
    """Seal one externally supplied artifact into an untrusted quarantine envelope."""
    baseline = str(repository_baseline_sha).lower().strip()
    if not FULL_SHA_RE.fullmatch(baseline):
        raise ValueError("FULL_BASELINE_SHA_REQUIRED")

    channel = _normalize_nonempty("SOURCE_CHANNEL", source_channel)
    source = _normalize_nonempty("SOURCE_REF", source_ref)
    kind = _normalize_nonempty("ARTIFACT_TYPE", artifact_type).upper()
    if kind not in ALLOWED_ARTIFACT_TYPES:
        raise ValueError("UNSUPPORTED_ARTIFACT_TYPE")
    if raw_evidence is None:
        raise ValueError("RAW_EVIDENCE_REQUIRED")

    claims = deepcopy(external_claims or {})
    if not isinstance(claims, dict):
        raise ValueError("EXTERNAL_CLAIMS_MUST_BE_MAPPING")
    _assert_no_prepromoted_claims(claims)

    raw_copy = deepcopy(raw_evidence)
    envelope = {
        "intake_version": INTAKE_VERSION,
        "intake_state": "SEALED_QUARANTINE_INTAKE",
        "trust_state": TRUST_STATE,
        "repository_baseline_sha": baseline,
        "source_channel": channel,
        "source_ref": source,
        "artifact_type": kind,
        "external_claims": claims,
        "raw_evidence": raw_copy,
        "raw_evidence_digest": _digest(raw_copy),
        "claim_boundary": {
            "external_delivery": "NOT_PROVEN_BY_INTAKE",
            "model_execution": "NOT_AUTHENTICATED_BY_INTAKE",
            "provider_authenticity": "UNVERIFIED",
            "independence": "UNVERIFIED",
            "authority": "NONE",
            "cognitive_effect": "NOT_ESTABLISHED",
        },
        "next_required_stage": "INDEPENDENT_RESOLUTION_OR_PROVIDER_BACKED_AUTHENTICATION",
    }
    envelope["intake_id"] = "IGT-EXT-" + _digest(_identity_material(envelope))[:24]
    envelope["envelope_digest"] = _digest(envelope)
    return envelope


def verify_external_evidence_intake(envelope: dict) -> dict:
    """Verify local sealing/quarantine semantics only."""
    reasons: list[str] = []
    if not isinstance(envelope, dict):
        return {"state": "INVALID", "reasons": ["ENVELOPE_NOT_MAPPING"]}

    required = {
        "intake_version", "intake_state", "trust_state", "repository_baseline_sha",
        "source_channel", "source_ref", "artifact_type", "external_claims",
        "raw_evidence", "raw_evidence_digest", "claim_boundary", "next_required_stage",
        "intake_id", "envelope_digest",
    }
    missing = sorted(required.difference(envelope))
    if missing:
        reasons.append("MISSING_FIELDS:" + ",".join(missing))

    if envelope.get("intake_version") != INTAKE_VERSION:
        reasons.append("INTAKE_VERSION_INVALID")
    if envelope.get("intake_state") != "SEALED_QUARANTINE_INTAKE":
        reasons.append("INTAKE_STATE_INVALID")
    if envelope.get("trust_state") != TRUST_STATE:
        reasons.append("TRUST_STATE_INVALID")
    if not FULL_SHA_RE.fullmatch(str(envelope.get("repository_baseline_sha", ""))):
        reasons.append("BASELINE_SHA_INVALID")
    if envelope.get("artifact_type") not in ALLOWED_ARTIFACT_TYPES:
        reasons.append("ARTIFACT_TYPE_INVALID")

    claims = envelope.get("external_claims")
    if not isinstance(claims, dict):
        reasons.append("EXTERNAL_CLAIMS_INVALID")
    else:
        try:
            _assert_no_prepromoted_claims(claims)
        except ValueError as exc:
            reasons.append(str(exc))

    if "raw_evidence" in envelope and "raw_evidence_digest" in envelope:
        if envelope.get("raw_evidence_digest") != _digest(envelope.get("raw_evidence")):
            reasons.append("RAW_EVIDENCE_DIGEST_MISMATCH")

    identity_fields = {
        "intake_version", "repository_baseline_sha", "source_channel", "source_ref",
        "artifact_type", "external_claims", "raw_evidence_digest",
    }
    if identity_fields.issubset(envelope):
        expected = "IGT-EXT-" + _digest(_identity_material(envelope))[:24]
        if envelope.get("intake_id") != expected:
            reasons.append("INTAKE_ID_MISMATCH")

    expected_boundary = {
        "external_delivery": "NOT_PROVEN_BY_INTAKE",
        "model_execution": "NOT_AUTHENTICATED_BY_INTAKE",
        "provider_authenticity": "UNVERIFIED",
        "independence": "UNVERIFIED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }
    if envelope.get("claim_boundary") != expected_boundary:
        reasons.append("CLAIM_BOUNDARY_INVALID")
    if envelope.get("next_required_stage") != "INDEPENDENT_RESOLUTION_OR_PROVIDER_BACKED_AUTHENTICATION":
        reasons.append("NEXT_STAGE_INVALID")

    supplied_digest = envelope.get("envelope_digest")
    if supplied_digest:
        body = deepcopy(envelope)
        body.pop("envelope_digest", None)
        if supplied_digest != _digest(body):
            reasons.append("ENVELOPE_DIGEST_MISMATCH")

    return {
        "state": "VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE" if not reasons else "INVALID",
        "reasons": reasons,
        "trust_state": TRUST_STATE if not reasons else "INVALID",
        "external_delivery": "NOT_PROVEN",
        "model_execution_authenticity": "NOT_PROVEN",
        "provider_authenticity": "UNVERIFIED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }
