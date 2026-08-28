import base64
import json

import pytest

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import EvidenceResolverAdapterError
from Services.GITHUB_EVIDENCE_RESOLVER_ADAPTER import (
    GitHubEvidenceResolverAdapter,
    GitHubEvidenceResolverConfig,
    parse_github_artifact_reference,
)
from experience_spine_igt import build_condition_payload
from experience_spine_igt_evidence_package import SCHEMA_VERSION, digest_value, seal_package
from experience_spine_igt_trusted_adapter_gate import (
    ApprovedResolverAdapter,
    execute_registered_adapter_correlation,
)


COMMIT = "90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa"
PART_REF = f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence/participant.json"
ATT_REF = f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence/attestation.json"


def _encode_json(value) -> str:
    return base64.b64encode(json.dumps(value).encode("utf-8")).decode("ascii")


def _package() -> dict:
    run_id = "RUN-GH-1"
    context_id = "CTX-GH-1"
    experience = {
        "status": "READY",
        "experience_items": [],
        "conflicts": [],
        "correlated_evidence_groups": [],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }
    payload = build_condition_payload("XSP-IGT-01", "L2", experience_packet=experience)
    response = {
        "prediction": "Inspect current evidence.",
        "identified_invariants": ["CURRENT_EVIDENCE_FIRST"],
        "selected_authority": "CURRENT_GATE",
        "scope": ["bounded-case"],
        "action": "inspect_before_action",
        "evidence_refs": ["CURRENT-1"],
        "non_claims": ["NO_BROAD_GENERALIZATION"],
    }
    attestation = {
        "run_id": run_id,
        "execution_context_id": context_id,
        "baseline_sha": COMMIT,
        "execution_independence": "YES",
        "information_independence": "YES",
        "state_independence": "YES",
        "temporal_independence": "YES",
        "mutation_independence": "YES",
        "source_conclusion_withheld": "YES",
        "leakage_detected": "NO",
    }
    return seal_package(
        {
            "schema_version": SCHEMA_VERSION,
            "package_id": "PKG-GH-1",
            "run_id": run_id,
            "case_id": "XSP-IGT-01",
            "condition": "L2",
            "participant_kind": "MODEL_RUN",
            "repository_baseline_sha": COMMIT,
            "execution_context_id": context_id,
            "source_model": "external/model-label",
            "source_instance_id": "external-instance-1",
            "execution_surface": "external-run-surface",
            "execution_started_at": "2026-08-28T20:00:00Z",
            "execution_completed_at": "2026-08-28T20:00:30Z",
            "participant_payload": payload,
            "participant_response": response,
            "independence_attestation": attestation,
            "participant_evidence_ref": PART_REF,
            "independence_attestation_ref": ATT_REF,
        }
    )


def _participant_observation(package: dict) -> dict:
    return {
        "status": "FOUND",
        "observed_ref": PART_REF,
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
        "observed_ref": ATT_REF,
        "run_id": package["run_id"],
        "execution_context_id": package["execution_context_id"],
        "repository_baseline_sha": package["repository_baseline_sha"],
        "attestation_digest": digest_value(package["independence_attestation"]),
        "attestation_content": package["independence_attestation"],
    }


class FakeTransport:
    def __init__(self, participant: dict, attestation: dict) -> None:
        self.participant = participant
        self.attestation = attestation
        self.requests = []
        self.missing_paths = set()

    def __call__(self, request, timeout):
        self.requests.append((request, timeout))
        url = request.full_url
        if any(path in url for path in self.missing_paths):
            raise FileNotFoundError(url)
        content = self.attestation if "attestation.json" in url else self.participant
        return {"type": "file", "sha": "a" * 40, "content": _encode_json(content)}


def _adapter(transport) -> GitHubEvidenceResolverAdapter:
    return GitHubEvidenceResolverAdapter(
        GitHubEvidenceResolverConfig(token="test-token"),
        transport=transport,
    )


def _registry(adapter: GitHubEvidenceResolverAdapter):
    identity = adapter.identity
    return {
        identity.adapter_id: ApprovedResolverAdapter(
            adapter_id=identity.adapter_id,
            adapter_kind=identity.adapter_kind,
            implementation_id=identity.implementation_id,
        )
    }


def test_reference_requires_full_immutable_sha_and_normalized_path():
    ref = parse_github_artifact_reference(PART_REF)
    assert ref.owner == "Sangaa"
    assert ref.repo == "ARGO-KOP"
    assert ref.commit_sha == COMMIT
    assert ref.path == "Evidence/participant.json"


@pytest.mark.parametrize(
    "value",
    [
        "https://github.com/Sangaa/ARGO-KOP/main/Evidence/a.json",
        "github+artifact://Sangaa/ARGO-KOP@main/Evidence/a.json",
        "github+artifact://Sangaa/ARGO-KOP@90ad59c/Evidence/a.json",
        f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/../secret.json",
        f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence//a.json",
        f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence\\a.json",
    ],
)
def test_mutable_or_ambiguous_references_are_rejected(value):
    with pytest.raises(EvidenceResolverAdapterError):
        parse_github_artifact_reference(value)


