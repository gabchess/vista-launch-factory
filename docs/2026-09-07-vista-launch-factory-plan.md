# Vista Launch Factory Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a claim-safe, Barry-gated launch factory that turns one Vista release folder into six review-ready outputs plus a one-release cadence binder, packaged for a recorded Wed Sep 9 E2E (no auto-publish).

**Architecture:** Pilot SoT lives as JSON schemas + Notion/Drive artifacts under `vista/work/`. Grok-crew is the brain; Notion button is the demo Run trigger (Gumloop/Drive documented as leave-behinds). Spine: ingest → retrieve → Claims Lock (Barry once, kill-switch on fail) → adapter₁ spot-check → remaining five + cadence → validate ≤2 → Barry pack approve → Drive package + honesty doc → optional HubSpot sandbox draft last → STOP. Writers never approve; WIP=1 in `awaiting_barry`.

**Tech Stack:** Python 3.11+, `jsonschema`, `pytest`, JSON Schema Draft 2020-12, Markdown templates (Notion/Barry/adapters/recording), local working tree under `/home/box/shared/handoffs/reggie-pilot/vista/work/` (not a production HubSpot/Vista write path). Optional later: HyperBots STACK doc note only if Gabe asks.

## Global Constraints

- Scope **B** — all six required outputs + full one-release campaign cadence (quality risk accepted)
- HOW = **Recorded factory** — pre-bake; room is Q&A (no live-wait generation)
- **Barry** = copy + creative ship gate (Claims Lock → O1 spot-check → pack approve)
- **No auto-publish** — humans publish out of band; forbidden transitions include drafting→published and awaiting_barry→sandbox without approve
- **HubSpot sandbox last** after Barry — draft only; no `/publish`; not “we own Vista HubSpot”
- **Customer.io ≠ Vista ESP** — never demo CIO as their ESP
- **Temporal OUT** — not required for Wed
- **Writer ≠ Barry** — different seats; Slack thumbs ≠ approve
- **WIP=1** in `awaiting_barry`
- **Cut-order** = contingency only (`decision.md`) — never quiet revert to thin spine; label bonus partial; fall back to old C only with explicit Gabe yes
- **No inventing Vista claims/pricing** — fixture uses placeholders (`FEATURE_NAME`, etc.) labelled as fixture until Reggie access

---

## File Structure

All new work lands under `/home/box/shared/handoffs/reggie-pilot/vista/work/` unless noted.

```text
work/
├── schemas/
│   ├── release_campaign.schema.json   # ReleaseCampaign SoT
│   ├── claim_ledger.schema.json       # allowed/forbidden/evidence + kill_switch
│   └── cadence_binder.schema.json     # one-release tier-blast cells + UTM stubs
├── fixtures/
│   └── demo-release/                  # LABELLED FIXTURE — not real Vista product facts
│       ├── FIXTURE_LABEL.md
│       ├── sources/
│       │   ├── loom_transcript.txt
│       │   ├── github_outline.md
│       │   └── footage_index.json
│       ├── claim_ledger.json
│       ├── release_campaign.json
│       └── cadence_binder.json
├── scripts/
│   ├── validate_ledger.py
│   ├── validate_campaign.py
│   └── build_package.py
├── adapters/
│   ├── 01_social_video.md
│   ├── 02_blog.md
│   ├── 03_email_segments.md
│   ├── 04_changelog.md
│   ├── 05_login_animation.md
│   └── 06_in_app_popup.md
├── notion/
│   └── campaign-template.md
├── barry/
│   ├── claims-lock-template.md
│   └── approve-pack-template.md
├── recording/
│   └── shot-list.md
├── honesty/
│   └── still-needs-human.md
├── handoff/                           # SOP later via sop-builder
│   └── README.md
├── trigger/
│   └── notion-run-leavebehind.md
├── hubspot/
│   └── sandbox-checklist.md
├── optional/
│   └── hyperbots-stack-note.md
├── prep/
│   └── tue-wed-checklist.md
├── tests/
│   ├── test_validate_ledger.py
│   ├── test_validate_campaign.py
│   ├── test_cadence_binder.py
│   ├── test_adapters_present.py
│   ├── test_build_package.py
│   └── conftest.py
├── requirements.txt
└── README.md
```

**Responsibility split:** schemas define shape; validators enforce claims + slots; fixtures are Vista-shaped placeholders; adapters are stub outputs for recording; Notion/Barry/recording/honesty/trigger/hubspot are leave-behind docs; `handoff/` is a placeholder for sop-builder; scripts never publish.

---
### Task 1: Scaffold `work/` + schemas + failing tests (ReleaseCampaign + ClaimLedger)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/requirements.txt`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/README.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/schemas/claim_ledger.schema.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/schemas/release_campaign.schema.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/conftest.py`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_ledger.py`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_campaign.py`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/scripts/__init__.py` (empty)
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/handoff/README.md`

**Interfaces:**
- Consumes: design SoT sketch (§7), DESIGN-LOCK §1–§2
- Produces: JSON Schema files; pytest that import `scripts.validate_ledger.validate_ledger` and `scripts.validate_campaign.validate_campaign` (not yet implemented — tests must fail)

- [ ] **Step 1: Create directory tree + requirements**

```bash
BASE=/home/box/shared/handoffs/reggie-pilot/vista/work
mkdir -p "$BASE"/{schemas,fixtures/demo-release/sources,scripts,adapters,notion,barry,recording,honesty,handoff,trigger,hubspot,optional,prep,tests}
printf 'jsonschema>=4.22.0\npytest>=8.0.0\n' > "$BASE/requirements.txt"
printf '# Vista launch factory working tree\n\nLABELLED FIXTURE until Reggie access. No inventing claims. No auto-publish.\n' > "$BASE/README.md"
printf '# Handoff SOP\n\nFull SOP via sop-builder after plan execution. Do not invent maintainer steps here.\n' > "$BASE/handoff/README.md"
touch "$BASE/scripts/__init__.py"
cd "$BASE" && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

- [ ] **Step 2: Write `claim_ledger.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://vista.local/schemas/claim_ledger.schema.json",
  "title": "ClaimLedger",
  "type": "object",
  "additionalProperties": false,
  "required": ["campaign_id", "allowed", "forbidden", "needs_disclaimer", "evidence", "kill_switch"],
  "properties": {
    "campaign_id": { "type": "string", "minLength": 1 },
    "allowed": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim_id", "text"],
        "properties": {
          "claim_id": { "type": "string", "minLength": 1 },
          "text": { "type": "string", "minLength": 1 }
        }
      }
    },
    "forbidden": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim_id", "text", "reason"],
        "properties": {
          "claim_id": { "type": "string" },
          "text": { "type": "string" },
          "reason": { "type": "string" }
        }
      }
    },
    "needs_disclaimer": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim_id", "text", "disclaimer"],
        "properties": {
          "claim_id": { "type": "string" },
          "text": { "type": "string" },
          "disclaimer": { "type": "string" }
        }
      }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim_id", "source", "path", "span_start", "span_end", "quote"],
        "properties": {
          "claim_id": { "type": "string" },
          "source": { "enum": ["loom_transcript", "github_outline", "footage_index"] },
          "path": { "type": "string" },
          "span_start": { "type": "integer", "minimum": 0 },
          "span_end": { "type": "integer", "minimum": 0 },
          "quote": { "type": "string", "minLength": 1 }
        }
      }
    },
    "kill_switch": {
      "type": "object",
      "additionalProperties": false,
      "required": ["armed", "reason"],
      "properties": {
        "armed": { "type": "boolean" },
        "reason": { "type": ["string", "null"] }
      }
    }
  }
}
```

