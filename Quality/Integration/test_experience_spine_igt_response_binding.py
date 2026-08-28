from copy import deepcopy

import pytest

from experience_spine_igt import REQUIRED_RESPONSE_FIELDS
from experience_spine_igt_participant_export import build_participant_export
from experience_spine_igt_response_binding import build_response_binding, verify_response_binding

BASELINE = "19805fbb948f4ae32e1c97169cc4f50b80681812"


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "task_id": "XSP-IGT-BINDING-PACKET",
        "execution_identity": "HERMUZ:binding-source",
        "execution_context": {"consumer_route": "HERMUZ"},
        "experience_items": [{
            "knowledge_id": "K-BINDING",
            "pattern": "Use current governed evidence before historical guidance.",
            "knowledge_scope": "project:test",
            "lifecycle_state": "PROMOTED",
            "validation_state": "VALIDATED",
            "evidence": ["E-BINDING-1"],
            "evidence_state": "PROVEN",
            "authority_state": "ADVISORY",
            "source_identity": "HERMUZ:prior-run",
            "source_type": "HERMUZ-ENGINEERING",
            "evidence_group": "EG-BINDING",
            "consumer_routes": ["HERMUZ"],
            "applicability_boundaries": ["binding-test"],
            "counterindications": [],
            "contradicts": [],
            "match_reasons": {"problem_types": ["response-attribution"]},
            "score": 1,
        }],
        "conflicts": [],
        "correlated_evidence_groups": [],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }


def _export(case_id="XSP-IGT-01", condition="B0") -> dict:
    kwargs = {
        "experiment_id": "IGT-BINDING-001",
        "case_id": case_id,
        "condition": condition,
        "baseline_sha": BASELINE,
    }
    if condition in {"L1", "L2"}:
        kwargs["experience_packet"] = _experience_packet()
    return build_participant_export(**kwargs)


def _response() -> dict:
    return {
        "prediction": "Proceed only with current governed evidence.",
        "identified_invariants": ["CURRENT_EVIDENCE"],
        "selected_authority": "CURRENT_CANONICAL_STATE",
        "scope": ["project:test"],
        "action": "REVALIDATE",
        "evidence_refs": ["E-BINDING-1"],
        "non_claims": ["NO_EXTERNAL_AUTHENTICITY_CLAIM"],
    }


@pytest.mark.parametrize("case_id", ["XSP-IGT-01", "XSP-IGT-02"])
@pytest.mark.parametrize("condition", ["B0", "L1", "L2"])
def test_all_six_rows_bind_to_exact_verified_exports(case_id, condition):
    export = _export(case_id, condition)
    binding = build_response_binding(participant_export=export, participant_response=_response())
    result = verify_response_binding(binding=binding, participant_export=export)
    assert result == {
        "state": "VERIFIED_LOCAL_BINDING",
        "reasons": [],
        "local_attribution": "PASS",
        "external_delivery": "NOT_PROVEN",
        "model_execution": "NOT_PROVEN",
        "provider_authenticity": "NOT_PROVEN",
        "authority": "NONE",
        "cognitive_effect": "INCONCLUSIVE",
    }
    assert binding["binding_state"] == "LOCALLY_BOUND_RESPONSE"
    assert binding["export_id"] == export["export_id"]
    assert binding["export_package_digest"] == export["package_digest"]
    assert binding["baseline_sha"] == BASELINE


def test_binding_is_deterministic_for_same_export_and_response():
    export = _export()
    first = build_response_binding(participant_export=export, participant_response=_response())
    second = build_response_binding(participant_export=export, participant_response=_response())
    assert first == second
    assert first["binding_id"].startswith("IGT-BIND-")
    assert len(first["response_digest"]) == 64
    assert len(first["binding_package_digest"]) == 64


def test_same_response_bound_to_different_condition_has_different_identity():
    b0 = build_response_binding(participant_export=_export(condition="B0"), participant_response=_response())
    l1 = build_response_binding(participant_export=_export(condition="L1"), participant_response=_response())
    assert b0["binding_id"] != l1["binding_id"]
    assert b0["export_id"] != l1["export_id"]


def test_swapping_export_after_binding_is_rejected():
    binding = build_response_binding(participant_export=_export(condition="B0"), participant_response=_response())
    result = verify_response_binding(binding=binding, participant_export=_export(condition="L1"))
    assert result["state"] == "INVALID"
    assert "EXPORT_ID_MISMATCH" in result["reasons"]
    assert "EXPORT_PACKAGE_DIGEST_MISMATCH" in result["reasons"]
    assert "CONDITION_MISMATCH" in result["reasons"]


def test_response_mutation_after_binding_breaks_digest_identity_and_package_seal():
    export = _export()
    binding = build_response_binding(participant_export=export, participant_response=_response())
    binding["participant_response"]["action"] = "MUTATED"
    result = verify_response_binding(binding=binding, participant_export=export)
    assert result["state"] == "INVALID"
    assert "RESPONSE_DIGEST_MISMATCH" in result["reasons"]
    assert "BINDING_PACKAGE_DIGEST_MISMATCH" in result["reasons"]


def test_export_mutation_after_binding_is_rejected_by_export_verifier():
    export = _export()
    binding = build_response_binding(participant_export=export, participant_response=_response())
    mutated = deepcopy(export)
    mutated["participant_payload"]["instruction"] += " changed"
    result = verify_response_binding(binding=binding, participant_export=mutated)
    assert result["state"] == "INVALID"
    assert "PARTICIPANT_EXPORT_INVALID" in result["reasons"]


def test_missing_response_field_fails_before_binding():
    response = _response()
    response.pop(REQUIRED_RESPONSE_FIELDS[0])
    with pytest.raises(ValueError, match="RESPONSE_CONTRACT_INVALID"):
        build_response_binding(participant_export=_export(), participant_response=response)


def test_unexpected_provider_or_execution_metadata_cannot_hide_inside_response():
    for field in ("provider_request_id", "execution_context_id", "delivery_receipt"):
        response = _response()
        response[field] = "invented"
        with pytest.raises(ValueError, match="UNEXPECTED_RESPONSE_FIELDS"):
            build_response_binding(participant_export=_export(), participant_response=response)


def test_binding_artifact_contains_no_external_execution_or_authenticity_surfaces():
    binding = build_response_binding(participant_export=_export(), participant_response=_response())
    serialized = repr(binding)
    for forbidden in (
        "provider_request_id", "provider_response_id", "execution_context_id",
        "delivery_receipt", "independence_attestation_ref", "external_authenticity",
    ):
        assert forbidden not in serialized


def test_build_rejects_invalid_or_tampered_export():
    export = _export()
    export["case_id"] = "XSP-IGT-02"
    with pytest.raises(ValueError, match="PARTICIPANT_EXPORT_INVALID"):
        build_response_binding(participant_export=export, participant_response=_response())


def test_binding_field_tamper_is_detected_against_same_export():
    export = _export()
    binding = build_response_binding(participant_export=export, participant_response=_response())
    binding["baseline_sha"] = "0" * 40
    result = verify_response_binding(binding=binding, participant_export=export)
    assert result["state"] == "INVALID"
    assert "BASELINE_SHA_MISMATCH" in result["reasons"]
    assert "BINDING_ID_MISMATCH" in result["reasons"]
    assert "BINDING_PACKAGE_DIGEST_MISMATCH" in result["reasons"]
