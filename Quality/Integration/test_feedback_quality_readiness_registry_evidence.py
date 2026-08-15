"""Prove governed evidence admission for Feedback Quality -> Learning Readiness."""

import shutil
from pathlib import Path

from execution_entrypoint import execute
from learning_pipeline_integration import assess_for_promotion
from runtime_evidence_capture import capture_repository_evidence
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence
from verified_seam_evidence_loader import load_records

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_feedback_quality_readiness_can_form_verified_registry_evidence(tmp_path):
    execution = execute(
        execution_id="EXEC-FEEDBACK-READINESS-REG-001",
        task_id="TASK-FEEDBACK-READINESS-REG-001",
        session_id="SESSION-FEEDBACK-READINESS-REG-001",
        source_trace_id="DECISION-TRACE-FEEDBACK-READINESS-REG-001",
        authorized=True,
        final_status="SUCCESS",
        stages=[{"name": "execute", "status": "SUCCESS"}],
    )
    trace_id = execution["execution_trace_id"]
    outcome = {
        "outcome_id": "OUT-FEEDBACK-READINESS-REG-001",
        "result": "SUCCESS",
        "evidence_trace_ids": [trace_id],
        "execution_trace_ids": [trace_id],
        "confidence": "HIGH",
    }

    result = assess_for_promotion(
        decision_id="DEC-FEEDBACK-READINESS-REG-001",
        execution_id=execution["execution_id"],
        outcome=outcome,
    )
    assert result["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert result["quality"]["quality"] == "ACCEPTABLE"
    assert result["report"]["knowledge_promoted"] is False

    runtime_result = {"execution": execution, "outcome": outcome}
    lineage = verify_runtime_outcome_evidence(runtime_result)
    assert lineage["status"] == "VERIFIED"

    captured = capture_repository_evidence(
        runtime_result,
        repository_root=str(tmp_path),
        relative_name="feedback_readiness_trace.json",
    )
    assert captured["status"] == "CAPTURED"

    contract = REPO_ROOT / "Runtime/Learning/FEEDBACK_QUALITY_GATE_CONTRACT.md"
    test_artifact = REPO_ROOT / "Quality/Integration/test_feedback_quality_to_learning_readiness.py"
    assert contract.is_file()
    assert test_artifact.is_file()

    contract_relative = "Runtime/Learning/FEEDBACK_QUALITY_GATE_CONTRACT.md"
    test_relative = "Quality/Integration/test_feedback_quality_to_learning_readiness.py"
    tmp_contract = tmp_path / contract_relative
    tmp_test = tmp_path / test_relative
    tmp_contract.parent.mkdir(parents=True, exist_ok=True)
    tmp_test.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(contract, tmp_contract)
    shutil.copyfile(test_artifact, tmp_test)

    candidate = {
        "seam": "Feedback Quality -> Learning Readiness",
        "contract": contract_relative,
        "test": test_relative,
        "trace": captured["repository_relative_path"],
        "verification_status": lineage["status"],
    }

    registry = load_records(tmp_path, [candidate])
    assert registry["Feedback Quality -> Learning Readiness"]["state"] == "CONNECTED"
    assert registry["Feedback Quality -> Learning Readiness"]["verification_status"] == "VERIFIED"


def test_unverified_feedback_readiness_evidence_cannot_promote(tmp_path):
    candidate = {
        "seam": "Feedback Quality -> Learning Readiness",
        "contract": "Runtime/Learning/FEEDBACK_QUALITY_GATE_CONTRACT.md",
        "test": "Quality/Integration/test_feedback_quality_to_learning_readiness.py",
        "trace": "Quality/Integration/evidence/runtime/feedback_readiness_trace.json",
        "verification_status": "UNVERIFIED",
    }

    try:
        load_records(tmp_path, [candidate])
    except ValueError as exc:
        assert str(exc) == "evidence not verified: Feedback Quality -> Learning Readiness"
    else:
        raise AssertionError("unverified evidence must not become CONNECTED")
