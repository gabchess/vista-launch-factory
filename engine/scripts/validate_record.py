#!/usr/bin/env python3
# STRUCTURAL_INTEGRITY_ONLY — validates a release-record against
# release-record.schema.json plus authority gates. Never publishes, never
# mutates the record, never substitutes for Barry's human judgment.
"""validate_record RECORD

Schema check + authority gates:
- no slot may be `approved` or `packaged` without a recorded Barry gate entry
  (gate `slot-N`, decided_by barry, decision approve);
- `claims_lock.state == locked_by_barry` requires a locked_at timestamp and a
  recorded Barry gate entry (gate `claims_lock`, decision approve).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "release-record.schema.json"


def _barry_approved(gates: list[dict[str, Any]], gate: str) -> bool:
    return any(
        isinstance(g, dict)
        and g.get("gate") == gate
        and g.get("decided_by") == "barry"
        and g.get("decision") == "approve"
        for g in gates
    )


def validate_record(record: dict[str, Any], *, schema_path: Path | None = None) -> dict[str, Any]:
    errors: list[str] = []
    path = schema_path or SCHEMA_PATH
    schema = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
        errors.append(f"schema: {err.message}")

    gates = record.get("gates") or []

    lock = record.get("claims_lock") or {}
    if lock.get("state") == "locked_by_barry":
        if not lock.get("locked_at"):
            errors.append("claims_lock locked_by_barry without locked_at timestamp")
        if not _barry_approved(gates, "claims_lock"):
            errors.append(
                "authority: claims_lock locked_by_barry without a recorded Barry "
                "gate entry (gate=claims_lock, decided_by=barry, decision=approve)"
            )

    for slot in record.get("slots") or []:
        if not isinstance(slot, dict):
            continue
        state = slot.get("state")
        n = slot.get("slot")
        if state in ("approved", "packaged"):
            if not _barry_approved(gates, f"slot-{n}"):
                errors.append(
                    f"authority: slot {n} is `{state}` without a recorded Barry gate "
                    f"entry (gate=slot-{n}, decided_by=barry, decision=approve) — "
                    "the writer seat never self-approves"
                )
        if state == "held" and not slot.get("hold_reason"):
            errors.append(f"slot {n} held without hold_reason")

    # allowed claims must carry evidence spans
    for claim in (record.get("claims") or {}).get("allowed") or []:
        if isinstance(claim, dict) and not claim.get("evidence"):
            errors.append(f"claim {claim.get('claim_id')} allowed without evidence span")

    return {"ok": len(errors) == 0, "errors": errors}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a release-record JSON")
    parser.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    record = json.loads(args.record.read_text(encoding="utf-8"))
    result = validate_record(record)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
