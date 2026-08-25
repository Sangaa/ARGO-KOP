"""Non-production, side-effect-free INTF-006 seam fixture.

This fixture is intentionally synthetic. It does not access devices, sensors,
credentials, repositories, or runtime authority. It exists only to exercise
the INTF-006 contract boundary and make the missing production seam explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class SyntheticEnvironmentObservation:
    source_id: str
    values: Mapping[str, object]
    synthetic: bool = True


def build_synthetic_observation(
    *, source_id: str = "TEST-SYNTHETIC-INTF006", values: Mapping[str, object] | None = None
) -> SyntheticEnvironmentObservation:
    """Return a deterministic observation with no external side effects."""
    return SyntheticEnvironmentObservation(
        source_id=source_id,
        values=dict(values or {"test_signal": "synthetic"}),
    )
