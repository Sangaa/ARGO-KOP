from pathlib import Path


def test_architecture_map_uses_authoritative_development_baseline():
    root = Path(__file__).resolve().parents[2]
    release = (root / "Release" / "VERSION.md").read_text(encoding="utf-8")
    architecture = (root / "Architecture" / "ARC_MAP.md").read_text(encoding="utf-8")

    marker = "Current Development Baseline"
    release_baseline = release.split(marker, 1)[1].split("\n", 2)[0].strip()
    assert f"Repository Development Baseline\n{release_baseline}" in architecture
    assert "Latest Official Release\n1.0.0" in architecture
