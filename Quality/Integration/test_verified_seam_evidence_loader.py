from verified_seam_evidence_loader import load_records


def _candidate():
    return {
        "seam": "Decision -> Authorization",
        "contract": "contract.md",
        "test": "test.py",
        "trace": "trace.json",
        "verification_status": "VERIFIED",
    }


def _trace():
    return '{"record_type":"EXECUTION_TRACE","trace_id":"TR-1","task_id":"TASK-1","session_id":"SESSION-1","final_status":"SUCCESS"}'


def test_loader_registers_only_complete_local_evidence(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    (tmp_path / "test.py").write_text("test", encoding="utf-8")
    (tmp_path / "trace.json").write_text(_trace(), encoding="utf-8")

    result = load_records(tmp_path, [_candidate()])
    assert result["Decision -> Authorization"]["state"] == "CONNECTED"


def test_loader_rejects_incomplete_candidate(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    candidate = _candidate()
    assert load_records(tmp_path, [candidate]) == {}


def test_loader_rejects_parent_traversal(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    (tmp_path / "test.py").write_text("test", encoding="utf-8")
    (tmp_path / "trace.json").write_text(_trace(), encoding="utf-8")
    candidate = _candidate()
    candidate["trace"] = "../trace.json"
    (tmp_path.parent / "trace.json").write_text(_trace(), encoding="utf-8")
    assert load_records(tmp_path, [candidate]) == {}


def test_loader_requires_files_not_directories(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    (tmp_path / "test.py").write_text("test", encoding="utf-8")
    (tmp_path / "trace.json").mkdir()
    assert load_records(tmp_path, [_candidate()]) == {}


def test_loader_rejects_non_trace_json(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    (tmp_path / "test.py").write_text("test", encoding="utf-8")
    (tmp_path / "trace.json").write_text('{"record_type":"OUTCOME"}', encoding="utf-8")
    assert load_records(tmp_path, [_candidate()]) == {}


def test_loader_rejects_trace_missing_identity(tmp_path):
    (tmp_path / "contract.md").write_text("contract", encoding="utf-8")
    (tmp_path / "test.py").write_text("test", encoding="utf-8")
    (tmp_path / "trace.json").write_text(
        '{"record_type":"EXECUTION_TRACE","trace_id":"TR-1"}',
        encoding="utf-8",
    )
    assert load_records(tmp_path, [_candidate()]) == {}
