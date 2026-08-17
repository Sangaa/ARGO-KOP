from __future__ import annotations

from dataclasses import dataclass

import pytest

from Runtime.Prototype.ENG006_SRV009_ADAPTER_CONTRACT import (
    PrototypeExecutionCandidate,
    execute_prototype_candidate,
)
from Tools.GOVERNED_WRITE_DISPATCH import ExistingFile


@dataclass
class InMemoryRepo:
    content: dict[str, str]

    def read(self, path: str):
        if path not in self.content:
            return None
        return ExistingFile(path=path, sha=f"sha:{path}", content=self.content[path])

    def create(self, path: str, content: str, message: str) -> str:
        if path in self.content:
            raise RuntimeError("ALREADY_EXISTS")
        self.content[path] = content
        return "commit:create"

    def update(self, path: str, content: str, message: str, sha: str) -> str:
        if path not in self.content:
            raise RuntimeError("NOT_FOUND")
        self.content[path] = content
        return "commit:update"

    def read_back(self, path: str) -> ExistingFile:
        if path not in self.content:
            raise RuntimeError("NOT_FOUND")
        return ExistingFile(path=path, sha=f"sha:{path}", content=self.content[path])


def test_prototype_adapter_dispatches_authorized_candidate_and_reads_back() -> None:
    repo = InMemoryRepo(content={})
    result = execute_prototype_candidate(
        PrototypeExecutionCandidate(
            path="Repository/TEST-P3.md",
            content="# P3 TEST\n",
            purpose="Prototype execution seam validation",
            necessity_evidence="P3 executable boundary evidence",
            commit_message="test: prototype ENG-006 to write dispatcher",
            authorized=True,
        ),
        read_current=repo.read,
        create_file=repo.create,
        update_file=repo.update,
        read_back=repo.read_back,
    )

    assert result.operation == "CREATE"
    assert result.post_read_verified is True
    assert repo.content["Repository/TEST-P3.md"] == "# P3 TEST\n"


def test_prototype_adapter_rejects_unauthorized_candidate() -> None:
    repo = InMemoryRepo(content={})
    with pytest.raises(ValueError, match="EXECUTION_NOT_AUTHORIZED"):
        execute_prototype_candidate(
            PrototypeExecutionCandidate(
                path="Repository/TEST-P3.md",
                content="# P3 TEST\n",
                purpose="Prototype execution seam validation",
                necessity_evidence="P3 executable boundary evidence",
                commit_message="test: unauthorized candidate",
                authorized=False,
            ),
            read_current=repo.read,
            create_file=repo.create,
            update_file=repo.update,
            read_back=repo.read_back,
        )
