from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
INV = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv"
ADD = ROOT / "Repository" / "REP-013_PRIORITY13_KNOWLEDGE_EXACT_CONTENT_TREE_ADDENDUM_2026-09-05_F.md"
REP013 = ROOT / "Repository" / "REP-013_REPOSITORY_CONTENT_TREE.md"
DIGEST = "8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7"


def _paths():
    lines = INV.read_text(encoding="utf-8").splitlines()
    return [line.split("\t", 1)[0] for line in lines[1:] if line.strip()]


def test_rep013_addendum_binds_exact_p13_knowledge_set() -> None:
    paths = _paths()
    assert len(paths) == 50
    payload = "".join(f"{p}\n" for p in sorted(paths)).encode()
    assert hashlib.sha256(payload).hexdigest() == DIGEST
    add = ADD.read_text(encoding="utf-8")
    assert "Tracked leaf count: `50`" in add
    assert DIGEST in add
    for path in paths:
        rel = path.removeprefix("Knowledge/")
        assert rel in add


def test_addendum_is_nonpromoting_and_rep013_fold_remains_open() -> None:
    add = ADD.read_text(encoding="utf-8")
    assert "ADDENDUM EVIDENCE != CANONICAL REP-013 SYNCHRONIZATION" in add
    assert "CANONICAL REP-013 SYNCHRONIZATION = OPEN" in add
    assert "PRIORITY 13 = OPEN" in add
    assert "Learning/Programming/Mathematics files are not promoted" in add

    rep013 = REP013.read_text(encoding="utf-8")
    old = rep013.split("### Knowledge/", 1)[1].split("### Engine/", 1)[0]
    assert "KNW-001_KNOWLEDGE_MODEL.md" not in old
    assert "KNW-002_KNOWLEDGE_CLASSIFICATION.md" in old
    assert DIGEST not in rep013


def test_addendum_does_not_claim_relationship_or_closure_semantics() -> None:
    add = ADD.read_text(encoding="utf-8")
    authority = add.split("## Authority boundary", 1)[1].split("## Canonical synchronization requirement", 1)[0]
    assert "no dependency, consumer, relationship, review, active-index admission or partition closure" in authority
