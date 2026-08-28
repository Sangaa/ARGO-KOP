from copy import deepcopy

import pytest

from experience_spine_igt_evidence_package import SCHEMA_VERSION, seal_package
from experience_spine_igt_participant_export import build_participant_export
from experience_spine_igt_response_binding import build_response_binding
from experience_spine_igt_binding_evidence_admission import (
    ADMISSION_STATE,
    verify_binding_aware_evidence_admission,
)

BASELINE = "6a1e7f1f80d04b00ac6c2601964c3821ce0bbe9c"


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "task_id": "XSP-IGT-ADMISSION-PACKET",
        "execution_identity": "HERMUZ:admission-source",
        "execution_context": {"consumer_route": "HERMUZ"},
        "experience_items": [{
            "knowledge_id": "K-ADMISSION",
            "pattern": "Prefer current governed evidence over historical assumptions.",
            "knowledge_scope": "project:test",
            "lifecycle_state": "PROMOTED",
            "validation_state": "VALIDATED",
            "evidence": ["E-ADMISSION-1"],
            "evidence_state": "PROVEN",
            "authority_state": "ADVISORY",
            "source_identity": "HERMUZ:prior-run",
            "source_type": "HERMUZ-ENGINEERING",
            "evidence_group": "EG-ADMISSION",
            "consumer_routes": ["HERMUZ"],
            "applicability_boundaries": ["admission-test"],
            "counterindications": [],
            "contradicts": [],
            "match_reasons": {"problem_types": ["cross-artifact-correlation"]},
            "score": 1,
        }],
        "conflicts": [],
        "correlated_evidence_groups": [],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }


def _response() -> dict:
    return {
        "prediction": "Use the current governed evidence.",
        "identified_invariants": ["CURRENT_EVIDENCE"],
        "selected_authority": "CURRENT_CANONICAL_STATE",
        "scope": ["project:test"],
        "action": "REVALIDATE",
        "evidence_refs": ["E-ADMISSION-1"],
        "non_claims": ["NO_PROVIDER_AUTHENTICITY_CLAIM"],
    }


def _export(condition="B0") -> dict:
    kwargs = {
        "experiment_id": "IGT-ADMISSION-001",
        "case_id": "XSP-IGT-01",
        "condition": condition,
        "baseline_sha": BASELINE,
    }
    if condition in {"L1", "L2"}:
        kwargs["experience_packet"] = _experience_packet()
    return build_participant_export(**kwargs)


def _binding(export: dict, response: dict | None = None) -> dict:
    return build_response_binding(
        participant_export=export,
        participant_response=response or _response(),
    )


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


def _package(export: dict, binding: dict, *, run_id="RUN-ADMIT-001", context_id="CTX-ADMIT-001") -> dict:
    package = {
        "schema_version": SCHEMA_VERSION,
        "package_id": f"PKG-{run_id}-{export['condition']}",
        "run_id": run_id,
        "case_id": export["case_id"],
        "condition": export["condition"],
        "participant_kind": "MODEL_RUN",
        "repository_baseline_sha": export["baseline_sha"],
        "execution_context_id": context_id,
        "source_model": "external-model-label",
        "source_instance_id": f"instance-{context_id}",
        "execution_surface": "external-independent-session",
        "execution_started_at": "2026-08-29T00:00:00Z",
        "execution_completed_at": "2026-08-29T00:00:30Z",
        "participant_payload": deepcopy(export["participant_payload"]),
        "participant_response": deepcopy(binding["participant_response"]),
        "independence_attestation": _attestation(run_id, context_id),
        "participant_evidence_ref": f"external-evidence://{run_id}",
        "independence_attestation_ref": f"external-attestation://{run_id}",
    }
    return seal_package(package)


