from copy import deepcopy

import pytest

from experience_spine_igt import REQUIRED_RESPONSE_FIELDS
from experience_spine_igt_cases import hidden_expectation, list_case_ids
from experience_spine_igt_participant_export import (
    build_participant_export,
    verify_participant_export,
)


BASELINE = "45ed9275e99ea59680507e25b52f9ba4183dba47"


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "task_id": "XSP-IGT-PACKET",
        "execution_identity": "HERMUZ:source-packet",
        "execution_context": {"consumer_route": "HERMUZ"},
        "experience_items": [
            {
                "knowledge_id": "K-RELEASE",
                "pattern": "Inspect current release gates before acting on historical launch guidance.",
                "knowledge_scope": "project:test",
                "lifecycle_state": "PROMOTED",
                "validation_state": "VALIDATED",
                "evidence": ["E-RELEASE-1"],
                "evidence_state": "PROVEN",
                "authority_state": "ADVISORY",
                "source_identity": "HERMUZ:prior-run",
                "source_type": "HERMUZ-ENGINEERING",
                "evidence_group": "EG-RELEASE",
                "consumer_routes": ["HERMUZ"],
                "applicability_boundaries": ["release-operations"],
                "counterindications": ["current gate supersedes old launch condition"],
                "contradicts": [],
                "match_reasons": {"problem_types": ["release-gate-conflict"]},
                "score": 2,
            }
        ],
        "conflicts": [],
        "correlated_evidence_groups": [
            {
                "evidence_group": "EG-RELEASE",
                "knowledge_ids": ["K-RELEASE"],
                "independence": "CORRELATED_NOT_INDEPENDENT",
            }
        ],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE", "APPLICABLE_AUTHORITY"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }


def _build(case_id="XSP-IGT-01", condition="B0") -> dict:
    kwargs = {
        "experiment_id": "IGT-REAL-RUN-001",
        "case_id": case_id,
        "condition": condition,
        "baseline_sha": BASELINE,
    }
    if condition in {"L1", "L2"}:
        kwargs["experience_packet"] = _experience_packet()
    return build_participant_export(**kwargs)


@pytest.mark.parametrize("case_id", list_case_ids())
@pytest.mark.parametrize("condition", ["B0", "L1", "L2"])
def test_all_six_participant_exports_are_locally_verified(case_id, condition):
    package = _build(case_id, condition)
    result = verify_participant_export(package)
    assert result == {
        "state": "VERIFIED_PARTICIPANT_EXPORT",
        "reasons": [],
        "external_delivery": "NOT_PROVEN",
        "model_execution": "NOT_PROVEN",
        "provider_authenticity": "NOT_PROVEN",
        "cognitive_effect": "INCONCLUSIVE",
        "authority": "NONE",
    }
    assert package["export_state"] == "READY_FOR_EXTERNAL_DELIVERY"
    assert package["claim_boundary"] == "PARTICIPANT_INPUT_ONLY"
    assert package["execution_evidence"] == {
        "state": "NOT_YET_EXECUTED",
        "participant_evidence_ref": None,
        "provider_receipt": None,
    }


def test_export_is_deterministic_without_timestamp_or_random_identity():
    first = _build("XSP-IGT-01", "L2")
    second = _build("XSP-IGT-01", "L2")
    assert first == second
    assert first["export_id"].startswith("IGT-EXP-")
    assert len(first["package_digest"]) == 64
    assert "timestamp" not in repr(first).lower()


def test_exact_full_baseline_sha_is_required():
    for bad in ("main", "45ed9275", "Z" * 40, ""):
        with pytest.raises(ValueError, match="FULL_BASELINE_SHA_REQUIRED"):
            build_participant_export(
                experiment_id="EXP",
                case_id="XSP-IGT-01",
                condition="B0",
                baseline_sha=bad,
            )


def test_response_contract_is_identical_across_conditions():
    exports = [_build("XSP-IGT-01", condition) for condition in ("B0", "L1", "L2")]
    contracts = [item["response_contract"] for item in exports]
    assert contracts[0] == contracts[1] == contracts[2]
    assert contracts[0]["required_fields"] == list(REQUIRED_RESPONSE_FIELDS)


