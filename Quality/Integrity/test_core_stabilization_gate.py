import json
from pathlib import Path

from canonical_spine_gap_map import SEAMS


def _runtime_registry_records(root: Path):
    declared = {f"{source} -> {destination}" for source, destination in SEAMS}
    records = {}
    for path in sorted((root / "Quality/Integration/evidence/runtime").glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and payload.get("seam") in declared:
            records[payload["seam"]] = payload
        elif isinstance(payload, dict):
            for seam, record in payload.items():
                if seam in declared:
                    records[seam] = record
    return declared, records


def test_core_stabilization_gate_has_complete_canonical_spine_evidence():
    root = Path(__file__).resolve().parents[2]
    declared, records = _runtime_registry_records(root)
    assert len(declared) == 11
    assert set(records) == declared
    for seam, payload in records.items():
        assert payload["state"] == "CONNECTED", seam
        assert payload["verification_status"] == "VERIFIED", seam
        for key in ("contract", "test", "trace"):
            assert (root / payload[key]).is_file(), (seam, key, payload[key])


def test_core_stabilization_gate_preserves_noncanonical_registry_handoff_boundary():
    root = Path(__file__).resolve().parents[2]
    declared, records = _runtime_registry_records(root)
    assert "Learning Pipeline -> Verified Registry" not in declared
    assert "Learning Pipeline -> Verified Registry" not in records


def test_core_stabilization_gate_does_not_claim_repository_wide_integrity():
    status = (Path(__file__).resolve().parents[2] / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    assert "INTEGRITY WARNING" in status or "INTEGRITY HOLD" in status
    assert "CONNECT" in status and "BASELINE" in status and "AUDIT IN PROGRESS" in status
