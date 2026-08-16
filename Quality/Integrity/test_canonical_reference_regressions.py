from pathlib import Path


def test_architecture_core_000_reference_targets_authoritative_core_path():
    root = Path(__file__).resolve().parents[2]
    architecture_readme = root / "Architecture/README.md"
    authoritative = root / "Core/CORE-000_PLATFORM_ARCHITECTURE.md"
    stale_duplicate = root / "Architecture/CORE-000_PLATFORM_ARCHITECTURE.md"

    text = architecture_readme.read_text(encoding="utf-8")
    assert "../Core/CORE-000_PLATFORM_ARCHITECTURE.md" in text
    assert authoritative.is_file()
    assert not stale_duplicate.exists()


def test_canonical_reference_regression_preserves_single_core_000_owner():
    root = Path(__file__).resolve().parents[2]
    matches = []
    for path in root.rglob("*.md"):
        if path.name == "CORE-000_PLATFORM_ARCHITECTURE.md":
            matches.append(path.relative_to(root).as_posix())
    assert matches == ["Core/CORE-000_PLATFORM_ARCHITECTURE.md"]
