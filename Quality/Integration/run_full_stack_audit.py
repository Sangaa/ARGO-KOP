"""Execute the repository-wide connectivity audit and emit a deterministic report."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from full_stack_audit_report import classify_audit


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    report = classify_audit(root)
    report["repository_root"] = str(root)
    report["execution_contract"] = {
        "candidate_findings_are_not_architectural_proof": True,
        "negative_findings_require_independent_verification": True,
        "runtime_reachability_requires_runtime_evidence": True,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
