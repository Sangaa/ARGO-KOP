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
        "path": "Repository/P391_TEST_SAFE_WRITE.md",
        "content": "new content\n",
        "commit_message": "test: P391 B07 matrix gap resolution",
        "purpose": "exercise previously unmapped governed write invariants",
        "importance": FileImportance.EXECUTABLE_TEST,
        "necessity_evidence": "Focused regression coverage for explicit B07 dispatcher branches.",
    }
    values.update(overrides)
    return WriteIntent(**values)


def test_write_purpose_is_required_before_repository_io():
    with pytest.raises(WriteDispatchError, match="WRITE_PURPOSE_REQUIRED"):
        dispatch_write(
            _intent(purpose="   "),
            read_current=lambda path: (_ for _ in ()).throw(
                AssertionError("No repository access before purpose validation")
            ),
            create_file=lambda *args: "never",
            update_file=lambda *args: "never",
            read_back=lambda path: ExistingFile(path, "sha", "new content\n"),
        )


def test_commit_message_is_required_before_repository_io():
    with pytest.raises(WriteDispatchError, match="COMMIT_MESSAGE_REQUIRED"):
        dispatch_write(
            _intent(commit_message=""),
            read_current=lambda path: (_ for _ in ()).throw(
                AssertionError("No repository access before commit-message validation")
            ),
            create_file=lambda *args: "never",
            update_file=lambda *args: "never",
            read_back=lambda path: ExistingFile(path, "sha", "new content\n"),
        )


def test_update_aborts_when_file_disappears_at_write_boundary():
    states = iter([
        ExistingFile("Repository/P391_TEST_SAFE_WRITE.md", "sha-1", "old\n"),
        None,
    ])

    def read_current(path):
        return next(states)

    with pytest.raises(WriteDispatchError, match="CURRENT_STATE_CHANGED_BEFORE_WRITE"):
        dispatch_write(
            _intent(),
            read_current=read_current,
            create_file=lambda *args: "never",
            update_file=lambda *args: (_ for _ in ()).throw(
                AssertionError("Update must not occur after file disappears")
            ),
            read_back=lambda path: ExistingFile(path, "sha", "new content\n"),
        )


def test_create_reports_explicit_post_read_persistence_verification():
    result = dispatch_write(
        _intent(),
        read_current=lambda path: None,
        create_file=lambda *args: "commit-create",
        update_file=lambda *args: "never",
        read_back=lambda path: ExistingFile(path, "created-sha", "new content\n"),
    )

    assert result.operation == "CREATE"
    assert result.commit_sha == "commit-create"
    assert result.post_read_verified is True
