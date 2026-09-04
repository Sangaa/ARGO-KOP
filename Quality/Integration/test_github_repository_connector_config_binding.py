from __future__ import annotations

import pytest

from Services.GITHUB_REPOSITORY_CONNECTOR import GitHubConnectorConfig
from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorError


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("owner", None),
        ("owner", ""),
        ("owner", "   "),
        ("owner", False),
        ("repo", None),
        ("repo", ""),
        ("repo", "   "),
        ("repo", False),
        ("token", None),
        ("token", ""),
        ("token", "   "),
        ("token", False),
        ("branch", None),
        ("branch", ""),
        ("branch", "   "),
        ("branch", False),
        ("api_base", None),
        ("api_base", ""),
        ("api_base", "   "),
        ("api_base", False),
    ],
)
def test_direct_config_rejects_incomplete_or_nontext_boundary_values(field: str, value: object):
    values = {
        "owner": "Sangaa",
        "repo": "ARGO-KOP",
        "token": "test-token",
        "branch": "main",
        "api_base": "https://api.github.com",
    }
    values[field] = value

    with pytest.raises(ConnectorError, match="GITHUB_CONNECTOR_CONFIGURATION_INCOMPLETE"):
        GitHubConnectorConfig(**values)


def test_direct_config_preserves_valid_explicit_boundary_values():
    config = GitHubConnectorConfig(
        owner="Sangaa",
        repo="ARGO-KOP",
        token="test-token",
        branch="release/test",
        api_base="https://example.invalid",
    )

    assert config.owner == "Sangaa"
    assert config.repo == "ARGO-KOP"
    assert config.token == "test-token"
    assert config.branch == "release/test"
    assert config.api_base == "https://example.invalid"
