from __future__ import annotations

from Tools.GOVERNED_WRITE_DISPATCH import (
    ExistingFile,
    FileImportance,
    WriteDispatchError,
    WriteIntent,
    dispatch_write,
)


def make_store():
    store: dict[str, ExistingFile] = {}
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


def test_dispatch_aborts_when_state_changes_before_update() -> None:
    store, writes, _, create_file, update_file, read_back = make_store()
    path = "fixtures/p5/race.md"
    store[path] = ExistingFile(path, "source-sha", "fixture-v1\n")
    calls = 0

    def racing_reader(target: str):
        nonlocal calls
        calls += 1
        current = store.get(target)
        if calls == 2 and current is not None:
            store[target] = ExistingFile(target, "newer-sha", current.content)
        return store.get(target)

    try:
        dispatch_write(
            WriteIntent(
                path=path,
                content="fixture-v2\n",
                commit_message="race update",
                purpose="P5 stale-state regression",
                importance=FileImportance.EXECUTABLE_TEST,
                necessity_evidence="P5-T13 current-state recheck",
            ),
            read_current=racing_reader,
            create_file=create_file,
            update_file=update_file,
            read_back=read_back,
        )
    except WriteDispatchError as exc:
        assert str(exc) == "CURRENT_STATE_CHANGED_BEFORE_WRITE"
    else:
        raise AssertionError("expected stale-state write rejection")

    assert writes == []
    assert store[path].sha == "newer-sha"
    assert store[path].content == "fixture-v1\n"


def test_dispatch_aborts_when_file_appears_before_create() -> None:
    store, writes, _, create_file, update_file, read_back = make_store()
    path = "fixtures/p5/create-race.md"
    calls = 0

    def racing_reader(target: str):
        nonlocal calls
        calls += 1
        if calls == 2:
            store[target] = ExistingFile(target, "arrived-sha", "other-writer\n")
        return store.get(target)

    try:
        dispatch_write(
            WriteIntent(
                path=path,
                content="fixture-v1\n",
                commit_message="race create",
                purpose="P5 create race regression",
                importance=FileImportance.EXECUTABLE_TEST,
                necessity_evidence="P5-T13 current-state recheck",
            ),
            read_current=racing_reader,
            create_file=create_file,
            update_file=update_file,
            read_back=read_back,
        )
    except WriteDispatchError as exc:
        assert str(exc) == "CURRENT_STATE_CHANGED_BEFORE_WRITE"
    else:
        raise AssertionError("expected create-race rejection")

    assert writes == []
    assert store[path].content == "other-writer\n"


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
