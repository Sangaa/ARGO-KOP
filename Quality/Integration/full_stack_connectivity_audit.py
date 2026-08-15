"""Repository-wide connectivity audit for ARGO-KOP.

The audit separates structural discovery from architectural proof. It can
identify candidates and evidence classes, but it never upgrades presence to
runtime connectivity on its own.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`+[^`]*?`+")
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
    """Normalize a local file/directory reference without inventing targets."""
    candidate = raw.strip().strip("`'\"")
    candidate = candidate.split("#", 1)[0].split("?", 1)[0].strip().rstrip(".,;:)")
    if not candidate or candidate.startswith(("http://", "https://", "mailto:", "#")):
        return None
    candidate = candidate.replace("\\", "/")
    target = (source.parent / candidate).resolve()
    try:
        return target.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def markdown_reference_candidates(text: str) -> set[str]:
    """Extract Markdown links while ignoring inline/fenced code spans."""
    visible = INLINE_CODE_RE.sub("", text)
    return {
        match.strip().strip("`'\"")
        for match in MARKDOWN_LINK_RE.findall(visible)
        if match.strip()
    }


def python_import_candidates(text: str) -> set[str]:
    """Return only import statements, avoiding prose/string false positives."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    refs: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            refs.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                prefix = "." * node.level
                refs.add(prefix + (node.module or ""))
            elif node.module:
                refs.add(node.module)
    return refs


def local_reference_candidates(text: str, suffix: str = ".md") -> set[str]:
    """Compatibility helper returning syntax-aware local candidates."""
    if suffix == ".py":
        return python_import_candidates(text)
    return markdown_reference_candidates(text)


def _import_to_path(raw: str) -> str | None:
    if raw.startswith("."):
        return None
    return raw.replace(".", "/")


def build_reference_graph(root: Path) -> tuple[dict[str, set[str]], list[dict[str, str]]]:
    files = discover_files(root)
    known = {_relative(root, p) for p in files}
    known_dirs = {
        _relative(root, p) for p in root.rglob("*")
        if p.is_dir() and not any(part in IGNORED_DIRS for part in p.parts)
    }
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
        refs = local_reference_candidates(text, path.suffix)
        for ref in refs:
            if path.suffix == ".py":
                if ref.startswith("."):
                    candidate = (path.parent / (ref.lstrip(".").replace(".", "/"))).as_posix()
                else:
                    candidate = _import_to_path(ref)
                if candidate is None:
                    continue
                matches = {candidate, f"{candidate}.py", f"{candidate}/__init__.py"}
                target = next((item for item in matches if item in known), None)
                if target:
                    graph[source].add(target)
                elif any(part in candidate.split("/") for part in ("Runtime", "Cognition", "Decision", "Knowledge", "Memory", "Quality", "Architecture", "Engine", "Services", "Models", "Repository")):
                    broken.append({"source": source, "reference": ref})
                continue

            rel = normalize_local_reference(ref, path, root)
            if rel is not None and (rel in known or rel in known_dirs) and rel != source:
                graph[source].add(rel)
            elif ("/" in ref or ref.endswith((".py", ".md", ".json", ".yaml", ".yml"))) and not ref.startswith(("http://", "https://")):
                broken.append({"source": source, "reference": ref})
    return graph, broken


def _test_imports(path: Path) -> set[str]:
    """Extract imported module basenames from a test file for coverage matching."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, SyntaxError):
        return set()
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.rsplit(".", 1)[-1] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.rsplit(".", 1)[-1])
    return names


def _has_local_test(path: Path, root: Path, test_files: set[str], graph: dict[str, set[str]]) -> bool:
    sibling_names = {f"test_{path.stem}.py", f"{path.stem}_test.py"}
    if any(path.parent.joinpath(name).is_file() for name in sibling_names):
        return True
    source = _relative(root, path)
    if any(source in graph.get(test, set()) for test in test_files):
        return True
    return any(path.stem in _test_imports(root / test) for test in test_files)


def _workflow_invokes(path: Path, root: Path) -> bool:
    """Detect explicit GitHub Actions invocation of a runtime script."""
    workflows = root / ".github" / "workflows"
    if not workflows.is_dir():
        return False
    relative = _relative(root, path)
    basename = path.name
    for workflow in workflows.glob("*.y*ml"):
        try:
            text = workflow.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if relative in text or basename in text:
            return True
    return False


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
    orphan_candidates = [
        _relative(root, p)
        for p in source_files
        if incoming[_relative(root, p)] == 0
        and p.parent.name not in {"Scripts", "Tools"}
        and not _has_local_test(p, root, test_files, graph)
        and not _workflow_invokes(p, root)
    ]
    runtime_sources = [p for p in source_files if p.is_relative_to(root / "Runtime")]
    untested_candidates = [
        _relative(root, p)
        for p in runtime_sources
        if not _has_local_test(p, root, test_files, graph) and not _workflow_invokes(p, root)
    ]
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
        "note": "Candidates require architectural review; zero incoming references alone do not prove a file is orphaned. Test-import matching is evidence of test coverage, not runtime reachability. Workflow invocation is evidence of CI execution intent, not runtime architectural connectivity.",
    }


if __name__ == "__main__":
    import json
    import sys
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(json.dumps(audit(root), indent=2, ensure_ascii=False))
