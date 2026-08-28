from experience_spine import build_experience_packet


def _profile(**overrides):
    profile = {
        "source_identity": "HERMUZ:test",
        "source_type": "HERMUZ-ENGINEERING",
        "evidence_state": "PROVEN",
        "authority_state": "ADVISORY",
        "consumer_routes": ["SHARED"],
        "evidence_group": "EVIDENCE-GROUP-DEFAULT",
        "domains": ["repository"],
        "problem_types": ["multi-writer-reconciliation"],
        "artifact_ids": [],
        "failure_classes": [],
        "applicability_boundaries": ["repository work"],
        "counterindications": [],
        "contradicts": [],
        "superseded_by": [],
    }
    profile.update(overrides)
    return profile


def _record(knowledge_id, **overrides):
    record = {
        "knowledge_id": knowledge_id,
        "task_id": f"TASK-{knowledge_id}",
        "session_id": "SESSION-1",
        "status": "PROMOTED",
        "validation": "VALIDATED",
        "knowledge_scope": "project:argo-kop",
        "evidence": [f"evidence:{knowledge_id}"],
        "provenance_preserved": True,
        "pattern": f"pattern-{knowledge_id}",
        "experience_profile": _profile(evidence_group=f"GROUP-{knowledge_id}"),
    }
    record.update(overrides)
    return record


def _context(**overrides):
    context = {
        "task_id": "EXPERIENCE-SPINE-CLEAN",
        "execution_identity": "HERMUZ:clean-extraction",
        "domain": "repository",
        "problem_types": ["multi-writer-reconciliation"],
        "allowed_scopes": ["project:argo-kop"],
        "consumer_route": "HERMUZ",
        "max_records": 5,
        "repository_ref": "hermuz/experience-spine-clean-20260828",
        "repository_head": "candidate-head",
        "concurrent_work_refs": ["PR-66", "PR-69"],
    }
    context.update(overrides)
    return context


def test_missing_context_holds_without_widening():
    packet = build_experience_packet([_record("K-1")], {"task_id": "T"})
    assert packet["status"] == "HOLD"
    assert packet["experience_items"] == []
    assert "allowed_scopes" in packet["missing"]


def test_lifecycle_validation_and_authority_axes_stay_separate():
    good = _record("K-GOOD")
    not_promoted = _record("K-CANDIDATE", status="VERIFIED")
    not_validated = _record("K-NOT-VALIDATED", validation="REPORTED")
    packet = build_experience_packet([good, not_promoted, not_validated], _context())

    assert [item["knowledge_id"] for item in packet["experience_items"]] == ["K-GOOD"]
    item = packet["experience_items"][0]
    assert item["lifecycle_state"] == "PROMOTED"
    assert item["validation_state"] == "VALIDATED"
    assert item["evidence_state"] == "PROVEN"
    assert item["authority_state"] == "ADVISORY"
    assert packet["excluded_summary"]["LIFECYCLE_NOT_PROMOTED"] == 1
    assert packet["excluded_summary"]["VALIDATION_NOT_VALIDATED"] == 1


def test_legacy_record_without_profile_is_not_guessed_into_spine():
    legacy = _record("K-LEGACY")
    legacy.pop("experience_profile")
    packet = build_experience_packet([legacy], _context())
    assert packet["status"] == "READY"
    assert packet["experience_items"] == []
    assert packet["excluded_summary"]["EXPERIENCE_PROFILE_MISSING"] == 1


def test_scope_and_consumer_route_are_explicit_filters():
    in_scope = _record("K-IN")
    out_scope = _record("K-OUT", knowledge_scope="platform")
    wrong_route = _record("K-ROUTE")
    wrong_route["experience_profile"] = _profile(
        consumer_routes=["ARGO"], evidence_group="GROUP-K-ROUTE"
    )

    packet = build_experience_packet([in_scope, out_scope, wrong_route], _context())
    assert [item["knowledge_id"] for item in packet["experience_items"]] == ["K-IN"]
    assert packet["excluded_summary"]["OUT_OF_SCOPE"] == 1
    assert packet["excluded_summary"]["CONSUMER_ROUTE_MISMATCH"] == 1