- [ ] **Step 3: Write `release_campaign.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://vista.local/schemas/release_campaign.schema.json",
  "title": "ReleaseCampaign",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "id", "title", "folder_id", "status", "fixture_label", "sources",
    "claim_ledger_ref", "voice_pack_ref", "segments", "artifacts",
    "cadence_ref", "barry", "hubspot_sandbox", "still_needs_human"
  ],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "title": { "type": "string", "minLength": 1 },
    "folder_id": { "type": "string", "minLength": 1 },
    "status": {
      "enum": [
        "idle", "ingested", "retrieving", "claims_gate", "needs_source_fix",
        "drafting", "validating", "held", "awaiting_barry", "approved",
        "packaged", "sandbox_exported", "closed"
      ]
    },
    "fixture_label": {
      "type": "string",
      "description": "Non-empty for labelled fixtures; empty string only for real Reggie folder"
    },
    "sources": {
      "type": "object",
      "additionalProperties": false,
      "required": ["loom", "transcript", "github_outline", "footage"],
      "properties": {
        "loom": { "type": "string" },
        "transcript": { "type": "string" },
        "github_outline": { "type": "string" },
        "footage": { "type": "array", "items": { "type": "string" } }
      }
    },
    "claim_ledger_ref": { "type": "string" },
    "voice_pack_ref": { "type": "string" },
    "segments": {
      "type": "object",
      "additionalProperties": false,
      "required": ["leads", "customers", "affiliate_rules"],
      "properties": {
        "leads": {
          "type": "array",
          "items": { "enum": ["SMB", "Agency", "Reseller_Affiliate"] }
        },
        "customers": {
          "type": "array",
          "items": { "enum": ["SMB", "Agency"] }
        },
        "affiliate_rules": { "type": "string" }
      }
    },
    "artifacts": {
      "type": "array",
      "minItems": 6,
      "maxItems": 6,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["slot", "type", "version", "path", "validation", "barry_status", "held"],
        "properties": {
          "slot": { "type": "integer", "minimum": 1, "maximum": 6 },
          "type": {
            "enum": [
              "social_video", "blog", "email_segments", "changelog",
              "login_animation", "in_app_popup"
            ]
          },
          "version": { "type": "integer", "minimum": 1 },
          "path": { "type": ["string", "null"] },
          "validation": { "enum": ["pending", "pass", "retryable_fail", "hard_fail"] },
          "barry_status": { "enum": ["not_submitted", "spot_check", "pending", "approved", "request_changes", "held"] },
          "held": { "type": "boolean" },
          "hold_reason": { "type": ["string", "null"] }
        }
      }
    },
    "cadence_ref": { "type": "string" },
    "barry": {
      "type": "object",
      "additionalProperties": false,
      "required": ["seat", "surface", "wip"],
      "properties": {
        "seat": { "const": "Barry VP Marketing" },
        "surface": { "type": "string" },
        "wip": { "type": "integer", "const": 1 }
      }
    },
    "hubspot_sandbox": {
      "type": "object",
      "additionalProperties": false,
      "required": ["draft_ids", "status"],
      "properties": {
        "draft_ids": { "type": "array", "items": { "type": "string" } },
        "status": { "enum": ["not_started", "draft_only", "blocked_no_barry", "skipped"] }
      }
    },
    "still_needs_human": { "type": "array", "items": { "type": "string" } }
  }
}
```

- [ ] **Step 4: Write failing tests (`conftest.py` + ledger + campaign)**

```python
# tests/conftest.py
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]

@pytest.fixture
def work_root() -> Path:
    return ROOT

@pytest.fixture
def schemas_dir(work_root: Path) -> Path:
    return work_root / "schemas"
```

```python
# tests/test_validate_ledger.py
def _minimal_ledger(**overrides):
    base = {
        "campaign_id": "camp_demo_001",
        "allowed": [
            {"claim_id": "c1", "text": "FEATURE_NAME lets teams schedule posts"}
        ],
        "forbidden": [
            {"claim_id": "f1", "text": "unlimited seats for $0", "reason": "pricing invention"}
        ],
        "needs_disclaimer": [],
        "evidence": [
            {
                "claim_id": "c1",
                "source": "github_outline",
                "path": "sources/github_outline.md",
                "span_start": 0,
                "span_end": 42,
                "quote": "FEATURE_NAME lets teams schedule posts",
            }
        ],
        "kill_switch": {"armed": False, "reason": None},
    }
    base.update(overrides)
    return base


def test_validate_ledger_pass_when_every_allowed_has_evidence():
    from scripts.validate_ledger import validate_ledger

    result = validate_ledger(_minimal_ledger())
    assert result["ok"] is True
    assert result["kill_switch"]["armed"] is False


def test_validate_ledger_fails_without_evidence_span_and_arms_kill_switch():
    from scripts.validate_ledger import validate_ledger

    ledger = _minimal_ledger(evidence=[])
    result = validate_ledger(ledger)
    assert result["ok"] is False
    assert result["kill_switch"]["armed"] is True
    assert any("c1" in e for e in result["errors"])


def test_validate_ledger_fails_on_forbidden_text_in_allowed():
    from scripts.validate_ledger import validate_ledger

    ledger = _minimal_ledger(
        allowed=[
            {"claim_id": "c1", "text": "FEATURE_NAME"},
            {"claim_id": "bad", "text": "unlimited seats for $0"},
        ],
        evidence=[
            {
                "claim_id": "c1",
                "source": "github_outline",
                "path": "sources/github_outline.md",
                "span_start": 0,
                "span_end": 12,
                "quote": "FEATURE_NAME",
            },
            {
                "claim_id": "bad",
                "source": "github_outline",
                "path": "sources/github_outline.md",
                "span_start": 0,
                "span_end": 5,
                "quote": "nope",
            },
        ],
    )
    result = validate_ledger(ledger)
    assert result["ok"] is False
    assert result["kill_switch"]["armed"] is True
    assert any("forbidden" in e.lower() for e in result["errors"])
```

```python
# tests/test_validate_campaign.py
REQUIRED_TYPES = [
    "social_video",
    "blog",
    "email_segments",
    "changelog",
    "login_animation",
    "in_app_popup",
]


def _minimal_campaign(**overrides):
    artifacts = []
    for i, t in enumerate(REQUIRED_TYPES, start=1):
        artifacts.append(
            {
                "slot": i,
                "type": t,
                "version": 1,
                "path": f"adapters/{i:02d}_{t}.md",
                "validation": "pass",
                "barry_status": "pending",
                "held": False,
                "hold_reason": None,
            }
        )
    base = {
        "id": "camp_demo_001",
        "title": "FIXTURE — FEATURE_NAME launch",
        "folder_id": "fixture/demo-release",
        "status": "drafting",
        "fixture_label": "LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT",
        "sources": {
            "loom": "sources/loom_transcript.txt",
            "transcript": "sources/loom_transcript.txt",
            "github_outline": "sources/github_outline.md",
            "footage": ["sources/footage_index.json"],
        },
        "claim_ledger_ref": "claim_ledger.json",
        "voice_pack_ref": "voice_pack/fixture_placeholder",
        "segments": {
            "leads": ["SMB", "Agency", "Reseller_Affiliate"],
            "customers": ["SMB", "Agency"],
            "affiliate_rules": "FIXTURE — legal TBD from Reggie",
        },
        "artifacts": artifacts,
        "cadence_ref": "cadence_binder.json",
        "barry": {
            "seat": "Barry VP Marketing",
            "surface": "Notion + Drive pack",
            "wip": 1,
        },
        "hubspot_sandbox": {"draft_ids": [], "status": "not_started"},
        "still_needs_human": ["Claims Lock seed", "Final publish"],
    }
    base.update(overrides)
    return base


def test_validate_campaign_requires_six_slots():
    from scripts.validate_campaign import validate_campaign

    result = validate_campaign(_minimal_campaign())
    assert result["ok"] is True


def test_validate_campaign_fails_when_slot_missing_and_not_held():
    from scripts.validate_campaign import validate_campaign

    camp = _minimal_campaign()
    camp["artifacts"][5]["path"] = None
    camp["artifacts"][5]["held"] = False
    result = validate_campaign(camp)
    assert result["ok"] is False
    assert any("slot 6" in e.lower() or "in_app_popup" in e.lower() for e in result["errors"])


def test_validate_campaign_allows_held_slot_without_path():
    from scripts.validate_campaign import validate_campaign

    camp = _minimal_campaign()
    camp["artifacts"][4]["path"] = None
    camp["artifacts"][4]["held"] = True
    camp["artifacts"][4]["hold_reason"] = "claim missing — hold on camera"
    camp["artifacts"][4]["barry_status"] = "held"
    result = validate_campaign(camp)
    assert result["ok"] is True
```

