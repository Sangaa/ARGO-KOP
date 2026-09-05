from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNW006 = ROOT / "Knowledge" / "KNW-006_KNOWLEDGE_QUALITY.md"


def test_knw006_authority_is_scope_bounded_not_repository_absolute() -> None:
    text = KNW006.read_text(encoding="utf-8")
    assert "Version: 1.1.1" in text
    assert "Status: Integrity Hold / Revalidated" in text
    assert "Repository always prevails" not in text
    assert "Repository location or repository approval alone does not make every knowledge item platform-wide canonical authority." in text
    assert "User-, project- and deployment-owned knowledge remains attributable to its originating scope" in text
    assert "Quality does not itself create canonical authority." in text


def test_knw006_preserves_higher_authority_and_non_overwrite_boundaries() -> None:
    text = KNW006.read_text(encoding="utf-8")
    assert "subject to higher Core, Governance, Architecture and Repository control authority" in text
    assert "shall not silently overwrite contextual knowledge" in text
