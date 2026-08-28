from copy import deepcopy

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import (
    EvidenceResolverAdapterError,
    ResolverAcquisition,
    ResolverAdapterIdentity,
)
from experience_spine_igt import build_condition_payload
from experience_spine_igt_evidence_package import SCHEMA_VERSION, digest_value, seal_package
from experience_spine_igt_trusted_adapter_gate import (
    ApprovedResolverAdapter,
    execute_registered_adapter_correlation,
)


BASELINE = "0664fb5451d2dacc7175009549ef9972d4efb0e6"
IDENTITY = ResolverAdapterIdentity(
    adapter_id="resolver/test-adapter",
    adapter_kind="provider-evidence-resolver",
    implementation_id="test-adapter-v1",
)
REGISTRY = {
    IDENTITY.adapter_id: ApprovedResolverAdapter(
        adapter_id=IDENTITY.adapter_id,
        adapter_kind=IDENTITY.adapter_kind,
        implementation_id=IDENTITY.implementation_id,
    )
}


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "experience_items": [
            {
                "knowledge_id": "K-TRUST-1",
                "pattern": "Prefer current evidence over historical guidance.",
                "knowledge_scope": "project:trusted-adapter-test",
                "lifecycle_state": "PROMOTED",
                "validation_state": "VALIDATED",
                "evidence": ["E-TRUST-1"],
                "evidence_state": "PROVEN",
                "authority_state": "ADVISORY",
                "source_identity": "HERMUZ:prior",
                "source_type": "HERMUZ-ENGINEERING",
                "evidence_group": "EG-TRUST",
                "consumer_routes": ["TEST"],
                "applicability_boundaries": ["release-operations"],
                "counterindications": [],
                "contradicts": [],
                "match_reasons": {"problem_types": ["authority-conflict"]},
                "score": 3,
            }
        ],
        "conflicts": [],
        "correlated_evidence_groups": [],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }


def _response() -> dict:
    return {
        "prediction": "Inspect current evidence.",
        "identified_invariants": ["CURRENT_EVIDENCE_FIRST"],
        "selected_authority": "CURRENT_GATE",
        "scope": ["bounded-case"],
        "action": "inspect_before_action",
        "evidence_refs": ["CURRENT-1"],
        "non_claims": ["NO_BROAD_GENERALIZATION"],
    }


def _attestation(run_id: str, context_id: str) -> dict:
    return {
        "run_id": run_id,
        "execution_context_id": context_id,
        "baseline_sha": BASELINE,
        "execution_independence": "YES",
        "information_independence": "YES",
        "state_independence": "YES",
        "temporal_independence": "YES",
        "mutation_independence": "YES",
        "source_conclusion_withheld": "YES",
        "leakage_detected": "NO",
    }


def _package() -> dict:
    run_id = "RUN-TRUST-1"
    context_id = "CTX-TRUST-1"
    payload = build_condition_payload("XSP-IGT-01", "L2", experience_packet=_experience_packet())
    return seal_package(
        {
            "schema_version": SCHEMA_VERSION,
            "package_id": "PKG-TRUST-1",
            "run_id": run_id,
            "case_id": "XSP-IGT-01",
            "condition": "L2",
            "participant_kind": "MODEL_RUN",
            "repository_baseline_sha": BASELINE,
            "execution_context_id": context_id,
            "source_model": "provider/model-v1",
            "source_instance_id": "provider-instance-1",
            "execution_surface": "provider-run-surface",
            "execution_started_at": "2026-08-28T20:00:00Z",
            "execution_completed_at": "2026-08-28T20:00:30Z",
            "participant_payload": payload,
            "participant_response": _response(),
            "independence_attestation": _attestation(run_id, context_id),
            "participant_evidence_ref": "provider://execution/RUN-TRUST-1",
            "independence_attestation_ref": "provider://attestation/RUN-TRUST-1",
        }
    )


def _participant_observation(package: dict) -> dict:
    return {
        "status": "FOUND",
        "observed_ref": package["participant_evidence_ref"],
        "run_id": package["run_id"],
        "case_id": package["case_id"],
        "condition": package["condition"],
        "execution_context_id": package["execution_context_id"],
        "repository_baseline_sha": package["repository_baseline_sha"],
        "source_model": package["source_model"],
        "source_instance_id": package["source_instance_id"],
        "execution_surface": package["execution_surface"],
        "execution_started_at": package["execution_started_at"],
        "execution_completed_at": package["execution_completed_at"],
        "payload_digest": package["payload_digest"],
        "response_digest": package["response_digest"],
    }


