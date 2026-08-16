from collections import defaultdict
from pathlib import Path
import re

DOCUMENT_ID_COLON_RE = re.compile(r"^Document ID:\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
DOCUMENT_ID_BLOCK_RE = re.compile(r"^\s*Document ID\s*:?\s*$\n(?:\s*\n)*\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", re.MULTILINE)
ID_RE = re.compile(r"^[A-Za-z]+-\d+$")
EXCLUDED_PREFIXES = ("Archive/", "Memory/Engineering_Journal/", "Quality/Integration/evidence/", "Quality/Integration/canonical_evidence/", "Quality/Integrity/")
EXCLUDED_PATTERNS = ("/REP-020_SESSION_DELTA_", "/REP-020_MATRIX_ADDENDUM_", "/REP-020_REVALIDATION_ADDENDUM_")
KNOWN_NONCANONICAL = {"Core/CORE-000_PLATFORM_IDENTITY.md", "Memory/MEM-008_MEMORY_TRACEABILITY.md", "Interfaces/INTF-002_GITHUB.md", "Interfaces/INTF-003_DATABASE.md", "Interfaces/INTF-006_WEB.md"}
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".yaml", ".yml", ".json"}


def _is_active_document(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel in KNOWN_NONCANONICAL or rel.startswith(EXCLUDED_PREFIXES):
        return False
    return not any(pattern in f"/{rel}" for pattern in EXCLUDED_PATTERNS)


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
    block = re.search(rf"^\s*{re.escape(key)}\s*$\n(?:\s*\n)*\s*([^\n]+?)\s*$", text, re.MULTILINE | re.IGNORECASE)
    return block.group(1).strip().lower() if block else None


def _document_ids(text: str):
    values = DOCUMENT_ID_COLON_RE.findall(text) + DOCUMENT_ID_BLOCK_RE.findall(text)
    return list(dict.fromkeys(values))


def _has_canonical_yes(text: str) -> bool:
    return _metadata_value(text, "Canonical") == "yes"


def _extract_document_ids(root: Path):
    owners = defaultdict(list)
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or not _is_active_document(path, root):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        header = _header(text)
        if not _has_canonical_yes(header):
            continue
        filename_id = _filename_id(path)
        declared_ids = _document_ids(header)
        ids = [filename_id] if filename_id and declared_ids else declared_ids
        for document_id in ids:
            owners[document_id].append(path.relative_to(root).as_posix())
    return owners


def test_active_canonical_document_id_is_unique_within_current_evidence_scope():
    root = Path(__file__).resolve().parents[2]
    owners = _extract_document_ids(root)
    duplicates = {document_id: paths for document_id, paths in owners.items() if len(set(paths)) > 1}
    assert not duplicates, f"active canonical Document ID collisions: {duplicates}"


def test_active_canonical_filename_and_document_id_do_not_drift():
    root = Path(__file__).resolve().parents[2]
    drifts = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or not _is_active_document(path, root):
            continue
        try:
            header = _header(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            continue
        if not _has_canonical_yes(header):
            continue
        filename_id = _filename_id(path)
        declared_ids = _document_ids(header)
        if filename_id and declared_ids and filename_id not in declared_ids:
            drifts[path.relative_to(root).as_posix()] = {"filename_id": filename_id, "declared_ids": declared_ids}
    assert not drifts, f"active canonical filename/Document ID drift: {drifts}"


def test_interfaces_folder_inventory_matches_current_canonical_api_identity():
    root = Path(__file__).resolve().parents[2]
    folder_status = (root / "Interfaces/_FOLDER_STATUS.md").read_text(encoding="utf-8")
    api = (root / "Interfaces/INTF-004_API.md").read_text(encoding="utf-8")
    inventory = folder_status.split("# Audit Findings", 1)[0]
    assert "`INTF-004_API.md` | `INTF-004` |" in inventory
    assert "`INTF-004_API.md` | `INT-004` |" not in inventory
    assert "Document ID: INTF-004" in api or "Document ID\nINTF-004" in api


def test_known_historical_identity_migrations_remain_resolved():
    root = Path(__file__).resolve().parents[2]
    governance = (root / "Governance/GOV-005_REVIEW_STANDARD.md").read_text(encoding="utf-8")
    lifecycle = (root / "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md").read_text(encoding="utf-8")
    architecture = (root / "Architecture/ARC-001_PLATFORM_ARCHITECTURE.md").read_text(encoding="utf-8")
    architecture_status = (root / "Architecture/_FOLDER_STATUS.md").read_text(encoding="utf-8")
    assert "Document ID: GOV-005" in governance
    assert "LIF-001" in lifecycle and _has_canonical_yes(lifecycle)
    assert "ARC-001" in architecture and "ARC-001" in architecture_status
    assert re.search(r"^Canonical\s*$\n(?:\s*\n)*\s*Yes\s+[—-]", architecture_status, re.MULTILINE)
    assert not (root / "Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md").exists()


def test_known_identity_boundaries_are_explicitly_classified():
    root = Path(__file__).resolve().parents[2]
    for relative in KNOWN_NONCANONICAL:
        text = (root / relative).read_text(encoding="utf-8")
        assert _metadata_value(text, "Canonical") == "no"


def test_current_models_identity_set_is_filename_and_metadata_consistent():
    root = Path(__file__).resolve().parents[2]
    expected = {
        "Models/MOD-001_KNOWLEDGE_MODEL.md": "MOD-001",
        "Models/MOD-002_ENTITY_MODEL.md": "MOD-002",
        "Models/MOD-003_DOCUMENT_MODEL.md": "MOD-003",
        "Models/MOD-004_MEMORY_MODEL.md": "MOD-004",
        "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md": "MOD-011",
    }
    findings = {}
    for relative, expected_id in expected.items():
        path = root / relative
        assert path.exists(), f"expected current Models artifact missing: {relative}"
        header = _header(path.read_text(encoding="utf-8"))
        filename_id = _filename_id(path)
        declared_ids = _document_ids(header)
        canonical = _metadata_value(header, "Canonical")
        if filename_id != expected_id or expected_id not in declared_ids or canonical != "yes":
            findings[relative] = {"expected_id": expected_id, "filename_id": filename_id, "declared_ids": declared_ids, "canonical": canonical}
    assert not findings, f"current Models identity drift: {findings}"
