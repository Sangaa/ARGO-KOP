from pathlib import Path


B07_CONSUMER = "Runtime/Execution/run010_eng006_srv009_consumer.py"


def test_no_direct_srv009_literal_outside_governed_consumer():
    """REL-009 forbids ad-hoc SRV-009 consumers, not the governed B07 seam itself."""
    root = Path(__file__).resolve().parents[2]
    runtime_execution = root / "Runtime" / "Execution"
    python_files = sorted(runtime_execution.rglob("*.py"))
    assert python_files, "Runtime/Execution Python scope must be inspectable"

    offenders = []
    for path in python_files:
        relative = path.relative_to(root).as_posix()
        if relative == B07_CONSUMER:
            continue
        text = path.read_text(encoding="utf-8")
        if "SRV-009" in text:
            offenders.append(relative)

    assert offenders == [], (
        "REL-009 negative executable-consumer boundary violated; "
        f"unexpected SRV-009 literal found in Runtime/Execution Python: {offenders}"
    )


def test_b07_consumer_uses_repository_connector_boundary():
    """The one permitted runtime SRV-009 seam must remain provider-neutral."""
    root = Path(__file__).resolve().parents[2]
    consumer = root / B07_CONSUMER
    assert consumer.exists(), "B07 governed consumer must exist"
    text = consumer.read_text(encoding="utf-8")
    assert "RepositoryConnector" in text
    assert "Services.REPOSITORY_CONNECTOR_INTERFACE" in text


def test_negative_gate_is_scoped_not_global():
    """The negative gate remains limited to Runtime/Execution/*.py."""
    root = Path(__file__).resolve().parents[2]
    assert (root / "Services/SRV-009_UPDATE_SERVICE.md").exists()
    assert (root / "Engine/ENG-006_EXECUTION_ENGINE.md").exists()
