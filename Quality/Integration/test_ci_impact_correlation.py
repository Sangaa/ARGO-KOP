"""Regression tests for the P6 CI-impact correlation helper.

These include controlled synthetic tests plus bounded canonical-repository
regressions for implementation and control-surface policy.
"""

from pathlib import Path

from ci_impact_correlation import classify_execution_evidence, correlate_paths


SYNTHETIC_SCOPE = """
| Path Class | P6 Scope | Authority | Evidence | Correlation Rule |
|---|---|---|---|---|
| `Engine/**` | `IN_SCOPE` | synthetic-test-authority | fixture | test |
| `Runtime/**` | `IN_SCOPE` | synthetic-test-authority | fixture | test |
| `Docs/**` | `OUT_OF_SCOPE` | synthetic-test-authority | fixture | test |
| `EJR/**` | `UNRESOLVED` | synthetic-governance-gap | fixture | test |
"""


def test_direct_matrix_mapping_is_reported_without_promotion() -> None:
    records = correlate_paths(["Engine/ENG-006_EXECUTION_ENGINE.md"], "| ENG-001 | `Engine/ENG-006_EXECUTION_ENGINE.md` | SRV-009 |", "", SYNTHETIC_SCOPE)
    assert records[0]["status"] == "MAPPED"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"
    assert records[0]["matrix_evidence"]


def test_in_scope_without_mapping_remains_unmapped() -> None:
    records = correlate_paths(["Engine/NewFile.md"], "| REL-001 | `Known/File.md` |", "| REL-001 | `Known/Other.md` |", SYNTHETIC_SCOPE)
    assert records[0]["eligibility"] == "IN_SCOPE"
    assert records[0]["status"] == "UNMAPPED"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


def test_out_of_scope_is_not_applicable_not_unmapped() -> None:
    records = correlate_paths(["Docs/NewFile.md"], "| REL-001 | `Docs/NewFile.md` |", "| REL-002 | `Docs/NewFile.md` |", SYNTHETIC_SCOPE)
    assert records[0]["eligibility"] == "OUT_OF_SCOPE"
    assert records[0]["status"] == "NOT_APPLICABLE"


def test_unresolved_is_policy_unresolved_not_unmapped() -> None:
    records = correlate_paths(["EJR/EJR-001.md"], "| REL-001 | `EJR/EJR-001.md` |", "| REL-002 | `EJR/EJR-001.md` |", SYNTHETIC_SCOPE)
    assert records[0]["eligibility"] == "UNRESOLVED"
    assert records[0]["status"] == "POLICY_UNRESOLVED"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


def test_unknown_path_is_unresolved_not_an_implicit_mapping_failure() -> None:
    records = correlate_paths(["Unknown/NewFile.md"], "| REL-001 | `Known/File.md` |", "| REL-001 | `Known/Other.md` |", SYNTHETIC_SCOPE)
    assert records[0]["eligibility"] == "UNRESOLVED"
    assert records[0]["status"] == "POLICY_UNRESOLVED"


def test_successful_stale_run_is_valid_execution_not_execution_failure() -> None:
    assert classify_execution_evidence("HEAD-NEW", "HEAD-OLD", "HEAD-OLD", True) == "VALID_EXECUTION_STALE_BASELINE"


def test_successful_exact_sha_chain_is_current_execution() -> None:
    assert classify_execution_evidence("HEAD", "HEAD", "HEAD", True) == "VALID_CURRENT_EXECUTION"


def test_current_run_with_mismatched_artifact_is_not_current_execution() -> None:
    assert classify_execution_evidence("HEAD", "HEAD", "ARTIFACT-OLD", True) == "ARTIFACT_IDENTITY_MISMATCH"


def test_current_run_with_missing_artifact_evidence_is_explicit() -> None:
    assert classify_execution_evidence("HEAD", "HEAD", "", True) == "ARTIFACT_EVIDENCE_MISSING"


def test_missing_identity_evidence_is_not_execution_failure() -> None:
    assert classify_execution_evidence("", "", "", True) == "IDENTITY_EVIDENCE_MISSING"


def test_failed_run_remains_execution_failure() -> None:
    assert classify_execution_evidence("HEAD", "HEAD", "HEAD", False) == "EXECUTION_FAILED"


def _canonical_sources() -> tuple[str, str, str]:
    root = Path(__file__).resolve().parents[2]
    matrix = (root / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(encoding="utf-8")
    registry = (root / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text(encoding="utf-8")
    scope = (root / "Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md").read_text(encoding="utf-8")
    return matrix, registry, scope


def test_current_repository_maps_run010_handoff_test_without_promotion() -> None:
    matrix, registry, scope = _canonical_sources()
    record = correlate_paths(["Quality/Integration/test_run010_eng006_handoff_contract.py"], matrix, registry, scope)[0]
    assert record["eligibility"] == "IN_SCOPE"
    assert record["status"] == "MAPPED"
    assert record["promotion"] == "NO_AUTO_PROMOTION"
    assert record["matrix_evidence"]


def test_current_repository_maps_p6_control_surfaces_without_promotion() -> None:
    matrix, registry, scope = _canonical_sources()
    paths = [
        "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md",
        "Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md",
        "Quality/Integration/test_ci_impact_correlation.py",
    ]
    records = correlate_paths(paths, matrix, registry, scope)
    assert [(r["eligibility"], r["status"], r["promotion"]) for r in records] == [
        ("IN_SCOPE", "MAPPED", "NO_AUTO_PROMOTION"),
        ("IN_SCOPE", "MAPPED", "NO_AUTO_PROMOTION"),
        ("IN_SCOPE", "MAPPED", "NO_AUTO_PROMOTION"),
    ]


def test_mutation_matrix_is_not_applicable_to_direct_p6_impact_even_if_mentioned() -> None:
    matrix, registry, scope = _canonical_sources()
    path = "Repository/MUT-2026-08-29-P6-CONTROL-SURFACE-CORRELATION-017_MUTATION_MATRIX.md"
    evidence_with_exact_path = matrix + "\n" + path
    record = correlate_paths([path], evidence_with_exact_path, registry, scope)[0]
    assert record["eligibility"] == "OUT_OF_SCOPE"
    assert record["status"] == "NOT_APPLICABLE"
    assert record["promotion"] == "NO_AUTO_PROMOTION"


if __name__ == "__main__":
    test_direct_matrix_mapping_is_reported_without_promotion()
    test_in_scope_without_mapping_remains_unmapped()
    test_out_of_scope_is_not_applicable_not_unmapped()
    test_unresolved_is_policy_unresolved_not_unmapped()
    test_unknown_path_is_unresolved_not_an_implicit_mapping_failure()
    test_successful_stale_run_is_valid_execution_not_execution_failure()
    test_successful_exact_sha_chain_is_current_execution()
    test_current_run_with_mismatched_artifact_is_not_current_execution()
    test_current_run_with_missing_artifact_evidence_is_explicit()
    test_missing_identity_evidence_is_not_execution_failure()
    test_failed_run_remains_execution_failure()
    test_current_repository_maps_run010_handoff_test_without_promotion()
    test_current_repository_maps_p6_control_surfaces_without_promotion()
    test_mutation_matrix_is_not_applicable_to_direct_p6_impact_even_if_mentioned()
    print("P6_CI_IMPACT_CORRELATION_REGRESSION=PASS")
