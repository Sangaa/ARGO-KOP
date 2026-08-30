"""Current-tree internal Document ID and document-level identity audit.

GOV-004/GOV-006 define the current metadata/naming constraints, while REP-001
defines the currently indexed active inventory scope. Identity discovery is
repository-observed rather than namespace-allowlisted: qualified metadata
``Document ID`` is primary, and a structural first-H1 identity is a fallback for
older artifacts that do not carry document metadata.

A ``Document ID`` mentioned inside the body of a journal, evidence record, or
other document is not the identity of the referencing document. Likewise, when
qualified metadata exists, a human/series/relationship H1 is not a second
identity authority. The audit therefore detects conflicting metadata IDs within
the document preamble instead of requiring metadata/H1 equality.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

DOCUMENT_ID_INLINE_RE = re.compile(r"^\s*Document ID\s*[:：]\s*(.+?)\s*$", re.I | re.M)
DOCUMENT_ID_BLOCK_RE = re.compile(r"^\s*Document ID\s*$\n\s*(.+?)\s*$", re.I | re.M)
# H1 fallback is generic by grammar, not unconstrained by surface text. A human
# title such as ``# ARGO KOP`` must not become identity ``ARGO`` merely because
# its first token is uppercase. Governed fallback identities use the repository's
# structural namespace + numeric sequence shape (for example REL-001/GOV-013A).
DOCUMENT_HEADING_ID_RE = re.compile(
    r"^\s*#\s+([A-Z][A-Z0-9_]{1,31}-\d{3}[A-Z]?)(?=\s|—|–|$)", re.I
)
NUMERIC_FILENAME_ID_RE = re.compile(
    r"^([A-Z][A-Z0-9]{1,31}-\d{3}[A-Z]?)(?:_|\.|$)", re.I
)
CANONICAL_INLINE_RE = re.compile(r"^\s*Canonical\s*[:：]\s*(Yes|No|Pending)\s*$", re.I | re.M)
CANONICAL_BLOCK_RE = re.compile(r"^\s*Canonical\s*$\n\s*(Yes|No|Pending)\s*$", re.I | re.M)
STATUS_RE = re.compile(r"^\s*Status\s*[:：]?\s*(.+?)\s*$", re.I | re.M)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml", ".py"}
LEGACY_TOKENS = ("legacy", "historical", "superseded", "archived", "noncanonical", "non-canonical")
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
    identity_source: str
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


def _clean_document_id(raw: str) -> str | None:
    value = raw.strip().strip("`").strip().strip("*").strip()
    if not value:
        return None
    return value.upper()


def _metadata_preamble(text: str) -> str:
    """Return the document-title/metadata band before substantive sections.

    ARGO documents use several historical layouts: some have one H1 title, some
    have an ID H1 followed by an uppercase title H1, and newer records often
    start substantive content at H2. The first heading is always treated as the
    document title. Additional H1 headings remain in the preamble only when they
    are a structural ID heading or an all-uppercase title. The first H2+ or first
    later human section H1 ends the metadata band.

    This prevents a body sentence such as ``Document ID: P6-SCOPE-001`` in an
    EJR describing another artifact from becoming the EJR's own identity.
    """
    lines = text.splitlines()
    seen_heading = False
    cutoff = len(lines)

    for index, line in enumerate(lines):
        stripped = line.strip()
        match = HEADING_RE.match(stripped)
        if not match:
            continue

        level = len(match.group(1))
        heading_text = match.group(2).strip()

        if not seen_heading:
            seen_heading = True
            continue

        if level > 1:
            cutoff = index
            break

        if DOCUMENT_HEADING_ID_RE.match(stripped):
            continue

        letters = "".join(char for char in heading_text if char.isalpha())
        if letters and letters == letters.upper():
            continue

        cutoff = index
        break

    return "\n".join(lines[:cutoff])


def _extract_metadata_document_ids(text: str) -> list[str]:
    """Return distinct qualified Document IDs from the document preamble."""
    preamble = _metadata_preamble(text)
    values: list[str] = []

    for regex in (DOCUMENT_ID_INLINE_RE, DOCUMENT_ID_BLOCK_RE):
        for match in regex.finditer(preamble):
            value = _clean_document_id(match.group(1))
            if value and value not in values:
                values.append(value)

    return values


def _extract_document_id(text: str) -> str | None:
    values = _extract_metadata_document_ids(text)
    return values[0] if values else None


def _extract_heading_id(text: str) -> str | None:
    """Return only a document-level first-H1 fallback identity token.

    A later section such as ``# GOV-011 Determination`` is not a second document,
    and a Python comment is not a Markdown document heading. Only the first H1 is
    inspected; if that H1 is a normal title rather than an identity, there is no
    heading fallback identity.
    """
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("# "):
            continue
        match = DOCUMENT_HEADING_ID_RE.match(stripped)
        return match.group(1).upper() if match else None
    return None


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
    match = NUMERIC_FILENAME_ID_RE.match(path.stem.upper())
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
    heading_identities: dict[str, list[str]] = {}
    metadata_document_id_conflicts: list[str] = []

    for path in tracked:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root).as_posix()
        archived_path = relative == "Archive" or relative.startswith("Archive/")
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            unreadable.append(relative)
            continue

        heading_id = None
        if path.suffix.lower() in {".md", ".markdown", ".rst", ".txt"}:
            heading_id = _extract_heading_id(text)
        if heading_id and not archived_path:
            heading_identities.setdefault(heading_id, []).append(relative)

        explicit_document_ids = _extract_metadata_document_ids(text)
        if len(explicit_document_ids) > 1:
            metadata_document_id_conflicts.append(
                f"{relative} => metadata IDs {', '.join(explicit_document_ids)}"
            )
        explicit_document_id = explicit_document_ids[0] if explicit_document_ids else None

        # Qualified metadata is authoritative for identity discovery. H1 is only
        # the fallback for older artifacts without qualified metadata.
        document_id = explicit_document_id or heading_id
        if not document_id:
            continue

        relative_path = Path(relative)
        records.append(
            ArtifactRecord(
                path=relative,
                document_id=document_id,
                identity_source="DOCUMENT_ID_FIELD" if explicit_document_id else "FIRST_H1_FALLBACK",
                canonical=_extract_canonical(text),
                archived=archived_path,
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
    ambiguous_duplicate_records: dict[str, list[dict[str, object]]] = {}
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
        ambiguous_duplicate_records[document_id] = [
            {
                "path": record.path,
                "identity_source": record.identity_source,
                "canonical": record.canonical,
                "indexed_active": record.indexed_active,
                "status": record.status,
                "deferred_domain": record.deferred_domain,
                "filename_prefix": record.filename_prefix,
            }
            for record in sorted(group, key=lambda item: item.path)
        ]

    heading_identity_collisions = {
        identity: sorted(paths)
        for identity, paths in sorted(heading_identities.items())
        if len(paths) > 1
    }

    # GOV-006 assigns GOV namespace ownership to Governance/. A template,
    # tool note, mutation matrix or historical evidence elsewhere may mention
    # the same GOV heading, but it is not a second Governance document owner.
    governance_heading_identity_collisions: dict[str, list[str]] = {}
    for identity, paths in heading_identities.items():
        governance_paths = sorted(path for path in paths if path.startswith("Governance/"))
        if identity.startswith("GOV-") and len(governance_paths) > 1:
            governance_heading_identity_collisions[identity] = governance_paths

    document_ids_by_path = {
        record.path: record.document_id
        for record in sorted(records, key=lambda item: item.path)
    }
    identity_sources_by_path = {
        record.path: record.identity_source
        for record in sorted(records, key=lambda item: item.path)
    }

    return {
        "tracked_files_scanned": len(tracked),
        "master_index_paths": len(active_index),
        "document_id_records": len(records),
        "document_ids_by_path": document_ids_by_path,
        "identity_sources_by_path": identity_sources_by_path,
        "metadata_document_id_conflicts": sorted(metadata_document_id_conflicts),
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
        "ambiguous_duplicate_records": {
            key: value for key, value in sorted(ambiguous_duplicate_records.items())
        },
        "heading_identity_collisions": heading_identity_collisions,
        "governance_heading_identity_collisions": governance_heading_identity_collisions,
        "filename_internal_id_mismatches": filename_mismatches,
        "unindexed_id_records_by_id": unindexed_ids,
        "unreadable": sorted(unreadable),
        "active_duplicate_pass": not duplicate_active_ids and not unreadable,
        "filename_alignment_pass": not filename_mismatches,
        "identity_scope_reconciled": (
            not canonical_unindexed
            and not ambiguous_duplicate_ids
            and not governance_heading_identity_collisions
            and not metadata_document_id_conflicts
        ),
        "governance_identity_hold_required": bool(governance_heading_identity_collisions),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(scan(Path(__file__).resolve().parents[2]), indent=2, sort_keys=True))
