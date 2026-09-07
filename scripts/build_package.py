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
    p.add_argument(
        "--work-root",
        type=Path,
        default=None,
        help="Repo/work root for resolving adapter paths (default: campaign_json.parents[2])",
    )
    args = p.parse_args(argv)
    root = build_package(args.campaign_json, args.out_dir, work_root=args.work_root)
    print(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
