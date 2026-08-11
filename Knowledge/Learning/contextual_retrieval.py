"""Context-bounded retrieval prototype."""


def retrieve_in_context(records: list[dict], context: dict) -> list[dict]:
    """Retrieve promoted records matching claim, project and allowed scope."""
    claim = str(context.get("claim", "")).lower()
    project_id = context.get("project_id")
    allowed_scope = context.get("allowed_scope")
    if not claim or not project_id or not allowed_scope:
        return []

    matches = []
    for record in records:
        if record.get("status") != "PROMOTED":
            continue
        if record.get("project_id") != project_id:
            continue
        if record.get("knowledge_scope") != allowed_scope:
            continue
        pattern = str(record.get("pattern", "")).lower()
        if any(token in pattern for token in claim.split() if len(token) > 2):
            matches.append(record)
    return matches
