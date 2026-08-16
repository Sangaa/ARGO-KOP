from collections import defaultdict
from pathlib import Path
import re


DOCUMENT_ID_COLON_RE = re.compile(r"^Document ID:\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
DOCUMENT_ID_BLOCK_RE = re.compile(r"^Document ID\s*$\n\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
FILENAME_ID_RE = re.compile(r"(?:^|/)([A-Za-z]+-\d+)(?:_|\.|$)")
EXCLUDED_PREFIXES = (
    "Archive/",
    "Memory/Engineering_Journal/",
    "Quality/Integration/evidence/",
    "Quality/Integration/canonical_evidence/",
    "Quality/Integrity/",
)
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".yaml", ".yml", ".json"}


def _is_active_document(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return not rel.startswith(EXCLUDED_PREFIXES)


def _header(text: str) -> str:
    # Identity metadata belongs to the document preamble. This excludes
    # related-document lists, examples and explanatory body text.
    for marker in ("# Purpose", "Purpose\n", "# 1."):
        if marker in text:
            text = text.split(marker, 1)[0]
    return text[:12000]


def _extract_document_ids(root: Path):
    owners = defaultdict(list)
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if not _is_active_document(path, root):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        header = _header(text)
        ids = DOCUMENT_ID_COLON_RE.findall(header) + DOCUMENT_ID_BLOCK_RE.findall(header)

        # A file may contain a retired/stale metadata block followed by its
        # current canonical Document ID. Prefer the ID that matches its filename.
        filename_match = FILENAME_ID_RE.search(path.relative_to(root).as_posix())
        filename_id = filename_match.group(1) if filename_match else None
        if filename_id and filename_id in ids:
            ids = [filename_id]
        else:
            ids = list(dict.fromkeys(ids))

        for document_id in ids:
            owners[document_id].append(path.relative_to(root).as_posix())
    return owners


def test_active_document_id_is_unique_within_current_evidence_scope():
    root = Path(__file__).resolve().parents[2]
    owners = _extract_document_ids(root)
    duplicates = {
        document_id: paths
        for document_id, paths in owners.items()
        if len(set(paths)) > 1
    }
    assert not duplicates, f"active Document ID collisions: {duplicates}"


def test_known_historical_identity_migrations_remain_resolved():
    root = Path(__file__).resolve().parents[2]
    owners = _extract_document_ids(root)
    assert owners["GOV-005"] == ["Governance/GOV-005_REVIEW_STANDARD.md"]
    assert owners["LIF-001"] == ["Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md"]
    assert owners["ARC-001"] == ["Architecture/ARC-001_PLATFORM_ARCHITECTURE.md"]
