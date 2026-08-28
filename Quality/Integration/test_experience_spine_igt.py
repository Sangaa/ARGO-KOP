from experience_spine_igt import (
    bounded_transfer_readiness,
    build_condition_payload,
    compare_conditions,
    evaluate_run,
    qualify_run,
    score_response,
    validate_case_separation,
)
from experience_spine_igt_cases import hidden_expectation, list_case_ids, participant_case


def _perfect_response(case_id: str) -> dict:
    expected = hidden_expectation(case_id)
    return {
        "prediction": "Current evidence and applicable authority should control the next bounded action.",
        "identified_invariants": expected["target_invariants"],
        "selected_authority": expected["accepted_authorities"][0],
        "scope": expected["required_scope"],
        "action": expected["accepted_actions"][0],
        "evidence_refs": expected["required_evidence"],
        "non_claims": expected["required_non_claims"],
    }


def _qualified_run(case_id: str, condition: str, *, run_id: str, context_id: str, participant_kind="MODEL_RUN") -> dict:
    return {
        "run_id": run_id,
        "case_id": case_id,
        "condition": condition,
        "participant_kind": participant_kind,
        "execution_context_id": context_id,
        "baseline_sha": "a4cc96203b689338a50b7233b46c15eae8449f5a",
        "execution_independence": "YES",
        "information_independence": "YES",
        "state_independence": "YES",
        "temporal_independence": "YES",
        "mutation_independence": "YES",
        "source_conclusion_withheld": "YES",
        "leakage_detected": "NO",
        "response": _perfect_response(case_id),
    }


def test_cases_are_materially_renamed_away_from_source_workstream_objects():
    serialized = repr([participant_case(case_id) for case_id in list_case_ids()])
    for forbidden in ("REL-009", "RUN-010", "SRV-009", "REP-014", "P4-C12"):
        assert forbidden not in serialized
    assert set(list_case_ids()) == {"XSP-IGT-01", "XSP-IGT-02"}


def test_hidden_expectations_are_not_present_in_participant_case():
    for case_id in list_case_ids():
        separation = validate_case_separation(case_id)
        assert separation == {
            "case_id": case_id,
            "separation": "PASS",
            "leaked_hidden_values": [],
        }


def test_b0_l1_l2_payloads_preserve_condition_boundaries_without_hidden_answer():
    packet = {"status": "READY", "experience_items": [{"knowledge_id": "K-RELEASE"}]}
    provenance = {"evidence_groups": ["EG-1"], "authority_boundary": "ADVISORY"}

    b0 = build_condition_payload("XSP-IGT-01", "B0")
    l1 = build_condition_payload("XSP-IGT-01", "L1", experience_packet=packet)
    l2 = build_condition_payload(
        "XSP-IGT-01", "L2", experience_packet=packet, provenance_envelope=provenance
    )

    assert "experience_packet" not in b0
    assert "provenance_envelope" not in b0
    assert l1["experience_packet"] == packet
    assert "provenance_envelope" not in l1
    assert l2["experience_packet"] == packet
    assert l2["provenance_envelope"] == provenance

    hidden = hidden_expectation("XSP-IGT-01")
    for payload in (b0, l1, l2):
        visible = repr(payload)
        assert hidden["accepted_authorities"][0] not in visible
        assert hidden["accepted_actions"][0] not in visible
        for invariant in hidden["target_invariants"]:
            assert invariant not in visible


def test_l1_and_l2_require_their_declared_information_surfaces():
    try:
        build_condition_payload("XSP-IGT-01", "L1")
    except ValueError as exc:
        assert str(exc) == "EXPERIENCE_PACKET_REQUIRED"
    else:
        raise AssertionError("L1 accepted missing experience packet")

    try:
        build_condition_payload("XSP-IGT-01", "L2", experience_packet={})
    except ValueError as exc:
        assert str(exc) == "PROVENANCE_ENVELOPE_REQUIRED"
    else:
        raise AssertionError("L2 accepted missing provenance envelope")


def test_scoring_uses_all_six_igt_dimensions_and_requires_full_fidelity():
    result = score_response("XSP-IGT-01", _perfect_response("XSP-IGT-01"))
    assert result["status"] == "PASS"
    assert result["score"] == 6
    assert result["max_score"] == 6
    assert set(result["dimensions"].values()) == {1}

    degraded = _perfect_response("XSP-IGT-01")
    degraded["action"] = "publish_now"
    degraded["non_claims"] = []
    failed = score_response("XSP-IGT-01", degraded)
    assert failed["status"] == "FAIL"
    assert failed["dimensions"]["action_selection"] == 0
    assert failed["dimensions"]["explanation_fidelity"] == 0


