from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github" / "workflows" / "real-matrix-regression.yml"


def test_real_matrix_workflow_covers_primary_and_corrective_matrix_names():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "Repository/*MUTATION_MATRIX*.md" in text
    assert "Repository/*CORRECTIVE_MATRIX*.md" in text
    assert "Quality/Integration/run_real_matrix_regression.py" in text
    assert "Quality/Integration/check_mutation_matrix_semantics.py" in text
    assert "python Quality/Integration/run_real_matrix_regression.py" in text


def test_corrective_matrix_trigger_is_additive_not_replacement():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert text.count("Repository/*MUTATION_MATRIX*.md") == 1
    assert text.count("Repository/*CORRECTIVE_MATRIX*.md") == 1
    assert ".github/workflows/real-matrix-regression.yml" in text
