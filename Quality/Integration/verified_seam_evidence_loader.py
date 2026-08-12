"""Load only evidence that exists as local contract/test/trace artifacts."""

from pathlib import Path, PurePosixPath

from verified_seam_evidence_registry import register


def _exists(root: Path, relative: str) -> bool:
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        return False
    return (root / path).is_file()


def load_records(root, candidates):
    records = []
    for candidate in candidates:
        if all(_exists(root, candidate.get(field, "")) for field in ("contract", "test", "trace")):
            records.append(candidate)
    return register(records)
