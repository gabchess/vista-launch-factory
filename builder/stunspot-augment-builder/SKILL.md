---
name: stunspot-augment-builder
description: >
  Use when scaffolding or leveling an installable Augment pack to the Stunspot /
  Victor Lane v0.1.3 finished-pack bar — START-HERE envelope, dual-host runtime,
  custody manifests, operate suite, and HITL/claim ceilings aligned across surfaces.
  Bake product topology + claim discipline only. Do not use for Victor deal/domain
  content, pricing, or branding customer packs as Victor/Stunspot.
---

# stunspot-augment-builder

Reusable recipe to scaffold a **customer-shippable Augment pack** from the Victor Lane
v0.1.3 **skeleton** (tree + HITL / claim discipline). The engine (schemas, validators,
adapters, product logic) sits *inside* the envelope — the pack *is* the product.

**Bar source:** Victor Lane v0.1.3 pack topology (`victor-pack-skeleton.md`).
**Not transferable:** Victor deal content, buyer fixtures as customer stories, Victor /
Stunspot brand on Vista or third-party customer materials.

---

## When to use

- Baking a new installable Augment (Claude ZIP + Codex skill) to Victor bar.
- Leveling an existing house pack (e.g. Scout-shaped) up to full envelope + claim lockstep.
- Wrapping an existing engine (`schemas/`, validators, CLI, MCP) so it *feels finished*
  (install → operate → authority → custody), not like a repo you run.

**Do not use** to copy Victor Lane domain prompts, deal rulings, Gideon boundary prose,
Northstar/RelayOps fixtures as customer narrative, or Stunspot branding into customer packs.

---

## Hard rules (read first)

1. **Skeleton + claim discipline only** — copy tree shape and HITL placement; write
   *product-specific* prose for promise, non-goals, first-ask, and authority.
2. **NEVER copy Victor Lane deal content or brand** into customer packs. Demo / sample
   materials must be **renamed** (synthetic product names, not Victor/Northstar/RelayOps
   as if they were the customer’s). Never brand Launch Factory or other Vista packs as
   “Victor Lane” / Stunspot on customer slides.
3. **Scripts = `STRUCTURAL_INTEGRITY_ONLY`** — validate structure, hashes, manifests,
   schema shape, arithmetic guards. Scripts do **not** confer institutional truth, send
   messages, publish, or mutate external systems.
4. **maintainer-source ≠ runtime** — never ship `maintainer-source/` as what the customer
   installs. Runtime = product-root + `codex/<slug>/` + `claude/*.zip`.
5. **Folder visible ≠ Augment active** — HOST-MATRIX must say what is verified vs not;
   fresh-host auto-activation is unverified unless proven.
6. **Claim ceilings aligned** across ≥3 locked surfaces (see HITL six places). Same
   non-goals / no-send / no-auto-publish / named human authority everywhere.
7. **Dual-host behavior parity** — Claude ↔ Codex preserve evidence status, posture,
   action class, invalid actions, exit gate. Identical prose not required.
8. **Do not invent pricing.** Do not block this recipe on unrelated tracks (e.g. A1).

---

## Target tree (must-copy skeleton)

Replace `<product-root>`, `<skill-slug>`, `<Product>`, `vX.Y.Z` per product.

```text
<product-root>/
  START-HERE.md
  README.md
  CHANGELOG.md
  HOST-MATRIX.md
  LICENSE-STATUS.md
  PROVENANCE.md
  release-manifest.json
  documentation-manifest.json
  <Product> T-NOVA vX.Y.Z.txt
  docs/
    INSTALL-CODEX.md
    INSTALL-CLAUDE.md
    DOCUMENTATION-CUSTODY.md
    FIRST-*-READ.md              # product-named first ritual
    OPERATE-*.md
    TRUST-PRIVACY-AND-AUTHORITY.md
    VALIDATION-AND-LIMITS.md
    TROUBLESHOOTING.md
    # recommended operate suite extras (Victor bar polish):
    # EXAMPLE-WALKTHROUGH.md, RECOVERY-AND-EXIT.md, MAINTENANCE.md,
    # ACCESSIBILITY.md, HUMAN-GAPS.md (honesty), PRESENTATION-ASSETS.md
  codex/<skill-slug>/
    SKILL.md
    README.md
    manifest.json
    agents/
    personas/
    knowledge/
      capability-and-authority.md   # REQUIRED
    references/
    schemas/                        # engine option A, or thin copy/pointer
    assets/
    examples/
    evals/
    fallbacks/
    scripts/                        # STRUCTURAL_INTEGRITY_ONLY (+ tests/)
  claude/
    <skill-slug>-vX.Y.Z.zip         # one-root zip; parity with codex skill
  maintainer-source/
    <skill-slug>-vX.Y.Z/skills/<skill-slug>/
                                    # NEVER ship as runtime
  engine/                           # optional engine option B (sibling SoT)
    schemas/ validators/ adapters/ fixtures/ scripts/
```

