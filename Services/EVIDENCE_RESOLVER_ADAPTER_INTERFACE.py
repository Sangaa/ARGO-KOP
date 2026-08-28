"""Provider-neutral external evidence resolver adapter interface.

The interface defines a governed acquisition boundary. Implementing this
protocol does not confer authority or prove upstream provider authenticity.
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
