from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
REP013 = ROOT / "Repository" / "REP-013_REPOSITORY_CONTENT_TREE.md"
CORE = ROOT / "Core"


def _rep013_core_members(text: str) -> list[str]:
    match = re.search(r"### Core/\n\n```text\nCore/\n(?P<body>.*?)\n```", text, re.S)
    assert match, "REP-013 Core inventory block not found"
    members = []
    for line in match.group("body").splitlines():
        m = re.match(r"[├└]── (.+)$", line)
        if m:
            members.append(m.group(1))
    return members


def test_rep013_core_inventory_matches_exact_top_level_core_files():
    physical = sorted(p.name for p in CORE.iterdir() if p.is_file())
    recorded = sorted(_rep013_core_members(REP013.read_text(encoding="utf-8")))
    assert recorded == physical


def test_rep013_preserves_legacy_core000_identity_as_physical_not_canonical():
    text = REP013.read_text(encoding="utf-8")
    assert "CORE-000_PLATFORM_IDENTITY.md" in _rep013_core_members(text)
    assert "Canonical: No / Legacy / Superseded" in text
    assert "listing it here does not promote it" in text


def test_rep013_p337_boundary_keeps_remaining_core_control_plane_open():
    text = REP013.read_text(encoding="utf-8")
    assert "REP-001 and REP-002 Core reconciliation remains open" in text
    assert "no Priority-7, Phase-1, Connected-Baseline or global integrity closure is claimed" in text
