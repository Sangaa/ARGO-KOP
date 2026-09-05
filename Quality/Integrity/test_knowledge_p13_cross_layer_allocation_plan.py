from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "REP-014_PRIORITY13_KNOWLEDGE_CROSS_LAYER_ALLOCATION_PLAN_2026-09-05_C.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"

SOURCE_PATHS = {
    "KNW-001": ROOT / "Knowledge" / "KNW-001_KNOWLEDGE_MODEL.md",
    "KNW-002": ROOT / "Knowledge" / "KNW-002_KNOWLEDGE_CLASSIFICATION.md",
    "KNW-003": ROOT / "Knowledge" / "KNW-003_KNOWLEDGE_RELATIONSHIPS.md",
    "KNW-004": ROOT / "Knowledge" / "KNW-004_KNOWLEDGE_LIFECYCLE.md",
    "KNW-005": ROOT / "Knowledge" / "KNW-005_KNOWLEDGE_GOVERNANCE.md",
    "KNW-006": ROOT / "Knowledge" / "KNW-006_KNOWLEDGE_QUALITY.md",
    "KNW-007": ROOT / "Knowledge" / "KNW-007_KNOWLEDGE_BASELINE.md",
    "KNW-008": ROOT / "Knowledge" / "KNW-008_KNOWLEDGE_TRACEABILITY.md",
    "KNW-009": ROOT / "Knowledge" / "KNW-009_KNOWLEDGE_EVOLUTION.md",
    "KNW-010": ROOT / "Knowledge" / "KNW-010_KNOWLEDGE_MAINTENANCE.md",
}

EXCLUDED_EXISTING = {
    ("KNW-002", "MOD-011"),
    ("KNW-003", "MOD-011"),
    ("KNW-004", "MOD-001"),
    ("KNW-004", "MOD-011"),
    ("KNW-009", "MOD-011"),
}


def _rows():
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "id\tsource\ttarget\ttype\ttarget_path\tevidence_class\tstate"
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        assert len(parts) == 7
        rows.append(parts)
    return rows


def _declares_identity(text: str, target: str) -> bool:
    if f"Document ID: {target}" in text or f"Document ID\n{target}" in text or f"Document ID\r\n{target}" in text:
        return True
    first_h1 = next((line.strip() for line in text.splitlines() if line.startswith("# ")), "")
    return first_h1 == f"# {target}"


def test_cross_layer_plan_has_exact_vacant_contiguous_cohort() -> None:
    rows = _rows()
    assert len(rows) == 39
    assert [r[0] for r in rows] == [f"REL-{i:03d}" for i in range(168, 207)]
    assert len({(r[1], r[2], r[3]) for r in rows}) == 39
    registry = REGISTRY.read_text(encoding="utf-8")
    for rel_id, *_ in rows:
        assert f"| {rel_id} |" not in registry


def test_every_candidate_is_directly_declared_and_target_exists() -> None:
    for rel_id, source, target, rel_type, target_path, evidence, state in _rows():
        assert rel_type == "REFERENCES"
        assert evidence == "DIRECT_RELATED_DOCUMENTS"
        assert state == "P13_CROSS_LAYER_DOCUMENTARY_NON_DEPENDENCY"
        source_text = SOURCE_PATHS[source].read_text(encoding="utf-8")
        assert f"`{target_path}`" in source_text, (rel_id, source, target_path)
        target_file = ROOT / target_path
        assert target_file.is_file(), (rel_id, target_path)
        target_text = target_file.read_text(encoding="utf-8")
        assert _declares_identity(target_text, target), (rel_id, target)


def test_stronger_or_existing_seams_are_not_duplicated() -> None:
    planned_pairs = {(r[1], r[2]) for r in _rows()}
    assert planned_pairs.isdisjoint(EXCLUDED_EXISTING)
    registry = REGISTRY.read_text(encoding="utf-8")
    assert "| REL-010 | KNW-002 | MOD-011 | CONSUMES |" in registry
    assert "| REL-110 | KNW-003 | MOD-011 | REFERENCES |" in registry
    assert "| REL-081 | KNW-004 | MOD-001 | REFERENCES |" in registry
    assert "| REL-111 | KNW-004 | MOD-011 | REFERENCES |" in registry
    assert "| REL-014 | KNW-009 | MOD-011 | CONSUMES |" in registry
