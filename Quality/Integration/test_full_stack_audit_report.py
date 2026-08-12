from full_stack_audit_report import classify_audit


def test_audit_report_preserves_gap_classes(tmp_path):
    (tmp_path / "Runtime").mkdir()
    (tmp_path / "Runtime" / "orphan.py").write_text("def run():\n    return True\n", encoding="utf-8")
    result = classify_audit(tmp_path)
    assert result["status"] == "AUDIT_COMPLETE"
    assert result["gap_count"] >= 1
    assert any(g["gap"] == "ORPHAN_CANDIDATE" for g in result["gaps"])
