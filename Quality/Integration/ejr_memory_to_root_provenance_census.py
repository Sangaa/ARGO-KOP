"""Evidence-only provenance census for the MEMORY_TO_ROOT_EJR H1 ambiguity cohort.

Target membership is derived from the current namespace-lineage classifier. This
module measures current content/reference/consumer evidence only and emits no
owner, canonical, migration, rename, delete, reassignment, suppression,
allocation, or authority decision.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path
from typing import Any

from internal_document_id_audit import TEXT_SUFFIXES, scan
from ejr_h1_namespace_lineage import current_repository_namespace_lineage

TARGET_CLASS = "MEMORY_TO_ROOT_EJR"
EXPECTED_GROUP_COUNT = 21
SELF_GENERATED_PATHS = {
    "Quality/Integration/ejr_memory_to_root_provenance_census.py",
    "Quality/Integration/test_ejr_memory_to_root_provenance_census.py",
    "Repository/MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202.md",
    "Repository/MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202_MUTATION_MATRIX.md",
    "Repository/ROOM071_RECONSTRUCTION_SUPPLEMENT_202_2026-08-30.md",
}


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "git command failed")
    return completed.stdout.strip()


def history_complete(root: Path) -> bool:
    return _git(root, "rev-parse", "--is-shallow-repository").lower() == "false"


def _tracked_text_paths(root: Path) -> list[Path]:
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    result: list[Path] = []
    for raw in output.split(b"\0"):
        if not raw:
            continue
        relative = Path(raw.decode("utf-8"))
        if relative.suffix.lower() in TEXT_SUFFIXES:
            result.append(relative)
    return sorted(result, key=lambda p: p.as_posix())


def _read(root: Path, relative: str | Path) -> str:
    return (root / relative).read_text(encoding="utf-8", errors="ignore")


def _first_h1(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _surface(path: str) -> str:
    if path.startswith("EJR/"):
        return "ROOT_EJR"
    if path.startswith("Memory/Engineering_Journal/"):
        return "MEMORY_EJR"
    return "OTHER"


def _reference_paths(root: Path, tracked: list[Path], group_paths: set[str], document_id: str) -> tuple[list[str], dict[str, list[str]]]:
    id_pattern = re.compile(rf"(?<![A-Z0-9]){re.escape(document_id)}(?![0-9A-Z])", re.I)
    external_id_refs: list[str] = []
    exact_member_refs: dict[str, list[str]] = {path: [] for path in sorted(group_paths)}
    for relative in tracked:
        relative_str = relative.as_posix()
        if relative_str in group_paths or relative_str in SELF_GENERATED_PATHS:
            continue
        try:
            text = _read(root, relative)
        except OSError:
            continue
        if id_pattern.search(text):
            external_id_refs.append(relative_str)
        for member_path in exact_member_refs:
            if member_path in text:
                exact_member_refs[member_path].append(relative_str)
    return sorted(set(external_id_refs)), {path: sorted(set(refs)) for path, refs in exact_member_refs.items()}


def classify_from_reports(root: Path, audit_report: dict[str, Any], lineage_report: dict[str, Any], *, expected_group_count: int = EXPECTED_GROUP_COUNT) -> dict[str, Any]:
    root = Path(root)
    if not history_complete(root) or not lineage_report.get("history_complete", False):
        return {"history_complete": False, "classification_complete": False, "decision": "HISTORY_INCOMPLETE", "target_class": TARGET_CLASS, "groups": {}}

    target_ids = sorted(
        document_id for document_id, group in lineage_report.get("groups", {}).items()
        if group.get("classification") == TARGET_CLASS
    )
    ambiguous = audit_report.get("ambiguous_duplicate_records", {})
    tracked = _tracked_text_paths(root)
    groups: dict[str, Any] = {}
    incomplete: list[str] = []

    if len(target_ids) != expected_group_count:
        incomplete.append("__COHORT_COUNT_DRIFT__")

    for document_id in target_ids:
        lineage_group = lineage_report["groups"][document_id]
        members = ambiguous.get(document_id) or []
        expected_cardinality = int(lineage_group.get("cardinality", 0))
        member_paths = sorted(str(member.get("path")) for member in members)
        sources = sorted({str(member.get("identity_source")) for member in members})
        if len(member_paths) != expected_cardinality or sources != ["FIRST_H1_FALLBACK"]:
            incomplete.append(document_id)
            groups[document_id] = {
                "membership_state": "UNEXPECTED_CURRENT_MEMBERSHIP",
                "expected_member_count": expected_cardinality,
                "member_count": len(member_paths),
                "identity_sources": sources,
                "member_paths": member_paths,
            }
            continue

        observations: list[dict[str, Any]] = []
        missing_paths: list[str] = []
        for path in member_paths:
            if not (root / path).is_file():
                missing_paths.append(path)
                continue
            text = _read(root, path)
            observations.append({
                "path": path,
                "surface": _surface(path),
                "first_h1": _first_h1(text),
                "content_sha256": _digest(text),
                "content_bytes_utf8": len(text.encode("utf-8")),
            })
        if missing_paths:
            incomplete.append(document_id)
            groups[document_id] = {"membership_state": "MISSING_CURRENT_PATH", "missing_paths": missing_paths, "members": observations}
            continue

        external_id_refs, exact_member_refs = _reference_paths(root, tracked, set(member_paths), document_id)
        digests = [item["content_sha256"] for item in observations]
        groups[document_id] = {
            "membership_state": "EXPECTED_H1_MEMBERSHIP",
            "member_count": len(member_paths),
            "namespace_sequence": lineage_group.get("namespace_sequence", []),
            "collapsed_namespace_sequence": lineage_group.get("collapsed_namespace_sequence", []),
            "content_all_distinct": len(set(digests)) == len(digests),
            "external_exact_id_reference_count": len(external_id_refs),
            "external_exact_id_reference_paths": external_id_refs,
            "external_exact_member_path_references": exact_member_refs,
            "members": observations,
        }

    return {
        "history_complete": True,
        "history_scope": "all locally reachable refs",
        "evidence_boundary": "current lineage-selected membership/content/title/exact references only; no ownership or identity mutation decision",
        "target_class": TARGET_CLASS,
        "expected_group_count": expected_group_count,
        "observed_group_count": len(target_ids),
        "target_ids": target_ids,
        "classification_complete": not incomplete,
        "decision": "CENSUSED" if not incomplete else "PARTIAL",
        "incomplete_group_ids": incomplete,
        "groups": groups,
    }


def current_repository_census(root: Path) -> dict[str, Any]:
    root = Path(root)
    return classify_from_reports(root, scan(root), current_repository_namespace_lineage(root))


if __name__ == "__main__":
    import json, sys
    result = current_repository_census(Path(__file__).resolve().parents[2])
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["history_complete"]:
        sys.exit(4)
    if not result["classification_complete"]:
        sys.exit(3)
