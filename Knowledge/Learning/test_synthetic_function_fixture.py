from synthetic_function_fixture import add


def test_expected_behavior():
    assert add(2, 3) == 5


def test_input_change_changes_result():
    assert add(4, 3) == 7


def test_negative_observation_is_detectable():
    assert add(2, 3) != 6
