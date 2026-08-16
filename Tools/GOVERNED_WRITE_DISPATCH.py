"""HERMUZ governed write dispatcher.

This module separates write *dispatch* from the concrete repository connector.
The caller supplies a reader, updater, creator, and read-back verifier.

Rules enforced here:
- inspect existence before choosing Create vs Update;
- Update requires the current content/blob SHA;
- Create requires explicit importance and evidence proving why the new file is
  necessary;
- a create/update decision is never inferred from the intended filename alone;
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
    - Create is selected only after a confirmed not-found result.
    - Update is selected only when a current SHA exists.
    - A race where a new file appears between the existence probe and Create
      must surface as an error; the dispatcher never silently overwrites it.
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
        # New-file creation is a structural mutation. Its need must already
        # be evidenced; this dispatcher intentionally does not manufacture the
        # justification from the filename.
        commit_sha = create_file(
            intent.path,
            intent.content,
            intent.commit_message,
        )
        operation = "CREATE"
    else:
        commit_sha = update_file(
            intent.path,
            intent.content,
            intent.commit_message,
            current.sha,
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
