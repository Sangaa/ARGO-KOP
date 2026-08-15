"""Prove the Learning Readiness -> Learning Pipeline seam has traceable evidence."""

import shutil
from pathlib import Path

from connected_spine_runner import run
from learning_pipeline_integration import assess_for_promotion
from runtime_evidence_capture import capture_repository_evidence
from runtime_outcome_evidence_verifier import verify_runtime_outcome_evidence
from verified_seam_evidence_loader import load_records
from synthetic_task_fixture import make_fixture


def test_learning_pipeline_seam_can_form_verified_registry_evidence(tmp_path):
    result = run(make_fixture())
    execution = result["execution"]

    lineage = verify_runtime_outcome_evidence(result)
    assert lineage["status"] == "VERIFIED"

    learning = assess_for_promotion(
        decision_id="DEC-LEARN-1",
        execution_id="EXEC-LEARN-1",
        outcome={
            "outcome_id": "OUT-LEARN-1",
            "result": "SUCCESS",
            "evidence_trace_ids": [execution["execution_trace_id"]],
            "execution_trace_ids": [execution["execution_trace_id"]],
            "confidence": "HIGH",
        },
    )
    assert learning["status"] == "READY_FOR_PROMOTION_REVIEW"
    assert learning["report"]["knowledge_promoted"] is False

    captured = capture_repository_evidence(
        result,
        repository_root=str(tmp_path),
        relative_name="learning_pipeline_trace.json",
    )
    assert captured["status"] == "CAPTURED"

    contract = Path("Runtime/Learning/LEARNING_PIPELINE_INTEGRATION_CONTRACT.md")
    test_artifact = Path("Runtime/Learning/test_learning_pipeline_integration.py")
    assert contract.is_file()
    assert test_artifact.is_file()

    tmp_contract = tmp_path / contract
    tmp_test = tmp_path / test_artifact
    tmp_contract.parent.mkdir(parents=True, exist_ok=True)
    tmp_test.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(contract, tmp_contract)
    shutil.copyfile(test_artifact, tmp_test)

    candidate = {
        "seam": "Learning Readiness -> Learning Pipeline",
        "contract": str(contract).replace("\\", "/"),
        "test": str(test_artifact).replace("\\", "/"),
        "trace": captured["repository_relative_path"],
        "verification_status": lineage["status"],
    }

    registry = load_records(tmp_path, [candidate])
    assert registry["Learning Readiness -> Learning Pipeline"]["state"] == "CONNECTED"
    assert registry["Learning Readiness -> Learning Pipeline"]["trace"] == captured["repository_relative_path"]
