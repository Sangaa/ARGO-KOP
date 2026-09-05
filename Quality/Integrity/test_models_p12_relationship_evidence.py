import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository" / "REP-014_PRIORITY12_MODELS_RELATIONSHIP_EVIDENCE_2026-09-05_B.tsv"


def _rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_models_relationship_evidence_is_exact_bounded_cohort() -> None:
    rows = _rows()
    assert len(rows) == 18
    assert [row["candidate_id"] for row in rows] == [f"P12-BR-{i:03d}" for i in range(1, 19)]
    assert {row["controlled_type"] for row in rows} == {"REFERENCES", "DEPENDS_ON"}


def test_every_candidate_has_current_source_target_and_direct_source_text() -> None:
    for row in _rows():
        source = ROOT / row["source_path"]
        target = ROOT / row["target_path"]
        assert source.is_file(), row
        assert target.is_file(), row
        source_text = source.read_text(encoding="utf-8")
        assert f"`{row['target_path']}`" in source_text, row


def test_controlled_type_matches_stable_source_representation() -> None:
    for row in _rows():
        if row["controlled_type"] == "REFERENCES":
            assert row["source_section"] == "Related Documents", row
            assert row["state"] == "DIRECT_SOURCE_VERIFIED", row
        elif row["controlled_type"] == "DEPENDS_ON":
            assert row["source_section"] == "Dependencies", row
            assert row["state"] == "DIRECT_SOURCE_AND_TARGET_VERIFIED", row
        else:
            raise AssertionError(row)


def test_reconstruction_reference_is_not_promoted_to_dependency() -> None:
    rows = _rows()
    assert not any(
        row["target_path"] == "Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md"
        and row["controlled_type"] == "DEPENDS_ON"
        for row in rows
    )
