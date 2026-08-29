"""Fail-closed trust-state transition orchestration for IGT external evidence.

This module does not infer trust from labels. It allows only explicit edges whose
concrete earning stage exists and is invoked by this guard.
"""
from __future__ import annotations

from typing import Any, Mapping

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import QuarantineEvidenceResolverAdapter
from experience_spine_igt_quarantine_resolution_gate import execute_quarantine_resolution
from experience_spine_igt_trusted_adapter_gate import ApprovedResolverAdapter


QUARANTINED = "UNTRUSTED_QUARANTINED"
RESOLVED_UNAUTHENTICATED = "RESOLVED_UNAUTHENTICATED"

KNOWN_STATES = {
    QUARANTINED,
    RESOLVED_UNAUTHENTICATED,
    "PROVIDER_AUTHENTICATED",
    "SOURCE_AUTHENTICATED",
    "EXTERNAL_AUTHENTICITY_VERIFIED",
    "EXECUTION_VERIFIED",
    "DELIVERY_VERIFIED",
    "QUALIFIED",
    "AUTHORIZED",
    "ADMITTED_BOUNDED",
    "PROMOTED",
}

ENABLED_EDGES = {
    (QUARANTINED, RESOLVED_UNAUTHENTICATED): "QUARANTINE_RESOLUTION_GATE",
}


def _result(*, state: str, current_state: str, requested_target: str, effective_state: str, **extra: Any) -> dict[str, Any]:
    result = {
        "state": state,
        "current_state": current_state,
        "requested_target": requested_target,
        "effective_state": effective_state,
        "authority": "NONE",
        "provider_authenticity": "UNVERIFIED",
        "transition_policy": "EXPLICIT_EDGE_ONLY",
    }
    result.update(extra)
    return result


def request_trust_transition(
    *,
    current_state: str,
    target_state: str,
    intake_envelope: object | None = None,
    adapter: QuarantineEvidenceResolverAdapter | None = None,
    approved_registry: Mapping[str, ApprovedResolverAdapter] | None = None,
    caller_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Request one trust transition without allowing caller-declared promotion.

    `caller_claims` are deliberately non-authoritative and never participate in
    transition eligibility. For the only currently enabled upward edge, this
    guard invokes the quarantine-resolution gate itself and accepts advancement
    only when that gate earns its exact success state.
    """
    if not isinstance(current_state, str) or current_state not in KNOWN_STATES:
        return _result(
            state="UNKNOWN_CURRENT_STATE",
            current_state=str(current_state),
            requested_target=str(target_state),
            effective_state=str(current_state),
            stage_invocation="NONE",
        )
    if not isinstance(target_state, str) or target_state not in KNOWN_STATES:
        return _result(
            state="UNKNOWN_TARGET_STATE",
            current_state=current_state,
            requested_target=str(target_state),
            effective_state=current_state,
            stage_invocation="NONE",
        )

    if current_state == target_state:
        return _result(
            state="NO_OP",
            current_state=current_state,
            requested_target=target_state,
            effective_state=current_state,
            stage_invocation="NONE",
        )

    edge = (current_state, target_state)
    if edge not in ENABLED_EDGES:
        return _result(
            state="TRANSITION_NOT_ENABLED",
            current_state=current_state,
            requested_target=target_state,
            effective_state=current_state,
            stage_invocation="NONE",
            reason="NO_IMPLEMENTED_GOVERNED_STAGE_FOR_REQUESTED_EDGE",
        )

    # Current legal edge: quarantine -> resolved-but-unauthenticated.
    if intake_envelope is None or adapter is None or approved_registry is None:
        return _result(
            state="TRANSITION_PRECONDITION_MISSING",
            current_state=current_state,
            requested_target=target_state,
            effective_state=current_state,
            stage_invocation="NOT_INVOKED",
        )

    stage_result = execute_quarantine_resolution(
        intake_envelope,
        adapter=adapter,
        approved_registry=approved_registry,
    )
    if stage_result.get("trust_state") != RESOLVED_UNAUTHENTICATED or stage_result.get("state") != RESOLVED_UNAUTHENTICATED:
        return _result(
            state="TRANSITION_STAGE_FAILED",
            current_state=current_state,
            requested_target=target_state,
            effective_state=current_state,
            stage_invocation=ENABLED_EDGES[edge],
            stage_result=stage_result,
        )

    return _result(
        state="TRANSITION_EARNED",
        current_state=current_state,
        requested_target=target_state,
        effective_state=RESOLVED_UNAUTHENTICATED,
        stage_invocation=ENABLED_EDGES[edge],
        provider_authenticity=stage_result.get("provider_authenticity", "UNVERIFIED"),
        stage_result=stage_result,
        caller_claims_effect="NONE",
    )
