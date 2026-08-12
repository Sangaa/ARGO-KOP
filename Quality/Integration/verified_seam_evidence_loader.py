"""Load only evidence that exists as local contract/test/trace artifacts."""

from pathlib import PurePosixPath

from verified_seam_evidence_registry import register


def _exists(root, relative):
    return (root / PurePosixPath(relative)).exists()


def load_records(root, candidates):
    records = []
    for candidate in candidates:
        if all(_exists(root, candidate[field]) for field in ("contract", "test", "trace")):
            records.append(candidate)
    return register(records)
