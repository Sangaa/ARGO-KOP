from copy import deepcopy

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import (
    EvidenceResolverAdapterError,
    ResolverAcquisition,
    ResolverAdapterIdentity,
)
from experience_spine_igt_external_evidence_intake import build_external_evidence_intake
from experience_spine_igt_quarantine_resolution_gate import execute_quarantine_resolution
from experience_spine_igt_trusted_adapter_gate import ApprovedResolverAdapter


BASELINE = "78342410e9cc6c59cf238a0dc7df3118c29bc18d"
SOURCE_REF = "evidence://external/exact-001"


def _intake(raw_evidence=None):
    if raw_evidence is None:
        raw_evidence = {
            "provider": "claimed-provider",
            "request_id": "req-1",
            "response_id": "resp-1",
            "payload": {"answer": "candidate"},
        }
    return build_external_evidence_intake(
        repository_baseline_sha=BASELINE,
        source_channel="provider-export",
        source_ref=SOURCE_REF,
        artifact_type="MODEL_EXECUTION_RECEIPT",
        raw_evidence=raw_evidence,
        external_claims={"claimed_provider": "claimed-provider"},
    )


class FakeQuarantineResolver:
    def __init__(self, observation, *, identity=None, requested_ref=SOURCE_REF, fail=None):
        self._identity = identity or ResolverAdapterIdentity(
            adapter_id="resolver/fake-quarantine",
            adapter_kind="fake-quarantine-resolver",
            implementation_id="fake-quarantine-v1",
        )
        self.observation = observation
        self.requested_ref = requested_ref
        self.fail = fail
        self.calls = 0
        self.change_identity_after_call = False

    @property
    def identity(self):
        if self.change_identity_after_call and self.calls:
            return ResolverAdapterIdentity(
                adapter_id=self._identity.adapter_id,
                adapter_kind=self._identity.adapter_kind,
                implementation_id="changed-implementation",
            )
        return self._identity

    def acquire_external(self, evidence_ref):
        self.calls += 1
        if self.fail:
            raise EvidenceResolverAdapterError(self.fail)
        return ResolverAcquisition(
            adapter_id=self._identity.adapter_id,
            adapter_kind=self._identity.adapter_kind,
            acquisition_id="ACQ-EXT-001",
            acquisition_surface="fake-read-only-surface",
            started_at="2026-08-29T05:40:00Z",
            completed_at="2026-08-29T05:40:01Z",
            requested_ref=self.requested_ref,
            observation=deepcopy(self.observation),
        )


def _found(raw):
    return {"status": "FOUND", "observed_ref": SOURCE_REF, "evidence_content": deepcopy(raw)}


def _registry(adapter):
    identity = adapter._identity
    return {
        identity.adapter_id: ApprovedResolverAdapter(
            adapter_id=identity.adapter_id,
            adapter_kind=identity.adapter_kind,
            implementation_id=identity.implementation_id,
        )
    }


def test_exact_approved_reacquisition_advances_only_to_resolved_unauthenticated():
    intake = _intake()
    adapter = FakeQuarantineResolver(_found(intake["raw_evidence"]))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))

    assert result["state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["trust_state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["technical_resolution"] == "EXACT_CONTENT_REACQUIRED_FROM_EXACT_REF"
    assert result["acquired_evidence_digest"] == intake["raw_evidence_digest"]
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["external_authenticity"] == "NOT_ESTABLISHED_BY_RESOLUTION"
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution_authenticity"] == "NOT_PROVEN"
    assert result["independence"] == "UNVERIFIED"
    assert result["authority"] == "NONE"
    assert result["cognitive_effect"] == "NOT_ESTABLISHED"
    assert adapter.calls == 1


def test_unapproved_adapter_is_not_invoked():
    intake = _intake()
    adapter = FakeQuarantineResolver(_found(intake["raw_evidence"]))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry={})
    assert result["state"] == "ADAPTER_NOT_APPROVED"
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"
    assert result["adapter_execution"] == "NOT_INVOKED"
    assert adapter.calls == 0


def test_registry_implementation_mismatch_is_not_invoked():
    intake = _intake()
    adapter = FakeQuarantineResolver(_found(intake["raw_evidence"]))
    identity = adapter._identity
    registry = {
        identity.adapter_id: ApprovedResolverAdapter(
            adapter_id=identity.adapter_id,
            adapter_kind=identity.adapter_kind,
            implementation_id="other-implementation",
        )
    }
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=registry)
    assert result["state"] == "ADAPTER_NOT_APPROVED"
    assert result["reason"] == "ADAPTER_IMPLEMENTATION_MISMATCH"
    assert adapter.calls == 0