def _attestation_observation(package: dict) -> dict:
    return {
        "status": "FOUND",
        "observed_ref": package["independence_attestation_ref"],
        "run_id": package["run_id"],
        "execution_context_id": package["execution_context_id"],
        "repository_baseline_sha": package["repository_baseline_sha"],
        "attestation_digest": digest_value(package["independence_attestation"]),
        "attestation_content": deepcopy(package["independence_attestation"]),
    }


class FakeAdapter:
    def __init__(self, package: dict) -> None:
        self._identity = IDENTITY
        self.package = package
        self.participant_calls = 0
        self.attestation_calls = 0
        self.participant_observation = _participant_observation(package)
        self.attestation_observation = _attestation_observation(package)
        self.fail_participant = False
        self.fail_attestation = False
        self.change_identity_after_participant = False
        self.same_acquisition_id = False
        self.inject_reserved = False
        self.bad_participant_ref = False
        self.bad_time_order = False

    @property
    def identity(self):
        if self.change_identity_after_participant and self.participant_calls:
            return ResolverAdapterIdentity(
                adapter_id=IDENTITY.adapter_id,
                adapter_kind=IDENTITY.adapter_kind,
                implementation_id="changed-during-run",
            )
        return self._identity

    def acquire_participant(self, evidence_ref: str) -> ResolverAcquisition:
        self.participant_calls += 1
        if self.fail_participant:
            raise EvidenceResolverAdapterError("PARTICIPANT_PROVIDER_FAILURE")
        observation = deepcopy(self.participant_observation)
        if self.inject_reserved:
            observation["resolver_id"] = "caller-injected"
        return ResolverAcquisition(
            adapter_id=IDENTITY.adapter_id,
            adapter_kind=IDENTITY.adapter_kind,
            acquisition_id="ACQ-P-1",
            acquisition_surface="fake-provider-api",
            started_at="2026-08-28T20:01:00Z" if not self.bad_time_order else "2026-08-28T20:02:00Z",
            completed_at="2026-08-28T20:01:01Z",
            requested_ref="provider://execution/OTHER" if self.bad_participant_ref else evidence_ref,
            observation=observation,
        )

    def acquire_attestation(self, evidence_ref: str) -> ResolverAcquisition:
        self.attestation_calls += 1
        if self.fail_attestation:
            raise EvidenceResolverAdapterError("ATTESTATION_PROVIDER_FAILURE")
        return ResolverAcquisition(
            adapter_id=IDENTITY.adapter_id,
            adapter_kind=IDENTITY.adapter_kind,
            acquisition_id="ACQ-P-1" if self.same_acquisition_id else "ACQ-A-1",
            acquisition_surface="fake-provider-api",
            started_at="2026-08-28T20:01:02Z",
            completed_at="2026-08-28T20:01:03Z",
            requested_ref=evidence_ref,
            observation=deepcopy(self.attestation_observation),
        )


def test_registered_adapter_is_invoked_by_gate_and_correlates_without_authenticity_overclaim():
    package = _package()
    adapter = FakeAdapter(package)
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "APPROVED_ADAPTER_PATH_CORRELATED"
    assert result["adapter_execution"] == "OBSERVED_BY_GOVERNED_GATE"
    assert result["registry_path"] == "APPROVED_IDENTITY_MATCH"
    assert result["external_authenticity"] == "INCONCLUSIVE"
    assert result["provider_backed_authenticity"] == "NOT_ESTABLISHED"
    assert result["authority"] == "NONE"
    assert result["cognitive_effect"] == "NOT_ESTABLISHED"
    assert adapter.participant_calls == 1
    assert adapter.attestation_calls == 1
    assert result["correlation"]["state"] == "CORRELATED_AWAITING_TRUSTED_ADAPTER"


def test_invalid_package_never_invokes_adapter():
    package = _package()
    package["participant_payload"]["hidden_expectation"] = {"correct_answer": "x"}
    package = seal_package(package)
    adapter = FakeAdapter(package)
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "PACKAGE_NOT_ELIGIBLE"
    assert result["adapter_execution"] == "NOT_INVOKED"
    assert adapter.participant_calls == 0
    assert adapter.attestation_calls == 0


