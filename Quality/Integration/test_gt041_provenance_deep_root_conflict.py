"""GT-041 regression: a deep explicit root conflict invalidates the whole provenance graph."""
from test_evidence_reasoning_classification import EvidenceObservation, classify, provenance_graph_state


def test_gt041_deep_child_root_conflict_invalidates_graph():
    common = dict(
        claim_id="run-status",
        claim_type="EXECUTION",
        proposition="run completed successfully",
        target_id="run:current",
        scope="repository",
        temporal_context="2026-08-24",
        authority_scope="FACTUAL",
        claim_fitness="DIRECT",
        identity_confidence="HIGH",
        evidence_independence="INDEPENDENT",
        completeness="COMPLETE",
        observed_value="SUCCESS",
        semantic_status="OBSERVED",
    )
    root = EvidenceObservation(
        evidence_id="ROOT-A",
        source_ref="root-source",
        evidence_layer="RUN_METADATA",
        provenance_root="ROOT-A",
        **common,
    )
    parent = EvidenceObservation(
        evidence_id="PARENT",
        source_ref="parent-source",
        evidence_layer="ARTIFACT",
        provenance_root="ROOT-A",
        provenance_parent="ROOT-A",
        **common,
    )
    child = EvidenceObservation(
        evidence_id="CHILD",
        source_ref="child-source",
        evidence_layer="REPORT",
        provenance_root="ROOT-B",
        provenance_parent="PARENT",
        **common,
    )
    root_b = EvidenceObservation(
        evidence_id="ROOT-B",
        source_ref="alternate-root-source",
        evidence_layer="RUN_METADATA",
        provenance_root="ROOT-B",
        **common,
    )
    observations = {x.evidence_id: x for x in (root, parent, child, root_b)}

    assert provenance_graph_state(observations) == "INVALID PROVENANCE"
    assert classify(parent, child, observations) == "UNRESOLVED"


def test_gt041_deep_root_conflict_is_not_a_claim_contradiction():
    common = dict(
        claim_id="run-status",
        claim_type="EXECUTION",
        proposition="run completed successfully",
        target_id="run:current",
        scope="repository",
        temporal_context="2026-08-24",
        authority_scope="FACTUAL",
        claim_fitness="DIRECT",
        identity_confidence="HIGH",
        evidence_independence="INDEPENDENT",
        completeness="COMPLETE",
        observed_value="SUCCESS",
        semantic_status="OBSERVED",
    )
    root_a = EvidenceObservation(evidence_id="ROOT-A", source_ref="A", evidence_layer="RUN_METADATA", provenance_root="ROOT-A", **common)
    parent = EvidenceObservation(evidence_id="PARENT", source_ref="P", evidence_layer="ARTIFACT", provenance_root="ROOT-A", provenance_parent="ROOT-A", **common)
    child = EvidenceObservation(evidence_id="CHILD", source_ref="C", evidence_layer="REPORT", provenance_root="ROOT-B", provenance_parent="PARENT", **common)
    root_b = EvidenceObservation(evidence_id="ROOT-B", source_ref="B", evidence_layer="RUN_METADATA", provenance_root="ROOT-B", **common)
    observations = {x.evidence_id: x for x in (root_a, parent, child, root_b)}

    assert classify(parent, child, observations) == "UNRESOLVED"