def test_unknown_or_negative_independence_quarantines_evidence():
    run = _qualified_run("XSP-IGT-01", "B0", run_id="R1", context_id="CTX-1")
    run["state_independence"] = "UNKNOWN"
    result = qualify_run(run)
    assert result["evidence_state"] == "QUARANTINED"
    assert result["independence_result"] == "INCONCLUSIVE"
    assert result["promotion_outcome"] == "INCONCLUSIVE"
    assert "STATE_INDEPENDENCE_UNKNOWN" in result["reasons"]


def test_leakage_or_missing_baseline_quarantines_even_a_perfect_response():
    run = _qualified_run("XSP-IGT-01", "L1", run_id="R2", context_id="CTX-2")
    run["baseline_sha"] = ""
    run["leakage_detected"] = "YES"
    evaluated = evaluate_run(run)
    assert evaluated["scoring"]["status"] == "PASS"
    assert evaluated["qualification"]["evidence_state"] == "QUARANTINED"
    assert evaluated["invariant_transfer"] == "INCONCLUSIVE"
    assert evaluated["cognitive_effect_claim"] == "NOT_ESTABLISHED_BY_SINGLE_RUN_EVALUATOR"


def test_qualified_run_can_record_bounded_case_transfer_without_granting_authority():
    run = _qualified_run("XSP-IGT-02", "L2", run_id="R3", context_id="CTX-3")
    evaluated = evaluate_run(run)
    assert evaluated["qualification"]["evidence_state"] == "QUALIFIED"
    assert evaluated["scoring"]["status"] == "PASS"
    assert evaluated["invariant_transfer"] == "PASS"
    assert evaluated["authority"] == "NONE"
    assert evaluated["cognitive_effect_claim"] == "NOT_ESTABLISHED_BY_SINGLE_RUN_EVALUATOR"


def test_condition_comparison_is_descriptive_and_never_declares_causal_improvement():
    b0 = _qualified_run("XSP-IGT-01", "B0", run_id="B0", context_id="CTX-B0")
    l1 = _qualified_run("XSP-IGT-01", "L1", run_id="L1", context_id="CTX-L1")
    l2 = _qualified_run("XSP-IGT-01", "L2", run_id="L2", context_id="CTX-L2")

    b0["response"]["action"] = "publish_now"
    b0["response"]["non_claims"] = []
    result = compare_conditions([evaluate_run(b0), evaluate_run(l1), evaluate_run(l2)])

    assert result["comparisons"][0]["L1_minus_B0"] > 0
    assert result["comparisons"][0]["L2_minus_L1"] == 0
    assert result["cognitive_effect"] == "INCONCLUSIVE_WITHOUT_QUALIFIED_INDEPENDENT_MODEL_RUN_DESIGN"
    assert "descriptive" in result["interpretation_boundary"].lower()


def test_python_fixtures_do_not_satisfy_independent_model_evidence_readiness():
    runs = [
        _qualified_run("XSP-IGT-01", "L1", run_id="F1", context_id="CTX-A", participant_kind="FIXTURE"),
        _qualified_run("XSP-IGT-02", "L1", run_id="F2", context_id="CTX-B", participant_kind="FIXTURE"),
    ]
    readiness = bounded_transfer_readiness([evaluate_run(run) for run in runs])
    assert readiness["status"] == "INSUFFICIENT_INDEPENDENT_MODEL_EVIDENCE"
    assert readiness["qualified_model_runs"] == 0
    assert readiness["promotion"] == "NONE"


def test_readiness_requires_two_cases_and_two_execution_contexts_even_for_model_runs():
    same_case = [
        _qualified_run("XSP-IGT-01", "B0", run_id="M1", context_id="CTX-A"),
        _qualified_run("XSP-IGT-01", "L1", run_id="M2", context_id="CTX-B"),
    ]
    not_ready = bounded_transfer_readiness([evaluate_run(run) for run in same_case])
    assert not_ready["status"] == "INSUFFICIENT_INDEPENDENT_MODEL_EVIDENCE"
    assert not_ready["materially_distinct_cases"] == 1

    two_cases = [
        _qualified_run("XSP-IGT-01", "L1", run_id="M3", context_id="CTX-C"),
        _qualified_run("XSP-IGT-02", "L1", run_id="M4", context_id="CTX-D"),
    ]
    ready = bounded_transfer_readiness([evaluate_run(run) for run in two_cases])
    assert ready["status"] == "READY_FOR_BOUNDED_TRANSFER_ANALYSIS"
    assert ready["qualified_model_runs"] == 2
    assert ready["materially_distinct_cases"] == 2
    assert ready["distinct_execution_contexts"] == 2
    assert ready["promotion"] == "NONE"
    assert ready["broad_generalization"] == "UNPROVEN"
    assert ready["model_weight_change"] == "UNPROVEN"
