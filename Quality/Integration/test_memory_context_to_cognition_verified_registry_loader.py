import json
from pathlib import Path

from verified_seam_evidence_loader import load_records


def test_memory_context_to_cognition_registry_record_loads_as_connected():
    root = Path(__file__).resolve().parents[2]
    record_path = root / "Quality/Integration/evidence/runtime/memory_context_to_cognition_verified_registry.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    registry = load_records(root, [record])
    assert registry["Memory / Context -> Cognition"]["state"] == "CONNECTED"
    assert registry["Memory / Context -> Cognition"]["verification_status"] == "VERIFIED"


def test_memory_context_to_cognition_registry_cannot_bypass_evidence_materialization():
    root = Path(__file__).resolve().parents[2]
    record = {
        "seam": "Memory / Context -> Cognition",
        "contract": "Cognition/CONTEXT_MEMORY_SELECTION_CONTRACT.md",
        "test": "Quality/Integration/test_memory_to_context_selection_boundary.py",
        "trace": "Quality/Integration/evidence/runtime/does-not-exist.json",
        "verification_status": "VERIFIED",
    }
    assert load_records(root, [record]) == {}
