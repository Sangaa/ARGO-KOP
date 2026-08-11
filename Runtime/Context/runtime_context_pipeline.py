"""Small pipeline joining runtime state, contextual retrieval and learning correction."""

from contextual_retrieval import retrieve_in_context
from knowledge_correction import assess_contradiction
from runtime_task_context import build_context


def prepare_task(state: dict, records: list[dict]) -> dict:
    context = build_context(state)
    knowledge = retrieve_in_context(records, context)
    return {"context": context, "knowledge": knowledge}


def evaluate_new_evidence(record: dict, evidence: list[str], *, contradiction: bool) -> dict:
    return assess_contradiction(record, evidence=evidence, contradiction=contradiction)
