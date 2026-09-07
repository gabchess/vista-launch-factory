# Barry — Claims Lock (once per campaign)

**Campaign:** {{campaign_id}} — {{title}}  
**Seat:** Barry VP Marketing (**writer ≠ Barry**)  
**Surface:** Notion approve card + linked claim ledger (or portable in-chat card)  
**When:** After ingest/retrieve/voice bind; **before** adapter fan-out

## Ledger summary
- Allowed claims: {{allowed_count}} (each with evidence span → transcript/outline/ZIP source)
- Forbidden list present: yes/no
- Kill-switch armed: {{kill_switch.armed}}
- Demo assets used as evidence: **never** (ADR 0001)

## Decision
- [ ] **Approve Claims Lock** — adapters may run (HELD slots still skipped)
- [ ] **Reject / kill-switch** — fix source; adapters stay cold; status → `needs_source_fix`

## Rules
- Every allowed claim must show evidence span from the release folder SoT
- No pricing / limits / roadmap invention
- Slack thumbs ≠ Claims Lock
- Fixture folders (e.g. Quorum Desk mock) must stay labelled fixture — no “as if real Vista” claims
