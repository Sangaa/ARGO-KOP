"""Provider-neutral external evidence resolver adapter interfaces.

The interfaces define governed acquisition boundaries. Implementing either
protocol does not confer authority or prove upstream provider authenticity.
Participant/attestation acquisition remains semantically separate from generic
quarantine-artifact re-acquisition.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class EvidenceResolverAdapterError(RuntimeError):
    """Explicit adapter/acquisition failure; callers must not infer success."""


@dataclass(frozen=True)
class ResolverAdapterIdentity:
    adapter_id: str
    adapter_kind: str
    implementation_id: str


@dataclass(frozen=True)
class ResolverAcquisition:
    adapter_id: str
    adapter_kind: str
    acquisition_id: str
    acquisition_surface: str
    started_at: str
    completed_at: str
    requested_ref: str
    observation: dict[str, Any]


class EvidenceResolverAdapter(Protocol):
    @property
    def identity(self) -> ResolverAdapterIdentity:
        """Return immutable adapter identity metadata."""

    def acquire_participant(self, evidence_ref: str) -> ResolverAcquisition:
        """Acquire participant execution evidence for the exact requested ref."""

    def acquire_attestation(self, evidence_ref: str) -> ResolverAcquisition:
        """Acquire independence-attestation evidence for the exact requested ref."""


class QuarantineEvidenceResolverAdapter(Protocol):
    """Generic re-acquisition protocol for one exact quarantined source ref.

    This protocol exists because an arbitrary quarantined artifact is not
    necessarily participant evidence or an independence attestation. A caller
    must not route generic evidence through those narrower channels merely to
    reuse an existing interface.
    """

    @property
    def identity(self) -> ResolverAdapterIdentity:
        """Return immutable adapter identity metadata."""

    def acquire_external(self, evidence_ref: str) -> ResolverAcquisition:
        """Re-acquire the exact external JSON value for the requested ref."""


PRODUCTION_RESOLVER_ADAPTER_REQUIREMENTS = (
    "immutable adapter identity",
    "explicit participant/attestation acquisition separation",
    "exact requested-reference binding",
    "explicit acquisition identity and surface",
    "explicit acquisition start/end timestamps",
    "explicit adapter failure states",
    "no authority inference from technical access",
    "no provider-authenticity inference from protocol conformance alone",
)

QUARANTINE_RESOLVER_ADAPTER_REQUIREMENTS = (
    "immutable adapter identity",
    "generic external acquisition kept separate from participant/attestation semantics",
    "exact requested-reference binding",
    "raw JSON value preserved without semantic promotion",
    "explicit acquisition identity and surface",
    "explicit acquisition start/end timestamps",
    "explicit unavailable/failure behavior",
    "no provider-authenticity inference from successful re-acquisition",
    "no authority inference from technical access",
)
