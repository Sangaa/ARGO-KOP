from copy import deepcopy

import pytest

from experience_spine_igt_external_evidence_intake import (
    ALLOWED_ARTIFACT_TYPES,
    build_external_evidence_intake,
    verify_external_evidence_intake,
)

BASELINE = "949acd74d65751786bc732a65902fbb00271d685"


def _build(**overrides):
    args = {
        "repository_baseline_sha": BASELINE,
        "source_channel": "provider-export",
        "source_ref": "receipt://opaque-001",
        "artifact_type": "MODEL_EXECUTION_RECEIPT",
        "raw_evidence": {
            "provider": "example-provider",
            "request_id": "req-123",
            "response_id": "resp-456",
            "payload": {"answer": "candidate"},
        },
        "external_claims": {
            "claimed_provider": "example-provider",
            "claimed_model": "example-model",
            "claimed_request_id": "req-123",
        },
    }
    args.update(overrides)
    return build_external_evidence_intake(**args)


def test_valid_external_evidence_is_sealed_but_untrusted():
    envelope = _build()
    result = verify_external_evidence_intake(envelope)
    assert result == {
        "state": "VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE",
        "reasons": [],
        "trust_state": "UNTRUSTED_QUARANTINED",
        "external_delivery": "NOT_PROVEN",
        "model_execution_authenticity": "NOT_PROVEN",
        "provider_authenticity": "UNVERIFIED",
        "authority": "NONE",
        "cognitive_effect": "NOT_ESTABLISHED",
    }
    assert envelope["intake_state"] == "SEALED_QUARANTINE_INTAKE"
    assert envelope["trust_state"] == "UNTRUSTED_QUARANTINED"


@pytest.mark.parametrize("artifact_type", sorted(ALLOWED_ARTIFACT_TYPES))
def test_all_supported_artifact_types_enter_same_quarantine(artifact_type):
    envelope = _build(artifact_type=artifact_type)
    assert envelope["artifact_type"] == artifact_type
    assert verify_external_evidence_intake(envelope)["trust_state"] == "UNTRUSTED_QUARANTINED"


def test_build_is_deterministic_for_identical_external_artifact():
    first = _build()
    second = _build()
    assert first == second
    assert first["intake_id"].startswith("IGT-EXT-")
    assert len(first["raw_evidence_digest"]) == 64
    assert len(first["envelope_digest"]) == 64


def test_raw_evidence_is_preserved_without_semantic_rewrite():
    raw = {"z": [3, 2, 1], "nested": {"claimed": True}, "text": "verbatim"}
    envelope = _build(raw_evidence=raw)
    assert envelope["raw_evidence"] == raw


def test_post_intake_raw_evidence_mutation_is_detected():
    envelope = _build()
    envelope["raw_evidence"]["payload"]["answer"] = "changed"
    result = verify_external_evidence_intake(envelope)
    assert result["state"] == "INVALID"
    assert "RAW_EVIDENCE_DIGEST_MISMATCH" in result["reasons"]
    assert "ENVELOPE_DIGEST_MISMATCH" in result["reasons"]


def test_source_ref_mutation_breaks_identity_and_digest():
    envelope = _build()
    envelope["source_ref"] = "receipt://different"
    result = verify_external_evidence_intake(envelope)
    assert "INTAKE_ID_MISMATCH" in result["reasons"]
    assert "ENVELOPE_DIGEST_MISMATCH" in result["reasons"]


def test_external_claims_may_carry_provider_ids_without_authenticating_them():
    envelope = _build()
    assert envelope["external_claims"]["claimed_request_id"] == "req-123"
    assert envelope["claim_boundary"]["provider_authenticity"] == "UNVERIFIED"
    assert verify_external_evidence_intake(envelope)["provider_authenticity"] == "UNVERIFIED"


@pytest.mark.parametrize(
    "blocked",
    [
        "AUTHENTICATED",
        "VERIFIED_PROVIDER",
        "PROVIDER_VERIFIED",
        "EXTERNAL_AUTHENTICITY_VERIFIED",
        "EXECUTION_VERIFIED",
        "DELIVERY_VERIFIED",
        "AUTHORIZED",
        "PROMOTED",
    ],
)
def test_prepromoted_external_claim_states_fail_closed(blocked):
    with pytest.raises(ValueError, match="PREPROMOTED_EXTERNAL_CLAIM"):
        _build(external_claims={"state": blocked})


def test_nested_prepromoted_claim_state_is_also_rejected():
    with pytest.raises(ValueError, match="PREPROMOTED_EXTERNAL_CLAIM"):
        _build(external_claims={"provider": {"auth": ["UNVERIFIED", "AUTHENTICATED"]}})


def test_verifier_rejects_post_build_trust_promotion():
    envelope = _build()
    envelope["trust_state"] = "AUTHENTICATED"
    result = verify_external_evidence_intake(envelope)
    assert "TRUST_STATE_INVALID" in result["reasons"]
    assert "ENVELOPE_DIGEST_MISMATCH" in result["reasons"]


def test_verifier_rejects_post_build_claim_boundary_promotion():
    envelope = _build()
    envelope["claim_boundary"]["model_execution"] = "EXECUTION_VERIFIED"
    result = verify_external_evidence_intake(envelope)
    assert "CLAIM_BOUNDARY_INVALID" in result["reasons"]
    assert "ENVELOPE_DIGEST_MISMATCH" in result["reasons"]


def test_full_baseline_sha_is_mandatory():
    for bad in ("main", "949acd74", "Z" * 40, ""):
        with pytest.raises(ValueError, match="FULL_BASELINE_SHA_REQUIRED"):
            _build(repository_baseline_sha=bad)


def test_source_channel_and_ref_are_required():
    with pytest.raises(ValueError, match="SOURCE_CHANNEL_REQUIRED"):
        _build(source_channel="")
    with pytest.raises(ValueError, match="SOURCE_REF_REQUIRED"):
        _build(source_ref="")


def test_none_raw_evidence_is_rejected_but_empty_structures_are_preservable():
    with pytest.raises(ValueError, match="RAW_EVIDENCE_REQUIRED"):
        _build(raw_evidence=None)
    empty = _build(raw_evidence={})
    assert empty["raw_evidence"] == {}
    assert verify_external_evidence_intake(empty)["state"] == "VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE"


def test_unknown_artifact_type_is_rejected():
    with pytest.raises(ValueError, match="UNSUPPORTED_ARTIFACT_TYPE"):
        _build(artifact_type="TRUST_ME_BRO")


def test_external_claims_must_be_mapping():
    with pytest.raises(ValueError, match="EXTERNAL_CLAIMS_MUST_BE_MAPPING"):
        _build(external_claims=["claimed"])


def test_intake_does_not_gain_authenticity_by_copying_provider_looking_fields():
    envelope = _build(
        raw_evidence={
            "provider_request_id": "req-real-looking",
            "provider_response_id": "resp-real-looking",
            "signature": "opaque-signature-looking-value",
            "status": "success",
        }
    )
    result = verify_external_evidence_intake(envelope)
    assert result["state"] == "VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE"
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution_authenticity"] == "NOT_PROVEN"
    assert result["provider_authenticity"] == "UNVERIFIED"


def test_deepcopy_prevents_caller_mutation_after_build_from_rewriting_intake():
    raw = {"receipt": {"id": "one"}}
    envelope = _build(raw_evidence=raw)
    original = deepcopy(envelope)
    raw["receipt"]["id"] = "two"
    assert envelope == original
