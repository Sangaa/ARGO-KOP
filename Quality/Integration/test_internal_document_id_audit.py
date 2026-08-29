from pathlib import Path
import json
import warnings

from internal_document_id_audit import scan


def test_current_tree_has_no_active_duplicate_document_ids_or_unreadable_text():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["active_duplicate_pass"], (
        f"duplicates={report['duplicate_active_ids']} unreadable={report['unreadable']}"
    )


def test_current_tree_filename_alignment_is_clean_for_identifier_named_artifacts():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["filename_alignment_pass"], (
        f"filename_mismatches={report['filename_internal_id_mismatches']}"
    )


def test_archive_records_are_reported_separately_from_active_identity():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["archived_records"] >= 0


def test_current_tree_governance_document_heading_identities_are_unique_after_migration():
    repo = Path(__file__).resolve().parents[2]
    report = scan(repo)
    collisions = report["governance_heading_identity_collisions"]

    # Document-level identity is evaluated only across Governance documents,
    # not arbitrary section headings, source comments, templates or mutation
    # evidence in other namespaces.
    assert collisions == {}, collisions
    assert report["governance_identity_hold_required"] is False

    # Assert a stable post-migration semantic checkpoint, not transient wording
    # from an earlier migration-in-progress state. Whole-repository identity
    # scope may still remain open independently of Governance identity closure.
    governance_status = (repo / "Governance" / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED" in governance_status
    assert "CONTENT REVIEW HOLDS REMAIN" in governance_status


def test_migrated_governance_ids_have_distinct_document_level_owners():
    repo = Path(__file__).resolve().parents[2]
    report = scan(repo)
    for identity in ("GOV-013", "GOV-013A", "GOV-014", "GOV-015", "GOV-016", "GOV-017", "GOV-019", "GOV-020", "GOV-021", "GOV-022", "GOV-023", "GOV-024", "GOV-025", "GOV-026", "GOV-027"):
        assert identity not in report["governance_heading_identity_collisions"]


def test_current_tree_internal_id_audit_report_is_emitted():
    report = scan(Path(__file__).resolve().parents[2])
    warnings.warn(
        "P2_INTERNAL_ID_AUDIT_REPORT=" + json.dumps(report, sort_keys=True),
        RuntimeWarning,
        stacklevel=1,
    )
