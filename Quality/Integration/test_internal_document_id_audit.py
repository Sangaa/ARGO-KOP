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

    assert identities["Cognition/COG-009_COGNITIVE_SESSION.md"] == "COG-009"
    assert identities["Decision/DEC-009_DECISION_GOVERNANCE.md"] == "DEC-009"
    assert identities["Release/RELEASE_MANIFEST.md"] == "REL-001"
    assert identities["PROJECT_BOOTSTRAP.md"] == "BOOTSTRAP-001"
    assert identities["PROJECT_STATUS.md"] == "PROJECT_STATUS"


def test_current_tree_has_no_conflicting_qualified_metadata_document_ids():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["metadata_document_id_conflicts"] == [], (
        f"metadata_conflicts={report['metadata_document_id_conflicts']}"
    )


def test_human_h1_title_does_not_override_explicit_document_identity(tmp_path, monkeypatch):
    (tmp_path / "Repository").mkdir()
    (tmp_path / "Repository" / "REP-001_MASTER_INDEX.md").write_text(
        "`PROJECT_STATUS.md`\n", encoding="utf-8"
    )
    (tmp_path / "PROJECT_STATUS.md").write_text(
        "# ARGO KOP — Current Project Status\n\nDocument ID: PROJECT_STATUS\nStatus: Integrity Warning\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "internal_document_id_audit._git_files",
        lambda root: [root / "Repository/REP-001_MASTER_INDEX.md", root / "PROJECT_STATUS.md"],
    )

    report = scan(tmp_path)
    assert report["document_ids_by_path"]["PROJECT_STATUS.md"] == "PROJECT_STATUS"
    assert report["identity_sources_by_path"]["PROJECT_STATUS.md"] == "DOCUMENT_ID_FIELD"
    assert report["metadata_document_id_conflicts"] == []


def test_structural_h1_fallback_accepts_unseen_namespace_without_allowlist(tmp_path, monkeypatch):
    (tmp_path / "Repository").mkdir()
    (tmp_path / "Repository" / "REP-001_MASTER_INDEX.md").write_text(
        "`Novel/NOVEL-321_EXAMPLE.md`\n", encoding="utf-8"
    )
    (tmp_path / "Novel").mkdir()
    (tmp_path / "Novel" / "NOVEL-321_EXAMPLE.md").write_text(
        "# NOVEL-321 — Example governed artifact\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "internal_document_id_audit._git_files",
        lambda root: [
            root / "Repository/REP-001_MASTER_INDEX.md",
            root / "Novel/NOVEL-321_EXAMPLE.md",
        ],
    )

    report = scan(tmp_path)
    assert report["document_ids_by_path"]["Novel/NOVEL-321_EXAMPLE.md"] == "NOVEL-321"
    assert report["identity_sources_by_path"]["Novel/NOVEL-321_EXAMPLE.md"] == "FIRST_H1_FALLBACK"


def test_body_document_id_reference_does_not_override_referencing_document_identity(tmp_path, monkeypatch):
    (tmp_path / "Repository").mkdir()
    (tmp_path / "Repository" / "REP-001_MASTER_INDEX.md").write_text("", encoding="utf-8")
    (tmp_path / "Memory").mkdir()
    journal = tmp_path / "Memory" / "EJR-288_EXAMPLE.md"
    journal.write_text(
        "# EJR-288 — Repair step\n\n"
        "## Status\nCLOSED\n\n"
        "## Action Executed\nCreated another artifact.\n\n"
        "Document ID: `P6-SCOPE-001`\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "internal_document_id_audit._git_files",
        lambda root: [root / "Repository/REP-001_MASTER_INDEX.md", journal],
    )

    report = scan(tmp_path)
    assert report["document_ids_by_path"]["Memory/EJR-288_EXAMPLE.md"] == "EJR-288"
    assert report["identity_sources_by_path"]["Memory/EJR-288_EXAMPLE.md"] == "FIRST_H1_FALLBACK"
    assert report["metadata_document_id_conflicts"] == []


def test_explicit_child_identity_may_coexist_with_parent_series_h1(tmp_path, monkeypatch):
    (tmp_path / "Repository").mkdir()
    index = tmp_path / "Repository" / "REP-001_MASTER_INDEX.md"
    delta = tmp_path / "Repository" / "REP-020_SESSION_DELTA_P24.md"
    index.write_text("", encoding="utf-8")
    delta.write_text(
        "# REP-020 — SESSION DELTA P24\n\n"
        "Platform: ARGO KOP\n"
        "Document ID: REP-020-P24-DELTA\n"
        "Status: Evidence Addendum / Non-Authority\n\n"
        "## Purpose\nEvidence only.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "internal_document_id_audit._git_files",
        lambda root: [index, delta],
    )

    report = scan(tmp_path)
    assert report["document_ids_by_path"]["Repository/REP-020_SESSION_DELTA_P24.md"] == "REP-020-P24-DELTA"
    assert report["identity_sources_by_path"]["Repository/REP-020_SESSION_DELTA_P24.md"] == "DOCUMENT_ID_FIELD"
    assert report["metadata_document_id_conflicts"] == []


def test_multiple_qualified_metadata_document_ids_are_a_real_conflict(tmp_path, monkeypatch):
    (tmp_path / "Repository").mkdir()
    index = tmp_path / "Repository" / "REP-001_MASTER_INDEX.md"
    artifact = tmp_path / "Repository" / "NOVEL-321_EXAMPLE.md"
    index.write_text("", encoding="utf-8")
    artifact.write_text(
        "# NOVEL-321 — Example\n\n"
        "Platform: ARGO KOP\n"
        "Document ID: NOVEL-321\n"
        "Status: Draft\n"
        "Document ID: NOVEL-322\n\n"
        "## Purpose\nSynthetic conflict.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "internal_document_id_audit._git_files",
        lambda root: [index, artifact],
    )

    report = scan(tmp_path)
    assert report["metadata_document_id_conflicts"] == [
        "Repository/NOVEL-321_EXAMPLE.md => metadata IDs NOVEL-321, NOVEL-322"
    ]
    assert report["identity_scope_reconciled"] is False


def test_current_tree_internal_id_audit_report_is_emitted():
    report = scan(Path(__file__).resolve().parents[2])
    warnings.warn(
        "P2_INTERNAL_ID_AUDIT_REPORT=" + json.dumps(report, sort_keys=True),
        RuntimeWarning,
        stacklevel=1,
    )
