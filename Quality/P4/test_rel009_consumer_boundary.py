"""P4 REL-009 safety gate.

This is a boundary/protection test, not executable-consumer proof by itself.
It prevents accidental promotion of RUN-010 -> SRV-009 while the repository
contains only relationship description rather than a callable consumer path.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
RUN_010 = ROOT / "Runtime" / "RUN-010_RUNTIME_REFERENCE.md"


def test_rel009_is_not_promoted_without_callable_consumer_evidence() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    runtime_reference = RUN_010.read_text(encoding="utf-8")

    # The canonical registry must still contain REL-009 and its unresolved
    # evidence state. This is a protection gate, not positive runtime proof.
    assert "| REL-009 |" in registry
    assert "REVALIDATION REQUIRED" in registry

    # RUN-010 explicitly describes the chain as a relationship description
    # rather than a universal claim about runtime execution.
    assert "relationship description" in runtime_reference
    assert "does not claim that every runtime operation follows this exact path" in runtime_reference


def test_rel009_gate_files_are_current() -> None:
    assert REGISTRY.exists()
    assert RUN_010.exists()


# Keep the test intentionally side-effect free: it must never mutate the
# repository or manufacture runtime evidence for the unresolved relationship.
