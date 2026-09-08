"""Check this portable evidence packet through the existing specialist seam.

Run with the repository Python environment. This checks file integrity and
request consistency; editorial judgment, media inspection and human decisions
remain separate recorded work.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


WORKSPACE = Path(__file__).resolve().parent
REPO = WORKSPACE.parents[2]


def read(name):
    return json.loads(data(name).decode("utf-8"))


def data(name):
    path = (WORKSPACE / name).resolve()
    if not path.is_relative_to(WORKSPACE):
        raise ValueError(f"Path outside baseline: {name}")
    return path.read_bytes()


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    index = read("baseline.json")
    manifest = read(index["files"]["sources"])
    ledger = read(index["files"]["claims"])
    approvals = read(index["files"]["approvals"])
    for key, name in index["files"].items():
        if key != "checks":
            data(name)
    for item in index["snapshot_binding"].values():
        check(digest(data(item["path"])) == item["sha256"], f"Changed input: {item['path']}")

    files = manifest["source_files"] + manifest["observations"] + manifest.get("creative_sources", [])
    for item in files:
        blob = data(item["path"])
        check(digest(blob) == item["sha256"], f"Source hash mismatch: {item['id']}")
        if "git_blob_oid" in item:
            git_blob = b"blob " + str(len(blob)).encode() + b"\0" + blob
            check(hashlib.sha1(git_blob).hexdigest() == item["git_blob_oid"], f"Git blob mismatch: {item['id']}")
            check(item["commit"] == index["source_revision"], "Mixed source revision")

    sources = {s["id"]: s for s in manifest["source_files"]}
    observations = {s["id"]: s for s in manifest["observations"]}
    for source in sources.values():
        if source["kind"] == "voice":
            selected = []
            for span in source["origin_spans"]:
                origin = observations[span["origin_id"]]
                text = data(origin["path"]).decode("utf-8")
                check(text[span["start"]:span["end"]] == span["quote"], "Voice origin span mismatch")
                selected.append(span["quote"])
            check(data(source["path"]).decode("utf-8") == "\n\n".join(selected) + "\n", "Changed voice selection")

    eligible = []
    for claim in ledger["claims"]:
        source = sources[claim["source_id"]]
        check(source["kind"] == "fact", "Voice sample used as fact")
        text = data(source["path"]).decode("utf-8")
        check(0 <= claim["start"] < claim["end"] <= len(text), "Invalid character span")
        check(text[claim["start"]:claim["end"]] == claim["quote"], "Claim quote mismatch")
        check(bool(claim["required_qualifier"]), "Missing claim qualifier")
        if claim["use"] == "eligible_for_claims_lock":
            eligible.append(claim["id"])
    held = {c["id"] for c in ledger["held_or_excluded"]}
    check(not set(eligible) & held, "Held claim selected for writer")
    check(index["first_writer"]["eligible_claim_ids"] == eligible, "Writer index differs from ledger")

    lock = approvals["claims_lock"]
    check(lock["status"] == "pending_human_review" and lock["decision"] is None, "This baseline records no Claims Lock decision")
    for binding in [lock["subject"], lock["brief"], lock["voice"]]:
        check(digest(data(binding["file"])) == binding["sha256"], "Claims Lock input binding mismatch")
    check(len(approvals["media"]) == 2, "Expected two preserved creative decisions")
    check(all(m["status"] == "approved_creative" and not m["applies_to_current_writing_claims_lock"] for m in approvals["media"]), "Creative approval scope changed")

    routes = []
    for key, role in [("source_request", "evidence_editor"), ("writer_request", "blog_editor")]:
        name = index["files"][key]
        request = read(name)
        for field in ["product_id", "campaign_id", "source_revision"]:
            check(request[field] == index[field], f"Mismatched {field}")
        check(request["artifacts"] == [], "N01 must not invent an article")
        check([c["id"] for c in request["claims"]] == eligible, "Request includes wrong claims")
        args = ["engine/scripts/specialist_route.py", "route", str((WORKSPACE / name).relative_to(REPO)), "--workspace", str(WORKSPACE.relative_to(REPO))]
        completed = subprocess.run([sys.executable, *args], cwd=REPO, capture_output=True, text=True, check=True)
        projection = json.loads(completed.stdout)
        check(projection["status"] == "ready_for_protocol", "Route held")
        check([s["role"] for s in projection["specialists"]] == [role], "Wrong specialist")
        check(projection["subject"] is None, "N01 has no artifact subject")
        check(projection["generation_authorized"] is False and projection["human_approval_granted"] is False, "Route authority changed")
        routes.append({"command": ".venv/bin/python " + " ".join(args), "exit_code": completed.returncode, "status": projection["status"], "roles": [role], "context_digest": projection["context_digest"], "subject": None, "generation_authorized": False, "human_approval_granted": False})

    check(len(index["five_email_test_audiences"]) == 5, "Expected five email test contexts")
    print(json.dumps({"status": "pass", "scope": "offline evidence integrity and existing source/draft route checks", "source_revision": index["source_revision"], "file_hashes_checked": len(files), "committed_git_blobs_checked": 3, "claim_spans_checked": len(ledger["claims"]), "voice_spans_checked": 5, "eligible_claims": len(eligible), "held_or_excluded_claims": len(held), "routes": routes, "media_file_reinspection": "Separate operator/Forge receipt; this portable check has no media files", "human_approval_granted": False, "provider_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
