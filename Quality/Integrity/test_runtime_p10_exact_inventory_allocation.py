import csv
import hashlib
from collections import Counter
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "Repository/REP-012_PRIORITY10_RUNTIME_EXACT_ALLOCATION_MANIFEST_2026-09-03_N.tsv"
REP012 = ROOT / "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md"
REP013 = ROOT / "Repository/REP-013_REPOSITORY_CONTENT_TREE.md"
STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"
EXPECTED_DIGEST = "a5db51a6d6cbf7dbf22bdb971fc0d2238d2bdef6627caadc4ee2b1933dad4438"
EXPECTED_DIRECTORIES = {
    "TOP": 17,
    "Context": 4,
    "Decision": 12,
    "Execution": 41,
    "Integration": 2,
    "Learning": 17,
    "Prototype": 25,
}
EXPECTED_CLASSES = {
    "CANONICAL_RUNTIME_CONTRACT": 10,
    "CANDIDATE_RUNTIME_CONTRACT": 5,
    "SUPPORTING_CONTRACT": 24,
    "IMPLEMENTATION": 36,
    "TEST": 36,
    "NAVIGATION": 2,
    "STATUS_EVIDENCE": 1,
    "EVIDENCE_REPORT": 1,
    "SCHEMA": 1,
    "TEST_FIXTURE": 1,
    "TEST_CONFIGURATION": 1,
}


def tracked_runtime_paths() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "Runtime"],
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(line for line in result.stdout.splitlines() if line)


def manifest_rows() -> list[dict[str, str]]:
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_manifest_is_exactly_the_current_git_tracked_runtime_inventory():
    paths = tracked_runtime_paths()
    rows = manifest_rows()
    manifest_paths = [row["path"] for row in rows]
    assert len(paths) == 118
    assert manifest_paths == paths
    assert len(manifest_paths) == len(set(manifest_paths))
    digest = hashlib.sha256("".join(f"{path}\n" for path in paths).encode()).hexdigest()
    assert digest == EXPECTED_DIGEST


def test_every_runtime_path_has_a_bounded_allocation_role_without_authority_promotion():
    rows = manifest_rows()
    assert Counter(row["artifact_class"] for row in rows) == Counter(EXPECTED_CLASSES)
    assert {row["domain"] for row in rows} == {"Runtime"}
    assert {row["allocation_state"] for row in rows} == {"ALLOCATED"}
    assert {row["authority_effect"] for row in rows} == {"NONE_BY_ALLOCATION"}

    directory_counts = Counter()
    for row in rows:
        parts = Path(row["path"]).parts
        directory_counts["TOP" if len(parts) == 2 else parts[1]] += 1
    assert directory_counts == Counter(EXPECTED_DIRECTORIES)


def test_control_surfaces_bind_the_exact_manifest_but_do_not_close_p10_implicitly():
    rep012 = REP012.read_text(encoding="utf-8")
    rep013 = REP013.read_text(encoding="utf-8")
    status = STATUS.read_text(encoding="utf-8")
    for text in (rep012, rep013, status):
        assert EXPECTED_DIGEST in text
        assert "118" in text
    assert MANIFEST.name in rep012
    assert MANIFEST.name in rep013
    assert "NONE_BY_ALLOCATION" in rep012
    assert "Priority 10 remains OPEN pending a separate explicit bounded closure-readiness decision." in status
