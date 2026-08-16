from pathlib import Path


CRITICAL_REFS = {
    "PROJECT_BOOTSTRAP.md": [
        "Core/CORE-003_CONSTITUTION.md",
        "Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md",
        "Repository/REP-001_MASTER_INDEX.md",
        "Release/VERSION.md",
    ],
    "Architecture/README.md": [
        "../Core/CORE-000_PLATFORM_ARCHITECTURE.md",
        "ARC-002_COMPONENT_ARCHITECTURE.md",
        "ARC-004_LAYER_MODEL.md",
        "ARC-006_DEPENDENCY_MODEL.md",
        "ARC-008_REPOSITORY_LAYOUT.md",
        "ARC-009_ARCHITECTURE_DECISIONS.md",
    ],
    "Release/VERSION.md": [
        "PROJECT_STATUS.md",
        "PROJECT_BOOTSTRAP.md",
        "Logs/CHANGELOG.md",
        "ROADMAP.md",
    ],
}


def _resolve_reference(root: Path, source_path: Path, reference: str) -> Path:
    if source_path.parent.name == "Release" and reference in {
        "PROJECT_STATUS.md",
        "PROJECT_BOOTSTRAP.md",
        "ROADMAP.md",
        "Logs/CHANGELOG.md",
    }:
        return root / reference
    return (source_path.parent / reference).resolve()


def test_critical_repository_references_resolve_to_current_files():
    root = Path(__file__).resolve().parents[2]
    for source, references in CRITICAL_REFS.items():
        source_path = root / source
        assert source_path.is_file(), source
        for reference in references:
            target = _resolve_reference(root, source_path, reference)
            assert target.is_file(), (source, reference, target)


def test_critical_reference_resolution_does_not_allow_duplicate_core_000_owner():
    root = Path(__file__).resolve().parents[2]
    owners = [
        path.relative_to(root).as_posix()
        for path in root.rglob("CORE-000_PLATFORM_ARCHITECTURE.md")
    ]
    assert owners == ["Core/CORE-000_PLATFORM_ARCHITECTURE.md"]
