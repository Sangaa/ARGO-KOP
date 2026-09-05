from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "Repository" / "P13_KNOWLEDGE_CONTROL_PLANE_RECONCILIATION_PLAN_2026-09-05_E.tsv"
INV = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv"
REP002 = ROOT / "Repository" / "REP-002_REPOSITORY_MAP.md"
REP012 = ROOT / "Repository" / "REP-012_REPOSITORY_ALLOCATION_REGISTRY.md"
REP013 = ROOT / "Repository" / "REP-013_REPOSITORY_CONTENT_TREE.md"
REP001 = ROOT / "Repository" / "REP-001_MASTER_INDEX.md"
STATUS = ROOT / "Knowledge" / "_FOLDER_STATUS.md"
DIGEST = "8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7"


def _inventory_paths():
    lines = INV.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "path\tphysical_role\tauthority_effect"
    return [line.split("\t", 1)[0] for line in lines[1:] if line.strip()]


def test_transaction_a_exact_inventory_is_self_consistent() -> None:
    paths = _inventory_paths()
    assert len(paths) == 50
    assert len(set(paths)) == 50
    payload = "".join(f"{path}\n" for path in sorted(paths)).encode()
    assert hashlib.sha256(payload).hexdigest() == DIGEST
    status = STATUS.read_text(encoding="utf-8")
    assert "Exact tracked leaf count\n`50`" in status
    assert DIGEST in status


def test_current_control_plane_debts_are_distinct_and_not_silently_closed() -> None:
    rep013 = REP013.read_text(encoding="utf-8")
    knowledge_section = rep013.split("### Knowledge/", 1)[1].split("### Engine/", 1)[0]
    assert "KNW-002_KNOWLEDGE_CLASSIFICATION.md" in knowledge_section
    assert "KNW-003_KNOWLEDGE_RELATIONSHIPS.md" in knowledge_section
    assert "KNW-004_KNOWLEDGE_LIFECYCLE.md" in knowledge_section
    assert "KNW-008_KNOWLEDGE_TRACEABILITY.md" in knowledge_section
    assert "KNW-009_KNOWLEDGE_EVOLUTION.md" in knowledge_section
    assert "KNW-001_KNOWLEDGE_MODEL.md" not in knowledge_section
    assert DIGEST not in rep013

    rep002 = REP002.read_text(encoding="utf-8")
    assert DIGEST not in rep002
    assert "P13 KNOWLEDGE" not in rep002.upper()

    rep012 = REP012.read_text(encoding="utf-8")
    assert DIGEST not in rep012
    assert "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv" not in rep012


def test_rep001_admission_is_separate_from_physical_reconciliation() -> None:
    plan = PLAN.read_text(encoding="utf-8")
    assert "REP-001\t1.7.8\tACTIVE_ADMISSION_INTENTIONALLY_HELD" in plan
    assert "NO_MUTATION_UNTIL_P13_DOMAIN_ADMISSION_REVIEW" in plan
    rep001 = REP001.read_text(encoding="utf-8")
    assert "Knowledge/KNW-001_KNOWLEDGE_MODEL.md" not in rep001


def test_control_plane_plan_never_promotes_by_inventory() -> None:
    text = PLAN.read_text(encoding="utf-8")
    assert "NONE_FROM_INVENTORY" in text
    assert "NONE_FROM_MAPPING" in text
    assert "NONE_FROM_ALLOCATION" in text
    assert "CLOSED_FOR_PHASE_1" not in text
    assert "GLOBAL PASS" not in text