### Engine placement (pick one SoT)

| Option | Where | Rule |
|---|---|---|
| **A** | `codex/<skill-slug>/schemas/` (+ validators beside scripts) | Matches Victor in-skill schemas; Claude zip vendors the same files. |
| **B** | Sibling `engine/` at product-root | Pack tree wraps it; `codex/.../schemas` and Claude zip are thin copies or pointers — **one** canonical set. |

No third divergent copy of schemas.

---

## HITL / non-goals — six places (aligned)

Every product pack must state the same authority envelope in all six:

1. **`START-HERE.md`** — “What \<Product\> is not”
2. **`codex/<skill-slug>/SKILL.md`** — Trust / Do-not
3. **`knowledge/capability-and-authority.md`** — capability vs authority; named human gate
4. **`docs/TRUST-PRIVACY-AND-AUTHORITY.md`** — privacy, upload policy, who decides
5. **`docs/VALIDATION-AND-LIMITS.md` + `HOST-MATRIX.md`** — what scripts/hosts prove vs not
6. **Skill README claim ceiling / self_check** — ceilings the pack will not cross

Also keep **promise, boundary, install path, first-ask, and claim ceilings** aligned
across root README, CHANGELOG highlights, and any CLAIMS ledger if present.

Minimum lockstep surfaces for ship: **≥3 of** START-HERE, SKILL Trust/Do-not, TRUST doc,
capability-and-authority, VALIDATION — prefer all six.

---

## Step-by-step recipe

### 0. Name the product (not the template)

- Choose `<product-root>`, `<skill-slug>`, display name, version `vX.Y.Z`.
- Write one-sentence **product promise** and one-sentence **first-ask** (memorable
  utterance after install). These are product-owned — do not paste Victor’s.
- Name the **human authority** (e.g. Barry) and the **forbidden actions**
  (no auto-publish, no send, no CRM write without separate tooling + approval).

### 1. Scaffold the envelope

Create the minimal tree above. Stub every required root file and `docs/` operate file
before deep engine work. Envelope before engine polish.

### 2. Write START-HERE (one door)

Structure (topology only — fill with product prose):

1. What the product does (one short block).
2. **Fastest path to value** — choose host → install → first read → first ask.
3. Inputs the user may bring (product-specific; privacy caveat).
4. **What \<Product\> is not** — non-goals / HITL (aligned with the other five places).
5. Links to TRUST and install docs.

Do not bury install behind README archaeology.

### 3. Dual-host packages

- **Codex:** full `codex/<skill-slug>/` tree with SKILL.md, manifest, knowledge,
  schemas/examples/evals/fallbacks, structural scripts.
- **Claude:** `claude/<skill-slug>-vX.Y.Z.zip` with **one root**; behavior parity with
  Codex (same evidence status / posture / invalid actions / exit gate).
- Document both doors in START-HERE and INSTALL-*.

### 4. HOST-MATRIX honesty

Table of capabilities × Codex × Claude × **evidence level**. Explicitly mark:

- Not included (e.g. CRM/email/calendar writes).
- Host-dependent / not freshly host-verified.
- Fresh-host automatic activation: **Not proven** unless you have evidence.

### 5. Custody artifacts

