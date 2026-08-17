import pytest

from Tools.controlled_rep014_rel003_candidate_builder import build_candidate


def _source() -> str:
    return """# REP-014\n\n## Relationship Record\n\n| ID | Source | Target | Type | State |\n|---|---|---|---|---|\n| REL-003 | ENG-004 | SRV-005 | PRODUCES | Revalidated within inspected scope |\n\n## Current Review\n\nKeep this content byte-equivalent.\n"""


def test_builder_requires_explicit_authorization(monkeypatch):
    import Tools.controlled_rep014_rel003_candidate_builder as builder
    monkeypatch.setattr(builder, "SOURCE_BLOB_SHA", builder.git_blob_sha1(_source()))
    with pytest.raises(RuntimeError, match="AUTHORIZATION_EVIDENCE_REQUIRED"):
        build_candidate(_source(), authorization_evidence="")


def test_builder_changes_only_rel003_row_and_preserves_other_sections(monkeypatch):
    source = _source()
    import Tools.controlled_rep014_rel003_candidate_builder as builder
    monkeypatch.setattr(builder, "SOURCE_BLOB_SHA", builder.git_blob_sha1(source))
    candidate, meta = builder.build_candidate(
        source,
        authorization_evidence="EJR-207 explicit semantic direction decision; candidate only.",
    )
    assert "| REL-003 | SRV-005 | ENG-004 | CONSUMES | Revalidation Required |" in candidate
    assert "Keep this content byte-equivalent." in candidate
    assert meta["unexpected_changes"] == 0
    assert meta["target_state"] == "Revalidation Required"
