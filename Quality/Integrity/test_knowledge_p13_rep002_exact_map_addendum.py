from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
INV = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv"
ADD = ROOT / "Repository" / "REP-002_PRIORITY13_KNOWLEDGE_EXACT_MAP_ADDENDUM_2026-09-05_G.md"
REP002 = ROOT / "Repository" / "REP-002_REPOSITORY_MAP.md"
REP001 = ROOT / "Repository" / "REP-001_MASTER_INDEX.md"
DIGEST = "8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7"


def _paths():
    lines = INV.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "path\tphysical_role\tauthority_effect"
    return [line.split("\t", 1)[0] for line in lines[1:] if line.strip()]


def test_rep002_addendum_binds_exact_transaction_a_path_set() -> None:
    paths = _paths()
    assert len(paths) == 50
    payload = "".join(f"{p}\n" for p in sorted(paths)).encode()
    assert hashlib.sha256(payload).hexdigest() == DIGEST
    add = ADD.read_text(encoding="utf-8")
    assert "Tracked leaf count: `50`" in add
    assert DIGEST in add
    assert "b7f215c7a1d6e028b28125e2ce5d3b1abc5be061" in add
    assert "identical" in add


def test_mapping_addendum_preserves_active_admission_boundary() -> None:
    add = ADD.read_text(encoding="utf-8")
    assert "PHYSICAL MAP != ACTIVE INDEX ADMISSION != SEMANTIC AUTHORITY" in add
    assert "CANONICAL FIELD != ACTIVE INDEX ADMISSION" in add
    assert "REP-001 ACTIVE ADMISSION = SEPARATE / HELD" in add
    assert "PRIORITY 13 = OPEN" in add
    rep001 = REP001.read_text(encoding="utf-8")
    assert "Knowledge/KNW-001_KNOWLEDGE_MODEL.md" not in rep001


def test_canonical_rep002_fold_remains_explicitly_open() -> None:
    add = ADD.read_text(encoding="utf-8")
    assert "CANONICAL REP-002 SYNCHRONIZATION = OPEN" in add
    rep002 = REP002.read_text(encoding="utf-8")
    assert DIGEST not in rep002
    assert "P13 EXACT KNOWLEDGE PHYSICAL MAP" not in rep002.upper()