| Artifact | Purpose |
|---|---|
| `PROVENANCE.md` | Where content came from; what is byte-preserved vs authored integration; synthetic demos named as fixtures |
| `LICENSE-STATUS.md` | Separate from LICENSE.md body — status of rights for this release |
| `release-manifest.json` | Product id, version, targets, file list + sha256/bytes |
| `documentation-manifest.json` | Doc set inventory for custody / parity |
| `CHANGELOG.md` | Versioned customer-visible changes |
| T-NOVA one-pager | Product voice/authority card (**product brand**, not Victor) |

### 6. Operate suite

Minimum: INSTALL-CODEX, INSTALL-CLAUDE, FIRST-*-READ, OPERATE-*, TRUST, VALIDATION,
TROUBLESHOOTING, DOCUMENTATION-CUSTODY.

Victor-bar polish: EXAMPLE-WALKTHROUGH, RECOVERY-AND-EXIT, MAINTENANCE, ACCESSIBILITY,
HUMAN-GAPS (honesty), PRESENTATION-ASSETS.

User must be able to **fail and recover** without the maintainer.

### 7. Skill interior (mind, not only CLI)

Under `codex/<skill-slug>/`:

- `knowledge/capability-and-authority.md` (required).
- personas /, agents /, references /, schemas /, examples /, evals /, fallbacks /.
- `scripts/` + `scripts/tests/` marked and implemented as **STRUCTURAL_INTEGRITY_ONLY**.
- Skill README states claim ceiling and points at self_check.

### 8. Align claim ceilings (checklist pass)

Re-read the six HITL places + first-ask + install promise. Diff them. Fix drift so no
surface implies send/publish/autonomy the others forbid.

### 9. Maintainer vs runtime split

- Build and edit under `maintainer-source/` if needed.
- Customer release root must **omit** shipping maintainer-source as the installable
  Augment. Zip/codex trees are the runtime.

### 10. First-ask ritual

Put **one memorable first utterance** on START-HERE (and echo in FIRST-*-READ).
Example pattern only: “Tell me what \<unit of work\> we are actually in.” — rewrite for
the product; do not copy Victor’s deal ask verbatim into unrelated packs.

### 11. Demo / sample materials

- Rename all demo eng Augment ZIPs / fixtures / walkthrough brands.
- Label synthetic cases as **fixtures**, not customer outcomes.
- Never present Victor Lane / Stunspot / Northstar / RelayOps as the customer’s product.

### 12. Release gate

Fill `release-manifest.json` (+ hashes). Confirm documentation-manifest. Run structural
self_check / pack tests only. Confirm HOST-MATRIX and VALIDATION do not overclaim.

---

## Ship checklist (B0 bar)

Use as a gate before calling a pack “Stunspot / Victor-bar”:

- [ ] **START-HERE** — one door; install path; **What X is not**
- [ ] **Dual-host** — `codex/<slug>/` full tree + `claude/<slug>-vX.Y.Z.zip`
- [ ] **HOST-MATRIX** — verified vs not; no implied CRM/email writes
- [ ] **PROVENANCE**
- [ ] **LICENSE-STATUS**
- [ ] **release-manifest.json** (files + hashes)
- [ ] **documentation-manifest.json**
- [ ] **TRUST-PRIVACY-AND-AUTHORITY**
- [ ] **VALIDATION-AND-LIMITS**
- [ ] **knowledge/capability-and-authority.md**
- [ ] **Operate suite** — INSTALL-*, FIRST-*-READ, OPERATE-*, TROUBLESHOOTING (+ recovery recommended)
- [ ] **maintainer-source ≠ runtime**
- [ ] **Claim ceilings aligned across ≥3 surfaces** (prefer all six HITL places)
- [ ] **First-ask ritual** on START-HERE
- [ ] **Scripts = STRUCTURAL_INTEGRITY_ONLY**
- [ ] **No Victor deal/brand leakage**; demos renamed
- [ ] T-NOVA / CHANGELOG / README present and version-aligned

---

## Diff — Scout vs Victor; Prospector = negative

