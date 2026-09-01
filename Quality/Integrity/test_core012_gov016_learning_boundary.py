from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CORE012 = ROOT / "Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md"
GOV016 = ROOT / "Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md"
REL = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE_STATUS = ROOT / "Core/_FOLDER_STATUS.md"


def _relationship_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("| REL-"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) == 5:
            rows.append(parts)
    return rows


def test_core012_explicitly_references_gov016_failure_learning_protocol() -> None:
    core = CORE012.read_text(encoding="utf-8", errors="ignore")
    assert "This rule works together with `GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`." in core
    assert "Failure → Root Cause → Corrective Pattern → Regression → Reuse" in core


def test_gov016_is_current_mandatory_failure_learning_target_without_reverse_core012_claim() -> None:
    gov = GOV016.read_text(encoding="utf-8", errors="ignore")
    assert "# GOV-016 — Failure-to-Learning Protocol" in gov
    assert "**Status:** ACTIVE / MANDATORY" in gov
    assert "Failure → Evidence → Root Cause → Failure Class" in gov
    assert "CORE-012" not in gov


def test_registry_records_one_way_reference_only() -> None:
    rows = _relationship_rows(REL.read_text(encoding="utf-8", errors="ignore"))
    assert [
        "REL-065",
        "CORE-012",
        "GOV-016",
        "REFERENCES",
        "**INTENTIONAL ONE-WAY / FAILURE-LEARNING-ALIGNED / NON-DEPENDENCY**",
    ] in rows

    seam_rows = [row for row in rows if {row[1], row[2]} == {"CORE-012", "GOV-016"}]
    assert seam_rows == [[
        "REL-065",
        "CORE-012",
        "GOV-016",
        "REFERENCES",
        "**INTENTIONAL ONE-WAY / FAILURE-LEARNING-ALIGNED / NON-DEPENDENCY**",
    ]]


def test_core_priority7_closure_is_bounded_not_global() -> None:
    status = CORE_STATUS.read_text(encoding="utf-8", errors="ignore")
    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in status
    assert "CORE = CLOSED_FOR_PHASE_1 / BOUNDED CORE PARTITION CERTIFIED" in status
    assert "Folder Certification\n\n🟢 CLOSED_FOR_PHASE_1" in status
    assert "Global integrity HOLD" in status
