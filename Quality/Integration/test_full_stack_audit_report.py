from pathlib import Path

from full_stack_audit_report import classify_audit


def test_audit_report_preserves_gap_classes(tmp_path):
    (tmp_path / "Runtime").mkdir()
    (tmp_path / "Runtime" / "orphan.py").write_text("def run():\n    return True\n", encoding="utf-8")
    result = classify_audit(tmp_path)
    assert result["status"] == "AUDIT_COMPLETE"
    assert result["gap_count"] >= 1
    assert any(g["gap"] == "ORPHAN_CANDIDATE" for g in result["gaps"])


def test_audit_report_surfaces_broken_reference(tmp_path: Path):
    (tmp_path / "A.md").write_text("[missing](missing.md)", encoding="utf-8")
    result = classify_audit(tmp_path)
    assert result["gaps"] == [
        {
            "path": "A.md",
            "gap": "BROKEN_REFERENCE",
            "severity": "HIGH",
            "reference": "missing.md",
        }
    ]
