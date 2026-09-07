# Troubleshooting

## Skill / Augment not active

**Symptom:** Files are on disk but the host does not behave like Launch Factory.  
**Check:** Folder visible ≠ Augment active. Re-run install ([INSTALL-CODEX.md](INSTALL-CODEX.md) / [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md)), reload host, confirm skill name.

## Claude ZIP missing

**Symptom:** No `claude/launch-factory-v0.1.0.zip`.  
**Expected in v0.1.0:** ZIP arrives in A2. Use Codex door or wait for A2. See `claude/README.md`.

## Pack tries to publish or send

**Symptom:** User or model proposes “just publish” / “send the email.”  
**Correct behavior:** Refuse. Barry HITL + authorized tooling required. Re-read TRUST and SKILL Do-not.

## Invented claims or pricing

**Symptom:** Output includes features/prices not in the release folder.  
**Correct behavior:** Strip to Claims Lock; escalate; do not ship. Validate ≤2 then human gap list.

## Expecting all six assets

**Symptom:** Reviewer expects video / login / popup as final.  
**Expected:** Slots 1/5/6 are HOLD stubs — see [HUMAN-GAPS.md](HUMAN-GAPS.md). Package must name the HOLD.

## Engine schemas empty or forked

**Symptom:** `engine/schemas/` missing, or a second schema set under `codex/launch-factory/schemas/` / Claude ZIP.  
**Expected (A3+):** Option B SoT lives under product-root `engine/` (schemas + `engine/scripts/` validators). Codex `schemas/` is a pointer only — do not invent a parallel tree. If `engine/` looks empty, you are on a pre-A3 checkout; pull main / this PR.
