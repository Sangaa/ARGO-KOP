"""Fail-closed EJR collision-safe allocation vacancy evidence.

This module does not allocate IDs. It proves whether a candidate EJR identity is
already occupied on current identity-bearing surfaces or reachable Git history.
A shallow repository can prove occupancy from visible evidence, but it cannot
prove vacancy and therefore fails closed.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

from internal_document_id_audit import (
    TEXT_SUFFIXES,
    _extract_heading_id,
    _extract_metadata_document_ids,
    _filename_prefix,
    _git_files,
)

EJR_ID_RE = re.compile(r"^EJR-\d{3}$", re.I)
DOCUMENT_TEXT_SUFFIXES = {".md", ".markdown", ".rst", ".txt"}


def normalize_candidate(raw: str) -> str:
    candidate = raw.strip().upper()
    if not EJR_ID_RE.fullmatch(candidate):
        raise ValueError(f"candidate must match EJR-NNN: {raw!r}")
    return candidate


def _git_text(root: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=root,
        stderr=subprocess.DEVNULL,
        text=True,
    )


def _git_bytes(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", *args],
        cwd=root,
        stderr=subprocess.DEVNULL,
    )


def _is_shallow(root: Path) -> bool:
    value = _git_text(root, "rev-parse", "--is-shallow-repository").strip().lower()
    return value == "true"


def _claim(surface: str, path: str, commit: str | None) -> dict[str, str | None]:
    return {"surface": surface, "path": path, "commit": commit}


def _current_claims(root: Path, candidate: str) -> list[dict[str, str | None]]:
    claims: list[dict[str, str | None]] = []

    for path in _git_files(root):
        relative = path.relative_to(root).as_posix()
        if _filename_prefix(Path(relative)) == candidate:
            claims.append(_claim("FILENAME_PREFIX", relative, "HEAD"))

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        if candidate in _extract_metadata_document_ids(text):
            claims.append(_claim("DOCUMENT_ID_FIELD", relative, "HEAD"))

        if path.suffix.lower() in DOCUMENT_TEXT_SUFFIXES and _extract_heading_id(text) == candidate:
            claims.append(_claim("FIRST_H1_IDENTITY", relative, "HEAD"))

    return _dedupe_claims(claims)


def _history_filename_claims(root: Path, candidate: str) -> list[dict[str, str | None]]:
    output = _git_text(
        root,
        "log",
        "--all",
        "--reverse",
        "--format=COMMIT:%H",
        "--name-only",
        "--",
    )
    claims: list[dict[str, str | None]] = []
    commit: str | None = None

    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("COMMIT:"):
            commit = line.split(":", 1)[1]
            continue
        if _filename_prefix(Path(line)) == candidate:
            claims.append(_claim("HISTORICAL_FILENAME_PREFIX", line, commit))

    return _dedupe_claims(claims)


def _history_content_claims(root: Path, candidate: str) -> list[dict[str, str | None]]:
    commits = [
        line.strip()
        for line in _git_text(
            root,
            "log",
            "--all",
            "--reverse",
            "--format=%H",
            "--pickaxe-all",
            "-S",
            candidate,
            "--",
        ).splitlines()
        if line.strip()
    ]
    claims: list[dict[str, str | None]] = []

    for commit in commits:
        changed_paths = [
            line.strip()
            for line in _git_text(
                root,
                "diff-tree",
                "--root",
                "--no-commit-id",
                "--name-only",
                "-r",
                commit,
            ).splitlines()
            if line.strip()
        ]
        for relative in changed_paths:
            suffix = Path(relative).suffix.lower()
            if suffix not in TEXT_SUFFIXES:
                continue
            try:
                text = _git_bytes(root, "show", f"{commit}:{relative}").decode(
                    "utf-8", errors="ignore"
                )
            except subprocess.CalledProcessError:
                continue

            if candidate in _extract_metadata_document_ids(text):
                claims.append(
                    _claim("HISTORICAL_DOCUMENT_ID_FIELD", relative, commit)
                )

            if suffix in DOCUMENT_TEXT_SUFFIXES and _extract_heading_id(text) == candidate:
                claims.append(
                    _claim("HISTORICAL_FIRST_H1_IDENTITY", relative, commit)
                )

    return _dedupe_claims(claims)


def _dedupe_claims(
    claims: list[dict[str, str | None]],
) -> list[dict[str, str | None]]:
    unique: dict[tuple[str | None, str | None], dict[str, str | None]] = {}
    for item in claims:
        key = (item["surface"], item["path"])
        unique.setdefault(key, item)
    return sorted(
        unique.values(),
        key=lambda item: (
            str(item["surface"] or ""),
            str(item["path"] or ""),
            str(item["commit"] or ""),
        ),
    )


def prove_vacancy(root: Path, raw_candidate: str) -> dict[str, object]:
    root = Path(root).resolve()
    candidate = normalize_candidate(raw_candidate)
    current_claims = _current_claims(root, candidate)
    shallow = _is_shallow(root)

    historical_claims: list[dict[str, str | None]] = []
    if not shallow:
        historical_claims = _dedupe_claims(
            _history_filename_claims(root, candidate)
            + _history_content_claims(root, candidate)
        )

    occupied = bool(current_claims or historical_claims)
    if occupied:
        decision = "OCCUPIED"
    elif shallow:
        decision = "HISTORY_INCOMPLETE"
    else:
        decision = "VACANT"

    return {
        "candidate": candidate,
        "decision": decision,
        "vacant": decision == "VACANT",
        "occupied": occupied,
        "history_complete": not shallow,
        "history_scope": "all locally reachable refs",
        "current_claims": current_claims,
        "historical_claims": historical_claims,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prove whether an EJR-NNN candidate is collision-safe to allocate."
    )
    parser.add_argument("candidate")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="repository root (default: current ARGO repository)",
    )
    args = parser.parse_args()

    try:
        report = prove_vacancy(args.root, args.candidate)
    except ValueError as exc:
        print(json.dumps({"decision": "INVALID_CANDIDATE", "error": str(exc)}, sort_keys=True))
        return 2

    print(json.dumps(report, indent=2, sort_keys=True))
    if report["decision"] == "VACANT":
        return 0
    if report["decision"] == "OCCUPIED":
        return 3
    return 4


if __name__ == "__main__":
    raise SystemExit(main())