- [ ] **Step 5: Run tests — expect FAIL (modules missing)**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
. .venv/bin/activate
PYTHONPATH=. pytest tests/test_validate_ledger.py tests/test_validate_campaign.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.validate_ledger'` (or similar import error).

- [ ] **Step 6: Local checkpoint (no push)**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
git init 2>/dev/null || true
git add schemas tests requirements.txt README.md handoff scripts/__init__.py
git commit -m "test: scaffold schemas + failing validator tests for ReleaseCampaign/ClaimLedger" || true
```

---
### Task 2: Implement validators (evidence spans, kill-switch, forbidden list)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/scripts/validate_ledger.py`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/scripts/validate_campaign.py`
- Test: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_ledger.py`
- Test: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_campaign.py`

**Interfaces:**
- Consumes: `dict` ledger / campaign objects; schema paths under `schemas/`
- Produces:
  - `validate_ledger(ledger: dict) -> dict` with keys `ok: bool`, `errors: list[str]`, `kill_switch: {"armed": bool, "reason": str|None}`
  - `validate_campaign(campaign: dict, *, schema_path: Path|None = None) -> dict` with keys `ok: bool`, `errors: list[str]`
  - CLI: `python -m scripts.validate_ledger path.json` exit 0 ok / 2 kill-switch / 1 other fail
  - CLI: `python -m scripts.validate_campaign path.json` exit 0 / 1

- [ ] **Step 1: Implement `validate_ledger.py`**

```python
"""Claim ledger validation — evidence spans + forbidden list + kill-switch."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "claim_ledger.schema.json"


def _load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    schema = _load_schema()
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(ledger), key=lambda e: list(e.path)):
        errors.append(f"schema: {err.message}")

    allowed_ids = {c["claim_id"] for c in ledger.get("allowed", []) if "claim_id" in c}
    evidence_by_claim: dict[str, list[dict[str, Any]]] = {}
    for ev in ledger.get("evidence", []):
        evidence_by_claim.setdefault(ev.get("claim_id", ""), []).append(ev)

    for claim in ledger.get("allowed", []):
        cid = claim.get("claim_id")
        spans = evidence_by_claim.get(cid, [])
        if not spans:
            errors.append(f"allowed claim {cid!r} has no evidence span")
            continue
        for sp in spans:
            if sp.get("span_end", -1) <= sp.get("span_start", 0):
                errors.append(f"evidence for {cid!r} has non-positive span")
            if not (sp.get("quote") or "").strip():
                errors.append(f"evidence for {cid!r} has empty quote")

    forbidden_texts = {
        (f.get("text") or "").strip().lower()
        for f in ledger.get("forbidden", [])
        if (f.get("text") or "").strip()
    }
    for claim in ledger.get("allowed", []):
        text = (claim.get("text") or "").strip().lower()
        for ft in forbidden_texts:
            if ft and ft in text:
                errors.append(
                    f"forbidden claim text appears in allowed claim {claim.get('claim_id')!r}: {ft!r}"
                )

    for cid in evidence_by_claim:
        if cid and cid not in allowed_ids and cid not in {
            c.get("claim_id") for c in ledger.get("needs_disclaimer", [])
        }:
            errors.append(f"evidence references unknown claim_id {cid!r}")

    armed = bool(errors)
    reason = "; ".join(errors) if armed else None
    return {
        "ok": not armed,
        "errors": errors,
        "kill_switch": {"armed": armed, "reason": reason},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate ClaimLedger JSON")
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    ledger = json.loads(args.path.read_text(encoding="utf-8"))
    result = validate_ledger(ledger)
    print(json.dumps(result, indent=2))
    if result["kill_switch"]["armed"]:
        return 2
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Implement `validate_campaign.py`**

```python
"""ReleaseCampaign validation — schema + six slots exist-or-held."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "release_campaign.schema.json"
CADENCE_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "cadence_binder.schema.json"

REQUIRED_TYPES = [
    "social_video",
    "blog",
    "email_segments",
    "changelog",
    "login_animation",
    "in_app_popup",
]

REQUIRED_CADENCE_CHANNELS = [
    "changelog",
    "email_interrupt",
    "story_video",
    "linkedin_written",
    "x_written",
    "threads_written",
    "instagram_video",
    "tiktok_video",
]

FORBIDDEN_STATUS_TRANSITIONS_NOTE = (
    "Validators do not publish. Forbidden: drafting→published; "
    "awaiting_barry→sandbox without Barry approve."
)


def validate_campaign(
    campaign: dict[str, Any], *, schema_path: Path | None = None
) -> dict[str, Any]:
    errors: list[str] = []
    path = schema_path or SCHEMA_PATH
    schema = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(campaign), key=lambda e: list(e.path)):
        errors.append(f"schema: {err.message}")

    artifacts = campaign.get("artifacts") or []
    by_slot = {a.get("slot"): a for a in artifacts if isinstance(a, dict)}
    types_seen = []
    for slot in range(1, 7):
        art = by_slot.get(slot)
        if art is None:
            errors.append(f"missing artifact slot {slot}")
            continue
        types_seen.append(art.get("type"))
        held = bool(art.get("held"))
        path_val = art.get("path")
        if not held and not path_val:
            errors.append(
                f"slot {slot} ({art.get('type')}) missing path and not held"
            )
        if held and not art.get("hold_reason"):
            errors.append(f"slot {slot} held without hold_reason")

    for required in REQUIRED_TYPES:
        if required not in types_seen:
            errors.append(f"missing required artifact type {required}")

    barry = campaign.get("barry") or {}
    if barry.get("wip") != 1:
        errors.append("barry.wip must be 1 (WIP=1 awaiting_barry)")
    if barry.get("seat") != "Barry VP Marketing":
        errors.append("barry.seat must be 'Barry VP Marketing'")

    segs = campaign.get("segments") or {}
    if not segs.get("leads"):
        errors.append("segments.leads must be present")
    if not segs.get("customers"):
        errors.append("segments.customers must be present")

    hs = campaign.get("hubspot_sandbox") or {}
    if hs.get("status") == "draft_only" and campaign.get("status") == "awaiting_barry":
        errors.append(
            "hubspot sandbox draft blocked while awaiting_barry (Apiana hygiene)"
        )

    return {"ok": len(errors) == 0, "errors": errors, "note": FORBIDDEN_STATUS_TRANSITIONS_NOTE}


def validate_cadence_binder(binder: dict[str, Any]) -> dict[str, Any]:
    """Used from Task 5 onward; defined here so one module owns campaign-adjacent checks."""
    errors: list[str] = []
    if not CADENCE_SCHEMA_PATH.exists():
        errors.append("cadence_binder.schema.json missing — complete Task 5")
        return {"ok": False, "errors": errors}
    schema = json.loads(CADENCE_SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(binder), key=lambda e: list(e.path)):
        errors.append(f"schema: {err.message}")
    channels = {c.get("channel") for c in binder.get("cells", [])}
    for ch in REQUIRED_CADENCE_CHANNELS:
        if ch not in channels:
            errors.append(f"missing cadence cell for channel {ch}")
    return {"ok": len(errors) == 0, "errors": errors}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate ReleaseCampaign JSON")
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    campaign = json.loads(args.path.read_text(encoding="utf-8"))
    result = validate_campaign(campaign)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Run tests — expect PASS**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
. .venv/bin/activate
PYTHONPATH=. pytest tests/test_validate_ledger.py tests/test_validate_campaign.py -v
```

Expected: all PASS.

- [ ] **Step 4: Local checkpoint (no push)**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
git add scripts/validate_ledger.py scripts/validate_campaign.py
git commit -m "feat: claim ledger kill-switch + campaign six-slot validators" || true
```

---
### Task 3: Fixture `demo-release` (Vista-shaped, NO invented product facts)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/FIXTURE_LABEL.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/sources/loom_transcript.txt`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/sources/github_outline.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/sources/footage_index.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/claim_ledger.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/release_campaign.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/cadence_binder.json` (stub cells; full tier-blast in Task 5)
- Modify: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_ledger.py` (fixture integration)
- Modify: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_validate_campaign.py` (fixture integration)

