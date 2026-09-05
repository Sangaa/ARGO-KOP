import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MOD003_BOUNDARY_EVIDENCE_2026-09-05_F.tsv"
MOD003 = ROOT / "Models" / "MOD-003_DOCUMENT_MODEL.md"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_mod003_boundary_cohort_is_exact() -> None:
    rows = _rows()
    assert len(rows) == 10
    assert [row["candidate_id"] for row in rows] == [f"P12-F-{i:03d}" for i in range(1, 11)]


def test_direct_related_documents_are_bounded_references() -> None:
    source = MOD003.read_text(encoding="utf-8")
    for row in _rows()[:9]:
        assert (ROOT / row["target_path"]).is_file(), row
        assert f"`{row['target_path']}`" in source, row
        assert row["controlled_type"] == "REFERENCES", row
        assert row["registry_action"] == "REGISTRATION_CANDIDATE", row


def test_repository_reference_direction_comes_from_mod003_not_index_membership() -> None:
    rows = {row["target_path"]: row for row in _rows()}
    assert rows["Repository/REP-001_MASTER_INDEX.md"]["authority_disposition"] == "DIRECT_SOURCE_REFERENCE_NOT_INDEX_DERIVATION"
    assert rows["Repository/REP-002_REPOSITORY_MAP.md"]["authority_disposition"] == "DIRECT_SOURCE_REFERENCE_NOT_MAPPING_DERIVATION"

    rep001 = (ROOT / "Repository/REP-001_MASTER_INDEX.md").read_text(encoding="utf-8")
    rep002 = (ROOT / "Repository/REP-002_REPOSITORY_MAP.md").read_text(encoding="utf-8")
    assert "Index membership therefore records inventory; it does not by itself certify the relationships" in rep001
    assert "Physical mapping records presence only." in rep002


def test_gov004_is_metadata_authority_not_reverse_document_model_dependency() -> None:
    gov004 = (ROOT / "Governance/GOV-004_DOCUMENT_METADATA.md").read_text(encoding="utf-8")
    assert "Defines the mandatory metadata and identity rules for canonical ARGO KOP documents." in gov004
    assert "Models/MOD-003_DOCUMENT_MODEL.md" not in gov004


def test_generic_runtime_template_validator_ripple_is_not_manufactured_into_edge() -> None:
    row = _rows()[-1]
    assert row["target_path"] == "Runtime/*;Templates/*;Quality/*"
    assert row["controlled_type"] == "NONE"
    assert row["authority_disposition"] == "NO_CONCRETE_CONSUMER_EDGE_PROVEN"
    assert row["registry_action"] == "HOLD_NO_REGISTRATION"

    source = MOD003.read_text(encoding="utf-8")
    assert "runtime/document loading dependencies" in source
    assert "affected document templates and validators" in source


def test_mod004_reverse_dependency_remains_separate_from_mod003_reference() -> None:
    mod004 = (ROOT / "Models/MOD-004_MEMORY_MODEL.md").read_text(encoding="utf-8")
    assert "# Semantic Dependencies" in mod004
    assert "`Models/MOD-003_DOCUMENT_MODEL.md`" in mod004
    assert "These dependencies describe semantic model composition only." in mod004
