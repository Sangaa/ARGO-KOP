"""Minimal governed retrieval for promoted knowledge records."""


def retrieve(records: list[dict], *, claim: str, scope: str | None = None) -> list[dict]:
    """Return promoted records whose tested pattern is relevant to the claim."""
    matches = []
    normalized = claim.lower()
    for record in records:
        if record.get("status") != "PROMOTED":
            continue
        if scope and record.get("knowledge_scope") != scope:
            continue
        pattern = str(record.get("pattern", "")).lower()
        if any(token in pattern for token in normalized.split() if len(token) > 2):
            matches.append(record)
    return matches
