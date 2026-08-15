"""Emit one real runtime-produced evidence record for CI inspection.

The artifact is created in the governed runtime-evidence target inside the CI
workspace and uploaded as workflow evidence. It is intentionally not committed
or promoted to the canonical registry by this script.
"""

import json
from pathlib import Path

from connected_spine_runner import run
from runtime_evidence_capture import capture_repository_evidence
from synthetic_task_fixture import make_fixture


def main() -> int:
    repository_root = Path(__file__).resolve().parents[2]
    result = run(make_fixture())
    captured = capture_repository_evidence(
        result,
        str(repository_root),
        "ci_connected_spine_execution_trace.json",
    )
    print(json.dumps(captured, sort_keys=True))
    if captured.get("status") != "CAPTURED":
        return 1
    target = repository_root / captured["repository_relative_path"]
    return 0 if target.exists() else 1


if __name__ == "__main__":
    raise SystemExit(main())
