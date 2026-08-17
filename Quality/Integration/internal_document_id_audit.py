"""Current-tree internal Document ID audit.

The audit follows GOV-004 metadata semantics:
- only active canonical artifacts participate in active-ID uniqueness;
- legacy/archive/non-canonical artifacts are reported separately;
- filename/internal-ID alignment is checked only when the filename carries
  an exact namespace-style identifier;
- textual references are not interpreted as document identity.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

NAMESPACE_PREFIXES = {
    "AI", "ARC", "AS", "CORE", "ENG", "EJR", "GOV", "INT", "INTF",
    "KNW", "LIF", "MEM", "MOD", "PLG", "REP", "RUN", "SPEC", "SRV",
}
NAMESPACE_PATTERN = "|".join(sorted(NAMESPACE_PREFIXES, key=len, reverse=True))
ID_PATTERN = rf"(?:{NAMESPACE_PATTERN})-\d{{3}}"
ID_RE = re.compile(rf"(?<![A-Z])({ID_PATTERN})(?![A-Z0-9-])", re.I)
INLINE_RE = re.compile(rf"^\s*Document ID\s*[:：]\s*`?({ID_PATTERN})`?\s*$", re.I | re.M)
BLOCK_RE = re.compile(rf"^\s*Document ID\s*$\n\s*`?({ID_PATTERN})`?\s*$", re.I | re.M)
CANONICAL_RE = re.compile(r"^\s*Canonical\s*[:：]\s*(Yes|No)\s*$", re.I | re.M)
STATUS_RE = re.compile(r"^\s*Status\s*[:：]?\s*(.+?)\s*$", re.I | re.M)
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml", ".py"}


@dataclass(frozen=True)
class ArtifactRecord:
    path: str
    document_id: str
    canonical: bool | None
    archived: bool
    filename_prefix: str | None
    status: str | None

    @property
    def active_canonical(self) -> bool:
        if self.archived:
            return False
        if self.canonical is False:
            return False
        status = (self.status or "").lower()
        return not any(token in status for token in ("legacy", "historical", "superseded", "archived"))


def _git_files(root: Path) -> list[Path]:
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    return [root / raw.decode("utf-8") for raw in output.split(b"\0") if raw]


def _extract_document_id(text: str) -> str | None:
    match = INLINE_RE.search(text) or BLOCK_RE.search(text)
    return match.group(1).upper() if match else None


def _extract_canonical(text: str) -> bool | None:
    match = CANONICAL_RE.search(text)
    if not match:
        return None
    return match.group(1).lower() == "yes"


def _extract_status(text: str) -> str | None:
    match = STATUS_RE.search(text)
    return match.group(1).strip() if match else None


def _filename_prefix(path: Path) -> str | None:
    stem = path.stem.upper()
    match = re.match(rf"^({ID_PATTERN})(?:_|\.|$)", stem, re.I)
    return match.group(1).upper() if match else None


def scan(root: Path) -> dict:
    root = Path(root)
    records: list[ArtifactRecord] = []
    unreadable: list[str] = []
    tracked = _git_files(root)

    for path in tracked:
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
                canonical=_extract_canonical(text),
                archived=archived,
                filename_prefix=_filename_prefix(path),
                status=_extract_status(text),
            )
        )

    active = [record for record in records if record.active_canonical]
    noncanonical = [record for record in records if not record.active_canonical]

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

    historical_reuse: dict[str, list[str]] = {}
    for record in noncanonical:
        historical_reuse.setdefault(record.document_id, []).append(record.path)
    historical_reuse = {
        document_id: sorted(paths)
        for document_id, paths in historical_reuse.items()
        if len(paths) > 1 or any(path.startswith("Memory/Engineering_Journal/") for path in paths)
    }

    return {
        "tracked_files_scanned": len(tracked),
        "document_id_records": len(records),
        "active_canonical_records": len(active),
        "noncanonical_records": len(noncanonical),
        "duplicate_active_ids": duplicate_active_ids,
        "filename_internal_id_mismatches": filename_mismatches,
        "historical_or_noncanonical_reuse": historical_reuse,
        "unreadable": sorted(unreadable),
        "active_duplicate_pass": not duplicate_active_ids and not unreadable,
        "filename_alignment_pass": not filename_mismatches,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(scan(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))
