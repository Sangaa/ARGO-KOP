from reasoning_packet_classifier import classify


def test_classifier_separates_context_categories():
    packet = {
        "context": {
            "facts": ["shipment is pending"],
            "assumptions": ["customer may reply today"],
            "unresolved_questions": ["connection vessel confirmation"],
        },
        "knowledge": [{"task_id": "K-001"}],
    }
    result = classify(packet)
    assert result["status"] == "READY_FOR_REASONING"
    assert result["facts"] == ["shipment is pending"]
    assert result["assumptions"] == ["customer may reply today"]
    assert result["known_knowledge"] == ["K-001"]
    assert result["decision_status"] == "NOT_EVALUATED"
    assert result["execution_status"] == "NOT_REQUESTED"


def test_incomplete_packet_holds():
    result = classify({"context": {}})
    assert result["status"] == "HOLD"
