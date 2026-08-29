from copy import deepcopy

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import ResolverAcquisition, ResolverAdapterIdentity
from experience_spine_igt_external_evidence_intake import build_external_evidence_intake
from experience_spine_igt_trust_state_transition_gate import request_trust_transition
from experience_spine_igt_trusted_adapter_gate import ApprovedResolverAdapter


BASELINE = "60e5739a19ee673031ebfbffca40d9c9c852c288"
SOURCE_REF = "evidence://external/transition-001"


def _intake():
    return build_external_evidence_intake(
        repository_baseline_sha=BASELINE,
        source_channel="provider-export",
        source_ref=SOURCE_REF,
        artifact_type="MODEL_EXECUTION_RECEIPT",
        raw_evidence={"provider": "claimed-provider", "payload": {"answer": "candidate"}},
        external_claims={"claimed_provider": "claimed-provider"},
    )


class FakeResolver:
    def __init__(self, raw, *, status="FOUND"):
        self._identity = ResolverAdapterIdentity(
            adapter_id="resolver/fake-transition",
            adapter_kind="fake-transition-resolver",
            implementation_id="fake-transition-v1",
        )
        self.raw = deepcopy(raw)
        self.status = status
        self.calls = 0

    @property
    def identity(self):
        return self._identity

    def acquire_external(self, evidence_ref):
        self.calls += 1
        if self.status == "FOUND":
            observation = {"status": "FOUND", "observed_ref": evidence_ref, "evidence_content": deepcopy(self.raw)}
        else:
            observation = {"status": self.status, "observed_ref": None}
        return ResolverAcquisition(
            adapter_id=self._identity.adapter_id,
            adapter_kind=self._identity.adapter_kind,
            acquisition_id="ACQ-TRANSITION-001",
            acquisition_surface="fake-read-only-surface",
            started_at="2026-08-29T05:55:00Z",
            completed_at="2026-08-29T05:55:01Z",
            requested_ref=evidence_ref,
            observation=observation,
        )


def _registry(adapter):
    identity = adapter.identity
    return {
        identity.adapter_id: ApprovedResolverAdapter(
            adapter_id=identity.adapter_id,
            adapter_kind=identity.adapter_kind,
            implementation_id=identity.implementation_id,
        )
    }


def test_guard_earns_only_current_implemented_transition_by_invoking_stage():
    intake = _intake()
    adapter = FakeResolver(intake["raw_evidence"])
    result = request_trust_transition(
        current_state="UNTRUSTED_QUARANTINED",
        target_state="RESOLVED_UNAUTHENTICATED",
        intake_envelope=intake,
        adapter=adapter,
        approved_registry=_registry(adapter),
        caller_claims={"verified": True, "authorized": True},
    )
    assert result["state"] == "TRANSITION_EARNED"
    assert result["effective_state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["stage_invocation"] == "QUARANTINE_RESOLUTION_GATE"
    assert result["caller_claims_effect"] == "NONE"
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["authority"] == "NONE"
    assert adapter.calls == 1


def test_future_authentication_jump_is_not_enabled_and_invokes_nothing():
    intake = _intake()
    adapter = FakeResolver(intake["raw_evidence"])
    result = request_trust_transition(
        current_state="RESOLVED_UNAUTHENTICATED",
        target_state="PROVIDER_AUTHENTICATED",
        intake_envelope=intake,
        adapter=adapter,
        approved_registry=_registry(adapter),
        caller_claims={"authenticated": True},
    )
    assert result["state"] == "TRANSITION_NOT_ENABLED"
    assert result["effective_state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["stage_invocation"] == "NONE"
    assert adapter.calls == 0


def test_direct_authority_or_promotion_jump_is_rejected():
    for target in ("AUTHORIZED", "ADMITTED_BOUNDED", "PROMOTED", "EXECUTION_VERIFIED"):
        result = request_trust_transition(
            current_state="UNTRUSTED_QUARANTINED",
            target_state=target,
            caller_claims={"verified": True, "authority": target},
        )
        assert result["state"] == "TRANSITION_NOT_ENABLED"
        assert result["effective_state"] == "UNTRUSTED_QUARANTINED"
        assert result["authority"] == "NONE"


def test_same_state_is_noop_and_requires_no_stage_dependencies():
    result = request_trust_transition(
        current_state="RESOLVED_UNAUTHENTICATED",
        target_state="RESOLVED_UNAUTHENTICATED",
    )
    assert result["state"] == "NO_OP"
    assert result["effective_state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["stage_invocation"] == "NONE"


def test_unknown_state_names_fail_closed():
    assert request_trust_transition(current_state="MAGIC_TRUST", target_state="AUTHORIZED")["state"] == "UNKNOWN_CURRENT_STATE"
    result = request_trust_transition(current_state="UNTRUSTED_QUARANTINED", target_state="MAGIC_AUTHENTICATED")
    assert result["state"] == "UNKNOWN_TARGET_STATE"
    assert result["effective_state"] == "UNTRUSTED_QUARANTINED"


def test_enabled_edge_requires_dependencies_before_stage_invocation():
    result = request_trust_transition(
        current_state="UNTRUSTED_QUARANTINED",
        target_state="RESOLVED_UNAUTHENTICATED",
    )
    assert result["state"] == "TRANSITION_PRECONDITION_MISSING"
    assert result["effective_state"] == "UNTRUSTED_QUARANTINED"
    assert result["stage_invocation"] == "NOT_INVOKED"


def test_resolution_failure_preserves_prior_trust_state():
    intake = _intake()
    adapter = FakeResolver(intake["raw_evidence"], status="UNAVAILABLE")
    result = request_trust_transition(
        current_state="UNTRUSTED_QUARANTINED",
        target_state="RESOLVED_UNAUTHENTICATED",
        intake_envelope=intake,
        adapter=adapter,
        approved_registry=_registry(adapter),
    )
    assert result["state"] == "TRANSITION_STAGE_FAILED"
    assert result["effective_state"] == "UNTRUSTED_QUARANTINED"
    assert result["stage_result"]["state"] == "RESOLUTION_UNAVAILABLE"
    assert adapter.calls == 1
