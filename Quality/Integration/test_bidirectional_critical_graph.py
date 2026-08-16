from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (_root() / relative).read_text(encoding="utf-8")


def test_eng006_srv009_relationship_has_endpoint_evidence():
    eng006 = _read("Engine/ENG-006_EXECUTION_ENGINE.md")
    srv009 = _read("Services/SRV-009_UPDATE_SERVICE.md")
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "SRV-009_UPDATE_SERVICE.md" in eng006
    assert "ENG-006_EXECUTION_ENGINE.md" in srv009
    assert "REL-005 | ENG-006 | SRV-009" in registry


def test_run010_critical_path_has_endpoint_evidence():
    run010 = _read("Runtime/RUN-010_RUNTIME_REFERENCE.md")
    eng006 = _read("Engine/ENG-006_EXECUTION_ENGINE.md")
    srv009 = _read("Services/SRV-009_UPDATE_SERVICE.md")
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "ENG-006 Execution → SRV-009 Controlled Mutation" in run010
    assert "RUN-010" not in eng006  # ENG-006 remains a domain endpoint, not a Runtime authority.
    assert "Runtime" in srv009 and "ENG-006_EXECUTION_ENGINE.md" in srv009
    assert "REL-008 | RUN-010 | ENG-006" in registry
    assert "REL-009 | RUN-010 | SRV-009" in registry