**Interfaces:**
- Consumes: validators from Task 2
- Produces: labelled fixture `campaign_id` `camp_demo_001`; placeholders only (`FEATURE_NAME`, `PLACEHOLDER_BENEFIT`)

- [ ] **Step 1: Write FIXTURE_LABEL + sources (placeholders only)**

`FIXTURE_LABEL.md`:

```markdown
# FIXTURE — NOT REAL VISTA PRODUCT FACTS

This folder is **Vista-shaped** for Wed recording rehearsal until Reggie shares the real release folder.

Rules:
- Do not replace placeholders with guessed Vista features, pricing, limits, or partner claims.
- When Reggie access lands, swap sources and re-run Claims Lock; delete or archive this fixture label.
- Label on camera: "fixture until Reggie folder".
```

`sources/loom_transcript.txt`:

```text
[FIXTURE TRANSCRIPT]
Speaker: Product (placeholder)
00:00 FEATURE_NAME helps teams do PLACEHOLDER_BENEFIT.
00:15 We are not stating pricing in this walkthrough.
00:20 Footage cue: UI_SCREEN_A shows schedule calendar placeholder.
```

`sources/github_outline.md`:

```markdown
# FIXTURE outline — FEATURE_NAME

- FEATURE_NAME lets teams schedule posts
- PLACEHOLDER_BENEFIT for SMB and Agency segments (segment truth TBD)
- No pricing in this outline
- Off-limits: unlimited seats for $0 (forbidden fixture row)
```

`sources/footage_index.json`:

```json
{
  "fixture_label": "LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT",
  "assets": [
    {
      "id": "UI_SCREEN_A",
      "path": "PLACEHOLDER_FOOTAGE/ui_screen_a.mp4",
      "notes": "fixture only — replace with Reggie footage"
    }
  ]
}
```

- [ ] **Step 2: Write `claim_ledger.json` + `release_campaign.json` + cadence stub**

`claim_ledger.json`:

```json
{
  "campaign_id": "camp_demo_001",
  "allowed": [
    {"claim_id": "c1", "text": "FEATURE_NAME lets teams schedule posts"},
    {"claim_id": "c2", "text": "FEATURE_NAME helps teams do PLACEHOLDER_BENEFIT"}
  ],
  "forbidden": [
    {
      "claim_id": "f1",
      "text": "unlimited seats for $0",
      "reason": "pricing invention — fixture forbidden list seed"
    }
  ],
  "needs_disclaimer": [],
  "evidence": [
    {
      "claim_id": "c1",
      "source": "github_outline",
      "path": "sources/github_outline.md",
      "span_start": 0,
      "span_end": 80,
      "quote": "FEATURE_NAME lets teams schedule posts"
    },
    {
      "claim_id": "c2",
      "source": "loom_transcript",
      "path": "sources/loom_transcript.txt",
      "span_start": 0,
      "span_end": 120,
      "quote": "FEATURE_NAME helps teams do PLACEHOLDER_BENEFIT"
    }
  ],
  "kill_switch": { "armed": false, "reason": null }
}
```

`release_campaign.json`:

```json
{
  "id": "camp_demo_001",
  "title": "FIXTURE — FEATURE_NAME launch",
  "folder_id": "fixture/demo-release",
  "status": "drafting",
  "fixture_label": "LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT",
  "sources": {
    "loom": "sources/loom_transcript.txt",
    "transcript": "sources/loom_transcript.txt",
    "github_outline": "sources/github_outline.md",
    "footage": ["sources/footage_index.json"]
  },
  "claim_ledger_ref": "claim_ledger.json",
  "voice_pack_ref": "voice_pack/fixture_placeholder",
  "segments": {
    "leads": ["SMB", "Agency", "Reseller_Affiliate"],
    "customers": ["SMB", "Agency"],
    "affiliate_rules": "FIXTURE — legal TBD from Reggie"
  },
  "artifacts": [
    {"slot": 1, "type": "social_video", "version": 1, "path": "adapters/01_social_video.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null},
    {"slot": 2, "type": "blog", "version": 1, "path": "adapters/02_blog.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null},
    {"slot": 3, "type": "email_segments", "version": 1, "path": "adapters/03_email_segments.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null},
    {"slot": 4, "type": "changelog", "version": 1, "path": "adapters/04_changelog.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null},
    {"slot": 5, "type": "login_animation", "version": 1, "path": "adapters/05_login_animation.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null},
    {"slot": 6, "type": "in_app_popup", "version": 1, "path": "adapters/06_in_app_popup.md", "validation": "pending", "barry_status": "not_submitted", "held": false, "hold_reason": null}
  ],
  "cadence_ref": "cadence_binder.json",
  "barry": {
    "seat": "Barry VP Marketing",
    "surface": "Notion + Drive pack",
    "wip": 1
  },
  "hubspot_sandbox": { "draft_ids": [], "status": "not_started" },
  "still_needs_human": [
    "Source folder quality (Reggie)",
    "Claims Lock seed / forbidden list confirm",
    "Voice pack encode",
    "Social video taste",
    "Login animation designer/Lottie",
    "Popup graphic taste / placement",
    "Final publish",
    "Segment / affiliate legal"
  ]
}
```

Minimal cadence stub until Task 5:

```json
{
  "campaign_id": "camp_demo_001",
  "fixture_label": "LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT",
  "cells": []
}
```

- [ ] **Step 3: Add fixture integration tests**

Append to `tests/test_validate_ledger.py`:

```python
def test_fixture_ledger_validates(work_root):
    from scripts.validate_ledger import validate_ledger
    import json

    path = work_root / "fixtures/demo-release/claim_ledger.json"
    ledger = json.loads(path.read_text(encoding="utf-8"))
    result = validate_ledger(ledger)
    assert result["ok"] is True
```

Append to `tests/test_validate_campaign.py`:

```python
def test_fixture_campaign_validates(work_root):
    from scripts.validate_campaign import validate_campaign
    import json

    path = work_root / "fixtures/demo-release/release_campaign.json"
    camp = json.loads(path.read_text(encoding="utf-8"))
    result = validate_campaign(camp)
    assert result["ok"] is True
    assert camp["fixture_label"].startswith("LABELLED_FIXTURE")
```

- [ ] **Step 4: Run validators on fixture**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
. .venv/bin/activate
PYTHONPATH=. python -m scripts.validate_ledger fixtures/demo-release/claim_ledger.json
PYTHONPATH=. python -m scripts.validate_campaign fixtures/demo-release/release_campaign.json
PYTHONPATH=. pytest tests/ -v -k fixture
```

Expected: exit 0; fixture tests PASS.

- [ ] **Step 5: Local checkpoint (no push)**

```bash
git add fixtures tests
git commit -m "feat: labelled demo-release fixture with placeholder claims only" || true
```

---

### Task 4: Notion campaign field map + Barry Claims Lock / pack approve templates

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/notion/campaign-template.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/barry/claims-lock-template.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/barry/approve-pack-template.md`

**Interfaces:**
- Consumes: ReleaseCampaign property names from schema; Barry HITL rules from design §3
- Produces: field map docs for Notion; approve cards that are not Slack thumbs

- [ ] **Step 1: Write Notion campaign field map**

