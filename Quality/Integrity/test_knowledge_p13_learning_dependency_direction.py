from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parents[2]
LEARNING = ROOT / "Knowledge" / "Learning"
ADAPTER = LEARNING / "promotion_gate_adapter.py"
RUNTIME_PIPELINE = ROOT / "Runtime" / "Context" / "runtime_context_pipeline.py"
ARC006 = ROOT / "Architecture" / "ARC-006_DEPENDENCY_MODEL.md"
AUDIT = ROOT / "Repository" / "P13_KNOWLEDGE_LEARNING_EXECUTABLE_SEAM_AUDIT_2026-09-05_I.tsv"


def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module)
    return imports


def test_non_test_learning_executables_do_not_import_runtime_upward() -> None:
    offenders = {}
    for path in sorted(LEARNING.glob("*.py")):
        if path.name.startswith("test_"):
            continue
        runtime_imports = sorted(name for name in _imports(path) if name == "Runtime" or name.startswith("Runtime."))
        if runtime_imports:
            offenders[path.name] = runtime_imports
    assert offenders == {}


def test_promotion_adapter_is_candidate_mapping_not_runtime_gate_owner() -> None:
    text = ADAPTER.read_text(encoding="utf-8")
    assert "def build_candidate(" in text
    assert "def evaluate_evidence(" not in text
    assert "Runtime.Prototype.learning_promotion_gate" not in text
    assert "Promotion-gate evaluation is" in text


def test_runtime_context_pipeline_consumes_knowledge_downward_without_authority_transfer() -> None:
    text = RUNTIME_PIPELINE.read_text(encoding="utf-8")
    assert "from contextual_retrieval import retrieve_in_context" in text
    assert "from knowledge_correction import assess_contradiction" in text
    assert "return assess_contradiction(" in text


def test_architecture_contract_prohibits_unapproved_reverse_dependency() -> None:
    arc = ARC006.read_text(encoding="utf-8")
    assert "Dependencies must not reverse this direction unless explicitly authorized by a governed architectural decision." in arc
    assert "## Knowledge / Specifications / Standards" in arc
    assert "May depend on: Repository, Architecture and applicable Governance rules." in arc
    assert "Validation failure blocks acceptance until corrected or explicitly dispositioned" in arc


def test_unit15_audit_preserves_nonpromotion_dispositions() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    assert "DIRECT_REVERSE_IMPORT\tKNOWLEDGE_DEPENDS_UPWARD_ON_RUNTIME_WITHOUT_GOVERNED_EXCEPTION\tREPAIR_REQUIRED_NOT_REGISTRY_ADMISSION" in audit
    assert "DIRECT_RUNTIME_IMPORT_AND_CALL_PLUS_P10_BOUNDARY_EVIDENCE\tRUNTIME_CONSUMES_KNOWLEDGE_CORRECTION_FAIL_CLOSED\tALREADY_GOVERNED_P10_SEAM_NO_DUPLICATE_REL_INFERENCE" in audit
    assert "TEST_CONSUMER\tSYNTHETIC_FIXTURE_ONLY\tNO_CANONICAL_RUNTIME_EDGE" in audit