| Element | Victor bar (copy shape) | Scout (nearest house ref) | Prospector |
|---|---|---|---|
| START-HERE + non-goals | Required | Strong — keep pattern | **No** — README only |
| Dual-host release | Codex tree + Claude ZIP | Partial (plugin + codex/ + skills/) | Thin (`.claude/skills/onboard`) |
| HOST-MATRIX | Required | **Missing** | **Missing** |
| PROVENANCE | Required | Soft | Soft |
| LICENSE-STATUS | Required separate | LICENSE.md only | LICENSE.md only |
| release-manifest + hashes | Required | Has RELEASE-MANIFEST + SHA256 | **No** |
| documentation-manifest | Required | **No** | **No** |
| Operate / first-read / recover | Named suite | Partial (SUPPORT, WHAT-BROKE) | **No** |
| TRUST + VALIDATION | Required pair | Partial (DATA-AND-PRIVACY, SECURITY) | Soft gates in README |
| capability-and-authority | Required in knowledge/ | Authz split across files | HITL in README/comments |
| Claim ceilings lockstep | ≥3–6 surfaces | CLAIMS.md strong; close last mile | No CLAIMS table — drift risk |
| Maintainer ≠ runtime | Required | Repo mixes runtime+dev | Repo = app |
| First-ask ritual | On START-HERE | Tool examples after install | `/onboard` then pipeline |
| Feels like Augment | **Yes** | **Close** | **No** — forkable pipeline |

**Nova locks for this builder:**

1. **Strict Victor skeleton** for Launch Factory and future packs (Scout = nearest house
   *reference* only — borrow CLAIMS honesty / install doors; do not stop at Scout file set).
2. **Prospector = negative example only** — do **not** use as Augment shape; excellent
   product narrative tone may be wrapped later, but not this week’s topology.
3. Finished = **install → operate → authority → custody** as products; schemas-green or
   “repo you run” is not Done.

### What Scout still misses (close the last mile)

- Add HOST-MATRIX, PROVENANCE, LICENSE-STATUS (or map LICENSE.md + explicit status).
- Expand toward OPERATE / FIRST-READ / TROUBLESHOOTING / RECOVERY (or rename SUPPORT /
  WHAT-BROKE into that map).
- Clarify fallbacks + maintainer vs runtime layout.
- Keep CLAIMS.md — Victor-equivalent strength; factory packs should carry claim ledger
  *and* customer-facing ceilings in the six HITL places.

### What this builder adds over generic augment-builder / portable-plugin-creator

Envelope discipline, HOST-MATRIX honesty, custody manifests, operate suite, six-place
HITL lockstep, structural-only scripts, maintainer≠runtime — not merely “skill ZIP exists.”

---

## Anti-patterns (refuse)

- Shipping schemas/CLI green as finished Augment.
- HITL only in internal honesty notes — not in START-HERE / SKILL / TRUST.
- Copying Victor deal prompts, rulings, or brand into customer packs.
- Treating Prospector’s app/MCP layout as the pack shape.
- Auto-publish / send / CRM write implied by any surface.
- Shipping `maintainer-source` as the customer install root.
- Scripts that “prove” institutional truth or perform external actions.
- Inventing pricing or commercial outcome claims in the envelope.

---

## Outputs of a successful bake

1. Product-root sticky pack matching the skeleton.
2. Dual-host installables with HOST-MATRIX honesty.
3. Six HITL surfaces aligned; first-ask on START-HERE.
4. Custody: PROVENANCE, LICENSE-STATUS, release-manifest, documentation-manifest.
5. Operate suite sufficient for non-maintainer recovery.
6. Engine (option A or B) wrapped — not naked.
7. No Victor/Stunspot brand or deal-domain leakage; demos renamed.

---

## References (consult, do not paste domain)

- `vista/refs/victor-pack-skeleton.md` — MUST-copy tree + rules
- `vista/refs/victor-lane-v0.1.3/` — structure/examples of envelope (topology only)
- `vista/gaps-past-augments-vs-victor.md` — Scout/Prospector scorecard + Nova locks
- `vista/REFRAME-stunspot-builder.md` — build order (skillify → ship builder → bake LF)
- `vista/architecture-augment.md` — HITL six places + engine placement

Issue: `gabchess/vista-launch-factory#28` (B0).
