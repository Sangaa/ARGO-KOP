from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
REP001 = ROOT / "Repository" / "REP-001_MASTER_INDEX.md"


def _core_layer(text: str) -> str:
    match = re.search(r"## 3\. Core Layer\n(?P<body>.*?)\n## 4\. Repository Layer", text, re.S)
    assert match, "REP-001 Core Layer section not found"
    return match.group("body")


def test_rep001_indexes_current_core000a_reference():
    text = REP001.read_text(encoding="utf-8")
    core = _core_layer(text)
    assert "Version: 1.11.5" in text
    assert "Core/CORE-000A_PLATFORM_GLOSSARY.md" in core


def test_rep001_does_not_promote_legacy_core000_identity():
    text = REP001.read_text(encoding="utf-8")
    core = _core_layer(text)
    assert "Core/CORE-000_PLATFORM_IDENTITY.md" not in core
    assert "does not promote the legacy `CORE-000_PLATFORM_IDENTITY.md`" in text


def test_rep001_reconciliation_keeps_priority7_open():
    text = REP001.read_text(encoding="utf-8")
    assert "REP-002 mapping drift" in text
    assert "Core certification remain open" in text