```markdown
# Notion — Campaign DB field map (pilot SoT)

One row per `ReleaseCampaign`. Drive holds blobs; Notion holds status + Barry queue.

| Notion property | Type | Maps to | Notes |
|---|---|---|---|
| Name | Title | `title` | e.g. FIXTURE — FEATURE_NAME launch |
| campaign_id | Rich text | `id` | `camp_demo_001` |
| folder_id | URL / text | `folder_id` | Drive folder once Reggie shares |
| status | Select | `status` | idle → … → closed (see schema enum) |
| fixture_label | Rich text | `fixture_label` | Non-empty = labelled fixture |
| claim_ledger | Files / URL | `claim_ledger_ref` | JSON in Drive |
| voice_pack_ref | Text | `voice_pack_ref` | |
| cadence_ref | Text / URL | `cadence_ref` | |
| artifact_1..6 | Files | `artifacts[].path` | Or linked Drive subfolder |
| barry_seat | Text | `barry.seat` | const Barry VP Marketing |
| barry_surface | Select | `barry.surface` | Notion + Drive pack (v1) |
| barry_wip | Number | `barry.wip` | **Must be 1** |
| hubspot_sandbox_status | Select | `hubspot_sandbox.status` | not_started / draft_only / blocked_no_barry / skipped |
| still_needs_human | Multi-select / text | `still_needs_human[]` | Honesty list |
| Run launch | Button | trigger | See `trigger/notion-run-leavebehind.md` |

**WIP rule:** only one campaign in `awaiting_barry` at a time (`barry.wip=1`).

**Not in Notion:** Customer.io as ESP; production HubSpot publish; Temporal run ids.
```

- [ ] **Step 2: Write Claims Lock template**

```markdown
# Barry — Claims Lock (once per campaign)

**Campaign:** {{campaign_id}} — {{title}}
**Seat:** Barry VP Marketing (writer ≠ Barry)
**Surface:** Notion approve card + linked ledger

## Ledger summary
- Allowed claims: {{allowed_count}}
- Forbidden list present: yes/no
- Kill-switch armed: {{kill_switch.armed}}

## Decision
- [ ] **Approve Claims Lock** — adapters may run
- [ ] **Reject / kill-switch** — fix source; do not draft

## Rules
- Every allowed claim must show evidence span (transcript or outline).
- No pricing / limits invention.
- Slack thumbs ≠ Claims Lock.
- On reject: status → `needs_source_fix`; adapters stay cold.
```

- [ ] **Step 3: Write pack approve template**

```markdown
# Barry — Pack approve (copy + creative)

**Campaign:** {{campaign_id}}
**Prerequisite:** Claims Lock approved; O1 spot-check done; validate ≤2 done
**WIP:** 1 in awaiting_barry

## Artifacts
| Slot | Type | Link | Spot-check | Decision |
|---|---|---|---|---|
| 1 | social_video | | required first | Approve / Request Changes |
| 2 | blog | | | |
| 3 | email_segments | | | |
| 4 | changelog | | | |
| 5 | login_animation | | | |
| 6 | in_app_popup | | | |
| — | cadence binder | | | |

## Decision
- [ ] **Approve pack** → status `approved` → package + honesty doc
- [ ] **Request Changes** — list artifact slot(s) to regenerate (named only; no silent rewrite-as-approve)

## Forbidden
- One click to ship / auto-publish
- HubSpot sandbox export before this approve
- Treating Slack emoji as approve
```

- [ ] **Step 4: Sanity check (doc presence)**

```bash
test -f /home/box/shared/handoffs/reggie-pilot/vista/work/notion/campaign-template.md
test -f /home/box/shared/handoffs/reggie-pilot/vista/work/barry/claims-lock-template.md
test -f /home/box/shared/handoffs/reggie-pilot/vista/work/barry/approve-pack-template.md
grep -q 'WIP' /home/box/shared/handoffs/reggie-pilot/vista/work/notion/campaign-template.md
grep -q 'kill-switch' /home/box/shared/handoffs/reggie-pilot/vista/work/barry/claims-lock-template.md
```

Expected: all commands exit 0.

- [ ] **Step 5: Local checkpoint (no push)**

```bash
git add notion barry
git commit -m "docs: Notion campaign field map + Barry Claims Lock and pack templates" || true
```

---
### Task 5: Cadence binder schema + tier-blast sample cells

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/schemas/cadence_binder.schema.json`
- Modify: `/home/box/shared/handoffs/reggie-pilot/vista/work/fixtures/demo-release/cadence_binder.json`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_cadence_binder.py`
- Modify: `/home/box/shared/handoffs/reggie-pilot/vista/work/scripts/validate_campaign.py` (`validate_cadence_binder` already stubbed in Task 2 — ensure schema file exists)

**Interfaces:**
- Consumes: `campaign_id` shared with ReleaseCampaign
- Produces: `validate_cadence_binder(binder: dict) -> dict` with `ok`, `errors`; tier order: changelog floor → interrupt email → story video → written social (LI/X/Threads) + IG/TikTok cells + UTM stubs

- [ ] **Step 1: Write failing test**

```python
# tests/test_cadence_binder.py
import json

REQUIRED_CHANNELS = [
    "changelog",
    "email_interrupt",
    "story_video",
    "linkedin_written",
    "x_written",
    "threads_written",
    "instagram_video",
    "tiktok_video",
]


def test_fixture_cadence_has_tier_blast_cells(work_root):
    from scripts.validate_campaign import validate_cadence_binder

    path = work_root / "fixtures/demo-release/cadence_binder.json"
    binder = json.loads(path.read_text(encoding="utf-8"))
    result = validate_cadence_binder(binder)
    assert result["ok"] is True
    channels = {c["channel"] for c in binder["cells"]}
    for ch in REQUIRED_CHANNELS:
        assert ch in channels
    assert binder["campaign_id"] == "camp_demo_001"
```

- [ ] **Step 2: Run test — expect FAIL**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work && . .venv/bin/activate
PYTHONPATH=. pytest tests/test_cadence_binder.py -v
```

Expected: FAIL (`cadence_binder.schema.json` missing and/or empty cells).

- [ ] **Step 3: Write schema + sample cells**

`schemas/cadence_binder.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://vista.local/schemas/cadence_binder.schema.json",
  "title": "CadenceBinder",
  "type": "object",
  "additionalProperties": false,
  "required": ["campaign_id", "fixture_label", "cells"],
  "properties": {
    "campaign_id": { "type": "string" },
    "fixture_label": { "type": "string" },
    "cells": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["order", "channel", "artifact_slot", "utm", "notes"],
        "properties": {
          "order": { "type": "integer", "minimum": 1 },
          "channel": {
            "enum": [
              "changelog",
              "email_interrupt",
              "story_video",
              "linkedin_written",
              "x_written",
              "threads_written",
              "instagram_video",
              "tiktok_video"
            ]
          },
          "artifact_slot": { "type": ["integer", "null"], "minimum": 1, "maximum": 6 },
          "utm": {
            "type": "object",
            "required": ["utm_source", "utm_medium", "utm_campaign"],
            "properties": {
              "utm_source": { "type": "string" },
              "utm_medium": { "type": "string" },
              "utm_campaign": { "type": "string" }
            }
          },
          "notes": { "type": "string" }
        }
      }
    }
  }
}
```

Replace fixture `cadence_binder.json`:

```json
{
  "campaign_id": "camp_demo_001",
  "fixture_label": "LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT",
  "cells": [
    {"order": 1, "channel": "changelog", "artifact_slot": 4, "utm": {"utm_source": "changelog", "utm_medium": "product", "utm_campaign": "camp_demo_001"}, "notes": "floor — FEATURE_NAME bullets only"},
    {"order": 2, "channel": "email_interrupt", "artifact_slot": 3, "utm": {"utm_source": "hubspot_sandbox", "utm_medium": "email", "utm_campaign": "camp_demo_001"}, "notes": "segmented announcement; draft only"},
    {"order": 3, "channel": "story_video", "artifact_slot": 1, "utm": {"utm_source": "social", "utm_medium": "video", "utm_campaign": "camp_demo_001"}, "notes": "social video + burned captions"},
    {"order": 4, "channel": "linkedin_written", "artifact_slot": 1, "utm": {"utm_source": "linkedin", "utm_medium": "social", "utm_campaign": "camp_demo_001"}, "notes": "written social cell"},
    {"order": 5, "channel": "x_written", "artifact_slot": 1, "utm": {"utm_source": "x", "utm_medium": "social", "utm_campaign": "camp_demo_001"}, "notes": "cut-order drop-early candidate"},
    {"order": 6, "channel": "threads_written", "artifact_slot": 1, "utm": {"utm_source": "threads", "utm_medium": "social", "utm_campaign": "camp_demo_001"}, "notes": "cut-order drop-first under clock"},
    {"order": 7, "channel": "instagram_video", "artifact_slot": 1, "utm": {"utm_source": "instagram", "utm_medium": "video", "utm_campaign": "camp_demo_001"}, "notes": "IG cell"},
    {"order": 8, "channel": "tiktok_video", "artifact_slot": 1, "utm": {"utm_source": "tiktok", "utm_medium": "video", "utm_campaign": "camp_demo_001"}, "notes": "TikTok cell — drop if IG exists under clock"}
  ]
}
```

- [ ] **Step 4: Run test — expect PASS**

```bash
PYTHONPATH=. pytest tests/test_cadence_binder.py -v
```

- [ ] **Step 5: Local checkpoint (no push)**

```bash
git add schemas/cadence_binder.schema.json fixtures/demo-release/cadence_binder.json tests/test_cadence_binder.py
git commit -m "feat: cadence binder schema + tier-blast fixture cells" || true
```

---

### Task 6: Six adapter output stubs + validation that all six slots exist or held

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/01_social_video.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/02_blog.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/03_email_segments.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/04_changelog.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/05_login_animation.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/adapters/06_in_app_popup.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_adapters_present.py`

