import pytest

from Tools.controlled_rep014_rel001_candidate_builder import build_candidate


def _source() -> str:
    return """# REP-014\n\n## Relationship Record\n\n| ID | Source | Target | Type | State |\n|---|---|---|---|---|\n| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | Revalidation Required |\n\n## Current Review\n\nKeep this content byte-equivalent.\n"""


def test_builder_requires_explicit_authorization():
    with pytest.raises(RuntimeError, match="AUTHORIZATION_EVIDENCE_REQUIRED"):
        build_candidate(
            _source(),
            target_state="Verified",
            authorization_evidence="",
        )


def test_builder_changes_only_rel001_row_and_preserves_other_sections(monkeypatch):
    source = _source()
    # This fixture is intentionally synthetic; patch the source hash expected by
    # the production builder so the candidate-construction logic can be tested
    # without mutating REP-014 or depending on a live checkout.
    import Tools.controlled_rep014_rel001_candidate_builder as builder

    monkeypatch.setattr(builder, "SOURCE_BLOB_SHA", builder.git_blob_sha1(source))
    candidate, meta = builder.build_candidate(
        source,
        target_state="Verified",
        authorization_evidence="TEST AUTHORIZATION ONLY; NO CANONICAL MUTATION.",
    )

    assert "| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | Verified |" in candidate
    assert "Keep this content byte-equivalent." in candidate
    assert meta["unexpected_changes"] == 0
    assert meta["current_state"] == "Revalidation Required"
    assert meta["target_state"] == "Verified"
