from copy import deepcopy

from experience_spine_igt import build_condition_payload
from experience_spine_igt_evidence_package import (
    SCHEMA_VERSION,
    detect_duplicate_identity,
    digest_value,
    package_digest,
    seal_package,
    validate_package,
)


BASELINE = "eea81fb5df6e2b532dc3b5edda1cbcf4c0da1f78"


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "task_id": "MODEL-RUN-PACKAGE-TEST",
        "execution_identity": "HERMUZ:test-source",
        "execution_context": {"consumer_route": "TEST"},
        "experience_items": [
            {
                "knowledge_id": "K-TEST-001",
                "pattern": "Inspect current evidence before applying historical guidance.",
                "knowledge_scope": "project:test",
                "lifecycle_state": "PROMOTED",
                "validation_state": "VALIDATED",
                "evidence": ["E-TEST-001"],
                "evidence_state": "PROVEN",
                "authority_state": "ADVISORY",
                "source_identity": "HERMUZ:prior",
                "source_type": "HERMUZ-ENGINEERING",
                "evidence_group": "EG-TEST-001",
                "consumer_routes": ["TEST"],
                "applicability_boundaries": ["release-operations"],
                "counterindications": [],
                "contradicts": [],
                "match_reasons": {"problem_types": ["authority-conflict"]},
                "score": 3,
            }
        ],
        "conflicts": [],
        "correlated_evidence_groups": [
            {
                "evidence_group": "EG-TEST-001",
                "knowledge_ids": ["K-TEST-001"],
                "independence": "CORRELATED_NOT_INDEPENDENT",
            }
        ],
        "excluded_summary": {},
        "reasoning_start": ["CURRENT_EVIDENCE", "APPLICABLE_AUTHORITY"],
        "authority_boundary": "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE",
        "evidence_boundary": "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
    }


