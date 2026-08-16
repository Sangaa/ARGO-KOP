import json
from pathlib import Path

from canonical_spine_gap_map import SEAMS


def test_verified_runtime_records_reference_existing_trace_and_test_files():
    root = Path(__file__).resolve().parents[2]
    declared = {f"{source} -> {destination}" for source, destination in SEAMS}
    registry_dir = root / "Quality/Integration/evidence/runtime"
    checked = 0
    for path in sorted(registry_dir.glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        seam = payload.get("seam")
        if seam not in declared:
            continue
        checked += 1
        assert payload.get("state") == "CONNECTED"
        assert payload.get("verification_status") == "VERIFIED"
        for key in ("contract", "test", "trace"):
            assert payload.get(key)
            assert (root / payload[key]).is_file(), (seam, key, payload[key])
    assert checked > 0
