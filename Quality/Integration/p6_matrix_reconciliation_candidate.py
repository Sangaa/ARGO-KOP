"""Build and verify bounded P6 matrix-reconciliation candidates from CI evidence.

This module implements the P6-08/P6-09 automation boundary without granting CI
repository authority. It produces a non-authoritative candidate artifact from
correlation evidence, then re-reads the checked-out REP-020/REP-014 surfaces to
verify that source identity remained stable. Canonical mutation still requires
normal ARGO governance and controlled-write authorization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MATRIX = REPO_ROOT / "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md"
DEFAULT_REGISTRY = REPO_ROOT / "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md"

STATE_MAP = {
    "MAPPED": "OBSERVED_IMPACT",
    "UNMAPPED": "REVALIDATION_REQUIRED",
    "NOT_APPLICABLE": "NOT_APPLICABLE",
    "POLICY_UNRESOLVED": "POLICY_UNRESOLVED",
}


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_candidate(
    correlation: dict[str, Any],
    execution_identity: dict[str, Any],
    matrix_text: str,
    registry_text: str,
) -> dict[str, Any]:
    head = str(correlation.get("head") or "")
    github_sha = str(execution_identity.get("github_sha") or "")
    checkout_sha = str(execution_identity.get("checkout_sha") or "")
    if not head or head != github_sha or head != checkout_sha:
        raise ValueError("CI_HEAD_IDENTITY_MISMATCH")

    records = []
    for record in correlation.get("records", []):
        status = str(record.get("status") or "")
        if status not in STATE_MAP:
            raise ValueError(f"UNSUPPORTED_CORRELATION_STATUS:{status}")
        records.append(
            {
                "path": record.get("path"),
                "eligibility": record.get("eligibility"),
                "correlation_status": status,
                "candidate_state": STATE_MAP[status],
                "promotion": "NO_AUTO_PROMOTION",
            }
        )

    return {
        "schema": "P6-MATRIX-RECONCILIATION-CANDIDATE/v1",
        "head": head,
        "base": correlation.get("base"),
        "workflow": execution_identity.get("workflow"),
        "run_id": execution_identity.get("run_id"),
        "correlation_schema": correlation.get("schema"),
        "correlation_overall": correlation.get("overall"),
        "matrix_source": "Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md",
        "matrix_sha256": _sha256(matrix_text),
        "relationship_source": "Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md",
        "relationship_sha256": _sha256(registry_text),
        "candidate_authority": "NON_AUTHORITATIVE_EVIDENCE_CANDIDATE",
        "promotion": "NO_AUTO_PROMOTION",
        "records": records,
    }


def verify_readback(
    candidate: dict[str, Any],
    expected_head: str,
    matrix_text: str,
    registry_text: str,
) -> dict[str, Any]:
    if candidate.get("schema") != "P6-MATRIX-RECONCILIATION-CANDIDATE/v1":
        raise ValueError("CANDIDATE_SCHEMA_INVALID")
    if candidate.get("head") != expected_head:
        raise ValueError("CANDIDATE_HEAD_MISMATCH")
    if candidate.get("promotion") != "NO_AUTO_PROMOTION":
        raise ValueError("AUTO_PROMOTION_FORBIDDEN")
    if candidate.get("candidate_authority") != "NON_AUTHORITATIVE_EVIDENCE_CANDIDATE":
        raise ValueError("CANDIDATE_AUTHORITY_INVALID")
    if candidate.get("matrix_sha256") != _sha256(matrix_text):
        raise ValueError("REP020_READBACK_MISMATCH")
    if candidate.get("relationship_sha256") != _sha256(registry_text):
        raise ValueError("REP014_READBACK_MISMATCH")
    return {
        "status": "VERIFIED",
        "head": expected_head,
        "matrix_readback": "VERIFIED_UNCHANGED",
        "relationship_readback": "VERIFIED_UNCHANGED",
        "promotion": "NO_AUTO_PROMOTION",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--correlation", default="ci-impact-correlation.json")
    parser.add_argument("--identity", default="ci-execution-identity.json")
    parser.add_argument("--output", default="p6-matrix-reconciliation-candidate.json")
    args = parser.parse_args()

    correlation = json.loads(Path(args.correlation).read_text(encoding="utf-8"))
    identity = json.loads(Path(args.identity).read_text(encoding="utf-8"))
    matrix_text = DEFAULT_MATRIX.read_text(encoding="utf-8")
    registry_text = DEFAULT_REGISTRY.read_text(encoding="utf-8")

    candidate = build_candidate(correlation, identity, matrix_text, registry_text)
    output = Path(args.output)
    output.write_text(json.dumps(candidate, indent=2, sort_keys=True), encoding="utf-8")

    readback_candidate = json.loads(output.read_text(encoding="utf-8"))
    result = verify_readback(
        readback_candidate,
        str(identity.get("checkout_sha") or ""),
        DEFAULT_MATRIX.read_text(encoding="utf-8"),
        DEFAULT_REGISTRY.read_text(encoding="utf-8"),
    )
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
