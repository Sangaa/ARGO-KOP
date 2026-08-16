from pathlib import Path
import json

from canonical_spine_gap_map import SEAMS
from canonical_spine_integration_audit import audit


def build_consolidated_audit(root: Path) -> dict:
    result = audit(root)
    registry_path = root / "Quality/Integration/verified_seam_evidence_registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else {}
    evidence = result["evidence"]
    canonical = {f"{source} -> {destination}" for source, destination in SEAMS}
    connected = sorted(seam for seam, state in evidence.items() if seam in canonical and state == "CONNECTED")
    partial = sorted(seam for seam, state in evidence.items() if seam in canonical and state == "PARTIAL")
    missing = sorted(seam for seam, state in evidence.items() if seam in canonical and state == "MISSING")
    return {
        "seam_count": len(SEAMS),
        "connected": connected,
        "partial": partial,
        "missing": missing,
        "registry_records": len(registry.get("records", [])) if isinstance(registry, dict) else 0,
        "authorization_to_execution_governed": evidence.get("Authorization -> Execution") != "CONNECTED",
    }


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    print(json.dumps(build_consolidated_audit(root), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
