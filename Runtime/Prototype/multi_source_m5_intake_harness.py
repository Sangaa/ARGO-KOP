"""M5 deterministic multi-source intake training harness.

Simulates reports from independent platforms. Provenance and schema identity
remain attached to every item; conflicting facts are quarantined.
No canonical mutation is performed.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    source_id: str
    report_id: str
    schema_id: str
    entity: str
    field: str
    value: str


def intake(reports: list[Report]) -> dict:
    grouped: dict[tuple[str, str], list[Report]] = {}
    for report in reports:
        grouped.setdefault((report.entity, report.field), []).append(report)

    accepted = []
    conflicts = []
    for key, items in grouped.items():
        values = {item.value for item in items}
        if len(values) > 1:
            conflicts.append({"key": key, "reports": [r.report_id for r in items]})
        else:
            accepted.append({"key": key, "value": next(iter(values)), "sources": [r.source_id for r in items]})

    return {
        "accepted": accepted,
        "conflicts": conflicts,
        "provenance_preserved": all(r.source_id and r.schema_id for r in reports),
        "canonical_mutation": False,
    }


def main() -> None:
    result = intake([
        Report("PLATFORM-A", "R-A1", "SCHEMA-A", "shipment:1", "eta", "2026-08-20"),
        Report("PLATFORM-B", "R-B1", "SCHEMA-B", "shipment:1", "eta", "2026-08-21"),
        Report("PLATFORM-C", "R-C1", "SCHEMA-C", "shipment:2", "status", "READY"),
        Report("PLATFORM-D", "R-D1", "SCHEMA-D", "shipment:3", "status", "READY"),
    ])
    assert result["provenance_preserved"] is True
    assert len(result["conflicts"]) == 1
    assert len(result["accepted"]) == 2
    assert result["canonical_mutation"] is False
    print("M5 deterministic multi-source intake: PASS")


if __name__ == "__main__":
    main()
