"""P5 model-independent controlled mutation harness.

Builds and validates a complete candidate from an authoritative source plus a
Mutation Matrix, then delegates the actual repository write to the governed
write dispatcher. Canonical files are not touched by this module during tests.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re
from typing import Iterable, Mapping


class HarnessError(RuntimeError):
    pass


@dataclass(frozen=True)
class Section:
    section_id: str
    order: int
    heading: str
    content: str
    sha256: str


@dataclass(frozen=True)
class Mutation:
    change_id: str
    section_id: str
    action: str
    expected_content: str | None = None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sectionize(markdown: str) -> list[Section]:
    """Split by stable level-2 headings while preserving exact section text."""
    matches = list(re.finditer(r"(?m)^## (.+)$", markdown))
    sections: list[Section] = []
    for index, match in enumerate(matches, start=1):
        end = matches[index].start() if index < len(matches) else len(markdown)
        content = markdown[match.start():end]
        heading = match.group(1).strip()
        sections.append(
            Section(
                section_id=f"SEC-{index:03d}",
                order=index,
                heading=heading,
                content=content,
                sha256=sha256_text(content),
            )
        )
    if not sections:
        raise HarnessError("SOURCE-INCOMPLETE: no sections detected")
    return sections


def build_section_matrix(source: str) -> list[Section]:
    if not source:
        raise HarnessError("SOURCE-INCOMPLETE")
    return sectionize(source)


def build_candidate(source: str, mutations: Iterable[Mutation]) -> tuple[str, dict[str, object]]:
    """Build from the full source and enforce zero-touch preservation."""
    source_sections = build_section_matrix(source)
    mutation_map: Mapping[str, Mutation] = {m.section_id: m for m in mutations}
    by_id = {section.section_id: section for section in source_sections}

    unknown = sorted(set(mutation_map) - set(by_id))
    if unknown:
        raise HarnessError(f"IDENTITY/AUTHORITY-GAP: unknown sections={unknown}")

    candidate = source
    changed = []

    # P5 v1 intentionally supports UPDATE only. ADD/REMOVE should be introduced
    # after the same preservation rules are separately tested.
    for section in reversed(source_sections):
        mutation = mutation_map.get(section.section_id)
        if mutation is None or mutation.action == "KEEP":
            continue
        if mutation.action != "UPDATE" or mutation.expected_content is None:
            raise HarnessError(f"UNSUPPORTED_ACTION: {mutation.action}")
        candidate = candidate[:]
        old = section.content
        if candidate.count(old) != 1:
            raise HarnessError(f"SECTION_BOUNDARY_AMBIGUOUS: {section.section_id}")
        candidate = candidate.replace(old, mutation.expected_content, 1)
        changed.append(section.section_id)

    candidate_sections = build_section_matrix(candidate)
    if [s.heading for s in source_sections] != [s.heading for s in candidate_sections]:
        raise HarnessError("UNEXPECTED-CHANGE: section order or headings changed")

    candidate_by_id = {s.section_id: s for s in candidate_sections}
    keep_mismatches = []
    for section in source_sections:
        mutation = mutation_map.get(section.section_id)
        if mutation is None or mutation.action == "KEEP":
            if section.sha256 != candidate_by_id[section.section_id].sha256:
                keep_mismatches.append(section.section_id)

    if keep_mismatches:
        raise HarnessError(f"KEEP-MISMATCH: {keep_mismatches}")

    unexpected = set(changed) - set(mutation_map)
    if unexpected:
        raise HarnessError(f"UNEXPECTED-CHANGE: {sorted(unexpected)}")

    report = {
        "source_sha256": sha256_text(source),
        "candidate_sha256": sha256_text(candidate),
        "source_section_count": len(source_sections),
        "candidate_section_count": len(candidate_sections),
        "changed_sections": sorted(changed),
        "keep_mismatches": keep_mismatches,
        "unexpected_changes": 0,
        "status": "PRE_COMMIT_VALIDATED",
    }
    return candidate, report
