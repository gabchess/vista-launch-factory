# Example 03 — Held-slot honesty (fixture)

**Fixture-only walkthrough** using the Quorum Desk mock GTM ship folder
(`engine/fixtures/mock-gtm-ship/`). Synthetic demo — not a real Vista Social
feature.

## Situation

The fixture run reaches packaging. Slots 2 (blog), 3 (email segments), and
4 (changelog) have real drafts. Slots **1 (social video), 5 (login animation),
6 (in-app popup)** have no real footage, encode track, or design source — the
fixture's `sources/footage_index.json` points at placeholders only.

## What the pack does

1. **HELD-skip, do not fabricate.** Each held slot ships as an explicit HELD
   stub with a hold reason, the same shape as the real spine run output
   (`packages/camp_vista_work_001/*/HELD.txt`):
   - Slot 1 — HELD: no real Loom/UI footage; demo assets must not enter the
     claim ledger (ADR 0001).
   - Slot 5 — HELD: no real login footage/Lottie source; held for claim-safety.
   - Slot 6 — HELD: no real popup graphic/copy source; held for claim-safety.
2. **The honesty doc travels with the package**
   (`engine/honesty/still-needs-human.md` shape): what still needs a human,
   what is held, and why.
3. **The Barry pack-approve card shows the holds** — the slot table lists
   1/5/6 as "HELD-skip," never as approved artifacts.
4. **The package summary says it plainly:** three real drafts + cadence, three
   held slots. Never "all six review-ready."

## Language rules at this step

- Allowed: "slot 1 is HELD pending real footage," "held for claim-safety."
- Forbidden: "coming soon," "in the pipeline," or any roadmap date — those are
  inventions without evidence.
- Forbidden: rendering a placeholder video/animation and calling it a draft.

**Failure shape:** a six-asset package where 1/5/6 contain invented scripts or
mockups presented as review-ready; or a summary that quietly omits the holds.
