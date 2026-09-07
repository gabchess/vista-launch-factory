#!/usr/bin/env python3
# STRUCTURAL_INTEGRITY_ONLY — regenerates release-manifest.json and
# documentation-manifest.json file lists (sha256 + bytes). This script never
# publishes, never alters claim boundaries, and never touches content files.
#
# Inclusion policy (preserved from 0.1.0 manifests):
#   - release-manifest.json: ALL shipped files under launch-factory/
#     (including maintainer-source/README.md, engine/, fixtures, the Claude
#     ZIP, and this script), EXCLUDING .git and BOTH manifest files
#     themselves (self-reference fix, 0.1.1 — circular hashes cannot
#     validate).
#   - documentation-manifest.json: documentation surface only — .md/.txt files
#     under launch-factory/ (including maintainer-source/README.md), EXCLUDING
#     .git, both manifest files, and engine/ internals other than
#     engine/README.md (policy preserved from the 0.1.0 manifest). Non-doc
#     files (json, zip, py, yaml, .gitkeep) are not listed here.
#
# Run from anywhere:  python3 launch-factory/scripts/regen_manifests.py

import hashlib
import json
import os
import sys

PACK_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFESTS = ("release-manifest.json", "documentation-manifest.json")
EXCLUDE_DIRS = {".git"}

EVIDENCE_BOUNDARY = (
    "Proves pack structure, file integrity (sha256/bytes), and documented "
    "Barry HITL gates only. Does not prove live host activation, semantic "
    "output quality, or customer outcomes; slots 1/5/6 are HELD and A7/A8 "
    "remain HOLD. See HOST-MATRIX.md."
)


def walk_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(PACK_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for fn in sorted(filenames):
            if fn == ".DS_Store":
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, PACK_ROOT)
            if rel in MANIFESTS:
                continue  # self-reference fix: manifests never list themselves
            out.append(rel)
    return sorted(out)


def digest(rel):
    with open(os.path.join(PACK_ROOT, rel), "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest(), len(data)


def main():
    files = walk_files()
    doc_files = [
        f for f in files
        if f.endswith((".md", ".txt"))
        and (not f.startswith("engine/") or f == "engine/README.md")
    ]

    rel_path = os.path.join(PACK_ROOT, "release-manifest.json")
    doc_path = os.path.join(PACK_ROOT, "documentation-manifest.json")
    with open(rel_path) as f:
        release = json.load(f)
    with open(doc_path) as f:
        docs = json.load(f)

    release["version"] = "0.1.1"
    release["evidence_boundary"] = EVIDENCE_BOUNDARY
    release["notes"] = (
        "A3 Option B engine + A4 mock-gtm-ship + A5 product-root barry/ HITL "
        "cards (Claims Lock → spot-check → pack approve). engine/barry "
        "templates retained. codex schemas = pointer. 0.1.1: manifests exclude "
        "themselves (self-reference fix); regenerate with "
        "scripts/regen_manifests.py (STRUCTURAL_INTEGRITY_ONLY)."
    )
    release["files"] = [
        {"path": p, "sha256": s, "bytes": b} for p in files for s, b in [digest(p)]
    ]

    docs["version"] = "0.1.1"
    docs["files"] = [
        {"path": p, "sha256": s} for p in doc_files for s, _ in [digest(p)]
    ]

    for path, obj in ((rel_path, release), (doc_path, docs)):
        with open(path, "w") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
            f.write("\n")

    print(
        f"release-manifest.json: {len(release['files'])} files; "
        f"documentation-manifest.json: {len(docs['files'])} files; "
        f"version 0.1.1; manifests self-excluded."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
