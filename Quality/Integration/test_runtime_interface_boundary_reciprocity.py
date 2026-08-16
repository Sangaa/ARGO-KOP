from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (_root() / relative).read_text(encoding="utf-8")


def test_runtime_interface_boundary_is_explicit_and_non_authoritative():
    run010 = _read("Runtime/RUN-010_RUNTIME_REFERENCE.md")
    intf001 = _read("Interfaces/INTF-001_INTERFACE_SPEC.md")
    intf010 = _read("Interfaces/INTF-010_INTEGRATIONS.md")

    assert "Interfaces/INTF-010_INTEGRATIONS.md" in run010
    assert "ARGO RUNTIME" in intf001
    assert "ARGO Runtime → Interface Contract" in intf010
    assert "does not independently create canonical authority" in intf010 or "does not" in intf010


def test_runtime_dependencies_include_current_interface_boundaries():
    run010 = _read("Runtime/RUN-010_RUNTIME_REFERENCE.md")

    assert "Interfaces/INTF-001_INTERFACE_SPEC.md" in run010
    assert "Interfaces/INTF-006_ENVIRONMENT_SENSING.md" in run010
    assert "Interfaces/INTF-010_INTEGRATIONS.md" in run010
