from __future__ import annotations

from typing import get_type_hints

from Services.REPOSITORY_CONNECTOR_INTERFACE import (
    ConnectorFile,
    PRODUCTION_CONNECTOR_REQUIREMENTS,
    RepositoryConnector,
)


def test_repository_connector_contract_shape() -> None:
    required = {
        "read_current",
        "create_file",
        "update_file",
        "read_back",
    }
    # Protocol methods are verified through the declared callable surface.
    for name in required:
        assert callable(getattr(RepositoryConnector, name, None)), name

    assert len(PRODUCTION_CONNECTOR_REQUIREMENTS) == 6
    assert get_type_hints(ConnectorFile) == {
        "path": str,
        "sha": str,
        "content": str,
    }
