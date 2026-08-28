"""CI-visible integration checks for the advisory Experience Spine projection."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "Knowledge" / "Learning" / "experience_spine.py"
SPEC = importlib.util.spec_from_file_location("experience_spine_clean", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
build_experience_packet = MODULE.build_experience_packet


def _profile(**overrides):
    profile = {
        "source_identity": "HERMUZ:verified-learning",
        "source_type": "HERMUZ-ENGINEERING",
        "evidence_state": "PROVEN",
        "authority_state": "ADVISORY",
        "consumer_routes": ["HERMUZ"],
        "evidence_group": "P4-C12-INCIDENT",
        "domains": ["repository"],
        "problem_types": ["consumer-impact-reconciliation"],
        "artifact_ids": ["REP-014"],
        "failure_classes": ["STALE_SEMANTIC_ASSERTION"],
        "applicability_boundaries": ["repository semantic-state changes"],
        "counterindications": ["no current-state change"],
        "contradicts": [],
        "superseded_by": [],
    }
    profile.update(overrides)
    return profile


def _record(knowledge_id="K-P4-C12", **overrides):
    record = {
        "knowledge_id": knowledge_id,
        "task_id": "P4-C12",
        "session_id": "2026-08-28",
        "status": "PROMOTED",
        "validation": "VALIDATED",
        "knowledge_scope": "project:argo-kop",
        "evidence": ["Repository/MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001.md"],
        "provenance_preserved": True,
        "pattern": "semantic-state mutations require assertion-consumer impact search",
        "experience_profile": _profile(),
    }
    record.update(overrides)
    return record


def _context():
    return {
        "task_id": "CI-EXPERIENCE-SPINE",
        "execution_identity": "GITHUB-ACTIONS:INTEGRATION",
        "domain": "repository",
        "problem_types": ["consumer-impact-reconciliation"],
        "allowed_scopes": ["project:argo-kop"],
        "consumer_route": "HERMUZ",
        "artifact_ids": ["REP-014"],
        "failure_classes": ["STALE_SEMANTIC_ASSERTION"],
        "repository_ref": "pull-request-head",
        "repository_head": "github-sha",
        "concurrent_work_refs": ["PR-66", "PR-69"],
    }


def test_packet_preserves_execution_source_and_authority_boundaries():
    packet = build_experience_packet([_record()], _context())
    assert packet["status"] == "READY"
    assert packet["execution_identity"] == "GITHUB-ACTIONS:INTEGRATION"
    assert packet["execution_context"]["concurrent_work_refs"] == ["PR-66", "PR-69"]
    item = packet["experience_items"][0]
    assert item["source_identity"] == "HERMUZ:verified-learning"
    assert item["lifecycle_state"] == "PROMOTED"
    assert item["validation_state"] == "VALIDATED"
    assert item["authority_state"] == "ADVISORY"
    assert packet["authority_boundary"] == "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE"


def test_correlated_records_are_visible_without_false_independence():
    second = _record("K-P4-C12-SECOND")
    packet = build_experience_packet([_record(), second], _context())
    assert packet["status"] == "READY"
    assert packet["correlated_evidence_groups"] == [
        {
            "evidence_group": "P4-C12-INCIDENT",
            "knowledge_ids": ["K-P4-C12", "K-P4-C12-SECOND"],
            "independence": "CORRELATED_NOT_INDEPENDENT",
        }
    ]


def test_conflicting_experience_requires_review_before_reuse_decision():
    first = _record("K-A")
    first["experience_profile"] = _profile(contradicts=["K-B"], evidence_group="A")
    second = _record("K-B")
    second["experience_profile"] = _profile(contradicts=["K-A"], evidence_group="B")
    packet = build_experience_packet([first, second], _context())
    assert packet["status"] == "REVIEW_REQUIRED"
    assert packet["conflicts"] == [["K-A", "K-B"]]
    assert packet["reasoning_start"][0:2] == ["CURRENT_EVIDENCE", "APPLICABLE_AUTHORITY"]
