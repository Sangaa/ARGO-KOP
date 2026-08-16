from pathlib import Path


def _read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def test_release_version_authority_keeps_official_release_and_development_baseline_distinct():
    root = Path(__file__).resolve().parents[2]
    version = _read(root, "Release/VERSION.md")
    changelog = _read(root, "Logs/CHANGELOG.md")

    assert "Official Release Version\n\n1.0.0" in version
    assert "Current Development Baseline\n\n3.2.1" in version
    assert "1.0.0 | Foundation | Latest Official Release" in changelog
    assert "3.2.1 — Active / Under Connected-Baseline Integrity Validation" in changelog


def test_project_status_does_not_redefine_release_authority():
    root = Path(__file__).resolve().parents[2]
    status = _read(root, "PROJECT_STATUS.md")
    assert "Latest Official Release" in status
    assert "Active Development Baseline:** v3.2.1" in status
    assert "`Release/VERSION.md` is authoritative" in status


def test_project_status_document_version_is_not_treated_as_platform_release_version():
    root = Path(__file__).resolve().parents[2]
    status = _read(root, "PROJECT_STATUS.md")
    assert "Version: 3.3.7" in status
    assert "Latest Official Release:** v1.0.0 Foundation" in status
    assert "Current Development Baseline" in status
