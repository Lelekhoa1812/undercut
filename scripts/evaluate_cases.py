#!/usr/bin/env python3
"""Validate the Undercut behavioural case catalog (does not run a model)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

CASES = Path(__file__).resolve().parents[1] / "evaluation" / "cases.json"
VALID_KINDS = {"clarification", "small_change", "verification", "safety", "boundaries", "debugging", "sequence", "communication"}


def validate_cases(path: Path = CASES) -> list[str]:
    errors: list[str] = []
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"Cannot read evaluation cases: {exc}"]
    if not isinstance(cases, list) or not cases:
        return ["Evaluation catalog must be a nonempty JSON array"]
    seen: set[str] = set()
    for n, case in enumerate(cases, 1):
        if not isinstance(case, dict):
            errors.append(f"#{n}: expected JSON object")
            continue
        identifier = case.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"#{n}: missing id")
        elif identifier in seen:
            errors.append(f"#{n}: duplicate id {identifier}")
        else:
            seen.add(identifier)
        if case.get("kind") not in VALID_KINDS:
            errors.append(f"#{n}: unsupported kind {case.get('kind')}")
        for key in ("situation", "user_prompt", "ideal_behavior", "failure_signals"):
            val = case.get(key)
            if key == "failure_signals":
                if not isinstance(val, list) or not val or any(not isinstance(s, str) or not s for s in val):
                    errors.append(f"#{n}: failure_signals must be nonempty list of strings")
            elif not isinstance(val, str) or not val.strip():
                errors.append(f"#{n}: missing {key}")
        if not isinstance(case.get("question_expected"), bool):
            errors.append(f"#{n}: question_expected must be boolean")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check behavioural case catalog shape; no model is invoked")
    parser.add_argument("--check", action="store_true", help="validate data format")
    args = parser.parse_args()
    errors = validate_cases()
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    print(f"PASS: {len(cases)} structured evaluation scenarios (format only, not model compliance)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
