"""End-to-end evidence proof from the actual controlled runner to registry promotion.

This test intentionally uses the runtime-produced trace and outcome rather than a
hand-authored trace fixture. It proves the bounded handoff only after runtime
lineage verification and explicit evidence materialization. The registry remains
an evidence gate, not a semantic authority.
"""

import json

from connected_spine_runner import run
from synthetic_task_fixture import make_fixture
from runtime_evidence_capture import capture_repository_evidence
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence
from verified_seam_evidence_loader import load_records


def test_actual_runtime_trace_and_outcome_can_form_registry_evidence(tmp_path):
    result = run(make_fixture())
    execution = result["execution"]
    outcome = result["outcome"]

    assert execution["execution_trace_id"] == execution["trace"]["trace_id"]
    assert outcome["execution_trace_ids"] == [execution["execution_trace_id"]]
    assert outcome["evidence_trace_ids"] == outcome["execution_trace_ids"]

    lineage = verify_runtime_outcome_evidence(result)
    assert lineage["status"] == "VERIFIED"
    assert lineage["execution_trace_id"] == execution["execution_trace_id"]

    captured = capture_repository_evidence(
        result,
        repository_root=str(tmp_path),
        relative_name="execution_trace.json",
    )
    assert captured["status"] == "CAPTURED"
    assert captured["trace_id"] == execution["execution_trace_id"]
    trace_relative = captured["repository_relative_path"]
    assert trace_relative == "Quality/Integration/evidence/runtime/execution_trace.json"

    contract = tmp_path / "evidence/contracts/execution_outcome_contract.md"
    test_artifact = tmp_path / "evidence/tests/execution_outcome_test.py"
    contract.parent.mkdir(parents=True)
    test_artifact.parent.mkdir(parents=True)
    contract.write_text("# bounded execution/outcome contract\n", encoding="utf-8")
    test_artifact.write_text("# executable integration test artifact\n", encoding="utf-8")

    candidate = {
        "seam": "Execution -> Outcome",
        "contract": "evidence/contracts/execution_outcome_contract.md",
        "test": "evidence/tests/execution_outcome_test.py",
        "trace": trace_relative,
        "verification_status": lineage["status"],
    }

    registry = load_records(tmp_path, [candidate])
    assert registry["Execution -> Outcome"]["state"] == "CONNECTED"
    assert registry["Execution -> Outcome"]["trace"] == trace_relative

    persisted_payload = json.loads(
        (tmp_path / trace_relative).read_text(encoding="utf-8")
    )
    assert persisted_payload["trace_id"] == outcome["execution_trace_ids"][0]


def test_governed_capture_rejects_absolute_target(tmp_path):
    result = capture_repository_evidence(
        {"execution": {"trace": {"record_type": "EXECUTION_TRACE"}}},
        repository_root=str(tmp_path),
        relative_name="/escape.json",
    )
    assert result == {"status": "HOLD", "reason": "INVALID_EVIDENCE_TARGET"}


def test_governed_capture_rejects_parent_traversal(tmp_path):
    result = capture_repository_evidence(
        {"execution": {"trace": {"record_type": "EXECUTION_TRACE"}}},
        repository_root=str(tmp_path),
        relative_name="../escape.json",
    )
    assert result == {"status": "HOLD", "reason": "INVALID_EVIDENCE_TARGET"}
