from pathlib import Path


def test_service_metadata_gaps_are_explicitly_bounded_until_revalidation():
    root = Path(__file__).resolve().parents[2]
    matrix = (root / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(encoding="utf-8")
    for service_id, filename in (
        ("SVC-003", "Services/SRV-003_MEMORY_SERVICE.md"),
        ("SVC-006", "Services/SRV-006_SEARCH_SERVICE.md"),
        ("SVC-007", "Services/SRV-007_LOGGING_SERVICE.md"),
        ("SVC-008", "Services/SRV-008_INDEX_SERVICE.md"),
    ):
        text = (root / filename).read_text(encoding="utf-8")
        assert service_id in matrix
        assert "Version" in text
        assert "Status" in text
        assert "Category" in text
        assert "Development Baseline" not in text


def test_service_metadata_gap_is_not_conflated_with_runtime_or_release_authority():
    root = Path(__file__).resolve().parents[2]
    version = (root / "Release/VERSION.md").read_text(encoding="utf-8")
    matrix = (root / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md").read_text(encoding="utf-8")
    assert "3.2.1" in version
    assert "METADATA GAP / REVALIDATION_REQUIRED" in matrix
