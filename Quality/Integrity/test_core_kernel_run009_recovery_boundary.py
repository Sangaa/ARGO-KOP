from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KERNEL = ROOT / "Core" / "ARGO_KERNEL.md"
RUN009 = ROOT / "Runtime" / "RUN-009_RECOVERY.md"
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_core_kernel_run009_recovery_boundary_is_direct_and_not_overpromoted():
    kernel = KERNEL.read_text(encoding="utf-8")
    recovery = RUN009.read_text(encoding="utf-8")
    registry = REP014.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    # Preserve Transaction N's exact proven source assertions.
    assert "Document ID\nCORE-KERNEL" in kernel
    assert "Recovery follows the applicable governed recovery flow." in kernel
    assert "`Runtime/RUN-009_RECOVERY.md`" in kernel
    assert "A name appearing in this document does not establish a dependency merely by being listed here." in kernel

    assert "Document ID: RUN-009" in recovery
    assert "Defines the Runtime Recovery mechanism of ARGO KOP." in recovery
    assert "Resume only when:" in recovery
    assert "Recovery restores the last safe validated execution context" in recovery

    registered = "| REL-070 | CORE-KERNEL | RUN-009 | REFERENCES | **INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY** |"
    assert registered in registry
    assert registry.count(registered) == 1

    forbidden = (
        "| CORE-KERNEL | RUN-009 | DEPENDS_ON |",
        "| CORE-KERNEL | RUN-009 | IMPLEMENTS |",
        "| CORE-KERNEL | RUN-009 | CONSUMES |",
        "| CORE-KERNEL | RUN-009 | GOVERNS |",
        "| RUN-009 | CORE-KERNEL | REFERENCES |",
        "| RUN-009 | CORE-KERNEL | DEPENDS_ON |",
        "| RUN-009 | CORE-KERNEL | IMPLEMENTS |",
        "| RUN-009 | CORE-KERNEL | CONSUMES |",
        "| RUN-009 | CORE-KERNEL | GOVERNS |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "CROSS-LAYER VALIDATION OPEN" in status
    assert "Folder Certification\n\n⏳ Pending" in status
