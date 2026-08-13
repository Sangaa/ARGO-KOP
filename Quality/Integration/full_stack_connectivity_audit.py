"""Repository-wide connectivity audit for ARGO-KOP.

The audit separates structural discovery from architectural proof. It can
identify candidates and evidence classes, but it never upgrades presence to
runtime connectivity on its own.
"""

from __future__ import annotations

import re
from pathlib import Path

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}
REFERENCE_RE = re.compile(r"(?:\]\(|from\s+|import\s+)([^\s)]+)")
EVIDENCE_CLASSES = (
    "IMPLEMENTED", "TESTED", "LINKED", "RUNTIME_REACHABLE",
    "DOCUMENTED", "ORPHAN_CANDIDATE", "UNTESTED_CANDIDATE", "BROKEN_REFERENCE",
)
LAYER_PATHS = (
    "Repository / Governance", "Architecture", "Knowledge", "Memory / Context",
    "Cognition / Reasoning", "Decision", "Authorization", "Runtime / Execution",
    "Trace / Outcome", "Feedback", "Learning", "Memory Observation",
)


def discover_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file() and not any(part in IGNORED_DIRS for part in p.parts))


def _relative(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def normalize_local_reference(raw: str, source: Path, root: Path) -> str | None:
    """Normalize a local markdown/Python reference without inventing targets."""
    candidate = raw.strip().strip("`'\"")
    candidate = candidate.split("#", 1)[0].split("?", 1)[0]
    if not candidate or candidate.startswith(("http://", "https://", "mailto:")):
        return None
    candidate = candidate.replace("\\", "/")
    target = (source.parent / candidate).resolve()
    try:
        return target.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def local_reference_candidates(text: str) -> set[str]:
    refs: set[str] = set()
    for match in REFERENCE_RE.findall(text):
        candidate = match.strip("`'\"")
        if not candidate.startswith(("http://", "https://")):
            refs.add(candidate)
    return refs


def build_reference_graph(root: Path) -> tuple[dict[str, set[str]], list[dict[str, str]]]:
    files = discover_files(root)
    known = {_relative(root, p) for p in files}
    graph = {_relative(root, p): set() for p in files}
    broken: list[dict[str, str]] = []
    for path in files:
        source = _relative(root, path)
        if path.suffix not in {".md", ".py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for ref in local_reference_candidates(text):
            rel = normalize_local_reference(ref, path, root)
            if rel is not None and rel in known and rel != source:
                graph[source].add(rel)
            elif ("/" in ref or ref.endswith((".py", ".md", ".json", ".yaml", ".yml"))) and not ref.startswith(("http://", "https://")):
                broken.append({"source": source, "reference": ref})
    return graph, broken


def _has_local_test(path: Path, root: Path, test_files: set[str], graph: dict[str, set[str]]) -> bool:
    sibling_names = {f"test_{path.stem}.py", f"{path.stem}_test.py"}
    if any(path.parent.joinpath(name).is_file() for name in sibling_names):
        return True
    source = _relative(root, path)
    return any(source in graph.get(test, set()) for test in test_files)


def _layer_for_path(relative: str) -> str:
    parts = Path(relative).parts
    joined = "/".join(parts).lower()
    if parts and parts[0] == "Runtime": return "Runtime / Execution"
    if parts and parts[0] == "Architecture": return "Architecture"
    if parts and parts[0] == "Governance": return "Repository / Governance"
    if "knowledge" in joined: return "Knowledge"
    if any(token in joined for token in ("cognition", "reasoning")): return "Cognition / Reasoning"
    if "memory" in joined or "context" in joined: return "Memory / Context"
    if "decision" in joined: return "Decision"
    if "author" in joined: return "Authorization"
    if any(token in joined for token in ("trace", "outcome")): return "Trace / Outcome"
    if "feedback" in joined: return "Feedback"
    if "learning" in joined: return "Learning"
    return "Repository / Governance"


def audit(root: Path) -> dict:
    root = root.resolve()
    files = discover_files(root)
    graph, broken = build_reference_graph(root)
    relative_files = {_relative(root, p): p for p in files}
    incoming = {name: 0 for name in relative_files}
    for targets in graph.values():
        for target in targets:
            incoming[target] += 1

    test_files = {_relative(root, p) for p in files if p.name.startswith("test_") or p.name.endswith("_test.py")}
    source_files = [p for p in files if p.suffix == ".py" and _relative(root, p) not in test_files]
    orphan_candidates = [_relative(root, p) for p in source_files if incoming[_relative(root, p)] == 0 and p.parent.name not in {"Scripts", "Tools"}]
    runtime_sources = [p for p in source_files if p.is_relative_to(root / "Runtime")]
    untested_candidates = [_relative(root, p) for p in runtime_sources if not _has_local_test(p, root, test_files, graph)]
    layer_counts = {layer: 0 for layer in LAYER_PATHS}
    for relative in relative_files:
        layer_counts[_layer_for_path(relative)] += 1

    return {
        "status": "AUDIT_COMPLETE",
        "file_count": len(files),
        "reference_edge_count": sum(len(v) for v in graph.values()),
        "broken_reference_candidates": sorted(broken, key=lambda item: (item["source"], item["reference"])),
        "orphan_candidates": sorted(orphan_candidates),
        "untested_candidates": sorted(set(untested_candidates)),
        "layer_file_counts": layer_counts,
        "evidence_classes": list(EVIDENCE_CLASSES),
        "note": "Candidates require architectural review; zero incoming references or missing local tests alone do not prove a file is invalid.",
    }


if __name__ == "__main__":
    import json
    import sys
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(json.dumps(audit(root), indent=2, ensure_ascii=False))
