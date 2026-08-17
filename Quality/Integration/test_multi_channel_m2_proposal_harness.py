from Runtime.Prototype.multi_channel_m2_proposal_harness import run_m2


def test_m2_isolates_proposal_workspaces_and_forbids_canonical_mutation():
    result = run_m2()
    assert result["canonical_mutation"] is False
    assert len(result["proposal_workspaces"]) == 2
    assert result["proposal_workspaces"][0]["channel_id"] != result["proposal_workspaces"][1]["channel_id"]
    assert result["proposal_workspaces"][0]["proposal"] != result["proposal_workspaces"][1]["proposal"]
    assert all(any(e["event"] == "READ_BACK" for e in trace) for trace in result["traces"])


def test_m2_detects_overlap_without_merging_it():
    result = run_m2(collide=True)
    assert result["canonical_mutation"] is False
    assert result["conflicts"] == [{"type": "SHARED_TARGET_OVERLAP", "task_ids": ["TASK-001", "TASK-002"]}]
