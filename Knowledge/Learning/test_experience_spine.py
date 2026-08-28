from experience_spine import build_experience_packet


def _record(knowledge_id, **overrides):
    record = {
        "knowledge_id": knowledge_id,
        "status": "PROMOTED",
        "knowledge_scope": "project:argo-kop",
        "evidence": [f"evidence:{knowledge_id}"],
        "evidence_state": "PROVEN",
        "authority_state": "NON-AUTHORITATIVE",
        "source_identity": "HORUS:test",
        "source_type": "HORUS-ANALYSIS",
        "consumer_routes": ["SHARED"],
        "domains": ["repository"],
        "problem_types": ["retrieval-defect"],
        "artifact_ids": [],
        "failure_classes": [],
        "pattern": f"pattern-{knowledge_id}",
    }
    record.update(overrides)
    return record


def _context(**overrides):
    context = {
        "task_id": "P375",
        "execution_identity": "HORUS:instance-current",
        "domain": "repository",
        "problem_types": ["retrieval-defect"],
        "allowed_scopes": ["project:argo-kop"],
        "max_records": 5,
        "consumer_route": "HERMUZ",
        "repository_ref": "feature/experience-spine-p375",
        "repository_head": "candidate-head",
        "concurrent_work_refs": ["PR-64", "PR-65"],
    }
    context.update(overrides)
    return context


def test_missing_context_holds_without_widening():
    packet = build_experience_packet([_record("K-1")], {"task_id": "P375"})
    assert packet["status"] == "HOLD"
    assert packet["experience_items"] == []
    assert "allowed_scopes" in packet["missing"]


def test_scope_and_authority_are_preserved():
    records = [
        _record("K-IN"),
        _record("K-OUT", knowledge_scope="platform"),
        _record("K-HOLD", evidence_state="UNPROVEN"),
    ]
    packet = build_experience_packet(records, _context())
    assert [item["knowledge_id"] for item in packet["experience_items"]] == ["K-IN"]
    assert packet["experience_items"][0]["authority_state"] == "NON-AUTHORITATIVE"
    assert packet["experience_items"][0]["source_identity"] == "HORUS:test"
    assert packet["authority_boundary"] == "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE"


def test_exact_artifact_match_outranks_textual_pattern():
    records = [
        _record("K-GENERAL", pattern="REP-014 REP-015 experience words"),
        _record("K-EXACT", artifact_ids=["REP-014"], problem_types=["other"]),
    ]
    packet = build_experience_packet(records, _context(artifact_ids=["REP-014"]))
    assert packet["experience_items"][0]["knowledge_id"] == "K-EXACT"
    assert packet["experience_items"][0]["match_reasons"]["artifact_ids"] == ["REP-014"]


def test_packet_is_bounded_and_deterministic():
    records = [_record(f"K-{index:02d}") for index in range(20)]
    packet = build_experience_packet(records, _context(max_records=100))
    assert len(packet["experience_items"]) == 10
    assert [item["knowledge_id"] for item in packet["experience_items"]] == [
        f"K-{index:02d}" for index in range(10)
    ]


def test_conflict_is_reported_not_silently_resolved():
    records = [
        _record("K-A", contradicts=["K-B"]),
        _record("K-B", contradicts=["K-A"]),
    ]
    packet = build_experience_packet(records, _context())
    assert packet["conflicts"] == [["K-A", "K-B"]]


def test_consumer_route_filters_other_execution_paths():
    records = [
        _record("K-HERMUZ", consumer_routes=["HERMUZ"]),
        _record("K-ARGO", consumer_routes=["ARGO"]),
    ]
    packet = build_experience_packet(records, _context(consumer_route="HERMUZ"))
    assert [item["knowledge_id"] for item in packet["experience_items"]] == ["K-HERMUZ"]
    assert packet["excluded_summary"]["CONSUMER_ROUTE_MISMATCH"] == 1


def test_duplicate_identity_holds_instead_of_shadowing_parallel_record():
    records = [
        _record("K-DUP", source_identity="HORUS:instance-a"),
        _record("K-DUP", source_identity="HORUS:instance-b"),
    ]
    packet = build_experience_packet(records, _context())
    assert packet["status"] == "HOLD"
    assert packet["reason"] == "DUPLICATE_KNOWLEDGE_IDENTITY"
    assert packet["duplicate_knowledge_ids"] == ["K-DUP"]
    assert packet["experience_items"] == []


def test_execution_context_preserves_multi_instance_attribution():
    packet = build_experience_packet([_record("K-1")], _context())
    assert packet["execution_identity"] == "HORUS:instance-current"
    assert packet["execution_context"] == {
        "repository_ref": "feature/experience-spine-p375",
        "repository_head": "candidate-head",
        "concurrent_work_refs": ["PR-64", "PR-65"],
        "consumer_route": "HERMUZ",
    }

