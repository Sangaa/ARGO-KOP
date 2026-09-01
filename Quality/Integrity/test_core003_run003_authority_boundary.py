from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE003 = ROOT / "Core" / "CORE-003_CONSTITUTION.md"
RUN003 = ROOT / "Runtime" / "RUN-003_CONFIGURATION.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_core003_run003_authority_boundary_is_direct_and_not_overpromoted():
    registry = REP014.read_text(encoding="utf-8")
    constitution = CORE003.read_text(encoding="utf-8")
    runtime = RUN003.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    assert "The Constitution defines the highest governing rules of the ARGO Platform." in constitution
    assert "All repository components shall comply with this Constitution within the scope applicable to them." in constitution

    assert "Document ID: RUN-003" in runtime
    assert "Canonical: Yes" in runtime
    assert "Priority: Critical" in runtime
    assert "Configuration controls runtime behavior without modifying repository architecture or authority." in runtime
    assert "Runtime configuration does not override:" in runtime
    assert "- `Core/CORE-003_CONSTITUTION.md`" in runtime
    assert "repository authority remains above runtime assumptions." in runtime

    # Transaction P is validation-first: registry synchronization is intentionally deferred.
    assert "| CORE-003 | RUN-003 | GOVERNS |" not in registry
    assert "| RUN-003 | CORE-003 | REFERENCES |" not in registry

    forbidden = (
        "| RUN-003 | CORE-003 | DEPENDS_ON |",
        "| RUN-003 | CORE-003 | GOVERNS |",
        "| RUN-003 | CORE-003 | IMPLEMENTS |",
        "| RUN-003 | CORE-003 | CONSUMES |",
        "| CORE-003 | RUN-003 | DEPENDS_ON |",
        "| CORE-003 | RUN-003 | IMPLEMENTS |",
        "| CORE-003 | RUN-003 | CONSUMES |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "CROSS-LAYER VALIDATION OPEN" in status
    assert "Folder Certification\n\n⏳ Pending" in status
