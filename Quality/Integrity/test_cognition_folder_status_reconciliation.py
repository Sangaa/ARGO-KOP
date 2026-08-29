from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cognition_folder_status_preserves_inventory_and_authority_boundaries():
    status = (ROOT / "Cognition/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    required = [
        "COG-001_COGNITIVE_NAVIGATION.md",
        "COG-009_COGNITIVE_SESSION.md",
        "COG-010_INTELLIGENCE_LAYER.md",
        "COG-010_REASONING_PIPELINE_BOUNDARY.md",
        "COGNITION_PASS_CONTRACT.md",
        "CONTEXT_CONFLICT_HANDLING_CONTRACT.md",
        "CONTEXT_MEMORY_SELECTION_CONTRACT.md",
        "CONTEXT_PROVENANCE_CONTRACT.md",
        "REASONING_CONTEXT_BRIDGE_CONTRACT.md",
        "REASONING_HOLD_AND_STATE_BEHAVIOR.md",
        "SESSION_CONTEXT_REHYDRATION_CONTRACT.md",
        "TRACEABLE_REASONING_CONTRACT.md",
        "context_conflict_detector.py",
        "context_loader.py",
        "context_memory_selector.py",
        "reasoning_context_bridge.py",
        "reasoning_hold.py",
        "reasoning_packet_classifier.py",
        "session_context_rehydrator.py",
        "traceable_reasoning.py",
        "test_context_conflict_detector.py",
        "test_context_loader.py",
        "test_context_memory_selector.py",
        "test_reasoning_context_bridge.py",
        "test_reasoning_hold.py",
        "test_reasoning_packet_classifier.py",
        "test_session_context_rehydrator.py",
        "test_traceable_reasoning.py",
    ]
    for item in required:
        assert item in status

    assert "35 tracked files" in status
    assert "INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN" in status
    assert "COG010_FILENAME_DUPLICATION != TWO ACTIVE AUTHORITIES" in status
    assert "COG010_REASONING_PIPELINE_BOUNDARY = CANDIDATE / NOT PROMOTED" in status
    assert "LEARNING HANDOFF != AUTOMATIC CANONICAL TRUTH" in status
    assert "COGNITIVE BENEFIT PROOF" in status
