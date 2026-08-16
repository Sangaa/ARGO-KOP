from pathlib import Path


def test_learning_engine_requires_handoff_review_authorization_and_explicit_promotion():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Engine/ENG-007_LEARNING_ENGINE.md").read_text(encoding="utf-8")

    for required in (
        "5. Session Learning Handoff",
        "6. Parent ARGO + Responsible Engineer Review",
        "7. Authorization where required",
        "9. Optional explicit Promotion to broader scope",
        "Technical write access ≠ authorization.",
        "Session feedback ≠ automatic canonical knowledge.",
        "User memory ≠ platform memory.",
    ):
        assert required in text


def test_learning_engine_blocks_implicit_model_or_user_to_platform_promotion():
    root = Path(__file__).resolve().parents[2]
    text = (root / "Engine/ENG-007_LEARNING_ENGINE.md").read_text(encoding="utf-8")
    assert "A temporary model instance must never silently convert a user's experience into platform truth." in text
    assert "Do not merge User/Session/Project memory into Platform Canonical Memory implicitly." in text
    assert "Do not ingest a model report into canonical knowledge without review appropriate to its impact." in text
