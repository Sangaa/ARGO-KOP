from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNW004 = ROOT / "Knowledge" / "KNW-004_KNOWLEDGE_LIFECYCLE.md"
KNW006 = ROOT / "Knowledge" / "KNW-006_KNOWLEDGE_QUALITY.md"
KNW010 = ROOT / "Knowledge" / "KNW-010_KNOWLEDGE_MAINTENANCE.md"


def _related_documents(text: str) -> str:
    section = text.split("# Related Documents", 1)[1]
    return section.split("\n# ", 1)[0]


def test_knw004_document_lifecycle_identity_is_current() -> None:
    text = KNW004.read_text(encoding="utf-8")
    related = _related_documents(text)
    assert "Version: 1.3.2" in text
    assert "`Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md` — document artifact lifecycle." in text
    assert "`Governance/GOV-005_REVIEW_STANDARD.md` — mandatory evidence-based review authority" in text
    assert "`GOV-005` — document artifact lifecycle." not in related


def test_knw006_review_standard_path_is_current() -> None:
    text = KNW006.read_text(encoding="utf-8")
    related = _related_documents(text)
    assert "Version: 1.1.2" in text
    assert "`Governance/GOV-005_REVIEW_STANDARD.md`" in related
    assert "Governance/GOV-006_REVIEW_STANDARD.md" not in related
    assert "stale `Governance/GOV-006_REVIEW_STANDARD.md` path" in text


def test_knw010_rep010_reference_uses_current_physical_identity() -> None:
    text = KNW010.read_text(encoding="utf-8")
    related = _related_documents(text)
    assert "Version: 1.1.2" in text
    assert "`Repository/REP-010_RELEASE_BASELINE.md`" in related
    assert "Repository/REP-010_REPOSITORY_MAINTENANCE.md" not in related
    assert "stale physical reference `Repository/REP-010_REPOSITORY_MAINTENANCE.md`" in text
    assert "known title/path coherence gap remains a separate repository concern" in text
