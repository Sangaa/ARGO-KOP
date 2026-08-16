import json
from pathlib import Path

from canonical_spine_gap_map import SEAMS
from canonical_spine_consolidated_audit import build_consolidated_audit


def _runtime_registry_records(root: Path):
    records = []
    for path in sorted((root / "Quality/Integration/evidence/runtime").glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and payload.get("seam"):
            records.append((payload["seam"], payload))
    return records


def test_runtime_registry_reconciles_only_declared_canonical_seams():
    root = Path(__file__).resolve().parents[2]
    declared = {f"{source} -> {destination}" for source, destination in SEAMS}
    records = _runtime_registry_records(root)
    assert records
    for seam, payload in records:
        if seam in declared:
            assert payload.get("verification_status") == "VERIFIED"
            assert payload.get("state") == "CONNECTED"


def test_learning_registry_handoff_is_not_promoted_into_canonical_spine():
    root = Path(__file__).resolve().parents[2]
    result = build_consolidated_audit(root)
    assert result["seam_count"] == len(SEAMS) == 11
    assert "Learning Pipeline -> Verified Registry" not in set(result["connected"] + result["partial"] + result["missing"])
