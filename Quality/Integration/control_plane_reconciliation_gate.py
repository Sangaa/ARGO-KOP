"""Executable gate for the current Phase-1 control-plane evidence boundary.

The gate reads the current session boundary manifest rather than hard-coding
historical artifact versions. It verifies identity/status drift while leaving
semantic closure decisions to the authoritative control-plane records.
"""

from pathlib import Path

MANIFEST = "Repository/REP-020_SESSION_DELTA_2026-08-17_P339.md"


def _field(text: str, name: str) -> str | None:
    for raw in text.splitlines():
        line = raw.strip().replace("**", "")
        prefix = f"{name}:"
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip("`")
    return None


def _manifest_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("| REP-"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 5:
            continue
        rows.append(
            {
                "document_id": parts[0],
                "path": parts[1],
                "version": parts[2],
                "status": parts[3],
                "boundary": parts[4],
            }
        )
    return rows


def evaluate(root: Path) -> dict:
    root = Path(root)
    missing: list[str] = []
    mismatches: list[str] = []
    manifest_path = root / MANIFEST

    if not manifest_path.is_file():
        return {
            "expected_artifacts": 0,
            "missing": [MANIFEST],
            "mismatches": [],
            "boundary_pass": False,
        }

    manifest_text = manifest_path.read_text(encoding="utf-8", errors="ignore")
    rows = _manifest_rows(manifest_text)

    if len(rows) < 7:
        mismatches.append(f"P339 manifest rows={len(rows)!r}; expected at least 7")

    if "Priority 1 is still OPEN" not in manifest_text:
        mismatches.append("P339 does not explicitly preserve the current Priority-1 OPEN boundary")

    for expected in rows:
        path = root / expected["path"]
        if not path.is_file():
            missing.append(expected["path"])
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        document_id = _field(text, "Document ID")
        version = _field(text, "Version")
        status = _field(text, "Status") or ""

        if document_id != expected["document_id"]:
            mismatches.append(f"{expected['path']}: Document ID={document_id!r}")
        if version != expected["version"]:
            mismatches.append(
                f"{expected['path']}: Version={version!r}; manifest={expected['version']!r}"
            )
        if expected["status"] not in status:
            mismatches.append(
                f"{expected['path']}: Status={status!r}; manifest requires={expected['status']!r}"
            )

    queue_text = (root / "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md").read_text(
        encoding="utf-8", errors="ignore"
    ) if (root / "Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md").is_file() else ""
    if "Priority 1" not in queue_text or "Phase 1 Open" not in queue_text:
        mismatches.append("REP-016 does not visibly preserve the open Phase-1 boundary")

    return {
        "expected_artifacts": len(rows),
        "missing": sorted(missing),
        "mismatches": sorted(mismatches),
        "boundary_pass": not missing and not mismatches,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(evaluate(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))
