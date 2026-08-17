"""Validate the minimum semantic contract of a governed Mutation Matrix."""
from __future__ import annotations
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = ("KEEP REQUIREMENT", "Execution Evidence", "Closure")
REQUIRED_COLUMNS = ("Change ID", "Target", "Action", "Expected Content", "Applied", "Verified")
VALID_BOOL = {"Y", "N"}


def validate_matrix_text(text: str) -> list[str]:
    errors: list[str] = []
    if not re.search(r"^#\s+MUTATION MATRIX\b", text, re.MULTILINE):
        errors.append("missing MUTATION MATRIX title")
    if not re.search(r"^Transaction ID:\s*`MUT-[^`]+`", text, re.MULTILINE):
        errors.append("missing valid Transaction ID")
    if not re.search(r"^Protocol:\s*GOV-014\b", text, re.MULTILINE):
        errors.append("missing GOV-014 protocol declaration")

    table_header = next((line for line in text.splitlines() if line.startswith("|") and "Change ID" in line), None)
    if table_header is None:
        errors.append("missing change table header")
    else:
        for col in REQUIRED_COLUMNS:
            if col not in table_header:
                errors.append(f"missing required matrix column: {col}")
        lines = text.splitlines()
        idx = lines.index(table_header)
        rows: list[list[str]] = []
        for line in lines[idx + 2 :]:
            if not line.startswith("|"):
                if rows:
                    break
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 6:
                errors.append("matrix data row does not contain six cells")
                continue
            rows.append(cells)
        if not rows:
            errors.append("matrix contains no data rows")
        for n, cells in enumerate(rows, start=1):
            if not cells[0]: errors.append(f"row {n}: missing Change ID")
            if not cells[1]: errors.append(f"row {n}: missing Target")
            if not cells[2]: errors.append(f"row {n}: missing Action")
            if not cells[3]: errors.append(f"row {n}: missing Expected Content")
            if cells[4] not in VALID_BOOL: errors.append(f"row {n}: Applied must be Y or N")
            if cells[5] not in VALID_BOOL: errors.append(f"row {n}: Verified must be Y or N")

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+{re.escape(heading)}\b", text, re.MULTILINE):
            errors.append(f"missing required section: {heading}")
    if "KEEP" not in text:
        errors.append("missing KEEP preservation language")
    if "Post-write read-back" not in text and "Post-readback" not in text:
        errors.append("missing post-write/read-back evidence language")
    if "Unexpected Changes" not in text and "Unexpected changes" not in text:
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
            for error in errors: print(f" - {error}")
        else:
            print(f"SEMANTIC PASS: {path}")
    print(f"MUTATION_MATRIX_SEMANTICS={'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
