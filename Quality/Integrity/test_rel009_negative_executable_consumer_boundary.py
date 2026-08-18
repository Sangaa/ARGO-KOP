from pathlib import Path


def test_no_srv009_literal_in_runtime_execution_python_scope():
    root = Path(__file__).resolve().parents[2]
    runtime_execution = root / "Runtime" / "Execution"
    python_files = sorted(runtime_execution.rglob("*.py"))
    assert python_files, "Runtime/Execution Python scope must be inspectable"

    offenders = []
    for path in python_files:
        text = path.read_text(encoding="utf-8")
        if "SRV-009" in text:
            offenders.append(path.relative_to(root).as_posix())

    assert offenders == [], (
        "REL-009 negative executable-consumer boundary violated; "
        f"SRV-009 literal found in Runtime/Execution Python: {offenders}"
    )


def test_negative_gate_is_scoped_not_global():
    """The gate is intentionally limited to Runtime/Execution/*.py."""
    root = Path(__file__).resolve().parents[2]
    assert (root / "Services/SRV-009_UPDATE_SERVICE.md").exists()
    assert (root / "Engine/ENG-006_EXECUTION_ENGINE.md").exists()
