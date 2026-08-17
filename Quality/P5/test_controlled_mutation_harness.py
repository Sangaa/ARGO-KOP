from __future__ import annotations

from pathlib import Path

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

FIXTURE = Path(__file__).parent / "fixtures" / "dual_path_update.md"


def test_traditional_path_update_preserves_keep_sections() -> None:
    candidate, report = build_candidate(
        SOURCE,
        [Mutation("C-001", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    assert "beta changed" in candidate
    assert report["keep_mismatches"] == []
    assert report["unexpected_changes"] == 0
    assert report["status"] == "PRE_COMMIT_VALIDATED"


def test_fixture_path_matches_traditional_path() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    candidate, report = build_candidate(
        source,
        [Mutation("F-001", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    expected, expected_report = build_candidate(
        SOURCE,
        [Mutation("C-001", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    assert candidate == expected
    assert report["status"] == expected_report["status"] == "PRE_COMMIT_VALIDATED"
    assert report["keep_mismatches"] == expected_report["keep_mismatches"] == []


def test_fixture_survives_a_second_update() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    first, first_report = build_candidate(
        source,
        [Mutation("F-002", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    second, second_report = build_candidate(
        first,
        [Mutation("F-003", "SEC-003", "UPDATE", "## Gamma\ngamma changed\n")],
    )
    assert first_report["status"] == "PRE_COMMIT_VALIDATED"
    assert second_report["status"] == "PRE_COMMIT_VALIDATED"
    assert "beta changed" in second
    assert "gamma changed" in second
    assert "alpha body" in second
    assert second_report["keep_mismatches"] == []
    assert second_report["unexpected_changes"] == 0


def test_fixture_repeat_update_keeps_prior_update_after_new_change() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    first, _ = build_candidate(
        source,
        [Mutation("F-004", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    second, report = build_candidate(
        first,
        [Mutation("F-005", "SEC-003", "UPDATE", "## Gamma\ngamma changed twice\n")],
    )
    assert "beta changed" in second
    assert "gamma changed twice" in second
    assert "alpha body" in second
    assert report["keep_mismatches"] == []
    assert report["unexpected_changes"] == 0


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
    # The fixture must prove zero-touch preservation of every untouched section.
    bad_source = SOURCE.replace("alpha body", "alpha body\nunexpected")
    candidate, report = build_candidate(
        bad_source,
        [Mutation("C-004", "SEC-002", "UPDATE", "## Beta\nbeta changed\n")],
    )
    assert "unexpected" in candidate
    assert report["keep_mismatches"] == []
