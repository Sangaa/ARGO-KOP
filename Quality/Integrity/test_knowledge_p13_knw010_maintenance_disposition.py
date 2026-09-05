from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNW010 = ROOT / "Knowledge" / "KNW-010_KNOWLEDGE_MAINTENANCE.md"


def test_knw010_approved_knowledge_is_reviewable_not_immutable() -> None:
    text = KNW010.read_text(encoding="utf-8")
    assert "Version: 1.1.2" in text
    assert "Status: Integrity Hold / Revalidated" in text
    assert "Delete Approved Knowledge" not in text
    assert "Approved or canonical knowledge is not permanently immune to revision or removal." in text
    assert "`APPROVED != IMMUTABLE`" in text
    assert "`CANONICAL != SACRED`" in text


def test_knw010_disposition_preserves_required_evidence_and_authority() -> None:
    text = KNW010.read_text(encoding="utf-8")
    assert "erase required provenance or material traceability" in text
    assert "conceal a contradiction, failure or superseded interpretation" in text
    assert "Under applicable authority it may be corrected, superseded, reclassified, archived or removed" in text
    assert "`REMOVAL != ERASURE OF REQUIRED EVIDENCE`" in text
    assert "Maintenance in one scope does not automatically authorize modification or promotion in another scope." in text
