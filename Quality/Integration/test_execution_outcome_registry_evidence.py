"""Governed registry evidence proof for the Execution -> Outcome seam."""

import json

from connected_spine_runner import run
from runtime_evidence_capture import capture_repository_evidence
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence
from synthetic_task_fixture import make_fixture
from verified_seam_evidence_loader import load_records


def test_execution_to_outcome_can_form_verified_registry_evidence(tmp_path):
    result = run(make_fixture())
    execution = result["execution"]
    outcome = result["outcome"]

    lineage = verify_runtime_outcome_evidence(result)
    assert lineage["status"] == "VERIFIED"

    captured = capture_repository_evidence(
        result,
        repository_root=str(tmp_path),
        relative_name="execution_outcome_trace.json",
    )
    assert captured["status"] == "CAPTURED"
    trace_relative = captured["repository_relative_path"]

    contract = tmp_path / "evidence/contracts/execution_outcome_contract.md"
    test_artifact = tmp_path / "evidence/tests/execution_outcome_test.py"
    contract.parent.mkdir(parents=True)
    test_artifact.parent.mkdir(parents=True)
    contract.write_text("# existing bounded execution/outcome contract\n", encoding="utf-8")
    test_artifact.write_text("# existing direct integration test\n", encoding="utf-8")

    registry = load_records(
        tmp_path,
        [{
            "seam": "Execution -> Outcome",
            "contract": "evidence/contracts/execution_outcome_contract.md",
            "test": "evidence/tests/execution_outcome_test.py",
            "trace": trace_relative,
            "verification_status": lineage["status"],
        }],
    )

    assert registry["Execution -> Outcome"]["state"] == "CONNECTED"
    assert registry["Execution -> Outcome"]["trace"] == trace_relative

    persisted = json.loads((tmp_path / trace_relative).read_text(encoding="utf-8"))
    assert persisted["trace_id"] == execution["execution_trace_id"]
    assert outcome["execution_trace_ids"] == [execution["execution_trace_id"]]


def test_execution_to_outcome_unverified_evidence_is_not_admitted(tmp_path):
    candidate = {
        "seam": "Execution -> Outcome",
        "contract": "evidence/contracts/execution_outcome_contract.md",
        "test": "evidence/tests/execution_outcome_test.py",
        "trace": "Quality/Integration/evidence/runtime/execution_outcome_trace.json",
        "verification_status": "UNVERIFIED",
    }

    try:
        load_records(tmp_path, [candidate])
    except ValueError as exc:
        assert str(exc) == "evidence not verified: Execution -> Outcome"
    else:
        raise AssertionError("unverified execution/outcome evidence must not become CONNECTED")
