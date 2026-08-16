from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

ACTIVE_MODELS = [
    "Models/MOD-001_KNOWLEDGE_MODEL.md",
    "Models/MOD-002_ENTITY_MODEL.md",
    "Models/MOD-003_DOCUMENT_MODEL.md",
    "Models/MOD-004_MEMORY_MODEL.md",
    "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_verified_models_are_present_in_both_repository_indexes():
    master_index = _read("Repository/REP-001_MASTER_INDEX.md")
    repository_map = _read("Repository/REP-002_REPOSITORY_MAP.md")

    for model in ACTIVE_MODELS:
        assert model in master_index, f"Models artifact missing from REP-001: {model}"
        assert model in repository_map, f"Models artifact missing from REP-002: {model}"


def test_index_alignment_is_bounded_to_currently_verified_models():
    # The guard intentionally does not require historical unresolved model
    # declarations to be recreated or indexed as active canonical artifacts.
    assert ACTIVE_MODELS == [
        "Models/MOD-001_KNOWLEDGE_MODEL.md",
        "Models/MOD-002_ENTITY_MODEL.md",
        "Models/MOD-003_DOCUMENT_MODEL.md",
        "Models/MOD-004_MEMORY_MODEL.md",
        "Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md",
    ]
