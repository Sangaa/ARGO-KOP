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


def test_candidate_provenance_is_preserved_without_promoting_state():
    evidence = {f"{a} -> {b}": "MISSING" for a, b in SEAMS}
    candidates = {f"{a} -> {b}": [] for a, b in SEAMS}
    candidates["Decision -> Authorization"] = [
        "Decision/AUTHORIZATION_STATE_BOUNDARY.md",
        "Runtime/Execution/EVIDENCE_DECISION_CONTINUITY_CONTRACT.md",
    ]

    result = build_gap_map(evidence, candidates)
    gap = next(item for item in result["gaps"] if item["seam"] == "Decision -> Authorization")
    assert gap["state"] == "MISSING"
    assert gap["candidate_files"] == candidates["Decision -> Authorization"]


def test_candidate_kinds_are_preserved_without_promoting_state():
    evidence = {f"{a} -> {b}": "PARTIAL" for a, b in SEAMS}
    candidates = {f"{a} -> {b}": [] for a, b in SEAMS}
    kinds = {f"{a} -> {b}": {} for a, b in SEAMS}
    seam = "Decision -> Authorization"
    candidates[seam] = ["Runtime/pipeline.py", "docs/decision.md"]
    kinds[seam] = {"Runtime/pipeline.py": "implementation", "docs/decision.md": "documentation"}

    result = build_gap_map(evidence, candidates, kinds)
    gap = next(item for item in result["gaps"] if item["seam"] == seam)
    assert gap["state"] == "PARTIAL"
    assert gap["candidate_kinds"] == kinds[seam]


def test_candidate_paths_must_be_repository_relative():
    evidence = {f"{a} -> {b}": "PARTIAL" for a, b in SEAMS}
    candidates = {f"{a} -> {b}": [] for a, b in SEAMS}
    candidates["Decision -> Authorization"] = ["../outside.md"]

    try:
        build_gap_map(evidence, candidates)
    except ValueError:
        return
    assert False, "candidate provenance must remain repository-relative"
