# Tixmancer

**Sup, I’m Tix. Your garage sale flipper.**

Tixmancer is a conversational web app for people who hunt for secondhand finds.
Sign in, tell Tix what you want and where you live, then keep the conversation,
search preferences and results with your account.

[tixmancer.xyz](https://tixmancer.xyz) is the canonical product domain. The
server can run it as a restricted preview or as a public waitlist.

## What the preview does

The current codebase includes:

- Google sign-in through Coinbase Developer Platform
- account-owned conversations and saved memory
- a real language-model conversation through Vercel AI Gateway
- installable PWA metadata for **Add to Home Screen** on iPhone and iPad
- stored preview records for searches, listings, connectors and wallet steps
- server-controlled preview access and a consent-based waitlist

The marketplace, notification and wallet tools are interactive simulations.
Their records are scoped to the signed-in account and labeled as simulated in
the product. The preview does not fetch live listings, send messages, accept a
deposit or make a purchase.

## Product flow

1. Open the home page and choose **Talk to Tix**.
2. Sign in with Google.
3. Tell Tix your name, location and what you want to find or sell.
4. Set a price limit or bring a listing.
5. Review the result and decide whether the item is worth chasing.

There is no preloaded buyer story. Tix uses the item, place, currency and limit
from the current account’s conversation.

## Release modes

`TIXMANCER_RELEASE_MODE=preview` shows the recording home and account entry.
Every other value fails closed to the public waitlist. Protected product
routes always require a signed-in account with an active server-side
entitlement, so the recording build stays limited to invited users.

This switch governs the account chat, consumer demo and their account-owned
APIs. The fixture seller and pay-per-score endpoints keep their separate public
x402 contracts. They do not grant access to the private preview.

## Base payment evidence

An earlier Tixmancer rail completed one 5.00 test USDC purchase on Base Sepolia
through the project’s own demo seller. The intent created a watch, the owner
armed a capped and expiring Spend Permission, the scheduler matched it, and the
approved purchase settled over x402.

[View the Base Sepolia transaction](https://sepolia.basescan.org/tx/0x2882e294c057b5d6bc4073e6ccc7e8ce4fe485e53bb4a776936aceb33842844f).

That transaction proves the payment mechanism against the demo seller. It does
not prove a marketplace purchase, third-party seller adoption or demand for the
consumer product. Production disables the inherited payment lab and its buyer
APIs, so the account-chat preview cannot call this payment rail.

## Safety boundary

- Base Sepolia is the only enabled network.
- Tixmancer never stores a user’s private key or seed phrase.
- Live marketplace access requires an official API or partner endpoint.
- A future purchase requires a supported seller plus a user-scoped cap, expiry,
  approval, revocation path and receipt.
- Historical evidence in `docs/evidence/` is immutable.

## Local setup

Requirements: Node.js 24, pnpm and Docker.

```bash
pnpm install --frozen-lockfile
cp .env.example .env.local
docker start tixmancer-test-pg
pnpm dev:consumer
```

Fill the account and model variables described in `.env.example`.
`dev:consumer` resets and migrates the allowlisted local preview database, then
starts the app at `http://127.0.0.1:4318`. Keep a deployed `DATABASE_URL` out of
`.env.local`. The Playwright harness also creates a disposable local database.

After the first Google sign-in, use a second terminal to find the internal
account ID and grant access to the local recording preview:

```bash
pnpm preview:access list
TIX_PREVIEW_USER_ID='paste-internal-user-uuid-here'
pnpm preview:access grant "$TIX_PREVIEW_USER_ID"
```

The command ignores `DATABASE_URL` and defaults to the disposable
`tixmancer_local_preview` database. A remote grant requires both an explicit
admin database URL and a confirmation tied to the same internal user ID:

```bash
TIX_PREVIEW_USER_ID='paste-internal-user-uuid-here'
TIXMANCER_PREVIEW_ADMIN_DATABASE_URL='postgres://...?sslmode=verify-full' \
TIXMANCER_PREVIEW_ADMIN_CONFIRM="grant:$TIX_PREVIEW_USER_ID" \
pnpm preview:access grant "$TIX_PREVIEW_USER_ID"
```

This is an operator command. The app exposes no public entitlement endpoint.

## Verification

```bash
pnpm run typecheck
pnpm run build
pnpm test
pnpm run test:e2e
pnpm run lint
pnpm eval:honesty
pnpm eval:tix-conversation:contracts
```

The model-backed conversation eval is separate because it makes a provider
request:

```bash
AI_GATEWAY_API_KEY=... pnpm eval:tix-conversation:model
```

## Roadmap

The next product slices are account-owned active hunts, listing photo and file
attachments, live supported marketplace sources, user-selected notification
connectors, and an optional permissioned wallet for one supported seller. The
wallet flow will expose quoted, awaiting approval, confirming, settled and
failed states only after each state is enforced by the payment system.

See [PRODUCT.md](./PRODUCT.md) for the product contract,
[docs/how-it-works.md](./docs/how-it-works.md) for the system boundary, and
[docs/grant/2026-09-06-batches-overview.md](./docs/grant/2026-09-06-batches-overview.md)
for the current Base Batches narrative.
