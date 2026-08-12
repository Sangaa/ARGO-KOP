"""Explicit evidence registry for promoting canonical seams to CONNECTED."""

from canonical_spine_gap_map import SEAMS

SEAM_KEYS = {f"{s} -> {d}" for s, d in SEAMS}
REQUIRED_EVIDENCE = ("contract", "test", "trace")


def register(records):
    registry = {}
    for record in records:
        seam = record["seam"]
        if seam not in SEAM_KEYS:
            raise ValueError(f"unknown seam: {seam}")
        if seam in registry:
            raise ValueError(f"duplicate seam evidence: {seam}")
        if not all(record.get(field) for field in REQUIRED_EVIDENCE):
            raise ValueError(f"incomplete evidence: {seam}")
        registry[seam] = {
            "state": "CONNECTED",
            "contract": record["contract"],
            "test": record["test"],
            "trace": record["trace"],
        }
    return registry
