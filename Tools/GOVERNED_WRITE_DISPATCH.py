"""HERMUZ governed write dispatcher.

This module separates write *dispatch* from the concrete repository connector.
The caller supplies a reader, updater, creator, and read-back verifier.

Rules enforced here:
- inspect existence before choosing Create vs Update;
- Update requires the current content/blob SHA;
- Create requires explicit importance and evidence proving why the new file is
  necessary;
- a create/update decision is never inferred from the intended filename alone;
- the current repository state is re-read immediately before write so a race
  after candidate validation cannot turn a stale transaction into a write;
- after mutation, the caller must perform a read-back and verify the resulting
  content before the mutation is considered persisted.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional, Protocol


class WriteDispatchError(RuntimeError):
    """Raised when the governed write sequence cannot safely continue."""


class FileImportance(str, Enum):
    CANONICAL = "CANONICAL"
    CONTROL_EVIDENCE = "CONTROL_EVIDENCE"
    EXECUTABLE_TEST = "EXECUTABLE_TEST"
    REPOSITORY_EVIDENCE = "REPOSITORY_EVIDENCE"
    SESSION_CHECKPOINT = "SESSION_CHECKPOINT"
    SUPPORTING = "SUPPORTING"


@dataclass(frozen=True)
class ExistingFile:
    path: str
    sha: str
    content: str


@dataclass(frozen=True)
class WriteIntent:
    path: str
    content: str
    commit_message: str
    purpose: str
    importance: FileImportance
    necessity_evidence: str
    canonical_scope: bool = False


@dataclass(frozen=True)
class WriteResult:
    operation: str
    path: str
    commit_sha: str
    post_read_verified: bool


class RepositoryReader(Protocol):
    def __call__(self, path: str) -> Optional[ExistingFile]:
        """Return current file or None only for a confirmed 404/not-found."""


class RepositoryWriter(Protocol):
    def __call__(self, path: str, content: str, message: str) -> str:
        """Create a new file and return its commit SHA."""


class RepositoryUpdater(Protocol):
    def __call__(self, path: str, content: str, message: str, sha: str) -> str:
        """Update an existing file and return its commit SHA."""


class RepositoryReadBack(Protocol):
    def __call__(self, path: str) -> ExistingFile:
        """Read the file after mutation."""


def dispatch_write(
    intent: WriteIntent,
    *,
    read_current: RepositoryReader,
    create_file: RepositoryWriter,
    update_file: RepositoryUpdater,
    read_back: RepositoryReadBack,
) -> WriteResult:
    """Choose Create or Update from current repository state, then verify it.

    Safety properties:
    - Create is selected only after a confirmed not-found result and a second
      existence probe immediately before the write.
    - Update is selected only when a current SHA exists, and the same SHA is
      confirmed immediately before the write.
    - A race where repository state changes between probes aborts the write;
      the dispatcher never silently writes a stale transaction.
    - Post-mutation read-back is mandatory and content must match exactly.
    """
    if not intent.path or intent.path.startswith("/") or ".." in intent.path.split("/"):
        raise WriteDispatchError("INVALID_REPOSITORY_PATH")
    if not intent.content.strip():
        raise WriteDispatchError("EMPTY_WRITE_CONTENT")
    if not intent.purpose.strip():
        raise WriteDispatchError("WRITE_PURPOSE_REQUIRED")
    if not intent.commit_message.strip():
        raise WriteDispatchError("COMMIT_MESSAGE_REQUIRED")

    if intent.importance in {
        FileImportance.CANONICAL,
        FileImportance.CONTROL_EVIDENCE,
        FileImportance.EXECUTABLE_TEST,
        FileImportance.REPOSITORY_EVIDENCE,
        FileImportance.SESSION_CHECKPOINT,
    } and not intent.necessity_evidence.strip():
        raise WriteDispatchError("NECESSITY_EVIDENCE_REQUIRED")

    current = read_current(intent.path)

    if current is None:
        # Re-check immediately before CREATE. A successful candidate build is
        # not proof that the path is still absent on the live repository.
        pre_write = read_current(intent.path)
        if pre_write is not None:
            raise WriteDispatchError("CURRENT_STATE_CHANGED_BEFORE_WRITE")
        commit_sha = create_file(
            intent.path,
            intent.content,
            intent.commit_message,
        )
        operation = "CREATE"
    else:
        # Re-check immediately before UPDATE. The expected SHA must still be
        # the live SHA at the write boundary, not merely the SHA used to build
        # the candidate earlier in the transaction.
        pre_write = read_current(intent.path)
        if pre_write is None:
            raise WriteDispatchError("CURRENT_STATE_CHANGED_BEFORE_WRITE")
        if pre_write.sha != current.sha:
            raise WriteDispatchError("CURRENT_STATE_CHANGED_BEFORE_WRITE")
        commit_sha = update_file(
            intent.path,
            intent.content,
            intent.commit_message,
            pre_write.sha,
        )
        operation = "UPDATE"

    verified = read_back(intent.path)
    if verified.content != intent.content:
        raise WriteDispatchError("POST_WRITE_READBACK_MISMATCH")

    return WriteResult(
        operation=operation,
        path=intent.path,
        commit_sha=commit_sha,
        post_read_verified=True,
    )