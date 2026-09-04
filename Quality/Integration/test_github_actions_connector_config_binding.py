from __future__ import annotations

import pytest

from Services.GITHUB_ACTIONS_CONNECTOR import GitHubActionsRepositoryConnector
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
        ("api_base", None),
        ("api_base", ""),
        ("api_base", "   "),
        ("api_base", False),
    ],
)
def test_direct_actions_config_rejects_incomplete_or_nontext_boundary_values(
    field: str, value: object
):
    values = {
        "owner": "Sangaa",
        "repo": "ARGO-KOP",
        "token": "test-token",
        "api_base": "https://api.github.com",
    }
    values[field] = value

    with pytest.raises(ConnectorError, match="GITHUB_ACTIONS_CONNECTOR_CONFIGURATION_INCOMPLETE"):
        GitHubActionsRepositoryConnector(**values)


def test_direct_actions_config_preserves_valid_explicit_boundary_values():
    connector = GitHubActionsRepositoryConnector(
        owner="Sangaa",
        repo="ARGO-KOP",
        token="test-token",
        api_base="https://example.invalid/",
    )

    assert connector._url("runs") == "https://example.invalid/repos/Sangaa/ARGO-KOP/actions/runs"
