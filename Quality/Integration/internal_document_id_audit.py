"""Current-tree internal Document ID audit.

GOV-004 defines identity rules, while REP-001 defines the currently verified
active inventory scope. This audit separates:
- indexed active canonical artifacts;
- canonical artifacts outside the current active inventory;
- canonical artifacts inside domains explicitly deferred by domain authority;
- legacy/non-canonical artifacts retained for provenance;
- shadowed legacy identities where one canonical owner coexists with
  explicit historical/non-canonical retained artifacts;
- ambiguous duplicate IDs that require an explicit identity decision.

It never promotes an unindexed artifact to active authority from its filename
or internal Document ID alone.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

NAMESPACE_PREFIXES = {
    "AI", "ARC", "AS", "CORE", "EJR", "ENG", "GOV", "INT", "INTF", "KNW",
    "LIF", "MEM", "MOD", "PLG", "REP", "RUN", "SPEC", "SRV",
}
NAMESPACE_PATTERN = "|".join(sorted(NAMESPACE_PREFIXES, key=len, reverse=True))
ID_PATTERN = rf"(?:{NAMESPACE_PATTERN})-\d{{3}}"
ID_RE = re.compile(rf"(?<![A-Z])({ID_PATTERN})(?![A-Z0-9-])", re.I)
INLINE_RE = re.compile(rf"^\s*Document ID\s*[:：]\s*`?({ID_PATTERN})`?\s*$", re.I | re.M)
BLOCK_RE = re.compile(rf"^\s*Document ID\s*$\n\s*`?({ID_PATTERN})`?\s*$", re.I | re.M)
CANONICAL_INLINE_RE = re.compile(r"^\s*Canonical\s*[:：]\s*(Yes|No|Pending)\s*$", re.I | re.M)
CANONICAL_BLOCK_RE = re.compile(r"^\s*Canonical\s*$\n\s*(Yes|No|Pending)\s*$", re.I | re.M)
STATUS_RE = re.compile(r"^\s*Status\s*[:：]?\s*(.+?)\s*$", re.I | re.M)
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml", ".py"}
LEGACY_TOKENS = ("legacy", "historical", "superseded", "archived", "noncanonical")
DEFERRED_DOMAIN_TOKENS = (
    "canonical pending",
    "pending consolidated validation",
    "under reconstruction",
    "staged reconstruction",
    "reconstruction pending",
)


@dataclass(frozen=True)
class ArtifactRecord:
    path: str
    document_id: str
    canonical: bool | None
    archived: bool
    indexed_active: bool
    filename_prefix: str | None
    status: str | None
    deferred_domain: bool

    @property
    def active_canonical(self) -> bool:
        if self.archived or not self.indexed_active:
            return False
        if self.canonical is False:
            return False
        status = (self.status or "").lower()
        return not any(token in status for token in LEGACY_TOKENS)

    @property
    def explicit_historical_or_noncanonical(self) -> bool:
        if self.archived:
            return True
        status = (self.status or "").lower()
        if self.canonical is False:
            return any(token in status for token in LEGACY_TOKENS)
        return any(token in status for token in LEGACY_TOKENS)

    @property
    def canonical_unindexed(self) -> bool:
        if self.archived or self.indexed_active or self.canonical is not True:
            return False
        if self.deferred_domain:
            return False
        status = (self.status or "").lower()
        return not any(token in status for token in LEGACY_TOKENS)


def _git_files(root: Path) -> list[Path]:
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    return [root / raw.decode("utf-8") for raw in output.split(b"\0") if raw]


def _master_index_paths(root: Path) -> set[str]:
    index_path = root / "Repository/REP-001_MASTER_INDEX.md"
    if not index_path.is_file():
        return set()
    text = index_path.read_text(encoding="utf-8", errors="ignore")
    paths = set()
    for match in re.finditer(r"`([A-Za-z0-9_./-]+\.md)`", text):
        paths.add(match.group(1))
    return paths


def _extract_document_id(text: str) -> str | None:
    match = INLINE_RE.search(text) or BLOCK_RE.search(text)
    return match.group(1).upper() if match else None


def _extract_canonical(text: str) -> bool | None:
    match = CANONICAL_INLINE_RE.search(text) or CANONICAL_BLOCK_RE.search(text)
    if not match:
        return None
    value = match.group(1).lower()
    return True if value == "yes" else False if value == "no" else None


def _extract_status(text: str) -> str | None:
    match = STATUS_RE.search(text)
    return match.group(1).strip() if match else None


def _filename_prefix(path: Path) -> str | None:
    stem = path.stem.upper()
    match = re.match(rf"^({ID_PATTERN})(?:_|\.|$)", stem, re.I)
    return match.group(1).upper() if match else None


def _deferred_domain(relative_path: Path, root: Path, folder_status_cache: dict[str, bool]) -> bool:
    parts = relative_path.parts
    if not parts:
        return False
    domain = parts[0]
    if domain in {"Archive", "Repository"}:
        return False
    if domain in folder_status_cache:
        return folder_status_cache[domain]
    status_path = root / domain / "_FOLDER_STATUS.md"
    if not status_path.is_file():
        folder_status_cache[domain] = False
        return False
    text = status_path.read_text(encoding="utf-8", errors="ignore").lower()
    deferred = any(token in text for token in DEFERRED_DOMAIN_TOKENS)
    folder_status_cache[domain] = deferred
    return deferred


def scan(root: Path) -> dict:
    root = Path(root)
    records: list[ArtifactRecord] = []
    unreadable: list[str] = []
    tracked = _git_files(root)
    active_index = _master_index_paths(root)
    folder_status_cache: dict[str, bool] = {}

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
        relative_path = Path(relative)
        archived = relative == "Archive" or relative.startswith("Archive/")
        records.append(
            ArtifactRecord(
                path=relative,
                document_id=document_id,
                canonical=_extract_canonical(text),
                archived=archived,
                indexed_active=relative in active_index,
                filename_prefix=_filename_prefix(relative_path),
                status=_extract_status(text),
                deferred_domain=_deferred_domain(relative_path, root, folder_status_cache),
            )
        )

    active = [record for record in records if record.active_canonical]
    unindexed = [record for record in records if not record.active_canonical and not record.archived]
    archived = [record for record in records if record.archived]
    canonical_unindexed = [record for record in records if record.canonical_unindexed]
    deferred_domain_records = [
        record for record in records
        if record.canonical is True and not record.indexed_active and not record.archived and record.deferred_domain
    ]

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

    unindexed_ids: dict[str, list[str]] = {}
    for record in unindexed:
        unindexed_ids.setdefault(record.document_id, []).append(record.path)
    unindexed_ids = {key: sorted(value) for key, value in unindexed_ids.items()}

    records_by_id: dict[str, list[ArtifactRecord]] = {}
    for record in records:
        if not record.archived:
            records_by_id.setdefault(record.document_id, []).append(record)

    ambiguous_duplicate_ids: dict[str, list[str]] = {}
    shadowed_legacy_ids: dict[str, list[str]] = {}
    for document_id, group in records_by_id.items():
        if len(group) < 2:
            continue
        canonical_group = [record for record in group if record.canonical is True]
        noncanonical_group = [record for record in group if record.canonical is not True]
        if len(canonical_group) == 1 and noncanonical_group and all(
            record.explicit_historical_or_noncanonical for record in noncanonical_group
        ):
            shadowed_legacy_ids[document_id] = sorted(record.path for record in noncanonical_group)
            continue
        if all(record.explicit_historical_or_noncanonical for record in group):
            continue
        ambiguous_duplicate_ids[document_id] = sorted(record.path for record in group)

    return {
        "tracked_files_scanned": len(tracked),
        "master_index_paths": len(active_index),
        "document_id_records": len(records),
        "active_indexed_canonical_records": len(active),
        "canonical_unindexed_records": len(canonical_unindexed),
        "canonical_unindexed_paths": sorted(record.path for record in canonical_unindexed),
        "deferred_domain_records": len(deferred_domain_records),
        "deferred_domain_paths": sorted(record.path for record in deferred_domain_records),
        "unindexed_id_records": len(unindexed),
        "archived_records": len(archived),
        "duplicate_active_ids": duplicate_active_ids,
        "shadowed_legacy_ids": {key: sorted(value) for key, value in sorted(shadowed_legacy_ids.items())},
        "ambiguous_duplicate_ids": {key: sorted(value) for key, value in sorted(ambiguous_duplicate_ids.items())},
        "filename_internal_id_mismatches": filename_mismatches,
        "unindexed_id_records_by_id": unindexed_ids,
        "unreadable": sorted(unreadable),
        "active_duplicate_pass": not duplicate_active_ids and not unreadable,
        "filename_alignment_pass": not filename_mismatches,
        "identity_scope_reconciled": not canonical_unindexed and not ambiguous_duplicate_ids,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(scan(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))