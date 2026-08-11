"""Build a task context envelope from runtime state."""


def build_context(state: dict) -> dict:
    """Convert active runtime state into the bounded retrieval context."""
    required = ("task_id", "session_id", "project_id", "domain", "active_state", "claim", "allowed_scope")
    missing = [key for key in required if not state.get(key)]
    if missing:
        raise ValueError(f"runtime context incomplete: {', '.join(missing)}")

    return {key: state[key] for key in required}
