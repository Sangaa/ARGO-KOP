from pathlib import Path
import re


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


def _document_id(text: str) -> str:
    patterns = (
        r"^Document ID\s*:?\s*(.+?)\s*$",
        r"^Document ID\s*$\n\s*(.+?)\s*$",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1).strip()
    raise AssertionError("Target has no readable Document ID")


def _expected_id(path: str) -> str:
    filename = Path(path).name
    match = re.match(r"^([A-Z]+-\d+)(?:_|\.)", filename)
    assert match, f"Target filename has no formal ID prefix: {path}"
    return match.group(1)


def test_inspected_models_relationship_targets_have_identity_consistent_with_filename():
    for source, targets in INSPECTED_TARGETS.items():
        assert (ROOT / source).is_file()
        for target in targets:
            path = ROOT / target
            assert path.is_file(), f"relationship target path unresolved: {source} -> {target}"
            actual_id = _document_id(path.read_text(encoding="utf-8"))
            expected_id = _expected_id(target)
            assert actual_id == expected_id, (
                f"relationship target identity drift: {target}: "
                f"filename={expected_id}, document_id={actual_id}"
            )


def test_identity_guard_does_not_infer_authority_or_dependency_direction():
    # Identity agreement is necessary evidence only. Authority and direction
    # remain separately governed and tested.
    assert INSPECTED_TARGETS
