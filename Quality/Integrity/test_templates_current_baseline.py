from pathlib import Path


def test_templates_readme_matches_current_development_baseline():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Templates/README.md").read_text(encoding="utf-8")
    assert "Development Baseline: 3.2.1" in text
    assert "Development Baseline: 3.3.0" not in text
    assert "Last Audit: 2026-08-16" in text
