from pathlib import Path

from full_stack_connectivity_audit import audit, build_reference_graph, discover_files, normalize_local_reference


def test_discovery_excludes_git_metadata(tmp_path: Path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "hidden.md").write_text("hidden", encoding="utf-8")
    (tmp_path / "A.md").write_text("# A", encoding="utf-8")
    assert Path("A.md") in [p.relative_to(tmp_path) for p in discover_files(tmp_path)]
    assert not any("hidden.md" in p.as_posix() for p in discover_files(tmp_path))


def test_reference_graph_detects_local_markdown_link(tmp_path: Path):
    (tmp_path / "A.md").write_text("[B](B.md)", encoding="utf-8")
    (tmp_path / "B.md").write_text("# B", encoding="utf-8")
    graph, broken = build_reference_graph(tmp_path)
    assert graph["A.md"] == {"B.md"}
    assert broken == []


def test_reference_graph_reports_missing_local_target(tmp_path: Path):
    (tmp_path / "A.md").write_text("[missing](missing.md)", encoding="utf-8")
    _, broken = build_reference_graph(tmp_path)
    assert broken == [{"source": "A.md", "reference": "missing.md"}]


def test_reference_normalization_strips_fragment_and_query(tmp_path: Path):
    source = tmp_path / "docs" / "A.md"
    source.parent.mkdir()
    target = tmp_path / "docs" / "B.md"
    target.write_text("# B", encoding="utf-8")
    assert normalize_local_reference("B.md#section?view=1", source, tmp_path) == "docs/B.md"


def test_reference_normalization_accepts_backslash_paths(tmp_path: Path):
    source = tmp_path / "docs" / "A.md"
    source.parent.mkdir()
    target = tmp_path / "docs" / "B.md"
    target.write_text("# B", encoding="utf-8")
    assert normalize_local_reference("B\\B.md", source, tmp_path) == "docs/B/B.md"


def test_reference_normalization_ignores_external_and_mailto_links(tmp_path: Path):
    source = tmp_path / "A.md"
    assert normalize_local_reference("https://example.com/x", source, tmp_path) is None
    assert normalize_local_reference("mailto:test@example.com", source, tmp_path) is None


def test_audit_reports_unreferenced_source_candidate(tmp_path: Path):
    (tmp_path / "module.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert result["status"] == "AUDIT_COMPLETE"
    assert "module.py" in result["orphan_candidates"]


def test_audit_does_not_treat_orphan_as_proven_failure(tmp_path: Path):
    (tmp_path / "module.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert "require architectural review" in result["note"]


def test_audit_reports_runtime_source_without_sibling_test(tmp_path: Path):
    runtime = tmp_path / "Runtime"
    runtime.mkdir()
    (runtime / "worker.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert "Runtime/worker.py" in result["untested_candidates"]


def test_audit_accepts_sibling_runtime_test(tmp_path: Path):
    runtime = tmp_path / "Runtime"
    runtime.mkdir()
    (runtime / "worker.py").write_text("def run(): pass", encoding="utf-8")
    (runtime / "test_worker.py").write_text("def test_run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert "Runtime/worker.py" not in result["untested_candidates"]


def test_audit_exposes_layer_inventory_and_evidence_classes(tmp_path: Path):
    (tmp_path / "Runtime").mkdir()
    (tmp_path / "Runtime" / "worker.py").write_text("def run(): pass", encoding="utf-8")
    result = audit(tmp_path)
    assert result["layer_file_counts"]["Runtime / Execution"] == 1
    assert "RUNTIME_REACHABLE" in result["evidence_classes"]
