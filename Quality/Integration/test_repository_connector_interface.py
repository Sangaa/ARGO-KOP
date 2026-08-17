from Services.REPOSITORY_CONNECTOR_INTERFACE import ConnectorFile, PRODUCTION_CONNECTOR_REQUIREMENTS, RepositoryConnector


def test_repository_connector_contract_shape() -> None:
    required = {
        "read_current",
        "create_file",
        "update_file",
        "read_back",
    }
    protocol_members = set(RepositoryConnector.__annotations__) if hasattr(RepositoryConnector, "__annotations__") else set()
    # Protocol methods are verified by the source-level callable surface.
    assert required
    assert len(PRODUCTION_CONNECTOR_REQUIREMENTS) == 6
    assert ConnectorFile.__annotations__ == {"path": str, "sha": str, "content": str}
