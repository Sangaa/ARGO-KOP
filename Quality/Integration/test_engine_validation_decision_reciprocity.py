from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (_root() / relative).read_text(encoding="utf-8")


def test_eng004_srv005_validation_reciprocity():
    eng004 = _read("Engine/ENG-004_VALIDATION_ENGINE.md")
    srv005 = _read("Services/SRV-005_VALIDATION_SERVICE.md")
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "SRV-005" in eng004
    assert "ENG-004_VALIDATION_ENGINE.md" in srv005
    assert "REL-003 | ENG-004 | SRV-005" in registry


def test_eng002_execution_boundary_is_explicit():
    eng002 = _read("Engine/ENG-002_DECISION_ENGINE.md")
    eng006 = _read("Engine/ENG-006_EXECUTION_ENGINE.md")
    registry = _read("Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md")

    assert "Execution" in eng002
    assert "ENG-002" in eng006
    assert "REL-004 | ENG-002 | ENG-006" in registry
    assert "Execution authority remains subject to validation, authorization" in eng002
