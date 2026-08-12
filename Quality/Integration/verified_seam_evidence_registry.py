"""Explicit evidence registry for promoting canonical seams to CONNECTED.

The registry is intentionally evidence-shaped, not trust-shaped: it accepts only
canonical seam keys and complete repository-relative evidence references.
Actual file materialization is verified by the loader/audit boundary.

Registry promotion remains conservative: an evidence record must explicitly
carry a verified evidence status; the registry does not infer verification from
file names or from candidate provenance.
"""

from pathlib import PurePosixPath

from canonical_spine_gap_map import SEAMS

SEAM_KEYS = {f"{s} -> {d}" for s, d in SEAMS}
REQUIRED_EVIDENCE = ("contract", "test", "trace")


def _valid_reference(value):
    if not isinstance(value, str) or not value.strip():
        return False
    path = PurePosixPath(value)
    return bool(path.parts) and not path.is_absolute() and ".." not in path.parts


def register(records):
    registry = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("seam evidence must be a record")
        seam = record.get("seam")
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        if seam in registry:
            raise ValueError(f"duplicate seam evidence: {seam}")
        if record.get("verification_status") != "VERIFIED":
            raise ValueError(f"evidence not verified: {seam}")
        if not all(_valid_reference(record.get(field)) for field in REQUIRED_EVIDENCE):
            raise ValueError(f"invalid or incomplete evidence: {seam}")
        registry[seam] = {
            "state": "CONNECTED",
            "contract": record["contract"],
            "test": record["test"],
            "trace": record["trace"],
            "verification_status": "VERIFIED",
        }
    return registry
