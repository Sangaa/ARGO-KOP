from pathlib import Path

from full_stack_connectivity_audit import audit, build_reference_graph, discover_files


def test_discovery_excludes_git_metadata(tmp_path: Path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "hidden.md").write_text("hidden", encoding="utf-8")
    (tmp_path / "A.md").write_text("# A", encoding="utf-8")
    assert Path("A.md") in [p.relative_to(tmp_path) for p in discover_files(tmp_path)]
    assert not any("hidden.md" in p.as_posix() for p in discover_files(tmp_path))


def test_reference_graph_detects_local_markdown_link(tmp_path: Path):
    (tmp_path / "A.md").write_text("[B](B.md)", encoding="utf-8")
    (tmp_path / "B.md").write_text("# B", encoding="utf-8")
    graph = build_reference_graph(tmp_path)
    assert graph["A.md"] == {"B.md"}


def test_audit_reports_unreferenced_source_candidate(tmp_path: Path):
    (tmp_path / "module.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert result["status"] == "AUDIT_COMPLETE"
    assert "module.py" in result["orphan_candidates"]


def test_audit_does_not_treat_orphan_as_proven_failure(tmp_path: Path):
    (tmp_path / "module.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert "require architectural review" in result["note"]
