from Runtime.Prototype.multi_channel_m1_harness import run_m1


def test_m1_two_channels_are_isolated_and_read_only():
    report = run_m1()
    assert report["mode"] == "M1_ONE_USER_MULTI_TASK_READ_ONLY"
    assert report["canonical_mutation"] is False
    assert [r["status"] for r in report["results"]] == ["SUCCESS", "SUCCESS"]
    assert [c["channel_id"] for c in report["contexts"]] == ["CHANNEL-A", "CHANNEL-B"]
    assert report["contexts"][0]["state"]["observed_topic"] == "alpha"
    assert report["contexts"][1]["state"]["observed_topic"] == "beta"
    assert report["contexts"][0]["state"] is not report["contexts"][1]["state"]


def test_m1_failure_is_contained_to_one_channel():
    report = run_m1(fail_task="TASK-001")
    assert [r["status"] for r in report["results"]] == ["FAILED", "SUCCESS"]
    assert report["contexts"][0]["state"] == {"observed_topic": "alpha"}
    assert report["contexts"][1]["state"] == {"observed_topic": "beta"}
    assert report["traces"][0][-1]["event"] == "FAIL"
    assert report["traces"][1][-1]["event"] == "COMPLETE"


def test_m1_trace_identity_is_channel_specific():
    report = run_m1()
    for trace in report["traces"]:
        assert trace
        ids = {(event["task_id"], event["channel_id"]) for event in trace}
        assert len(ids) == 1
