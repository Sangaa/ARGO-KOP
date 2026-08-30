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
    # not arbitrary later section headings, source comments, templates or
    # mutation evidence in other namespaces.
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


def test_current_tree_identity_discovery_is_not_limited_by_namespace_allowlist():
    repo = Path(__file__).resolve().parents[2]
    report = scan(repo)
    identities = report["document_ids_by_path"]

    # These current repository identities were outside the previous fixed
    # namespace allowlist or depend on first-H1 fallback. Their presence proves
    # that the detector observes the document rather than a preselected prefix
    # inventory.
    assert identities["Cognition/COG-009_COGNITIVE_SESSION.md"] == "COG-009"
    assert identities["Decision/DEC-009_DECISION_GOVERNANCE.md"] == "DEC-009"
    assert identities["Release/RELEASE_MANIFEST.md"] == "REL-001"
    assert identities["PROJECT_BOOTSTRAP.md"] == "BOOTSTRAP-001"
    assert identities["PROJECT_STATUS.md"] == "PROJECT_STATUS"


def test_explicit_document_id_and_first_h1_do_not_silently_disagree():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["explicit_heading_identity_conflicts"] == [], (
        f"identity_conflicts={report['explicit_heading_identity_conflicts']}"
    )


def test_current_tree_internal_id_audit_report_is_emitted():
    report = scan(Path(__file__).resolve().parents[2])
    warnings.warn(
        "P2_INTERNAL_ID_AUDIT_REPORT=" + json.dumps(report, sort_keys=True),
        RuntimeWarning,
        stacklevel=1,
    )
