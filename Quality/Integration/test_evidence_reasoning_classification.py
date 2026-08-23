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


def classify(a: EvidenceObservation, b: EvidenceObservation) -> str:
    same_identity = (a.claim_id == b.claim_id and a.target_id == b.target_id and a.scope == b.scope and a.temporal_context == b.temporal_context)
    if not same_identity:
        return "DIFFERENT CLAIMS"
    if a.proposition != b.proposition:
        return "DIFFERENT EVIDENCE LAYERS"
    if a.observed_value == b.observed_value:
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
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED", semantic_status="VERIFIED_OCCURRENCE")
    capability = EvidenceObservation(evidence_id="cap-2", execution_identity="run:current", target_commit="c422556", semantic_status="VERIFIED_CAPABILITY", **common)
    unbound = EvidenceObservation(evidence_id="occ-2", execution_identity=None, target_commit=None, **common)
    assert classify_execution_occurrence(capability, unbound) == "UNRESOLVED"


def test_verified_occurrence_with_bound_identity_is_verifiable():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED", semantic_status="VERIFIED_OCCURRENCE")
    capability = EvidenceObservation(evidence_id="cap-3", execution_identity="run:current", target_commit="c422556", semantic_status="VERIFIED_CAPABILITY", **common)
    occurrence = EvidenceObservation(evidence_id="occ-3", execution_identity="run:current", target_commit="c422556", **common)
    assert classify_execution_occurrence(capability, occurrence) == "VERIFIED_OCCURRENCE"


def test_cross_binding_mismatch_is_unresolved():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED", semantic_status="VERIFIED_OCCURRENCE")
    capability = EvidenceObservation(evidence_id="cap-4", execution_identity="run:current", target_commit="target-A", semantic_status="VERIFIED_CAPABILITY", **common)
    mismatch = EvidenceObservation(evidence_id="occ-4", execution_identity="run:current", target_commit="target-B", **common)
    assert classify_execution_occurrence(capability, mismatch) == "UNRESOLVED"


def test_execution_identity_mismatch_is_unresolved():
    common = dict(claim_id="execution-channel", claim_type="EXECUTION", proposition="execution evidence channel", target_id="ARGO-KOP", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", source_ref="github:current-commit", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", evidence_independence="CORRELATED", completeness="COMPLETE", observed_value="EXECUTED", semantic_status="VERIFIED_OCCURRENCE")
    capability = EvidenceObservation(evidence_id="cap-5", execution_identity="run:A", target_commit="target-A", semantic_status="VERIFIED_CAPABILITY", **common)
    mismatch = EvidenceObservation(evidence_id="occ-5", execution_identity="run:B", target_commit="target-A", **common)
    assert classify_execution_occurrence(capability, mismatch) == "UNRESOLVED"


def test_correlated_evidence_is_not_independent_corroboration():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", evidence_layer="EXECUTION_SURFACE", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    metadata = EvidenceObservation(evidence_id="e6", source_ref="run-metadata", evidence_independence="CORRELATED", **common)
    artifact = EvidenceObservation(evidence_id="e7", source_ref="artifact-upload", evidence_independence="CORRELATED", **common)
    assert classify(metadata, artifact) == "CONSISTENT / CORRELATED"


def test_independent_evidence_is_stronger_corroboration():
    common = dict(claim_id="run-status", claim_type="EXECUTION", proposition="run completed successfully", target_id="run:current", scope="repository", temporal_context="2026-08-23", authority_scope="FACTUAL", claim_fitness="DIRECT", identity_confidence="HIGH", completeness="COMPLETE", observed_value="SUCCESS", semantic_status="OBSERVED")
    run = EvidenceObservation(evidence_id="e8", source_ref="workflow-run", evidence_layer="RUN_METADATA", evidence_independence="INDEPENDENT", **common)
    external = EvidenceObservation(evidence_id="e9", source_ref="independent-check", evidence_layer="INDEPENDENT_CHECK", evidence_independence="INDEPENDENT", **common)
    assert classify(run, external) == "CONSISTENT / INDEPENDENT CORROBORATION"
