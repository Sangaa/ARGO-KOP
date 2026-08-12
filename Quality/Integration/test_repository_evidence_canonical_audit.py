from connected_spine_runner import run
from canonical_spine_integration_audit import audit
from runtime_evidence_capture import capture_repository_evidence
from synthetic_task_fixture import make_fixture


def _materialize_seam_artifacts(tmp_path):
    contract = tmp_path / "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md"
    test = tmp_path / "Quality/Integration/test_repository_evidence_canonical_audit.py"
    contract.parent.mkdir(parents=True, exist_ok=True)
    test.parent.mkdir(parents=True, exist_ok=True)
    contract.write_text("# execution trace contract\n", encoding="utf-8")
    test.write_text("# executable audit test artifact\n", encoding="utf-8")


def test_repository_backed_verified_evidence_reaches_canonical_audit(tmp_path):
    result = run(make_fixture())
    captured = capture_repository_evidence(result, str(tmp_path), "execution_trace.json")
    assert captured["status"] == "CAPTURED"
    _materialize_seam_artifacts(tmp_path)

    candidate = {
        "seam": "Execution -> Execution Trace",
        "state": "CONNECTED",
        "contract": "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md",
        "test": "Quality/Integration/test_repository_evidence_canonical_audit.py",
        "trace": captured["repository_relative_path"],
        "verification_status": "VERIFIED",
    }

    report = audit(tmp_path, {candidate["seam"]: candidate})

    assert report["status"] == "INTEGRATION_AUDIT_COMPLETE"
    assert report["evidence"][candidate["seam"]] == "CONNECTED"
    assert report["verified_connection_count"] == 1


def test_canonical_audit_rejects_unverified_repository_evidence(tmp_path):
    result = run(make_fixture())
    captured = capture_repository_evidence(result, str(tmp_path), "execution_trace.json")
    _materialize_seam_artifacts(tmp_path)
    candidate = {
        "seam": "Execution -> Execution Trace",
        "state": "CONNECTED",
        "contract": "Runtime/Execution/EXECUTION_TRACE_CONTRACT.md",
        "test": "Quality/Integration/test_repository_evidence_canonical_audit.py",
        "trace": captured["repository_relative_path"],
        "verification_status": "UNVERIFIED",
    }

    try:
        audit(tmp_path, {candidate["seam"]: candidate})
    except ValueError as exc:
        assert str(exc) == "verified seam record is not VERIFIED: Execution -> Execution Trace"
    else:
        raise AssertionError("unverified evidence must not reach canonical CONNECTED")
