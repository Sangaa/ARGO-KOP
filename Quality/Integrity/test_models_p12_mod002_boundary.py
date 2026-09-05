import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MOD002_BOUNDARY_EVIDENCE_2026-09-05_E.tsv"
MOD002 = ROOT / "Models" / "MOD-002_ENTITY_MODEL.md"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_mod002_boundary_cohort_is_exact() -> None:
    rows = _rows()
    assert len(rows) == 12
    assert [row["candidate_id"] for row in rows] == [f"P12-E-{i:03d}" for i in range(1, 13)]


def test_direct_related_documents_are_references_only() -> None:
    rows = _rows()[:9]
    source = MOD002.read_text(encoding="utf-8")
    for row in rows:
        target = ROOT / row["target_path"]
        assert target.is_file(), row
        assert f"`{row['target_path']}`" in source, row
        assert row["controlled_type"] == "REFERENCES", row
        assert row["registry_action"] == "REGISTRATION_CANDIDATE", row


def test_architecture_references_do_not_transfer_ownership_or_dependency() -> None:
    rows = {row["target_path"]: row for row in _rows()}
    assert rows["Architecture/ARC-002_COMPONENT_ARCHITECTURE.md"]["authority_disposition"] == "ARCHITECTURE_REFERENCE_NON_OWNERSHIP"
    assert rows["Architecture/ARC-006_DEPENDENCY_MODEL.md"]["authority_disposition"] == "ARCHITECTURE_REFERENCE_NON_DEPENDENCY"

    arc002 = (ROOT / "Architecture/ARC-002_COMPONENT_ARCHITECTURE.md").read_text(encoding="utf-8")
    arc006 = (ROOT / "Architecture/ARC-006_DEPENDENCY_MODEL.md").read_text(encoding="utf-8")
    assert "reference does not transfer ownership" in arc002
    assert "A textual reference to a file path does not by itself establish an architectural dependency." in arc006


def test_repository_index_and_map_are_not_entity_model_relationships() -> None:
    rows = {row["target_path"]: row for row in _rows()}
    for target in ("Repository/REP-001_MASTER_INDEX.md", "Repository/REP-002_REPOSITORY_MAP.md"):
        row = rows[target]
        assert row["controlled_type"] == "NONE"
        assert row["registry_action"] == "DO_NOT_REGISTER"

    rep001 = (ROOT / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    rep002 = (ROOT / "Repository/REP-002_REPOSITORY_MAP.md").read_text(encoding="utf-8")
    assert "Index membership therefore records inventory; it does not by itself certify the relationships" in rep001
    assert "Physical mapping records presence only." in rep002


def test_generic_consumer_classes_are_not_manufactured_into_edges() -> None:
    row = _rows()[-1]
    assert row["target_path"] == "Interfaces/*;Services/*;Runtime/*"
    assert row["controlled_type"] == "NONE"
    assert row["authority_disposition"] == "NO_CONCRETE_EDGE_PROVEN"
    assert row["registry_action"] == "HOLD_NO_REGISTRATION"

    source = MOD002.read_text(encoding="utf-8")
    assert "interfaces and services consuming entity identity" in source
    assert "runtime consumers" in source
