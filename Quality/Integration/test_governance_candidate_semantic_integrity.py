from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_governance_candidate_semantic_authority_boundaries():
    version_text = (ROOT / "Release" / "VERSION.md").read_text(encoding="utf-8")
    gov012 = (ROOT / "Governance" / "GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md").read_text(encoding="utf-8")
    celm = (ROOT / "Governance" / "CELM-001_CONNECTOR_ENVIRONMENTAL_LEARNING_MODEL.md").read_text(encoding="utf-8")
    gov017_compat = (ROOT / "Governance" / "GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md").read_text(encoding="utf-8")
    gov025 = (ROOT / "Governance" / "GOV-025_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md").read_text(encoding="utf-8")

    assert "Current Development Baseline\n\n3.2.1" in version_text
    assert "Development Baseline: 3.2.1" in gov012
    assert "Development Baseline: 3.3.0" not in gov012

    assert "NON-CANONICAL COMPATIBILITY RECORD" in gov017_compat
    assert "GOV-025" in celm
    assert "GOV-025" in gov025
    assert "PROPOSED" in gov025.upper()
    assert "GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md` governs the active training program" not in celm
    assert "candidate" in celm.lower()


def test_candidate_review_does_not_promote_candidate_governance():
    candidates = [
        "GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md",
        "GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md",
        "GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md",
        "GOV-023_HERMUZ_CONTROLLED_DIAGNOSTIC_EXPERIMENT_PROTOCOL.md",
        "GOV-024_HERMUZ_SOLUTION_SIMULATION_AND_EFFECT_ANALYSIS_PROTOCOL.md",
        "GOV-025_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md",
        "GOV-026_HERMUZ_SOLUTION_EVOLUTION_AND_STABILITY_PROTOCOL.md",
    ]
    for name in candidates:
        text = (ROOT / "Governance" / name).read_text(encoding="utf-8").upper()
        assert ("PROPOSED" in text or "CANDIDATE" in text)
        assert "CANONICAL: YES" not in text
