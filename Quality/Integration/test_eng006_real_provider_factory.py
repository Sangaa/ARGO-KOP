import pytest

from Services.ENG006_REAL_PROVIDER_FACTORY import build_real_eng006_consumer


def test_real_provider_factory_fails_closed_without_credentials(monkeypatch):
    for key in ("ARGO_GITHUB_OWNER", "ARGO_GITHUB_REPO", "ARGO_GITHUB_TOKEN"):
        monkeypatch.delenv(key, raising=False)
    with pytest.raises(Exception, match="GITHUB_CONNECTOR_CONFIGURATION_INCOMPLETE"):
        build_real_eng006_consumer()
