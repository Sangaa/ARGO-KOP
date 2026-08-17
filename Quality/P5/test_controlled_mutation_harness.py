from __future__ import annotations

import pytest

from Tools.P5_CONTROLLED_MUTATION_HARNESS import HarnessError, Mutation, build_candidate


SOURCE = """# Fixture

## Alpha
alpha body

## Beta
beta body

## Gamma
gamma body
"""


def test_update_preserves_keep_sections() -> None:
    candidate, report = build_candidate(
        SOURCE,
        [Mutation("C-001", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    assert "beta changed" in candidate
    assert report["keep_mismatches"] == []
    assert report["unexpected_changes"] == 0
    assert report["status"] == "PRE_COMMIT_VALIDATED"


def test_missing_section_aborts() -> None:
    with pytest.raises(HarnessError, match="IDENTITY/AUTHORITY-GAP"):
        build_candidate(
            SOURCE,
            [Mutation("C-002", "SEC-099", "UPDATE", "## Missing\ncontent\n")],
        )


def test_remove_not_supported_until_explicitly_gated() -> None:
    with pytest.raises(HarnessError, match="UNSUPPORTED_ACTION"):
        build_candidate(SOURCE, [Mutation("C-003", "SEC-002", "REMOVE")])


def test_keep_mismatch_is_detected() -> None:
    # A mutation cannot silently rewrite a non-target section. The harness
    # should fail before commit when that happens.
    bad_source = SOURCE.replace("alpha body", "alpha body\nunexpected")
    candidate, report = build_candidate(
        bad_source,
        [Mutation("C-004", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    assert "unexpected" in candidate
    assert report["keep_mismatches"] == []
