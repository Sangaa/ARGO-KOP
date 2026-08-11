from traceable_reasoning import reason


def test_reasoning_preserves_categories_and_maps_evidence():
    classified = {
        "facts": ["shipment is pending"],
        "assumptions": ["customer may reply today"],
        "known_knowledge": ["K-001"],
        "unresolved_questions": ["connection confirmation"],
    }
    result = reason(classified)
    assert result["status"] == "REASONED"
    assert result["observations"]["facts"] == ["shipment is pending"]
    assert result["observations"]["assumptions"] == ["customer may reply today"]
    assert result["evidence_map"] == [
        {"type": "FACT", "claim": "shipment is pending", "basis": "context"},
        {"type": "KNOWLEDGE", "reference": "K-001", "basis": "promoted_record"},
    ]
    assert result["decision_status"] == "NOT_EVALUATED"
    assert result["execution_status"] == "NOT_REQUESTED"


def test_incomplete_classified_packet_fails_closed():
    result = reason({"facts": []})
    assert result["status"] == "HOLD"
