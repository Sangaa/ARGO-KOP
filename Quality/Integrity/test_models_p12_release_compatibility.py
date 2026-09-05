from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "Release" / "VERSION.md"
MODELS = [
    ROOT / "Models" / "MOD-001_KNOWLEDGE_MODEL.md",
    ROOT / "Models" / "MOD-002_ENTITY_MODEL.md",
    ROOT / "Models" / "MOD-003_DOCUMENT_MODEL.md",
    ROOT / "Models" / "MOD-004_MEMORY_MODEL.md",
    ROOT / "Models" / "MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
]


def _field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*([^\n]+)$", text, flags=re.MULTILINE)
    assert match, f"missing {name}"
    return match.group(1).strip()


def test_models_keep_artifact_version_separate_from_platform_version_dimensions() -> None:
    release = RELEASE.read_text(encoding="utf-8")
    assert "Official Release Version\n\n1.0.0" in release
    assert "Current Development Baseline\n\n3.2.1" in release
    assert "MUST NOT treat a development baseline as an official release" in release

    for path in MODELS:
        text = path.read_text(encoding="utf-8")
        artifact_version = _field(text, "Version")
        baseline = _field(text, "Development Baseline")
        assert baseline == "3.2.1", path
        assert artifact_version != baseline, path
        assert artifact_version != "1.0.0", path


def test_historical_mod009_is_not_recreated_as_release_authority() -> None:
    status = (ROOT / "Models" / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "`MOD-009_VERSION_MODEL.md` — would risk collision with Release/version authority; no recreate" in status
    assert "ARTIFACT_VERSION != DEVELOPMENT_BASELINE != OFFICIAL_RELEASE" in (
        ROOT / "Repository" / "REP-014_PRIORITY12_MODELS_RELEASE_COMPATIBILITY_EVIDENCE_2026-09-05_K.tsv"
    ).read_text(encoding="utf-8")
