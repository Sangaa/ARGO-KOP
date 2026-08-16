from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _canonical_value(text: str):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().lower() == "canonical" and index + 1 < len(lines):
            return lines[index + 1].strip().lower()
        if line.strip().lower().startswith("canonical:"):
            return line.split(":", 1)[1].strip().lower()
    return None


def test_core000_legacy_identity_is_not_canonical():
    legacy = (ROOT / "Core/CORE-000_PLATFORM_IDENTITY.md").read_text(encoding="utf-8")
    assert _canonical_value(legacy) == "no"
    assert "Core/CORE-002_ARGO_IDENTITY.md" in legacy
    assert "Core/CORE-000_PLATFORM_ARCHITECTURE.md" in legacy


def test_core000_has_no_second_canonical_owner_in_core_namespace():
    canonical_core000 = []
    for path in (ROOT / "Core").glob("CORE-000*.md"):
        text = path.read_text(encoding="utf-8")
        if _canonical_value(text) == "yes" and "CORE-000" in text:
            canonical_core000.append(path.name)

    assert canonical_core000 == ["CORE-000_PLATFORM_ARCHITECTURE.md"]
