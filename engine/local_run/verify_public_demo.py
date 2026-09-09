#!/usr/bin/env python3
"""Verify the public Vista Work package without changing it."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PKG = REPO / "packages" / "camp_vista_work_public_001"
CHECKS = 0


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def media(path: Path) -> dict:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height,pix_fmt", "-of", "json", str(path)], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def main() -> None:
    run = json.loads((PKG / "run.json").read_text())
    require(run["status"] == "review_ready_pending_barry", "run is not pending Barry review")
    require(run["paid_provider_calls"] == 0, "new paid provider call recorded")
    require(run["outputs"] == ["blog", "five_emails", "changelog", "social_video", "login_animation", "in_app_popup", "campaign"], "output list drifted")

    source_manifest = json.loads((PKG / "source-manifest.json").read_text())
    require(len(source_manifest["files"]) == 3, "source capture count")
    for record in source_manifest["files"]:
        path = PKG / record["path"]
        require(path.is_file() and sha(path) == record["sha256"], f"source hash {record['path']}")

    claims = json.loads((PKG / "claims/claim-ledger.json").read_text())
    require(claims["campaign_id"] == "camp_vista_work_public_001", "claim campaign binding")
    require({item["claim_id"] for item in claims["allowed"]} == {"vw1", "vw2", "vw3", "vw4"}, "claims lock drift")
    require(any(item.get("source") == "public_web_capture" and item["claim_id"] == "vw1" for item in claims["evidence"]), "public linked-task evidence")
    require(any(item.get("source") == "public_web_capture" and item["claim_id"] == "vw3" for item in claims["evidence"]), "public source-navigation evidence")

    email_dir = PKG / "artifacts/emails"
    email_files = sorted(email_dir.glob("*.md"))
    require([p.stem for p in email_files] == ["customer_agency", "customer_smb", "lead_agency", "lead_reseller_affiliate", "lead_smb"], "five segment IDs")
    bodies = [p.read_text() for p in email_files]
    require(len(set(bodies)) == 5, "email variants are not distinct")
    require(all("Preheader:" in body for body in bodies), "email preheaders")
    require(len({body.split("\n", 1)[0] for body in bodies}) == 5, "email subjects are not distinct")
    require(all("Still needs human" not in body and "Claims:" not in body and "Affiliate rules" not in body for body in bodies), "internal email notes leaked")
    require(all(("Learn more" in body) if body.startswith("# Keep") or body.startswith("# Give") or body.startswith("# Show") else ("Open Vista Work" in body) for body in bodies), "email CTA")

    social = media(PKG / "artifacts/social/vista-work-social-concept.mp4")
    login = media(PKG / "artifacts/login/vista-work-login-concept.mp4")
    require(social["streams"][0]["codec_name"] == "h264" and social["streams"][0]["width"] == 1080 and social["streams"][0]["height"] == 1920, "social encoding")
    require(float(social["format"]["duration"]) >= 11.9, "social duration")
    require(login["streams"][0]["codec_name"] == "h264" and login["streams"][0]["width"] == 1920 and login["streams"][0]["height"] == 1080, "login encoding")
    require(float(login["format"]["duration"]) >= 7.9, "login duration")
    popup = (PKG / "artifacts/popup/preview.html").read_text()
    require("<dialog" in popup and "showModal" in popup and "Escape" in popup and "vista-work-popup.svg" in popup, "popup interaction preview")

    review = (PKG / "review.html").read_text()
    for required in ("blog.html", "lead_smb.html", "lead_agency.html", "lead_reseller_affiliate.html", "customer_smb.html", "customer_agency.html", "changelog.html", "linkedin.md", "x.md", "threads.md", "tiktok.md", "vista-work-social-concept.mp4", "vista-work-login-concept.mp4", "preview.html", "calendar.csv", "revision-v2.json", "recording-pending.md"):
        require(required in review, f"review link {required}")
    calendar = json.loads((PKG / "campaign/calendar.json").read_text())
    require(calendar["scheduled"] is False and calendar["timezone"] == "America/Sao_Paulo", "campaign scheduling boundary")
    calendar_csv = (PKG / "campaign/calendar.csv").read_text().splitlines()[0]
    require("proposed_day" in calendar_csv and "order" in calendar_csv and "timezone" in calendar_csv, "campaign planning fields")
    require({row["channel"] for row in calendar["rows"]} >= {"blog", "email", "changelog", "linkedin", "x", "threads", "tiktok", "instagram", "login", "in_app"}, "campaign channel coverage")
    for row in calendar["rows"]:
        require(row["asset_id"] in calendar["asset_index"], f"campaign asset {row['asset_id']}")
        require((PKG / calendar["asset_index"][row["asset_id"]]).is_file(), f"campaign path {row['asset_id']}")
    revision = json.loads((PKG / "reviews/revision-v2.json").read_text())
    require(revision["from"] == "v1" and revision["to"] == "v2" and revision["barry_approval"] == "pending", "revision record")
    require(revision["before_sha256"] == sha(PKG / "artifacts/changelog.md") and revision["after_sha256"] == sha(PKG / "artifacts/changelog-v2.md"), "revision hashes")
    costs = json.loads((PKG / "costs/costs.json").read_text())
    require(costs["incremental_paid_calls_this_run"] == 0 and costs["observed_usd_this_run"] == 0, "cost record")
    export = json.loads((PKG / "export-manifest.json").read_text())
    require(export["human_approval"] is False and export["publishing_authorized"] is False, "publish boundary")
    for record in export["files"]:
        path = PKG / record["path"]
        require(path.is_file() and sha(path) == record["sha256"], f"export hash {record['path']}")
    print(json.dumps({"status": "pass", "checks": CHECKS, "package_files": len(export["files"]), "barry_approval": False, "publishing": False, "paid_provider_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
