"""Repository-wide connectivity audit for ARGO-KOP.

This audit is intentionally structural: it discovers files, extracts local
Markdown/Python references, and reports disconnected or untested-looking
areas. It does not declare architectural correctness from text alone.
"""

from __future__ import annotations

import re
from pathlib import Path

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}
REFERENCE_RE = re.compile(r"(?:\]\(|from\s+|import\s+)([^\s)]+)")


def discover_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*")
        if p.is_file() and not any(part in IGNORED_DIRS for part in p.parts)
    )


def _relative(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def local_reference_candidates(text: str) -> set[str]:
    refs: set[str] = set()
    for match in REFERENCE_RE.findall(text):
        candidate = match.strip("`'\"")
        if candidate.startswith(("http://", "https://")):
            continue
        refs.add(candidate)
    return refs


def build_reference_graph(root: Path) -> dict[str, set[str]]:
    files = discover_files(root)
    known = {_relative(root, p) for p in files}
    graph = {_relative(root, p): set() for p in files}

    for path in files:
        source = _relative(root, path)
        if path.suffix not in {".md", ".py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for ref in local_reference_candidates(text):
            normalized = (path.parent / ref).resolve()
            try:
                rel = normalized.relative_to(root.resolve()).as_posix()
            except ValueError:
                continue
            if rel in known and rel != source:
                graph[source].add(rel)
    return graph


def _has_local_test(path: Path, root: Path, test_files: set[str], graph: dict[str, set[str]]) -> bool:
    """Return whether a source file has a sibling test or a test referencing it."""
    sibling_names = {
        f"test_{path.stem}.py",
        f"{path.stem}_test.py",
    }
    if any(path.parent.joinpath(name).is_file() for name in sibling_names):
        return True
    source = _relative(root, path)
    return any(source in graph.get(test, set()) for test in test_files)


def audit(root: Path) -> dict:
    root = root.resolve()
    files = discover_files(root)
    graph = build_reference_graph(root)
    relative_files = {_relative(root, p): p for p in files}
    incoming = {name: 0 for name in relative_files}
    for targets in graph.values():
        for target in targets:
            incoming[target] += 1

    test_files = {
        _relative(root, p) for p in files
        if p.name.startswith("test_") or p.name.endswith("_test.py")
    }
    source_files = [p for p in files if p.suffix == ".py" and _relative(root, p) not in test_files]

    orphan_candidates = [
        _relative(root, p) for p in source_files
        if incoming[_relative(root, p)] == 0 and p.parent.name not in {"Scripts", "Tools"}
    ]
    runtime_sources = [
        p for p in source_files
        if p.is_relative_to(root / "Runtime")
    ]
    untested_candidates = [
        _relative(root, p) for p in runtime_sources
        if not _has_local_test(p, root, test_files, graph)
    ]

    return {
        "status": "AUDIT_COMPLETE",
        "file_count": len(files),
        "reference_edge_count": sum(len(v) for v in graph.values()),
        "orphan_candidates": sorted(orphan_candidates),
        "untested_candidates": sorted(set(untested_candidates)),
        "note": "Candidates require architectural review; zero incoming references or missing local tests alone do not prove a file is invalid.",
    }


if __name__ == "__main__":
    import json
    import sys

    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(json.dumps(audit(root), indent=2, ensure_ascii=False))
