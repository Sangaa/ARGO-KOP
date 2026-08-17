from __future__ import annotations

from Tools.GOVERNED_WRITE_DISPATCH import (
    ExistingFile,
    FileImportance,
    WriteDispatchError,
    WriteIntent,
    dispatch_write,
)


def make_store() -> tuple[dict[str, ExistingFile], list[str]]:
    store = {}
    writes: list[str] = []

    def read_current(path: str):
        return store.get(path)

    def create_file(path: str, content: str, message: str) -> str:
        if path in store:
            raise AssertionError("CREATE_RACE")
        store[path] = ExistingFile(path, f"sha-create-{len(writes)}", content)
        writes.append(message)
        return f"commit-create-{len(writes)}"

    def update_file(path: str, content: str, message: str, sha: str) -> str:
        current = store[path]
        assert current.sha == sha
        store[path] = ExistingFile(path, f"sha-update-{len(writes)}", content)
        writes.append(message)
        return f"commit-update-{len(writes)}"

    def read_back(path: str) -> ExistingFile:
        return store[path]

    return store, writes, read_current, create_file, update_file, read_back


def test_dispatch_create_and_readback() -> None:
    store, writes, read_current, create_file, update_file, read_back = make_store()
    result = dispatch_write(
        WriteIntent(
            path="fixtures/p5/example.md",
            content="fixture-v1\n",
            commit_message="test create",
            purpose="P5 fixture create",
            importance=FileImportance.EXECUTABLE_TEST,
            necessity_evidence="P5 test matrix",
        ),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )
    assert result.operation == "CREATE"
    assert result.post_read_verified is True
    assert store["fixtures/p5/example.md"].content == "fixture-v1\n"
    assert writes == ["test create"]


def test_dispatch_update_uses_current_sha() -> None:
    store, writes, read_current, create_file, update_file, read_back = make_store()
    store["fixtures/p5/example.md"] = ExistingFile(
        "fixtures/p5/example.md", "source-sha", "fixture-v1\n"
    )
    result = dispatch_write(
        WriteIntent(
            path="fixtures/p5/example.md",
            content="fixture-v2\n",
            commit_message="test update",
            purpose="P5 fixture update",
            importance=FileImportance.EXECUTABLE_TEST,
            necessity_evidence="P5 test matrix",
        ),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )
    assert result.operation == "UPDATE"
    assert store["fixtures/p5/example.md"].content == "fixture-v2\n"
    assert writes == ["test update"]


def test_dispatch_rejects_missing_necessity_evidence() -> None:
    store, writes, read_current, create_file, update_file, read_back = make_store()
    del store, writes
    try:
        dispatch_write(
            WriteIntent(
                path="fixtures/p5/example.md",
                content="fixture\n",
                commit_message="bad",
                purpose="P5 fixture",
                importance=FileImportance.CONTROL_EVIDENCE,
                necessity_evidence="",
            ),
            read_current=read_current,
            create_file=create_file,
            update_file=update_file,
            read_back=read_back,
        )
    except WriteDispatchError as exc:
        assert str(exc) == "NECESSITY_EVIDENCE_REQUIRED"
    else:
        raise AssertionError("expected governed dispatch rejection")