**Interfaces:**
- Consumes: claim_ids `c1`, `c2` only; fixture paths in campaign
- Produces: six markdown stubs; test asserts files exist for non-held slots

- [ ] **Step 1: Write failing presence test**

```python
# tests/test_adapters_present.py
from pathlib import Path
import json


def test_six_adapter_files_exist_or_held(work_root: Path):
    camp = json.loads((work_root / "fixtures/demo-release/release_campaign.json").read_text())
    missing = []
    for art in camp["artifacts"]:
        if art.get("held"):
            continue
        path = art.get("path")
        if not path or not (work_root / path).exists():
            missing.append(art["type"])
    assert missing == [], f"missing adapters for: {missing}"
```

- [ ] **Step 2: Run — expect FAIL**

```bash
PYTHONPATH=. pytest tests/test_adapters_present.py -v
```

Expected: FAIL listing missing adapter types.

- [ ] **Step 3: Write six stubs (claims cited; no pricing)**

`adapters/01_social_video.md`:

```markdown
# O1 Social video + burned captions (FIXTURE)
**campaign_id:** camp_demo_001
**claims_used:** c1, c2
**length_bounds:** 15–45s (fixture)
**assets:** UI_SCREEN_A (placeholder footage)
**captions:** burned-in stub — "FEATURE_NAME lets teams schedule posts"
**honesty:** taste pass still needs human / Barry creative
**validation:** cut + captions file present; claims in ledger only
```

`adapters/02_blog.md`:

```markdown
# O2 Blog → vistasocial.com/insights/ (FIXTURE draft)
**H1:** Introducing FEATURE_NAME (fixture)
## What it is
FEATURE_NAME lets teams schedule posts. [claim:c1]
## Why it matters
FEATURE_NAME helps teams do PLACEHOLDER_BENEFIT. [claim:c2]
## CTA
Learn more in-product (human publishes)
**voice_pack_ref:** voice_pack/fixture_placeholder
```

`adapters/03_email_segments.md`:

```markdown
# O3 Email ×5 segments (FIXTURE drafts — HubSpot sandbox later)
| Segment | Status | Subject stub |
|---|---|---|
| leads / SMB | draft | FEATURE_NAME for SMB teams (fixture) |
| leads / Agency | draft | FEATURE_NAME for agencies (fixture) |
| leads / Reseller_Affiliate | draft | FEATURE_NAME partner note (fixture; legal TBD) |
| customers / SMB | draft | What's new: FEATURE_NAME (fixture) |
| customers / Agency | draft | What's new: FEATURE_NAME (fixture) |
Claims: c1, c2 only. No pricing. N/A explicit OK if Reggie marks a segment out.
```

`adapters/04_changelog.md`:

```markdown
# O4 Changelog → suggestions.vistasocial.com/changelog (FIXTURE)
- FEATURE_NAME lets teams schedule posts [c1]
- PLACEHOLDER_BENEFIT [c2]
No pricing. Feature bullets only.
```

`adapters/05_login_animation.md`:

```markdown
# O5 Login animation (FIXTURE — weakest LLM cell)
**format:** labelled mock (Lottie/MP4 TBD from Reggie)
**brief:** 3s loop hinting FEATURE_NAME calendar affordance — no new claims
**claims_used:** none new (visual only)
**honesty:** designer/Lottie still needs human
```

`adapters/06_in_app_popup.md`:

```markdown
# O6 In-app popup (FIXTURE)
**graphic:** PLACEHOLDER_GRAPHIC
**copy:** Try FEATURE_NAME — schedule posts faster. [c1]
**CTA:** Open FEATURE_NAME
**placement/size:** TBD from Reggie
**claims_gated:** c1 only
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
PYTHONPATH=. pytest tests/test_adapters_present.py tests/test_validate_campaign.py -v
```

- [ ] **Step 5: Local checkpoint (no push)**

```bash
git add adapters tests/test_adapters_present.py
git commit -m "feat: six adapter markdown stubs with ledger-cited placeholders" || true
```

---

### Task 7: `build_package.py` → Drive-ready folder layout + honesty doc stub

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/scripts/build_package.py`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/honesty/still-needs-human.md`
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/tests/test_build_package.py`

**Interfaces:**
- Consumes: `build_package(campaign_path: Path, out_dir: Path, *, work_root: Path | None = None) -> Path`
- Produces: Drive-ready folder:

```text
<out_dir>/<campaign_id>/
  01_social_video/
  02_blog/
  03_email_segments/
  04_changelog/
  05_login_animation/
  06_in_app_popup/
  cadence/
  provenance/
  honesty/still-needs-human.md
  MANIFEST.json
```

- [ ] **Step 1: Write honesty stub + failing test**

`honesty/still-needs-human.md`:

```markdown
# Still needs a human (Wed honesty)

| Step | Why human |
|---|---|
| Source folder quality | Bad Loom / thin outline → garbage in |
| Claims Lock seed (forbidden list) | Barry/Reggie confirm |
| Voice pack encode | Style guide + past newsletters |
| Social video taste | Captions burn basic; brand polish = Barry |
| Login animation | Designer / Lottie |
| Popup graphic taste / placement | From Reggie |
| Final publish | CMS, changelog, login, in-app |
| Segment / affiliate legal | Reseller rules |

Factory stops at review-ready package. **No auto-publish.**
```

```python
# tests/test_build_package.py
from pathlib import Path
import json


def test_build_package_layout(work_root, tmp_path):
    from scripts.build_package import build_package

    out = build_package(
        work_root / "fixtures/demo-release/release_campaign.json",
        tmp_path / "drive_ready",
        work_root=work_root,
    )
    assert out.name == "camp_demo_001"
    for name in [
        "01_social_video",
        "02_blog",
        "03_email_segments",
        "04_changelog",
        "05_login_animation",
        "06_in_app_popup",
        "cadence",
        "provenance",
        "honesty",
    ]:
        assert (out / name).exists()
    assert (out / "honesty" / "still-needs-human.md").exists()
    manifest = json.loads((out / "MANIFEST.json").read_text())
    assert manifest["campaign_id"] == "camp_demo_001"
    assert manifest["auto_publish"] is False
