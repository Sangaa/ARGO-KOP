from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN015 = ROOT / "Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md"
RUN011 = ROOT / "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md"
WORKFLOW = ROOT / ".github/workflows/runtime-prototype-tests.yml"
REGISTRY = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"


def test_runtime_workflow_executes_the_run011_prototype_boundary():
    contract = RUN015.read_text(encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert RUN011.is_file()
    assert "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md" in contract
    assert "- 'Runtime/Prototype/**'" in workflow
    assert "working-directory: Runtime/Prototype" in workflow
    assert "run: python -m pytest -q" in workflow
    assert "run: python run_acceptance_scenarios.py" in workflow
    assert "run: python -m pytest -q Quality/Integration" in workflow
    assert "working-directory: Quality/Integrity" in workflow


def test_rel060_registry_is_exact_and_scope_limited():
    registry = REGISTRY.read_text(encoding="utf-8")
    contract = RUN015.read_text(encoding="utf-8")
    assert registry.count(
        "| REL-060 | RUN-015 | RUN-011 | VALIDATES | "
        "**WORKFLOW-BOUND ACCEPTANCE / EXACT-HEAD-REVALIDATED / SCOPE-LIMITED** |"
    ) == 1
    for stronger_type in ("DEPENDS_ON", "CONSUMES", "IMPLEMENTS", "GOVERNS"):
        assert f"| REL-060 | RUN-015 | RUN-011 | {stronger_type} |" not in registry
    assert "CI EVIDENCE AVAILABLE != FULL RUNTIME CERTIFICATION" in contract
    assert "PROTOTYPE TEST PASS != CANDIDATE AUTHORITY PROMOTION" in contract
    assert "This is **not** a complete graph." in registry
