import pytest

from Tools.GOVERNED_WRITE_DISPATCH import (
    ExistingFile,
    FileImportance,
    WriteDispatchError,
    WriteIntent,
    dispatch_write,
)


def _intent(**overrides):
    values = {
        "path": "Repository/TEST_SAFE_WRITE.md",
        "content": "new content\n",
        "commit_message": "test: governed safe write",
        "purpose": "exercise create/update routing",
        "importance": FileImportance.EXECUTABLE_TEST,
        "necessity_evidence": "Dedicated regression test for create/update routing.",
    }
    values.update(overrides)
    return WriteIntent(**values)


def test_existing_file_routes_to_update_and_uses_current_sha():
    calls = []
    current = ExistingFile(
        path="Repository/TEST_SAFE_WRITE.md",
        sha="old-sha",
        content="old content\n",
    )

    def read_current(path):
        return current

    def create_file(*args):
        raise AssertionError("Create must not be called for an existing file")

    def update_file(path, content, message, sha):
        calls.append((path, content, message, sha))
        return "commit-update"

    def read_back(path):
        return ExistingFile(path=path, sha="new-sha", content="new content\n")

    result = dispatch_write(
        _intent(),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )

    assert result.operation == "UPDATE"
    assert result.post_read_verified is True
    assert calls == [
        (
            "Repository/TEST_SAFE_WRITE.md",
            "new content\n",
            "test: governed safe write",
            "old-sha",
        )
    ]


def test_missing_file_routes_to_create():
    calls = []

    def read_current(path):
        return None

    def create_file(path, content, message):
        calls.append((path, content, message))
        return "commit-create"

    def update_file(*args):
        raise AssertionError("Update must not be called for a missing file")

    def read_back(path):
        return ExistingFile(path=path, sha="new-sha", content="new content\n")

    result = dispatch_write(
        _intent(),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )

    assert result.operation == "CREATE"
    assert calls == [
        (
            "Repository/TEST_SAFE_WRITE.md",
            "new content\n",
            "test: governed safe write",
        )
    ]


def test_create_requires_necessity_evidence():
    with pytest.raises(WriteDispatchError, match="NECESSITY_EVIDENCE_REQUIRED"):
        dispatch_write(
            _intent(necessity_evidence=""),
            read_current=lambda path: None,
            create_file=lambda *args: "never",
            update_file=lambda *args: "never",
            read_back=lambda path: ExistingFile(path, "sha", "new content\n"),
        )


def test_readback_mismatch_is_a_hard_failure():
    with pytest.raises(WriteDispatchError, match="POST_WRITE_READBACK_MISMATCH"):
        dispatch_write(
            _intent(),
            read_current=lambda path: None,
            create_file=lambda *args: "commit-create",
            update_file=lambda *args: "never",
            read_back=lambda path: ExistingFile(path, "sha", "different\n"),
        )


def test_invalid_parent_traversal_is_rejected_before_io():
    with pytest.raises(WriteDispatchError, match="INVALID_REPOSITORY_PATH"):
        dispatch_write(
            _intent(path="../escape.md"),
            read_current=lambda path: (_ for _ in ()).throw(
                AssertionError("No repository access should occur")
            ),
            create_file=lambda *args: "never",
            update_file=lambda *args: "never",
            read_back=lambda path: ExistingFile(path, "sha", "new content\n"),
        )
