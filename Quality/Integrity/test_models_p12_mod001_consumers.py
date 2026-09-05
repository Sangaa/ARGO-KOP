import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MOD001_CONSUMER_EVIDENCE_2026-09-05_C.tsv"
ARC004 = ROOT / "Architecture" / "ARC-004_LAYER_MODEL.md"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_mod001_consumer_cohort_is_exact_and_current() -> None:
    rows = _rows()
    assert len(rows) == 7
    assert [row["candidate_id"] for row in rows] == [f"P12-C-{i:03d}" for i in range(1, 8)]
    for row in rows:
        assert (ROOT / row["source_path"]).is_file(), row
        assert (ROOT / row["target_path"]).is_file(), row


def test_rel002_is_corrected_semantically_not_replaced_by_new_id() -> None:
    row = _rows()[0]
    assert row["source_path"] == "Services/SRV-004_KNOWLEDGE_SERVICE.md"
    assert row["target_path"] == "Models/MOD-001_KNOWLEDGE_MODEL.md"
    assert row["controlled_type"] == "DEPENDS_ON"
    assert row["registry_action"] == "CORRECT_EXISTING_STABLE_ID_PENDING_SAFE_REGISTRY_WRITE"

    source = (ROOT / row["source_path"]).read_text(encoding="utf-8")
    assert "Models / MOD-001 Knowledge Domain Model" in source
    assert "Models/MOD-001_KNOWLEDGE_MODEL.md" in source


def test_srv010_navigation_does_not_manufacture_semantic_edge() -> None:
    row = _rows()[1]
    assert row["controlled_type"] == "NONE"
    assert row["registry_action"] == "DO_NOT_REGISTER"


def test_knw004_related_document_is_reference_only() -> None:
    row = _rows()[2]
    assert row["controlled_type"] == "REFERENCES"
    assert row["registry_action"] == "REGISTRATION_CANDIDATE"
    source = (ROOT / row["source_path"]).read_text(encoding="utf-8")
    assert "Models/MOD-001_KNOWLEDGE_MODEL.md" in source


def test_intelligence_semantic_contracts_may_depend_downstream_on_knowledge() -> None:
    rows = _rows()[3:5]
    assert {row["source_path"] for row in rows} == {
        "Intelligence/INT-001_INTELLIGENCE_LAYER.md",
        "Intelligence/INT-002_PATTERN_EXTRACTION.md",
    }
    assert all(row["controlled_type"] == "DEPENDS_ON" for row in rows)
    assert all(row["registry_action"] == "REGISTRATION_CANDIDATE" for row in rows)

    int001 = (ROOT / "Intelligence/INT-001_INTELLIGENCE_LAYER.md").read_text(encoding="utf-8")
    int002 = (ROOT / "Intelligence/INT-002_PATTERN_EXTRACTION.md").read_text(encoding="utf-8")
    assert "complying with `Models/MOD-001`" in int001
    assert "adhering to `Models/MOD-001_KNOWLEDGE_MODEL.md`" in int002

    architecture = ARC004.read_text(encoding="utf-8")
    assert "Repository folders are physical storage locations and MUST NOT be interpreted as architectural layers automatically." in architecture
    assert "Knowledge / Specifications / Standards" in architecture
    assert "Cognition / Engine" in architecture


def test_repository_inventory_and_mapping_are_not_semantic_consumer_edges() -> None:
    rows = _rows()[5:7]
    assert all(row["controlled_type"] == "NONE" for row in rows)
    assert all(row["registry_action"] == "DO_NOT_REGISTER" for row in rows)

    rep001 = (ROOT / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    rep002 = (ROOT / "Repository/REP-002_REPOSITORY_MAP.md").read_text(encoding="utf-8")
    assert "Index membership therefore records inventory; it does not by itself certify the relationships" in rep001
    assert "Physical mapping records presence only." in rep002
