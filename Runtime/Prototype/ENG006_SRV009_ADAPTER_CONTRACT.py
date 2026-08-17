"""Prototype-only bridge for the ENG-006 -> governed write-dispatch seam.

This module intentionally does not provide production SRV-009 implementation.
It proves only that an authorized execution candidate can be translated into
an explicit governed write intent and dispatched through the existing
GOVERNED_WRITE_DISPATCH seam under a caller-supplied repository connector.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from Tools.GOVERNED_WRITE_DISPATCH import (
    FileImportance,
    WriteIntent,
    WriteResult,
    dispatch_write,
)


@dataclass(frozen=True)
class PrototypeExecutionCandidate:
    path: str
    content: str
    purpose: str
    necessity_evidence: str
    commit_message: str
    authorized: bool


def execute_prototype_candidate(
    candidate: PrototypeExecutionCandidate,
    *,
    read_current: Callable[..., Any],
    create_file: Callable[..., str],
    update_file: Callable[..., str],
    read_back: Callable[..., Any],
) -> WriteResult:
    """Dispatch an authorized candidate through the governed write seam.

    This is a prototype boundary test only. It must not be treated as
    production SRV-009 authority or as proof of runtime architectural closure.
    """
    if not candidate.authorized:
        raise ValueError("EXECUTION_NOT_AUTHORIZED")

    intent = WriteIntent(
        path=candidate.path,
        content=candidate.content,
        commit_message=candidate.commit_message,
        purpose=candidate.purpose,
        importance=FileImportance.REPOSITORY_EVIDENCE,
        necessity_evidence=candidate.necessity_evidence,
        canonical_scope=False,
    )

    return dispatch_write(
        intent,
        read_current=read_current,
        create_file=create_file,
        update_file=update_file,
        read_back=read_back,
    )
