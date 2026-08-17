"""P4 REL-009 safety gate.

This is a boundary/protection test, not executable-consumer proof by itself.
It prevents accidental promotion of RUN-010 -> SRV-009 while the repository
contains only relationship description rather than a callable consumer path.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
RUN_010 = ROOT / "Runtime" / "RUN-010_RUNTIME_REFERENCE.md"


def test_rel009_is_not_promoted_without_callable_consumer_evidence() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    runtime_reference = RUN_010.read_text(encoding="utf-8")

    # Verify the canonical table row structurally instead of relying on a
    # broad substring split that can be confused by later evidence sections.
    match = re.search(
        r"^\|\s*REL-009\s*\|[^\n]*\|\s*CONSUMES\s*\|\s*([^|\n]+?)\s*\|\s*$",
        registry,
        flags=re.MULTILINE,
    )
    assert match is not None, "REL-009 canonical registry row not found"
    state = match.group(1).replace("**", "").strip()
    assert state == "REVALIDATION REQUIRED"

    # RUN-010 describes the path architecturally and explicitly limits that
    # description; wording is checked in two stable fragments.
    assert "relationship description" in runtime_reference
    assert "does not claim that every runtime operation follows this exact path" in runtime_reference


def test_rel009_gate_files_are_current() -> None:
    assert REGISTRY.exists()
    assert RUN_010.exists()


# Keep the test intentionally side-effect free: it must never mutate the
# repository or manufacture runtime evidence for the unresolved relationship.
