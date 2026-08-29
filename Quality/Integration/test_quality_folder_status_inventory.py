from pathlib import Path


def test_quality_folder_status_tracks_current_top_level_inventory_without_promotion():
    text = Path("Quality/_FOLDER_STATUS.md").read_text(encoding="utf-8")

    required = [
        "Integration/",
        "Integrity/",
        "P4/",
        "P5/",
        "Tests/",
        "P5_CONTROLLED_MUTATION_RECONCILIATION_HARNESS_TEST_MATRIX_2026-08-17.md",
        "QLT-001_QUALITY_ASSURANCE.md",
        "QLT-002_DOCUMENT_VALIDATION.md",
        "QLT-003_ARCHITECTURE_REVIEW.md",
        "QLT-004_CONSISTENCY_CHECK.md",
        "QLT-005_RELEASE_REVIEW.md",
        "_FOLDER_STATUS.md",
    ]
    for item in required:
        assert item in text

    assert "TOP-LEVEL INVENTORY VERIFIED" in text
    assert "INTEGRITY HOLD" in text
    assert "Zero-byte legacy placeholder; no capability/authority established" in text
    assert "PHYSICAL PRESENCE != CAPABILITY" in text
    assert "TOP-LEVEL INVENTORY VERIFIED` does not mean `RECURSIVE INVENTORY VERIFIED" in text
    assert "Quality folder identity checked" in text
    assert "Local inventory reconciled." not in text
