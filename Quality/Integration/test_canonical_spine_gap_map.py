from canonical_spine_gap_map import SEAMS, build_gap_map


def test_complete_evidence_has_no_gaps():
    evidence = {f"{a} -> {b}": "CONNECTED" for a, b in SEAMS}
    result = build_gap_map(evidence)
    assert result["status"] == "GAP_MAP_COMPLETE"
    assert result["seam_count"] == len(SEAMS)
    assert result["gap_count"] == 0


def test_missing_seam_is_explicitly_reported():
    evidence = {f"{a} -> {b}": "CONNECTED" for a, b in SEAMS}
    evidence["Reasoning -> Decision"] = "PARTIAL"
    result = build_gap_map(evidence)
    assert result["gap_count"] == 1
    assert result["gaps"][0]["seam"] == "Reasoning -> Decision"
    assert result["gaps"][0]["state"] == "PARTIAL"


def test_invalid_state_is_rejected():
    try:
        build_gap_map({f"{a} -> {b}": "UNKNOWN" for a, b in SEAMS})
    except ValueError:
        return
    assert False, "invalid seam state must be rejected"
