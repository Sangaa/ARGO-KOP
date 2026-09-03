from pathlib import Path

from Runtime.Prototype.cognitive_loop_harness import run
from Runtime.Prototype.learning_promotion_gate import candidate_from_trace, evaluate


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def _trace():
    return run(
        {
            "task_id": "REL-059-TRACE",
            "session_id": "P10-D",
            "active_state": "outcome_observed",
            "evidence": ["source:rel059"],
            "knowledge": ["rule:learning-promotion"],
            "requested_outcome": "prepare safe proposal",
        },
        human_approved=True,
    )


def _candidate(**overrides):
    values = {
        "observed_result": "proposal accepted",
        "pattern": "validated proposal structure",
        "confidence": 0.95,
        "promotion_authority": False,
        "governing_conflict": False,
    }
    values.update(overrides)
    return candidate_from_trace(_trace(), **values)


def test_action_authority_does_not_become_learning_authority():
    trace = _trace()
    assert trace["authorization"]["status"] == "AUTHORIZED"
    assert evaluate(_candidate()) == {"status": "HOLD", "reason": "PROMOTION_AUTHORITY_MISSING"}
    assert trace["result"] == {"executed": False, "external_side_effect": False}


def test_trace_provenance_crosses_only_the_explicit_candidate_adapter():
    item = _candidate(promotion_authority=True)
    assert item["task_id"] == "REL-059-TRACE"
    assert item["session_id"] == "P10-D"
    assert item["evidence"] == ["source:rel059"]
    assert item["validation"] == "VALIDATED"
    assert evaluate(item) == {"status": "PROMOTION_ELIGIBLE", "promote": True}


def test_conflict_and_incomplete_identity_fail_closed():
    assert evaluate(_candidate(promotion_authority=True, governing_conflict=True)) == {
        "status": "HOLD",
        "reason": "GOVERNING_CONFLICT",
    }
    blank = _candidate(promotion_authority=True)
    blank["task_id"] = None
    result = evaluate(blank)
    assert result["status"] == "HOLD"
    assert result["reason"] == "CANDIDATE_INCOMPLETE"
    assert result["invalid"] == ["task_id"]


def test_rel059_registry_scope_is_exact_and_not_promoted():
    registry = REGISTRY.read_text(encoding="utf-8")
    assert registry.count(
        "| REL-059 | RUN-014 | RUN-011 | VALIDATES | "
        "**TRACE-TO-LEARNING-CANDIDATE / EXECUTABLE-TESTED / "
        "SEPARATE-PROMOTION-AUTHORITY** |"
    ) == 1
    for stronger_type in ("DEPENDS_ON", "CONSUMES", "IMPLEMENTS", "GOVERNS"):
        assert f"| REL-059 | RUN-014 | RUN-011 | {stronger_type} |" not in registry
    assert "This is **not** a complete graph." in registry
