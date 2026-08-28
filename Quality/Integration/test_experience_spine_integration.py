"""CI bridge for the bounded Experience Spine candidate."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "Knowledge" / "Learning" / "experience_spine.py"
SPEC = importlib.util.spec_from_file_location("experience_spine_candidate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
build_experience_packet = MODULE.build_experience_packet


def _context():
    return {
        "task_id": "CI-EXPERIENCE-SPINE",
        "execution_identity": "GITHUB-ACTIONS:INTEGRATION",
        "domain": "repository",
        "problem_types": ["multi-instance-conflict"],
        "allowed_scopes": ["project:argo-kop"],
        "consumer_route": "HERMUZ",
        "artifact_ids": ["REP-014"],
        "repository_ref": "pull-request-head",
        "repository_head": "github-sha",
        "concurrent_work_refs": ["PR-64", "PR-66"],
    }


def _record(source_identity="HORUS:review"):
    return {
        "knowledge_id": "K-MULTI-INSTANCE-001",
        "status": "PROMOTED",
        "knowledge_scope": "project:argo-kop",
        "evidence": ["Repository/MUT-2026-08-28-HORUS-EXPERIENCE-SPINE-002.md"],
        "evidence_state": "PROVEN",
        "authority_state": "NON-AUTHORITATIVE",
        "source_identity": source_identity,
        "source_type": "HORUS-ANALYSIS",
        "consumer_routes": ["HERMUZ"],
        "domains": ["repository"],
        "problem_types": ["multi-instance-conflict"],
        "artifact_ids": ["REP-014"],
        "failure_classes": ["IDENTITY_COLLISION"],
        "applicability_boundaries": ["current repository workset"],
        "counterindications": ["unverified branch state"],
        "pattern": "reconcile concurrent paths before mutation",
    }


def test_integration_packet_preserves_execution_and_source_lineage():
    packet = build_experience_packet([_record()], _context())
    assert packet["status"] == "READY"
    assert packet["execution_identity"] == "GITHUB-ACTIONS:INTEGRATION"
    assert packet["execution_context"]["concurrent_work_refs"] == ["PR-64", "PR-66"]
    assert packet["experience_items"][0]["source_identity"] == "HORUS:review"
    assert packet["experience_items"][0]["authority_state"] == "NON-AUTHORITATIVE"
    assert packet["authority_boundary"] == "RETRIEVAL_DOES_NOT_PROMOTE_OR_AUTHORIZE"


def test_integration_packet_holds_on_parallel_identity_collision():
    packet = build_experience_packet(
        [_record("HORUS:instance-a"), _record("HORUS:instance-b")],
        _context(),
    )
    assert packet["status"] == "HOLD"
    assert packet["reason"] == "DUPLICATE_KNOWLEDGE_IDENTITY"
    assert packet["duplicate_knowledge_ids"] == ["K-MULTI-INSTANCE-001"]
    assert packet["experience_items"] == []