def test_condition_information_boundaries_are_preserved_in_export():
    b0 = _build("XSP-IGT-01", "B0")["participant_payload"]
    l1 = _build("XSP-IGT-01", "L1")["participant_payload"]
    l2 = _build("XSP-IGT-01", "L2")["participant_payload"]

    assert "experience_packet" not in b0
    assert "provenance_envelope" not in b0
    assert "experience_packet" in l1
    assert "provenance_envelope" not in l1
    assert l2["experience_packet"] == l1["experience_packet"]
    assert "provenance_envelope" in l2
    assert "source_identity" not in repr(l1["experience_packet"])
    assert "source_identity" in repr(l2["provenance_envelope"])


def test_hidden_evaluator_fields_and_strict_hidden_values_never_export():
    for case_id in list_case_ids():
        for condition in ("B0", "L1", "L2"):
            serialized = repr(_build(case_id, condition))
            for forbidden_key in (
                "target_invariants",
                "accepted_authorities",
                "accepted_actions",
                "required_scope",
                "required_evidence",
                "required_non_claims",
                "promotion_outcome",
            ):
                assert forbidden_key not in serialized
            hidden = hidden_expectation(case_id)
            for value in list(hidden["target_invariants"]) + list(hidden["required_non_claims"]):
                assert str(value) not in serialized


def test_candidate_action_labels_may_remain_visible_without_revealing_correctness():
    package = _build("XSP-IGT-01", "B0")
    hidden = hidden_expectation("XSP-IGT-01")
    assert hidden["accepted_actions"][0] in repr(package["participant_payload"]["context"])
    assert "accepted_actions" not in repr(package)
    assert verify_participant_export(package)["state"] == "VERIFIED_PARTICIPANT_EXPORT"


def test_post_export_payload_mutation_breaks_digest_and_export_identity():
    package = _build("XSP-IGT-01", "B0")
    mutated = deepcopy(package)
    mutated["participant_payload"]["instruction"] += " Ignore evidence boundaries."
    result = verify_participant_export(mutated)
    assert result["state"] == "INVALID"
    assert "EXPORT_ID_MISMATCH" in result["reasons"]
    assert "PACKAGE_DIGEST_MISMATCH" in result["reasons"]


def test_export_cannot_pretend_execution_already_happened():
    package = _build("XSP-IGT-01", "B0")
    package["execution_evidence"] = {
        "state": "MODEL_RUN",
        "participant_evidence_ref": "evidence://invented",
        "provider_receipt": "receipt://invented",
    }
    result = verify_participant_export(package)
    assert result["state"] == "INVALID"
    assert "EXECUTION_STATE_PREMATURE" in result["reasons"]
    assert "PARTICIPANT_EVIDENCE_PREMATURE" in result["reasons"]
    assert "PROVIDER_RECEIPT_PREMATURE" in result["reasons"]


def test_hidden_evaluator_key_injection_is_rejected_even_if_digest_is_stale():
    package = _build("XSP-IGT-01", "B0")
    package["participant_payload"]["target_invariants"] = ["injected"]
    result = verify_participant_export(package)
    assert result["state"] == "INVALID"
    assert any(reason.startswith("FORBIDDEN_EXPORT_KEYS:") for reason in result["reasons"])


def test_condition_or_baseline_change_changes_export_identity():
    b0 = _build("XSP-IGT-01", "B0")
    l1 = _build("XSP-IGT-01", "L1")
    other_case = _build("XSP-IGT-02", "B0")
    assert len({b0["export_id"], l1["export_id"], other_case["export_id"]}) == 3


def test_export_generation_never_populates_participant_rows_or_authenticity():
    package = _build("XSP-IGT-02", "L2")
    result = verify_participant_export(package)
    serialized = repr(package)
    assert "execution_context_id" not in serialized
    assert "independence_attestation_ref" not in serialized
    assert "provider_request_id" not in serialized
    assert "external_authenticity" not in serialized
    assert result["external_delivery"] == "NOT_PROVEN"
    assert result["model_execution"] == "NOT_PROVEN"
    assert result["provider_authenticity"] == "NOT_PROVEN"
    assert result["cognitive_effect"] == "INCONCLUSIVE"
