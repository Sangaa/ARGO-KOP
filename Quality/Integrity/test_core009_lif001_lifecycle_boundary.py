from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CORE009 = ROOT / "Core/CORE-009_PLATFORM_LIFECYCLE.md"
LIF001 = ROOT / "Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md"
REL = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
CORE_STATUS = ROOT / "Core/_FOLDER_STATUS.md"
LIF_STATUS = ROOT / "Lifecycle/_FOLDER_STATUS.md"


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


def test_core009_uses_current_document_lifecycle_identity_and_path() -> None:
    text = CORE009.read_text(encoding="utf-8", errors="ignore")
    assert "`LIF-001` — document lifecycle." in text
    assert "`Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`" in text
    assert "`GOV-005` — document lifecycle." not in text
    assert "`Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md`" not in text


def test_lif001_preserves_document_scope_and_explicit_core009_interaction() -> None:
    text = LIF001.read_text(encoding="utf-8", errors="ignore")
    assert "Document ID\n\nLIF-001" in text
    assert "Canonical\n\nYes" in text
    assert "`Core/CORE-009_PLATFORM_LIFECYCLE.md`" in text
    assert "This lifecycle is **document-scoped**" in text
    assert "The historical path is retired after migration" in text


def test_relationship_registry_records_only_documentary_lifecycle_seam() -> None:
    rows = _relationship_rows(REL.read_text(encoding="utf-8", errors="ignore"))
    assert [
        "REL-063",
        "CORE-009",
        "LIF-001",
        "REFERENCES",
        "**DOCUMENT-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY**",
    ] in rows
    assert [
        "REL-064",
        "LIF-001",
        "CORE-009",
        "REFERENCES",
        "**PLATFORM-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY**",
    ] in rows

    forbidden = {"DEPENDS_ON", "GOVERNS", "IMPLEMENTS", "CONSUMES"}
    seam_rows = [row for row in rows if {row[1], row[2]} == {"CORE-009", "LIF-001"}]
    assert seam_rows
    assert all(row[3] not in forbidden for row in seam_rows)


def test_core_closure_does_not_close_lifecycle_partition() -> None:
    core_status = CORE_STATUS.read_text(encoding="utf-8", errors="ignore")
    lifecycle_status = LIF_STATUS.read_text(encoding="utf-8", errors="ignore")
    assert "BOUNDED CROSS-LAYER VALIDATION CLOSED FOR CORE CERTIFICATION SCOPE" in core_status
    assert "CORE = CLOSED_FOR_PHASE_1 / BOUNDED CORE PARTITION CERTIFIED" in core_status
    assert "Consolidated Lifecycle certification: **OPEN / INTEGRITY HOLD**" in lifecycle_status
    assert "No `PASS` claim is made until cross-domain references are validated" in lifecycle_status
