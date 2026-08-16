from pathlib import Path
import re


def _text(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def _value(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}\s*\n\n([^\n]+)", text, re.MULTILINE)
    assert match, f"missing {label}"
    return match.group(1).strip()


def test_release_version_remains_authoritative_for_release_and_baseline():
    root = Path(__file__).resolve().parents[2]
    version = _text(root, "Release/VERSION.md")
    status = _text(root, "PROJECT_STATUS.md")
    changelog = _text(root, "Logs/CHANGELOG.md")

    assert _value(version, "Official Release Version") == "1.0.0"
    assert _value(version, "Current Development Baseline") == "3.2.1"
    assert "Latest Official Release" in status
    assert "3.2.1" in status
    assert "3.2.1 — Active / Under Connected-Baseline Integrity Validation" in changelog


def test_status_document_version_is_not_mistaken_for_platform_baseline():
    root = Path(__file__).resolve().parents[2]
    status = _text(root, "PROJECT_STATUS.md")
    assert "Version: 3.3.7" in status
    assert "Active Development Baseline:** v3.2.1" in status
    assert "Latest Official Release:** v1.0.0 Foundation" in status
