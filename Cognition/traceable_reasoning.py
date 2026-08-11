"""First traceable reasoning pass over a classified cognition packet."""


def reason(classified: dict) -> dict:
    required = ("facts", "assumptions", "known_knowledge", "unresolved_questions")
    missing = [key for key in required if key not in classified]
    if missing:
        return {"status": "HOLD", "reason": "CLASSIFIED_PACKET_INCOMPLETE", "missing": missing}

    evidence = []
    for fact in classified["facts"]:
        evidence.append({"type": "FACT", "claim": fact, "basis": "context"})
    for knowledge_id in classified["known_knowledge"]:
        evidence.append({"type": "KNOWLEDGE", "reference": knowledge_id, "basis": "promoted_record"})

    return {
        "status": "REASONED",
        "observations": {
            "facts": classified["facts"],
            "assumptions": classified["assumptions"],
            "known_knowledge": classified["known_knowledge"],
            "unresolved_questions": classified["unresolved_questions"],
        },
        "evidence_map": evidence,
        "decision_status": "NOT_EVALUATED",
        "execution_status": "NOT_REQUESTED",
    }
