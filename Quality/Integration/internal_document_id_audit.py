"""Current-tree internal Document ID audit.

The audit is intentionally conservative:
- active canonical identity is keyed by explicit internal Document ID;
- Archive paths are reported separately and do not collide with active IDs;
- filename prefix alignment is checked only when the filename itself carries a
  namespace-style identifier (e.g. REP-011, ENG-006, SRV-009);
- reference-only occurrences inside other documents are not treated as IDs.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

ID_RE = re.compile(r"\b([A-Z]{2,8}-\d{3})\b")
INLINE_RE = re.compile(r"^\s*Document ID\s*[:：]\s*`?([A-Z]{2,8}-\d{3})`?\s*$", re.I | re.M)
BLOCK_RE = re.compile(
    r"^\s*Document ID\s*$\n\s*`?([A-Z]{2,8}-\d{3})`?\s*$",
    re.I | re.M,
)
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml", ".py"}
NAMESPACE_PREFIXES = {"AI", "ARC", "AS", "ENG", "GOV", "INTF", "KNW", "LIF", "MOD", "PLG", "REP", "RUN", "SPEC", "SRV"}


@dataclass(frozen=True)
class ArtifactRecord:
    path: str
    document_id: str
    archived: bool
    filename_prefix: str | None


def _git_files(root: Path) -> list[Path]:
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    return [root / raw.decode("utf-8") for raw in output.split(b"\0") if raw]


def _extract_document_id(text: str) -> str | None:
    match = INLINE_RE.search(text) or BLOCK_RE.search(text)
    return match.group(1).upper() if match else None


def _filename_prefix(path: Path) -> str | None:
    stem = path.name.upper()
    match = ID_RE.search(stem)
    if not match:
        return None
    candidate = match.group(1)
    prefix = candidate.split("-", 1)[0]
    return candidate if prefix in NAMESPACE_PREFIXES else None


def scan(root: Path) -> dict:
    root = Path(root)
    records: list[ArtifactRecord] = []
    unreadable: list[str] = []

    for path in _git_files(root):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            unreadable.append(path.relative_to(root).as_posix())
            continue
        document_id = _extract_document_id(text)
        if not document_id:
            continue
        relative = path.relative_to(root).as_posix()
        archived = relative == "Archive" or relative.startswith("Archive/")
        records.append(
            ArtifactRecord(
                path=relative,
                document_id=document_id,
                archived=archived,
                filename_prefix=_filename_prefix(path),
            )
        )

    active = [record for record in records if not record.archived]
    archived = [record for record in records if record.archived]

    by_id: dict[str, list[str]] = {}
    for record in active:
        by_id.setdefault(record.document_id, []).append(record.path)
    duplicate_active_ids = {
        document_id: sorted(paths)
        for document_id, paths in by_id.items()
        if len(paths) > 1
    }

    filename_mismatches = sorted(
        {
            f"{record.path} => filename {record.filename_prefix} / internal {record.document_id}"
            for record in active
            if record.filename_prefix and record.filename_prefix != record.document_id
        }
    )

    return {
        "tracked_files_scanned": len(_git_files(root)),
        "document_id_records": len(records),
        "active_records": len(active),
        "archived_records": len(archived),
        "duplicate_active_ids": duplicate_active_ids,
        "filename_internal_id_mismatches": filename_mismatches,
        "unreadable": sorted(unreadable),
        "active_duplicate_pass": not duplicate_active_ids and not unreadable,
        "filename_alignment_pass": not filename_mismatches,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(scan(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))
