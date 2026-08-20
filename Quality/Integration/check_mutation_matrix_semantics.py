"""Validate the minimum semantic contract of a governed Mutation Matrix."""
from __future__ import annotations
import re
import sys
from pathlib import Path

REQUIRED_COLUMNS = ("Change ID", "Target", "Action", "Expected Content", "Applied", "Verified")
VALID_BOOL = {"Y", "N"}


def _heading_exists(text: str, heading: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(heading)}\b", text, re.MULTILINE | re.IGNORECASE))


def validate_matrix_text(text: str) -> list[str]:
    errors: list[str] = []
    if not re.search(r"^#\s+MUTATION MATRIX\b", text, re.MULTILINE | re.IGNORECASE):
        errors.append("missing MUTATION MATRIX title")
    if not re.search(r"^Transaction ID:\s*`MUT-[^`]+`", text, re.MULTILINE):
        errors.append("missing valid Transaction ID")

    # Current matrices declare GOV-014 explicitly. Older governed matrices may
    # predate the explicit Protocol field; retain validation for those artifacts
    # when their transaction evidence and boundary sections are present.
    explicit_protocol = bool(re.search(r"^Protocol:\s*GOV-014\b", text, re.MULTILINE))
    legacy_governed_shape = _heading_exists(text, "Boundary") and bool(
        re.search(r"^##\s+(Post-Commit Reconciliation|Execution Evidence)\b", text, re.MULTILINE | re.IGNORECASE)
    )
    if not explicit_protocol and not legacy_governed_shape:
        errors.append("missing GOV-014 protocol declaration or recognized legacy governed shape")

    table_header = next(
        (line for line in text.splitlines() if line.startswith("|") and "Change ID" in line),
        None,
    )
    if table_header is None:
        errors.append("missing change table header")
    else:
        header_cells = [c.strip() for c in table_header.strip().strip("|").split("|")]
        column_index = {name: header_cells.index(name) for name in REQUIRED_COLUMNS if name in header_cells}
        for col in REQUIRED_COLUMNS:
            if col not in column_index:
                errors.append(f"missing required matrix column: {col}")

        lines = text.splitlines()
        idx = lines.index(table_header)
        rows: list[list[str]] = []
        expected_width = len(header_cells)
        for line in lines[idx + 2 :]:
            if not line.startswith("|"):
                if rows:
                    break
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != expected_width:
                errors.append(f"matrix data row does not contain {expected_width} cells")
                continue
            rows.append(cells)

        if not rows:
            errors.append("matrix contains no data rows")
        else:
            for n, cells in enumerate(rows, start=1):
                for col in REQUIRED_COLUMNS:
                    if col not in column_index:
                        continue
                    value = cells[column_index[col]]
                    if col == "Change ID" and not value:
                        errors.append(f"row {n}: missing Change ID")
                    elif col == "Target" and not value:
                        errors.append(f"row {n}: missing Target")
                    elif col == "Action" and not value:
                        errors.append(f"row {n}: missing Action")
                    elif col == "Expected Content" and not value:
                        errors.append(f"row {n}: missing Expected Content")
                    elif col in {"Applied", "Verified"} and value not in VALID_BOOL:
                        errors.append(f"row {n}: {col} must be Y or N")

    keep_present = bool(re.search(r"\bKEEP\b", text, re.IGNORECASE))
    evidence_present = bool(
        re.search(r"Post[- ](?:write )?read[- ]?back|Post-commit read-back|Post-commit reconciliation", text, re.IGNORECASE)
    )
    unexpected_present = bool(
        re.search(r"Unexpected Changes|UNEXPECTED changes|UNEXPECTED CHANGES|UNEXPECTED_(?:ADDITIONS|DELETIONS)", text)
    )

    if not keep_present:
        errors.append("missing KEEP preservation language")
    if not evidence_present:
        errors.append("missing post-write/read-back evidence language")
    if not unexpected_present:
        errors.append("missing Unexpected Changes preservation control")

    return errors


def validate_path(path: str) -> list[str]:
    return validate_matrix_text(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: check_mutation_matrix_semantics.py <matrix> [...]", file=sys.stderr)
        return 2
    failed = False
    for path in argv:
        errors = validate_path(path)
        if errors:
            failed = True
            print(f"SEMANTIC FAIL: {path}")
            for error in errors:
                print(f" - {error}")
        else:
            print(f"SEMANTIC PASS: {path}")
    print(f"MUTATION_MATRIX_SEMANTICS={'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
