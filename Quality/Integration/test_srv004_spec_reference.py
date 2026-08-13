from pathlib import Path


def test_srv004_uses_existing_spec001_knowledge_organization_artifact():
    root = Path(__file__).resolve().parents[2]
    service = (root / "Services" / "SRV-004_KNOWLEDGE_SERVICE.md").read_text(encoding="utf-8")
    spec = root / "Specifications" / "01-Knowledge-Organization.md"
    content = spec.read_text(encoding="utf-8")

    assert spec.is_file()
    assert "SPEC-001-KNOWLEDGE-ORGANIZATION" in content
    assert "Specifications/01-Knowledge-Organization.md" in service
    assert "SPEC-001-KNOWLEDGE-ORGANIZATION (`Specifications/01-Knowledge-Organization.md`)" in service
    assert "SPEC-001_KNOWLEDGE_SPECIFICATION.md" not in service
