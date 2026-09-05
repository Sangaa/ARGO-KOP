import csv
import hashlib
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository/REP-012_PRIORITY12_MODELS_EXACT_ALLOCATION_MANIFEST_2026-09-05_A.tsv"
STATUS = ROOT / "Models/_FOLDER_STATUS.md"
DIGEST = "cf8274ea93cabcb0e55e47b55b00050c1dab98c888582b3b4c2a858c36621498"
EXPECTED = [
    "Models/MOD-001_KNOWLEDGE_MODEL.md",
    "Models/MOD-002_ENTITY_MODEL.md",
    "Models/MOD-003_DOCUMENT_MODEL.md",
    "Models/MOD-004_MEMORY_MODEL.md",
    "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
    "Models/README.md",
    "Models/_FOLDER_STATUS.md",
]


def tracked_paths():
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "Models"],
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(line for line in result.stdout.splitlines() if line)


def manifest_rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_p12_models_manifest_equals_exact_git_tree():
    paths = tracked_paths()
    assert paths == EXPECTED
    assert len(paths) == 7
    assert hashlib.sha256("".join(f"{path}\n" for path in paths).encode()).hexdigest() == DIGEST
    rows = manifest_rows()
    assert [row["path"] for row in rows] == EXPECTED
    assert len({row["path"] for row in rows}) == 7


def test_p12_models_allocation_is_non_authoritative():
    rows = manifest_rows()
    assert {row["domain"] for row in rows} == {"Models"}
    assert {row["allocation_state"] for row in rows} == {"ALLOCATED"}
    assert {row["authority_effect"] for row in rows} == {"NONE_BY_ALLOCATION"}
    classes = {row["path"]: row["artifact_class"] for row in rows}
    for path in EXPECTED[:5]:
        assert classes[path] == "MODEL_ARTIFACT_EXISTING_AUTHORITY_UNCHANGED"
    assert classes["Models/README.md"] == "DOMAIN_CONTAINER_EVIDENCE"
    assert classes["Models/_FOLDER_STATUS.md"] == "STATUS_EVIDENCE"


def test_p12_models_status_preserves_open_relationship_boundary():
    status = STATUS.read_text(encoding="utf-8")
    assert "7 tracked top-level files" in status
    assert DIGEST in status
    assert "NONE_BY_ALLOCATION" in status
    assert "Priority 12 remains **OPEN**" in status
    assert "INTEGRITY HOLD / STAGED RECONSTRUCTION" in status
    assert "MOD-011" in status and "Proposed / Future-Ready" in status
    assert "Transaction A is `CLOSED / VERIFIED / RESUME-SAFE`" in status
    assert "relationship/content graph" in status
    assert "EXACT PHYSICAL INVENTORY != ACTIVE SEMANTIC AUTHORITY" in status
