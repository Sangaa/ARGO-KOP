from pathlib import Path


def test_decision_memory_preserves_evidence_and_revision_traceability():
    root = Path(__file__).resolve().parents[2]
    model = (root / "Memory/Decision_Memory/DM-001_DECISION_RECORD_MODEL.md").read_text(encoding="utf-8")
    revision = (root / "Memory/Decision_Memory/DM-003_DECISION_EVIDENCE_AND_REVISION.md").read_text(encoding="utf-8")
    assert "does not authorize mutation of protected repository layers" in model
    assert "No Silent Rewrite" in revision
    assert "original decision" in revision
    assert "new evidence" in revision


def test_project_memory_does_not_convert_one_project_lesson_into_platform_truth():
    root = Path(__file__).resolve().parents[2]
    project = (root / "Memory/Project_Memory/PM-004_PROJECT_KNOWLEDGE_AND_LESSONS.md").read_text(encoding="utf-8")
    assert "A single project lesson is not automatically a universal rule." in project
    assert "Cross-Project Evidence" in project
    assert "Platform Knowledge Candidate" in project
    assert "does not create a Knowledge authority model" in project


def test_decision_and_project_memory_remain_candidate_integrity_hold_domains():
    root = Path(__file__).resolve().parents[2]
    index = (root / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    assert "Memory/Decision_Memory/DM-001_DECISION_RECORD_MODEL.md" in index
    assert "Memory/Project_Memory/PM-004_PROJECT_KNOWLEDGE_AND_LESSONS.md" in index
    assert "Candidate / Integrity Hold" in index
