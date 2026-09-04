import base64
import json

import pytest

from Services.EVIDENCE_RESOLVER_ADAPTER_INTERFACE import EvidenceResolverAdapterError
from Services.GITHUB_EVIDENCE_RESOLVER_ADAPTER import (
    GitHubEvidenceResolverAdapter,
    GitHubEvidenceResolverConfig,
)


COMMIT = "90ad59cac9fbba69c1ed32cacc84d531eb5d9dfa"
REF = f"github+artifact://Sangaa/ARGO-KOP@{COMMIT}/Evidence/blob.json"


def _encode_json(value) -> str:
    return base64.b64encode(json.dumps(value).encode("utf-8")).decode("ascii")


def _adapter_with_sha(blob_sha):
    def transport(request, timeout):
        return {"type": "file", "sha": blob_sha, "content": _encode_json({"value": 1})}

    return GitHubEvidenceResolverAdapter(
        GitHubEvidenceResolverConfig(token="test-token"),
        transport=transport,
    )


def test_blob_sha_preserves_exact_provider_string_identity():
    blob_sha = "AbC-provider-identity"
    acquisition = _adapter_with_sha(blob_sha).acquire_external(REF)

    assert acquisition.observation["github_artifact_blob_sha"] == blob_sha


@pytest.mark.parametrize(
    "blob_sha",
    [None, True, False, 0, 17, 1.5, [], {}, "", "   "],
)
def test_blob_sha_rejects_missing_blank_or_non_string_identity(blob_sha):
    with pytest.raises(EvidenceResolverAdapterError, match="GITHUB_EVIDENCE_BLOB_SHA_MISSING"):
        _adapter_with_sha(blob_sha).acquire_external(REF)


def test_blob_sha_type_validation_prevents_identity_coercion():
    with pytest.raises(EvidenceResolverAdapterError):
        _adapter_with_sha(True).acquire_external(REF)

    # The old behavior could record "True" as a provider identity via str(True).
    # A provider identifier must be validated, not synthesized by coercion.
