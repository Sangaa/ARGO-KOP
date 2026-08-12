from verified_seam_evidence_loader import load_records


def _candidate():
    return {
        "seam": "Decision -> Authorization",
        "contract": "contract.md",
        "test": "test.py",
        "trace": "trace.md",
    }


def test_loader_registers_only_complete_local_evidence(tmp_path):
    for path in ("contract.md", "test.py", "trace.md"):
        (tmp_path / path).write_text("evidence", encoding="utf-8")

    result = load_records(tmp_path, [_candidate()])
    assert result["Decision -> Authorization"]["state"] == "CONNECTED"


def test_loader_rejects_incomplete_candidate(tmp_path):
    (tmp_path / "contract.md").write_text("evidence", encoding="utf-8")
    candidate = _candidate()
    assert load_records(tmp_path, [candidate]) == {}


def test_loader_rejects_parent_traversal(tmp_path):
    for path in ("contract.md", "test.py", "trace.md"):
        (tmp_path / path).write_text("evidence", encoding="utf-8")
    candidate = _candidate()
    candidate["trace"] = "../trace.md"
    (tmp_path.parent / "trace.md").write_text("outside evidence", encoding="utf-8")
    assert load_records(tmp_path, [candidate]) == {}


def test_loader_requires_files_not_directories(tmp_path):
    (tmp_path / "contract.md").write_text("evidence", encoding="utf-8")
    (tmp_path / "test.py").write_text("evidence", encoding="utf-8")
    (tmp_path / "trace.md").mkdir()
    assert load_records(tmp_path, [_candidate()]) == {}
