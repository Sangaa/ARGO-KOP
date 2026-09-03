from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REP001 = ROOT / "Repository/REP-001_MASTER_INDEX.md"
REP002 = ROOT / "Repository/REP-002_REPOSITORY_MAP.md"
REP012 = ROOT / "Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md"
REP013 = ROOT / "Repository/REP-013_REPOSITORY_CONTENT_TREE.md"
REP014 = ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"
STATUS = ROOT / "Runtime/_FOLDER_STATUS.md"

RUNTIME_PATHS = (
    "RUN-011_COGNITIVE_LOOP_PROTOTYPE.md",
    "RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md",
    "RUN-013_CONTROLLED_HANDOFF.md",
    "RUN-014_LEARNING_PROMOTION_TEST.md",
    "RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md",
)


def test_gate14_named_runtime_inventory_agrees_across_control_plane():
    rep001 = REP001.read_text(encoding="utf-8")
    rep002 = REP002.read_text(encoding="utf-8")
    rep012 = REP012.read_text(encoding="utf-8")
    rep013 = REP013.read_text(encoding="utf-8")

    for index, filename in enumerate(RUNTIME_PATHS, start=11):
        assert f"Runtime/{filename}" in rep001
        assert f"Runtime/{filename}" in rep002
        assert filename in rep013
        assert f"| RUN-{index:03d} | Runtime | MAPPED | RE_READ / Integrity Hold |" in rep012


def test_gate14_named_relationship_cohort_is_complete():
    registry = REP014.read_text(encoding="utf-8")
    expected = {
        "REL-055": "| REL-055 | RUN-011 | ENG-013 | REFERENCES |",
        "REL-056": "| REL-056 | ENG-014 | RUN-011 | REFERENCES |",
        "REL-057": "| REL-057 | RUN-012 | RUN-011 | VALIDATES |",
        "REL-058": "| REL-058 | RUN-013 | RUN-011 | VALIDATES |",
        "REL-059": "| REL-059 | RUN-014 | RUN-011 | VALIDATES |",
        "REL-060": "| REL-060 | RUN-015 | RUN-011 | VALIDATES |",
    }
    for relationship_id, row_prefix in expected.items():
        assert registry.count(row_prefix) == 1, relationship_id


def test_gate14_bounded_result_preserves_independent_runtime_holds():
    status = STATUS.read_text(encoding="utf-8")
    assert "14. Runtime ↔ Repository control plane — BOUNDED VERIFIED FOR RUN-011..015 + REL-055..060 / BROADER CONTROL-PLANE HOLD" in status
    assert "12. Runtime ↔ Knowledge / Memory integration — OPEN / CONSOLIDATED VALIDATION REQUIRED" in status
    assert "13. Runtime ↔ Interfaces / external connectors — OPEN / IMPLEMENTATION VALIDATION REQUIRED" in status
    assert "EXECUTABLE PROMOTION HOLD" in status
    assert "🟡 VALIDATED / CROSS-LAYER INTEGRATION HOLD" in status
