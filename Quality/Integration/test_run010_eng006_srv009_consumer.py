from dataclasses import dataclass

from Runtime.Execution.run010_eng006_srv009_consumer import dispatch_srv009_update


@dataclass
class FakeConnector:
    current = None
    calls: list[tuple] = None

    def __post_init__(self):
        self.calls = []

    def read_current(self, path):
        self.calls.append(("read_current", path))
        return self.current

    def create_file(self, path, content, commit_message):
        self.calls.append(("create_file", path, content, commit_message))
        self.current = type("F", (), {"path": path, "sha": "new-sha", "content": content})()
        return "commit-create"

    def update_file(self, path, content, commit_message, current_sha):
        self.calls.append(("update_file", path, content, commit_message, current_sha))
        self.current = type("F", (), {"path": path, "sha": "updated-sha", "content": content})()
        return "commit-update"

    def read_back(self, path):
        self.calls.append(("read_back", path))
        return self.current


def test_unauthorized_does_not_dispatch():
    connector = FakeConnector()
    result = dispatch_srv009_update(
        connector,
        path="Repository/test.txt",
        content="x",
        commit_message="test",
        authorized=False,
    )
    assert result.status == "REJECTED"
    assert connector.calls == []


def test_authorized_absent_target_dispatches_create_and_read_back():
    connector = FakeConnector()
    result = dispatch_srv009_update(
        connector,
        path="Repository/test.txt",
        content="x",
        commit_message="test",
        authorized=True,
    )
    assert result.status == "COMPLETED"
    assert result.commit_sha == "commit-create"
    assert [call[0] for call in connector.calls] == [
        "read_current",
        "create_file",
        "read_back",
    ]
