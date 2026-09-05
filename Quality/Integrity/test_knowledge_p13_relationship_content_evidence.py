from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B_EVIDENCE.tsv"
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def _rows() -> list[list[str]]:
    lines = EVIDENCE.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "source\ttarget_or_claim\tclassification\tcurrent_disposition\tevidence"
    return [line.split("\t") for line in lines[1:] if line.strip()]


def test_known_content_contradictions_are_explicitly_bounded() -> None:
    rows = _rows()
    repairs = {(r[0], r[1]) for r in rows if r[3] == "REPAIR_REQUIRED"}
    assert repairs == {
        ("KNW-006", "Repository always prevails"),
        ("KNW-007", "approved repository knowledge is baseline/authoritative"),
        ("KNW-008", "complete history + historical knowledge shall never be deleted"),
        ("KNW-010", "maintenance shall never Delete Approved Knowledge"),
    }


def test_existing_stable_relationship_ids_are_preserved() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    expected = (
        "| REL-010 | KNW-002 | MOD-011 | CONSUMES |",
        "| REL-014 | KNW-009 | MOD-011 | CONSUMES |",
        "| REL-081 | KNW-004 | MOD-001 | REFERENCES |",
        "| REL-110 | KNW-003 | MOD-011 | REFERENCES |",
        "| REL-111 | KNW-004 | MOD-011 | REFERENCES |",
    )
    for row in expected:
        assert row in registry


def test_related_documents_are_not_promoted_to_dependencies_by_evidence_only() -> None:
    rows = _rows()
    candidates = [r for r in rows if r[3].startswith("CANDIDATE_")]
    assert candidates
    assert all(r[2] == "REFERENCES" for r in candidates)
