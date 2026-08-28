from experience_spine import build_experience_packet


def _record(knowledge_id, **overrides):
    record = {
        "knowledge_id": knowledge_id,
        "status": "PROMOTED",
        "knowledge_scope": "project:argo-kop",
        "evidence": [f"evidence:{knowledge_id}"],
        "evidence_state": "PROVEN",
        "authority_state": "NON-AUTHORITATIVE",
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
        "domain": "repository",
        "problem_types": ["retrieval-defect"],
        "allowed_scopes": ["project:argo-kop"],
        "max_records": 5,
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


