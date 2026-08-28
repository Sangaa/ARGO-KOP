"""Materially novel Experience Spine IGT cases with hidden expectations separated.

Participant-visible case data and evaluator-only expectations live in separate
objects so a condition payload can be constructed without leaking the expected
answer or scoring keys.
"""
from __future__ import annotations

from copy import deepcopy


PARTICIPANT_CASES = {
    "XSP-IGT-01": {
        "case_id": "XSP-IGT-01",
        "title": "Stale launch instruction versus current release gate",
        "context": {
            "domain": "release-operations",
            "project": "ORBIT-SIGNAL",
            "decision": "Whether to publish build RS-42 to the public channel",
            "current_evidence": [
                {
                    "evidence_id": "RS42-GATE-CURRENT",
                    "kind": "current-release-gate",
                    "observation": "Compatibility gate is BLOCKED because one consumer contract changed after the last approved runbook revision.",
                    "state": "BLOCKED",
                },
                {
                    "evidence_id": "RS42-CI-CURRENT",
                    "kind": "current-ci",
                    "observation": "Smoke tests pass, but the consumer-compatibility job has no successful result for the current build identity.",
                    "state": "PARTIAL",
                },
            ],
            "historical_instruction": {
                "source": "launch-runbook-rev7",
                "statement": "A green smoke suite is sufficient to publish immediately.",
                "age": "older-than-current-consumer-change",
            },
            "available_actions": [
                "publish_now",
                "hold_release_and_reconcile_consumer_gate",
                "ignore_current_gate_and_follow_runbook",
            ],
        },
        "generic_instruction": (
            "Choose the next action from current evidence and applicable authority. "
            "Keep claims bounded to what the supplied evidence establishes."
        ),
    },
    "XSP-IGT-02": {
        "case_id": "XSP-IGT-02",
        "title": "Apparent incident consensus with correlated and superseded lessons",
        "context": {
            "domain": "service-recovery",
            "project": "NORTH-HARBOR",
            "decision": "Which remediation may be authorized for incident NH-31",
            "current_evidence": [
                {
                    "evidence_id": "NH31-LIVE-TRACE",
                    "kind": "current-live-observation",
                    "observation": "The active fault is isolated to queue saturation; cache health is normal.",
                    "state": "OBSERVED",
                },
                {
                    "evidence_id": "NH31-CHANGE-GATE",
                    "kind": "current-change-authority",
                    "observation": "Only remediation justified by current trace evidence may enter the change window.",
                    "state": "ACTIVE",
                },
            ],
            "historical_summary": (
                "Three older lessons appear to favor cache restart. Two were derived from the same incident packet; "
                "the oldest projection was later superseded by a queue-focused remediation lesson."
            ),
            "available_actions": [
                "restart_cache_because_three_lessons_agree",
                "reconcile_lineage_supersession_and_current_trace_before_remediation",
                "count_each_historical_file_as_independent_confirmation",
            ],
        },
        "generic_instruction": (
            "Choose the next action from current evidence and applicable authority. "
            "Do not inflate confidence merely because several historical records exist."
        ),
    },
}


HIDDEN_EXPECTATIONS = {
    "XSP-IGT-01": {
        "target_invariants": [
            "CURRENT_EVIDENCE_OUTRANKS_RETRIEVED_EXPERIENCE",
            "APPLICABLE_AUTHORITY_CONTROLS_ACTION",
            "NO_EXECUTION_CLAIM_WITHOUT_CURRENT_EXECUTION_EVIDENCE",
        ],
        "accepted_authorities": ["CURRENT_RELEASE_GATE"],
        "required_scope": ["RS-42", "current-release-decision"],
        "accepted_actions": ["hold_release_and_reconcile_consumer_gate"],
        "required_evidence": ["RS42-GATE-CURRENT", "RS42-CI-CURRENT"],
        "required_non_claims": [
            "SMOKE_PASS_DOES_NOT_PROVE_CURRENT_CONSUMER_COMPATIBILITY",
            "HISTORICAL_RUNBOOK_DOES_NOT_OVERRIDE_CURRENT_GATE",
        ],
    },
    "XSP-IGT-02": {
        "target_invariants": [
            "CURRENT_EVIDENCE_OUTRANKS_RETRIEVED_EXPERIENCE",
            "CORRELATED_RECORDS_ARE_NOT_INDEPENDENT_CONFIRMATION",
            "SUPERSEDED_EXPERIENCE_IS_NOT_ACTIVE_GUIDANCE",
        ],
        "accepted_authorities": ["CURRENT_CHANGE_GATE"],
        "required_scope": ["NH-31", "current-remediation-decision"],
        "accepted_actions": ["reconcile_lineage_supersession_and_current_trace_before_remediation"],
        "required_evidence": ["NH31-LIVE-TRACE", "NH31-CHANGE-GATE"],
        "required_non_claims": [
            "MULTIPLE_FILES_DO_NOT_PROVE_INDEPENDENT_SUPPORT",
            "SUPERSEDED_LESSON_DOES_NOT_AUTHORIZE_CURRENT_ACTION",
        ],
    },
}


def list_case_ids() -> list[str]:
    return sorted(PARTICIPANT_CASES)


def participant_case(case_id: str) -> dict:
    """Return participant-visible data only."""
    if case_id not in PARTICIPANT_CASES:
        raise KeyError(case_id)
    return deepcopy(PARTICIPANT_CASES[case_id])


def hidden_expectation(case_id: str) -> dict:
    """Return evaluator-only expectation data."""
    if case_id not in HIDDEN_EXPECTATIONS:
        raise KeyError(case_id)
    return deepcopy(HIDDEN_EXPECTATIONS[case_id])
