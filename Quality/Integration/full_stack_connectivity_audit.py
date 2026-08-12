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
    known = {p.as_posix() for p in files}
    graph = {p.as_posix(): set() for p in files}

    for path in files:
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
            if rel in known and rel != path.as_posix():
                graph[path.as_posix()].add(rel)
    return graph


def audit(root: Path) -> dict:
    files = discover_files(root)
    graph = build_reference_graph(root)
    incoming = {p.as_posix(): 0 for p in files}
    for targets in graph.values():
        for target in targets:
            incoming[target] += 1

    docs = {".md"}
    test_files = {p.as_posix() for p in files if p.name.startswith("test_") or p.name.endswith("_test.py")}
    source_files = [p for p in files if p.suffix == ".py" and p.as_posix() not in test_files]

    orphan_candidates = [
        p.as_posix() for p in source_files
        if incoming[p.as_posix()] == 0 and p.parent.name not in {"Scripts", "Tools"}
    ]
    untested_candidates = [
        p.as_posix() for p in source_files
        if p.parent.as_posix().startswith((root / "Runtime").as_posix())
        and not any(p.parent.joinpath(t).exists() for t in test_files if Path(t).parent == p.parent)
    ]

    return {
        "status": "AUDIT_COMPLETE",
        "file_count": len(files),
        "reference_edge_count": sum(len(v) for v in graph.values()),
        "orphan_candidates": sorted(orphan_candidates),
        "untested_candidates": sorted(set(untested_candidates)),
        "note": "Candidates require architectural review; zero incoming references alone does not prove a file is invalid.",
    }


if __name__ == "__main__":
    import json
    import sys

    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(json.dumps(audit(root), indent=2, ensure_ascii=False))
