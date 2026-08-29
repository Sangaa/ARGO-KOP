from pathlib import Path


def test_qlt001_semantics_match_current_runtime_and_governance():
    text = Path("Quality/QLT-001_QUALITY_ASSURANCE.md").read_text(encoding="utf-8")

    assert "Governance/GOV-005_REVIEW_STANDARD.md" in text
    assert "GOV-005_DOCUMENT_LIFECYCLE_STANDARD.md" not in text

    assert "Automated Rollback" not in text
    assert "FAULT" in text and "HOLD" in text
    assert "Runtime/RUN-009_RECOVERY.md" in text

    assert "immutable audit log entry saved under `Logs/`" not in text
    assert "QUALITY REQUIREMENT != UNIVERSAL EXECUTION PROOF" in text
    assert "FAULT/HOLD + GOVERNED RECOVERY != AUTOMATIC ROLLBACK" in text
    assert "TRACEABILITY REQUIREMENT != IMMUTABLE LOG-STORAGE PROOF" in text

    # Empty historical QLT placeholders remain non-capabilities; this repair
    # must not silently promote them.
    assert "does not promote the empty legacy placeholders QLT-002..005" in text
