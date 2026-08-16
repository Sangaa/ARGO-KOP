import json
from pathlib import Path

from canonical_spine_gap_map import SEAMS


def _records(root: Path):
    declared = {f"{source} -> {destination}" for source, destination in SEAMS}
    records = {}
    for path in sorted((root / "Quality/Integration/evidence/runtime").glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and payload.get("seam") in declared:
            seam = payload["seam"]
            assert seam not in records, f"duplicate runtime registry record: {seam}"
            records[seam] = payload
        elif isinstance(payload, dict):
            for seam, record in payload.items():
                if seam in declared:
                    assert seam not in records, f"duplicate runtime registry record: {seam}"
                    records[seam] = record
    return declared, records


def test_runtime_registry_coverage_is_eleven_verified_seams():
    root = Path(__file__).resolve().parents[2]
    declared, records = _records(root)
    assert len(declared) == 11
    assert len(records) == 11

    for seam in declared:
        payload = records[seam]
        assert payload["state"] == "CONNECTED"
        assert payload["verification_status"] == "VERIFIED"
        for key in ("contract", "test", "trace"):
            assert (root / payload[key]).is_file(), (seam, key, payload[key])

    authorization_execution = records["Authorization -> Execution"]
    assert authorization_execution.get("evidence_mode", "CONTROLLED_SYNTHETIC") == "CONTROLLED_SYNTHETIC"


def test_runtime_registry_coverage_does_not_count_registry_handoff_as_canonical_seam():
    root = Path(__file__).resolve().parents[2]
    declared, records = _records(root)
    assert "Learning Pipeline -> Verified Registry" not in declared
    assert "Learning Pipeline -> Verified Registry" not in records
