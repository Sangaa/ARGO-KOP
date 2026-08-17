from check_mutation_matrix_preflight import evaluate


def test_protected_change_without_matrix_fails_condition():
    protected, matrices = evaluate(["Engine/ENG-TEST.md", "EJR/EJR-TEST.md"])
    assert protected == ["Engine/ENG-TEST.md"]
    assert matrices == []


def test_protected_change_with_matrix_passes_condition():
    protected, matrices = evaluate(
        ["Engine/ENG-TEST.md", "Repository/MUT-TEST_MUTATION_MATRIX.md"]
    )
    assert protected == ["Engine/ENG-TEST.md"]
    assert matrices == ["Repository/MUT-TEST_MUTATION_MATRIX.md"]


def test_documentation_only_is_exempt():
    protected, matrices = evaluate(["EJR/EJR-TEST.md", "Docs/TEST.md"])
    assert protected == []
    assert matrices == []


def test_matrix_only_is_exempt():
    protected, matrices = evaluate(["Repository/MUT-TEST_MUTATION_MATRIX.md"])
    assert protected == []
    assert matrices == ["Repository/MUT-TEST_MUTATION_MATRIX.md"]
