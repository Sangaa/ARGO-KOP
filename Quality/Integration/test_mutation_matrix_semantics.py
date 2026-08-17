from check_mutation_matrix_semantics import validate_matrix_text

VALID = '''# MUTATION MATRIX — TEST
Transaction ID: `MUT-TEST-001`
Target scope: test
Protocol: GOV-014 v1.0.1

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| TEST-001 | `Engine/ENG-TEST.md` | UPDATE | bounded test change | N | N |

## KEEP REQUIREMENT

All other content is `KEEP`.

## Execution Evidence

- Post-write read-back completed.
- Unexpected Changes = 0.

## Closure

`TEST TRANSACTION = CONTROLLED`.
'''

VALID_NO_ROWS = '''# MUTATION MATRIX — TEST
Transaction ID: `MUT-TEST-002`
Protocol: GOV-014 v1.0.1
| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
## KEEP REQUIREMENT
## Execution Evidence
## Closure
'''

INVALID_BOOL = '''# MUTATION MATRIX — TEST
Transaction ID: `MUT-TEST-003`
Protocol: GOV-014 v1.0.1
| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| TEST-003 | `Engine/ENG-TEST.md` | UPDATE | bounded test change | MAYBE | N |
## KEEP REQUIREMENT
KEEP
## Execution Evidence
Post-readback.
Unexpected Changes = 0.
## Closure
closed
'''


def test_valid_matrix_passes():
    assert validate_matrix_text(VALID) == []


def test_missing_rows_fail():
    errors = validate_matrix_text(VALID_NO_ROWS)
    assert "matrix contains no data rows" in errors


def test_invalid_boolean_fails():
    errors = validate_matrix_text(INVALID_BOOL)
    assert "row 1: Applied must be Y or N" in errors
