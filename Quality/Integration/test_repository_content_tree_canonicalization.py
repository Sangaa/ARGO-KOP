from pathlib import Path


def test_repository_content_tree_uses_current_baseline_and_specification_path():
    root = Path(__file__).resolve().parents[2]
    tree = (root / "Repository" / "REP-013_REPOSITORY_CONTENT_TREE.md").read_text(encoding="utf-8")
    assert "Development Baseline: 3.2.1" in tree
    assert "Specifications/01-Knowledge-Organization.md" in tree
    assert "Specifications/SPEC-001-KNOWLEDGE-ORGANIZATION.md" not in tree
