from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REP002 = ROOT / "Repository" / "REP-002_REPOSITORY_MAP.md"


def _core_section(text: str) -> str:
    return text.split("## 3. Core Layer", 1)[1].split("## 4. Repository Layer", 1)[0]


def test_rep002_maps_current_core000a_and_core012() -> None:
    text = REP002.read_text(encoding="utf-8")
    core = _core_section(text)

    assert "`Core/CORE-000A_PLATFORM_GLOSSARY.md`" in core
    assert "`Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`" in core


def test_rep002_does_not_promote_legacy_core000_identity() -> None:
    text = REP002.read_text(encoding="utf-8")
    core = _core_section(text)

    assert "- `Core/CORE-000_PLATFORM_IDENTITY.md`" not in core
    assert "legacy `Core/CORE-000_PLATFORM_IDENTITY.md`" in core


def test_rep002_reconciliation_keeps_bounded_integrity_state() -> None:
    text = REP002.read_text(encoding="utf-8")

    assert "Version: 1.7.6" in text
    assert "Status: Integrity Hold" in text
    assert "This is a bounded physical-map reconciliation only." in text
