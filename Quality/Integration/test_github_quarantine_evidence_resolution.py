import base64
import json

from Services.GITHUB_EVIDENCE_RESOLVER_ADAPTER import (
    GitHubEvidenceResolverAdapter,
    GitHubEvidenceResolverConfig,
)
from experience_spine_igt_external_evidence_intake import build_external_evidence_intake
from experience_spine_igt_quarantine_resolution_gate import execute_quarantine_resolution
from experience_spine_igt_trusted_adapter_gate import ApprovedResolverAdapter


COMMIT = "78342410e9cc6c59cf238a0dc7df3118c29bc18d"
REF = f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence/quarantine-artifact.json"


def _encode(value):
    return base64.b64encode(
        json.dumps(value, ensure_ascii=False).encode("utf-8")
    ).decode("ascii")


class StaticTransport:
    def __init__(self, value):
        self.value = value
        self.requests = []
        self.missing = False

    def __call__(self, request, timeout):
        self.requests.append((request, timeout))
        if self.missing:
            raise FileNotFoundError(request.full_url)
        return {"type": "file", "sha": "b" * 40, "content": _encode(self.value)}


def _adapter(transport):
    return GitHubEvidenceResolverAdapter(
        GitHubEvidenceResolverConfig(token="test-token"),
        transport=transport,
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


def _intake(raw):
    return build_external_evidence_intake(
        repository_baseline_sha=COMMIT,
        source_channel="immutable-github-artifact",
        source_ref=REF,
        artifact_type="OTHER_EXTERNAL_EVIDENCE",
        raw_evidence=raw,
        external_claims={"claimed_origin": "external-provider"},
    )


def test_generic_github_acquisition_nests_raw_json_without_control_field_laundering():
    raw = {
        "resolver_id": "external-payload-value",
        "authority": "AUTHORIZED-looking-but-untrusted",
        "nested": {"value": 7},
    }
    transport = StaticTransport(raw)
    adapter = _adapter(transport)
    acquisition = adapter.acquire_external(REF)

    assert acquisition.requested_ref == REF
    assert acquisition.acquisition_id.startswith("GH-EVID-EXTERNAL-")
    assert acquisition.observation["status"] == "FOUND"
    assert acquisition.observation["observed_ref"] == REF
    assert acquisition.observation["evidence_content"] == raw
    assert acquisition.observation["github_artifact_commit_sha"] == COMMIT
    assert acquisition.observation["github_artifact_blob_sha"] == "b" * 40
    assert acquisition.observation.get("authority") is None
    assert acquisition.observation.get("resolver_id") is None


def test_generic_github_acquisition_supports_non_object_json_values():
    raw = ["a", {"b": 2}, False]
    acquisition = _adapter(StaticTransport(raw)).acquire_external(REF)
    assert acquisition.observation["evidence_content"] == raw


def test_generic_github_404_is_unavailable_not_fabricated_mismatch():
    transport = StaticTransport({"unused": True})
    transport.missing = True
    acquisition = _adapter(transport).acquire_external(REF)
    assert acquisition.observation == {"status": "UNAVAILABLE", "observed_ref": None}
    assert acquisition.acquisition_id.startswith("GH-EVID-EXTERNAL-")


def test_exact_immutable_github_reacquisition_flows_to_resolved_unauthenticated_only():
    raw = {"receipt": {"request_id": "req-1", "status": "success-looking"}}
    transport = StaticTransport(raw)
    adapter = _adapter(transport)
    intake = _intake(raw)

    result = execute_quarantine_resolution(
        intake,
        adapter=adapter,
        approved_registry=_registry(adapter),
    )

    assert result["state"] == "RESOLVED_UNAUTHENTICATED"
    assert result["technical_resolution"] == "EXACT_CONTENT_REACQUIRED_FROM_EXACT_REF"
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution_authenticity"] == "NOT_PROVEN"
    assert result["authority"] == "NONE"
    assert len(transport.requests) == 1


def test_github_reacquisition_content_change_is_detected_by_gate():
    intake = _intake({"value": "sealed"})
    adapter = _adapter(StaticTransport({"value": "changed"}))
    result = execute_quarantine_resolution(
        intake,
        adapter=adapter,
        approved_registry=_registry(adapter),
    )
    assert result["state"] == "RESOLUTION_MISMATCH"
    assert "RAW_EVIDENCE_DIGEST_MISMATCH" in result["reasons"]
    assert result["trust_state"] == "UNTRUSTED_QUARANTINED"
