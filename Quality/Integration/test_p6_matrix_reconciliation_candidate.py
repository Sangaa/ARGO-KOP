import copy

import pytest

from p6_matrix_reconciliation_candidate import build_candidate, verify_readback


def _correlation(status="MAPPED"):
    return {
        "schema": "P6-CI-IMPACT-CORRELATION/v4",
        "base": "base-sha",
        "head": "head-sha",
        "overall": "MAPPED",
        "records": [
            {
                "path": "Engine/ENG-006_EXECUTION_ENGINE.md",
                "eligibility": "IN_SCOPE",
                "status": status,
            }
        ],
    }


def _identity():
    return {
        "workflow": "Full-Stack Repository Audit",
        "run_id": "123",
        "github_sha": "head-sha",
        "checkout_sha": "head-sha",
    }


def test_build_candidate_is_non_authoritative_and_head_bound():
    candidate = build_candidate(_correlation(), _identity(), "matrix", "registry")
    assert candidate["head"] == "head-sha"
    assert candidate["candidate_authority"] == "NON_AUTHORITATIVE_EVIDENCE_CANDIDATE"
    assert candidate["promotion"] == "NO_AUTO_PROMOTION"
    assert candidate["records"][0]["candidate_state"] == "OBSERVED_IMPACT"


def test_unmapped_becomes_revalidation_not_promotion():
    candidate = build_candidate(_correlation("UNMAPPED"), _identity(), "matrix", "registry")
    assert candidate["records"][0]["candidate_state"] == "REVALIDATION_REQUIRED"
    assert candidate["records"][0]["promotion"] == "NO_AUTO_PROMOTION"


def test_build_candidate_fails_closed_on_ci_identity_mismatch():
    identity = _identity()
    identity["checkout_sha"] = "other"
    with pytest.raises(ValueError, match="CI_HEAD_IDENTITY_MISMATCH"):
        build_candidate(_correlation(), identity, "matrix", "registry")


def test_readback_verifies_unchanged_sources():
    candidate = build_candidate(_correlation(), _identity(), "matrix", "registry")
    result = verify_readback(candidate, "head-sha", "matrix", "registry")
    assert result["status"] == "VERIFIED"
    assert result["matrix_readback"] == "VERIFIED_UNCHANGED"
    assert result["relationship_readback"] == "VERIFIED_UNCHANGED"


def test_readback_detects_rep020_drift():
    candidate = build_candidate(_correlation(), _identity(), "matrix", "registry")
    with pytest.raises(ValueError, match="REP020_READBACK_MISMATCH"):
        verify_readback(candidate, "head-sha", "matrix-changed", "registry")


def test_readback_detects_rep014_drift():
    candidate = build_candidate(_correlation(), _identity(), "matrix", "registry")
    with pytest.raises(ValueError, match="REP014_READBACK_MISMATCH"):
        verify_readback(candidate, "head-sha", "matrix", "registry-changed")


def test_readback_rejects_auto_promotion():
    candidate = build_candidate(_correlation(), _identity(), "matrix", "registry")
    mutated = copy.deepcopy(candidate)
    mutated["promotion"] = "AUTO_PROMOTE"
    with pytest.raises(ValueError, match="AUTO_PROMOTION_FORBIDDEN"):
        verify_readback(mutated, "head-sha", "matrix", "registry")
