# Engine (Option B — source of truth)

Launch Factory uses **engine placement Option B**: a sibling `engine/` at product root, wrapped by the Augment tree. Codex `schemas/` and the future Claude ZIP are thin copies or pointers — **one** canonical set.

## A1 status — placeholder

This directory is intentionally a placeholder for issue A1 (skeleton). It will wrap / import:

- `vista/work` schemas (e.g. release campaign, claim ledger, cadence binder, artifact schemas);
- validators;
- adapters;
- labelled fixtures (mock release folder);
- scripts for validate / package — **no publish**.

Do not invent a second divergent schema tree under `codex/launch-factory/schemas/` while this SoT is empty. When import lands, update `release-manifest.json` and HOST-MATRIX evidence rows.
