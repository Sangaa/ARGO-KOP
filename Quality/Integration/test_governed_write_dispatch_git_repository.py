import subprocess
from pathlib import Path

from Tools.GOVERNED_WRITE_DISPATCH import ExistingFile, FileImportance, WriteIntent, dispatch_write


def _git(cwd: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=cwd, text=True).strip()


def _make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.name", "ARGO Test")
    _git(repo, "config", "user.email", "argo-test@example.invalid")
    return repo


def _adapter(repo: Path):
    def _abs(path: str) -> Path:
        candidate = repo / path
        if candidate.resolve().parent != repo.resolve() and repo.resolve() not in candidate.resolve().parents:
            raise AssertionError("path escaped temporary repository")
        return candidate

    def read_current(path: str):
        target = _abs(path)
        if not target.exists():
            return None
        sha = _git(repo, "hash-object", str(target.relative_to(repo)))
        return ExistingFile(path=path, sha=sha, content=target.read_text())

    def create_file(path: str, content: str, message: str) -> str:
        target = _abs(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise RuntimeError("RACE_EXISTING_FILE")
        target.write_text(content)
        _git(repo, "add", path)
        _git(repo, "commit", "-q", "-m", message)
        return _git(repo, "rev-parse", "HEAD")

    def update_file(path: str, content: str, message: str, sha: str) -> str:
        target = _abs(path)
        if not target.exists():
            raise RuntimeError("MISSING_FILE_ON_UPDATE")
        current_sha = _git(repo, "hash-object", str(target.relative_to(repo)))
        if current_sha != sha:
            raise RuntimeError("STALE_CONTENT_SHA")
        target.write_text(content)
        _git(repo, "add", path)
        _git(repo, "commit", "-q", "-m", message)
        return _git(repo, "rev-parse", "HEAD")

    def read_back(path: str):
        result = read_current(path)
        if result is None:
            raise AssertionError("POST_WRITE_FILE_MISSING")
        return result

    return read_current, create_file, update_file, read_back


def test_governed_dispatch_real_git_create_then_update(tmp_path):
    repo = _make_repo(tmp_path)
    read_current, create_file, update_file, read_back = _adapter(repo)
    path = "Repository/TEST_SAFE_WRITE.md"

    create_result = dispatch_write(
        WriteIntent(
            path=path,
            content="v1\n",
            commit_message="test: create governed file",
            purpose="real git repository integration coverage",
            importance=FileImportance.EXECUTABLE_TEST,
            necessity_evidence="Temporary integration fixture only.",
        ),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )

    assert create_result.operation == "CREATE"
    assert create_result.post_read_verified is True
    assert _git(repo, "log", "-1", "--format=%s") == "test: create governed file"

    update_result = dispatch_write(
        WriteIntent(
            path=path,
            content="v2\n",
            commit_message="test: update governed file",
            purpose="real git repository integration coverage",
            importance=FileImportance.EXECUTABLE_TEST,
            necessity_evidence="Temporary integration fixture only.",
        ),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )

    assert update_result.operation == "UPDATE"
    assert update_result.post_read_verified is True
    assert (repo / path).read_text() == "v2\n"
    assert _git(repo, "log", "--oneline") .count("test:") == 2


def test_governed_dispatch_real_git_rejects_stale_sha(tmp_path):
    repo = _make_repo(tmp_path)
    read_current, create_file, update_file, read_back = _adapter(repo)
    path = "Repository/TEST_SAFE_WRITE.md"

    dispatch_write(
        WriteIntent(
            path=path,
            content="v1\n",
            commit_message="test: create governed file",
            purpose="real git repository integration coverage",
            importance=FileImportance.EXECUTABLE_TEST,
            necessity_evidence="Temporary integration fixture only.",
        ),
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )

    stale = ExistingFile(path=path, sha="definitely-stale", content="v1\n")
    assert stale.sha != read_current(path).sha

    try:
        update_file(path, "v2\n", "test: stale update must fail", stale.sha)
    except RuntimeError as exc:
        assert str(exc) == "STALE_CONTENT_SHA"
    else:
        raise AssertionError("stale SHA was incorrectly accepted")
