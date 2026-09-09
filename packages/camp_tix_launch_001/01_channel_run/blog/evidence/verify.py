#!/usr/bin/env python3
"""Recheck article bindings and local files. This cannot approve the writing."""
from pathlib import Path
import hashlib
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN = ROOT.parents[1]
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
receipt = json.loads((ROOT / "provenance.json").read_text())
metadata = json.loads((ROOT / "metadata.json").read_text())
request = json.loads((ROOT / receipt["request"]["path"]).read_text())
article = (ROOT / "article.md").read_text()
checks = []


def check(name, condition, evidence):
    checks.append({"check": name, "status": "pass" if condition else "fail", "evidence": evidence})


for binding in [receipt["request"], receipt["route"], receipt["drafting_authority"], receipt["claim_ledger"]] + receipt["artifacts"]:
    check("bound_file", digest(ROOT / binding["path"]) == binding["sha256"], binding["path"])
for source in receipt["sources"]:
    check("selected_source_hash", digest(CAMPAIGN / source["path"]) == source["sha256"], source["id"])
for claim in request["claims"]:
    source = next(item for item in request["sources"] if item["id"] == claim["source_id"])
    text = (CAMPAIGN / source["path"]).read_text()
    check("exact_claim_span", text[claim["start"]:claim["end"]] == claim["quote"], claim["id"])
parts = article.strip().split("\n\n")
check("all_blocks_mapped", len(parts) == len(receipt["blocks"]), str(len(parts)))
for part, block in zip(parts, receipt["blocks"]):
    check("block_binding", part == block["text"] and article[block["start_character"]:block["end_character"]] == part and hashlib.sha256(part.encode()).hexdigest() == block["sha256"], block["block_id"])
    check("eligible_claim_ids", set(block["claim_ids"]) <= {item["id"] for item in request["claims"]}, block["block_id"])
for image in receipt["images"]:
    check("image_hash", digest(ROOT / image["path"]) == image["sha256"], image["path"])
    approvals = json.loads((ROOT / image["parent_approval_reference"]).read_text())["media"]
    parent = next(item for item in approvals if item["id"] == image["source_media_id"])
    check("image_parent_approval_binding", parent["sha256"] == image["source_sha256"] and parent["status"] == "approved_creative", image["path"])
for image in [metadata["hero"]] + metadata["inline_images"]:
    header = (ROOT / image["path"]).read_bytes()[:24]
    check("image_dimensions", header[:8] == b"\x89PNG\r\n\x1a\n" and struct.unpack(">II", header[16:24]) == (image["width"], image["height"]), image["path"])
for target in re.findall(r"\]\(([^)]+)\)", article):
    check("article_link", target == "https://tixmancer.xyz/" or (not target.startswith("http") and (ROOT / target).is_file()), target)
check("no_em_dash", "\u2014" not in article, "article.md")
check("metadata_lengths", len(metadata["seo_title"]) == metadata["seo_title_characters"] and len(metadata["meta_description"]) == metadata["meta_description_characters"], "metadata.json")
check("human_review_pending", receipt["approval"]["status"] == "pending" and metadata["approval"]["status"] == "pending", "article and metadata")
check("no_publishing_authority", receipt["publishing_authorized"] is False and metadata["publishing_authorized"] is False and metadata["published_at"] is None, "article and metadata")
html = (ROOT / "article.html").read_text()
check("preview_uses_local_assets", all(f'src="{image["path"]}"' in html for image in receipt["images"]) and "<script" not in html, "article.html")
result = {"schema_version": "article-checks/v1", "artifact_sha256": digest(ROOT / "article.md"), "status": "pass" if all(item["status"] == "pass" for item in checks) else "fail", "checks": checks, "limits": "Local structural evidence. Semantic accuracy, tone and final human approval require review; browser layout and live CTA collection are not tested by this script."}
(ROOT / "evidence/checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"], "checks": len(checks), "artifact_sha256": result["artifact_sha256"]}))
raise SystemExit(0 if result["status"] == "pass" else 1)
