from copy import deepcopy

from ejr_ambiguity_source_signature_census import summarize


def test_source_signature_census_is_deterministic_and_non_mutating():
    report = {
        "ambiguous_duplicate_records": {
            "EJR-003": [
                {"path": "a", "identity_source": "DOCUMENT_ID_FIELD"},
                {"path": "b", "identity_source": "DOCUMENT_ID_FIELD"},
            ],
            "EJR-026": [
                {"path": "c", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "d", "identity_source": "FIRST_H1_FALLBACK"},
                {"path": "e", "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "EJR-180": [
                {"path": "f", "identity_source": "DOCUMENT_ID_FIELD"},
                {"path": "g", "identity_source": "FIRST_H1_FALLBACK"},
            ],
            "NOVEL-999": [
                {"path": "h", "identity_source": "SYNTHETIC_SOURCE"},
                {"path": "i", "identity_source": "FIRST_H1_FALLBACK"},
            ],
        }
    }
    before = deepcopy(report)

    census = summarize(report)

    assert report == before
    assert census["total_ambiguous_groups"] == 4
    assert census["counts_by_signature"] == {
        "DOCUMENT_ID_FIELD_ONLY": 1,
        "FIRST_H1_FALLBACK_ONLY": 1,
        "MIXED": 1,
        "OTHER:FIRST_H1_FALLBACK+SYNTHETIC_SOURCE": 1,
    }
    assert census["counts_by_cardinality"] == {"2": 3, "3": 1}
    assert census["ejr"]["group_count"] == 3
    assert census["ejr"]["group_ids"] == ["EJR-003", "EJR-026", "EJR-180"]
    assert census["ejr"]["counts_by_signature"] == {
        "DOCUMENT_ID_FIELD_ONLY": 1,
        "FIRST_H1_FALLBACK_ONLY": 1,
        "MIXED": 1,
    }
    assert census["groups"]["EJR-026"]["cardinality"] == 3
    assert census["groups"]["EJR-180"]["source_counts"] == {
        "DOCUMENT_ID_FIELD": 1,
        "FIRST_H1_FALLBACK": 1,
    }
