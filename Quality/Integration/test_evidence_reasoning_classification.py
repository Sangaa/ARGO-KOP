"""Controlled runtime proof for ARGO evidence reasoning classification."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class EvidenceObservation:
    evidence_id: str
    claim_id: str
    claim_type: str
    proposition: str
    target_id: str
    scope: str
    temporal_context: str
    evidence_layer: str
    source_ref: str
    authority_scope: str
    claim_fitness: str
    identity_confidence: str
    evidence_independence: str
    completeness: str
    observed_value: str
    semantic_status: str = "OBSERVED"
    execution_identity: Optional[str] = None
    target_commit: Optional[str] = None
    provenance_root: Optional[str] = None
    provenance_parent: Optional[str] = None


def provenance_graph_state(observations: dict[str, EvidenceObservation]) -> str:
    """Return INVALID PROVENANCE when a parent/root chain is cyclic, broken, or inconsistent."""
    visiting = set()
    visited = set()

    def visit(node_id: str) -> bool:
        if node_id in visiting:
            return True
        if node_id in visited:
            return False
        visiting.add(node_id)
        node = observations.get(node_id)
        if node:
            if node.provenance_parent:
                if node.provenance_parent not in observations:
                    visiting.remove(node_id)
                    return True
                if visit(node.provenance_parent):
                    return True
                parent = observations[node.provenance_parent]
                if node.provenance_root and parent.provenance_root and node.provenance_root != parent.provenance_root:
                    visiting.remove(node_id)
                    return True
                if node.provenance_root and not parent.provenance_root and node.provenance_parent != node.provenance_root:
                    visiting.remove(node_id)
                    return True
            if node.provenance_root:
                if node.provenance_root not in observations:
                    visiting.remove(node_id)
                    return True
        visiting.remove(node_id)
        visited.add(node_id)
        return False

    for evidence_id in observations:
        if visit(evidence_id):
            return "INVALID PROVENANCE"
    return "VALID PROVENANCE"


def provenance_connected(a: EvidenceObservation, b: EvidenceObservation, observations: dict[str, EvidenceObservation]) -> bool:
    if provenance_graph_state(observations) != "VALID PROVENANCE":
        return False
    if a.provenance_root and b.provenance_root and a.provenance_root == b.provenance_root:
        return True
    parents = {a.evidence_id, b.evidence_id}
    frontier = list(parents)
    visited = set(parents)
    while frontier:
        current_id = frontier.pop()
        current = observations.get(current_id)
        if not current or not current.provenance_parent:
            continue
        parent_id = current.provenance_parent
        if parent_id in parents:
            return True
        if parent_id not in visited:
            visited.add(parent_id)
            frontier.append(parent_id)
    return False


def classify(a: EvidenceObservation, b: EvidenceObservation, observations: Optional[dict[str, EvidenceObservation]] = None) -> str:
    same_identity = (a.claim_id == b.claim_id and a.target_id == b.target_id and a.scope == b.scope and a.temporal_context == b.temporal_context)
    if not same_identity:
        return "DIFFERENT CLAIMS"
    if a.proposition != b.proposition:
        return "DIFFERENT EVIDENCE LAYERS"
    if observations:
        if provenance_graph_state(observations) != "VALID PROVENANCE":
            return "UNRESOLVED"
    if a.observed_value == b.observed_value:
        if observations and provenance_connected(a, b, observations):
            return "CONSISTENT / CORRELATED"
        if a.evidence_independence == "INDEPENDENT" and b.evidence_independence == "INDEPENDENT":
            return "CONSISTENT / INDEPENDENT CORROBORATION"
        return "CONSISTENT / CORRELATED"
    if a.completeness != "COMPLETE" or b.completeness != "COMPLETE":
        return "UNRESOLVED"
    return "CONTRADICTION"


def classify_execution_occurrence(capability: EvidenceObservation, occurrence: EvidenceObservation) -> str:
    if capability.claim_type != "EXECUTION" or occurrence.claim_type != "EXECUTION":
        return "UNRESOLVED"
    if capability.semantic_status != "VERIFIED_CAPABILITY" or occurrence.semantic_status != "VERIFIED_OCCURRENCE":
        return "UNRESOLVED"
    if not occurrence.execution_identity or not occurrence.target_commit:
        return "UNRESOLVED"
    if capability.execution_identity and occurrence.execution_identity != capability.execution_identity:
        return "UNRESOLVED"
    if capability.target_commit and occurrence.target_commit != capability.target_commit:
        return "UNRESOLVED"
    return "VERIFIED_OCCURRENCE"


def resolve_by_authority(a: EvidenceObservation, b: EvidenceObservation) -> Optional[str]:
    if classify(a, b) != "CONTRADICTION":
        return None
    if a.authority_scope == "AUTHORITATIVE" and b.authority_scope != "AUTHORITATIVE":
        return a.observed_value
    if b.authority_scope == "AUTHORITATIVE" and a.authority_scope != "AUTHORITATIVE":
        return b.observed_value
    return None


def test_contradiction_resolves_by_claim_authority():
    base = dict(claim_id="baseline", claim_type="NORMATIVE", proposition="development baseline", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="REPOSITORY_STATE", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="INDEPENDENT", completeness="COMPLETE", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="e1", source_ref="Release/VERSION.md", authority_scope="AUTHORITATIVE", observed_value="3.2.1", **base)
    b = EvidenceObservation(evidence_id="e2", source_ref="historical:REP-012", authority_scope="HISTORICAL", observed_value="3.3.0", **base)
    assert classify(a, b) == "CONTRADICTION" and resolve_by_authority(a, b) == "3.2.1"


def test_different_layers_are_not_contradiction():
    common = dict(claim_id="execution-identity", claim_type="EXECUTION", target_id="run:32548603868", scope="repository", temporal_context="run:32548603868", source_ref="github", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="e3", proposition="run is bound to artifact", evidence_layer="ARTIFACT_METADATA", observed_value="BOUND", **common)
    b = EvidenceObservation(evidence_id="e4", proposition="run identity is present in payload", evidence_layer="ARTIFACT_PAYLOAD", observed_value="PRESENT", **common)
    assert classify(a, b) == "DIFFERENT EVIDENCE LAYERS"


def test_incomplete_evidence_is_unresolved_not_contradiction():
    common = dict(claim_id="impact-policy", claim_type="DERIVED_RESULT", proposition="impact mapping result", target_id="commit:test", scope="repository", temporal_context="2026-08-23", evidence_layer="CORRELATION_AUDIT", source_ref="artifact:ci-impact-correlation", authority_scope="PRODUCER_RESULT", claim_fitness="DIRECT", identity_confidence="MEDIUM", evidence_independence="DERIVED", observed_value="POLICY_UNRESOLVED", semantic_status="UNRESOLVED")
    a = EvidenceObservation(evidence_id="e5", completeness="INCOMPLETE", **common)
    b = EvidenceObservation(evidence_id="e6", completeness="COMPLETE", observed_value="PASS", **{k:v for k,v in common.items() if k != "observed_value"})
    assert classify(a, b) == "UNRESOLVED"


def test_resolution_does_not_mutate_original_observations():
    common = dict(claim_id="x", claim_type="NORMATIVE", proposition="x", target_id="t", scope="s", temporal_context="v", evidence_layer="REPOSITORY_STATE", source_ref="source", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="INDEPENDENT", completeness="COMPLETE", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="a", authority_scope="AUTHORITATIVE", observed_value="A", **common)
    b = EvidenceObservation(evidence_id="b", authority_scope="HISTORICAL", observed_value="B", **common)
    assert resolve_by_authority(a, b) == "A" and a.observed_value == "A" and b.observed_value == "B"


def test_missing_execution_identity_is_unresolved_not_failure():
    common = dict(claim_id="execution-claim", claim_type="EXECUTION", proposition="GT-018 execution observed", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_OBSERVATION", source_ref="github:execution-surface", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="LOW", evidence_independence="CORRELATED", semantic_status="UNRESOLVED")
    a = EvidenceObservation(evidence_id="e7", completeness="INCOMPLETE", observed_value="EXECUTION_ID_UNAVAILABLE", **common)
    b = EvidenceObservation(evidence_id="e8", completeness="COMPLETE", observed_value="FAIL", **common)
    assert classify(a, b) == "UNRESOLVED"


def test_verified_capability_does_not_promote_unrelated_occurrence():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:historical-run", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="AVAILABLE")
    capability = EvidenceObservation(evidence_id="cap-1", semantic_status="VERIFIED_CAPABILITY", **common)
    current = EvidenceObservation(evidence_id="occ-1", semantic_status="UNRESOLVED", **{**common, "source_ref":"github:current-commit", "observed_value":"EXECUTION_ID_UNAVAILABLE"})
    assert classify_execution_occurrence(capability, current) == "UNRESOLVED"


def test_verified_occurrence_requires_explicit_bound_identity():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED")
    capability = EvidenceObservation(evidence_id="cap-2", execution_identity="run:current", target_commit="c422556", semantic_status="VERIFIED_CAPABILITY", **common)
    unbound = EvidenceObservation(evidence_id="occ-2", execution_identity=None, target_commit=None, semantic_status="VERIFIED_OCCURRENCE", **common)
    assert classify_execution_occurrence(capability, unbound) == "UNRESOLVED"


def test_verified_occurrence_with_bound_identity_is_verifiable():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED")
    capability = EvidenceObservation(evidence_id="cap-3", execution_identity="run:current", target_commit="c422556", semantic_status="VERIFIED_CAPABILITY", **common)
    occurrence = EvidenceObservation(evidence_id="occ-3", execution_identity="run:current", target_commit="c422556", semantic_status="VERIFIED_OCCURRENCE", **common)
    assert classify_execution_occurrence(capability, occurrence) == "VERIFIED_OCCURRENCE"


def test_cross_binding_mismatch_is_unresolved():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED")
    capability = EvidenceObservation(evidence_id="cap-4", execution_identity="run:current", target_commit="target-A", semantic_status="VERIFIED_CAPABILITY", **common)
    mismatch = EvidenceObservation(evidence_id="occ-4", execution_identity="run:current", target_commit="target-B", semantic_status="VERIFIED_OCCURRENCE", **common)
    assert classify_execution_occurrence(capability, mismatch) == "UNRESOLVED"


def test_execution_identity_mismatch_is_unresolved():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="EXECUTED", evidence_independence="CORRELATED")
    capability = EvidenceObservation(evidence_id="cap-5", execution_identity="run:A", target_commit="target-A", semantic_status="VERIFIED_CAPABILITY", **common)
    mismatch = EvidenceObservation(evidence_id="occ-5", execution_identity="run:B", target_commit="target-A", semantic_status="VERIFIED_OCCURRENCE", **common)
    assert classify_execution_occurrence(capability, mismatch) == "UNRESOLVED"


def test_correlated_evidence_is_not_independent_corroboration():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", evidence_layer="RUN_METADATA", source_ref="run-metadata", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    metadata = EvidenceObservation(evidence_id="e6", **common)
    artifact = EvidenceObservation(evidence_id="e7", source_ref="artifact-upload", evidence_layer="ARTIFACT", **{k:v for k,v in common.items() if k not in {"source_ref", "evidence_layer"}})
    assert classify(metadata, artifact) == "CONSISTENT / CORRELATED"


def test_independent_evidence_is_stronger_corroboration():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    run = EvidenceObservation(evidence_id="e8", source_ref="workflow-run", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", **common)
    external = EvidenceObservation(evidence_id="e9", source_ref="independent-check", evidence_layer="INDEPENDENT_CHECK", evidence_independence="INDEPENDENT", **common)
    assert classify(run, external) == "CONSISTENT / INDEPENDENT CORROBORATION"


def test_transitive_provenance_marks_independence_as_correlated():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root = EvidenceObservation(evidence_id="root", source_ref="source-run", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="root", **common)
    child = EvidenceObservation(evidence_id="child", source_ref="derived-artifact", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root=None, provenance_parent="root", **common)
    grandchild = EvidenceObservation(evidence_id="grandchild", source_ref="derived-report", evidence_layer="REPORT", evidence_independence="INDEPENDENT", provenance_root=None, provenance_parent="child", **common)
    observations = {x.evidence_id: x for x in (root, child, grandchild)}
    assert classify(root, grandchild, observations) == "CONSISTENT / CORRELATED"


def test_disconnected_provenance_can_remain_independent():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root_a = EvidenceObservation(evidence_id="root-A", source_ref="workflow-run-A", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="root-A", **common)
    root_b = EvidenceObservation(evidence_id="root-B", source_ref="workflow-run-B", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="root-B", **common)
    a = EvidenceObservation(evidence_id="ind-a", source_ref="artifact-A", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="root-A", provenance_parent="root-A", **common)
    b = EvidenceObservation(evidence_id="ind-b", source_ref="artifact-B", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="root-B", provenance_parent="root-B", **common)
    observations = {x.evidence_id: x for x in (root_a, root_b, a, b)}
    assert provenance_graph_state(observations) == "VALID PROVENANCE"
    assert classify(a, b, observations) == "CONSISTENT / INDEPENDENT CORROBORATION"


def test_provenance_cycle_invalidates_corroboration():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="INDEPENDENT", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="cycle-a", source_ref="source-A", evidence_layer="RUN_METADATA", provenance_parent="cycle-b", **common)
    b = EvidenceObservation(evidence_id="cycle-b", source_ref="source-B", evidence_layer="RUN_METADATA", provenance_parent="cycle-a", **common)
    observations = {a.evidence_id: a, b.evidence_id: b}
    assert provenance_graph_state(observations) == "INVALID PROVENANCE"
    assert classify(a, b, observations) == "UNRESOLVED"


def test_missing_parent_invalidates_provenance_and_blocks_independence():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="INDEPENDENT", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="broken-a", source_ref="derived-artifact", evidence_layer="ARTIFACT", provenance_parent="missing-root", **common)
    b = EvidenceObservation(evidence_id="broken-b", source_ref="independent-check", evidence_layer="CHECK", provenance_root="root-b", **common)
    observations = {a.evidence_id: a, b.evidence_id: b}
    assert provenance_graph_state(observations) == "INVALID PROVENANCE"
    assert classify(a, b, observations) == "UNRESOLVED"


def test_valid_provenance_without_missing_links_preserves_independence():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root_a = EvidenceObservation(evidence_id="root-A", source_ref="run-A", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="root-A", **common)
    root_b = EvidenceObservation(evidence_id="root-B", source_ref="run-B", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="root-B", **common)
    a = EvidenceObservation(evidence_id="valid-a", source_ref="artifact-A", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="root-A", provenance_parent="root-A", **common)
    b = EvidenceObservation(evidence_id="valid-b", source_ref="artifact-B", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="root-B", provenance_parent="root-B", **common)
    observations = {x.evidence_id: x for x in (root_a, root_b, a, b)}
    assert provenance_graph_state(observations) == "VALID PROVENANCE"
    assert classify(a, b, observations) == "CONSISTENT / INDEPENDENT CORROBORATION"


def test_missing_root_blocks_independent_corroboration_even_when_roots_differ():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    a = EvidenceObservation(evidence_id="unbound-a", source_ref="run-A", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="not-loaded-A", **common)
    b = EvidenceObservation(evidence_id="unbound-b", source_ref="run-B", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="not-loaded-B", **common)
    observations = {a.evidence_id: a, b.evidence_id: b}
    assert classify(a, b, observations) == "UNRESOLVED"


def test_gt039_root_parent_mismatch_is_invalid_provenance_not_claim_contradiction():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-24", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root_a = EvidenceObservation(evidence_id="ROOT-A", source_ref="root-source-A", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", **common)
    root_b = EvidenceObservation(evidence_id="ROOT-B", source_ref="root-source-B", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="ROOT-B", **common)
    child = EvidenceObservation(evidence_id="CHILD", source_ref="child-source", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="ROOT-B", provenance_parent="ROOT-A", **common)
    observations = {x.evidence_id: x for x in (root_a, root_b, child)}
    assert provenance_graph_state(observations) == "INVALID PROVENANCE"
    assert classify(root_a, child, observations) == "UNRESOLVED"


def test_gt039_matching_root_and_parent_remains_valid():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-24", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root = EvidenceObservation(evidence_id="ROOT-A", source_ref="root-source-A", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", **common)
    child = EvidenceObservation(evidence_id="CHILD", source_ref="child-source", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", provenance_parent="ROOT-A", **common)
    observations = {x.evidence_id: x for x in (root, child)}
    assert provenance_graph_state(observations) == "VALID PROVENANCE"
    assert classify(root, child, observations) == "CONSISTENT / CORRELATED"


def test_gt040_explicit_root_agreement_across_multilevel_parent_chain():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-24", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    root = EvidenceObservation(evidence_id="ROOT-A", source_ref="root-source", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", **common)
    parent = EvidenceObservation(evidence_id="PARENT", source_ref="parent-source", evidence_layer="ARTIFACT", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", provenance_parent="ROOT-A", **common)
    child = EvidenceObservation(evidence_id="CHILD", source_ref="child-source", evidence_layer="REPORT", evidence_independence="INDEPENDENT", provenance_root="ROOT-A", provenance_parent="PARENT", **common)
    observations = {x.evidence_id: x for x in (root, parent, child)}
    assert provenance_graph_state(observations) == "VALID PROVENANCE"
    assert classify(parent, child, observations) == "CONSISTENT / CORRELATED"
