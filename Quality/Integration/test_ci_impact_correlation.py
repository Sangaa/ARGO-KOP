"""Regression tests for the P6 CI-impact correlation helper."""

from ci_impact_correlation import correlate_paths


def test_direct_matrix_mapping_is_reported_without_promotion() -> None:
    records = correlate_paths(
        ["Engine/ENG-006_EXECUTION_ENGINE.md"],
        "| ENG-001 | `Engine/ENG-006_EXECUTION_ENGINE.md` | SRV-009 |",
        "",
    )
    assert records[0]["status"] == "MAPPED"
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"
    assert records[0]["matrix_evidence"]


def test_unmapped_path_is_explicit_not_inferred() -> None:
    records = correlate_paths(
        ["Unknown/NewFile.md"],
        "| REL-001 | `Known/File.md` |",
        "| REL-001 | `Known/Other.md` |",
    )
    assert records[0]["status"] == "UNMAPPED"
    assert records[0]["matrix_evidence"] == []
    assert records[0]["relationship_evidence"] == []
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


def test_same_basename_does_not_create_false_mapping() -> None:
    records = correlate_paths(
        ["Runtime/NewFile.md"],
        "| REL-001 | `Repository/NewFile.md` |",
        "| REL-002 | `Docs/NewFile.md` |",
    )
    assert records[0]["status"] == "UNMAPPED"
    assert records[0]["matrix_evidence"] == []
    assert records[0]["relationship_evidence"] == []
    assert records[0]["promotion"] == "NO_AUTO_PROMOTION"


if __name__ == "__main__":
    test_direct_matrix_mapping_is_reported_without_promotion()
    test_unmapped_path_is_explicit_not_inferred()
    test_same_basename_does_not_create_false_mapping()
    print("P6_CI_IMPACT_CORRELATION_REGRESSION=PASS")
