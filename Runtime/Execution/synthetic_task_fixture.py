"""Build a synthetic task through the experimental ARGO spine."""


def make_fixture() -> dict:
    return {
        "task": {"task_id": "SYN-TASK-001", "project_id": "ARGO-KOP", "claim": "shipment is pending"},
        "context": {
            "task_id": "SYN-TASK-001",
            "session_id": "SYN-SESSION-001",
            "project_id": "ARGO-KOP",
            "domain": "operations",
            "active_state": "pending",
            "claim": "shipment is pending",
            "allowed_scope": "synthetic_operations",
            "facts": ["shipment is pending"],
            "assumptions": [],
            "unresolved_questions": [],
        },
        "knowledge": [{
            "task_id": "SYN-K-001",
            "project_id": "ARGO-KOP",
            "status": "PROMOTED",
            "pattern": "pending shipment requires verified next-step review",
            "knowledge_scope": "synthetic_operations",
        }],
        "rules": ["VERIFY_BEFORE_ACTION"],
        "authorization": {"approved": True, "authorized_by": "synthetic-human", "authorization_id": "SYN-AUTH-001"},
    }
