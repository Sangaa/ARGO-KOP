"""Run semantic validation against the versioned real Matrix corpus."""
from pathlib import Path
import subprocess
import sys

CORPUS = [
    "Repository/MUT-2026-08-17-REP001-001_MUTATION_MATRIX.md",
    "Repository/MUT-2026-08-17-REP001-002_MUTATION_MATRIX.md",
    "Repository/MUT-2026-08-17-AUDIT-RECON-001_MUTATION_MATRIX.md",
]


def main() -> int:
    print(f"REAL_MATRIX_CORPUS_COUNT={len(CORPUS)}")
    missing = [path for path in CORPUS if not Path(path).is_file()]
    if missing:
        for path in missing:
            print(f"CORPUS MISSING: {path}")
        return 2
    result = subprocess.run(
        [sys.executable, "Quality/Integration/check_mutation_matrix_semantics.py", *CORPUS],
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