def test_invalid_or_mutated_intake_is_rejected_before_adapter_execution():
    intake = _intake()
    intake["trust_state"] = "AUTHENTICATED"
    adapter = FakeQuarantineResolver(_found(intake["raw_evidence"]))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "INTAKE_NOT_ELIGIBLE"
    assert result["adapter_execution"] == "NOT_INVOKED"
    assert adapter.calls == 0


def test_acquisition_requested_ref_must_equal_sealed_source_ref():
    intake = _intake()
    adapter = FakeQuarantineResolver(
        _found(intake["raw_evidence"]),
        requested_ref="evidence://external/other",
    )
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_EXECUTION_FAILED"
    assert "ACQUISITION_REQUESTED_REF_MISMATCH" in result["reason"]
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"


def test_found_observed_ref_mismatch_stays_quarantined():
    intake = _intake()
    observation = _found(intake["raw_evidence"])
    observation["observed_ref"] = "evidence://external/other"
    adapter = FakeQuarantineResolver(observation)
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_MISMATCH"
    assert "OBSERVED_REF_MISMATCH" in result["reasons"]
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"


def test_content_mismatch_cannot_advance_even_when_ref_matches():
    intake = _intake()
    changed = deepcopy(intake["raw_evidence"])
    changed["payload"]["answer"] = "different"
    adapter = FakeQuarantineResolver(_found(changed))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_MISMATCH"
    assert "RAW_EVIDENCE_DIGEST_MISMATCH" in result["reasons"]
    assert "RAW_EVIDENCE_CONTENT_MISMATCH" in result["reasons"]


def test_canonical_digest_detects_json_type_difference_even_if_python_equality_is_loose():
    intake = _intake(raw_evidence={"value": True})
    adapter = FakeQuarantineResolver(_found({"value": 1}))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_MISMATCH"
    assert "RAW_EVIDENCE_DIGEST_MISMATCH" in result["reasons"]


def test_unavailable_is_not_mismatch_and_does_not_advance_trust():
    intake = _intake()
    adapter = FakeQuarantineResolver({"status": "UNAVAILABLE", "observed_ref": None})
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_UNAVAILABLE"
    assert result["technical_resolution"] == "UNAVAILABLE_BY_THIS_APPROVED_ADAPTER_PATH"
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"
    assert result["provider_authenticity"] == "UNVERIFIED"


def test_unavailable_with_content_is_contradictory_and_fails_closed():
    intake = _intake()
    adapter = FakeQuarantineResolver(
        {"status": "UNAVAILABLE", "observed_ref": None, "evidence_content": intake["raw_evidence"]}
    )
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_MISMATCH"
    assert "UNAVAILABLE_OBSERVATION_CONTRADICTS_CONTENT" in result["reasons"]


def test_partial_resolution_remains_inconclusive_and_quarantined():
    intake = _intake()
    adapter = FakeQuarantineResolver({"status": "PARTIAL", "observed_ref": SOURCE_REF})
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_INCONCLUSIVE"
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"


def test_observation_cannot_inject_trust_or_authority_control_fields():
    intake = _intake()
    observation = _found(intake["raw_evidence"])
    observation["authority"] = "AUTHORIZED"
    adapter = FakeQuarantineResolver(observation)
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_EXECUTION_FAILED"
    assert "OBSERVATION_RESERVED_CONTROL_INJECTION:authority" in result["reason"]
    assert result["authority"] == "NONE"


def test_adapter_identity_must_remain_stable_during_execution():
    intake = _intake()
    adapter = FakeQuarantineResolver(_found(intake["raw_evidence"]))
    adapter.change_identity_after_call = True
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_EXECUTION_FAILED"
    assert "ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION" in result["reason"]


def test_adapter_exception_fails_closed_without_authenticity_promotion():
    intake = _intake()
    adapter = FakeQuarantineResolver({}, fail="SOURCE_UNAVAILABLE")
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLUTION_EXECUTION_FAILED"
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["authority"] == "NONE"


def test_generic_resolution_supports_non_object_json_evidence_without_semantic_rewrite():
    raw = ["receipt", {"value": 3}, False]
    intake = _intake(raw_evidence=raw)
    adapter = FakeQuarantineResolver(_found(raw))
    result = execute_quarantine_resolution(intake, adapter=adapter, approved_registry=_registry(adapter))
    assert result["state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["resolution_observation"]["evidence_content"] == raw
