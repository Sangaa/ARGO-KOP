"""Canonical-repository P6 scope/correlation integration tests.

These tests read the real repository scope contract, REP-020 and REP-014. They
must not replace controlled synthetic tests; they prove that the implementation
actually consumes the canonical repository policy.
"""

from pathlib import Path

from ci_impact_correlation import correlate_paths, scope_for_path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCOPE = (REPO_ROOT / "Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md").read_text(
    encoding="utf-8"
)
MATRIX = (REPO_ROOT / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(
    encoding="utf-8"
)
RELATIONSHIPS = (
    REPO_ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
).read_text(encoding="utf-8")


def test_canonical_in_scope_path_is_deterministic() -> None:
    assert scope_for_path("Engine/ENG-006_EXECUTION_ENGINE.md", SCOPE) == "IN_SCOPE"
    records = correlate_paths(
        ["Engine/ENG-006_EXECUTION_ENGINE.md"], MATRIX, RELATIONSHIPS, SCOPE
    )
    assert records[0]["eligibility"] == "IN_SCOPE"
    assert records[0]["status"] in {"MAPPED", "UNMAPPED"}


def test_canonical_ejr_policy_is_out_of_scope_for_direct_p6_impact() -> None:
    path = "EJR/EJR-284_2026-08-21_HERMUZ_P6_DOCUMENTATION_PATH_POLICY_GAP.md"
    assert scope_for_path(path, SCOPE) == "OUT_OF_SCOPE"
    records = correlate_paths([path], MATRIX, RELATIONSHIPS, SCOPE)
    assert records[0]["eligibility"] == "OUT_OF_SCOPE"
    assert records[0]["status"] == "NOT_APPLICABLE"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


def test_out_of_scope_ejr_cannot_be_promoted_by_mapping_evidence() -> None:
    path = "EJR/EJR-284_2026-08-21_HERMUZ_P6_DOCUMENTATION_PATH_POLICY_GAP.md"
    records = correlate_paths(
        [path],
        f"{path}\n{MATRIX}",
        f"{path}\n{RELATIONSHIPS}",
        SCOPE,
    )
    assert records[0]["eligibility"] == "OUT_OF_SCOPE"
    assert records[0]["status"] == "NOT_APPLICABLE"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


def test_unknown_path_is_policy_unresolved_not_unmapped() -> None:
    records = correlate_paths(["Unknown/NewFile.md"], MATRIX, RELATIONSHIPS, SCOPE)
    assert records[0]["eligibility"] == "UNRESOLVED"
    assert records[0]["status"] == "POLICY_UNRESOLVED"


def test_ejr_scope_does_not_hide_independent_in_scope_path() -> None:
    paths = [
        "EJR/EJR-284_2026-08-21_HERMUZ_P6_DOCUMENTATION_PATH_POLICY_GAP.md",
        "Engine/ENG-006_EXECUTION_ENGINE.md",
    ]
    records = correlate_paths(paths, MATRIX, RELATIONSHIPS, SCOPE)
    by_path = {record["path"]: record for record in records}
    assert by_path[paths[0]]["status"] == "NOT_APPLICABLE"
    assert by_path[paths[1]]["eligibility"] == "IN_SCOPE"
    assert by_path[paths[1]]["status"] in {"MAPPED", "UNMAPPED"}


if __name__ == "__main__":
    test_canonical_in_scope_path_is_deterministic()
    test_canonical_ejr_policy_is_out_of_scope_for_direct_p6_impact()
    test_out_of_scope_ejr_cannot_be_promoted_by_mapping_evidence()
    test_unknown_path_is_policy_unresolved_not_unmapped()
    test_ejr_scope_does_not_hide_independent_in_scope_path()
    print("P6_CANONICAL_REPOSITORY_SCOPE_REGRESSION=PASS")
