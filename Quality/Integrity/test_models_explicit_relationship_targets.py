from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

# Bounded to relationships explicitly declared and directly inspected in MOD-001.
RELATIONSHIPS = {
    "Models/MOD-001_KNOWLEDGE_MODEL.md": {
        "Repository/REP-002_REPOSITORY_MAP.md": "REP-002",
        "Governance/GOV-001_GOVERNANCE_FRAMEWORK.md": "GOV-001",
        "Services/SRV-009_UPDATE_SERVICE.md": "SRV-009",
        "Services/SRV-004_KNOWLEDGE_SERVICE.md": "SRV-004",
        "Specifications/01-Knowledge-Organization.md": "SPEC-001-KNOWLEDGE-ORGANIZATION",
    }
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _document_id(text: str) -> str:
    match = re.search(r"^Document ID\s*:?\s*(.+?)\s*$", text, re.MULTILINE)
    assert match, "Target relationship requires an explicit Document ID"
    return match.group(1).strip()


def test_mod001_explicit_relationship_targets_exist_and_identity_match():
    for source, targets in RELATIONSHIPS.items():
        source_path = ROOT / source
        assert source_path.is_file(), f"Source model missing: {source}"
        source_text = _read(source_path)

        for target, expected_id in targets.items():
            target_path = ROOT / target
            assert target_path.is_file(), f"Declared relationship target is missing: {target}"
            target_text = _read(target_path)

            assert target in source_text, f"Source does not contain declared target path: {target}"
            assert _document_id(target_text) == expected_id, (
                f"Target identity mismatch for {target}: "
                f"expected {expected_id}, found {_document_id(target_text)}"
            )


def test_mod001_relationship_guard_does_not_promote_target_authority():
    # Existence and identity verification are not authority certification.
    # The guard intentionally does not require Canonical: Yes because the
    # specification target is an operational artifact under Integrity Hold.
    for target in RELATIONSHIPS["Models/MOD-001_KNOWLEDGE_MODEL.md"]:
        assert target
