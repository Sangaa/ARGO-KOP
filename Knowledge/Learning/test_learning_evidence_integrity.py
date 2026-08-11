from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def test_promotion_candidate_preserves_provenance():
    candidate = read("SYNTHETIC_LEARNING_PROMOTION_CANDIDATE_001.md")
    assert "SYNTHETIC_LEARNING_FIXTURE_001.md" in candidate
    assert "SYNTHETIC_LEARNING_EXPERIMENT_001.md" in candidate
    assert "SYNTHETIC_LEARNING_EVIDENCE_001.md" in candidate


def test_candidate_scope_is_narrow():
    candidate = read("SYNTHETIC_LEARNING_PROMOTION_CANDIDATE_001.md")
    assert "AWAITING PROMOTION GATE EVALUATION" in candidate
    assert "universal rules" in candidate
