import csv
import hashlib
from collections import Counter
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository/REP-012_PRIORITY11_INTERFACES_EXACT_ALLOCATION_MANIFEST_2026-09-03_A.tsv"
REP001 = ROOT / "Repository/REP-001_MASTER_INDEX.md"
REP002 = ROOT / "Repository/REP-002_REPOSITORY_MAP.md"
REP012 = ROOT / "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md"
REP013 = ROOT / "Repository/REP-013_REPOSITORY_CONTENT_TREE.md"
STATUS = ROOT / "Interfaces/_FOLDER_STATUS.md"
DIGEST = "81e052fe0ae6cf61f6a70b15acafa4cd07e5372ef168a1228790db314c8eaae9"
CLASSES = Counter({
    "CANONICAL_INTERFACE_CONTRACT": 3,
    "INTERFACE_ARTIFACT_UNPROMOTED": 6,
    "CANDIDATE_CANONICAL_INTERFACE_CONTRACT": 1,
    "LEGACY_NONCANONICAL_PROVENANCE": 1,
    "STATUS_EVIDENCE": 1,
})


def tracked_paths():
    result = subprocess.run(["git", "-C", str(ROOT), "ls-files", "Interfaces"], check=True, capture_output=True, text=True)
    return sorted(line for line in result.stdout.splitlines() if line)


def rows():
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_manifest_equals_exact_git_interfaces_tree():
    paths = tracked_paths()
    manifest_paths = [row["path"] for row in rows()]
    assert len(paths) == 12
    assert manifest_paths == paths
    assert len(manifest_paths) == len(set(manifest_paths))
    assert hashlib.sha256("".join(f"{path}\n" for path in paths).encode()).hexdigest() == DIGEST


def test_allocations_are_complete_and_non_authoritative():
    manifest = rows()
    assert Counter(row["artifact_class"] for row in manifest) == CLASSES
    assert {row["domain"] for row in manifest} == {"Interfaces"}
    assert {row["allocation_state"] for row in manifest} == {"ALLOCATED"}
    assert {row["authority_effect"] for row in manifest} == {"NONE_BY_ALLOCATION"}


def test_current_control_surfaces_bind_all_paths_and_keep_p11_open():
    paths = tracked_paths()
    for surface in (REP002, REP013, STATUS):
        text = surface.read_text(encoding="utf-8")
        for path in paths:
            assert path.removeprefix("Interfaces/") in text, (surface, path)
    rep001 = REP001.read_text(encoding="utf-8")
    for active in ("INTF-001_INTERFACE_SPEC.md", "INTF-004_API.md", "INTF-006_ENVIRONMENT_SENSING.md", "INTF-010_INTEGRATIONS.md", "_FOLDER_STATUS.md"):
        assert active in rep001
    for inactive in ("INTF-006_WEB.md", "INTF-007_USER_INTERFACE.md", "INTF-008_CONNECTORS.md", "INTF-009_IMPORT_EXPORT.md"):
        assert inactive not in rep001
    for surface in (REP012, REP013, STATUS):
        text = surface.read_text(encoding="utf-8")
        assert DIGEST in text
        assert "12" in text
    assert MANIFEST.name in REP012.read_text(encoding="utf-8")
    assert "P11 / INTERFACES = IN_PROGRESS" in STATUS.read_text(encoding="utf-8")
    assert "provider authenticity" in STATUS.read_text(encoding="utf-8")
