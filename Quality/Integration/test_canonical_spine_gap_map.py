from canonical_spine_gap_map import SEAMS, build_gap_map, classify_candidate_path


def test_complete_evidence_has_no_gaps():
    evidence = {f"{a} -> {b}": "CONNECTED" for a, b in SEAMS}
    result = build_gap_map(evidence)
    assert result["status"] == "GAP_MAP_COMPLETE"
    assert result["seam_count"] == len(SEAMS)
    assert result["gap_count"] == 0
    assert result["candidate_kind_counts"] == {}


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
    assert result["candidate_kind_counts"] == {"implementation": 1, "documentation": 1}


def test_candidate_paths_must_be_repository_relative():
    evidence = {f"{a} -> {b}": "PARTIAL" for a, b in SEAMS}
    candidates = {f"{a} -> {b}": [] for a, b in SEAMS}
    candidates["Decision -> Authorization"] = ["../outside.md"]

    try:
        build_gap_map(evidence, candidates)
    except ValueError:
        return
    assert False, "candidate provenance must remain repository-relative"


def test_candidate_classification_is_path_based_and_non_promotional():
    assert classify_candidate_path("Runtime/pipeline.py") == "implementation"
    assert classify_candidate_path("Quality/Integration/test_pipeline.py") == "test"
    assert classify_candidate_path("Runtime/contracts/decision_contract.md") == "contract"
    assert classify_candidate_path("Runtime/EXECUTION_TRACE.json") == "trace"
    assert classify_candidate_path("docs/decision.md") == "documentation"


def test_candidate_classification_does_not_change_seam_state():
    evidence = {f"{a} -> {b}": "PARTIAL" for a, b in SEAMS}
    seam = "Decision -> Authorization"
    candidates = {f"{a} -> {b}": [] for a, b in SEAMS}
    candidates[seam] = ["Runtime/pipeline.py"]
    kinds = {f"{a} -> {b}": {} for a, b in SEAMS}
    kinds[seam] = {"Runtime/pipeline.py": classify_candidate_path("Runtime/pipeline.py")}

    result = build_gap_map(evidence, candidates, kinds)
    gap = next(item for item in result["gaps"] if item["seam"] == seam)
    assert gap["state"] == "PARTIAL"
    assert gap["candidate_kinds"]["Runtime/pipeline.py"] == "implementation"
