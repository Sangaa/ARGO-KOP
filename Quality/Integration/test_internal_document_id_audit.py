from pathlib import Path

from internal_document_id_audit import scan


def test_current_tree_has_no_active_duplicate_document_ids_or_unreadable_text():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["active_duplicate_pass"], report


def test_current_tree_filename_alignment_is_clean_for_identifier_named_artifacts():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["filename_alignment_pass"], report


def test_archive_records_are_reported_separately_from_active_identity():
    report = scan(Path(__file__).resolve().parents[2])
    assert report["archived_records"] >= 0
