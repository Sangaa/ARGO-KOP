from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
INV = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv"
MAN = ROOT / "Repository" / "REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_MANIFEST_2026-09-05_H.tsv"
ADD = ROOT / "Repository" / "REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_BINDING_2026-09-05_H.md"
REP012 = ROOT / "Repository" / "REP-012_REPOSITORY_ALLOCATION_REGISTRY.md"
DIGEST = "8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7"


def _inventory_rows():
    lines = INV.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "path\tphysical_role\tauthority_effect"
    return [line.split("\t") for line in lines[1:] if line.strip()]


def _manifest_rows():
    lines = MAN.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "path\tphysical_role\tallocation_state\tauthority_effect\tsource_evidence"
    return [line.split("\t") for line in lines[1:] if line.strip()]


def test_allocation_manifest_is_exact_transform_of_transaction_a_inventory() -> None:
    inv = _inventory_rows()
    man = _manifest_rows()
    assert len(inv) == len(man) == 50
    assert len({r[0] for r in man}) == 50
    expected = [[path, role, "ALLOCATED", "NONE_BY_ALLOCATION", "P13_TRANSACTION_A_EXACT_INVENTORY"] for path, role, _ in inv]
    assert man == expected
    payload = "".join(f"{r[0]}\n" for r in sorted(man)).encode()
    assert hashlib.sha256(payload).hexdigest() == DIGEST


def test_allocation_binding_is_nonpromoting_and_open() -> None:
    add = ADD.read_text(encoding="utf-8")
    assert "Tracked Knowledge leaves: `50`" in add
    assert DIGEST in add
    assert "ALLOCATED != MAPPED ACTIVE AUTHORITY != REVIEWED != CANONICAL PROMOTION != CLOSED_FOR_PHASE_1" in add
    assert "CANONICAL REP-012 SYNCHRONIZATION = OPEN" in add
    assert "PRIORITY 13 = OPEN" in add
    assert all(r[2] == "ALLOCATED" and r[3] == "NONE_BY_ALLOCATION" for r in _manifest_rows())


def test_current_canonical_rep012_is_not_silently_treated_as_folded() -> None:
    rep012 = REP012.read_text(encoding="utf-8")
    assert "Version: 1.0.13" in rep012
    assert DIGEST not in rep012
    assert "REP-012_PRIORITY13_KNOWLEDGE_EXACT_ALLOCATION_MANIFEST_2026-09-05_H.tsv" not in rep012