def test_transport_request_uses_exact_contents_path_and_full_commit_ref():
    package = _package()
    transport = FakeTransport(_participant_observation(package), _attestation_observation(package))
    adapter = _adapter(transport)
    acquisition = adapter.acquire_participant(PART_REF)
    assert acquisition.requested_ref == PART_REF
    assert acquisition.observation["github_artifact_commit_sha"] == COMMIT
    request, timeout = transport.requests[0]
    assert request.method == "GET"
    assert "/repos/Sangaa/ARGO-KOP/contents/Evidence/participant.json?ref=" in request.full_url
    assert COMMIT in request.full_url
    assert timeout == 20.0
    assert request.get_header("Authorization") == "Bearer test-token"


def test_adapter_surface_is_read_only():
    package = _package()
    adapter = _adapter(FakeTransport(_participant_observation(package), _attestation_observation(package)))
    for forbidden in ("create_file", "update_file", "delete_file", "write", "put"):
        assert not hasattr(adapter, forbidden)


def test_acquired_json_adds_github_artifact_identity_without_model_authenticity_claim():
    package = _package()
    adapter = _adapter(FakeTransport(_participant_observation(package), _attestation_observation(package)))
    acquisition = adapter.acquire_participant(PART_REF)
    observation = acquisition.observation
    assert observation["status"] == "FOUND"
    assert observation["github_artifact_owner"] == "Sangaa"
    assert observation["github_artifact_repo"] == "ARGO-KOP"
    assert observation["github_artifact_path"] == "Evidence/participant.json"
    assert observation["github_artifact_blob_sha"] == "a" * 40
    assert "external_authenticity" not in observation
    assert "model_execution_verified" not in observation


def test_404_becomes_identified_unavailable_acquisition():
    package = _package()
    transport = FakeTransport(_participant_observation(package), _attestation_observation(package))
    transport.missing_paths.add("participant.json")
    adapter = _adapter(transport)
    acquisition = adapter.acquire_participant(PART_REF)
    assert acquisition.observation == {"status": "UNAVAILABLE", "observed_ref": None}
    assert acquisition.acquisition_id.startswith("GH-EVID-PARTICIPANT-")
    assert acquisition.acquisition_surface == "github-contents-api-immutable-ref"


def test_directory_target_fails_closed():
    def transport(request, timeout):
        return {"type": "dir", "sha": "a" * 40, "content": ""}

    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_TARGET_NOT_FILE"):
        _adapter(transport).acquire_participant(PART_REF)


def test_invalid_base64_or_json_fails_closed():
    def bad_base64(request, timeout):
        return {"type": "file", "sha": "a" * 40, "content": "%%%not-base64%%%"}

    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_CONTENT_DECODE_FAILED"):
        _adapter(bad_base64).acquire_participant(PART_REF)

    def bad_json(request, timeout):
        return {"type": "file", "sha": "a" * 40, "content": base64.b64encode(b"not-json").decode()}

    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_JSON_INVALID"):
        _adapter(bad_json).acquire_participant(PART_REF)


def test_non_object_json_is_rejected():
    def transport(request, timeout):
        return {"type": "file", "sha": "a" * 40, "content": _encode_json([1, 2, 3])}

    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_JSON_NOT_OBJECT"):
        _adapter(transport).acquire_participant(PART_REF)


def test_artifact_cannot_self_inject_resolver_identity():
    package = _package()
    observation = _participant_observation(package)
    observation["resolver_id"] = "self-declared"
    transport = FakeTransport(observation, _attestation_observation(package))
    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_RESERVED_IDENTITY_INJECTION:resolver_id"):
        _adapter(transport).acquire_participant(PART_REF)


def test_exact_github_artifacts_flow_through_governed_adapter_gate_but_do_not_verify_model_execution():
    package = _package()
    transport = FakeTransport(_participant_observation(package), _attestation_observation(package))
    adapter = _adapter(transport)
    result = execute_registered_adapter_correlation(
        package,
        adapter=adapter,
        approved_registry=_registry(adapter),
    )
    assert result["state"] == "APPROVED_ADAPTER_PATH_CORRELATED"
    assert result["external_authenticity"] == "INCONCLUSIVE"
    assert result["provider_backed_authenticity"] == "NOT_ESTABLISHED"
    assert result["correlation"]["state"] == "CORRELATED_AWAITING_TRUSTED_ADAPTER"
    assert len(transport.requests) == 2


def test_github_artifact_content_mismatch_remains_mismatch():
    package = _package()
    participant = _participant_observation(package)
    participant["payload_digest"] = "0" * 64
    adapter = _adapter(FakeTransport(participant, _attestation_observation(package)))
    result = execute_registered_adapter_correlation(
        package,
        adapter=adapter,
        approved_registry=_registry(adapter),
    )
    assert result["state"] == "APPROVED_ADAPTER_PATH_MISMATCH"
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_environment_configuration_requires_token(monkeypatch):
    monkeypatch.delenv("ARGO_GITHUB_TOKEN", raising=False)
    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_RESOLVER_TOKEN_MISSING"):
        GitHubEvidenceResolverConfig.from_environment()
