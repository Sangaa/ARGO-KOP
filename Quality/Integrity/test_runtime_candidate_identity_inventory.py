from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_CANDIDATES = {
    f"RUN-{index:03d}": ROOT / "Runtime" / name
    for index, name in {
        11: "RUN-011_COGNITIVE_LOOP_PROTOTYPE.md",
        12: "RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md",
        13: "RUN-013_CONTROLLED_HANDOFF.md",
        14: "RUN-014_LEARNING_PROMOTION_TEST.md",
        15: "RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md",
    }.items()
}
FOLDER_STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"


def test_runtime_candidate_artifacts_match_filename_and_document_identity():
    for run_id, path in RUNTIME_CANDIDATES.items():
        assert path.is_file(), f"missing runtime candidate artifact: {path}"
        text = path.read_text(encoding="utf-8")
        assert re.search(rf"(?m)^#\s+{re.escape(run_id)}(?:\s+—|\s*$)", text)
        assert re.search(rf"(?m)^Document ID\s*$\n\s*{re.escape(run_id)}\s*$", text) or re.search(
            rf"(?m)^Document ID\s*:\s*{re.escape(run_id)}\s*$", text
        )
        assert "Integrity Hold" in text


def test_runtime_folder_status_declares_the_same_candidate_scope():
    text = FOLDER_STATUS.read_text(encoding="utf-8")
    for run_id in RUNTIME_CANDIDATES:
        assert run_id in text
    assert "Filename / internal ID alignment — PASS FOR DIRECTLY REVIEWED RUN-011..015" in text


def test_runtime_candidate_identity_guard_does_not_promote_prototype_authority():
    text = FOLDER_STATUS.read_text(encoding="utf-8")
    assert "CROSS-LAYER INTEGRATION HOLD" in text
    assert "prototype evidence" in text
    assert "not globally certified" in text or "global Runtime certification" in text
