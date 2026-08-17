"""Executable gate for the current Phase-1 control-plane evidence boundary.

This gate does not decide semantic closure. It verifies that the current
canonical control-plane artifacts still expose the evidence boundary recorded
by the latest session checkpoint and therefore prevents silent state drift.
"""

from pathlib import Path

EXPECTED = {
    "Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md": {
        "Document ID": "REP-011",
        "Version": "1.1.2",
        "status_contains": "Active / Integrity Hold",
    },
    "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md": {
        "Document ID": "REP-012",
        "Version": "1.0.9",
        "status_contains": "Active Control / Integrity Hold",
    },
    "Repository/REP-013_REPOSITORY_CONTENT_TREE.md": {
        "Document ID": "REP-013",
        "Version": "1.1.2",
        "status_contains": "Phase 1 Population In Progress",
    },
    "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md": {
        "Document ID": "REP-014",
        "Version": "1.2.6",
        "status_contains": "Relationship Enumeration In Progress",
    },
    "Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md": {
        "Document ID": "REP-015",
        "Version": "1.0.7",
        "status_contains": "Phase 1 Open / Integrity Hold",
    },
    "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md": {
        "Document ID": "REP-016",
        "Version": "1.3.0",
        "status_contains": "Phase 1 Open / Integrity Hold",
    },
    "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md": {
        "Document ID": "REP-020",
        "Version": "0.2.0",
        "status_contains": "Provisional / Phase-1 Seed / Not Authority",
    },
}


def _field(text: str, name: str) -> str | None:
    for raw in text.splitlines():
        line = raw.strip().replace("**", "")
        prefix = f"{name}:"
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip("`")
    return None


def evaluate(root: Path) -> dict:
    root = Path(root)
    missing = []
    mismatches = []
    for relative, expected in EXPECTED.items():
        path = root / relative
        if not path.is_file():
            missing.append(relative)
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        document_id = _field(text, "Document ID")
        version = _field(text, "Version")
        status = _field(text, "Status") or ""
        if document_id != expected["Document ID"]:
            mismatches.append(f"{relative}: Document ID={document_id!r}")
        if version != expected["Version"]:
            mismatches.append(f"{relative}: Version={version!r}")
        if expected["status_contains"] not in status:
            mismatches.append(f"{relative}: Status={status!r}")

    queue_text = (root / "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md").read_text(
        encoding="utf-8", errors="ignore"
    ) if not (root / "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md").is_file() else (root / "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md").read_text(encoding="utf-8", errors="ignore")
    p335 = root / "Repository/REP-020_SESSION_DELTA_2026-08-17_P335.md"
    if not p335.is_file():
        missing.append(p335.relative_to(root).as_posix())
    else:
        p335_text = p335.read_text(encoding="utf-8", errors="ignore")
        for required in (
            "Priority 1 remains OPEN.",
            "Control Plane: PARTIALLY RECONCILED / INTEGRITY HOLD",
            "Global PASS: NOT CLAIMED",
        ):
            if required not in p335_text:
                mismatches.append(f"P335 missing: {required}")

    if "Priority 1" not in queue_text or "Phase 1 Open" not in queue_text:
        mismatches.append("REP-016 does not visibly preserve the open Phase-1 boundary")

    return {
        "expected_artifacts": len(EXPECTED),
        "missing": sorted(missing),
        "mismatches": sorted(mismatches),
        "boundary_pass": not missing and not mismatches,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(evaluate(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))