def test_unregistered_adapter_never_invokes_external_acquisition():
    package = _package()
    adapter = FakeAdapter(package)
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry={})
    assert result["state"] == "ADAPTER_NOT_APPROVED"
    assert result["reason"] == "ADAPTER_NOT_REGISTERED"
    assert result["adapter_execution"] == "NOT_INVOKED"
    assert adapter.participant_calls == 0


def test_registry_implementation_mismatch_blocks_before_acquisition():
    package = _package()
    adapter = FakeAdapter(package)
    registry = {
        IDENTITY.adapter_id: ApprovedResolverAdapter(
            adapter_id=IDENTITY.adapter_id,
            adapter_kind=IDENTITY.adapter_kind,
            implementation_id="other-implementation",
        )
    }
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=registry)
    assert result["state"] == "ADAPTER_NOT_APPROVED"
    assert result["reason"] == "ADAPTER_IMPLEMENTATION_MISMATCH"
    assert adapter.participant_calls == 0


def test_reserved_resolver_identity_in_observation_is_rejected():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.inject_reserved = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert "OBSERVATION_RESERVED_IDENTITY_INJECTION:resolver_id" in result["reason"]
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_adapter_requested_ref_mismatch_is_rejected_before_correlation():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.bad_participant_ref = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert result["reason"] == "ACQUISITION_REQUESTED_REF_MISMATCH"


def test_adapter_identity_change_during_execution_fails_closed():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.change_identity_after_participant = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert result["reason"] == "ADAPTER_IDENTITY_CHANGED_DURING_EXECUTION"
    assert adapter.participant_calls == 1
    assert adapter.attestation_calls == 0


def test_participant_and_attestation_cannot_reuse_same_acquisition_identity():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.same_acquisition_id = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert result["reason"] == "ACQUISITION_CHANNEL_ID_COLLISION"


def test_external_observation_mismatch_stays_mismatch_on_approved_adapter_path():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.participant_observation["payload_digest"] = "0" * 64
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "APPROVED_ADAPTER_PATH_MISMATCH"
    assert result["correlation"]["state"] == "EXTERNAL_EVIDENCE_MISMATCH"
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_adapter_exception_is_explicit_failure_not_inconclusive_success():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.fail_participant = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert "PARTICIPANT_PROVIDER_FAILURE" in result["reason"]
    assert result["adapter_execution"] == "FAILED"


def test_attestation_exception_after_participant_is_explicit_failure():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.fail_attestation = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert "ATTESTATION_PROVIDER_FAILURE" in result["reason"]
    assert adapter.participant_calls == 1
    assert adapter.attestation_calls == 1


def test_acquisition_time_order_is_validated():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.bad_time_order = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_EXECUTION_FAILED"
    assert result["reason"] == "ACQUISITION_TIME_ORDER_INVALID"


def test_registry_membership_never_yields_external_authenticity_verified():
    package = _package()
    adapter = FakeAdapter(package)
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert "VERIFIED" not in result["state"]
    assert result["external_authenticity"] != "VERIFIED"
    assert result["provider_backed_authenticity"] == "NOT_ESTABLISHED"


def test_self_declared_trust_inside_observation_has_no_authorizing_effect():
    package = _package()
    adapter = FakeAdapter(package)
    adapter.participant_observation["trusted"] = True
    adapter.participant_observation["approved"] = True
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "APPROVED_ADAPTER_PATH_CORRELATED"
    assert result["external_authenticity"] == "INCONCLUSIVE"
    assert result["authority"] == "NONE"


def test_noncanonical_adapter_identity_is_rejected_before_acquisition():
    package = _package()

    class BadIdentityAdapter(FakeAdapter):
        @property
        def identity(self):
            return {"adapter_id": IDENTITY.adapter_id}

    adapter = BadIdentityAdapter(package)
    result = execute_registered_adapter_correlation(package, adapter=adapter, approved_registry=REGISTRY)
    assert result["state"] == "ADAPTER_IDENTITY_REJECTED"
    assert "ADAPTER_IDENTITY_NOT_CANONICAL" in result["reason"]
    assert result["adapter_execution"] == "NOT_INVOKED"
    assert adapter.participant_calls == 0
