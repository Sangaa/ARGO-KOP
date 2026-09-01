from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOV006 = ROOT / "Governance" / "GOV-006_NAMING_CONVENTION_STANDARD.md"


def test_gov006_core_parent_matches_current_repository_reality() -> None:
    text = GOV006.read_text(encoding="utf-8")

    current_row = "| **`CORE`** | Platform Identity & Constitution | `Core/` | `Core/CORE-003_CONSTITUTION.md` |"
    stale_authority_row = "| **`CORE`** | Platform Identity & Constitution | `Architecture/` | `Architecture/CORE-003_CONSTITUTION.md` |"

    assert current_row in text
    assert stale_authority_row not in text


def test_gov006_historical_reference_does_not_count_as_active_authority() -> None:
    text = GOV006.read_text(encoding="utf-8")

    assert "The prior `Architecture/CORE-003_CONSTITUTION.md` example was a stale historical naming example" in text


def test_gov006_factual_repair_does_not_promote_authority() -> None:
    text = GOV006.read_text(encoding="utf-8")

    assert "Version: 1.3.1" in text
    assert "Status: Proposed / Audit-Derived Update" in text
    assert "does **not** promote this document beyond its current `Proposed / Audit-Derived Update` status" in text
