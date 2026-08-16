from collections import defaultdict
from pathlib import Path
import re


DOCUMENT_ID_COLON_RE = re.compile(r"^Document ID:\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
DOCUMENT_ID_BLOCK_RE = re.compile(r"^\s*Document ID\s*:?\s*$\n(?:\s*\n)*\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
ID_RE = re.compile(r"^[A-Za-z]+-\d+$")
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
    for marker in ("# Purpose", "Purpose\n", "# 1."):
        if marker in text:
            text = text.split(marker, 1)[0]
    return text[:12000]


def _filename_id(path: Path):
    token = path.stem.split("_", 1)[0]
    return token if ID_RE.fullmatch(token) else None


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
        filename_id = _filename_id(path)
        if filename_id and re.search(r"^\s*Document ID\b", header, re.MULTILINE | re.IGNORECASE):
            ids = [filename_id]
        else:
            ids = DOCUMENT_ID_COLON_RE.findall(header) + DOCUMENT_ID_BLOCK_RE.findall(header)
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
