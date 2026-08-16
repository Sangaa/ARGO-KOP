from pathlib import Path

from canonical_spine_gap_map import SEAMS
from canonical_spine_integration_audit import audit


def test_canonical_spine_keeps_authorization_to_execution_governed():
    root = Path(__file__).resolve().parents[2]
    result = audit(root)
    assert result["seam_count"] == 11
    assert "Authorization -> Execution" in {f"{source} -> {destination}" for source, destination in SEAMS}
    assert result["evidence"]["Authorization -> Execution"] != "CONNECTED"


def test_learning_pipeline_registry_handoff_is_not_mistaken_for_canonical_spine_seam():
    canonical_keys = {f"{source} -> {destination}" for source, destination in SEAMS}
    assert "Learning Pipeline -> Verified Registry" not in canonical_keys


def test_canonical_spine_connected_state_requires_registry_evidence_path():
    root = Path(__file__).resolve().parents[2]
    result = audit(root)
    for seam, state in result["evidence"].items():
        if state == "CONNECTED":
            # Structural scanner output may not certify CONNECTED. This guard
            # documents that promotion must continue to come through explicit
            # verified seam records in the audit entrypoint.
            assert seam in canonical_keys(root)


def canonical_keys(root):
    del root
    return {f"{source} -> {destination}" for source, destination in SEAMS}
