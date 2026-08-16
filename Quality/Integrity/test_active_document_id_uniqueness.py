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
EXCLUDED_PATTERNS = (
    "/REP-020_SESSION_DELTA_",
    "/REP-020_MATRIX_ADDENDUM_",
    "/REP-020_REVALIDATION_ADDENDUM_",
)
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".yaml", ".yml", ".json"}


def _is_active_document(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel.startswith(EXCLUDED_PREFIXES):
        return False
    if any(pattern in f"/{rel}" for pattern in EXCLUDED_PATTERNS):
        return False
    return True


def _header(text: str) -> str:
    for marker in ("# Purpose", "Purpose\n", "# 1."):
        if marker in text:
            text = text.split(marker, 1)[0]
    return text[:12000]


def _filename_id(path: Path):
    token = path.stem.split("_", 1)[0]
    return token if ID_RE.fullmatch(token) else None


def _metadata_value(text: str, key: str):
    block = re.search(rf"^\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text, re.MULTILINE | re.IGNORECASE)
    if block:
        return block.group(1).strip().lower()
    block = re.search(rf"^\s*{re.escape(key)}\s*$\n\s*([^\n]+?)\s*$", text, re.MULTILINE | re.IGNORECASE)
    return block.group(1).strip().lower() if block else None


def _has_canonical_yes(text: str) -> bool:
    return _metadata_value(text, "Canonical") == "yes"


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
        if not _has_canonical_yes(header):
            continue

        filename_id = _filename_id(path)
        has_declared_id = bool(re.search(r"^\s*Document ID\b", header, re.MULTILINE | re.IGNORECASE))
        if filename_id and has_declared_id:
            ids = [filename_id]
        else:
            ids = DOCUMENT_ID_COLON_RE.findall(header) + DOCUMENT_ID_BLOCK_RE.findall(header)
            ids = list(dict.fromkeys(ids))

        for document_id in ids:
            owners[document_id].append(path.relative_to(root).as_posix())
    return owners


def test_active_canonical_document_id_is_unique_within_current_evidence_scope():
    root = Path(__file__).resolve().parents[2]
    owners = _extract_document_ids(root)
    duplicates = {
        document_id: paths
        for document_id, paths in owners.items()
        if len(set(paths)) > 1
    }
    assert not duplicates, f"active canonical Document ID collisions: {duplicates}"


def test_known_historical_identity_migrations_remain_resolved():
    root = Path(__file__).resolve().parents[2]
    governance = (root / "Governance/GOV-005_REVIEW_STANDARD.md").read_text(encoding="utf-8")
    lifecycle = (root / "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md").read_text(encoding="utf-8")
    architecture = (root / "Architecture/ARC-001_PLATFORM_ARCHITECTURE.md").read_text(encoding="utf-8")

    assert "Document ID: GOV-005" in governance
    assert "LIF-001" in lifecycle and _has_canonical_yes(lifecycle)
    assert "ARC-001" in architecture and _has_canonical_yes(architecture)
    assert not (root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md").exists()


def test_known_identity_boundaries_are_explicitly_classified():
    root = Path(__file__).resolve().parents[2]
    for relative in (
        "Core/CORE-000_PLATFORM_IDENTITY.md",
        "Memory/MEM-008_MEMORY_TRACEABILITY.md",
        "Interfaces/INTF-002_GITHUB.md",
        "Interfaces/INTF-003_DATABASE.md",
        "Interfaces/INTF-006_WEB.md",
    ):
        text = (root / relative).read_text(encoding="utf-8")
        assert _metadata_value(text, "Canonical") == "no"
