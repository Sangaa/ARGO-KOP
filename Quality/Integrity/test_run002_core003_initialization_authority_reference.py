from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP014 = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE003 = ROOT / "Core" / "CORE-003_CONSTITUTION.md"
RUN002 = ROOT / "Runtime" / "RUN-002_INITIALIZATION.md"
CORE_STATUS = ROOT / "Core" / "_FOLDER_STATUS.md"


def test_run002_core003_initialization_authority_reference_is_bounded():
    registry = REP014.read_text(encoding="utf-8")
    constitution = CORE003.read_text(encoding="utf-8")
    runtime = RUN002.read_text(encoding="utf-8")
    status = CORE_STATUS.read_text(encoding="utf-8")

    assert "The Constitution defines the highest governing rules of the ARGO Platform." in constitution
    assert "All repository components shall comply with this Constitution within the scope applicable to them." in constitution

    assert "Document ID: RUN-002" in runtime
    assert "Canonical: Yes" in runtime
    assert "Priority: Critical" in runtime
    assert "Initialization prepares only the components required for the current operation and MUST complete validation before execution begins." in runtime
    assert "Each component MUST verify its declared dependencies." in runtime
    assert "Initialization MUST NOT mark Runtime `READY` while the required integrity gate is failed or held." in runtime
    assert "required authority cannot be resolved;" in runtime
    assert "- `Core/CORE-003_CONSTITUTION.md`" in runtime
    assert "It MUST NOT imply that the entire repository is globally clean." in runtime

    # Transaction R is validation-first. Registration, if still warranted after fresh recomputation, is separate.
    assert "| RUN-002 | CORE-003 | REFERENCES |" not in registry
    assert "| CORE-003 | RUN-002 | GOVERNS |" not in registry

    forbidden = (
        "| RUN-002 | CORE-003 | DEPENDS_ON |",
        "| RUN-002 | CORE-003 | GOVERNS |",
        "| RUN-002 | CORE-003 | IMPLEMENTS |",
        "| RUN-002 | CORE-003 | CONSUMES |",
        "| CORE-003 | RUN-002 | REFERENCES |",
        "| CORE-003 | RUN-002 | DEPENDS_ON |",
        "| CORE-003 | RUN-002 | IMPLEMENTS |",
        "| CORE-003 | RUN-002 | CONSUMES |",
    )
    for marker in forbidden:
        assert marker not in registry

    assert "CROSS-LAYER VALIDATION OPEN" in status
    assert "Folder Certification\n\n⏳ Pending" in status
