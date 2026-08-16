from pathlib import Path
import json

from canonical_spine_gap_map import SEAMS
from canonical_spine_integration_audit import audit
from verified_seam_evidence_loader import load_records

CANONICAL_SEAMS = {f"{source} -> {destination}" for source, destination in SEAMS}


def _load_verified_registry_records(root: Path) -> list[dict]:
    evidence_root = root / "Quality/Integration/evidence/runtime"
    records = []
    if not evidence_root.is_dir():
        return records
    for path in sorted(evidence_root.glob("*_verified_registry.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and "seam" in payload:
            if payload.get("seam") in CANONICAL_SEAMS:
                records.append(payload)
            continue
        if isinstance(payload, dict):
            for seam, record in payload.items():
                if seam not in CANONICAL_SEAMS or not isinstance(record, dict):
                    continue
                normalized = dict(record)
                normalized["seam"] = seam
                records.append(normalized)
    return records


def build_consolidated_audit(root: Path) -> dict:
    root = Path(root)
    registry_candidates = _load_verified_registry_records(root)
    verified_seams = load_records(root, registry_candidates) if registry_candidates else {}
    result = audit(root, verified_seams=verified_seams)
    evidence = result["evidence"]
    canonical = CANONICAL_SEAMS
    connected = sorted(seam for seam in canonical if evidence.get(seam) == "CONNECTED")
    partial = sorted(seam for seam in canonical if evidence.get(seam) == "PARTIAL")
    missing = sorted(seam for seam in canonical if evidence.get(seam) == "MISSING")
    governed = sorted(
        seam for seam in canonical if evidence.get(seam) in {"BLOCKED_BY_GOVERNANCE", "INTENTIONALLY_ISOLATED"}
    )
    authorization_state = evidence.get("Authorization -> Execution")
    return {
        "seam_count": len(SEAMS),
        "connected": connected,
        "partial": partial,
        "missing": missing,
        "governed_or_isolated": governed,
        "verified_registry_records_loaded": len(verified_seams),
        # A connected record here proves a governed, side-effect-bounded seam;
        # it does not imply autonomous real-world execution authority.
        "authorization_to_execution_governed": authorization_state == "CONNECTED",
    }


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    print(json.dumps(build_consolidated_audit(root), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
