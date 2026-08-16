from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _metadata(text: str, key: str):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().lower() == key.lower():
            for candidate in lines[index + 1 : index + 4]:
                if candidate.strip():
                    return candidate.strip()
        prefix = f"{key}:"
        if line.strip().lower().startswith(prefix.lower()):
            return line.split(":", 1)[1].strip()
    return None


def test_mem008_has_one_canonical_owner_and_one_retained_noncanonical_artifact():
    guided = (ROOT / "Memory/MEM-008_GUIDED_DISCOVERY_LEARNING_METHOD.md").read_text(encoding="utf-8")
    traceability = (ROOT / "Memory/MEM-008_MEMORY_TRACEABILITY.md").read_text(encoding="utf-8")

    assert _metadata(guided, "Canonical").lower() == "yes"
    assert _metadata(traceability, "Canonical").lower() == "no"

    assert "active canonical `MEM-008` owner is" in traceability
    assert "Memory/MEM-008_GUIDED_DISCOVERY_LEARNING_METHOD.md" in traceability
    assert "Noncanonical Retained Artifact" in traceability


def test_mem008_identity_reconciliation_does_not_silently_create_a_second_owner():
    canonical_candidates = []
    for path in (ROOT / "Memory").glob("MEM-008*.md"):
        text = path.read_text(encoding="utf-8")
        if _metadata(text, "Canonical").lower() == "yes":
            canonical_candidates.append(path.name)

    assert canonical_candidates == ["MEM-008_GUIDED_DISCOVERY_LEARNING_METHOD.md"]
