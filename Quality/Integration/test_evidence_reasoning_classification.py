"""Controlled runtime proof for ARGO evidence reasoning classification.

This test fixture is deliberately self-contained and side-effect free. It proves
only the evidence-classification boundary; it does not authorize or execute an
external action.
"""

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


def classify(a: EvidenceObservation, b: EvidenceObservation) -> str:
    same_claim = (
        a.claim_id == b.claim_id
        and a.proposition == b.proposition
        and a.target_id == b.target_id
        and a.scope == b.scope
        and a.temporal_context == b.temporal_context
    )

    if not same_claim:
        return "DIFFERENT EVIDENCE LAYERS"

    if a.observed_value == b.observed_value:
        return "CONSISTENT / CORROBORATED"

    if a.completeness != "COMPLETE" or b.completeness != "COMPLETE":
        return "UNRESOLVED"

    return "CONTRADICTION"


def resolve_by_authority(a: EvidenceObservation, b: EvidenceObservation) -> Optional[str]:
    if classify(a, b) != "CONTRADICTION":
        return None
    if a.authority_scope == "AUTHORITATIVE" and b.authority_scope != "AUTHORITATIVE":
        return a.observed_value
    if b.authority_scope == "AUTHORITATIVE" and a.authority_scope != "AUTHORITATIVE":
        return b.observed_value
    return None


def test_contradiction_resolves_by_claim_authority():
    base = dict(
        claim_id="baseline",
        claim_type="NORMATIVE",
        proposition="development baseline",
        target_id="ARGO-KOP",
        scope="repository",
        temporal_context="2026-08-23",
        evidence_layer="REPOSITORY_STATE",
        claim_fitness="DIRECT",
        identity_confidence="HIGH",
        evidence_independence="INDEPENDENT",
        completeness="COMPLETE",
        semantic_status="OBSERVED",
    )
    authoritative = EvidenceObservation(
        evidence_id="e1", source_ref="Release/VERSION.md",
        authority_scope="AUTHORITATIVE", observed_value="3.2.1", **base
    )
    historical = EvidenceObservation(
        evidence_id="e2", source_ref="historical:REP-012",
        authority_scope="HISTORICAL", observed_value="3.3.0", **base
    )

    assert classify(authoritative, historical) == "CONTRADICTION"
    assert resolve_by_authority(authoritative, historical) == "3.2.1"


def test_different_layers_are_not_contradiction():
    common = dict(
        claim_id="execution-identity",
        claim_type="EXECUTION",
        target_id="run:32548603868",
        scope="repository",
        temporal_context="run:32548603868",
        source_ref="github",
        authority_scope="FACTUAL",
        claim_fitness="DIRECT",
        identity_confidence="HIGH",
        evidence_independence="CORRELATED",
        completeness="COMPLETE",
        semantic_status="OBSERVED",
    )
    metadata = EvidenceObservation(
        evidence_id="e3", proposition="run is bound to artifact",
        evidence_layer="ARTIFACT_METADATA", observed_value="BOUND", **common
    )
    payload = EvidenceObservation(
        evidence_id="e4", proposition="run identity is present in payload",
        evidence_layer="ARTIFACT_PAYLOAD", observed_value="PRESENT", **common
    )

    assert classify(metadata, payload) == "DIFFERENT EVIDENCE LAYERS"


def test_incomplete_evidence_is_unresolved_not_contradiction():
    common = dict(
        claim_id="impact-policy",
        claim_type="DERIVED_RESULT",
        proposition="impact mapping result",
        target_id="commit:test",
        scope="repository",
        temporal_context="2026-08-23",
        evidence_layer="CORRELATION_AUDIT",
        source_ref="artifact:ci-impact-correlation",
        authority_scope="PRODUCER_RESULT",
        claim_fitness="DIRECT",
        identity_confidence="MEDIUM",
        evidence_independence="DERIVED",
        observed_value="POLICY_UNRESOLVED",
        semantic_status="UNRESOLVED",
    )
    unresolved = EvidenceObservation(
        evidence_id="e5", completeness="INCOMPLETE", **common
    )
    competing = EvidenceObservation(
        evidence_id="e6", completeness="COMPLETE", observed_value="PASS", **{k: v for k, v in common.items() if k != "observed_value"}
    )

    assert classify(unresolved, competing) == "UNRESOLVED"


def test_resolution_does_not_mutate_original_observations():
    common = dict(
        claim_id="x", claim_type="NORMATIVE", proposition="x", target_id="t",
        scope="s", temporal_context="v", evidence_layer="REPOSITORY_STATE",
        source_ref="source", claim_fitness="DIRECT", identity_confidence="HIGH",
        evidence_independence="INDEPENDENT", completeness="COMPLETE",
        semantic_status="OBSERVED",
    )
    a = EvidenceObservation(evidence_id="a", authority_scope="AUTHORITATIVE", observed_value="A", **common)
    b = EvidenceObservation(evidence_id="b", authority_scope="HISTORICAL", observed_value="B", **common)
    before_a, before_b = a, b

    assert resolve_by_authority(a, b) == "A"
    assert a == before_a
    assert b == before_b
