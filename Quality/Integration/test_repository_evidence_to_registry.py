from connected_spine_runner import run
from runtime_evidence_capture import capture_repository_evidence
from verified_seam_evidence_loader import load_records
from synthetic_task_fixture import make_fixture


def _materialize_seam_artifacts(tmp_path):
    contract = tmp_path / "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md"
    test = tmp_path / "Quality/Integration/test_repository_evidence_to_registry.py"
    contract.parent.mkdir(parents=True, exist_ok=True)
    test.parent.mkdir(parents=True, exist_ok=True)
    contract.write_text("# execution trace contract\n", encoding="utf-8")
    test.write_text("# executable evidence test artifact\n", encoding="utf-8")


def test_repository_evidence_can_be_loaded_as_verified_seam(tmp_path):
    result = run(make_fixture())
    captured = capture_repository_evidence(result, str(tmp_path), "execution_trace.json")
    assert captured["status"] == "CAPTURED"
    assert captured["repository_relative_path"] == (
        "Quality/Integration/evidence/runtime/execution_trace.json"
    )
    _materialize_seam_artifacts(tmp_path)

    candidate = {
        "seam": "Execution -> Execution Trace",
        "contract": "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md",
        "test": "Quality/Integration/test_repository_evidence_to_registry.py",
        "trace": captured["repository_relative_path"],
        "verification_status": "VERIFIED",
    }

    registry = load_records(tmp_path, [candidate])
    assert registry["Execution -> Execution Trace"]["state"] == "CONNECTED"
    assert registry["Execution -> Execution Trace"]["verification_status"] == "VERIFIED"


def test_repository_evidence_cannot_promote_without_verified_status(tmp_path):
    result = run(make_fixture())
    captured = capture_repository_evidence(result, str(tmp_path), "execution_trace.json")
    _materialize_seam_artifacts(tmp_path)
    candidate = {
        "seam": "Execution -> Execution Trace",
        "contract": "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md",
        "test": "Quality/Integration/test_repository_evidence_to_registry.py",
        "trace": captured["repository_relative_path"],
        "verification_status": "UNVERIFIED",
    }

    try:
        load_records(tmp_path, [candidate])
    except ValueError as exc:
        assert str(exc) == "evidence not verified: Execution -> Execution Trace"
    else:
        raise AssertionError("unverified repository evidence must not become CONNECTED")
