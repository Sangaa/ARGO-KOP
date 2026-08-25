from Quality.Integrity.fixtures.intf006_synthetic_seam import build_synthetic_observation


def test_intf006_synthetic_seam_is_explicitly_non_production():
    observation = build_synthetic_observation()
    assert observation.synthetic is True
    assert observation.source_id == "TEST-SYNTHETIC-INTF006"
    assert observation.values["test_signal"] == "synthetic"


def test_intf006_synthetic_seam_is_side_effect_free():
    observation = build_synthetic_observation(values={"temperature": 25})
    assert dict(observation.values) == {"temperature": 25}
