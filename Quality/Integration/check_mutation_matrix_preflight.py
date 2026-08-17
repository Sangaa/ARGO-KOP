"""Detect high-risk repository mutations that lack an accompanying Matrix.

The gate is intentionally conservative: canonical Runtime/Engine/Service/Repository
artifacts require a Mutation Matrix in the same change set. Documentation, tests,
CI, templates, EJR/session records, and existing Matrix files are exempt.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import PurePosixPath

EXEMPT_PREFIXES = (
    "EJR/",
    "Quality/",
    "Templates/",
    ".github/",
    "Docs/",
)
CANONICAL_PREFIXES = (
    "Engine/",
    "Services/",
    "Runtime/",
    "Repository/REP-",
    "Interfaces/",
    "Cognition/COG-",
    "Decision/",
    "Memory/",
)
MATRIX_MARKERS = ("MUT-", "MUTATION_MATRIX")


def changed_files(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def is_matrix(path: str) -> bool:
    return any(marker in PurePosixPath(path).name for marker in MATRIX_MARKERS)


def requires_matrix(path: str) -> bool:
    if path.startswith(EXEMPT_PREFIXES) or is_matrix(path):
        return False
    return path.startswith(CANONICAL_PREFIXES)


def evaluate(files: list[str]) -> tuple[list[str], list[str]]:
    protected = [p for p in files if requires_matrix(p)]
    matrices = [p for p in files if is_matrix(p)]
    return protected, matrices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("head")
    args = parser.parse_args()

    files = changed_files(args.base, args.head)
    protected, matrices = evaluate(files)

    print(f"changed_files={len(files)}")
    print(f"protected_changes={len(protected)}")
    print(f"mutation_matrices={len(matrices)}")
    for path in protected:
        print(f"PROTECTED: {path}")
    for path in matrices:
        print(f"MATRIX: {path}")

    if protected and not matrices:
        print("MUTATION_MATRIX_PREFLIGHT=FAIL")
        return 1

    print("MUTATION_MATRIX_PREFLIGHT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
