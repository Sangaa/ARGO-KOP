from pathlib import Path


def _read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def test_core_kernel_references_run001_without_dependency_inversion():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")
    kernel = _read(root, "Core/ARGO_KERNEL.md")
    runtime = _read(root, "Runtime/RUN-001_BOOT_SEQUENCE.md")
    dependency_model = _read(root, "Architecture/ARC-006_DEPENDENCY_MODEL.md")

    expected = (
        "| REL-062 | CORE-KERNEL | RUN-001 | REFERENCES | "
        "**INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY** |"
    )
    assert expected in registry
    assert "Runtime/RUN-001_BOOT_SEQUENCE.md" in kernel
    assert "current canonical runtime sequence defined by `Runtime/RUN-001_BOOT_SEQUENCE.md`" in kernel
    assert "Core/CORE-003_CONSTITUTION.md" in runtime
    assert "## Core\n\nDepends on: None at the architectural layer level." in dependency_model


def test_core_kernel_run001_boundary_does_not_manufacture_reverse_or_dependency_edge():
    root = Path(__file__).resolve().parents[2]
    registry = _read(root, "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "| REL-062 | CORE-KERNEL | RUN-001 | DEPENDS_ON |" not in registry
    assert "| REL-062 | CORE-KERNEL | RUN-001 | CONSUMES |" not in registry
    assert "| REL-062 | CORE-KERNEL | RUN-001 | IMPLEMENTS |" not in registry
    assert "| RUN-001 | CORE-KERNEL |" not in registry
    assert "broader Core cross-layer validation and certification remain open" in registry
