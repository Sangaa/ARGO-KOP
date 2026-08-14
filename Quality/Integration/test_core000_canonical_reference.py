from pathlib import Path


def test_architecture_readme_points_to_canonical_core000():
    root = Path(__file__).resolve().parents[2]
    readme = (root / "Architecture" / "README.md").read_text(encoding="utf-8")
    target = root / "Core" / "CORE-000_PLATFORM_ARCHITECTURE.md"
    assert "../Core/CORE-000_PLATFORM_ARCHITECTURE.md" in readme
    assert target.is_file()
    content = target.read_text(encoding="utf-8")
    assert "Document ID\nCORE-000" in content
    assert "Canonical\nYes" in content
