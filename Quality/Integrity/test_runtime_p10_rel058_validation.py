import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
RUN013 = ROOT / "Runtime/RUN-013_CONTROLLED_HANDOFF.md"
HANDOFF = ROOT / "Runtime/Prototype/CONTROLLED_HANDOFF.md"
HARNESS_PATH = ROOT / "Runtime/Prototype/cognitive_loop_harness.py"
GATE_PATH = ROOT / "Runtime/Prototype/controlled_execution_gate.py"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _payload():
    return {
        "task_id": "REL-058-GATE",
        "session_id": "P10-C",
        "active_state": "ready_for_proposal",
        "evidence": ["source:rel058"],
        "knowledge": ["rule:controlled-handoff"],
        "requested_outcome": "prepare safe proposal",
    }


def test_rel058_has_direct_contract_and_implementation_evidence():
    registry = REGISTRY.read_text(encoding="utf-8")
    run013 = RUN013.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")

    assert "Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md" in run013
    assert "controlled_execution_gate.py" in handoff
    assert registry.count(
        "| REL-058 | RUN-013 | RUN-011 | VALIDATES | "
        "**CONTROLLED-HANDOFF TRACE GATE / EXECUTABLE-TESTED / "
        "SIDE-EFFECT-FREE / NON-AUTHORITY** |"
    ) == 1


def test_rel058_gate_validates_run011_trace_without_execution():
    harness = _load("rel058_harness", HARNESS_PATH)
    gate = _load("rel058_gate", GATE_PATH)

    ready_trace = harness.run(_payload(), human_approved=True)
    ready = gate.evaluate(ready_trace)
    assert ready == {"status": "READY_FOR_CONTROLLED_HANDOFF", "side_effects": False}
    assert ready_trace["result"] == {"executed": False, "external_side_effect": False}

    unauthorized = gate.evaluate(harness.run(_payload(), human_approved=False))
    assert unauthorized == {"status": "HOLD", "reason": "AUTHORIZATION_MISSING"}

    incomplete = gate.evaluate({"task_id": "REL-058-INCOMPLETE"})
    assert incomplete["status"] == "HOLD"
    assert incomplete["reason"] == "TRACE_INCOMPLETE"


def test_rel058_is_not_promoted_beyond_bounded_validation():
    registry = REGISTRY.read_text(encoding="utf-8")
    for stronger_type in ("DEPENDS_ON", "CONSUMES", "IMPLEMENTS", "GOVERNS"):
        assert f"| REL-058 | RUN-013 | RUN-011 | {stronger_type} |" not in registry

    assert "This is **not** a complete graph." in registry
