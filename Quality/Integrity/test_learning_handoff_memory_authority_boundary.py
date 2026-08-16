from pathlib import Path


def test_learning_handoff_template_preserves_distinct_handoff_and_ingestion_states():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Memory/Engineering_Journal/SESSION_LEARNING_HANDOFF_TEMPLATE.md").read_text(encoding="utf-8")
    assert "Handoff Status: COMPLETE / PENDING / FAILED / BLOCKED" in text
    assert "Status: NOT STARTED / UNDER REVIEW / ACCEPTED / REJECTED / DEFERRED / APPLIED" in text
    assert "A handoff is not ingestion, and ingestion is not canonical promotion." in text


def test_learning_handoff_references_authoritative_memory_and_learning_boundaries():
    root = Path(__file__).resolve().parents[2]
    learning = (root / "Engine/ENG-007_LEARNING_ENGINE.md").read_text(encoding="utf-8")
    memory = (root / "Memory/MEM-005_MEMORY_GOVERNANCE.md").read_text(encoding="utf-8")
    knowledge = (root / "Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md").read_text(encoding="utf-8")
    assert "Session Learning Handoff" in learning
    assert "Promotion" in memory
    assert "Promotion or Reclassification Decision" in knowledge


def test_learning_handoff_has_no_path_to_implicit_platform_promotion():
    root = Path(__file__).resolve().parents[2]
    learning = (root / "Engine/ENG-007_LEARNING_ENGINE.md").read_text(encoding="utf-8")
    assert "User learning is not canonical ARGO learning by default." in learning
    assert "A useful lesson may remain permanently local." in learning
    assert "required authority approves publication" in learning
