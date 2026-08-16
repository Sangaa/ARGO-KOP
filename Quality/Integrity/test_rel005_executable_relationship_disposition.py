from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DISPOSITION = ROOT / "Repository/REP-020_RELATIONSHIP_DISPOSITION_2026-08-16_P259.md"
PROBE = ROOT / "Quality/Integration/ENG006_SRV009_EXECUTABLE_CONSUMER_PROBE.md"
REP014 = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def test_rel005_has_current_revalidation_disposition():
    text = DISPOSITION.read_text(encoding="utf-8")
    assert "REL-005 = REVALIDATION REQUIRED" in text
    assert "DOCUMENTED / CONTRACTUAL" in text
    assert "does not provide a callable `SRV-009` consumer implementation" in text


def test_rel005_executable_proof_requires_existing_probe_and_registry_revalidation():
    disposition = DISPOSITION.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")
    registry = REP014.read_text(encoding="utf-8")
    assert "ENG-006" in probe and "SRV-009" in probe
    assert "Revalidation Required" in disposition
    assert "REL-005" in registry
    assert "IMPLEMENTS" in registry


def test_guard_does_not_promote_absent_implementation():
    text = DISPOSITION.read_text(encoding="utf-8")
    assert "must not be treated as executable `IMPLEMENTS` evidence" in text
    assert "Directly reconcile `REL-005` inside `REP-014`" in text
