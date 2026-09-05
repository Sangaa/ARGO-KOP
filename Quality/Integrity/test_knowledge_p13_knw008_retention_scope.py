from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNW008 = ROOT / "Knowledge" / "KNW-008_KNOWLEDGE_TRACEABILITY.md"


def test_knw008_retention_is_proportional_not_absolute() -> None:
    text = KNW008.read_text(encoding="utf-8")
    assert "Version: 1.1.1" in text
    assert "Status: Integrity Hold / Revalidated" in text
    assert "Every knowledge object shall preserve its complete history." not in text
    assert "Historical knowledge shall never be deleted." not in text
    assert "Retention is governed and proportional." in text
    assert "Destructive deletion is not automatically prohibited." in text


def test_knw008_preserves_material_evidence_without_making_history_sacred() -> None:
    text = KNW008.read_text(encoding="utf-8")
    assert "shall never be used to erase contradictory evidence" in text
    assert "Historical knowledge does not replace current authoritative knowledge merely because it is retained." in text
    assert "without turning history into immutable authority" in text
