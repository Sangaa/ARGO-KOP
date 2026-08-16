from pathlib import Path


def test_connected_spine_runner_has_material_execution_to_outcome_lineage_proof():
    root = Path(__file__).resolve().parents[2]
    test = (root / "Runtime/Execution/test_connected_spine_runner.py").read_text(encoding="utf-8")
    runner = (root / "Runtime/Execution/connected_spine_runner.py").read_text(encoding="utf-8")
    assert "record_execution_outcome" in runner
    assert 'result["execution"]["execution_trace_id"] == result["outcome"]["execution_trace_ids"][0]' in test
    assert 'result["outcome"]["evidence_trace_ids"] == result["outcome"]["execution_trace_ids"]' in test
    assert 'result["outcome"]["result"] == "INCONCLUSIVE"' in test


def test_connected_spine_runner_preserves_authorization_stop_boundary():
    root = Path(__file__).resolve().parents[2]
    test = (root / "Runtime/Execution/test_connected_spine_runner.py").read_text(encoding="utf-8")
    assert "test_missing_authorization_stops_before_execution_and_outcome" in test
    assert 'result["outcome"] is None' in test
