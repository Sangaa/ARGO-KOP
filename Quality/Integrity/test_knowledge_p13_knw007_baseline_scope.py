from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNW007 = ROOT / "Knowledge" / "KNW-007_KNOWLEDGE_BASELINE.md"


def test_knw007_baseline_is_platform_scoped_not_repository_wide() -> None:
    text = KNW007.read_text(encoding="utf-8")
    assert "Version: 1.1.1" in text
    assert "Status: Integrity Hold / Revalidated" in text
    assert "The approved repository knowledge is the current baseline." not in text
    assert "Repository knowledge is authoritative." not in text
    assert "governed knowledge explicitly accepted for canonical `PLATFORM` scope" in text
    assert "Repository storage, document approval or local validation alone does not make a knowledge item part of the platform Knowledge Baseline." in text


def test_knw007_preserves_contextual_scope_and_higher_authority() -> None:
    text = KNW007.read_text(encoding="utf-8")
    assert "User-, project- and deployment-owned knowledge remains attributable to its originating scope" in text
    assert "not an independent authority above Core, Governance, Architecture or Repository control contracts" in text
    assert "Repository write access is not baseline authority." in text
