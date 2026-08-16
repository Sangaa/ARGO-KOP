from pathlib import Path


def test_runtime_integration_dependencies_are_materialized():
    root = Path(__file__).resolve().parents[2]
    required = {
        "Runtime/RUN-010_RUNTIME_REFERENCE.md": [
            "Interfaces/INTF-010_INTEGRATIONS.md",
            "Interfaces/INTF-001_INTERFACE_SPEC.md",
            "Engine/ENG-006_EXECUTION_ENGINE.md",
            "Services/SRV-005_VALIDATION_SERVICE.md",
            "Services/SRV-009_UPDATE_SERVICE.md",
        ],
        "Interfaces/INTF-010_INTEGRATIONS.md": [
            "Architecture/ARC-007_INTEGRATION_MODEL.md",
            "Architecture/ARC-006_DEPENDENCY_MODEL.md",
        ],
        "Services/SRV-009_UPDATE_SERVICE.md": [
            "Engine/ENG-006_EXECUTION_ENGINE.md",
            "Services/SRV-005_VALIDATION_SERVICE.md",
            "Services/SRV-008_INDEX_SERVICE.md",
        ],
    }
    for source, targets in required.items():
        source_path = root / source
        assert source_path.is_file(), source
        text = source_path.read_text(encoding="utf-8")
        for target in targets:
            target_path = root / target
            assert target_path.is_file(), (source, target)
            assert target_path.name in text, (source, target)


def test_interface_and_update_service_preserve_authority_boundaries():
    root = Path(__file__).resolve().parents[2]
    interface = (root / "Interfaces/INTF-010_INTEGRATIONS.md").read_text(encoding="utf-8")
    service = (root / "Services/SRV-009_UPDATE_SERVICE.md").read_text(encoding="utf-8")
    assert "A connector is an **integration mechanism**, not a new cognitive authority." in interface
    assert "Technical write completion is not equivalent to governed acceptance" in service
