from verified_seam_evidence_loader import load_records


def test_loader_registers_only_complete_local_evidence(tmp_path):
    for path in ("contract.md", "test.py", "trace.md"):
        (tmp_path / path).write_text("evidence", encoding="utf-8")

    records = [{
        "seam": "Decision -> Authorization",
        "contract": "contract.md",
        "test": "test.py",
        "trace": "trace.md",
    }]
    result = load_records(tmp_path, records)
    assert result["Decision -> Authorization"]["state"] == "CONNECTED"


def test_loader_rejects_incomplete_candidate(tmp_path):
    (tmp_path / "contract.md").write_text("evidence", encoding="utf-8")
    records = [{
        "seam": "Decision -> Authorization",
        "contract": "contract.md",
        "test": "missing.py",
        "trace": "missing.md",
    }]
    assert load_records(tmp_path, records) == {}
