import hashlib

from Tools.P4_REL009_CONTROLLED_MUTATION import (
    NEW_ROW,
    NEW_SECTION,
    OLD_ROW,
    REL005_GUARD,
    REL061_GUARD,
    SECTION_END,
    SECTION_START,
    build_candidate,
)


def _blob_sha(text: str) -> str:
    raw = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def _source() -> str:
    return (
        "HEADER\n"
        + REL005_GUARD
        + "\nKEEP-BEFORE\n"
        + OLD_ROW
        + "\nKEEP-BETWEEN-ROW-AND-SECTION\n"
        + SECTION_START
        + "historical rel009 body\n"
        + SECTION_END
        + "REL061 BODY\n"
        + REL061_GUARD
        + "\nKEEP-TAIL\n"
    )


def test_rel009_builder_changes_only_authorized_row_and_section():
    source = _source()
    candidate = build_candidate(source, _blob_sha(source))

    assert OLD_ROW not in candidate
    assert candidate.count(NEW_ROW) == 1
    assert candidate.count(NEW_SECTION) == 1
    assert candidate.count(REL005_GUARD) == 1
    assert candidate.count(REL061_GUARD) == 1
    assert "KEEP-BEFORE\n" in candidate
    assert "KEEP-BETWEEN-ROW-AND-SECTION\n" in candidate
    assert candidate[candidate.index(SECTION_END):] == source[source.index(SECTION_END):]


def test_rel009_builder_rejects_stale_source_sha():
    source = _source()
    try:
        build_candidate(source, "0" * 40)
    except ValueError as exc:
        assert str(exc).startswith("SOURCE_BLOB_SHA_MISMATCH")
    else:
        raise AssertionError("expected stale source SHA rejection")


def test_rel009_builder_rejects_missing_preservation_guard():
    source = _source().replace(REL005_GUARD, "REL005-MISSING")
    try:
        build_candidate(source, _blob_sha(source))
    except ValueError as exc:
        assert str(exc) == "REL005_PRESERVATION_GUARD_FAILED"
    else:
        raise AssertionError("expected REL-005 preservation guard rejection")
