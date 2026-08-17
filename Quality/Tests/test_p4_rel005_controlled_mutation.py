from Tools.P4_REL005_CONTROLLED_MUTATION import (
    NEW_ROW,
    OLD_ROW,
    SECTION_END,
    SECTION_START,
    build_candidate,
)


def test_rel005_builder_changes_only_targeted_state():
    source = (
        "HEADER\n"
        + OLD_ROW
        + "\nKEEP-A\n"
        + SECTION_START
        + "old body\n"
        + SECTION_END
        + "KEEP-B\n"
        + "| REL-009 | RUN-010 | SRV-009 | CONSUMES | **REVALIDATION REQUIRED** |\n"
        + "| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |\n"
    )
    import hashlib

    raw = source.encode("utf-8")
    source_sha = hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
    candidate = build_candidate(source, source_sha)

    assert OLD_ROW not in candidate
    assert NEW_ROW in candidate
    assert "KEEP-A\n" in candidate
    assert "KEEP-B\n" in candidate
    assert candidate.count("| REL-009 | RUN-010 | SRV-009 | CONSUMES | **REVALIDATION REQUIRED** |") == 1
    assert candidate.count("| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |") == 1


def test_rel005_builder_rejects_wrong_sha():
    source = OLD_ROW + "\n" + SECTION_START + "x\n" + SECTION_END
    try:
        build_candidate(source, "0" * 40)
    except ValueError as exc:
        assert str(exc).startswith("SOURCE_BLOB_SHA_MISMATCH")
    else:
        raise AssertionError("expected source SHA guard to fail")
