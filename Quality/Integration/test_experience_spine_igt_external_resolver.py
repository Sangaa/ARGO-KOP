from copy import deepcopy

from experience_spine_igt import build_condition_payload
from experience_spine_igt_evidence_package import SCHEMA_VERSION, digest_value, seal_package
from experience_spine_igt_external_resolver import (
    bind_resolver_receipt,
    correlate_attestation_observation,
    correlate_external_evidence,
    correlate_participant_observation,
    detect_duplicate_resolution_identity,
    evidence_fingerprint,
    observation_digest,
)


BASELINE = "069c7c0b4103c745e40c6b2aa54f47816b560418"


def _experience_packet() -> dict:
    return {
        "status": "READY",
        "experience_items": [
            {
                "knowledge_id": "K-RESOLVE-1",
                "pattern": "Prefer current evidence over historical guidance.",
                "knowledge_scope": "project:resolver-test",
                "lifecycle_state": "PROMOTED",
                "validation_state": "VALIDATED",
                "evidence": ["E-RESOLVE-1"],
                "evidence_state": "PROVEN",
                "authority_state": "ADVISORY",
                "source_identity": "HERMUZ:prior",
                "source_type": "HERMUZ-ENGINEERING",
                "evidence_group": "EG-RESOLVE",
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


def _package(condition: str = "L2", *, run_id: str = "RUN-EXT-1", context_id: str = "CTX-EXT-1") -> dict:
    payload = build_condition_payload(
        "XSP-IGT-01",
        condition,
        experience_packet=_experience_packet() if condition in {"L1", "L2"} else None,
    )
    return seal_package(
        {
            "schema_version": SCHEMA_VERSION,
            "package_id": f"PKG-{run_id}-{condition}",
            "run_id": run_id,
            "case_id": "XSP-IGT-01",
            "condition": condition,
            "participant_kind": "MODEL_RUN",
            "repository_baseline_sha": BASELINE,
            "execution_context_id": context_id,
            "source_model": "provider/model-v1",
            "source_instance_id": f"instance-{context_id}",
            "execution_surface": "external-provider-run",
            "execution_started_at": "2026-08-28T21:00:00Z",
            "execution_completed_at": "2026-08-28T21:00:25Z",
            "participant_payload": payload,
            "participant_response": _response(),
            "independence_attestation": _attestation(run_id, context_id),
            "participant_evidence_ref": f"provider://execution/{run_id}",
            "independence_attestation_ref": f"provider://attestation/{run_id}",
        }
    )


def _participant_observation(package: dict, *, status: str = "FOUND") -> dict:
    observation = {
        "status": status,
        "resolver_id": "resolver-adapter-A",
        "resolution_id": f"RES-P-{package['run_id']}",
        "requested_ref": package["participant_evidence_ref"],
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
    if status == "UNAVAILABLE":
        observation["observed_ref"] = None
    return observation


def _attestation_observation(package: dict, *, status: str = "FOUND") -> dict:
    observation = {
        "status": status,
        "resolver_id": "resolver-adapter-B",
        "resolution_id": f"RES-A-{package['run_id']}",
        "requested_ref": package["independence_attestation_ref"],
        "observed_ref": package["independence_attestation_ref"],
        "run_id": package["run_id"],
        "execution_context_id": package["execution_context_id"],
        "repository_baseline_sha": package["repository_baseline_sha"],
        "attestation_digest": digest_value(package["independence_attestation"]),
        "attestation_content": deepcopy(package["independence_attestation"]),
    }
    if status == "UNAVAILABLE":
        observation["observed_ref"] = None
    return observation


def _receipt(observation: dict) -> dict:
    return {
        "resolver_id": observation["resolver_id"],
        "resolution_id": observation["resolution_id"],
        "source_ref": observation["observed_ref"],
        "observation_digest": observation_digest(observation),
    }


def test_exact_participant_observation_correlates_to_package_identity_and_digests():
    package = _package()
    result = correlate_participant_observation(package, _participant_observation(package))
    assert result["state"] == "CORRELATED"
    assert result["reasons"] == []
    assert result["observation_digest"]
    assert result["evidence_fingerprint"]


def test_exact_attestation_observation_correlates_to_embedded_attestation():
    package = _package()
    result = correlate_attestation_observation(package, _attestation_observation(package))
    assert result["state"] == "CORRELATED"
    assert result["reasons"] == []


def test_matching_observations_without_receipts_remain_correlated_untrusted():
    package = _package()
    result = correlate_external_evidence(
        package,
        participant_observation=_participant_observation(package),
        attestation_observation=_attestation_observation(package),
    )
    assert result["state"] == "CORRELATED_UNTRUSTED"
    assert result["external_authenticity"] == "INCONCLUSIVE"
    assert result["production_trusted_adapter"] == "NOT_ESTABLISHED"
    assert result["authority"] == "NONE"
    assert result["cognitive_effect"] == "NOT_ESTABLISHED"


def test_even_bound_receipts_cannot_make_pure_correlation_externally_verified():
    package = _package()
    participant = _participant_observation(package)
    attestation = _attestation_observation(package)
    result = correlate_external_evidence(
        package,
        participant_observation=participant,
        attestation_observation=attestation,
        participant_receipt=_receipt(participant),
        attestation_receipt=_receipt(attestation),
    )
    assert result["participant_receipt"]["state"] == "RECEIPT_BOUND"
    assert result["attestation_receipt"]["state"] == "RECEIPT_BOUND"
    assert result["state"] == "CORRELATED_AWAITING_TRUSTED_ADAPTER"
    assert result["external_authenticity"] == "INCONCLUSIVE"
    assert result["production_trusted_adapter"] == "NOT_ESTABLISHED"
    assert "VERIFIED" not in result["state"]


def test_payload_digest_mismatch_is_direct_external_evidence_mismatch():
    package = _package()
    participant = _participant_observation(package)
    participant["payload_digest"] = "0" * 64
    result = correlate_external_evidence(
        package,
        participant_observation=participant,
        attestation_observation=_attestation_observation(package),
    )
    assert result["state"] == "EXTERNAL_EVIDENCE_MISMATCH"
    assert result["external_authenticity"] == "MISMATCH"
    assert "PAYLOAD_DIGEST_MISMATCH" in result["participant"]["reasons"]


def test_source_model_mismatch_is_not_hidden_by_matching_run_id():
    package = _package()
    participant = _participant_observation(package)
    participant["source_model"] = "other/provider-model"
    result = correlate_participant_observation(package, participant)
    assert result["state"] == "MISMATCH"
    assert "SOURCE_MODEL_MISMATCH" in result["reasons"]


def test_execution_surface_or_time_mismatch_is_direct_mismatch():
    package = _package()
    participant = _participant_observation(package)
    participant["execution_surface"] = "other-surface"
    participant["execution_started_at"] = "2026-08-28T22:00:00Z"
    result = correlate_participant_observation(package, participant)
    assert result["state"] == "MISMATCH"
    assert "EXECUTION_SURFACE_MISMATCH" in result["reasons"]
    assert "EXECUTION_STARTED_AT_MISMATCH" in result["reasons"]


def test_attestation_digest_mismatch_is_direct_mismatch():
    package = _package()
    observation = _attestation_observation(package)
    observation["attestation_digest"] = "f" * 64
    result = correlate_attestation_observation(package, observation)
    assert result["state"] == "MISMATCH"
    assert "ATTESTATION_DIGEST_MISMATCH" in result["reasons"]


def test_attestation_content_mismatch_is_not_hidden_by_matching_digest_field():
    package = _package()
    observation = _attestation_observation(package)
    observation["attestation_content"]["state_independence"] = "NO"
    result = correlate_attestation_observation(package, observation)
    assert result["state"] == "MISMATCH"
    assert "ATTESTATION_CONTENT_MISMATCH" in result["reasons"]


def test_requested_reference_mismatch_is_direct_mismatch_before_content_comparison():
    package = _package()
    observation = _participant_observation(package)
    observation["requested_ref"] = "provider://execution/OTHER"
    result = correlate_participant_observation(package, observation)
    assert result == {
        "state": "MISMATCH",
        "reasons": ["REQUESTED_REF_MISMATCH"],
        "kind": "PARTICIPANT",
    }


def test_unavailable_evidence_is_not_misclassified_as_mismatch_but_has_resolver_identity():
    package = _package()
    participant = _participant_observation(package, status="UNAVAILABLE")
    result = correlate_external_evidence(
        package,
        participant_observation=participant,
        attestation_observation=_attestation_observation(package),
    )
    assert result["participant"]["state"] == "UNAVAILABLE"
    assert result["state"] == "EXTERNAL_EVIDENCE_UNAVAILABLE"
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_unavailable_without_resolution_identity_is_mismatch_of_resolver_event_not_absence_proof():
    package = _package()
    participant = _participant_observation(package, status="UNAVAILABLE")
    participant["resolution_id"] = ""
    result = correlate_participant_observation(package, participant)
    assert result["state"] == "MISMATCH"
    assert "RESOLUTION_ID_MISSING" in result["reasons"]


def test_partial_observation_is_inconclusive_not_mismatch():
    package = _package()
    participant = _participant_observation(package, status="PARTIAL")
    result = correlate_external_evidence(
        package,
        participant_observation=participant,
        attestation_observation=_attestation_observation(package),
    )
    assert result["participant"]["state"] == "INCONCLUSIVE"
    assert result["state"] == "EXTERNAL_EVIDENCE_INCONCLUSIVE"
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_receipt_binding_detects_resolution_or_observation_digest_mismatch():
    package = _package()
    observation = _participant_observation(package)
    receipt = _receipt(observation)
    receipt["resolution_id"] = "OTHER-RESOLUTION"
    result = bind_resolver_receipt(observation, receipt)
    assert result["state"] == "RECEIPT_MISMATCH"
    assert "RECEIPT_RESOLUTION_ID_MISMATCH" in result["reasons"]
    assert result["resolver_trust"] == "UNAUTHENTICATED_BY_PURE_CORRELATION"


def test_structurally_invalid_package_is_not_eligible_for_external_correlation():
    package = _package()
    package["participant_payload"]["hidden_expectation"] = {"correct_answer": "x"}
    package = seal_package(package)
    result = correlate_external_evidence(
        package,
        participant_observation=_participant_observation(package),
        attestation_observation=_attestation_observation(package),
    )
    assert result["state"] == "PACKAGE_NOT_ELIGIBLE"
    assert result["package_state"] == "INVALID"
    assert result["external_authenticity"] == "INCONCLUSIVE"


def test_quarantined_package_is_not_eligible_for_external_correlation():
    package = _package()
    package["participant_evidence_ref"] = ""
    package = seal_package(package)
    result = correlate_external_evidence(
        package,
        participant_observation={},
        attestation_observation={},
    )
    assert result["state"] == "PACKAGE_NOT_ELIGIBLE"
    assert result["package_state"] == "QUARANTINED"


def test_duplicate_resolution_record_does_not_create_independent_corroboration():
    package = _package()
    one = _participant_observation(package)
    two = deepcopy(one)
    result = detect_duplicate_resolution_identity([one, two])
    assert result["state"] == "DUPLICATE_RESOLUTION_EVIDENCE"
    assert result["duplicate_resolution_ids"] == [(one["resolver_id"], one["resolution_id"])]
    assert result["duplicate_observation_digests"] == [observation_digest(one)]
    assert result["duplicate_evidence_fingerprints"] == [evidence_fingerprint(one)]
    assert result["independent_corroboration"] == "NOT_ESTABLISHED_BY_DUPLICATION"


def test_resolution_id_churn_cannot_turn_same_evidence_into_corroboration():
    package = _package()
    one = _participant_observation(package)
    two = deepcopy(one)
    two["resolution_id"] = "RES-DIFFERENT"
    result = detect_duplicate_resolution_identity([one, two])
    assert result["duplicate_resolution_ids"] == []
    assert result["duplicate_observation_digests"] == []
    assert result["duplicate_evidence_fingerprints"] == [evidence_fingerprint(one)]
    assert result["state"] == "DUPLICATE_RESOLUTION_EVIDENCE"
    assert result["independent_corroboration"] == "NOT_ESTABLISHED_BY_DUPLICATION"


def test_different_resolver_metadata_does_not_change_underlying_evidence_fingerprint():
    package = _package()
    one = _participant_observation(package)
    two = deepcopy(one)
    two["resolver_id"] = "resolver-adapter-C"
    two["resolution_id"] = "RES-OTHER"
    assert observation_digest(one) != observation_digest(two)
    assert evidence_fingerprint(one) == evidence_fingerprint(two)