```

- [ ] **Step 2: Run — expect FAIL**

```bash
PYTHONPATH=. pytest tests/test_build_package.py -v
```

- [ ] **Step 3: Implement `build_package.py`**

```python
"""Build Drive-ready package folder — never publishes."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

SLOT_DIRS = {
    1: "01_social_video",
    2: "02_blog",
    3: "03_email_segments",
    4: "04_changelog",
    5: "05_login_animation",
    6: "06_in_app_popup",
}


def build_package(
    campaign_path: Path, out_dir: Path, *, work_root: Path | None = None
) -> Path:
    campaign_path = campaign_path.resolve()
    if work_root is None:
        # .../fixtures/demo-release/release_campaign.json → work/
        work_root = campaign_path.parents[2]
    campaign: dict[str, Any] = json.loads(campaign_path.read_text(encoding="utf-8"))
    camp_id = campaign["id"]
    root = out_dir / camp_id
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)

    for slot, dirname in SLOT_DIRS.items():
        d = root / dirname
        d.mkdir()
        art = next(a for a in campaign["artifacts"] if a["slot"] == slot)
        if art.get("held"):
            (d / "HELD.txt").write_text(
                art.get("hold_reason") or "held", encoding="utf-8"
            )
            continue
        src = work_root / art["path"]
        if src.exists():
            shutil.copy2(src, d / src.name)
        else:
            (d / "MISSING.txt").write_text(str(src), encoding="utf-8")

    cadence_src = campaign_path.parent / campaign.get("cadence_ref", "cadence_binder.json")
    (root / "cadence").mkdir()
    if cadence_src.exists():
        shutil.copy2(cadence_src, root / "cadence" / cadence_src.name)

    prov = root / "provenance"
    prov.mkdir()
    for key in ("transcript", "github_outline"):
        rel = campaign["sources"][key]
        src = campaign_path.parent / rel
        if src.exists():
            shutil.copy2(src, prov / src.name)
    ledger = campaign_path.parent / campaign["claim_ledger_ref"]
    if ledger.exists():
        shutil.copy2(ledger, prov / ledger.name)

    honesty_src = work_root / "honesty" / "still-needs-human.md"
    (root / "honesty").mkdir()
    if honesty_src.exists():
        shutil.copy2(honesty_src, root / "honesty" / "still-needs-human.md")
    else:
        (root / "honesty" / "still-needs-human.md").write_text(
            "\n".join(campaign.get("still_needs_human", [])), encoding="utf-8"
        )

    manifest = {
        "campaign_id": camp_id,
        "title": campaign["title"],
        "fixture_label": campaign.get("fixture_label"),
        "status": "packaged",
        "auto_publish": False,
        "barry_seat": campaign["barry"]["seat"],
        "hubspot_sandbox": campaign.get("hubspot_sandbox"),
        "note": "STOP — humans publish out of band",
    }
    (root / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return root


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("campaign_json", type=Path)
    p.add_argument("out_dir", type=Path)
    args = p.parse_args(argv)
    root = build_package(args.campaign_json, args.out_dir)
    print(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
PYTHONPATH=. pytest tests/test_build_package.py -v
PYTHONPATH=. python -m scripts.build_package fixtures/demo-release/release_campaign.json /tmp/vista-pkg
```

- [ ] **Step 5: Local checkpoint (no push)**

```bash
git add scripts/build_package.py honesty tests/test_build_package.py
git commit -m "feat: Drive-ready build_package + honesty stub" || true
```

---
### Task 8: Recording `shot-list.md` locked to design §3

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/recording/shot-list.md`

**Interfaces:**
- Consumes: design §3 / DESIGN-LOCK §3 verbatim beat order
- Produces: shot list used for pre-bake recording (no live-wait)

- [ ] **Step 1: Write shot list**

```markdown
# Recording shot list — Vista Launch Factory (locked to design §3)

**HOW:** Recorded factory. Pre-bake everything. Live = architecture + artifact Qs only.

## Beats (in order)
1. Marketer clicks **Run** (Notion button — demo default)
2. Folder ingest visible (fixture folder labelled on screen)
3. Claims ledger on screen → **Claims Lock** (Barry once)
4. O1 → Barry spot-check beat
5. Jump-cut O2–O6 + cadence binder (tier blast)
6. Pack approve → frozen package + honesty doc
7. HubSpot sandbox draft last (optional ~10s) → **STOP**

## Must show
- Provenance next to copy
- WIP=1 in awaiting_barry
- Writer ≠ Barry

## Must not
- Token stream
- Auto-publish
- Customer.io as Vista ESP
- Invented facts
- Six orphans with no cadence story

## If claim missing
Hold one artifact on camera (reliability on next feature) — label `held` + reason.

## Cut-order contingency (not the target)
If clock slips: follow `decision.md` cut-order; label bonus partial; never quiet-ship thin C without Gabe yes.
```

- [ ] **Step 2: Verify lock phrases present**

```bash
f=/home/box/shared/handoffs/reggie-pilot/vista/work/recording/shot-list.md
grep -q 'Claims Lock' "$f"
grep -q 'HubSpot sandbox' "$f"
grep -q 'Must not' "$f"
grep -q 'WIP=1' "$f"
grep -q 'Writer ≠ Barry' "$f"
```

- [ ] **Step 3: Local checkpoint (no push)**

```bash
git add recording/shot-list.md
git commit -m "docs: recording shot-list locked to design §3" || true
```

---

### Task 9: Trigger leave-behind notes (Notion default demo)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/trigger/notion-run-leavebehind.md`

**Interfaces:**
- Consumes: design §4 / architecture non-engineer trigger options
- Produces: Notion as demo default; Gumloop + Drive documented as leave-behinds (not brain)

- [ ] **Step 1: Write leave-behind doc**

```markdown
# Non-engineer Run trigger — leave-behind

**Demo default:** Notion button on Campaign row → “Run launch”.
**Brain:** Grok-crew (not Gumloop, not Temporal).
**Gumloop / Drive:** document for handoff; do not require for Wed hero.

## Notion (demo)
1. Property `Run launch` button on campaign row (`notion/campaign-template.md`).
2. Button sets status `ingested` and posts a checklist comment: folder_id, claim_ledger link, WIP check.
3. Orchestrator (crew) picks up from Notion/Drive — marketer does not open a terminal.
4. Status visible on same row through `awaiting_barry`.

## Gumloop (leave-behind)
- Form: folder URL in → status out.
- Trigger only — not the claims brain.
- Install path already available; wire after Notion demo path is solid.

## Drive label (leave-behind)
- Label/tag on release folder watched by crew routine.
- No Temporal watcher.

## Handoff must name
- Who clicks Run (marketing)
- Where Barry Approves / Request Changes
- How to re-run one output
- Builder ≠ maintainer
```

- [ ] **Step 2: Verify Notion is marked default**

```bash
grep -q 'Demo default' /home/box/shared/handoffs/reggie-pilot/vista/work/trigger/notion-run-leavebehind.md
grep -q 'Temporal' /home/box/shared/handoffs/reggie-pilot/vista/work/trigger/notion-run-leavebehind.md
```

- [ ] **Step 3: Local checkpoint (no push)**

```bash
git add trigger/notion-run-leavebehind.md
git commit -m "docs: Notion Run trigger leave-behind (Gumloop/Drive noted)" || true
```

---

### Task 10: HubSpot sandbox last checklist (draft only; Apiana hygiene)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/hubspot/sandbox-checklist.md`

**Interfaces:**
- Consumes: design §4 HubSpot row; Apiana connector claim hygiene
- Produces: checklist that blocks sandbox export before Barry approve; never `/publish`

- [ ] **Step 1: Write checklist**

```markdown
# HubSpot sandbox — last step checklist (Apiana hygiene)

**Order:** only after Barry pack approve on email artifacts.
**Account:** Reggie sandbox invite — not production.
**CIO:** ours only — never demo as Vista ESP.

## Before opening HubSpot
- [ ] Campaign status is `approved` or `packaged` (not `awaiting_barry`)
- [ ] Email adapter (O3) claims ⊆ ledger
- [ ] Segments mapped: leads SMB/Agency/Reseller_Affiliate + customers SMB/Agency (or explicit N/A)
- [ ] MANIFEST.json has `auto_publish: false`

## In sandbox
- [ ] Create **draft** emails only
- [ ] Record `draft_ids[]` on campaign `hubspot_sandbox`
- [ ] Set `hubspot_sandbox.status` = `draft_only`
- [ ] **Do not** call publish / marketing send / production lists

## Recording
- Optional ~10s beat showing draft UI → STOP
- Say on camera: “sandbox draft; humans send later”

## Refuse
- Production HubSpot send in trial recording
- Claiming we own Vista HubSpot
- Swapping Vista ESP to Customer.io
- Export while kill-switch armed
```

- [ ] **Step 2: Verify refuse lines**

```bash
f=/home/box/shared/handoffs/reggie-pilot/vista/work/hubspot/sandbox-checklist.md
grep -q 'draft_only' "$f"
grep -q 'Customer.io' "$f"
grep -q 'awaiting_barry' "$f"
```

- [ ] **Step 3: Local checkpoint (no push)**

```bash
git add hubspot/sandbox-checklist.md
git commit -m "docs: HubSpot sandbox-last checklist (draft only)" || true
```

---

### Task 11: HyperBots same-day doc note (OPTIONAL — skip push unless Gabe asks)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/optional/hyperbots-stack-note.md`

**Interfaces:**
- Consumes: Gabe explicit ask for public STACK update
- Produces: draft note only; **no** `git push` to `gabchess/HyperBots` in this plan

- [ ] **Step 1: Write optional note stub**

```markdown
# OPTIONAL — HyperBots STACK note (do not push unless Gabe asks)

**Repo target if asked:** gabchess/HyperBots (docs only).
**Default for this pilot:** keep working tree under `reggie-pilot/vista/work/`.

## Draft blurb (only if Gabe wants public STACK update)
Vista Social paid-trial launch factory (Sep 2026): claim-ledger-gated fan-out to six review-ready launch artifacts + one-release cadence binder; Barry HITL; recorded E2E; Notion/Drive SoT; no Temporal; no auto-publish.

## Implementer rule
- Skip this task’s push by default.
- If Gabe says yes: open a docs PR / edit STACK markdown only — no runtime secrets, no forged Vista claims.
- Prefer linking to this handoff path over copying fixture claims into public docs.
```

- [ ] **Step 2: Explicit skip gate**

```bash
# Default: do nothing else. Only continue to a HyperBots docs edit when Gabe message includes an explicit STACK update ask.
echo "Task 11 push: SKIPPED unless Gabe asks"
```

Expected: no remote push occurs.

- [ ] **Step 3: Local checkpoint of the optional note only (no HyperBots push)**

```bash
git add optional/hyperbots-stack-note.md
git commit -m "docs: optional HyperBots STACK note (push gated on Gabe)" || true
```

---

### Task 12: Prep checklist Tue→Wed (Reggie access gates)

**Files:**
- Create: `/home/box/shared/handoffs/reggie-pilot/vista/work/prep/tue-wed-checklist.md`

**Interfaces:**
- Consumes: `questions-for-reggie.md`, decision cut-order signals
- Produces: ordered gate list; fixture remains labelled until each gate clears

- [ ] **Step 1: Write checklist**

```markdown
# Tue → Wed prep checklist (Reggie access gates)

**Present:** Wed Sep 9, 2026 paid trial. **HOW:** recorded factory.

## Gates (block real-feature swap until checked)
- [ ] Source folder link + view perms (Loom, GitHub outline, footage)
- [ ] Brand / style guide + past newsletters + popup examples ETA
- [ ] HubSpot sandbox invite (draft-only confirmed)
- [ ] Barry review surface confirmed (Notion + Drive pack default)
- [ ] Which real feature release is the Wed ingest
- [ ] Loom + outline paths for that release
- [ ] Login animation format (Lottie / MP4 / still) + constraints
- [ ] In-app popup size + placement
- [ ] Channel priority if cut-order goes live
- [ ] Off-limits claims list from Reggie

## Until gates clear
- Keep `fixture_label` non-empty
- Do not invent FEATURE_NAME replacements
- Rehearse recording on fixture

## Cut-order signal (<24h to Wed)
Live if: folder late, voice pack missing, or social video blocking E2E record.
Then: Tom contingency order from `decision.md` — label bonus partial; Gabe yes required to fall back to thin C.

## Day-of Wed
- [ ] Pre-bake recording complete (shot-list.md)
- [ ] Package + honesty doc frozen
- [ ] HubSpot draft optional beat ready or skipped
- [ ] Handoff SOP status: sop-builder after this plan (folder `handoff/` stub exists)
- [ ] No auto-publish, no CIO-as-ESP, no live-wait generation
```

- [ ] **Step 2: Verify gates mention fixture + cut-order**

```bash
f=/home/box/shared/handoffs/reggie-pilot/vista/work/prep/tue-wed-checklist.md
grep -q 'fixture_label' "$f"
grep -q 'cut-order' "$f"
grep -q 'HubSpot sandbox' "$f"
```

- [ ] **Step 3: Run full pytest suite**

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
. .venv/bin/activate
PYTHONPATH=. pytest tests/ -v
```

Expected: all PASS.

- [ ] **Step 4: Local checkpoint (no push)**

```bash
git add prep/tue-wed-checklist.md
git commit -m "docs: Tue-Wed Reggie access gate checklist" || true
```

---

## Self-Review

### 1. Spec coverage

| Spec / lock item | Task(s) |
|---|---|
| Scope B six outputs + full one-release cadence | 5, 6, 7 |
| Recorded factory HOW + shot list §3 | 8 |
| Spine Claims Lock → O1 spot-check → pack approve | 4, 2 |
| Kill-switch / evidence spans / forbidden list | 2, 3 |
| Notion SoT + Barry queue | 4, 9 |
| Six adapters + exist-or-held | 6, 2 |
| Cadence tier blast + UTMs | 5 |
| Package + honesty doc | 7 |
| HubSpot sandbox last draft-only | 10 |
| Trigger leave-behind (Notion default) | 9 |
| Human-gaps table | 7 (`still-needs-human.md`) |
| Handoff SOP via sop-builder later | 1 (`handoff/README.md` stub) — full SOP out of this plan by design |
| Cut-order contingency only | 8, 12 + Global Constraints |
| No inventing claims/pricing | 3, Global Constraints |
| Temporal OUT / CIO ≠ ESP / no auto-publish / writer≠Barry / WIP=1 | Global Constraints + 2, 4, 9, 10 |
| Optional HyperBots STACK | 11 (push gated) |
| Tue→Wed Reggie gates | 12 |
| Design §1–§5 / DESIGN-LOCK | Header + tasks above |

**Gaps (intentional / noted):**
- Full marketer Handoff SOP is deferred to **sop-builder** (design §6 / §10) — only `handoff/README.md` stub in-plan.
- Real Drive/Notion/Gumloop/HubSpot network calls are **not** implemented (leave-behind docs + local package only) — correct for pre-Reggie-access pilot.
- Voice pack encode + real footage burn-in remain human-gaps (honesty doc), not automated cells.
- Matt Notion board retitle is process outside this working tree (design §10.5).
- Fixture `affiliate_rules` / login format / popup placement still await Reggie answers (`questions-for-reggie.md`) — checklist Task 12 gates them; no invented answers.

### 2. Placeholder scan

- No engineer-action `TBD`/`TODO`/`implement later` without concrete content — Reggie-dependent blanks are explicit fixture labels or unchecked checklist boxes.
- Fixture uses `FEATURE_NAME` / `PLACEHOLDER_*` **on purpose** (constraint: no invented Vista facts).
- Task 11 push is explicitly skipped unless Gabe asks (not a vague TODO).

### 3. Type consistency

- `campaign_id` / `id` = `camp_demo_001` across ledger, campaign, cadence, package manifest.
- Artifact `type` enum matches adapter filenames and `REQUIRED_TYPES`.
- `validate_ledger` → `{ok, errors, kill_switch}`; `validate_campaign` → `{ok, errors}`; `validate_cadence_binder` → `{ok, errors}`; `build_package(...) -> Path`.
- Barry seat const `Barry VP Marketing`; `barry.wip` const `1`.
- HubSpot status enum includes `draft_only` / `blocked_no_barry` aligned with checklist.
- Status enum matches architecture state machine; sandbox blocked while `awaiting_barry`.

---

## Execution notes (for parent / implementer)

- Working tree: `/home/box/shared/handoffs/reggie-pilot/vista/work/` — local `git` checkpoints only; **no git push**; **no CloudAgent**; **no CreateAgent**; **do not hire bots**.
- Forge → `gabchess/HyperBots` only if docs land there **and** Gabe asks (Task 11).
- After this plan: invoke **sop-builder** for full handoff SOP; swap fixture when Reggie gates clear.
