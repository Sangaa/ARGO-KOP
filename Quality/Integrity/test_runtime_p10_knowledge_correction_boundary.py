from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "Knowledge/Learning"
RUNTIME_CONTEXT = ROOT / "Runtime/Context"
sys.path.insert(0, str(KNOWLEDGE))
sys.path.insert(0, str(RUNTIME_CONTEXT))

from knowledge_correction import assess_contradiction  # noqa: E402
from runtime_context_pipeline import evaluate_new_evidence  # noqa: E402


CONTRACT = KNOWLEDGE / "EVIDENCE_FEEDBACK_LOOP.md"


def promoted():
    return {"task_id": "SYN-P10-H", "status": "PROMOTED", "claim": "bounded"}


def test_invalid_review_inputs_fail_closed_without_mutation():
    cases = [
        (promoted(), [], True, "INVALID_EVIDENCE"),
        ({"task_id": "", "status": "PROMOTED"}, ["proof"], True, "MISSING_STABLE_TASK_ID"),
        ({"task_id": "SYN-P10-H", "status": "CANDIDATE"}, ["proof"], True, "SOURCE_NOT_PROMOTED"),
        (promoted(), ["proof"], "true", "INVALID_CONTRADICTION_SIGNAL"),
    ]
    for record, evidence, contradiction, reason in cases:
        snapshot = dict(record)
        result = evaluate_new_evidence(record, evidence, contradiction=contradiction)
        assert result["status"] == "HOLD"
        assert result["reason"] == reason
        assert record == snapshot


def test_valid_promoted_contradiction_stays_review_only():
    record = promoted()
    snapshot = dict(record)
    result = assess_contradiction(record, evidence=["contradictory-proof"], contradiction=True)
    assert result["status"] == "DEMOTION_REVIEW_REQUIRED"
    assert result["record_id"] == "SYN-P10-H"
    assert record == snapshot
    assert "DEMOTED" not in result.values()


def test_contract_binds_fail_closed_and_review_only_boundary():
    contract = CONTRACT.read_text(encoding="utf-8")
    assert "Invalid evidence, identity, source state or contradiction signal must fail closed as `HOLD`" in contract
    assert "`DEMOTION_REVIEW_REQUIRED` remains a review proposal only" in contract
    assert "promoted record remains immutable until governed authority acts" in contract