def test_exact_artifact_match_outranks_lower_weight_match():
    general = _record("K-GENERAL")
    exact = _record("K-EXACT")
    exact["experience_profile"] = _profile(
        problem_types=["other"],
        artifact_ids=["REP-014"],
        evidence_group="GROUP-K-EXACT",
    )
    packet = build_experience_packet(
        [general, exact], _context(artifact_ids=["REP-014"])
    )
    assert packet["experience_items"][0]["knowledge_id"] == "K-EXACT"
    assert packet["experience_items"][0]["match_reasons"]["artifact_ids"] == ["REP-014"]


def test_packet_is_bounded_and_deterministic():
    records = [_record(f"K-{index:02d}") for index in range(20)]
    packet = build_experience_packet(records, _context(max_records=100))
    assert len(packet["experience_items"]) == 10
    assert [item["knowledge_id"] for item in packet["experience_items"]] == [
        f"K-{index:02d}" for index in range(10)
    ]


def test_duplicate_identity_holds_instead_of_source_preference():
    first = _record("K-DUP")
    second = _record("K-DUP")
    second["experience_profile"] = _profile(
        source_identity="HORUS:other",
        source_type="HORUS-ANALYSIS",
        evidence_group="GROUP-OTHER",
    )
    packet = build_experience_packet([first, second], _context())
    assert packet["status"] == "HOLD"
    assert packet["reason"] == "DUPLICATE_KNOWLEDGE_IDENTITY"
    assert packet["duplicate_knowledge_ids"] == ["K-DUP"]
    assert packet["experience_items"] == []


def test_conflict_requires_review_and_is_not_silently_resolved():
    first = _record("K-A")
    second = _record("K-B")
    first["experience_profile"] = _profile(
        contradicts=["K-B"], evidence_group="GROUP-A"
    )
    second["experience_profile"] = _profile(
        contradicts=["K-A"], evidence_group="GROUP-B"
    )
    packet = build_experience_packet([first, second], _context())
    assert packet["status"] == "REVIEW_REQUIRED"
    assert packet["reason"] == "CONFLICTING_EXPERIENCE_REQUIRES_CURRENT_EVIDENCE_REVIEW"
    assert packet["conflicts"] == [["K-A", "K-B"]]
    assert len(packet["experience_items"]) == 2


def test_same_evidence_group_is_reported_as_correlated_not_independent():
    first = _record("K-A")
    second = _record("K-B")
    first["experience_profile"] = _profile(evidence_group="COMMON-SOURCE")
    second["experience_profile"] = _profile(evidence_group="COMMON-SOURCE")
    packet = build_experience_packet([first, second], _context())
    assert packet["status"] == "READY"
    assert packet["correlated_evidence_groups"] == [
        {
            "evidence_group": "COMMON-SOURCE",
            "knowledge_ids": ["K-A", "K-B"],
            "independence": "CORRELATED_NOT_INDEPENDENT",
        }
    ]
    assert packet["evidence_boundary"] == "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION"


def test_superseded_record_is_excluded_without_rewriting_it():
    old = _record("K-OLD")
    old["experience_profile"] = _profile(
        superseded_by=["K-NEW"], evidence_group="GROUP-OLD"
    )
    new = _record("K-NEW")
    packet = build_experience_packet([old, new], _context())
    assert [item["knowledge_id"] for item in packet["experience_items"]] == ["K-NEW"]
    assert packet["excluded_summary"]["SUPERSEDED"] == 1
    assert old["status"] == "PROMOTED"


def test_execution_context_preserves_multi_writer_attribution():
    packet = build_experience_packet([_record("K-1")], _context())
    assert packet["execution_identity"] == "HERMUZ:clean-extraction"
    assert packet["execution_context"] == {
        "repository_ref": "hermuz/experience-spine-clean-20260828",
        "repository_head": "candidate-head",
        "concurrent_work_refs": ["PR-66", "PR-69"],
        "consumer_route": "HERMUZ",
    }
    assert packet["authority_boundary"] == "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE"
