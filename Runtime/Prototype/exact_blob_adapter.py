"""Non-production exact-blob verification seam for KRS-001 Pilot 3."""

import hashlib


def consume_exact_blob(artifact_bytes: bytes, expected_blob_sha: str, harness):
    """Verify exact content identity before passing content to the existing harness.

    This adapter performs no external I/O and does not change production behavior.
    """
    observed = hashlib.sha1(artifact_bytes).hexdigest()
    if observed != expected_blob_sha:
        raise ValueError(f"exact blob mismatch: expected={expected_blob_sha} observed={observed}")
    result = harness(artifact_bytes)
    return {
        "expected_blob_sha": expected_blob_sha,
        "observed_blob_sha": observed,
        "blob_match": True,
        "harness_result": result,
        "external_side_effect": False,
    }
