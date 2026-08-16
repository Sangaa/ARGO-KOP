import json
from pathlib import Path

from canonical_spine_gap_map import SEAMS


def _payload_records(payload):
    if isinstance(payload, dict) and "seam" in payload:
        yield payload["seam"], payload
        return
    if isinstance(payload, dict):
        for seam, record in payload.items():
            if isinstance(record, dict):
                yield seam, record


def test_verified_runtime_registry_has_exactly_one_record_per_declared_seam():
    root = Path(__file__).resolve().parents[2]
    declared = {f"{source} -> {destination}" for source, destination in SEAMS}
    registry_dir = root / "Quality/Integration/evidence/runtime"
    records = {}
    for path in sorted(registry_dir.glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for seam, record in _payload_records(payload):
            if seam in declared:
                assert seam not in records, f"duplicate runtime registry record: {seam}"
                records[seam] = record

    missing = declared - set(records)
    assert not missing, f"canonical seams missing runtime registry records: {sorted(missing)}"

    for seam, payload in records.items():
        assert payload.get("state") == "CONNECTED"
        assert payload.get("verification_status") == "VERIFIED"
        for key in ("contract", "test", "trace"):
            assert (root / payload[key]).is_file(), (seam, key, payload[key])
