from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_decision_status_matches_current_inventory_and_hold_boundary():
    status = (ROOT / "Decision/_FOLDER_STATUS.md").read_text(encoding="utf-8")
    index = (ROOT / "Decision/DEC-010_DECISION_INDEX.md").read_text(encoding="utf-8")

    required_status_items = [
        "DEC-001_DECISION_MODEL.md",
        "DEC-010_DECISION_INDEX.md",
        "AUTHORIZATION_AND_EXECUTION_BOUNDARY.md",
        "AUTHORIZATION_STATE_BOUNDARY.md",
        "DECISION_PASS_CONTRACT.md",
        "decision_context_contract.md",
        "authorization_gate.py",
        "decision_pass.py",
        "decision_trace_producer.py",
        "test_authorization_and_execution_plan.py",
        "test_authorization_state_boundary.py",
        "test_decision_context_contract.py",
        "test_decision_pass.py",
        "test_decision_trace_producer.py",
    ]
    for item in required_status_items:
        assert item in status

    for i in range(1, 11):
        assert f"DEC-{i:03d}" in status

    assert "22 tracked files" in status
    assert "INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN" in status
    assert "DECISION_MEMORY != DECISION AUTHORITY" in status

    assert "Last Updated: 2026-08-29" in index
    assert "Status: Approved / Integrity Hold / Revalidated" in index
    assert "INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN" in index
    assert "Module Status\n\nCompleted" not in index
    assert "YYYY-MM-DD" not in index
