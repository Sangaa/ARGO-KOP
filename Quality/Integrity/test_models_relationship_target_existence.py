"""Bounded Models relationship-target existence guard.

This guard validates only explicitly inspected relationship targets. It does
not certify relationship authority, reciprocity, or the complete Models graph.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

INSPECTED_TARGETS = {
    "Models/MOD-002_ENTITY_MODEL.md": [
        "Models/MOD-003_DOCUMENT_MODEL.md",
        "Models/MOD-004_MEMORY_MODEL.md",
        "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
        "Architecture/ARC-002_COMPONENT_ARCHITECTURE.md",
        "Architecture/ARC-006_DEPENDENCY_MODEL.md",
        "Architecture/ARC-009_ARCHITECTURE_DECISIONS.md",
        "Architecture/ARC-010_EVOLUTION_MODEL.md",
        "Governance/GOV-004_DOCUMENT_METADATA.md",
        "Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md",
    ],
    "Models/MOD-004_MEMORY_MODEL.md": [
        "Models/MOD-002_ENTITY_MODEL.md",
        "Models/MOD-003_DOCUMENT_MODEL.md",
        "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
        "Architecture/ARC-009_ARCHITECTURE_DECISIONS.md",
        "Architecture/ARC-010_EVOLUTION_MODEL.md",
        "Runtime/RUN-004_CONTEXT_LOADING.md",
        "Runtime/RUN-008_RUNTIME_STATE.md",
        "Runtime/RUN-009_RECOVERY.md",
        "Engine/ENG-007_LEARNING_ENGINE.md",
    ],
}


def test_inspected_models_relationship_targets_exist():
    for source, targets in INSPECTED_TARGETS.items():
        source_text = (ROOT / source).read_text(encoding="utf-8")
        for target in targets:
            assert target in source_text, f"declared target missing from source: {source} -> {target}"
            assert (ROOT / target).is_file(), f"relationship target path unresolved: {source} -> {target}"


def test_guard_remains_bounded_to_inspected_relationships():
    assert set(INSPECTED_TARGETS) == {
        "Models/MOD-002_ENTITY_MODEL.md",
        "Models/MOD-004_MEMORY_MODEL.md",
    }