def _response() -> dict:
    return {
        "prediction": "Use current evidence and preserve scope.",
        "identified_invariants": ["CURRENT_EVIDENCE_FIRST"],
        "selected_authority": "CURRENT_GATE",
        "scope": ["bounded-case"],
        "action": "inspect_before_action",
        "evidence_refs": ["CURRENT-EVIDENCE-1"],
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


def _package(condition: str, *, run_id: str = "RUN-PKG-001", context_id: str = "CTX-PKG-001") -> dict:
    payload = build_condition_payload(
        "XSP-IGT-01",
        condition,
        experience_packet=_experience_packet() if condition in {"L1", "L2"} else None,
    )
    package = {
        "schema_version": SCHEMA_VERSION,
        "package_id": f"PKG-{run_id}-{condition}",
        "run_id": run_id,
        "case_id": "XSP-IGT-01",
        "condition": condition,
        "participant_kind": "MODEL_RUN",
        "repository_baseline_sha": BASELINE,
        "execution_context_id": context_id,
        "source_model": "external-model-label",
        "source_instance_id": f"instance-{context_id}",
        "execution_surface": "external-independent-session",
        "execution_started_at": "2026-08-28T20:00:00Z",
        "execution_completed_at": "2026-08-28T20:00:30Z",
        "participant_payload": payload,
        "participant_response": _response(),
        "independence_attestation": _attestation(run_id, context_id),
        "participant_evidence_ref": f"external-evidence://{run_id}",
        "independence_attestation_ref": f"external-attestation://{run_id}",
    }
    return seal_package(package)


def test_sealing_is_deterministic_and_does_not_mutate_source():
    source = {
        "schema_version": SCHEMA_VERSION,
        "participant_payload": {"b": 2, "a": 1},
        "participant_response": {"z": [3, 2, 1]},
    }
    original = deepcopy(source)
    first = seal_package(source)
    second = seal_package(source)
    assert source == original
    assert first == second
    assert first["payload_digest"] == digest_value(source["participant_payload"])
    assert first["response_digest"] == digest_value(source["participant_response"])
    assert first["package_digest"] == package_digest(first)


def test_valid_b0_package_is_structurally_qualified_but_external_authenticity_unverified():
    result = validate_package(_package("B0"))
    assert result["state"] == "STRUCTURALLY_QUALIFIED"
    assert result["structural_validity"] == "PASS"
    assert result["internal_integrity"] == "PASS"
    assert result["external_authenticity"] == "UNVERIFIED"
    assert result["eligible_for_external_resolution"] is True
    assert result["authority"] == "NONE"
    assert result["cognitive_effect"] == "NOT_ESTABLISHED"


def test_valid_l1_package_has_no_authority_or_provenance_leak_and_qualifies():
    package = _package("L1")
    experience = package["participant_payload"]["experience_packet"]
    assert "authority_boundary" not in experience
    assert "evidence_boundary" not in experience
    assert "correlated_evidence_groups" not in experience
    item = experience["experience_items"][0]
    for field in (
        "evidence",
        "evidence_state",
        "authority_state",
        "source_identity",
        "source_type",
        "evidence_group",
        "consumer_routes",
    ):
        assert field not in item
    assert validate_package(package)["state"] == "STRUCTURALLY_QUALIFIED"


def test_valid_l2_package_contains_provenance_envelope_and_qualifies():
    package = _package("L2")
    payload = package["participant_payload"]
    assert "authority_boundary" not in payload["experience_packet"]
    assert payload["provenance_envelope"]["authority_boundary"] == "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE"
    assert payload["provenance_envelope"]["experience_items"][0]["source_identity"] == "HERMUZ:prior"
    assert validate_package(package)["state"] == "STRUCTURALLY_QUALIFIED"


def test_d07_l1_authority_boundary_leak_is_invalid_even_with_resealed_digests():
    package = _package("L1")
    package["participant_payload"]["experience_packet"]["authority_boundary"] = "LEAKED"
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "L1_AUTHORITY_BOUNDARY_LEAK" in result["reasons"]
    assert result["internal_integrity"] == "PASS"


def test_payload_tampering_after_seal_is_invalid_and_breaks_integrity():
    package = _package("B0")
    package["participant_payload"]["instruction"] = "tampered after seal"
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "PAYLOAD_DIGEST_MISMATCH" in result["reasons"]
    assert "PACKAGE_DIGEST_MISMATCH" in result["reasons"]
    assert result["internal_integrity"] == "FAIL"


def test_hidden_evaluator_key_contamination_is_invalid_even_when_resealed():
    package = _package("B0")
    package["participant_payload"]["hidden_expectation"] = {"correct_answer": "publish_now"}
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert any(reason.startswith("EVALUATOR_CONTAMINATION:") for reason in result["reasons"])
    assert result["external_authenticity"] == "UNVERIFIED"


def test_case_or_condition_identity_mismatch_is_invalid():
    package = _package("B0")
    package["participant_payload"]["case_id"] = "OTHER-CASE"
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "PAYLOAD_CASE_ID_MISMATCH" in result["reasons"]


def test_attestation_identity_mismatch_is_invalid():
    package = _package("B0")
    package["independence_attestation"]["execution_context_id"] = "OTHER-CONTEXT"
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "ATTESTATION_CONTEXT_ID_MISMATCH" in result["reasons"]


def test_unknown_independence_is_quarantined_not_promoted_to_invalid_or_qualified():
    package = _package("B0")
    package["independence_attestation"]["state_independence"] = "UNKNOWN"
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "QUARANTINED"
    assert "STATE_INDEPENDENCE_NOT_ESTABLISHED" in result["reasons"]
    assert result["structural_validity"] == "PASS"
    assert result["internal_integrity"] == "PASS"
    assert result["eligible_for_external_resolution"] is False


def test_missing_external_evidence_reference_is_quarantined():
    package = _package("B0")
    package["participant_evidence_ref"] = ""
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "QUARANTINED"
    assert "PARTICIPANT_EVIDENCE_REF_MISSING" in result["reasons"]
    assert result["external_authenticity"] == "UNVERIFIED"


def test_b0_rejects_experience_packet_contamination():
    package = _package("B0")
    package["participant_payload"]["experience_packet"] = {"status": "READY"}
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "B0_EXPERIENCE_PACKET_LEAK" in result["reasons"]


def test_l2_requires_provenance_envelope():
    package = _package("L2")
    package["participant_payload"].pop("provenance_envelope")
    package = seal_package(package)
    result = validate_package(package)
    assert result["state"] == "INVALID"
    assert "L2_PROVENANCE_ENVELOPE_MISSING" in result["reasons"]


def test_duplicate_package_or_run_identity_never_counts_as_independent_confirmation():
    one = _package("B0", run_id="RUN-DUP", context_id="CTX-DUP")
    two = deepcopy(one)
    result = detect_duplicate_identity([one, two])
    assert result["state"] == "DUPLICATE_IDENTITY_DETECTED"
    assert one["package_id"] in result["duplicate_package_ids"]
    assert result["duplicate_run_keys"] == [("RUN-DUP", "XSP-IGT-01", "B0", "CTX-DUP")]
    assert result["independent_confirmation"] == "NOT_ESTABLISHED_BY_MULTIPLICITY"


def test_distinct_package_id_but_same_run_identity_is_still_duplicate_run_evidence():
    one = _package("B0", run_id="RUN-SAME", context_id="CTX-SAME")
    two = deepcopy(one)
    two["package_id"] = "PKG-DIFFERENT-NAME"
    two = seal_package(two)
    result = detect_duplicate_identity([one, two])
    assert result["duplicate_package_ids"] == []
    assert result["duplicate_run_keys"] == [("RUN-SAME", "XSP-IGT-01", "B0", "CTX-SAME")]
    assert result["state"] == "DUPLICATE_IDENTITY_DETECTED"
