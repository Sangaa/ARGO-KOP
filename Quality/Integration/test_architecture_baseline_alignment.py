from pathlib import Path
import re


def _development_baseline(text: str) -> str:
    match = re.search(r"Current Development Baseline\s+([0-9]+\.[0-9]+\.[0-9]+)", text)
    assert match
    return match.group(1)


def test_architecture_map_uses_authoritative_development_baseline():
    root = Path(__file__).resolve().parents[2]
    release = (root / "Release" / "VERSION.md").read_text(encoding="utf-8")
    architecture = (root / "Architecture" / "ARC_MAP.md").read_text(encoding="utf-8")

    release_baseline = _development_baseline(release)
    assert f"Repository Development Baseline\n{release_baseline}" in architecture
    assert "Latest Official Release\n1.0.0" in architecture
