"""Bounded bidirectional relationship guards for currently inspected Models edges.

These tests validate only explicitly declared related-document edges. They do not
certify the full Models graph or elevate any domain status.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_entity_document_model_relationship_is_explicit_on_both_sides():
    entity = _text("Models/MOD-002_ENTITY_MODEL.md")
    document = _text("Models/MOD-003_DOCUMENT_MODEL.md")

    assert "`Models/MOD-003_DOCUMENT_MODEL.md`" in entity
    assert "`Models/MOD-002_ENTITY_MODEL.md`" in document


def test_memory_knowledge_source_relationship_is_explicit_on_both_sides():
    memory = _text("Models/MOD-004_MEMORY_MODEL.md")
    source = _text("Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md")

    assert "`Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`" in memory
    assert "`Models/MOD-004_MEMORY_MODEL.md`" in source


def test_models_domain_status_remains_unpromoted():
    status = _text("Models/_FOLDER_STATUS.md")
    assert "INTEGRITY HOLD / STAGED RECONSTRUCTION" in status
    assert "Canonical: Pending consolidated validation" in status