@pytest.mark.parametrize("condition", ["B0", "L1", "L2"])
def test_valid_correlated_chain_is_admitted_without_authenticity_promotion(condition):
    export = _export(condition)
    binding = _binding(export)
    package = _package(export, binding)
    result = verify_binding_aware_evidence_admission(
        participant_export=export,
        response_binding=binding,
        evidence_package=package,
    )
    assert result["state"] == ADMISSION_STATE
    assert result["correlation"] == "PASS"
    assert result["export_verification"] == "VERIFIED_PARTICIPANT_EXPORT"
    assert result["binding_verification"] == "VERIFIED_LOCAL_BINDING"
    assert result["package_verification"] == "STRUCTURALLY_QUALIFIED"
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution"] == "NOT_AUTHENTICATED_BY_CORRELATION"
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["authority"] == "NONE"
    assert result["cognitive_effect"] == "NOT_ESTABLISHED"


def test_valid_package_with_different_response_is_rejected_even_if_resealed():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    package["participant_response"]["action"] = "DIFFERENT_BUT_STRUCTURALLY_VALID"
    package = seal_package(package)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "PACKAGE_RESPONSE_BINDING_MISMATCH" in result["reasons"]
    assert "PACKAGE_RESPONSE_DIGEST_BINDING_MISMATCH" in result["reasons"]


def test_valid_package_with_different_payload_is_rejected_even_if_resealed():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    package["participant_payload"]["instruction"] += " additional participant-visible text"
    package = seal_package(package)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "PACKAGE_PAYLOAD_EXPORT_MISMATCH" in result["reasons"]
    assert "PACKAGE_PAYLOAD_DIGEST_EXPORT_MISMATCH" in result["reasons"]


def test_package_from_other_condition_cannot_be_admitted_against_binding():
    export = _export("B0")
    binding = _binding(export)
    other_export = _export("L1")
    other_binding = _binding(other_export)
    package = _package(other_export, other_binding)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "PACKAGE_PAYLOAD_EXPORT_MISMATCH" in result["reasons"]
    assert "PACKAGE_CONDITION_EXPORT_MISMATCH" in result["reasons"]


def test_tampered_binding_is_rejected_before_correlation():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    binding["baseline_sha"] = "0" * 40
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "RESPONSE_BINDING_INVALID" in result["reasons"]


def test_tampered_export_is_rejected_before_correlation():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    export["participant_payload"]["instruction"] += " changed"
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "PARTICIPANT_EXPORT_INVALID" in result["reasons"]


def test_quarantined_package_is_not_admitted_even_when_payload_response_correlate():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    package["independence_attestation"]["state_independence"] = "UNKNOWN"
    package = seal_package(package)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "EVIDENCE_PACKAGE_NOT_STRUCTURALLY_QUALIFIED" in result["reasons"]
    assert result["package_verification"] == "QUARANTINED"


def test_invalid_package_is_not_admitted_even_when_response_matches():
    export = _export()
    binding = _binding(export)
    package = _package(export, binding)
    package["participant_payload"]["hidden_expectation"] = {"correct_answer": "x"}
    package = seal_package(package)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == "INVALID"
    assert "EVIDENCE_PACKAGE_NOT_STRUCTURALLY_QUALIFIED" in result["reasons"]
    assert result["package_verification"] == "INVALID"


def test_correlation_never_upgrades_provider_or_execution_authenticity():
    export = _export("L2")
    binding = _binding(export)
    package = _package(export, binding)
    result = verify_binding_aware_evidence_admission(
        participant_export=export, response_binding=binding, evidence_package=package
    )
    assert result["state"] == ADMISSION_STATE
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution"] == "NOT_AUTHENTICATED_BY_CORRELATION"
    assert result["provider_authenticity"] == "UNVERIFIED"
    assert result["independence"] == "REQUIRES_EXISTING_PACKAGE_ATTESTATION_AND_EXTERNAL_RESOLUTION"


def test_non_mapping_inputs_fail_closed():
    result = verify_binding_aware_evidence_admission(
        participant_export=None, response_binding=None, evidence_package=None
    )
    assert result["state"] == "INVALID"
    assert "PARTICIPANT_EXPORT_NOT_MAPPING" in result["reasons"]
    assert "RESPONSE_BINDING_NOT_MAPPING" in result["reasons"]
    assert "EVIDENCE_PACKAGE_NOT_MAPPING" in result["reasons"]
