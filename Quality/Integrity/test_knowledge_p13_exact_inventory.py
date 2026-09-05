from __future__ import annotations

from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "Knowledge"
INVENTORY = ROOT / "Repository" / "MUT-2026-09-05-P13-KNOWLEDGE-EXACT-INVENTORY-ALLOCATION-A_INVENTORY.tsv"
STATUS = KNOWLEDGE / "_FOLDER_STATUS.md"
README = KNOWLEDGE / "README.md"
EXPECTED_DIGEST = "8ef530bc3b91a11e68e01df02e6d7bb29de4ee7824eada45c0b2928e03f85dc7"


def _repo_paths_from_tree() -> list[str]:
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in KNOWLEDGE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    )


def _manifest_paths() -> list[str]:
    lines = INVENTORY.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "path\tphysical_role\tauthority_effect"
    return sorted(line.split("\t", 1)[0] for line in lines[1:] if line.strip())


def test_exact_knowledge_inventory_matches_manifest() -> None:
    actual = _repo_paths_from_tree()
    expected = _manifest_paths()
    assert len(actual) == 50
    assert actual == expected
    digest = sha256(("\n".join(actual) + "\n").encode()).hexdigest()
    assert digest == EXPECTED_DIGEST


def test_allocation_does_not_promote_supporting_surfaces() -> None:
    status = STATUS.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    assert "PRIORITY-13 EXACT INVENTORY VERIFIED" in status
    assert "PHYSICAL ALLOCATION != CANONICAL PROMOTION != RELATIONSHIP VALIDATION != PARTITION CLOSURE" in status
    for i in range(1, 11):
        assert f"KNW-{i:03d}_" in readme
    assert "Knowledge/Learning" not in readme.split("## Canonical Artifacts", 1)[1].split("## Authority Boundary", 1)[0]
    assert "Priority 13 remains OPEN" in status
