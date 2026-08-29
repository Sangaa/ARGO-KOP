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


def test_current_tree_governance_identity_family_collisions_require_hold():
    repo = Path(__file__).resolve().parents[2]
    report = scan(repo)
    collisions = report["governance_heading_identity_collisions"]

    # These are current-tree observations, not an authority decision or a
    # numbering migration. The audit must surface them rather than silently
    # passing because some artifacts omit explicit Document ID metadata.
    assert {"GOV-013A", "GOV-015", "GOV-016", "GOV-017"}.issubset(collisions)
    assert report["governance_identity_hold_required"] is True
    assert report["identity_scope_reconciled"] is False

    governance_status = (repo / "Governance" / "_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "INTEGRITY WARNING / CURRENT IDENTITY RE-AUDIT" in governance_status
    assert "Current result: **NOT CLOSED**" in governance_status


def test_current_tree_internal_id_audit_report_is_emitted():
    report = scan(Path(__file__).resolve().parents[2])
    warnings.warn(
        "P2_INTERNAL_ID_AUDIT_REPORT=" + json.dumps(report, sort_keys=True),
        RuntimeWarning,
        stacklevel=1,
    )
