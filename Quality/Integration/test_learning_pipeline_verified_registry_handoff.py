"""Prove the Learning Pipeline can hand off a verified record without promotion authority."""

import json
from pathlib import Path

from verified_seam_evidence_loader import load_records


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_learning_pipeline_verified_registry_handoff_is_materialized():
    registry_path = REPO_ROOT / "Quality/Integration/evidence/runtime/learning_pipeline_to_verified_registry_verified_registry.json"
    payload = json.loads(registry_path.read_text(encoding="utf-8"))

    assert payload["seam"] == "Learning Pipeline -> Verified Registry"
    assert payload["state"] == "CONNECTED"
    assert payload["verification_status"] == "VERIFIED"
    assert (REPO_ROOT / payload["contract"]).is_file()
    assert (REPO_ROOT / payload["test"]).is_file()
    assert (REPO_ROOT / payload["trace"]).is_file()

    loaded = load_records(REPO_ROOT, [payload])
    assert loaded[payload["seam"]]["state"] == "CONNECTED"
    assert loaded[payload["seam"]]["verification_status"] == "VERIFIED"
